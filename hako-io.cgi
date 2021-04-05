#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# 入出力用スクリプト(ver1.00)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# Hakoniwa R.A. ver1.11
# 初期設定用スクリプト(箱庭諸島 ver2.30)
# 使用条件、使用方法等は、read-renas.txtファイルを参照
#
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------

require './hako-const.cgi';
#----------------------------------------------------------------------
# 島データ入出力
#----------------------------------------------------------------------

# 全島データ読みこみ
sub readIslandsFile {
    my ($num) = @_; # 0だと地形読みこまず
                    # -1だと全地形を読む
                    # 番号だとその島の地形だけは読みこむ

    # データファイルを開く
    if (!open(IN, "${HdirName}/$HmainData")) {
        rename("${HdirName}/hakojima.tmp", "${HdirName}/$HmainData");
        return 0 if(!open(IN, "${HdirName}/$HmainData"));
    }

    # 各パラメータの読みこみ
    my $tmp = <IN>;
    chomp($tmp);
    ($HislandTurn, $HplayNow, $HDayEvent,$HSpace_Debris) = split(/,/, $tmp); # ターン数, ゲーム中フラグ, イベントフラグ
    $HislandLastTime= int(<IN>); # 最終更新時間
    return 0 if (!$HislandLastTime);

    # unitTimeの上書き
    if ($HarmisticeTurn && ($HislandTurn < $HarmisticeTurn)) {
        $HarmTime = $HunitTime;
        $HunitTime = $HarmisticeTime;
    }

    $HislandNumber = int(<IN>); # 島の総数
    $islandNumber = $HislandNumber - 1; # 島の総数 - 1
    # 次に割り当てるIDと管理人預かりの島ID
    $tmp = <IN>;
    chomp($tmp);
    ($HislandNextID, @HpreDeleteID) = split(/,/, $tmp);

    # flexTime処理
    $HunitTime = 3600 * $HflexTime[($HislandTurn % ($#HflexTime + 1))] if(INIT_FLEX_TIME_SET);

    $Hmonth = 0;        # 季節処理なし

    # ターン処理判定
    my ($now) = time;
    my ($flag) = 0;   # ターン更新前は0，更新時は1
    my ($tempMode) = $HmainMode;

    if (   ( ($Hdebug && ($HmainMode eq 'Hdebugturn')) || (($now - $HislandLastTime) >= $HunitTime) )
        && ( !$HgameLimitTurn || ($HislandTurn < $HgameLimitTurn) )
        && ( !$HsurvivalTurn || ($HislandNumber != 1) || ($HislandTurn <= $HsurvivalTurn) )
                                                                                            ) {
        $HmainMode = 'turn';
        $num = -1; # 全島読みこむ
        $flag = 1; # 更新フラグを1に
    }

    $HnextTime = $HislandLastTime + $HunitTime;
    if ($flag) {
        $HnextTime += $HunitTime;
    }

    if ((!$HgameLimitTurn || ($HislandTurn + $flag <= $HgameLimitTurn)) && (!$HsurvivalTurn || ($HislandNumber != 1) || ($HislandTurn <= $HsurvivalTurn))) {
        $HleftTime = $HnextTime - $now;
        $HplayNow  = 1;
        $HnextTime = sprintf('%d月 %d日 %d時', (gmtime($HnextTime + $Hjst))[4] + 1, (gmtime($HnextTime + $Hjst))[3,2]);
    }
    else {
        $HplayNow  = 0;
        $HnextTime = ' ';
    }

    # 島の読みこみ
    my ($i);
    $HbfieldNumber = 0;
    foreach $i (0..$islandNumber) {
        $Hislands[$i] = readIsland($num, $i);
        $HidToNumber{$Hislands[$i]->{'id'}} = $i;
        if ( ($Hislands[$i]->{'id'}  > 100) || ($Hislands[$i]->{'BF_Flag'} == $HBF_MONSTER_HOUSE) ) {
            $HbfieldNumber++;
            $Hislands[$i]->{'field'} = 1;
        }
        else {
            foreach (@HpreDeleteID) {
                if ($Hislands[$i]->{'id'} == $_) {
                    $Hislands[$i]->{'predelete'} = 1;
                }
            }
        }
    }

    # No.1
    @HrankingID = split(/,/, <IN>);
    # ファイルを閉じる
    close(IN);

    if (   (!$HplayNow) 
        || ($HitemComplete)
        || ($HsurvivalTurn && ($islandNumber == $HbfieldNumber) && ($HislandTurn > $HsurvivalTurn))
       ) {
        # トップモードに変更
        $HmainMode = ($tempMode ne '') ? $tempMode : 'top';
        $HplayNow  = 0;
        $HnextTime = ' ';
    }

    # 同盟データの読み込み
    readAllyFile() if($HallyUse || $HsurvivalTurn || ($HmainMode eq 'asetup'));
    return 1;
}

# 島ひとつ読みこみ
sub readIsland {
    my ($num, $iNo) = @_;

    my ($chiptemp);
    my ($factoryHT, $weather , $temperature , $weather_old , $weather_chain);
    my ($name, $id, $prize, $absent, $comment, $password, $money, $food,$old_food, $tempfood, $BF_Flag, $hakoteam, $stadiumnum,
        $pop, $area, $farm, $factory, $mountain, $pts, $eis1, $eis2, $eis3, $eis4, $eis5, $eis6, $taiji, $onm,
        $id1, $ownername, @totoyoso, $shutomessage, $monumentnum, $rena, $shrtmp, $shr, $shrturn, $fore, $pika, $hamu, $monta, $tare, $zipro, $leje,
        $monslive, $monslivetype, $hmonslivetype, $tax, $eisei2, $eisei3, $eisei4, $eisei5, $eisei6, $inoraland,
        $missiles, $landscore, $army_resouce, $extstr, @ext);

    my ($ally_turn);
    my (@taiji_list);
    my (@sendmo_kind , @sendmo_id);
    my ($civreq);
    my ($civreq_abs,$civreq_kind,$civreq_num);

    $sendmo_kind[0] = 0;
    $sendmo_id[0] = 0;

    $name = <IN>;               # ■1   # 島の名前
    chomp($name);
    $landscore = 0;
    if ($name =~ s/,(.*)$//g) {
        $landscore = int($1);           # BFスコア
    }
    else {
        $landscore = 0;
    }

    $id = int(<IN>);            # ■2   # ID番号
    $prize = <IN>;              # ■3   # 受賞
    chomp($prize);
    my ($r) = "\r";
    $prize =~ s/$r//g;                  # 受賞
    $absent = <IN>;             # ■4   # 放置ターン数
    chomp($absent);
    $BF_Flag = 0;
    if ($absent =~ s/,(.*)$//g) {
        $BF_Flag = int($1);             # BF_Flag
    }
    else {
        $BF_Flag = 0;
    }
    $absent = $absent;                  # 連続資金繰り数
    $comment = <IN>;            # ■5   # コメント
    chomp($comment);
    $password = <IN>;           # ■6   # 暗号化パスワード
    chomp($password);
    $money = int(<IN>);         # ■7   # 資金
    $tempfood = <IN>;           # ■8
    chomp($tempfood);
    if ($tempfood =~ s/,(.*)$//g) {
        $old_food = int($1);            # 前ターン消費食料
    } else {
        $old_food = 0;                  # 前ターン消費食料
    }
    $food = int($tempfood);             # 食料
    $pop = int(<IN>);           # ■9   # 人口

    my ($tmp,$old_area, $yobi11);
    my ($zoo);
    my ($happy);
    my ($trade_max);
    $tmp = <IN>;                # ■10
    chomp($tmp);
    ($area ,$old_area ,$farm,$happy,$trade_max) = split(/,/, $tmp);

    $area = int($area);                 # 広さ
    $old_area = int($old_area);         # 広さ
    $farm = int($farm);                 # 農場
    $happy = int($happy);               # 幸福度
    $trade_max = int($trade_max);       # 貿易

    $tmp = <IN>;                # ■11
    chomp($tmp);
    @taiji_list = split(/,/, $tmp);

    $chiptemp = <IN>;           # ■12
    chomp($chiptemp);
    ($factory ,$factoryHT ,$yaku_work,$yaku,$inoraland,$weather,$weather_old,$weather_chain,$temperature) = split(/,/, $chiptemp);
    $factory = int($factory);
    $factoryHT = int($factoryHT);
    $yaku_work = int($yaku_work);
    $yaku = int($yaku);
    $inoraland = int($inoraland);
    $weather = int($weather);
    $weather_old = int($weather_old);
    $temperature = int($temperature);
    $weather_chain = int($weather_chain);

    $tmp = <IN>;                # ■13  # 採掘場
    chomp($tmp);
    my ($effect ,$missileDa);
    my ($gomi);
    my ($tha_point);
    my ($tha_diff);
    my ($zoo_Mons_cnt);
    ($mountain ,$effect ,$missileDa,$ally_turn,$gomi,$tha_point,$tha_diff,$zoo_Mons_cnt) = split(/,/, $tmp);
    $mountain = int($mountain);
    $effect = int($effect);
    $missileDa = int($missileDa);
    $ally_turn = int($ally_turn);
    $gomi = int($gomi);
    $pts = int(<IN>);           # ■14  # ポイント
    $eis1 = int(<IN>);          # ■15  # 気象衛星
    $eis1 = ($eis1) ? $eis1 : 0;

    $eis2 = int(<IN>);          # ■16  # 観測衛星
    $eis2 = ($eis2) ? $eis2 : 0;

    $eis3 = int(<IN>);          # ■17  # 迎撃衛星
    $eis3 = ($eis3) ? $eis3 : 0;

    $eis4 = int(<IN>);          # ■18  # 軍事衛星
    $eis4 = ($eis4) ? $eis4 : 0;

    $eis5 = int(<IN>);          # ■19  # 防衛衛星
    $eis5 = ($eis5) ? $eis5 : 0;

    $eis6 = int(<IN>);          # ■20  # イレギュラー
    $eis6 = ($eis6) ? $eis6 : 0;

    $extstr = <IN>;             # ■21  # 拡張領域(未使用の$eis7を流用)
    chomp($extstr);
    @ext = split(/\,/,$extstr);
    $army_resouce = int(<IN>);  # ■22  # 軍事物資(未使用の$eis8を流用)
    $taiji = int(<IN>);         # ■23  # 怪獣退治数
    $onm = <IN>;                # ■24  # オーナー名
    chomp($onm);
    $ownername = $onm;                  # オーナー名(未使用)
    $id1 = $id;                         # ID番号(未使用)

    if (1) {            # メンテしていないので、■■1固定■■
        my $tmp = <IN>; # toto予想(左右)
        chomp($tmp);            # ■25
        @totoyoso = split(/,/, $tmp);

        $shutomessage = <IN>;   # ■26  # 首都名とか
        chomp($shutomessage);
        if ($shutomessage =~ s/,(.*),(.*)$//g) {     # 首都名
            $stadiumnum = $1;                       # スタジアムの数
            $hakoteam = $2;                         # チーム名
        } else {
            $stadiumnum = "zante";                  # スタジアムの数
            $hakoteam = "zansta";                   # チーム名
        }

        $monumentnum = int(<IN>); # ■27    # 記念碑の数
        $rena = int(<IN>); # ■28  # ミサイル基地と海底基地の経験値
        $shrtmp = <IN>; # ■29  # 未使用の'momotan'を「時の神殿」のフラグに流用
        chomp($shrtmp);
        ($shr, $shrturn) = split(/,/, $shrtmp);
        $fore = int(<IN>);      # ■30  # 森林規模
        $pika = int(<IN>);      # ■31  # 増加資金
        $hamu = int(<IN>);      # ■32  # 増加人口
        $monta = int(<IN>);     # ■33  # 増加ポイント

        $tmp = <IN>;            # ■34  # 養鶏所
        chomp($tmp);
        ($tare,$zipro,$leje) = split(/,/, $tmp);
        $tare = int($tare);             # 養鶏所規模
        $zipro = int($zipro);           # 養豚場規模
        $leje = int($leje);             # 牧場規模

        $tmp = <IN>;            # ■35
        chomp($tmp);
        $zoo = $tmp;

        $yobi11 = int(<IN>);    # ■36

    }

    $monslive = int(<IN>);      # ■37  # 怪獣出現数
    $tmp = <IN>;                # ■38  # 怪獣出現種類
    chomp($tmp);
    ($monslivetype, $hmonslivetype) = split(/,/, $tmp);
    $tax = int(<IN>);        # ■39  # 税率
    $eisei2 = int(<IN>);        # ■40  # 通算観光者数
    $eisei3 = int(<IN>);        # ■41  # 未使用
    $eisei4 = <IN>;             # ■42  # サッカーチーム・データ
    chomp($eisei4);
    my ($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $eisei4);
    my ($kachiten) = $stwin * 3 + $stdrow;
    $eisei5 = <IN>;             # ■43  #ペット・データ
    chomp($eisei5);
    $eisei6 = <IN>;             # ■44  #ユニーク地形・データ
    chomp($eisei6);

    $missiles = int(<IN>);      # ■45  # ミサイル発射可能数

    # HidToNameテーブルへ保存
    $HidToName{$id} = $name;

    # 地形
    my (@land, @landValue,@landValue2, @landValue3, $line, @command, @lbbs);
    my (@item_land, @item_landValue, @item_landValue2, @item_landValue3);

    if (($num == -1) || ($num == $id)) {
        if (!open(IIN, "${HdirName}/${id}.${HsubData}")) {
            if (-e "${HdirName}/${id}tmp.${HsubData}") {

                rename("${HdirName}/${id}tmp.${HsubData}", "${HdirName}/${id}.${HsubData}");
            }
            elsif(-e "${HdirName}/${HsubDataold}.${id}") {

                rename("${HdirName}/${HsubDataold}.${id}", "${HdirName}/${id}.${HsubData}");
            }
            if (!open(IIN, "${HdirName}/${id}.${HsubData}")) {
                exit(0);
            }
        }
        my ($x, $y, $i);
        foreach $y (0..$islandSize) {
            $line = <IIN>;
            foreach $x (0..$islandSize) {
                $line =~ s/^(..)(......)(..)(....)(..)//;
                $land[$x][$y] = hex($1);
                $landValue[$x][$y] = hex($2);
                $landValue2[$x][$y] = hex($3);
                $landValue3[$x][$y] = hex($4);
                if ($land[$x][$y] == $HlandShrine && $landValue[$x][$y] > 0 && $shrturn) {
                    $landValue[$x][$y] = $shrturn;
                }
            }
        }

        #持ち物
        $line = <IIN>;
        foreach $x (0..$HItem_MAX) {
            $line =~ s/^(..)(......)(..)(....)(..)//;
            $item_land[$x] = hex($1);
            $item_landValue[$x] = hex($2);
            $item_landValue2[$x] = hex($3);
            $item_landValue3[$x] = hex($4);
        }

        # コマンド
        for ($i = 0; $i < $HcommandMax; $i++) {
            $line = <IIN>;
            $line =~ /^([0-9]*),([0-9]*),([0-9]*),([0-9]*),([0-9]*)$/;
            $command[$i] = {
                'kind' => int($1),
                'target' => int($2),
                'x' => int($3),
                'y' => int($4),
                'arg' => int($5)
            }
        }


        my (@pro_data1);
        {
            my ($readed_line) = 1;
            my ($word) = '';

            while ($word = <IIN>)  {
                chomp($word);
                if ($word eq 'produces') {

                    my ($cnt);
                    my (@read_pro_data);
                    my ($product);
                    $line = <IIN>;
                    chomp($line);
                    @read_pro_data = split(/,/, $line);

                    $cnt = 0;
                    foreach $product (@HProduct_Food_hash_table) {

                        $pro_data{$product} = ($read_pro_data[$cnt]) ? $read_pro_data[$cnt] : 0 ;
                        $cnt++;
                    }
                }


                if ($word eq 'CivReqest') {

                    $line = <IIN>;
                    chomp($line);
                    $civreq = $line;

                    $line = <IIN>;
                    chomp($line);
                    $civreq_abs = $line;
                    $line = <IIN>;
                    chomp($line);
                    ($civreq_kind , $civreq_num) = split(/,/, $line);
                }

                if ($word eq 'lbbs') {

                    $readed_line = 0;
                    # ローカル掲示板
                    for ($i = 0; $i < $HlbbsMax; $i++) {
                        $lbbs[$i] = "0<<0>>";

                        if ($readed_line) {

                            $line = $word;
                            $readed_line = 0;
                        }
                        else {

                            $line = <IIN>;
                        }
                        chomp($line);
                        if (INIT_LBBS_OLD_TO_NEW) {
                            # 掲示板ログの形式を変換する
                            if ($line =~ /^([0-9]*)\>(.*)\>(.*)$/) {
                                # 標準形式ログである
                                $line = "0<<$1>$2>$3";
                            }
                        }
                        $lbbs[$i] = ($line) ? $line : '';
                    }
                }
            }
        }
        close(IIN);
    }

    # 島型にして返す
    return {
        'name' => $name,
        'ownername' => $ownername,
        'id' => $id,
        'id1' => $id1,
        'landscore' => $landscore,
        'prize' => $prize,
        'absent' => $absent,
        'tha_point' => $tha_point,
        'tha_diff' => $tha_diff,
        'zoo_Mons_cnt' => $zoo_Mons_cnt,
        'stadiumnum' => $stadiumnum,
        'yaku_work' => $yaku_work,
        'yaku' => $yaku,
        'inoraland' => $inoraland,
        'hakoteam' => $hakoteam,
        'BF_Flag' => $BF_Flag,
        'comment' => $comment,
        'password' => $password,
        'money' => $money,
        'food' => $food,
        'old_food' => $old_food,
        'pop' => $pop,
        'area' => $area,
        'old_area' => $old_area,
        'happy' => $happy,
        'farm' => $farm,
        'factory' => $factory,
        'factoryHT' => $factoryHT,
        'mountain' => $mountain,
        'pts' => $pts,
        'eis1' => $eis1,
        'eis2' => $eis2,
        'eis3' => $eis3,
        'eis4' => $eis4,
        'eis5' => $eis5,
        'eis6' => $eis6,
        'ext' => \@ext,
        'army' => $army_resouce,
        'taiji' => $taiji,
        'onm' => $onm,
        'monsterlive' => $monslive,
        'monsterlivetype' => $monslivetype,
        'hmonsterlivetype' => $hmonslivetype,
        'eisei1' => $tax,
        'eisei2' => $eisei2,
        'eisei3' => $eisei3,
        'eisei4' => $eisei4,
        'eisei5' => $eisei5,
        'eisei6' => $eisei6,
        'kachiten' => $kachiten,
        'missiles' => $missiles,
        'totoyoso' => \@totoyoso,
        'shutomessage' => $shutomessage,
        'kei' => $monumentnum,
        'rena' => $rena,
        'shr' => $shr,
        'shrturn' => $shrturn,
        'fore' => $fore,
        'pika' => $pika,
        'hamu' => $hamu,
        'monta' => $monta,
        'tare' => $tare,
        'zipro' => $zipro,
        'leje' => $leje,
        'weather' => $weather,
        'weather_old' => $weather_old,
        'weather_chain' => $weather_chain,
        'temperature' => $temperature,
        'effect' => $effect,
        'zoo' => $zoo,
        'ally_turn' => $ally_turn,
        'gomi' => $gomi,
        'missileAlert' => $missileDa,
        'taiji_list' => \@taiji_list,
        'land' => \@land,
        'landValue' => \@landValue,
        'landValue2' => \@landValue2,
        'landValue3' => \@landValue3,
        'item_land' => \@item_land,
        'item_landValue' => \@item_landValue,
        'item_landValue2' => \@item_landValue2,
        'item_landValue3' => \@item_landValue3,
        'command' => \@command,
        'lbbs' => \@lbbs,
        'sendmo_kind' => \@sendmo_kind,
        'sendmo_id' => \@sendmo_id,
        'trade_max' => $trade_max,
        # プロダクト
        'kome' => $pro_data{'kome'},
        'yasai' => $pro_data{'yasai'},
        'kudamono' => $pro_data{'kudamono'},
        'seafood' => $pro_data{'seafood'},
        'sio' => $pro_data{'sio'},
        'toriniku' => $pro_data{'toriniku'},
        'butaniku' => $pro_data{'butaniku'},
        'gyuniku' => $pro_data{'gyuniku'},
        'nazoniku' => $pro_data{'nazoniku'},
        'tamago' => $pro_data{'tamago'},
        # リクエスト
        'civreq' => $civreq,
        'civreq_abs' => $civreq_abs,
        'civreq_kind' => $civreq_kind,
        'civreq_num' => $civreq_num,
    };
}

# 全島データ書き込み
sub writeIslandsFile {
    my($num) = @_;

    # ファイルを開く
    open(OUT, ">${HdirName}/hakojima.tmp");

    # 各パラメータ書き込み
    print OUT "$HislandTurn,$HplayNow,$HDayEvent,$HSpace_Debris\n";
    print OUT "$HislandLastTime\n";
    print OUT "$HislandNumber\n";
    print OUT "$HislandNextID," . join(',', @HpreDeleteID) . "\n";

    # 島の書きこみ
    my ($i);
    foreach $i (0..$islandNumber) {
        writeIsland($Hislands[$i], $num);
    }

    print OUT join(',', @HrankingID);
    # ファイルを閉じる
    close(OUT);

    # 怪獣出現数の書き込み
    if (!$HnewGame) {
        if (open(MIN, ">${HdirName}/monslive.tmp")) {
            foreach $i (0..$islandNumber) {
                print MIN $Hislands[$i]->{'monsterlive'} . "\n";
                print MIN $Hislands[$i]->{'monsterlivetype'} . "," . $Hislands[$i]->{'hmonsterlivetype'} . "\n";
                print MIN $Hislands[$i]->{'eisei1'} . "\n";
                print MIN $Hislands[$i]->{'eisei2'} . "\n";
                print MIN $Hislands[$i]->{'eisei3'} . "\n";
                print MIN $Hislands[$i]->{'eisei4'} . "\n";
                print MIN $Hislands[$i]->{'eisei5'} . "\n";
                print MIN $Hislands[$i]->{'eisei6'} . "\n";
            }
        close(MIN);
        }
    }

    # ミサイル発射可能数の書き込み
    if (!$HnewGameM) {
        if (open(MIN, ">${HdirName}/missiles.tmp")) {
            foreach $i (0..$islandNumber) {
                print MIN $Hislands[$i]->{'missiles'} . "\n";
            }
            close(MIN);
        }
    }

    # 同盟データの書き込み
    writeAllyFile() if($HallyUse || $HarmisticeTurn || ($HmainMode eq 'asetup'));

    # 島の書きこみ
    my ($id);
    foreach $i (0..$islandNumber) {
        $id = $Hislands[$i]->{'id'};
        if (($num <= -1) || ($num == $id)) {
            unlink("${HdirName}/${id}.${HsubData}");
            rename("${HdirName}/${id}tmp.${HsubData}", "${HdirName}/${id}.${HsubData}");
        }
    }

    # 本来の名前にする
    unlink("${HdirName}/$HmainData");
    rename("${HdirName}/hakojima.tmp", "${HdirName}/$HmainData");

    # 怪獣出現数
    if (!$HnewGame) {
        unlink("${HdirName}/monslive.dat");
        rename("${HdirName}/monslive.tmp", "${HdirName}/monslive.dat");
    }
    # ミサイル発射可能数
    if (!$HnewGameM) {
        unlink("${HdirName}/missiles.dat");
        rename("${HdirName}/missiles.tmp", "${HdirName}/missiles.dat");
    }

}


# 島ひとつ書き込み
sub writeIsland {
    my ($island, $num) = @_;

    my ($i);
    my ($taijilist) = '';

    $taijilist .= $island->{'taiji_list'}[0];
    for ($i = 1 ; $i < 5 ; $i++) {

        if (defined $island->{'taiji_list'}[$i]) {
            $taijilist .= "," . $island->{'taiji_list'}[$i];
        }else{
            last;
        }
    }

    my ($landscore);
    $landscore = int($island->{'landscore'});
    print OUT $island->{'name'} . ",$landscore\n";
    print OUT $island->{'id'} . "\n";
    print OUT $island->{'prize'} . "\n";
    print OUT $island->{'absent'} . ",$island->{'BF_Flag'}\n";
    print OUT $island->{'comment'} . "\n";
    print OUT $island->{'password'} . "\n";
    print OUT $island->{'money'} . "\n";
    print OUT $island->{'food'} . ",$island->{'old_food'}\n";
    print OUT $island->{'pop'} . "\n";
    print OUT $island->{'area'} . ',' .$island->{'old_area'}. ',' . $island->{'farm'} . ',' . $island->{'happy'} . ",1\n";
    print OUT "$taijilist\n";
    print OUT $island->{'factory'}.",".$island->{'factoryHT'}.",".$island->{'yaku_work'}.",".$island->{'yaku'}.",".$island->{'inoraland'}.",".$island->{'weather'}.",".$island->{'weather_old'}.",".$island->{'weather_chain'}.",".$island->{'temperature'}."\n";
    print OUT $island->{'mountain'} . "," . $island->{'effect'} .",".$island->{'missileAlert'}."," . $island->{'ally_turn'}.",".$island->{'gomi'}.",".$island->{'tha_point'}.",".$island->{'tha_diff'}.",".$island->{'zoo_Mons_cnt'}."\n";
    print OUT $island->{'pts'} . "\n";
    print OUT $island->{'eis1'} . "\n";
    print OUT $island->{'eis2'} . "\n";
    print OUT $island->{'eis3'} . "\n";
    print OUT $island->{'eis4'} . "\n";
    print OUT $island->{'eis5'} . "\n";
    print OUT $island->{'eis6'} . "\n";
    print OUT join(',', @{$island->{'ext'}}) . "\n";
    print OUT $island->{'army'} . "\n";
    print OUT $island->{'taiji'} . "\n";
    print OUT $island->{'onm'} . "\n";

    # 地形
    my ($id) = $island->{'id'};
    if (($num <= -1) || ($num == $id)) {
        open(IOUT, ">${HdirName}/${id}tmp.${HsubData}");

        my ($land, $landValue,$landValue2,$landValue3);
        $land = $island->{'land'};
        $landValue = $island->{'landValue'};
        $landValue2 = $island->{'landValue2'};
        $landValue3 = $island->{'landValue3'};
        my($x, $y);
        foreach $y (0..$islandSize) {
            foreach $x (0..$islandSize) {
                unless($land->[$x][$y] == $HlandShrine && $landValue->[$x][$y] > 0) {
                    printf IOUT ("%02x%06x%02x%04x%02x", $land->[$x][$y], $landValue->[$x][$y],$landValue2->[$x][$y],$landValue3->[$x][$y],0);
                } else {
                    $island->{'shrturn'} = $landValue->[$x][$y];
                    printf IOUT ("%02x%06x%02x%04x%02x", $land->[$x][$y], 1,$landValue2->[$x][$y],$landValue3->[$x][$y],0);
                }
            }
            print IOUT "\n";
        }

        # 持ち物
        $item_land = $island->{'item_land'};
        $item_landValue = $island->{'item_landValue'};
        $item_landValue2 = $island->{'item_landValue2'};
        foreach $y (0..$HItem_MAX) {
            printf IOUT ("%02x%06x%02x%04x%02x", $item_land->[$y], $item_landValue->[$y],$item_landValue2->[$y],0,0);
        }
        print IOUT "\n";


        # コマンド
        my ($command, $i);
        $command = $island->{'command'};
        for ($i = 0; $i < $HcommandMax; $i++) {
            printf IOUT ("%d,%d,%d,%d,%d\n",
                            $command->[$i]->{'kind'},
                            $command->[$i]->{'target'},
                            $command->[$i]->{'x'},
                            $command->[$i]->{'y'},
                            $command->[$i]->{'arg'}
                        );
        }

        # 食べ物
        print IOUT "produces\n";
        {
            my ($product);
            my ($data);
            $data = '';
            foreach $product (@HProduct_Food_hash_table) {
                $data .= $island->{$product} . ',';
            }
            print IOUT "${data}0\n";
            print IOUT "0\n";
            print IOUT "0\n";
            print IOUT "0\n";
            print IOUT "0\n";
            print IOUT "0\n";
        }

        # ローカル掲示板
        print IOUT "lbbs\n";
        {
            my ($lbbs);
            $lbbs = $island->{'lbbs'};
            for($i = 0; $i < $HlbbsMax; $i++) {
                print IOUT $lbbs->[$i] . "\n";
            }
        }

        # 市民の要望
        print IOUT "CivReqest\n";
        {
            print IOUT "$island->{'civreq'}\n";           # 要望有無
            print IOUT "$island->{'civreq_abs'}\n";           # 放置ターン
            print IOUT "$island->{'civreq'},$island->{'civreq_num'}\n";           # 内容、数値
            print IOUT "0\n";           # 
            print IOUT "0\n";           # 
        }
        close(IOUT);
    }

    if (1) {# メンテしていないので、■■1固定■■
        my ($totoyoso) = $island->{'totoyoso'};
        print OUT join(',', @$totoyoso) . "\n";
        print OUT $island->{'shutomessage'} . ",".$island->{'stadiumnum'}.",".$island->{'hakoteam'}."\n";
        print OUT $island->{'kei'} . "\n";
        print OUT $island->{'rena'} . "\n";
        print OUT $island->{'shr'} . ',' . $island->{'shrturn'} . "\n";
        print OUT $island->{'fore'} . "\n";
        print OUT $island->{'pika'} . "\n";
        print OUT $island->{'hamu'} . "\n";
        print OUT $island->{'monta'} . "\n";
        print OUT $island->{'tare'} . "," . $island->{'zipro'} . "," .$island->{'leje'}."\n";
        print OUT $island->{'zoo'} . "\n";
        print OUT "0\n";
    }
    if (1) {
        print OUT $island->{'monsterlive'} . "\n";
        print OUT $island->{'monsterlivetype'} . "," . $island->{'hmonsterlivetype'} . "\n";
        print OUT $island->{'eisei1'} . "\n";
        print OUT $island->{'eisei2'} . "\n";
        print OUT $island->{'eisei3'} . "\n";
        print OUT $island->{'eisei4'} . "\n";
        print OUT $island->{'eisei5'} . "\n";
        print OUT $island->{'eisei6'} . "\n";
    }
    print OUT $island->{'missiles'} . "\n";
}


#----------------------------------------------------------------------
# 同盟データ入出力
#----------------------------------------------------------------------
# 同盟データ読みこみ
sub readAllyFile {
    # データファイルを開く
    if (!open(IN, "${HdirName}/${HallyData}")) {
        rename("${HdirName}/ally.tmp", "${HdirName}/${HallyData}");
        if (!open(IN, "${HdirName}/${HallyData}")) {
            return 0;
        }
    }

    # 同盟の読みこみ
    my ($i);
    $HallyNumber   = int(<IN>); # 同盟の総数
    for ($i = 0; $i < $HallyNumber; $i++) {
        $Hally[$i] = readAlly();
        $HidToAllyNumber{$Hally[$i]->{'id'}} = $i;
    }
    # 加盟している同盟のIDを格納
    for ($i = 0; $i < $HallyNumber; $i++) {
        my ($member)  = $Hally[$i]->{'memberId'};
        foreach (@$member) {
            my $n = $HidToNumber{$_};
            next unless(defined $n);
            push(@{$Hislands[$n]->{'allyId'}}, $Hally[$i]->{'id'});
        }
    }

    $ally->{'number'} = $HallyNumber;
    # ファイルを閉じる
    close(IN);

    return 1;
}


# 同盟ひとつ読みこみ
sub readAlly {
    my ($name, $mark, $color, $id, $ownerName, $password, $jpass, $score, $number,
        $occupation, $allystr, @allymember, $extstr, @ext, $comment, $title, $message);
    $name = <IN>; # 同盟の名前
    chomp($name);
    $mark = <IN>; # 同盟の識別マーク
    chomp($mark);
    $color = <IN>; # 識別マークの色
    chomp($color);
    $id = int<IN>; # 同盟ID（主催者のものと一緒）
    $ownerName = <IN>; # 主催者の島の名前
    chomp($ownerName);
    $password = <IN>; # パスワード（主催者のものと一緒）
    chomp($password);
    $jpass = <IN>; # パスワード（Takayanのjpass:ターン更新時に書き換え）
    chomp($jpass);
    $score = int(<IN>); # 同盟のスコア
    $number = int(<IN>); # 同盟に属する島の数
    $occupation = int(<IN>); # 占有率
    $allystr = <IN>;
    chomp($allystr);
    @allymember = split(/\,/,$allystr);
    $extstr = <IN>; # 拡張領域
    chomp($extstr);
    @ext = split(/\,/,$extstr);
    # ext[0] 発射したミサイル(unitCountターン分)
    # ext[1] 受けたミサイル(unitCountターン分)
    # ext[2] 収入(unitCountターン分)
    $comment = <IN>;
    chomp($comment);
    $message = <IN>;
    chomp($message);
    ($title, $message) = split('<>', $message);

    # 陣営型にして返す
    return {
        'name' => $name,
        'mark' => $mark,
        'color' => $color,
        'id' => $id,
        'oName' => $ownerName,
        'password' => $password,
        'Takayan' => $jpass,
        'score' => $score,
        'number' => $number,
        'occupation' => $occupation,
        'memberId' => \@allymember,
        'ext' => \@ext,
        'comment' => $comment,
        'title' => $title,
        'message' => $message,
    };
}


# 同盟データ書き込み
sub writeAllyFile {
    # ファイルを開く
    open(OUT, ">${HdirName}/ally.tmp");

    # 陣営データの書きこみ
    print OUT "$HallyNumber\n";
    for ($i = 0; $i < $HallyNumber; $i++) {
        writeAlly($Hally[$i]);
    }
    # ファイルを閉じる
    close(OUT);

    # 本来の名前にする
    unlink("${HdirName}/${HallyData}");
    rename("${HdirName}/ally.tmp", "${HdirName}/${HallyData}");
}


# 同盟ひとつ書き込み
sub writeAlly {
    my ($ally) = @_;

    print OUT $ally->{'name'} . "\n";
    print OUT $ally->{'mark'} . "\n";
    print OUT $ally->{'color'} . "\n";
    print OUT $ally->{'id'} . "\n";
    print OUT $ally->{'oName'} . "\n";
    print OUT $ally->{'password'} . "\n";
    print OUT $ally->{'Takayan'} . "\n";
    print OUT $ally->{'score'} . "\n";
    print OUT $ally->{'number'} . "\n";
    print OUT $ally->{'occupation'} . "\n";
    my $memId = $ally->{'memberId'};
    print OUT join(',', @$memId) . "\n";
    #拡張領域
    my $ext = $ally->{'ext'};
    print OUT join(',', @$ext) . "\n";
    print OUT $ally->{'comment'} . "\n";
    print OUT $ally->{'title'} . '<>' . $ally->{'message'} . "\n";
}


# [a-zA-Z]で構成される8文字のパスワードを作る
sub makeRandomString {

    my ($baseString) = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    my ($baseLen) = length($baseString);
    my ($i, $passward);

    for ($i = 0; $i < 8; $i++) {
        $passward .= substr($baseString, rand($baseLen), 1);
    }

    return $passward;
}


# 同盟の占有率の計算
sub allyOccupy {

    my ($i);
    my ($totalScore) = 0;

    for ($i = 0; $i < $HallyNumber; $i++) {
        $totalScore += $Hally[$i]->{'score'};
    }

    for ($i = 0; $i < $HallyNumber; $i++) {
        if ($totalScore != 0) {
            $Hally[$i]->{'occupation'} = int($Hally[$i]->{'score'} / $totalScore * 100);
        } else {
            $Hally[$i]->{'occupation'} = int(100 / $HallyNumber);
        }
    }

    return;
}

# 島放棄の時の同盟関連処理
sub islandDeadAlly {
    my ($island, $id, $name) = @_;

    $id   = $island->{'id'}   if($id eq '');
    $name = $island->{'name'} if($name eq '');
    my $n = $HidToAllyNumber{$id};
    if (defined $n) {
        if (!$HsurvivalTurn || ($Hally[$i]->{'number'} == 1)) {
            make_pastlog($id, $name);
            $Hally[$n]->{'dead'} = 1;
            $HidToAllyNumber{$id} = undef;
            $HallyNumber--;
            allySort();
        }
    } else {
        make_pastlog($id, $name) if(-f "${HlogdirName}/${id}$Hlogfile_name");
        foreach (@{$island->{'allyId'}}) {
            my $i = $HidToAllyNumber{$_};
            my $allyMember = $Hally[$i]->{'memberId'};
            my @newAllyMember = ();
            foreach (@$allyMember) {
				if(!(defined $HidToNumber{$_})) {
				} elsif($_ == $id) {
					$Hally[$i]->{'score'} -= $island->{'pts'};
					$Hally[$i]->{'number'} -= 1;
				} else {
					push(@newAllyMember, $_);
				}
			}
			$Hally[$i]->{'memberId'} = \@newAllyMember;
		}
	}
}

#----------------------------------------
# 過去ログ処理(YY-BBS)
#----------------------------------------
sub make_pastlog {
	my($id, $name) = @_;
	# ログファイル
	my $logfile = "${HlogdirName}/${id}$Hlogfile_name";
	my $logfileNew = "${HlogdirName}/${id}-${HislandTurn}$Hlogfile_name";
	return if !(-f $logfile);
	rename($logfile, $logfileNew);
	# 盟主ログファイル
	my $logfile2 = "${HlogdirName}/${id}$Hlogfile2_name";
	my $logfile2New = "${HlogdirName}/${id}-${HislandTurn}$Hlogfile2_name";
	return if !(-f $logfile2);
	rename($logfile2, $logfile2New);
	# カウンタファイル
	if($Hcounter) {
		my $cntfile = "${HlogdirName}/${id}$Hcntfile_name";
		my $cntfileNew = "${HlogdirName}/${id}-${HislandTurn}$Hcntfile_name";
		return if !(-f $cntfile);
		rename($cntfile, $cntfileNew);
	}
	# 過去ログ用NOファイル
	if($Hpastkey) {
		my $nofile  = "${HlogdirName}/${id}$Hnofile_name";
		return if !(-f $nofile);
		# 過去NOを開く
		open(NO,"$nofile") || die $!;
		my $count = <NO>;
		close(NO);
		my $nofileNew  = "${HlogdirName}/${id}-${HislandTurn}$Hnofile_name";
		rename($nofile, $nofileNew);
		foreach (1..$count) {
			my $pastfile = sprintf("%s/%04d\.%d\.cgi", $HpastdirName,$_,$id);
			my $pastfileNew = sprintf("%s/%04d\.%d-%d\.cgi", $HpastdirName,$_,$id,$HislandTurn);
			rename($pastfile, $pastfileNew);
		}
	}
	# 消滅した同盟のデータを保存
	my $ally = $Hally[$HidToAllyNumber{$id}];
	my $allyName = "<FONT COLOR=\"$ally->{'color'}\"><B>$ally->{'mark'}</B></FONT>$ally->{'name'}";
	if(!open(IN, "${HlogdirName}/dead${HallyData}")) {
		open(LOG, ">${HlogdirName}/dead${HallyData}") || die $!;
		close(LOG);
		open(IN, "${HlogdirName}/dead${HallyData}") || die $!;
	}
	my @lines = <IN>;
	close(IN);
	unshift(@lines, "${id}-${HislandTurn},$allyName,${name}${AfterName}\n");
	open(OUT, ">${HlogdirName}/dead${HallyData}");
	print OUT @lines;
	close(OUT);
}

# 島名を返す
sub islandName {
    my ($island) = @_;

    my ($name);
    my ($i);
    my ($mark);
    my ($color);
    foreach (@{$island->{'allyId'}}) {
        $i = $HidToAllyNumber{$_};
        $mark  = $Hally[$i]->{'mark'};
        $color = $Hally[$i]->{'color'};
        $name .= '<FONT COLOR="' . $color . '"><B>' . $mark . '</B></FONT>';
    }
    $name .= $island->{'name'} . $AfterName;

    return ($name);
}

#----------------------------------------------------------------------
# パスワードチェック
#----------------------------------------------------------------------
sub checkPassword {

	my($island, $p2) = @_;
	my $p1 = $island->{'password'};

	# nullチェック
	if($p2 eq '') {
		return 0;
	}

	# マスタパスワードチェック
	if(checkMasterPassword($p2)) {
		return 2;
	}

	# 本来のチェック
	if($p1 eq encode($p2)) {
		return 1;
	}

	if($island->{'preab'} && ($HmainMode ne 'preab') && ($HmainMode ne 'change')) {
		my $ally = $Hally[$HidToAllyNumber{$island->{'allyId'}[0]}];
		if($ally->{'Takayan'} eq $p2) {
			return 1;
		}
	}
	return 0;
}

# マスタパスワードのチェック
sub checkMasterPassword {
    my ($pass) = shift;
    return (crypt($pass, 'ma') eq $HmasterPassword);
}

# 特殊パスワードのチェック
sub checkSpecialPassword {
    my ($pass) = shift;
    return (crypt($pass, 'sp') eq $HspecialPassword || crypt($pass, 'ma') eq $HmasterPassword);
}

# パスワードのエンコード
sub encode {
    my ($pass) = shift;
    return ($cryptOn ? crypt($pass, 'h2') : $pass);
}

# パスワード間違い
sub tempWrongPassword {
    axeslog(1, 'PASS error!') if ($HtopAxes && $HtopAxes != 3);
    out(<<END);
<script type="text/javascript">
<!-- $debug_msg
function init(){
}
function SelectList(theForm){
}
//-->
</SCRIPT>
<span class="big">パスワードが違います。</span>
<A HREF=\"$HthisFile\"><span class="big">トップへ戻る</span></A>
END
	if($HpassError) {
		my $agent   = $ENV{'HTTP_USER_AGENT'};
		my $addr    = $ENV{'REMOTE_ADDR'};
		my $host    = $ENV{'REMOTE_HOST'};
		if ($gethostbyaddr && (($host eq '') || ($host eq $addr))) {
			$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2) || $addr;
		} elsif($host eq '') {
			$host = $addr;
		}
		my($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime(time + $Hjst);
		my $day = ('日','月','火','水','木','金','土')[$wday];
		$year = $year + 1900;
		$mon = $mon + 1;
		my $date = sprintf("%04d/%02d/%02d(%s) %02d:%02d:%02d",$year,$mon,$mday,$day,$hour,$min,$sec);
		out(<<END);
<hr>
<table><tr><th><span class="big">【<span class='attention'>！警告！</span>】</span></th></tr>
<TR><TD>あなたの情報を記録させていただきました。
　$date<BR>　<B>$host - $addr - $agent</B>
</TD></TR>
<TR><TD class='N'>
<BR>　<A HREF='http://www.ipa.go.jp/security/ciadr/law199908.html' target='_blank'><B>不正アクセス行為の禁止等に関する法律</B></A>が2001年2月13日に施行されました。
<BR><BR>　この法律は、ハイテク犯罪の防止と高度情報通信社会の健全な発展を目的としたもので、刑法で処罰できない部分を対象とする法律です。
<BR><BR>　刑法では、何らかの被害が出ないと罰することはできなかったのですが、不正アクセス禁止法では、
<span class='attention'>不正アクセスを行った時点で処罰の対象となります。</span>
<BR><BR>　実際の法律を噛み砕いて説明すると、
『<a href='http://www.ipa.go.jp/security/ciadr/law199908.html#不正アクセス行為' target='_blank'><b>不正アクセス</b></a>とは、<b>パスワード等で保護された領域に、権限のないものが勝手にアクセスすること</b>』で、
これに違反した場合、『<span class='attention'>懲役１年以下、又は、５０万円以下の罰金</span>』が科せられることになります。
<BR><BR>　単なる「パスワードの入力ミス」であればよいのですが、あまりにも頻繁であれば、<B>管理者として相応の措置をとらざるを得ません。</B>
<BR><BR>　${HtagTH_}繰り返しパスワードエラーが発生した場合、何か特別な理由があるのでしたら、この下にあるリンクの「掲示板」もしくは「メール」にてご連絡くださいますようお願いいたします。${H_tagTH}
</td></tr></table>
END
    }
}

#----------------------------------------------------------------------
# アクセスログ取得
#----------------------------------------------------------------------
sub axeslog {
    my ($mode, $error) = @_;

    my ($addr) = $ENV{'REMOTE_ADDR'};

    if ( $addr ne "192.168.24.53" ) {
        my $host    = $ENV{'REMOTE_HOST'};
        my @lines;
        my $agent   = $ENV{'HTTP_USER_AGENT'};
        my $referer = $ENV{'HTTP_REFERER'} if(!$mode);

        if (($host eq $addr) || ($host eq '')) {
            $host = gethostbyaddr(pack('C4',split(/\./,$addr)),2) || $addr;
        }

        my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime(time + $Hjst);
        $year = $year + 1900;
        $mon = $mon + 1;
        my ($date) = sprintf("%04d/%02d/%02d %02d:%02d:%02d",$year,$mon,$mday,$hour,$min,$sec);

        open(IN, "$HaxesLogfile");
        @lines = <IN>;
        close(IN);

        my $island_name = $Hislands[$HidToNumber{$HcurrentID}]->{'name'};

        while ($HaxesMax <= @lines) { pop @lines; }
        my ($id);
        if ($mode) {
            $id = ($defaultID eq $HcurrentID) ? $defaultID : "$defaultID=>$HcurrentID";
        }
        else {
            $id = $defaultID;
        }
        my ($pass) = $HinputPassword if(($error =~ /error/) || ($HtopAxes > 4));
        unshift(@lines, "[$date] - $referer - $host - $addr - $agent - $id($rqID) - $island_name - $pass - $error\n");

        if (open(OUT, ">$HaxesLogfile") ){
            foreach $line (@lines) {
                print OUT $line;
            }
            close(OUT);
        }
        else {
            tempProblem();
            return;
        }
    }
}

#----------------------------------------------------------------------
# 入出力
#----------------------------------------------------------------------

# 標準出力への出力
sub out {
#   print STDOUT jcode::sjis($_[0], 'euc'); # jcode使用時
    print STDOUT $_[0];
}

# デバッグログ
sub HdebugOut {
    open(DOUT, ">>debug.log");
    print DOUT ($_[0]);
    close(DOUT);
}

1;
