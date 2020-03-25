#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# ターン進行モジュール(ver1.02)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# Hakoniwa R.A. ver1.11
# メインスクリプト(箱庭諸島 ver2.30)
# 使用条件、使用方法等は、read-renas.txtファイルを参照
#
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# 定数
#----------------------------------------------------------------------
    # 周囲８ヘックスの座標
    @ax = (0,1,1,1,0,-1,0,1,2,2,2,1,0,-1,-1,-2,-1,-1,0,2,2,3,3,3,2,2,1,0,-1,-2,-2,-3,-2,-2,-1,0,1,2,3,3,4,4,4,3,3,2,1,0,-1,-2,-2,-3,-3,-4,-3,-3,-2,-2,-1,0,1,3,3,4,4,5,5,5,4,4,3,3,2,1,0,-1,-2,-3,-3,-4,-4,-5,-4,-4,-3,-3,-2,-1,0,1,2,3,4,4,5,5,6,6,6,5,5,4,4,3,2,1,0,-1,-2,-3,-3,-4,-4,-5,-5,-6,-5,-5,-4,-4,-3,-3,-2,-1,0,1,2,4,4,5,5,6,6,7,7,7,6,6,5,5,4,4,3,2,1,0,-1,-2,-3,-4,-4,-5,-5,-6,-6,-7,-6,-6,-5,-5,-4,-4,-3,-2,-1,0,1,2,3,4,5,5,6,6,7,7,8,8,8,7,7,6,6,5,5,4,3,2,1,0,-1,-2,-3,-4,-4,-5,-5,-6,-6,-7,-7,-8,-7,-7,-6,-6,-5,-5,-4,-4,-3,-2,-1,0,1,2,3);
    @ay = (0,-1,0,1,1,0,-1,-2,-1,0,1,2,2,2,1,0,-1,-2,-2,-3,-2,-1,0,1,2,3,3,3,3,2,1,0,-1,-2,-3,-3,-3,-4,-3,-2,-1,0,1,2,3,4,4,4,4,4,3,2,1,0,-1,-2,-3,-4,-4,-4,-4,-5,-4,-3,-2,-1,0,1,2,3,4,5,5,5,5,5,5,4,3,2,1,0,-1,-2,-3,-4,-5,-5,-5,-5,-5,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,6,6,6,6,6,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-6,-6,-6,-6,-6,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,7,7,7,7,7,7,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-7,-7,-7,-7,-7,-7,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,8,8,8,8,8,8,8,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-8,-8,-8,-8,-8,-8,-8);

    @Htowns = ($HlandTown, $HlandProcity, $HlandMinato,
               $HlandFrocity, $HlandNewtown, $HlandBigtown, $HlandBettown, $HlandUmicity, $HlandOilCity,
               $HlandOnsen, $HlandRizort, $HlandBigRizort, $HlandShuto, $HlandUmishuto,
               $HlandSeatown, $HlandSeacity, $HlandInaka);

    @Htowns_CrimeLine = ($HlandBigtown,$HlandBettown,$HlandUmicity,$HlandOilCity,$HlandShuto, $HlandUmishuto,$HlandSeatown, $HlandSeacity);

    @Hseas = ($HlandSea, $HlandSbase, $HlandSeacity, $HlandSeatown, $HlandIce, $HlandFrocity, $HlandUmishuto, $HlandFune, $HlandUmiamu, $HlandOil, $HlandNursery);

    #----------------------------------------
    # 災害
    #----------------------------------------
    # 収穫、収入倍率(通常を１とした場合に対する比率%)
    # 季節の導入設定はhako-init.cgi
    # 0:季節なし              0, 1月, 2月, 3月, 4月, 5月, 6月, 7月, 8月, 9月,10月,11月,12月
    @Hfood1Incom        = ( 100,  80,  80,  80, 100, 100, 100, 100, 100, 100, 120, 120, 120); # 食料(農業)
    @Hfood2Incom        = ( 100, 100, 100, 100, 100, 100, 100,  80,  80,  80, 120, 120, 120); # 食料(漁業)
    @Hmoney1Incom       = ( 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100); # 資金(工業)
    @Hmoney2Incom       = ( 100, 100,  80, 120, 120, 100,  80, 120, 100, 100, 100, 100, 120); # 資金(商業)
    # 食料消費量(通常を１とした場合に対する比率%)
    @HeatenFoodS        = ( 100,  90,  90,  90, 100, 100, 100,  90,  80,  90, 150, 150, 150);

    # 通常災害発生率(確率は0.1%単位)
    # 0:季節なし        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12月
    @HdisEarthquake = ( 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5); # 地震
    @HdisTsunami    = ( 5,15, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5); # 津波
    @HdisTyphoon    = ( 6, 1, 1, 1, 2, 3, 5, 7, 8, 9, 9, 5, 2); # 台風
    @HdisMeteo      = ( 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6); # 隕石
    @HdisHugeMeteo  = ( 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1); # 巨大隕石
    @HdisEruption   = ( 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5); # 噴火
    @HdisFire       = ( 5, 9, 9, 8, 7, 5, 3, 2, 1, 1, 1, 2, 5); # 火災
    $HdisMaizo      = 15 ; # 埋蔵金

    # 地盤沈下
    $HdisFallBorder = 250; # 安全限界の広さ(Hex数)
    @HdisFalldown   = (15,15,15,15,15,15,15,15,15,15,15,15,15); # その広さを超えた場合の確率


#----------------------------------------------------------------------
# include
#----------------------------------------------------------------------
require ('./hako-turn_log.cgi');     # ログ出力ファイル
require ('./hako-turn_monster.cgi'); # スパゲッティ 怪獣処理を引っ越してゆく
require ('./hako-turn_food.cgi');
require ('./hako-turn_land.cgi');
require ('./hako-trade.cgi');

#use strict;
#use warnings;
use LWP::Simple;

#----------------------------------------------------------------------
# static
#----------------------------------------------------------------------
my ($HnoDisFlag);
my ($HflagKai);           # スタジアム
my ($InoraParkEvent) = 0;
my ($Hyosengameend) = 0;

my ($Appearance_monster) = "none";


my (@order);
#----------------------------------------------------------------------


#----------------------------------------------------------------------
# ターン進行モード
#----------------------------------------------------------------------
# メイン
sub turnMain {
    # 順番決め
    my (@line,$sepTurn);
    $HsepTurnFlag = 0;
    $InoraParkEvent = 0;            #いのらランドのイベント
    $sepTurn = $HsepTurn;
    $HDayEvent_Edge = 0;

    $Appearance_monster = "none";

    if (!$HsepTurn || $HsepTurn >= $HislandNumber) {

        @order = randomArray($HislandNumber);
        $sepTurn = $HislandNumber;
    }
    else {

        $HsepTurnFlag = 1;
        unless (-e "${HdirName}/septurn.cgi") {

            @order = randomArray($HislandNumber);
            if (!open(SOUT, ">${HdirName}/septurn.cgi")) {

                unlock();
                tempProblem();
                exit(0);
            }

            my ($c) = 0;
            foreach (@order) {
                $c++;
                print SOUT $_;
                if (   ($c % $HsepTurn == 0)
                    || ($c == $HislandNumber)  ) {
                    print SOUT "\n";
                }
                else {
                    print SOUT ",";
                }
            }
            close(SOUT);
        }

        if (!open(IN, "${HdirName}/septurn.cgi")) {
            unlock();
            tempProblem();
            exit(0);
        }

        @line = <IN>;
        close(IN);
        if ($line[0] ne '') {

            chomp($line[0]);
            @order = split(',', $line[0]);
            close(IN);
            $rest = $#order + 1;
            $sepTurn = $rest if($HsepTurn > $rest);
            if (!open(SOUT, ">${HdirName}/septurn.cgi")) {

                unlock();
                tempProblem();
                exit(0);
            }
            shift(@line);
            print SOUT join('', @line);
            close(SOUT);
        }
        else {
            unlink("${HdirName}/septurn.cgi");
            $HsepTurnFlag = 0;
            $sepTurn = 0;
        }
    }

    $HislandLastTime += $HunitTime;    # 最終更新時間を更新

    $HislandTurn++;             # ターン番号

    my ($i, $j);

    # 座標配列を作る
    makeRandomPointArray();

    # Hakoniwa Cupログ
    unlink("${HdirName}/hakojima.lhc") if ((-e "${HdirName}/hakojima.lhc") && !($HislandTurn % 100));

    CalcNoDisFlag();        #  災害有無設定

    # 収入、消費フェイズ
    for ($i = 0; $i < $sepTurn; $i++) {

        # ターン開始前のポイント、資金、人口をメモる
        $Hislands[$order[$i]]->{'oldPts'}   = $Hislands[$order[$i]]->{'pts'};
        $Hislands[$order[$i]]->{'oldMoney'} = $Hislands[$order[$i]]->{'money'};
        $Hislands[$order[$i]]->{'lastFood'} = $Hislands[$order[$i]]->{'food'};
        $Hislands[$order[$i]]->{'oldPop'}   = $Hislands[$order[$i]]->{'pop'};
        $Hislands[$order[$i]]->{'lastarea'} = $Hislands[$order[$i]]->{'area'};
        $Hislands[$order[$i]]->{'missileAlert'} = 0;    # ここでミサイルの履歴を削除する

        # 各種の値を計算
        estimate($order[$i]);
        next if ($Hislands[$order[$i]]->{'predelete'});

        income($Hislands[$order[$i]]); # 収入フェイズ
        $Hislands[$order[$i]]->{'ally_turn'}++ if ($Hislands[$order[$i]]->{'ally_turn'} < 50);
    }

    # 記念日イベント
    DayEvent();

    # コマンド処理
    my ($island);
    for ($i = 0; $i < $sepTurn; $i++) {

        $island = $Hislands[$order[$i]];
        $island->{'missiled'} = 0;
        next if ($island->{'predelete'});
        # 戻り値1になるまで繰り返し
        while (!doCommand($island)){};
        # 整地ログ(まとめてログ出力)
        logMatome($island, $HlogOmit2, 'seichi') if ($HlogOmit2);
        logHikkosi_miss( $island->{'id'} , islandName($island)) if ($island->{'stockflag'} == 55);
    }

    TradeEvent();

    # 成長および単ヘックス災害
    for ($i = 0; $i < $sepTurn; $i++) {

        HakoCup_TeamReset($Hislands[$order[$i]]);
        next if($Hislands[$order[$i]]->{'predelete'});  #あずかりの島は飛ばす
        $HflagKai = 0;
        doEachHex($Hislands[$order[$i]]);
    }

    # 参加島への制裁内容を読み込む
    readPunishData();

    my ($remainCampNumber);
    if ($HarmisticeTurn) {
        # 陣営消滅判定
        $remainCampNumber = $HallyNumber;
        if ($HcampDeleteRule) {

            my ($threshold) = 100 / $HallyNumber / 2;
            for ($i=0; $i<$HallyNumber; $i++) {
                if ($Hally[$i]->{'occupation'} < $threshold) {
                    islandDeadAlly('', $Hally[$i]->{'id'}, $Hally[$i]->{'name'});
                    foreach (@{$Hally[$i]->{'memberId'}}){
                        $Hislands[$HidToNumber{$_}]->{'dead'} = 1;
                    }
                    $remainCampNumber--;
                    logCampDelete($Hally[$i]->{'name'});
                }
            }
        }
    }

    # 島全体処理 災害系
    for ($i = 0; $i < $sepTurn; $i++) {

        $island = $Hislands[$order[$i]];
        next if ($island->{'predelete'});
        doIslandProcess($order[$i], $island);
        if (   ($island->{'id'} <= 100)
            && ( !$island->{'BF_Flag'} )
                                         ) {
            doIslandunemployed($order[$i], $island) ;
        }
    }

    if (!$HsepTurnFlag) {
        my ($remainNumber) = $HislandNumber;
        @order = randomArray($HislandNumber) if ($HsepTurn);
        # 賞関係と増加率処理
        foreach $i (0..$islandNumber) {
            $island = $Hislands[$order[$i]];
            doPrize($order[$i], $island) if (!$HsepTurn || $HsepTurn > $islandNumber);

            # 死滅判定
            if ($island->{'dead'}) {

                $island->{'pop'} = 0;
                $island->{'pts'} = 0;
                $island->{'field'} = 0;
                $remainNumber--;

            } elsif(   ($island->{'pop'} == 0)
                    && ($island->{'id'} <= 100)
                    && ( !$island->{'BF_Flag'} ) ) {

                OutAlly($island);
                $island->{'dead'} = 1;
                $island->{'pts'} = 0;
                $remainNumber--;
                # 死滅メッセージ
                my ($tmpid) = $island->{'id'};
                $HidToNumber{$tmpid} = undef;
                logDead($tmpid, islandName($island));
                unlink("${HdirName}/${tmpid}.${HsubData}");
                unlink("${HdirName}/savedata.$tmpid") if (-e "${HdirName}/savedata.$tmpid");
            }
            else {

                $island->{'dead'} = 0;
            }
        }

        # Ranking記録
        makeRankingData();

        # 箱庭カップ
        if ( ($HislandTurn % 100) == 41) {
            my ($stsin) = '';
            my @HCislands = @Hislands;
            my @idx = (0..$#Hislands);
            @idx = sort { $Hislands[$a]->{'field'} <=> $Hislands[$b]->{'field'} ||
                          $Hislands[$a]->{'hcover'} <=> $Hislands[$b]->{'hcover'} ||
                          $Hislands[$b]->{'hcdata'}[3] <=> $Hislands[$a]->{'hcdata'}[3] ||
                          $Hislands[$b]->{'hcdata'}[4] <=> $Hislands[$a]->{'hcdata'}[4] ||
                          $Hislands[$a]->{'hcdata'}[5] <=> $Hislands[$b]->{'hcdata'}[5] ||
                          $Hislands[$b]->{'hcdata'}[6] <=> $Hislands[$a]->{'hcdata'}[6] ||
                          $Hislands[$b]->{'hcdata'}[7] <=> $Hislands[$a]->{'hcdata'}[7] ||
                          $Hislands[$a]->{'hcdata'}[8] <=> $Hislands[$b]->{'hcdata'}[8] ||
                          $a <=> $b } @idx;
            @HCislands = @HCislands[@idx];

            for ($i = 0; $i < 8; $i++) {
                my ($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $HCislands[$i]->{'eisei4'});
                if ($stshoka != 0) {
                    $stshoka = 6;
                    $HCislands[$i]->{'eisei4'} = "$sto,$std,$stk,$stwin,$stdrow,$stlose,$stwint,$stdrowt,$stloset,$styusho,$stshoka";
                    $stsin .= islandName($HCislands[$i]) . "、";
                }
            }
            logHCsin($id, $name, $stsin) if ($stsin ne '');
        }

        # ポイント順にソート
        islandSort('pts', 1);

        # 歴代最多人口記録処理
        islandReki();

        # ターン杯対象ターンだったら、その処理
        if (   !($HislandTurn % $HturnPrizeUnit)
            || (zorome($HislandTurn) ) ) {

            my ($island) = $Hislands[$HbfieldNumber];
            my ($value, $str);

            $value = $HislandTurn + random(1001);
            $island->{'money'} += $value;
            logPrizet($island->{'id'}, islandName($island), "$HislandTurn${Hprize[0]}", "$value$HunitMoney");

            # 神殿のお祭り
            Sinden_Omaturi($island , $HislandTurn , 1001);

            # 神社のお祭り
            Jinja_Omaturi($island , $HislandTurn , 1001);

            my ($prize1, $prize2) = split(/\t/, $island->{'prize'});
            $prize1 .= "${HislandTurn},";
            $island->{'prize'} = "$prize1\t$prize2";
        }

        # 島数カット
        $HislandNumber = $remainNumber;
        $islandNumber = $remainNumber - 1;

        if ($HallyNumber) { # 同盟関連処理

            # 陣営カット(消滅ルール)
            $HallyNumber = $remainCampNumber if ($HarmisticeTurn);
            for ($i = 0; $i < $HallyNumber; $i++) {

                $Hally[$i]->{'score'} = 0;
                # 維持費(いなくなった島があってもいた時の頭割りで処理)
                my ($keepCost) = int($HcostKeepAlly / $Hally[$i]->{'number'}) if($Hally[$i]->{'number'});
                $Hally[$i]->{'number'} = 0;
                my ($allyMember) = $Hally[$i]->{'memberId'};
                foreach (@$allyMember) {

                    my ($no) = $HidToNumber{$_};
                    if (defined $no) {

                        $Hally[$i]->{'score'} += $Hislands[$no]->{'pts'};
                        $Hally[$i]->{'number'}++;
                        # 維持費徴収
                        $Hislands[$no]->{'money'} -= $keepCost  if(!$HarmisticeTurn);;
                        $Hislands[$no]->{'money'} = 0 if($Hislands[$no]->{'money'} < 0);
                        # 貢献度(人口なら1万人につき1ポイント)
                        $Hislands[$no]->{'ext'}[1] += int($island->{'pop'}/10);
                    }
                }
                $Hally[$i]->{'Takayan'} = makeRandomString();
            }
            allyOccupy();
            allySort();
        }

        # 終了条件の判定
        GameOver_wrap();

        # Hakoniwa Cup開催ログ
        logHC($id, $name, $Hstsanka) if (!($HislandTurn % 100) && $Hstsanka);

        # BF得点
        if ( !($HislandTurn % 100) ) {
            my ($i);
            my ($max_point) = -1;
            my ($land_id) = -1;

            # 島全体処理
            for ($i = 0; $i < $sepTurn; $i++) {
                $island = $Hislands[$order[$i]];
                $island->{'tha_point'} = $island->{'pts'};      # 100くぎり

                if ($island->{'predelete'}) {
                    $island->{'landscore'} = 0;
                    next;
                }
                if ( $island->{'landscore'} ) {

                    if (   ($max_point == -1)                       # 初回
                        || ($max_point < $island->{'landscore'} )   # 得点高い
                        || (   ($max_point < $island->{'landscore'} )  
                            && ($Hislands[$order[$land_id]]->{'pts'} > $island->{'pts'} ) ) ) {

                        $max_point = $island->{'landscore'};
                        $land_id = $island->{'id'};
                    }

                    $island->{'money'} += ($island->{'landscore'} * $HBF_Point_Value);
                    logBF_SCORE($island->{'id'}, islandName($island) , $island->{'landscore'});
                    $island->{'landscore'} = 0 ;
                }
            }

            my ($presentID) = $land_id;
            ItemPresent($Hislands[$HidToNumber{$presentID}] , $HlandOmamori , 84);
        }

        # 島全体処理
        for ($i = 0; $i < $sepTurn; $i++) {
            my ($max_point) = -1;
            my ($land_id) = -1;

            $island = $Hislands[$order[$i]];
            next if($island->{'predelete'});

            if ( $island->{'landscore'} ) {

                if (   ($max_point == -1 )                      # 初回
                    || ($max_point < $island->{'landscore'} )   # 得点高い
                    || (   ($max_point < $island->{'landscore'} )  
                        && ( $Hislands[$order[$land_id]]->{'pts'} > $island->{'pts'} ) ) ) {
                    $max_point = $island->{'landscore'};
                    $land_id = $island->{'id'};
                }
            }
        }

        # 島全体処理 食料チェック
        for ($i = 0; $i < $sepTurn; $i++) {

            $island = $Hislands[$order[$i]];
            next if($island->{'predelete'});
            weather_calc($island);
            food_product_check($island);
        }


        CivReqestEvent();

        # スペースデブリ 自然消滅
        CalcSpaceDebri();

        # ----------------------------------------------------------------------
        # バックアップターンであれば、書く前にrename
        if (!($HislandTurn % $HbackupTurn)) {

            my ($i);
            my ($tmp) = $HbackupTimes - 1;
            myrmtree("${HdirName}.bak$tmp");
            for ($i = $tmp; $i > 0; $i--) {

                my ($j) = $i - 1;
                rename("${HdirName}.bak$j", "${HdirName}.bak$i");
            }
            rename("${HdirName}", "${HdirName}.bak0");
            mkdir("${HdirName}", $HdirMode);

            # ログファイルをコピー
            for ($i = 0; $i <= $HlogMax; $i++) {

                copy("${HdirName}.bak0/hakojima.log$i", "${HdirName}/hakojima.log$i") if(-e "${HdirName}.bak0/hakojima.log$i");
            }
            copy("${HdirName}.bak0/hakojima.his", "${HdirName}/hakojima.his") if(-e "${HdirName}.bak0/hakojima.his");
            copy("${HdirName}.bak0/hakojima.lhc", "${HdirName}/hakojima.lhc") if(-e "${HdirName}.bak0/hakojima.lhc");
            copy("${HdirName}.bak0/rekidai.dat", "${HdirName}/rekidai.dat") if(-e "${HdirName}.bak0/rekidai.dat");
            copy("${HdirName}.bak0/$HtradeFile", "${HdirName}/$HtradeFile") if(-e "${HdirName}.bak0/$HtradeFile");

            # savedata(時の記憶)があればコピー
            # ALLYチャット
            foreach $i (0..$islandNumber) {

                my ($island) = $Hislands[$i];
                copy("${HdirName}.bak0/savedata.$island->{'id'}", "${HdirName}/savedata.$island->{'id'}") if(-e "${HdirName}.bak0/savedata.$island->{'id'}");
                copy("${HdirName}.bak0/${HallychatDataName}$island->{'id'}.cht", "${HdirName}/${HallychatDataName}$island->{'id'}.cht") if(-e "${HdirName}.bak0/${HallychatDataName}$island->{'id'}.cht");
            }

            if ($HsepTurn) {
                rename("${HdirName}.bak0/secret.tmp", "${HdirName}/secret.tmp");
                rename("${HdirName}.bak0/late.tmp", "${HdirName}/late.tmp");
                rename("${HdirName}.bak0/log.tmp", "${HdirName}/log.tmp");
            }
        }

        # ファイルに書き出し
        writeIslandsFile(-1);

        # ログファイルを後ろにずらす
        LogFileSlide();

        PerformanceLog();   #    負荷計測

        if (   ($HsepTurn)
            && ($HsepTurn < $HislandNumber) ) {

            my (@tmpSecretLogPool, @tmpLateLogPool, @tmpLogPool);

            open(LIN, "${HdirName}/secret.tmp");
            @tmpSecretLogPool = <LIN>;
            chomp(@tmpSecretLogPool);
            close(LIN);
            unlink("${HdirName}/secret.tmp");

            open(LIN, "${HdirName}/late.tmp");
            @tmpLateLogPool = <LIN>;
            chomp(@tmpLateLogPool);
            close(LIN);
            unlink("${HdirName}/late.tmp");

            open(LIN, "${HdirName}/log.tmp");
            @tmpLogPool = <LIN>;
            chomp(@tmpLogPool);
            close(LIN);
            unlink("${HdirName}/log.tmp");

            @HsecretLogPool = (@tmpSecretLogPool, @HsecretLogPool);
            @HlateLogPool = (@tmpLateLogPool, @HlateLogPool);
            @HlogPool = (@tmpLogPool, @HlogPool);
        }

        logFlush();             # ログ書き出し
        logHistoryTrim();       # 記録ログ調整
#       logHcupTrim();# ※戦績表示のためカット
        MakeHtmlLog();

        # トップへ
        require('./hako-top.cgi');
        topPageMain();
    }
    else {

        for ($i = 0; $i < $sepTurn; $i++) {
            $island = $Hislands[$order[$i]];
            doPrize($order[$i], $island);

            # 死滅判定
            if ($island->{'dead'}) {
                $island->{'pop'} = 0;
                $island->{'pts'} = 0;
                $island->{'field'} = 0;
            }
        }
        # 最終更新時間を更新
        $HislandLastTime -= $HunitTime;
        # ターン番号
        $HislandTurn--;
        # ファイルに書き出し
        writeIslandsFile(-1);

        PerformanceLog();       #    負荷計測

        # tmpログ書き出し
        tempLogFlush();
        MakeHtmlLog();

        {
            my ($all) = $HislandNumber / $HsepTurn + 1;
            $all = ($all == int($all)) ? $all : int($all) + 1;
            my ($count) = $all - $#line - 2;
            tempRefresh($Hrefresh, "ターン更新中(${count}/${all})<BR>そのまましばらくお待ちください");
        }
    }

    {
        if (!(DEBUG_MODE)) {
            my ($url) = 'http://localhost:8123/hako/hakoniwa_bot.php?turn=';
            if ($Appearance_monster eq "none") {
                $url = "$url$HislandTurn&monster=-1";

            }
            else {
                $url = "$url$HislandTurn&monster=$Appearance_monster";

            }
            # LWP::Simpleの「get」関数を使用

            my ($html) = get("$url") or die "";
        }
    }
}



#----------------------------------------------------------------------
#
#   島民の要求
#

sub CivReqestEvent {

    my ($i);
    my ($island);
    my ($id);

    # 島全体処理
    for ($i = 0; $i < $HislandNumber; $i++) {

        $island = $Hislands[$order[$i]];
        next if($island->{'predelete'});

        $id = $island->{'id'};

        if ($island->{'civreq'}) {

            $island->{'civreq_abs'}++;

            if ($island->{'civreq_abs'} > 8) {
                $island->{'civreq'} = 0;
                $island->{'civreq_abs'} = 0;
                logOut("debug:島民は、要望が受け入れられなかったとして悲しんでいますが、デバッグ中だったことに気づいて笑ってしまっています。" , $id);
            }
        }
        else {

            $island->{'civreq_abs'} = 0;
            if (random(100) < 10){ 

                my ($req) = random($CivReqNum-1)+1;
                $island->{'civreq'} = $req;

                if ($CivReqkind[($req)] eq 'tax') {

                    $island->{'civreq_num'} = random(9);
                }
                else {
                    $island->{'civreq_num'} = random(20) + 10;
                }

                my ($unit) = $CivReqDispUnit[$req];
                logOut("debug:島民が要望を出しました。:$CivReqDisp[$req] $island->{'civreq_num'}$CivReqDispUnit[$req]" , $id);
            }
        }

    }
}


#----------------------------------------------------------------------
#
#   ランキングデータ
#

sub makeRankingData {

    my ($i);

    # Ranking記録
    @HrankingID = ();
    foreach $i (0..$islandNumber) {

        my @hcdata = split(/,/, $Hislands[$i]->{'eisei4'});
        $Hislands[$i]->{'hcdata'} = \@hcdata;
        if ($hcdata[10] >= 10) {
            $Hislands[$i]->{'hcover'} = 1;
        }

        $Hislands[$i]->{'kachiten'} = $hcdata[3]*3 + $hcdata[4];
        $Hislands[$i]->{'kachitent'} = $hcdata[6]*3 + $hcdata[7];
        my ($siaisu) = $hcdata[6] + $hcdata[7] + $hcdata[8];
        $siaisu = 1 if($siaisu == 0);
        $Hislands[$i]->{'shoritu'} = int($hcdata[6] / $siaisu * 100);
        $Hislands[$i]->{'teamforce'} = $hcdata[0] + $hcdata[1] + $hcdata[2];
        $Hislands[$i]->{'styusho'} = $hcdata[9];

        my ($mshp, $msap, $msdp, $mssp) = (split(/,/, $Hislands[$i]->{'eisei5'}))[0..3];
        $Hislands[$i]->{'force'} = $mshp + $msap + $msdp + $mssp;

        foreach (split(/,/, $Hislands[$i]->{'eisei6'})) {
            # $Hislands[$i]->{'tuni'} += $_;
            $Hislands[$i]->{'uni'}++ if($_ > 0);
        }
    }

    my @elements   = ( 'pop'   , 'farm'  , 'factory', 'mountain'   , 'fore' ,
                       'tare'  , 'zipro' , 'leje'   , 'monsterlive', 'taiji',
                      'monta'  , 'hamu'  , 'pika'   , 'kei'        , 'rena' ,
                      'force'  , 'eisei2', 'uni'    , 'teamforce'  , 'styusho',
                      'shoritu', 'kachitent', 'kachiten' , 'tha_diff' , 'zoo_Mons_cnt' , 'factoryHT','area');

    my @islands;
    foreach (@elements) {
        $islands{$_} = islandSort($_);
        push(@HrankingID, $islands{$_}->{'id'});
    }
}


#----------------------------------------------------------------------
#
#   スペースデブリ減算
#
sub CalcSpaceDebri {

    $HSpace_Debris -= $HSpaceDebri_evapo;       # スペースデブリ 自然消滅

    if ($HSpace_Debris < 0 ) {

        $HSpace_Debris = 0;
    }
}


#----------------------------------------------------------------------
#
#   ログファイルを後ろにずらす
#
sub LogFileSlide {

    my ($i , $j , $s , $d);
    # ログファイルを後ろにずらす
    for ($i = ($HlogMax - 1); $i >= 0; $i--) {
        $j = $i + 1;
        $s = "${HdirName}/hakojima.log$i";
        $d = "${HdirName}/hakojima.log$j";
        unlink($d);
        rename($s, $d);
    }
}


#----------------------------------------------------------------------
#    負荷計測
##### 追加 親方20020307
#                       を移動
sub PerformanceLog {
##### 追加 親方20020307
        if ($Hperformance) {
            my ($uti, $sti, $cuti, $csti) = times();
            $uti += $cuti;
            $sti += $csti;
            my ($cpu) = $uti + $sti;
#            ログファイル書き出し(テスト計測用 普段はコメントにしておいてください)
#            open(POUT,">>cpu-t.log");
#            print POUT "CPU($cpu) : user($uti) system($sti)\n";
#            close(POUT);
            my ($timea) = sprintf("%.3f",Time::HiRes::time - $Hakoniwa_start_time);
            logLate("<small>負荷計測[1] CPU($cpu) : user($uti) system($sti) t:$timea</small>",0);
        }
#####
}


#----------------------------------------------------------------------
#
#  災害有無設定
#
sub CalcNoDisFlag {

    if (   ($HarmisticeTurn)
        && ($HislandTurn < $HarmisticeTurn) ) {

        $HnoDisFlag = 1;        # 停戦期間は無災害
    }
    else {

        $HnoDisFlag = 0;        # 災害あり
    }
}


#----------------------------------------------------------------------
sub zorome {

    my ($num) = @_;
    my ($ret) = 0;

    my ($tar) = substr($num, 0, 1);
    my ($len) = length($num);

    if (   ($num > 1000)
        && ($num =~ /${tar}{$len}/)) {

        $ret = 1;
    }

    return ($ret);
}


#----------------------------------------------------------------------
sub MakeHtmlLog {

    if (HTML_LOG_MAKE) {
        if (-e "${HhtmlDir}/hakolog.html") {
            unlink("${HhtmlDir}/hakolog.html");
        }
    }
}


#----------------------------------------------------------------------
sub weather_calc {
    my ($island) = @_;

    my ($wet);
    my ($wet_old);
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $mon += 1;

    $wet_old = $island->{'weather'};

    temperature_calc($island);

    $wet = weather_role($HWeather_table[$mon][0],$HWeather_table[$mon][1],$HWeather_table[$mon][2]);

    if ($island->{'temperature'} < 3) {

        $wet = $HWeather_Snow;
    }

    if ($wet_old == $wet) {

        $island->{'weather_chain'}++;
    }
    else {

        $island->{'weather_chain'} = 1 ;
    }
    $island->{'weather'} = $wet;
    $island->{'weather_old'} = $wet_old;
}


#----------------------------------------------------------------------
# 天候を決める
#----------------------------------------------------------------------
sub weather_role {
    my ($sun , $clu , $rain) = @_;

    my ($sum) = $sun + $clu + $rain;
    my ($rand) = random($sum);

    if ($rand < $sun) {

        return 0;
    }
    elsif ($rand < $sun + $clu) {

        return 1;
    }
    else {

        return 2;
    }

    return 0;
}


#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub temperature_calc {
    my ($island) = @_;

    my ($ra);
    my ($sec,$dummy,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $mon += 1;

    my ($temp) = $island->{'temperature'};

    my ($max) = $HTemperatureMax[$mon];
    my ($ave) = $HTemperatureAve[$mon];
    my ($min) = $HTemperatureMin[$mon];

    if (random(100) > 50){

        $temp += random(4);
    }
    else {

        $temp -= random(4);
    }

    if (random(100) < 70){

        if ($temp < $ave) {

            $temp += random(2);
            $temp += random(3) if(random(100) < 10);
        }
        else {

            $temp -= random(2);
            $temp -= random(3) if(random(100) < 10);
        }
    }

    $temp = $max if ($temp > $max);
    $temp = $min if ($temp < $min);

    $island->{'temperature'} = $temp;
}

#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub DayEvent {

    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $mon += 1;

    #$HDayEvent = 0;

    if (($mon == 1) && ($mday == 1) ) {      # 正月

        if (!$HDayEvent) {
            $HDayEvent = 1;

            my ($val) = (5) ; #鏡餅 HP5
            ItemPresent_ALL_island($HlandBigFood , $val ,  0, 0);
        }
    }
    elsif (isPockeyDay($mon , $mday)) {
        if (!$HDayEvent) {
            $HDayEvent = 1;
            $HDayEvent_Edge = 1;
        }
    }
    elsif (($mon == 2) && ($mday == 14)) {

        if (!$HDayEvent) {
            $HDayEvent = 1;

            my ($mKind) = 1 + (seqnum($HislandTurn) % 2);
            my ($val) = ($mKind << $Food_Kind_Shift) + (5) ; #チョコレート HP5
            ItemPresent_ALL_island($HlandBigFood , $val ,  0, 0);
        }

    }
    elsif (($mon == 3) && ($mday == 3)) {

        if (!$HDayEvent) {
            $HDayEvent = 1;
            $HDayEvent_Edge = 1 + int($HislandNumber / 12);

            my ($mKind) = 1 + (seqnum($HislandTurn) % 2);
            my ($val) = (3 << $Food_Kind_Shift) + (5) ; #ひしもち HP5
            ItemPresent_ALL_island($HlandBigFood , $val ,  0, 0);
        }

    }
    else {
        $HDayEvent = 0;
    }
}

#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub TradeEvent {

    my ($HtradeFile) = "trade.trd";

    open(IN, "<" , "${HdirName}/${HtradeFile}");
    my @lines = <IN>;
    close(IN);

    # 書き込みとイベント
    my ($data);
    open(OUT, ">" , "${HdirName}/${HtradeFile}");
    chomp($lines[0]);
    print OUT "$lines[0]\n";

    for ($i = 1 ; $i < (@lines) ; $i++) {

        $data = TradeDataConv($lines[$i]);

        doTrade($data);

        if ($data->{'absent'} < 12) {

            print OUT TradeDataToStr($data);
        }
    }
    close(OUT);
}


#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub doTrade {
    my ($data) = @_;

    if (   ($data->{'check1'} == 1)
        && ($data->{'check2'} == 1) ) {

        $data->{'absent'} = 0;

        # --------

        my ($island1_id , $island2_id);
        my ($island1 , $island2);
        my ($island_pay_m , $island_pay_obj);

        $island1_id = $data->{'island1_id'};
        $island2_id = $data->{'island2_id'};

        # 取引可能かチェック
        $island1 = $Hislands[$HidToNumber{$island1_id}];
        $island2 = $Hislands[$HidToNumber{$island2_id}];

        unless ($island1->{'trade_max'} > $island1->{'trade_cnt'}) {
            logOut("取引回数が上限で取引できませんでした。" , $island1_id);
            logOut("取引回数が上限で取引できませんでした。" , $island2_id);
            return ;
        }
        unless ($island2->{'trade_max'} > $island2->{'trade_cnt'}) {
            logOut("取引回数が上限で取引できませんでした。" , $island1_id);
            logOut("取引回数が上限で取引できませんでした。" , $island2_id);
            return ;
        }

        # お金
        if ($data->{'payside'}) {
            $island_pay_m = $island1;
        }
        else {
            $island_pay_m = $island2;
        }

        if ($island_pay_m->{'money'} < $data->{'money'}) {
            logOut("資金不足のため、取引ができませんでした。" , $island1_id);
            logOut("資金不足のため、取引ができませんでした。" , $island2_id);
            return ;
        }

        # オブジェ
        if ($data->{'objside'}) {
            $island_pay_obj = $island1;
        }
        else {
            $island_pay_obj = $island2;
        }

        # --------

        my ($name) = islandName($island2);
        logOut("debug:${HtagName_}$name${H_tagName}との取引が行われました。" , $island1_id);
        my ($name) = islandName($island1);
        logOut("debug:${HtagName_}$name${H_tagName}との取引が行われました。" , $island2_id);

        $island1->{'trade_cnt'}++;
        $island2->{'trade_cnt'}++;
    }
    else {

        $data->{'absent'} += 1;
    }
}


#----------------------------------------------------------------------
sub TradeDataToStr {
    my ($data) = @_;

    my ($TradeTargetID) = $data->{'id'};
    my ($island1_id) = $data->{'island1_id'};
    my ($island2_id) = $data->{'island2_id'};
    my ($obj) = $data->{'obj'};
    my ($obj_num) = $data->{'obj_num'};
    my ($objside) = $data->{'objside'};
    my ($money) = $data->{'money'};
    my ($payside) = $data->{'payside'};
    my ($check1) = $data->{'check1'};
    my ($check2) = $data->{'check2'};
    my ($absent) = $data->{'absent'};

    return ("$TradeTargetID,$island1_id,$island2_id,$obj,$obj_num,$objside,$money,$payside,$check1,$check2,$absent\n");

    # "$trade_next_id,$HcurrentID,$TradeTargetID,$TradeObject,$TradeObjectNum,$TradeMoney,$TradePaySide,0,0\n";
}

#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub ItemPresent_ALL_island {
    my ($kind , $val , $val2 , $val3) = @_;

    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $mon += 1;

    my ($i);
    my ($island);
    my ($name);
    my ($ItemName);
    my ($mKind);
    # $ItemName = landName($kind, $val,$val2);
    # 島全体処理
    for ($i = 0; $i < $HislandNumber; $i++) {

        $island = $Hislands[$i];
        $name = islandName($island);
        next if ($island->{'predelete'});
        next if ($island->{'BF_Flag'});

        if (   ($mon == 2)
            && ($mday == 14) ) {

            $mKind = 1 + (seqnum($i) % 2);
            $val = ($mKind << $Food_Kind_Shift) + (5) ; #チョコレート HP5
            $ItemName = landName($kind, $val, $val2);
        }

        ItemPresent($island, $kind,$val);
        logOut("${HtagName_}${name}${H_tagName}へ<B>$ItemName</B>が送られました。",$island->{'id'} );
    }

}


#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub ItemPresent {
    my ($island, $itemland,$itemland_value) = @_;

    my ($i);
    my ($item);
    my ($item_lv);
    my ($item_lv2);
    my ($item_lv3);
    my ($item_ret);

    $item     = $island->{'item_land'};
    $item_lv  = $island->{'item_landValue'};
    $item_lv2 = $island->{'item_landValue2'};
    $item_lv3 = $island->{'item_landValue3'};
    $item_ret = 0;

    for ($i = 0; $i < $HItem_MAX; $i++) {

        if ($item->[$i] == $HItem_Nothing ) {

            $item_ret = 1;
            $item->[$i] = $itemland;
            $item_lv->[$i] = $itemland_value;
            $item_lv2->[$i] = 0;
            $item_lv3->[$i] = 0;
            last;
        }
    }

    return $item_ret;
}


#----------------------------------------------------------------------
# 終了かどうか
#----------------------------------------------------------------------
sub GameOver_wrap {

    # 終了条件の判定
    my ($n) = gameOver();
    if (   ($HarmisticeTurn)
        && ($HislandTurn <= $HgameLimitTurn)
        && ($n != -1)) {

        logHistory("${HtagName_}${Hally[$n]->{'name'}}${H_tagName}が<B>勝利</B>しました！");
        $Hally[$n]->{'name'} = '【勝者！】' . $Hally[$n]->{'name'};
        $HplayNow = 0;
    }
}

#----------------------------------------------------------------------
# 終了かどうか
#----------------------------------------------------------------------
sub gameOver {
    # 時間切れ
    if ($HgameLimitTurn) {
        if ($HislandTurn >= $HgameLimitTurn) {
            # トップの陣営をかえす
            return 0;
        }
    }
    # コールド
    my ($i);
    for ($i = 0; $i < $HallyNumber; $i++) {
        if ($Hally[$i]->{'occupation'} >= $HfinishOccupation) {
            #return $i;
        }
    }
    return -1;
}


#----------------------------------------------------------------------
# 参加島への制裁内容を読み込む
#----------------------------------------------------------------------
sub readPunishData {

    if (open(Fpunish, "<${HdirName}/punish.dat")) {

        local(@_);
        my ($island);
        while (<Fpunish>) {
            chomp;
            @_ = split(',');
            my($obj);
            $obj->{id} = shift;
            $obj->{punish} = shift;
            $obj->{x} = shift;
            $obj->{y} = shift;
            $HpunishInfo{$obj->{id}} = $obj;
        }
        close(Fpunish);
    }
    # 制裁データを削除する
    unlink("${HdirName}/punish.dat");
}


#----------------------------------------------------------------------
# 未使用
#----------------------------------------------------------------------
sub tempRefresh {
    my ($delay, $str) = @_;
    my ($next) = $HislandTurn + 1;
        out(<<END);
<meta http-equiv='refresh' content='$delay; url="$HthisFile?UNLOCK=$HsepTurnFlag"'>
<h1><small>ターン</small> ${HislandTurn} => ${next}</h1>
<h2>$str</h2>
END
}


#----------------------------------------------------------------------
# 収入、消費フェイズ
#----------------------------------------------------------------------
sub income {
    my ($island) = @_;
    my ($pop, $farm, $factory, $mountain, $factoryHT , $park_work) =
    (
        $island->{'pop'},
        $island->{'farm'} * 10,
        $island->{'factory'},
        $island->{'mountain'},
        $island->{'factoryHT'},
        $island->{'park_work'}
    );
    my ($co0) = $island->{'co0'};            # 大学の効果
    my ($co1) = $island->{'co1'};            # 大学の効果

    $island->{'farmer'} = 0;
    $island->{'business'} = 0;

    if ($island->{'effect'} & $g_Island_Retro) {
        $factoryHT = 0;
        $factory = $island->{'park_work'};
    }

    # 収入
    if ($pop > $farm) {
        # 農業だけじゃ手が余る場合
        Calc_Product_Food($island , $farm); # 農場フル稼働
        $island->{'money'} += int(min(int(($pop - $farm) / 10), $factory + $factoryHT + $mountain) * ($co1 + 1) * $Hmoney1Incom[0]/100);
        $island->{'farmer'} = 1;
        $island->{'business'} = 1;
    }
    else {
        # 農業だけで手一杯の場合
        Calc_Product_Food($island , $pop);  # 全員野良仕事
        $island->{'farmer'} = 1;
    }

    # 食料消費
    my ($foodkind);
    $foodkind = food_product_consumption($island , int($pop * $HeatenFood * $HeatenFoodS[0]/100) );
    # logOut("debug:食料種類:$foodkind" , $island->{'id'});
}


#----------------------------------------------------------------------
# foodの算出
#----------------------------------------------------------------------
sub Calc_Product_Food {
    my ($island , $pop) = @_;

    return if ($pop <= 0);

    my ($debug_pop);
    my ($debug_in) = "pop:$pop/";

    my ($co0) = ($island->{'co0'}) ? ($island->{'co0'}) : 0;            # 農業大学
    $island->{'food'} += int($pop * ($co0 + 1) * $Hfood1Incom[0]/100);

    $debug_pop = int($pop * ($co0 + 1) * $Hfood1Incom[0]/100);

    my (%product_wk) = ();
    my ($product_num , $product_sum) = (0,0);
    {
        my ($product);
        foreach $product (@HProduct_Food_hash_table) {

            $product_wk{$product} = ($island->{$product . '_work'} * 10);
            $product_sum += ($island->{$product . '_work'}) ? ($island->{$product . '_work'}*10) : 0;
            $product_num += ($island->{$product . '_work'}) ? 1 : 0;
            $debug_in .="$product:($island->{$product . '_work'})/"
        }
    }

    return if ($product_num <= 0);

    my ($ave) = int($product_sum / $product_num);
    my ($woker) = 0;
    my ($val) = 0;

    my ($debug_prodct) = 0;

    for my $key (sort {$product_wk{$a} <=> $product_wk{$b}} keys %product_wk) {

        $val = ($product_wk{$key}) ? ($product_wk{$key}) : 0 ;
        next if ($val <= 0);

        $val = ($ave <= $val) ? $ave : $val;
        $woker = ($val <= $pop) ? $val : $pop;
        $woker = ($woker < 0) ? 0 : $woker;

        $island->{$key} += int($woker * ($co0 + 1) * $Hfood1Incom[0]/100);
        $debug_prodct += int($woker * ($co0 + 1) * $Hfood1Incom[0]/100);

        $product_sum -= $woker;
        $pop -= $woker;
        last if ($pop <= 0);

        $product_num--;
        next if ($product_num <= 0);

        $ave = int($product_sum / $product_num);
    }

    if ($debug_prodct != $debug_pop) {
        logOut("生産不一致：$debug_in" , $island->{'id'});
        logOut("生産不一致：$debug_pop / $debug_prodct" , $island->{'id'});
    }
}


#----------------------------------------------------------------------
# 神殿のお祭り
#----------------------------------------------------------------------
sub Sinden_Omaturi {
    my ($island,$base,$rand) = @_;

    if ($island->{'sin'} > 0) {
        my ($value);
        $value = $base + random($rand);
        $island->{'money'} += $value;
        logSinMoney($island->{'id'}, islandName($island), "$value$HunitMoney");
    }
}


#----------------------------------------------------------------------
# 神社のお祭り
#----------------------------------------------------------------------
sub Jinja_Omaturi {
    my ($island,$base,$rand) = @_;

    if ($island->{'jin'} > 0) {
        my ($value);
        $value = $base + random($rand);
        $island->{'money'} += $value;
        logJinMoney($island->{'id'}, islandName($island), "$value$HunitMoney");
    }
}


#----------------------------------------------------------------------
# コマンドフェイズ
#----------------------------------------------------------------------
sub doCommand {
    my ($island) = @_;
    # コマンド取り出し
    my ($comArray, $command);
    $comArray = $island->{'command'};
    $command = $comArray->[0]; # 最初のを取り出し
    slideFront($comArray, 0); # 以降を詰める

    # 各要素の取り出し
    my($kind, $target, $x, $y, $arg) =
    (
        $command->{'kind'},
        $command->{'target'},
        $command->{'x'},
        $command->{'y'},
        $command->{'arg'}
    );

    # 導出値
    my ($name) = islandName($island);
    my ($id) = $island->{'id'};
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};
    my ($landKind) = $land->[$x][$y];
    my ($lv) = $landValue->[$x][$y];
    my ($lv2) = $landValue2->[$x][$y];
    my ($lv3) = $landValue3->[$x][$y];
    my ($cost) = $HcomCost[$kind];
    my ($comName) = $HcomName[$kind];
    my ($point) = "($x, $y)";
    my ($landName) = landName($landKind, $lv, $lv2, $lv3);

    if (   ($kind == $HcomDoNothing)
        && (   ($id <= 100)
            && (!$island->{'BF_Flag'}))) {
        # 資金繰り
#       logPropaganda($id, $name, $comName);
        $island->{'money'} += int(10 * $Hmoney1Incom[$Hmonth]/100);
        if ($HeasyMode) {
            $island->{'money'} += random(100);
            if (random(100) < 5) {
                my $value = 1+ random(1999);
                $island->{'money'} += $value;
                # 収入ログ
                logEnjo($id, $name, $landName, $point , "$value$HunitMoney") if ($value > 0);
            }
        }
        $island->{'absent'}++;

        # 自動放棄
        if ($island->{'absent'} >= $HgiveupTurn) {
            $comArray->[0] = {
                'kind' => $HcomGiveup,
                'target' => 0,
                'x' => 0,
                'y' => 0,
                'arg' => 0
            }
        }
        return 1;
    }

    $island->{'absent'} = 0;        #資金繰り回数を0に

    # 値段算出
    {
        my ($temp_cost);
        $temp_cost = $cost;
        if ($temp_cost =~ s/Pointx(.*)$//g) {
            $cost = $island->{'pts'} * int($1);
        }
        else {
            $cost = $temp_cost;
        }
    }

    if (   ($kind != $HcomGivefood)
        && ($kind != $HcomSell)
        && ($kind != $HcomSave)
        && ($kind != $HcomLoad)
        && ($kind != $HcomFood)
        && ($kind != $HcomMoney) ){

        if ($island->{'business'} > 0) {
            if ($island->{'shtf'} > 0) {        #ハイテク企業 改造 片持ち

                $cost = int($cost * 9 / 10);
            }
            elsif ($island->{'htf'} > 0){

                $cost = int($cost * 2 / 3);
            }
        }
    }

    # コストチェック
    if (   ($cost > 0)
        && ($island->{'money'} < $cost)
        && ($kind != $HcomFarmcpc)
            ) { # 金の場合(家畜販売の場合、コストチェックしない)

        logNoAny($id, $name, $comName, '資金不足の');
        return 0;
    }
    elsif (   ($cost < 0)
           && ($island->{'food'} < (-$cost) ) ) {# 食料の場合
        logNoAny($id, $name, $comName, '備蓄食料不足の');
        return 0;
    }

    # コマンドで分岐
    if (   ($kind == $HcomPrepare)
        || ($kind == $HcomPrepare2) ) {
        # 整地、地ならし
        if ( ($landKind == $HlandSea) ||
             ($landKind == $HlandIce) ||
             ($landKind == $HlandGold) ||
             ($landKind == $HlandYougan) ||
             ($landKind == $HlandShrine) ||
             ($landKind == $HlandRottenSea) ||
             ($landKind == $HlandMountain) ||
             ($landKind == $HlandGomi) ||
             ($landKind == $HlandGomiFactory) ||
             ($landKind == $HlandMonster)) {
            # 海、金山、時の神殿、腐海、山、怪獣は整地できない
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

        if ($landKind == $HlandMonument) {       # 記念碑

            if (   (79 < $lv)
                && ($lv < 84) ) {
                #$island->{'food'} += 20000; # 食べちゃえ
                food_product_plus($island , 'tamago' ,20000);
            }
            elsif ((73 < $lv) && ($lv < 80)) {
                $island->{'money'} += 20000; # 宝石会社売却
            }

        }
        elsif ($landKind == $HlandEgg) {       # 卵
            #$island->{'food'} += 20000; # 食べちゃえ
            food_product_plus($island , 'tamago' ,20000);

        }
        elsif ( $landKind == $HlandTown ) {
            logTownDel($id, $name, $landName ,'整地', $point , $lv);
        }

        # 目的の場所を平地にする
        if (($landKind == $HlandOil) ||         # 油田
            ($landKind == $HlandFune) ||        # 船
            ($landKind == $HlandSbase) ||       # 海底基地
            ($landKind == $HlandSeacity) ||     # 海底都市
            ($landKind == $HlandSeatown) ||     # 海底新都市
            ($landKind == $HlandFrocity) ||     # 海上都市メガフロート
            ($landKind == $HlandUmiamu) ||      # 海あみゅ
            ($landKind == $HlandUmishuto) ||    # 海底首都
            ($landKind == $HlandNursery) ||     # 養殖場
            ($landKind == $HlandUmicity) ||     # 養殖場
            ($landKind == $HlandOilCity) ||     # 油田都市
            (0)                          ) {

            if ($landKind == $HlandNursery) {

                SetSeaShallowLand($island , $x , $y);
            }
            else {

                $land->[$x][$y] = $HlandSea;
                $landValue->[$x][$y] = 0;
                $landValue->[$x][$y] = 1 if ($landKind == $HlandNursery);    # 養殖場は浅瀬に
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }
        }
        else {
            SetPlains_Normal($island , $x , $y);
        }

        # 整地ログを１本化
        if ($HlogOmit2) {

            my ($sno) = $island->{'seichi'};
            $island->{'seichi'}++;

            if ($HlogOmit2 == 1) {
                my ($seichipnt);
                ($seichipnt->{x}, $seichipnt->{y}) = ($x, $y);
                $island->{'seichipnt'}->[$sno] = $seichipnt;
            }
        }
        else {
            logLandSuc($id, $name, '整地', $point);
        }

        # 金を差し引く
        $island->{'money'} -= $cost;

        if ($kind == $HcomPrepare2) { # 地ならし

            $island->{'prepare2'}++;
            # ターン消費せず
            return 0;
        }
        else {
            # 整地なら、埋蔵金の可能性あり
            if (!$HnoDisFlag && (random(1000) < $HdisMaizo) ) {
                my ($v) = 100 + random(901);
                $island->{'money'} += $v;
                logMaizo($id, $name, $comName, $v);
            }
            return 1;
        }

    } elsif ( ($kind == $HcomReclaim) || 
              ($kind == $HcomReclaim2) ||
              ($kind == $HcomReclaim_spd) ||
              ($kind == $HcomMinato) ||
              ($kind == $HcomSeki) ||
              ($kind == $HcomReclaim2dan) ) {
        # 埋め立て、遠距離埋め立て、港、関所

        my ($flag) = 1;
        # 周りに陸があるかチェック
        my ($seaCount) = countAround($land, $x, $y, 7, @Hseas);
        if (   ($seaCount == 7)
            && ($kind != $HcomReclaim2)
            && ($kind != $HcomSeki)) {

            # 全部海のとき、埋め立て、港建設は不能
            logLandFail2($id, $name, $comName, $point, "周辺に陸地がなかった");
            return 0;
        }

        if (   ($kind == $HcomReclaim)
            || ($kind == $HcomReclaim2)
            || ($kind == $HcomReclaim2dan)
            || ($kind == $HcomReclaim_spd) ) {
            # 埋め立て
            if ( ($landKind != $HlandSea) &&
                 ($landKind != $HlandSbase) &&
                 ($landKind != $HlandSeacity) &&
                 ($landKind != $HlandSeatown) &&
                 ($landKind != $HlandNursery) &&
                 ($landKind != $HlandUmicity) &&
                 ($landKind != $HlandOil) &&
                 ($landKind != $HlandUmiamu) &&
                 ($landKind != $HlandPlains) &&
                 ($landKind != $HlandUmishuto) &&
                 ($landKind != $HlandWaste) ) {
                # 海、油田、海あみゅ、海底基地、海底都市、海底新都市、平地、荒地、養殖場、しか埋め立てできない
                logLandFail($id, $name, $comName, $landName, $point);
                return 0;
            }

            # 2段埋め立て
            if ($kind == $HcomReclaim2dan) {

                if (   ($landKind == $HlandSea) && ($lv == 1) ) {
                    # 浅瀬の場合
                    # 目的の場所を山にする
                    SetMountain_Normal($island,$x,$y);

                } elsif(   ($landKind == $HlandPlains)
                        || ($landKind == $HlandWaste) ) {
                    # 平地、荒地なら、目的の場所を山にする
                    SetMountain_Normal($island,$x,$y);
                    $flag = 0;

                } else {
                    # 海、油田、養殖場、海あみゅ、海底基地、海底都市、海底新都市なら、
                    # 目的の場所を荒地にする
                    SetWasteLand_Normal($island,$x,$y);     # $HlandWaste
                }
            }
            else {
                #通常の埋め立て
                if ( ($landKind == $HlandSea) && ($lv == 1) ) {
                    # 浅瀬の場合
                    # 目的の場所を荒地にする
                    SetWasteLand_Normal($island,$x,$y);     # $HlandWaste

                } elsif(   ($landKind == $HlandPlains)
                        || ($landKind == $HlandWaste) ) {
                    # 平地、荒地なら、目的の場所を山にする
                    SetMountain_Normal($island,$x,$y);
                    $cost = $HcomCost[$HcomReclaim]; #コストを埋めてたに変える
                    $flag = 0;
                } else {
                    # 海、油田、養殖場、海あみゅ、海底基地、海底都市、海底新都市なら、目的の場所を浅瀬にする
                    SetSeaShallowLand($island , $x , $y);
                    $flag = 0;
                }

                if ($kind == $HcomReclaim_spd) {
                    $comName = $HcomName[$HcomReclaim];
                }
            }

        } elsif ($kind == $HcomMinato) {
            # 港
            unless (   ($landKind == $HlandSea)
                    && ($lv == 1) ){
                # 浅瀬しか港にできない
                logLandFail($id, $name, $comName, $landName, $point);
                return 0;
            }
            # 目的の場所を港にする
            $land->[$x][$y] = $HlandMinato;
            $landValue->[$x][$y] = 0;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;

        } elsif ($kind == $HcomSeki) {
            # 関所
            if (($landKind != $HlandSea) || ($lv != 1)) {
                # 浅瀬しか関所にできない
                logLandFail($id, $name, $comName, $landName, $point);
                return 0;
            }
            # 目的の場所を関所にする
            $land->[$x][$y] = $HlandSeki;
            $landValue->[$x][$y] = 0;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
        }
        logLandSuc($id, $name, $comName, $point);

        if ($flag) {
            $island->{'area'}++;
            if ($seaCount <= 4) {
            # 周りの海が3ヘックス以内なので、浅瀬にする
                my ($i, $sx, $sy);
                for ($i = 1; $i < 7; $i++) {
                    $sx = $x + $ax[$i];
                    $sy = $y + $ay[$i];
                    # 行による位置調整
                    $sx-- if(!($sy % 2) && ($y % 2));
                    # 範囲内の場合
                    if (   ($sx >= 0) && ($sx < $HislandSize)
                        && ($sy >= 0) && ($sy < $HislandSize)
                        && ($land->[$sx][$sy] == $HlandSea)) {
                        $landValue->[$sx][$sy] = 1;
                    }
                }
            }
        }
        # 金を差し引く
        $island->{'money'} -= $cost;
        if ($kind == $HcomReclaim_spd) {
            $island->{'prepare2'}++;
            return 0;
        }
        else {
            return 1;
        }

    } elsif($kind == $HcomPropaganda) {             # 誘致活動

        logPropaganda($id, $name, $comName);
        $island->{'propaganda'} = 1;
        $island->{'money'} -= $cost;
        if ($arg > 1) {
            $arg--;
            slideBack($comArray, 0);
            $comArray->[0] = {
                'kind' => $kind,
                'target' => $target,
                'x' => $x,
                'y' => $y,
                'arg' => $arg
            };
        }
        return 1;

    } elsif ($kind == $HcomFune) {
        # 造船・出航
        if ($landKind != $HlandSea) {
            # 海しか造船できない
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        # 周りに港があるかチェック
        my ($seaCount) = countAround($land, $x, $y, 7, $HlandMinato);
        if ($seaCount == 0) {
            # 港がないから造船不能
            logLandFail2($id, $name, $comName, $point, "周辺に港町がなかった");
            return 0;
        }
        # コストチェック
        my ($value) = ($arg * $cost);
        if ($island->{'money'} < $value) {
            logNoAny($id, $name, $comName, "資金不足の");
            return 0;
        }
        if ($arg == $HcomFrocity_num) {
            # 海上都市にする
            $land->[$x][$y] = $HlandFrocity;
            $landValue->[$x][$y] = 1;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
        }
        else {
            # 目的の場所を船にする
            $land->[$x][$y] = $HlandFune;
            $arg = 1 if($arg >= $HfuneNumber || !$arg);
            $landValue->[$x][$y] = $arg;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
        }
        logLandSuc($id, $name, $comName, $point);
        # 金を差し引く
        $island->{'money'} -= $value;
        return 1;

    } elsif($kind == $HcomDestroy) {
        # 掘削
        if(    ($landKind == $HlandSbase)
            || ($landKind == $HlandSeacity)
            || ($landKind == $HlandSeatown)
            || ($landKind == $HlandNursery)
            || ($landKind == $HlandUmicity)
            || ($landKind == $HlandOil)
            || ($landKind == $HlandFune)
            || ($landKind == $HlandUmiamu)
            || ($landKind == $HlandFrocity)
            || ($landKind == $HlandRottenSea)
            || ($landKind == $HlandUmishuto)
            || ($landKind == $HlandMonster)
            || ($landKind == $HlandYougan)
            || ($landKind == $HlandBigFood)
                                            ) {
            # 海底基地、海底都市、海底新都市、油田、船、養殖場、海あみゅ、腐海、怪獣は掘削できない
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

        if (($landKind == $HlandSea) && !$lv) {
            # 海なら、油田探し
            # 投資額決定
            if ($HarmisticeTurn && ($HislandTurn <= $HgameLimitTurn)) {
                # 開発期間中は油田禁止
                logNotAvail($id, $name, $comName);
                return 0;
            }
            $arg = 1 if($arg == 0);
            my ($value, $p);
            $p = ($arg * $cost > $island->{'money'}) ? int($island->{'money'} / $cost) : $arg;
            $value = $p * $cost;
            $island->{'money'} -= $value;
            # 見つかるか判定
            if ($p > random(100) + $island->{'oil'} * 25) {
                # 油田見つかる
                if ($arg == 1) {

                    logOil200Found($id, $name, $point, $comName, "$value$HunitMoney");
                    SetMonument_Normal($island ,$x , $y , 95);
                }
                else {

                    logOilFound($id, $name, $point, $comName, "$value$HunitMoney");
                    SetOilLand($island ,$x , $y);
                }

                $island->{'oil'}++;

                Sinden_Omaturi($island , 0 , 1001);     # 神殿
                Jinja_Omaturi($island , 0 , 1001);      # 神社
            }
            else {
                # 無駄撃ちに終わる
                logOilFail($id, $name, $point, $comName, "$value$HunitMoney");
            }
            return 1;
        }
        # 目的の場所を浅瀬にする。山、金山、時の神殿なら荒地に。浅瀬なら海に。
        if (   ($landKind == $HlandMountain)
            || ($landKind == $HlandGold)
            || ($landKind == $HlandShrine)
            || ($landKind == $HlandOnsen) ) {

            SetWasteLand_Normal($island,$x,$y);     # $HlandWaste

        } elsif($landKind == $HlandSea) {
            SetSeaLand_Normal($island , $x , $y);

        } else {
            SetSeaShallowLand($island , $x , $y);
            $island->{'area'}-- if($landKind != $HlandIce);
        }
        logLandSuc($id, $name, $comName, $point);
        # 金を差し引く
        $island->{'money'} -= $cost;
        return 1;

    } elsif($kind == $HcomDestroy2) {
        # 掘削
        if (   ($landKind == $HlandSbase)
            || ($landKind == $HlandSeacity)
            || ($landKind == $HlandSeatown)
            || ($landKind == $HlandUmicity)
            || ($landKind == $HlandOilCity)
            || ($landKind == $HlandNursery)
            || ($landKind == $HlandOil)
            || ($landKind == $HlandFune)
            || ($landKind == $HlandUmiamu)
            || ($landKind == $HlandFrocity)
            || ($landKind == $HlandRottenSea)
            || ($landKind == $HlandYougan)
            || ($landKind == $HlandUmishuto)
            || (   ($landKind == $HlandSea)
                && ($lv == 0) )
            || ($landKind == $HlandMonster)
            || ($landKind == $HlandYougan)
            || ($landKind == $HlandBigFood)
                                            ) {
            # 海底基地、海底都市、海底新都市、油田、船、養殖場、海あみゅ、腐海、怪獣は掘削できない
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

        # 目的の場所を浅瀬にする。山、金山、時の神殿なら荒地に。浅瀬なら海に。
        if (   ($landKind == $HlandMountain)
            || ($landKind == $HlandGold)
            || ($landKind == $HlandShrine)
            || ($landKind == $HlandOnsen)
                                                ){

            SetWasteLand_Normal($island,$x,$y);     # $HlandWaste
        } elsif($landKind == $HlandSea) {
            SetSeaLand_Normal($island , $x , $y);

        } else {
            SetSeaShallowLand($island , $x , $y);
            $island->{'area'}-- if($landKind != $HlandIce);
        }

        $comName = $HcomName[$HcomDestroy];
        logLandSuc($id, $name, $comName, $point);
        # 金を差し引く
        $island->{'money'} -= $cost;
        $island->{'prepare2'}++;
        return 0;

    } elsif($kind == $HcomOnsen) {# 温泉掘削

        if (   ($landKind == $HlandMountain)
            && ($lv == 0)
                                    ) {
            # 山なら、温泉探し
            # 投資額決定
            $arg = 1 if(!$arg);
            my ($value, $p);
            $value = min($arg * ($cost), $island->{'money'});
            $p = int($value / $cost);
            $value = $p * $cost;
            $island->{'money'} -= $value;

            # 見つかるか判定
            if(random(10000) < $p * 15) {
                my($v) = 1000 + random(2001);
                $island->{'money'} += $v;
                $land->[$x][$y] = $HlandGold;
                $landValue->[$x][$y] = 1;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                logGold($id, $name, $comName, $v);

                # 神殿
                Sinden_Omaturi($island , 0 , 1001);

                # 神社
                Jinja_Omaturi($island , 0 , 1001);

            } elsif(random(1000) < 50) {
                logEggFound($id, $name, $comName);
                $land->[$x][$y] = $HlandEgg;
                $landValue->[$x][$y] = random($HEggKindMax);
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

            } elsif(random(1000) < 50) {
                logIsekiFound($id, $name, $comName);
                SetMonument_Normal($island , $x , $y , 84);

            } elsif($p > random(100) + $island->{'hot'} * 30) {
                # 温泉見つかる
                logHotFound($id, $name, $point, $comName, "$value$HunitMoney");
                $land->[$x][$y] = $HlandOnsen;
                $landValue->[$x][$y] = 1;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

            } else {
                # 無駄撃ちに終わる
                logHotFail($id, $name, $point, $comName, "$value$HunitMoney");
            }

            if(random(1000) < 15) {
                my($v) = 100 + random(901);
                $island->{'money'} += $v;
                logMaizo($id, $name, $comName, $v);
            }
            return 1;
        } else {
            # 山以外は掘削できない
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

    } elsif($kind == $HcomYotei) {
        if(!($landKind == $HlandPlains)){

            # 不適当な地形
            logLandFail($id, $name, $comName, $landName, $point);
            return 0; # ターン消費なし
        }
        # 目的の場所を平地にする
        $land->[$x][$y] = $HlandPlains;
        if ( $lv == 0 ) {
            $landValue->[$x][$y] = 1;
        }else{
            $landValue->[$x][$y] = 0;
        }
        $landValue2->[$x][$y] = 0;
        $landValue3->[$x][$y] = 0;
        return 0; # ターン消費なし

    } elsif($kind == $HcomSellTree) {
        # 伐採
        if($landKind != $HlandForest) {
            # 森以外は伐採できない
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        # 目的の場所を平地にする
        SetPlains_Normal($island, $x,$y);
        logLandSuc($id, $name, $comName, $point);
        if(random(1000) < 75) {
            logEggFound($id, $name, $comName);
            $land->[$x][$y] = $HlandEgg;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            $landValue->[$x][$y] = random($HEggKindMax);
        }
        # 売却金を得る
        $island->{'money'} += $HtreeValue * $lv;
        return 0; # ターン消費なし

    # 地上建設系
    } elsif(($kind == $HcomPlant) ||    # 植林
            ($kind == $HcomFarm) ||        # 農場
            ($kind == $HcomFoodim) ||    # 食物研究所
            ($kind == $HcomFarmcpc) ||    # 牧場
            ($kind == $HcomCollege) ||    # 大学設置
            ($kind == $HcomFactory) ||    # 工場
            ($kind == $HcomBase) ||        # ミサイル基地
            ($kind == $HcomMonument) ||    # 記念碑
            ($kind == $HcomHaribote) ||    # ハリボテ
            ($kind == $HcomMonbuy) ||    # 怪獣購入
            ($kind == $HcomMonbuyt) ||    # テトラ購入
            ($kind == $HcomPark) ||        # 遊園地
            ($kind == $HcomMine) ||        # 地雷
            ($kind == $HcomNursery) ||    # 養殖場
            ($kind == $HcomKyujo) ||    # 野球場
            ($kind == $HcomYakusho) ||    # 役所コマンド
            ($kind == $HcomUmiamu) ||    # 海あみゅ
            ($kind == $HcomNewtown) ||    # ニュータウン
            ($kind == $HcomRizort) ||    # リゾート
            ($kind == $HcomDbase) || # 防衛施設
            ($kind == $HcomFire) || # 消防署建設
            ($kind == $HcomZoo) || # 動物園
            (0)) {

        if(!
            (   ($landKind == $HlandPlains)
             || ($landKind == $HlandTown)
             || (   ($landKind == $HlandPark)
                 && ($kind == $HcomPark) )
             || (   ($landKind == $HlandIce)
                 && ($kind == $HcomPark) )
             || (   ($landKind == $HlandBeachPark)
                 && ($kind == $HcomPark) )
             || (   ($landKind == $HlandSunahama)
                 && ($lv == 0)
                 && ($kind == $HcomPark) )
             || (   ($kind == $HcomUmiamu)
                 && (   ($landKind == $HlandSea) && (!$lv)
                     || ($landKind == $HlandUmiamu) ) )
             || (   ($landKind == $HlandMonument)
                 && ($kind == $HcomMonument)  )
             || (   ($kind == $HcomFarm)
                 && (   ($landKind == $HlandFarm)
                     || ($landKind == $HlandForest)
                     || ($landKind == $HlandSunahama)
                                                     ) )
             || (   (   ($landKind == $HlandFarmchi)
                     || ($landKind == $HlandFarmpic)
                     || ($landKind == $HlandFarmcow) )
                 && ($kind == $HcomFarmcpc) )
             || (   ($landKind == $HlandCollege)
                 && ($kind == $HcomCollege)  )
             || (   ($landKind == $HlandFoodim)
                 && ($kind == $HcomFoodim) )
             || (   ($landKind == $HlandFactory)
                 && ($kind == $HcomFactory) )
             || (   (($landKind == $HlandSea) && !$lv)
                 && ($kind == $HcomMine) )
             || (   ($landKind == $HlandForest)
                 && ($kind == $HcomFactory) )
             || (   (   ($landKind == $HlandSea) && ($lv)
                     || ($landKind == $HlandNursery))
                 && ($kind == $HcomNursery) )
             || (   ($landKind == $HlandZoo)
                 && ($kind == $HcomZoo) )
                                            ) ) {
            # 不適当な地形
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

        # 種類で分岐
        if($kind == $HcomPlant) {
            # 植林
            $land->[$x][$y] = $HlandForest;
            $landValue->[$x][$y] = 1; # 木は最低単位
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logPBSuc($id, $name, $comName, $point);

        } elsif(($kind == $HcomMonbuy) || ($kind == $HcomMonbuyt)) {
            # 怪獣購入・テトラ購入
            my $mKind = MonsterBuySpawn();

            $mKind = 29 if($kind == $HcomMonbuyt); # 神獣テトラ
            $lv = Calc_MonsterLandValue($mKind);
            $land->[$x][$y] = $HlandMonster;
            $landValue->[$x][$y] = $lv;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            $island->{'monsterlive'}++;
            # 怪獣情報
            my($mName) = (monsterSpec($lv))[1];
            # メッセージ
            logMonsFree($id, $name, $mName, $point);

        } elsif($kind == $HcomBase) {
            # ミサイル基地
            $land->[$x][$y] = $HlandBase;
            $landValue->[$x][$y] = 0; # 経験値0
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logPBSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomFactory) {
            # 工場
            if($landKind == $HlandFactory) {
                # すでに工場の場合
                $landValue->[$x][$y] += $HFactory_add; # 規模 + 10000人
                $landValue->[$x][$y] = $HFactory_limit if($landValue->[$x][$y] > $HFactory_limit); # 最大 100000人

            } elsif($landKind == $HlandForest) {
                # 目的の場所を工場に
                $land->[$x][$y] = $HlandFactory;
                $landValue->[$x][$y] = $HFactory_base; # 規模 = 30000人
                $landValue2->[$x][$y] = 1;
                $landValue3->[$x][$y] = 0;

            } else {
                # 目的の場所を工場に
                $land->[$x][$y] = $HlandFactory;
                $landValue->[$x][$y] = $HFactory_base; # 規模 = 30000人
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomPark) {
            # 遊園地
            if($landKind == $HlandPark) {
                # すでに遊園地の場合
                $landValue->[$x][$y] += $HPark_add; # 規模 + 30000人
                $landValue->[$x][$y] = $HPark_limit if($landValue->[$x][$y] > $HPark_limit); # 最大 100000人
            } elsif($landKind == $HlandIce) {
                # すでに氷河の場合
                $landValue->[$x][$y] += $HIce_add; # 規模 + 25000人
                $landValue->[$x][$y] = $HPark_limit if($landValue->[$x][$y] > $HPark_limit); # 最大 100000人
            } elsif($landKind == $HlandSunahama) {
                # すでに氷河の場合
                $land->[$x][$y] = $HlandBeachPark;
                $landValue->[$x][$y] = $HPark_base; # 規模 + 25000人
            } elsif($landKind == $HlandBeachPark) {
                # すでに氷河の場合
                $landValue->[$x][$y] += $HIce_add; # 規模 + 25000人
                $landValue->[$x][$y] = $HPark_limit if($landValue->[$x][$y] > $HPark_limit); # 最大 100000人
            } else {
                # 目的の場所を遊園地に
                $land->[$x][$y] = $HlandPark;
                $landValue->[$x][$y] = $HPark_base; # 規模 = 10000人
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                $island->{'par'}++;
            }
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomZoo) {

            my (@mons_list);
            my ($tmp);

            if ($landKind == $HlandZoo) {
                # 動物園
                my ($nigekaiju);
                my ($nigeflag);

                $tmp = $island->{'zoo'};
                chomp($tmp);
                @mons_list = split(/\,/,$tmp);

                $nigekaiju = $arg;
                $nigeflag = 0;

                # 怪獣を買ってるか？
                if ($mons_list[$nigekaiju] > 0) {
                    my ($i, $sx, $sy, $la_Kind, $mlv);

                    # 周囲1HEXの土地を確認
                    for ($i = 1; $i < 7; $i++) {
                        $sx = $x + $ax[$i];
                        $sy = $y + $ay[$i];

                        # 行による位置調整
                        if ((($sy % 2) == 0) && (($y % 2) == 1)) {
                            $sx--;
                        }

                        if ( ($sx < 0) || ($sx >= $HislandSize) ||
                             ($sy < 0) || ($sy >= $HislandSize)) {

                        } else {
                            # 範囲内の場合
                            $la_Kind = $land->[$sx][$sy];
                            $mlv = $landValue->[$sx][$sy];
                            $point = "($sx, $sy)";

                            if (   ($la_Kind == $HlandWaste)
                                || ($la_Kind == $HlandPlains) 
                                || ($la_Kind == $HlandTown)
                                || ($la_Kind == $HlandForest)
                                || ($la_Kind == $HlandHaribote)
                                                                 ) {

                                if ($nigeflag < 1) {
                                    $nigeflag = 1;
                                    $mons_list[$nigekaiju] -= 1;
                                    # $lv = ($mKind << $Mons_Kind_Shift) + $HmonsterBHP[$mKind] + random($HmonsterDHP[$mKind]);
                                    $mlv = ($nigekaiju << $Mons_Kind_Shift)
                                         + $HmonsterBHP[$nigekaiju] + random($HmonsterDHP[$nigekaiju]);

                                    my ($mval2) = 0;
                                    $land->[$sx][$sy] = $HlandMonster;
                                    $landValue->[$sx][$sy] = $mlv;
                                    $landValue2->[$sx][$sy] = $mval2;
                                    $landValue3->[$sx][$sy] = 0;
                                    $island->{'monsterlive'}++;

                                    my ($mKind, $mName, $mHp) = monsterSpec($mlv);
                                    logNige2($id, $name, landName($la_Kind, $mlv, $mval2), $mName, "($x, $y)");
                                    Write_ZooState($island , $nigekaiju , $mons_list[$nigekaiju] );
                                    last;
                                }
                            }
                        }
                    }

                    if ($nigeflag < 1) {
                        $mlv = ($nigekaiju << $Mons_Kind_Shift)
                            + $HmonsterBHP[$nigekaiju] + random($HmonsterDHP[$nigekaiju]);

                        # どこに現れるか決める
                        my ($bx, $by, $i ,$la_Kind);

                        for ($i = 0; $i < $HpointNumber; $i++) {
                            $bx = $Hrpx[$i];
                            $by = $Hrpy[$i];

                            $la_Kind = $land->[$bx][$by];

                            if (   ($la_Kind == $HlandWaste)
                                || ($la_Kind == $HlandPlains) 
                                || ($la_Kind == $HlandTown)
                                || ($la_Kind == $HlandForest)
                                || ($la_Kind == $HlandFarm)
                                || ($la_Kind == $HlandFactory)
                                || ($la_Kind == $HlandHaribote)
                                || ($la_Kind == $HlandNewtown)
                                                                 ) {

                                # 地形名
                                my($lName) = landName($la_Kind, $landValue->[$bx][$by],$landValue2->[$bx][$by]);

                                # そのヘックスを怪獣に
                                $land->[$bx][$by] = $HlandMonster;
                                $landValue->[$bx][$by] = $mlv;
                                $landValue2->[$bx][$by] = 0;
                                $landValue3->[$bx][$by] = 0;
                                $island->{'monsterlive'}++;

                                $mons_list[$nigekaiju] -= 1;
                                Write_ZooState($island , $nigekaiju , $mons_list[$nigekaiju]);

                                # 怪獣情報
                                my($mKind, $mName, $mHp) = monsterSpec($mlv);

                                # メッセージ
                                logMonsCome($id, $name, $mName, "($bx, $by)", $lName);
                                last;
                            }
                        }
                    }
                }
                return 0;

            }
            else {
                my ($zlv);
                my ($first);
                my ($safe2) = 0 ;

                # 目的の場所を動物園に
                $zlv = 10 + $island->{'zoo_capacity'};
                $land->[$x][$y] = $HlandZoo;
                $landValue->[$x][$y] = 10; # 規模 = 10000人
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

                my ($zookazu, $zookazus, $m_syurui) = Get_ZooState($island);

                $first = 1;
                while((random(4) != 0) || ($first == 1)) {

                    # 繰り返し注文のため、ここで zoo取得
                    $tmp = $island->{'zoo'};
                    chomp($tmp);
                    @mons_list = split(/\,/,$tmp);

                    # 仕入れる怪獣選択
                    my ($flag , $monster , $plus);
                    my ($siire);
                    my ($safe);

                    # 仕入れる怪獣選択
                    if ($island->{'taiji'}) {

                        $safe = 0;
                        # 繰り返し
                        while (1) {

                            $flag = 0;
                            $siire = random($#HmonsterName);    # すべての怪獣から

                            if (random(100) < $HmonsterZoo[$siire]) {
                                $flag = GetTaijiFlag($island , $siire);

                                if ($flag) {
                                    last;
                                }
                            }

                            $safe++;

                            if ($safe > 30) {
                                # 繰り返しが 30超えたら いのら固定
                                $siire = 1;
                                last;
                            }
                        }
                    }
                    else {
                        # 怪獣倒したことないなら、いのら固定
                        $siire = 1;
                    }

                    # 新規建設時は、まだ飼えるかだけ。
                    if (   ($zlv > $zookazu)            # 怪獣がまだ飼えるかどうか。
                                                    ) {

                        $plus = ($mons_list[$siire]) ? ($mons_list[$siire] + 1) : 1 ;
                        logSiire($id, $name, landName($HlandZoo, 1,0), "$HmonsterName[$siire]", "($x, $y)");
                        Write_ZooState($island , $siire , $plus );
                        $first = 0;
                    }
                    else{
                        last;
                    }

                    $safe2++;
                    if ($safe2 > 30) {
                        # 繰り返しが 30超えたら いのら固定
                        last;
                    }
                }
            }

        } elsif($kind == $HcomFire) {
            # 消防署建設
            $land->[$x][$y] = $HlandFiredept;
            $landValue->[$x][$y] = 0;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomNursery) {
            # 養殖場
            if ($landKind == $HlandNursery) {
                # すでに養殖場の場合
                $landValue->[$x][$y] += $HNursery_add; # 規模 + 5000人
                $landValue->[$x][$y] = $HNursery_limit if($landValue->[$x][$y] > $HNursery_limit); # 最大 100000人
            } elsif(($landKind == $HlandSea) && $lv) {
                # 目的の場所を養殖場に
                $land->[$x][$y] = $HlandNursery;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                $landValue->[$x][$y] = $HNursery_base; # 規模 = 20000人
            }
            else {
                # 不適当な地形
                logLandFail($id, $name, $comName, $landName, $point);
                return 0;
            }
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomKyujo) {
            # 野球場
            $land->[$x][$y] = $HlandKyujo;
            $landValue->[$x][$y] = 0;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomNewtown) {
            # ニュータウン
            my($pop);
            if ( $land->[$x][$y] == $HlandTown ) {
                $pop = $landValue->[$x][$y];
            }
            else {
                $pop = 1;
            }
            $land->[$x][$y] = $HlandNewtown;
            $landValue->[$x][$y] = $pop;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomRizort) {
            # 目的の場所をリゾートにする
            $land->[$x][$y] = $HlandRizort;
            $landValue->[$x][$y] = 1;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomUmiamu) {
            # 海あみゅ
            if ($landKind == $HlandUmiamu) {
                # すでに海あみゅの場合
                $landValue->[$x][$y] += $HUmiamu_add; # 規模 + 30000人
                $landValue->[$x][$y] = $HUmiamu_limit if($landValue->[$x][$y] > $HUmiamu_limit); # 最大 1000000人
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

            }
            elsif(($landKind == $HlandSea) && !$lv) {
                # 海なら、目的の場所を海あみゅに
                $land->[$x][$y] = $HlandUmiamu;
                $landValue->[$x][$y] = $HUmiamu_base; # 規模 = 50000人
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                $island->{'amu'}++;

            }
            else {
                # 不適当な地形
                logLandFail($id, $name, $comName, $landName, $point);
                return 0;
            }
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomFarm) {
            # 農場
            if($landKind == $HlandFarm) {
                # すでに農場の場合
                $landValue->[$x][$y] += $HFarm_add; # 規模 + 2000人
                $landValue->[$x][$y] = $HFarm_limit if($landValue->[$x][$y] > $HFarm_limit); # 最大 50000人

            } else {
                # 目的の場所を農場に
                $land->[$x][$y] = $HlandFarm;
                $landValue->[$x][$y] = $HFarm_base; # 規模 = 10000人
                if ($landKind == $HlandForest) {
                    $landValue2->[$x][$y] = 1;
                } elsif($landKind == $HlandSunahama) {
                    $landValue2->[$x][$y] = 2;
                }else{
                    $landValue2->[$x][$y] = 0;
                }
                $landValue3->[$x][$y] = 0;
            }
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomFoodim) {
            # 食物研究所
            if($landKind == $HlandFoodim) {
                # すでに食物研究所の場合
                $landValue->[$x][$y] += $HFoodim_add; # 規模 + 10000人
                $landValue->[$x][$y] = $HFoodim_limit if($landValue->[$x][$y] > $HFoodim_limit); # 最大 500000人
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

            } else {
                # 目的の場所を食物研究所に
                $land->[$x][$y] = $HlandFoodim;
                $landValue->[$x][$y] = $HFoodim_base; # 規模 = 30000人
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomCollege) {
            # 大学設置
            my ($col_name);
            if (   ($landKind == $HlandCollege)
                && (   ($lv == 4)
                    || ($lv == 96) )
                                     ) {
                $landValue->[$x][$y] = 100 - $lv;
                logLandSuc($id, $name, $comName, $point);
                return 0;

            } elsif(($landKind == $HlandCollege) && (($lv == 97) || ($lv == 98))) {
                $landValue->[$x][$y] = 195 - $lv;
                logLandSuc($id, $name, $comName, $point);
                return 0;

            } else {
                # 大学建設

                $land->[$x][$y] = $HlandCollege;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                if(random(100) < 30) {
                    $landValue->[$x][$y] = 0;
                    $col_name = '(農業大学)';

                } elsif(random(100) < 30) {
                    $landValue->[$x][$y] = 1;
                    $col_name = '(工業大学)';

                } elsif(random(100) < 15) {
                    $landValue->[$x][$y] = 2;
                    $col_name = '(総合大学)';

                } elsif(random(100) < 15) {
                    $landValue->[$x][$y] = 3;
                    $col_name = '(軍事大学)';

                } elsif(random(100) < 15) {
                    $landValue->[$x][$y] = 4;
                    $col_name = '(生物大学)';

                    if(($island->{'co4'} == 0) && ($island->{'co99'} == 0) && ($island->{'c28'} == 0)) {
                        $island->{'eisei5'} = "3,5,5,5,0,0,0";
                    }

                } else {
                    $landValue->[$x][$y] = 5;
                    $col_name = '(気象大学)';

                }
            }
            my($comLog);

            $comLog = "${comName}${col_name}";
            logLandSuc($id, $name, $comLog, $point);

        } elsif($kind == $HcomFarmcpc) {
            # 牧場
            $arg = 1 if(($arg >= 4) || ($arg == 0));
            my @ltmp = ($HlandFarmchi, $HlandFarmpic, $HlandFarmcow);
            my @mtmp = (10, 20, 50);
            my($l, $flag);
            $flag = 0;
            foreach $l (@ltmp) {
                if($landKind == $l) {
                    $island->{'money'} += $lv * $mtmp[$flag];
                    last;
                }
                $flag++;
            }
            if($flag == 3){
                # コストチェック
                my $value = $arg * $cost;
                if($island->{'money'} < $value) {
                    logNoAny($id, $name, $comName, "資金不足の");
                    return 0;
                }
                $land->[$x][$y] = $ltmp[$arg - 1];
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                $island->{'money'} -= $value;
            }
            $landValue->[$x][$y] = 1;
            logLandSuc($id, $name, $comName, $point);
            if($flag == 3){
                return 1;
            } else {
                return 0;
            }

        } elsif($kind == $HcomDbase) {
            # 防衛施設
            # 目的の場所を防衛施設に
            $land->[$x][$y] = $HlandDefence;
            $landValue->[$x][$y] = 0;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomYakusho) {
            my($shutoCount) = countAround($land, $x, $y, 7, $HlandShuto, $HlandUmishuto);

            if(   ($island->{'shu'} == 0)
               || ($shutoCount == 0)
               || ($island->{'yaku'} > 0) ) {
                logLandFail2($id, $name, $comName, $point, "条件を満たしていない<B>$landName</B>の");
                return 0;
            }
            $land->[$x][$y] = $HlandYakusho;                    # 役所にする
            $island->{'yaku_work'} |= $HYakushoWorkExist;       # 役所が存在
            $island->{'yaku_work'} |= $HYakushoWorkYotei;       # 予定地確保をON
            $landValue->[$x][$y] = 1;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomMine) {
            # 地雷設置
            $arg = 1 if($arg == 0);
            $arg = $HMine_limit if($arg > $HMine_limit);
            $arg = min($arg, int($island->{'money'} / $cost));
            $cost *= $arg;
            $land->[$x][$y] = $HlandMine;

            $landValue->[$x][$y] = $arg;
            $landValue->[$x][$y] |= $Hmine_SEA_FLAG if($landKind == $HlandSea);
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logPBSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomHaribote) {

            if (   ($arg >= $HTrainBase)
                && ($arg <= $HTrainMAX) ) {

                $land->[$x][$y] = $HlandTrain;
                $landValue->[$x][$y] = $arg;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                logLandSuc($id, $name, "線路建設", $point);

            }
            else {
                # ハリボテ
                $land->[$x][$y] = $HlandHaribote;
                $landValue->[$x][$y] = 0;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                logHariSuc($id, $name, $comName, $HcomName[$HcomDbase], $point);
            }

        } elsif ($kind == $HcomMonument) {
            # 記念碑
            if ($landKind == $HlandMonument) {
                return 0 if (!$HuseBigMissile);
                # すでに記念碑の場合
                # ターゲット取得
                my ($tn) = $HidToNumber{$target};
                # ターゲットがすでにない場合、何も言わずに中止
                return 0 unless(defined $tn);

                my ($aId, %amityFlag);
                foreach $aId (@{$island->{'allyId'}}) {
                    foreach (@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}) {
                        next if($_ == $id);
                        $amityFlag{$_} = $HcampAtk;
                    }
                }
                # 開発期間ならコマンドを無視
                if ($HarmisticeTurn && ($HislandTurn <= $HarmisticeTurn || $amityFlag{$target})) {
                    # 攻撃が許可されていない
                    logNotAvail($id, $name, $comName);
                    return 0;
                }

                my ($tIsland) = $Hislands[$tn];
                # 自島の人口が少ないか、目標島の人口が少ないかBattleFieldなら、実行は許可されない
                if (   ($tIsland->{'id'} != $id)
                    && (   ($island->{'pop'} < $HguardPop)
                        || ($tIsland->{'pop'} < $HguardPop)
                        || ($tIsland->{'id'} > 100) ) ) {
                    logNoAny($id, $name, $comName, "実行が許可されない");
                    return 0;
                }
                $tIsland->{'bigmissile'}++;
                # その場所は荒地に
                SetWasteLand_Normal($island,$x,$y);     # $HlandWaste
                logMonFly($id, $name, $landName, $point);

            } else {

                if ( $arg == 94 ) {
                    # 目的の場所を香取くんに
                    $land->[$x][$y] = $HlandKatorikun;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    logLandSuc($id, $name, "豚の香取くん建設", $point);

                } elsif($arg == 17) {
                    # 目的の場所をロケットに
                    $land->[$x][$y] = $HlandRocket;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    logLandSuc($id, $name, "ロケット建設", $point);

                } elsif($arg == 42) {
                    # 目的の場所を駅に
                    $land->[$x][$y] = $HlandStation;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    logLandSuc($id, $name, "駅建設", $point);

                }else{
                    # 目的の場所を記念碑に
                    $land->[$x][$y] = $HlandMonument;
                    $arg = 0 if($arg >= $HmonumentNumber);
                    $landValue->[$x][$y] = $arg;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    logLandSuc($id, $name, $comName, $point);
                }
            }
        }

        #以上、地上建設系でreturnしてないコマンドをまとめて
        # 金を差し引く
        $island->{'money'} -= $cost;
        # 回数付きなら、コマンドを戻す
        if (    ($kind == $HcomFarm)
            || ($kind == $HcomFoodim)
            || ($kind == $HcomNursery)
            || ($kind == $HcomPark)
            || ($kind == $HcomUmiamu)
            || ($kind == $HcomFactory) ) {

            if ($arg > 1) {
                $arg--;
                slideBack($comArray, 0);
                $comArray->[0] = {
                    'kind' => $kind,
                    'target' => $target,
                    'x' => $x,
                    'y' => $y,
                    'arg' => $arg
                };
            }
        }
        return 1;

    } elsif($kind == $HcomMountain) {
        # 採掘場
        if ($landKind == $HlandMountain) {
            # すでに採掘場の場合
            $landValue->[$x][$y] += $HMountain_add; # 規模 + 5000人
            $landValue->[$x][$y] = $HMountain_limit if($landValue->[$x][$y] > $HMountain_limit); # 最大 200000人
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;

        } elsif($landKind == $HlandGold) {
            # すでに金山の場合
            $landValue->[$x][$y] += $HGold_add; # 規模 + 20000人
            $landValue->[$x][$y] = $HGold_limit if($landValue->[$x][$y] > $HGold_limit); # 最大 200000人
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;

        } else {
            # 不適当な地形
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        logLandSuc($id, $name, $comName, $point);

        if(random(1000) < 9) { # 0.9%で金山に
            my($v) = 1000 + random(4001); # 1000〜5000億の収入
            $island->{'money'} += $v;
            $land->[$x][$y] = $HlandGold;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logGold($id, $name, $comName, $v);

            Sinden_Omaturi($island , 0 , 1001);

            # 神社
            Jinja_Omaturi($island , 0 , 1001);
        }
        # 金を差し引く
        $island->{'money'} -= $cost;
        # 回数つきならコマンドを戻す
        if($arg > 1) {
            $arg--;
            slideBack($comArray, 0);
            $comArray->[0] = {
                'kind' => $kind,
                'target' => $target,
                'x' => $x,
                'y' => $y,
                'arg' => $arg
            };
        }
        return 1;

    } elsif($kind == $HcomHTget) {
        # ハイテク
        if($landKind == $HlandHTFactory) {
            # すでに採掘場の場合
            $landValue->[$x][$y] += $HHTFactory_add; # 規模 + 10000人
            $landValue->[$x][$y] = $HHTFactory_limit if($landValue->[$x][$y] > $HHTFactory_limit); # 最大 500000人
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;

        } elsif($landKind == $HlandFactory) {
            if($lv == $HFactory_limit) {
                $land->[$x][$y] = $HlandHTFactory;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            } else {
                logLandFail2($id, $name, $comName, $point, "条件を満たしていない<B>$landName</B>の");
                return 0;
            }

        } elsif(   ($landKind == $HlandMonument)
                && ($landValue->[$x][$y] == 10)
                                                ) {
            if ( random(2) ) {
                $landValue->[$x][$y] = 72;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

            }else{
                $landValue->[$x][$y] = 73;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }

        } else {
            # 不適当な地形
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        logLandSuc($id, $name, $comName, $point);

        # 金を差し引く
        $island->{'money'} -= $cost;
        if ($arg > 1) {
            $arg--;
            slideBack($comArray, 0);
            $comArray->[0] = {
                'kind' => $kind,
                'target' => $target,
                'x' => $x,
                'y' => $y,
                'arg' => $arg
            };
        }
        return 1;


    } elsif($kind == $HcomBettown) {
        my ($shutoCount) = countAround($land, $x, $y, 7, $HlandShuto, $HlandUmishuto);
        my ($betCount) = countAround($land, $x, $y, 7, $HlandBettown);

        if ($landKind != $HlandBigtown){
            # 不適当な地形
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

        if (($island->{'shu'} > 0) && (($shutoCount > 0) || ($betCount > 1))) {
            $land->[$x][$y] = $HlandBettown;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);
            # 金を差し引く
            $island->{'money'} -= $cost;
            return 1;
        } else {
            logLandFail2($id, $name, $comName, $point, "条件を満たしていない<B>$landName</B>の");
            return 0;
        }

    } elsif ($kind == $HcomKai) {

        if ($landKind == $HlandKyujo) {
            if ( !$island->{'stadiumnum'} ) {
                $island->{'eisei4'} = "1,1,1,0,0,0,0,0,0,0,10";
            }
            $land->[$x][$y] = $HlandKyujokai;
            $landValue->[$x][$y] = 0;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            $island->{'stadiumnum'}++;
            logLandSuc($id, $name, $comName, $point);
            # 金を差し引く
            $island->{'money'} -= $cost;
            return 1;

        } elsif ($landKind == $HlandKyujokai) {
            my ($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $island->{'eisei4'});
            $sto++;
            $std++;
            $stk++;
            $island->{'eisei4'} = "$sto,$std,$stk,$stwin,$stdrow,$stlose,$stwint,$stdrowt,$stloset,$styusho,$stshoka";
            logLandSuc($id, $name, $comName, $point);
            # 金を差し引く
            $island->{'money'} -= $cost;
            if($arg > 1) {
                $arg--;
                slideBack($comArray, 0);
                $comArray->[0] = {
                    'kind' => $kind,
                    'target' => $target,
                    'x' => $x,
                    'y' => $y,
                    'arg' => $arg
                };
            }
            return 1;

        } elsif (($landKind == $HlandFune) && ($lv == 10)) {
            $landValue->[$x][$y] = 19;
            logLandSuc($id, $name, $comName, $point);
            # 金を差し引く
            $island->{'money'} -= $cost;
            return 1;

        } elsif ($landKind == $HlandRizort) {
            my ($seaCount) = countAround($land, $x, $y, 7, @Hseas);
            my ($rizortCount) = countAround($land, $x, $y, 7, $HlandRizort, $HlandBigRizort);
            my ($value);
            $value = $lv+$island->{'eis1'}+$island->{'eis2'}+$island->{'eis3'}+$island->{'eis5'}+int($island->{'fore'}/10)+int($island->{'rena'}/10)-$island->{'monsterlive'}*100;

            if (   ($seaCount > 2)
                && ($value > 500)
                && ($rizortCount > 2) ) {

                $land->[$x][$y] = $HlandBigRizort;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                logLandSuc($id, $name, $comName, $point);
                # 金を差し引く
                $island->{'money'} -= $cost;
                return 1;
            }
            else {
                logLandFail2($id, $name, $comName, $point, "条件を満たしていない<B>$landName</B>の");
                return 0;
            }

        } elsif (   ($landKind == $HlandYakusho)
                 && ($lv < 6) ) {

            $landValue->[$x][$y] ++;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;

            if ($landValue->[$x][$y] == 2) {
                $island->{'yaku_work'} |= $HYakushoWorkSeiti;
            }
            logLandSuc($id, $name, $comName, $point);
            # 金を差し引く
            $island->{'money'} -= $cost;
            if ($arg > 1) {
                $arg--;
                slideBack($comArray, 0);
                $comArray->[0] = {
                    'kind' => $kind,
                    'target' => $target,
                    'x' => $x,
                    'y' => $y,
                    'arg' => $arg
                };
            }
            return 1;
        }
        elsif ($landKind == $HlandDefence) {

            my ($deflv , $defHP) = GetDefenceSpec($landValue->[$x][$y]);

            if ( $deflv == 0 ) {

                $landValue->[$x][$y] = 1;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }
            elsif ($deflv == 1) {

                $landValue->[$x][$y] = 82;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }
            elsif ($deflv == 2) {

                if ( $defHP < 10 ) {
                    $defHP += 2;
                    $defHP = 10 if ( $defHP > 10 );
                    $landValue->[$x][$y] = 2 + ($defHP << $HDefenceHP_SHIFT);
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;

                }else{
                    # 不適当な地形
                    logLandFail($id, $name, $comName, $landName, $point);
                    return 0;
                }

            }
            logLandSuc($id, $name, $comName, $point);
            # 金を差し引く
            $island->{'money'} -= $cost;
            return 1;

        } elsif($landKind == $HlandHTFactory) {# ハイテク工場
            $land->[$x][$y] = $HlandSHTF;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);
            # 金を差し引く
            $island->{'money'} -= $cost;
            return 1;

        } elsif(   ($landKind == $HlandSunahama)
                && ($lv == 0)  ) {# 砂浜
            $landValue->[$x][$y] = 1;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;

            logLandSuc($id, $name, $comName, $point);
            # 金を差し引く
            $island->{'money'} -= $cost;
            return 1;

        } elsif(   ($landKind == $HlandZoo) ) {     # 動物園  強化

            my ($limit) = 200;
            my ($div) = 75;
            my ($add) = 10;

            $landValue->[$x][$y] += $add;
            if ($landValue->[$x][$y] > int($island->{'rena'}/$div)) {
                $landValue->[$x][$y] = int($island->{'rena'}/$div);
            }

            if ($landValue->[$x][$y] > $limit) {
                $landValue->[$x][$y] = $limit;
            }

            logLandSuc($id, $name, $comName, $point);
            # 金を差し引く
            $island->{'money'} -= $cost;
            if ($arg > 1) {
                $arg--;
                slideBack($comArray, 0);
                $comArray->[0] = {
                    'kind' => $kind,
                    'target' => $target,
                    'x' => $x,
                    'y' => $y,
                    'arg' => $arg
                };
            }
            return 1;

        } elsif (   ($landKind == $HlandPark)
                && ($lv >= $HPark_limit)
                && ($island->{'inoraland'} == 0 ) ) {

            $land->[$x][$y] = $HlandInoraLand;
            $landValue->[$x][$y] = $HPark_limit;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);
            # 金を差し引く
            $island->{'money'} -= $cost;
            return 1;

        } elsif ($landKind == $HlandInoraLand) {

            # いのらランドが成長
            $landValue->[$x][$y] += $HInoraland_add; # 規模++
            $landValue->[$x][$y] = $HInoraland_limit if($landValue->[$x][$y] > $HInoraland_limit); # 最大

            logLandSuc($id, $name, $comName, $point);
            # 金を差し引く
            $island->{'money'} -= $cost;
            if ($arg > 1) {
                $arg--;
                slideBack($comArray, 0);
                $comArray->[0] = {
                    'kind' => $kind,
                    'target' => $target,
                    'x' => $x,
                    'y' => $y,
                    'arg' => $arg
                };
            }
            return 1;

        } elsif(   ($landKind == $HlandTown)
                && ($lv <= $HInaka_limit)
                                            ) {
            # いなか
            $land->[$x][$y] = $HlandInaka;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);
            # 金を差し引く
            $island->{'money'} -= $cost;

        } else {
            # 不適当な地形
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

    } elsif ($kind == $HcomSbase) {
        # 海底基地
        unless (($landKind == $HlandSea) && !$lv){
            # 海以外には作れない
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        $land->[$x][$y] = $HlandSbase;
        $landValue->[$x][$y] = 0;                   # 経験値0
        $landValue2->[$x][$y] = 0;
        $landValue3->[$x][$y] = 0;
        logLandSuc($id, $name, $comName, '(?, ?)');
        # 金を差し引く
        $island->{'money'} -= $cost;
        return 1;

    } elsif ($kind == $HcomSeacity) {
        # 海底都市
        if (($landKind != $HlandSea) || $lv) {
            # 海以外には作れない
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        $land->[$x][$y] = $HlandSeacity;
        $landValue->[$x][$y] = 0;           # 人口0
        $landValue2->[$x][$y] = 0;
        $landValue3->[$x][$y] = 0;
        logLandSuc($id, $name, $comName, '(?, ?)');
        # 金を差し引く
        $island->{'money'} -= $cost;
        return 1;

    } elsif($kind == $HcomProcity) {
        # 防災化
        if(($landKind != $HlandTown) || ($lv < 100)){
            # １万人都市以外には作れない
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        $land->[$x][$y] = $HlandProcity;
        $landValue->[$x][$y] = 100; # 人口10000
        $landValue2->[$x][$y] = 0;
        $landValue3->[$x][$y] = 0;
        logLandSuc($id, $name, $comName, $point);
        # 金を差し引く
        $island->{'money'} -= $cost;
        return 1;

    } elsif ($kind == $HcomBigtown) {
        # 現代化
        if ( ($landKind != $HlandNewtown) || ($lv < 150) ||
             (countAround($land, $x, $y, 19, @Htowns) < 16) ) {
            # 15000人以上のニュータウンでないと作れない
            # 周りの都市の個数が少ないと建設不能
            logLandFail2($id, $name, $comName, $point, "条件を満たしていない<B>$landName</B>の");
            return 0;
        }
        $land->[$x][$y] = $HlandBigtown;
        $landValue2->[$x][$y] = 0;
        $landValue3->[$x][$y] = 0;
        logLandSuc($id, $name, $comName, $point);
        # 金を差し引く
        $island->{'money'} -= $cost;
        return 1;

    } elsif($kind == $HcomSeatown) {
        # 海底新都市
        if(   ($landKind != $HlandSeacity)
           || ($lv < 200)
           || (countAround($land, $x, $y, 19, @Htowns) < 16)){
            # 20000人以上の海底都市でないと作れない
            # 周りの都市の個数が少ないと建設不能
            logLandFail2($id, $name, $comName, '(?, ?)', "条件を満たしていない<B>$landName</B>の");
            return 0;
        }
        $land->[$x][$y] = $HlandSeatown;
        $landValue2->[$x][$y] = 0;
        $landValue3->[$x][$y] = 0;
        logLandSuc($id, $name, $comName, '(?, ?)');
        # 金を差し引く
        $island->{'money'} -= $cost;
        return 1;

    } elsif($kind == $HcomBoku) {
        # 僕の引越し
        my($towncount) = countAround($land, $x, $y, 19, $HlandTown,$HlandNewtown);
        my($pop_limit);
        if(   (!$towncount)
           || (   ($landKind != $HlandProcity)
               && ($landKind != $HlandShuto)
               && ($landKind != $HlandUmishuto)
                                                )  ) {
            # 防災都市以外では実行不能
            # 周りに都市がないと実行不能
            if (!$towncount) {
                logLandFail2($id, $name, $comName, $point, "条件(周囲の都市数)を満たした都市でなかった");
            }else{
                logLandFail2($id, $name, $comName, $point, "条件を満たした都市でなかった");
            }
            return 0;
        }
        $landValue->[$x][$y] += int(10 * ($towncount / 2) ); # 規模 + 1000人

        $pop_limit = $HProcity_limit if($landKind == $HlandProcity);
        $pop_limit = $HShuto_limit if(($landKind == $HlandShuto) || ($landKind == $HlandUmishuto));

        $landValue->[$x][$y] = $pop_limit if($landValue->[$x][$y] > $pop_limit);
        my($i,$sx,$sy);

        for($i = 1; $i < 19; $i++) {

            $sx = $x + $ax[$i];
            $sy = $y + $ay[$i];

            if(   ($land->[$sx][$sy] == $HlandTown)
               || ($land->[$sx][$sy] == $HlandNewtown) ){
                $landValue->[$sx][$sy] -= int(20 / $towncount);
                if($landValue->[$sx][$sy] <= 0) {
                    # 平地に戻す
                    $land->[$sx][$sy] = $HlandPlains;
                    $landValue->[$sx][$sy] = 0;
                    next;
                }
            }
        }

        logLandSuc($id, $name, $comName, $point);
        # 金を差し引く
        $island->{'money'} -= $cost;
        # 回数つきならコマンドを戻す
        if($arg > 1) {
            $arg--;
            slideBack($comArray, 0);
            $comArray->[0] = {
                'kind' => $kind,
                'target' => $target,
                'x' => $x,
                'y' => $y,
                'arg' => $arg
                };
        }
        return 1;

    } elsif($kind == $HcomBoku2) {  # 僕の引越し2

        # 怪獣はキャンセル
        if($landKind == $HlandMonster) {
            my($mKind, $mName, $mHp) = monsterSpec($landValue->[$x][$y]);
            logBokuFail2($id, $name, $comName, $mName, $point);
            return 0;
        }

        # すでに場所指定済み
        if (($island->{'stockflag'} == 55)) {

            if (   ($landKind == $HlandPlains)
                || ($landKind == $HlandSea)
                                            ) {

                # 通常の引っ越し
                my($bck,$sx,$sy);
                $bck = $island->{'pointb'};
                # メッセージから x y を取得
                if($bck =~ s/\((.*),(.*)\)〜$//g) {
                    $sx = int($1);
                    $sy = int($2);
                }

                $island->{'pointb'} .= "($x, $y)";
                $land->[$x][$y] = $island->{'stocklandkind'};
                $landValue->[$x][$y] = $island->{'stocklandvalue'};
                $landValue2->[$x][$y] = $island->{'stocklandvalue2'};
                $landValue3->[$x][$y] = $island->{'stocklandvalue3'};

                $island->{'money'} -= $cost;

                logLandSuc($id, $name, $comName, $island->{'pointb'});

                # 元の位置を平地にする
                $land->[$sx][$sy] = $HlandPlains;
                $landValue->[$sx][$sy] = 0;
                $island->{'stockflag'} = 0;         #引越済み
                return 1;

            }elsif(   ($landKind == $HlandFrocity)                  # 海都市作成
                   && ($island->{'stocklandkind'} == $HlandBettown)
                   && ($island->{'stocklandvalue'} >= 1000 ) ){
                my($bck,$sx,$sy);
                $bck = $island->{'pointb'};
                # メッセージから x y を取得
                if($bck =~ s/\((.*),(.*)\)〜$//g) {
                    $sx = int($1);
                    $sy = int($2);
                }

                $island->{'pointb'} .= "($x, $y)";
                $land->[$x][$y] = $HlandUmicity;
                $landValue->[$x][$y] += $island->{'stocklandvalue'};
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

                $island->{'money'} -= $cost;

                logLandSuc($id, $name, $comName, $island->{'pointb'});

                # 元の位置を平地にする
                $land->[$sx][$sy] = $HlandPlains;
                $landValue->[$sx][$sy] = 0;
                $landValue2->[$sx][$sy] = 0;
                $landValue3->[$sx][$sy] = 0;
                $island->{'stockflag'} = 0;         #引越済み
                return 1;

            }elsif(   ($landKind == $HlandOil)                      # 油田都市作成
                   && ($island->{'stocklandkind'} == $HlandBettown)
                   && ($island->{'stocklandvalue'} >= 1000 ) ){

                my($bck,$sx,$sy);
                $bck = $island->{'pointb'};
                # メッセージから x y を取得
                if($bck =~ s/\((.*),(.*)\)〜$//g) {
                    $sx = int($1);
                    $sy = int($2);
                }

                $island->{'pointb'} .= "($x, $y)";
                $land->[$x][$y] = $HlandOilCity;
                $landValue->[$x][$y] = $island->{'stocklandvalue'};
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

                $island->{'money'} -= $cost;

                logLandSuc($id, $name, $comName, $island->{'pointb'});

                # 元の位置を平地にする
                $land->[$sx][$sy] = $HlandPlains;
                $landValue->[$sx][$sy] = 0;
                $landValue2->[$sx][$sy] = 0;
                $landValue3->[$sx][$sy] = 0;
                $island->{'stockflag'} = 0;         #引越済み
                return 1;

            }
            elsif (   ($landKind == $HlandMountain)                  # ゆめをみるしま
                #   && ($lv == 0)
                   && (0)# ガードで無効
                   && ($island->{'stocklandkind'} == $HlandEgg) ){
                my($bck,$sx,$sy);
                $bck = $island->{'pointb'};
                # メッセージから x y を取得
                if($bck =~ s/\((.*),(.*)\)〜$//g) {
                    $sx = int($1);
                    $sy = int($2);
                }

                $island->{'pointb'} .= "($x, $y)";
                $land->[$x][$y] = $HlandMonument;
                $landValue->[$x][$y] += $island->{'stocklandvalue'};
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

                $island->{'money'} -= $cost;

                logLandSuc($id, $name, $comName, $island->{'pointb'});

                # 元の位置を平地にする
                $land->[$sx][$sy] = $HlandPlains;
                $landValue->[$sx][$sy] = 0;
                $landValue2->[$sx][$sy] = 0;
                $landValue3->[$sx][$sy] = 0;
                $island->{'stockflag'} = 0;         #引越済み
                return 1;

            }elsif(   ($landKind == $HlandWaste)                        # ご神体作成
                   && ($lv == 2)                                        # 隕石あと
                   && ($island->{'stocklandkind'} == $HlandMonument)    # 聖樹
                   && ($island->{'stocklandvalue'} == 1 )               # 聖樹
                                                            ){

                # 神社を探す
                my ($i,$cx,$cy);
                my ($check);
                $check = 0;
                for($i = 1; $i < 7; $i++) {

                    $cx = $x + $ax[$i];
                    $cy = $y + $ay[$i];

                    # 神社を探す
                    if(   ($land->[$cx][$cy] == $HlandMonument)
                       && ($landValue->[$cx][$cy] == 27) ){
                        $check = 1;
                        last;
                    }
                }

                if ($check == 1) {

                    my($bck,$sx,$sy);
                    $bck = $island->{'pointb'};
                    # メッセージから x y を取得
                    if($bck =~ s/\((.*),(.*)\)〜$//g) {
                        $sx = int($1);
                        $sy = int($2);
                    }

                    $island->{'pointb'} .= "($x, $y)";
                    $land->[$x][$y] = $HlandMonument;
                    $landValue->[$x][$y] = 96;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;

                    $island->{'money'} -= $cost;

                    logLandSuc($id, $name, $comName, $island->{'pointb'});

                    # 元の位置を平地にする
                    $land->[$sx][$sy] = $HlandPlains;
                    $landValue->[$sx][$sy] = 0;
                    $island->{'stockflag'} = 0;         #引越済み
                    return 1;

                } else {
                    # 適さない
                    my ($tmp_point);
                    $tmp_point = $island->{'pointb'};
                    $tmp_point .= "($x, $y)";
                    logLandFail($id, $name, $comName, $landName, $tmp_point);
                    return 0;
                }

            }
            else {
                # 適さない
                my($tmp_point);
                $tmp_point = $island->{'pointb'};
                $tmp_point .= "($x, $y)";
                logLandFail($id, $name, $comName, $landName, $tmp_point);
                return 0;
            }

        } else {

            $island->{'stocklandkind'} = $land->[$x][$y];
            $island->{'stocklandvalue'} = $landValue->[$x][$y];
            $island->{'stocklandvalue2'} = $landValue2->[$x][$y];
            $island->{'stocklandvalue3'} = $landValue3->[$x][$y];
            $island->{'pointb'} = "($x, $y)〜";
            $island->{'stockflag'} = 55;
            return 0;
        }

    }
    elsif($kind == $HcomHouse) {
        # 島主の家
        if($island->{'hou'} > 0) {
            # 税率変更
            $island->{'eisei1'} = $arg;
            logLandSuc($id, $name, $comName, $point);
            return 0;
        } else {
            if(($landKind != $HlandPlains) && ($landKind != $HlandTown)) {
                # 不適当な地形
                logLandFail($id, $name, $comName, $landName, $point);
                return 0;
            } else {
                $arg = 5 if(!$arg);
                $island->{'eisei1'} = $arg;
                $land->[$x][$y] = $HlandHouse;
                my $hlv;
                foreach (0..9) {
                    $hlv = 9 - $_;
                    last if($island->{'pts'} > $HouseLevel[$hlv]);
                }
                $landValue->[$x][$y] = $hlv;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                logLandSuc($id, $name, $comName, $point);
                # 金を差し引く
                $island->{'money'} -= $cost;
                return 1;
            }
        }

    }
    elsif ($kind == $HcomEisei) {
        # 人工衛星打ち上げ
        $arg = 1 if(($arg > 6) || !$arg);
        my $value = $arg * $cost;
        #             気象, 観測, 迎撃, 軍事, 防衛, イレ
        my @rocket = (   1,   1,   2,   3,    4, 10);
        my @tech   = (  10,  40, 100, 250, 1000, 2000);
        my @failp  = ( 700, 500, 600, 400,  200, 3000);
        my @failq  = ( 100, 100 , 10,  10,   10, 1);

        if($island->{'m17'} < $rocket[$arg - 1]) { # ロケットが$rocket以上ないとダメ
            logNoAny($id, $name, $comName, "ロケットが足りない");
            return 0;
        } elsif($island->{'rena'} < $tech[$arg - 1]) { # 軍事技術Lv$tech以上ないとダメ
            logNoAny($id, $name, $comName, "軍事技術が足りない");
            return 0;
        } elsif($island->{'money'} < $value) {
            logNoAny($id, $name, $comName, "資金不足の");
            return 0;
        } elsif(random(10000) > $failp[$arg - 1] + $failq[$arg - 1] * $island->{'rena'}) {
            logEiseifail($id, $name, $comName, $point);
            # 金を差し引く
            $island->{'money'} -= $value;
            $HSpace_Debris += $HRocketMiss_SpaceDebri;
            return 1;
        }
        my $nkind = 'eis' . $arg;
        $island->{$nkind} = ($arg == 6) ? 250 : 100;
        logPropaganda($id, $name, $comName);
        # 金を差し引く
        $island->{'money'} -= $value;
        $HSpace_Debris += $HRocket_SpaceDebri;
        return 1;

        # 人工衛星修復
    } elsif($kind == $HcomEiseimente) {
        if ($island->{'m17'} > 0) {
            $arg = 1 if(($arg > 5) || !$arg);
            my $nkind = 'eis' . $arg;
            if($island->{$nkind}) {
                $island->{$nkind} = 150;
                logPropaganda($id, $name, $comName);
            } else {
                logNoAny($id, $name, $comName, "指定の人工衛星がない");
                return 0;
            }
            # 金を差し引く
            $island->{'money'} -= $cost;
            $HSpace_Debris += $HRocket_SpaceDebri;
            return 1;
        }else{

            logNoAny($id, $name, $comName, "ロケットが足りない");
            return 0;
        }

        # 衛星破壊砲
    } elsif($kind == $HcomEiseiAtt) {
        my ($aId, %amityFlag);
        foreach $aId (@{$island->{'allyId'}}) {
            foreach (@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}) {
                next if($_ == $id);
                $amityFlag{$_} = $HcampAtk;
            }
        }
        # 開発期間ならコマンドを無視
        if ($HarmisticeTurn && ($HislandTurn <= $HarmisticeTurn || $amityFlag{$target})) {
            # 攻撃が許可されていない
            logNotAvail($id, $name, $comName);
            return 0;
        }
        # ターゲット取得
        my ($tn) = $HidToNumber{$target};
        if ($tn eq '') {
            # ターゲットがすでにない
            logNoAny($id, $name, $comName, "目標の${AfterName}に人が見当たらない");
            return 0;
        }
        # 事前準備
        my ($tIsland) = $Hislands[$tn];
        my ($tName) = islandName($tIsland);

        my ($tkind, $eName, $p, $nkind);
        $arg = 1 if (($arg > 6) || !$arg);
        $tkind = 'eis' . $arg;
        my ($eis6, $eis4) = ($island->{'eis6'}, $island->{'eis4'});

        if ($eis6 || $eis4) { # イレギュラーか軍事衛星がある場合

            $eName = $HeiseiName[$arg];
            $p = ($eis6 >= 1) ? 110 : 70;
            if ($tIsland->{$tkind}) {

                if (random(100) < $p - 10 * $arg) {

                    $tIsland->{$tkind} = 0;
                    $HSpace_Debris += $HRocketBroken_SpaceDebri;
                    logEiseiAtts($id, $target, $name, $tName, $comName, $eName);
                }
                else {
                    logEiseiAttf($id, $target, $name, $tName, $comName, $eName);
                }
            }
            else {
                logNoAny($id, $name, $comName, "指定の人工衛星がない");
                return 0;
            }

            $nkind = ($eis6 >= 1) ? 'eis6' : 'eis4';
            $island->{$nkind} -= 30;
            if ($island->{$nkind} < 1) {
                $island->{$nkind} = 0;
                logEiseiEnd($id, $name, ($eis6 >= 1) ? $HeiseiName[6] : $HeiseiName[4]);
            }
            # 金を差し引く
            $island->{'money'} -= $cost;
            return 1;

        } else { # イレギュラーも軍事衛星もない場合
            logNoAny($id, $name, $comName, "必要な人工衛星がない");
            return 0;
        }

    } elsif($kind == $HcomEiseiLzr) {
        # 衛星レーザー
        my($aId, %amityFlag);
        foreach $aId (@{$island->{'allyId'}}) {
            foreach (@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}) {
                next if($_ == $id);
                $amityFlag{$_} = $HcampAtk;
            }
        }
        # 開発期間ならコマンドを無視
        if ($HarmisticeTurn && ($HislandTurn <= $HarmisticeTurn || $amityFlag{$target})) {
            # 攻撃が許可されていない
            logNotAvail($id, $name, $comName);
            return 0;
        }
        my($tn) = $HidToNumber{$target};
        unless(defined $tn) {
            # ターゲットがすでにない
            logNoAny($id, $name, $comName, "目標の${AfterName}に人が見当たらない");
            return 0;
        }
        # 事前準備
        my ($tIsland) = $Hislands[$tn];
        my ($tName) = islandName($tIsland);
        my ($tLand) = $tIsland->{'land'};
        my ($tLandValue) = $tIsland->{'landValue'};
        my ($tLandValue2) = $tIsland->{'landValue2'};
        my ($tLandValue3) = $tIsland->{'landValue3'};
        # 自島の人口が少ないか、目標島の人口が少ないかBattleFieldなら、実行は許可されない
        if(   ($tIsland->{'id'} != $id)
           && (   ($island->{'pop'} < $HguardPop)
               || ($tIsland->{'pop'} < $HguardPop)
               || ($tIsland->{'id'} >100)  )  ) {
            logNoAny($id, $name, $comName, "実行が許可されない");
            return 0;
        }

        if ($tIsland->{'predelete'}) {
            logNoAny($id, $name, $comName, "実行が許可されない");
            return 0;
        }

        # 着弾点誤差なし
        # 着弾点の地形等算出
        my ($tL) = $tLand->[$x][$y];
        my ($tLv) = $tLandValue->[$x][$y];
        my ($tLv2) = $tLandValue2->[$x][$y];
        my ($tLv3) = $tLandValue3->[$x][$y];
        my ($tLname) = landName($tL, $tLv, $tLv2);
        my ($tPoint) = "($x, $y)";

        my ($eis6, $eis4) = ($island->{'eis6'}, $island->{'eis4'});

        if ($eis6 || $eis4) { # イレギュラーか軍事衛星がある場合

            LazerAttack($island, $tIsland,$x,$y,$comName,'');

            my ($nkind) = ($eis6 > 0) ? 'eis6' : 'eis4';
            $island->{$nkind} -= (($eis6 > 0) ? 5 : 10);
            if ($island->{$nkind} < 1) {
                $island->{$nkind} = 0;
                logEiseiEnd($id, $name, ($eis6 > 0) ? $HeiseiName[6] : $HeiseiName[4]);
            }
            $island->{'money'} -= $cost;
            return 1;
        } else {
            logNoAny($id, $name, $comName, "必要な人工衛星がない");
            return 0;
        }

        # ミサイル系
    }
    elsif (($kind == $HcomMissileNM)  || # 通常ミサイル
           ($kind == $HcomMissilePP)  || # PPミサイル
           ($kind == $HcomMissileSPP) || # SPPミサイル
           ($kind == $HcomMissileST)  || # STミサイル
           ($kind == $HcomMissileSS)  || # 核ミサイル
           ($kind == $HcomMissileLR)  || # 地形隆起弾
           ($kind == $HcomMissileLD)) {  # 陸地破壊弾

        my ($NextCommandNotMissile);
        my ($TurnCost);

        $NextCommandNotMissile = 0;
        $TurnCost = 0;

        my ($aId, %amityFlag);
        foreach $aId (@{$island->{'allyId'}}) {
            foreach (@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}) {
                next if($_ == $id);
                $amityFlag{$_} = $HcampAtk;
            }
        }

        if ($HanyMissileMode){#複数ミサイル発射可能モード
            # 次のコマンドもミサイル系か？
            my ($tempkind);
            $tempkind = $comArray->[0]->{'kind'};
            if (   ($tempkind == $HcomMissileNM)
                || ($tempkind == $HcomMissilePP)
                || ($tempkind == $HcomMissileST)
                || ($tempkind == $HcomMissileSPP)
                || ($tempkind == $HcomMissileLD)
                || ($tempkind == $HcomMissileLR)
                                                ) {
                # ミサイル系
                $NextCommandNotMissile = 0;
            }else{
                $NextCommandNotMissile = 1;
            }
        }else{
            $NextCommandNotMissile = 1;

        }

        # ここで、ミサイル履歴と、次のコマンドがミサイルかどうかを決める。

        $TurnCost = $NextCommandNotMissile & $island->{'missiled'};

        # 開発期間ならコマンドを無視
        if ($HarmisticeTurn && ($HislandTurn <= $HarmisticeTurn || $amityFlag{$target})) {
            # 攻撃が許可されていない
            logNotAvail($id, $name, $comName);
            return $TurnCost;
        }

        # ターゲット取得
        my($tn) = $HidToNumber{$target};
        unless(defined $tn) {
            # ターゲットがすでにない
            logNoAny($id, $name, $comName, "目標の${AfterName}に人が見当たらない");
            return $TurnCost;
        }

        my ($flag) = 0;
        if (   (INIT_USE_ARM_SUPPLY)
            && (!$island->{'army'}) ) {
            logNoAny($id, $name, $comName, "軍事物資がない");
            return $TurnCost;
        }

        if (   (!$arg)
            || (   (INIT_USE_ARM_SUPPLY)
                && ($arg > $island->{'army'}))) {
            # 0、または、軍事物資より多い場合
            $arg = (INIT_USE_ARM_SUPPLY) ? $island->{'army'} : 100;
            # ＲＡはMaxで100発みたいです
        }

        # 事前準備
        my ($tIsland) = $Hislands[$tn];
        my ($tName) = islandName($tIsland);
        my ($tLand) = $tIsland->{'land'};
        my ($tLandValue) = $tIsland->{'landValue'};
        my ($tLandValue2) = $tIsland->{'landValue2'};
        my ($tLandValue3) = $tIsland->{'landValue3'};
        my ($tx, $ty, $err);

        # BattleFieldでなくて、自島の人口が少ないか、目標島の人口が少ないなら、実行は許可されない
        if(   ($tIsland->{'id'} <= 100)
           && ($tIsland->{'BF_Flag'} == 0)
           && ($tIsland->{'id'} != $id)
           && (   ($island->{'pop'} < $HguardPop)
               || ($tIsland->{'pop'} < $HguardPop)) ) {
            logNoAny($id, $name, $comName, "実行が許可されない");
            return $TurnCost;
        }

        if ($tIsland->{'predelete'}) {

            logNoAny($id, $name, $comName, "実行が許可されない");
            return $TurnCost;
        }

        # バトルフィールドへのミサイルチェック
        if ( $tIsland->{'BF_Flag'} ) {
            if ( $island->{'BF_Missile'} >= $HBF_Missile_Limit ) {
                logNoAny($id, $name, $comName, "実行が許可されない(バトルフィールド上限30)");

                return $TurnCost;
            }
        }

        # 誤差
        if($kind == $HcomMissilePP) { # PPミサイル
            $err = 7;
        } elsif($kind == $HcomMissileSS) { # 核ミサイル
            $err = 7;
        } elsif($kind == $HcomMissileSPP) { # SPPミサイル
            $err = 1;
        } else {
            $err = 19;
        }

        # BattleFieldなら、@HkindBFM以外は許可されない
        my $flagBFM = 1;
        foreach (@HkindBFM) {
            if($kind == $_) {
                $flagBFM = 0;
                last;
            }
        }

        if (   ($tIsland->{'id'} > 100)
            || ($tIsland->{'BF_Flag'}) ) {

            if ($flagBFM) {
                logNoAny($id, $name, $comName, "許可されていない種類のミサイルである");
                return $TurnCost;
            }
        }
        elsif(   ($HtargetMonster)
                && ($tIsland->{'id'} != $id)
                && (!countAround($tLand, $x, $y, $err, $HlandMonster, $HlandRottenSea)) ) {
            # 射程内に怪獣・腐海がなければ、発射中止
            logNoTarget($id, $name, $comName);
            return $TurnCost;
        }

        # 難民の数
        my ($boat) = 0;

        my ($mukou, $bouei, $kaijumukou, $kaijuhit, $total, $fuhatu, $alltotal) =
           (0     , 0     , 0          , 0        , 0     , 0      , 0);

        # 金が尽きるか指定数に足りるか基地全部が撃つまでループ
        my ($bx, $by, $count) = (0,0,0);

        while (($arg > 0) && ($island->{'money'} >= $cost)) {
            # 基地を見つけるまでループ
            while($count < $HpointNumber) {
                $bx = $Hrpx[$count];
                $by = $Hrpy[$count];
                last if(($land->[$bx][$by] == $HlandBase) || ($land->[$bx][$by] == $HlandSbase));
                $count++;
            }
            last if($count > $pointNumber); # 見つからなかったらそこまで

            $flag = 1; # 最低一つ基地があったので、flagを立てる

            # 基地のレベルを算出
            my ($missiles) = $island->{'missiles'}->[$bx][$by];
            my ($level) = expToLevel($land->[$bx][$by], $landValue->[$bx][$by]) - $missiles;
            if ($level <= 0) { $count++; next; }; # この基地は全弾発射している

            my ($tid);      # 敵の島ID

            # 基地内でループ
            while (   ($level > 0)
                   && ($arg > 0)
                   && ($island->{'money'} > $cost) ) {

                $tid = $tIsland->{'id'};        #id コピー

                if (random(300) < $alltotal-int($island->{'rena'}/100)) {
                    $level--;
                    $arg--;
                    $island->{'money'} -= $cost;
                    $total++;
                    $alltotal++;
                    $fuhatu++;
                    # 軍事物資を減らす
                    $island->{'army'}-- if($HuseArmSupply);
                    last if (!$level || !$arg || ($island->{'money'} < $cost));
                }

                if ($kind != $HcomMissileST) {
                    $island->{'ext'}[1] += $cost; # 貢献度
                    $island->{'ext'}[6]++; # 発射したミサイルの数
                    if ($HallyNumber) {
                        foreach (@{$island->{'allyId'}}) {
                            $Hally[$HidToAllyNumber{$_}]->{'ext'}[0]++ if ( ($tIsland->{'BF_Flag'} == 0 ) );
                        }
                    }
                }

                if ($HallyNumber) {
                    my ($allyflag) = 0;
                    my ($ai);
                    foreach $ai (@{$island->{'allyId'}}) {
                        foreach (@{$tIsland->{'allyId'}}) {
                            if($_ == $ai) {
                                $allyflag = 1;
                                last;
                            }
                        }
                    }
                    if ($allyflag) {
                        # 味方に撃たれた場合貢献度マイナス(受けたミサイルの数はカウントしない)
                        $tIsland->{'ext'}[1] -= $cost; # 貢献度
                    }
                    else {
                        # 敵に撃たれた場合貢献度プラス
                        $tIsland->{'ext'}[1] += $cost; # 貢献度
                        $tIsland->{'ext'}[5]++; # 受けたミサイルの数
                    }
                    foreach (@{$tIsland->{'allyId'}}) {
                        $Hally[$HidToAllyNumber{$_}]->{'ext'}[1]++ if ( ($tIsland->{'BF_Flag'} == 0 ) );
                    }
                }


                # 撃ったのが確定なので、各値を消耗させる
                $level--;
                $missiles++;
                $arg--;
                $island->{'money'} -= $cost;
                $island->{'missiled'} = 1;
                $total++;
                $alltotal++;
                # 軍事物資を減らす
                $island->{'army'}-- if($HuseArmSupply);


                if ( $tIsland->{'BF_Flag'} ) {
                    if ( $island->{'BF_Missile'} >= $HBF_Missile_Limit ) {
                        logNoAny($id, $name, $comName, "実行が許可されない(バトルフィールド上限$HBF_Missile_Limit)");
                        return 1;

                    }
                    else {
                        $island->{'BF_Missile'} ++ ;
                    }
                }

                # 着弾点算出
                my ($r) = random($err);
                $tx = $x + $ax[$r];
                $ty = $y + $ay[$r];
                $tx-- if((($ty % 2) == 0) && (($y % 2) == 1));

                # 着弾点範囲内外チェック
                if (($tx < 0) || ($tx > $islandSize) || ($ty < 0) || ($ty > $islandSize)) {
                    # 範囲外
                    $mukou++;
                    next;
                }

                if ( !$tIsland->{'BF_Flag'} ) {
                    $tIsland->{'missileAlert'} = 1;
                }

                # 着弾点の地形等算出
                my ($tL) = $tLand->[$tx][$ty];
                my ($tLv) = $tLandValue->[$tx][$ty];
                my ($tLv2) = $tLandValue2->[$tx][$ty];
                my ($tLv3) = $tLandValue3->[$tx][$ty];
                my ($tLname) = landName($tL, $tLv,$tLv2,$tLv3);
                my ($tPoint) = "($tx, $ty)";

                # 防衛施設判定
                my ($defence) = 0;
                my ($defper) = 0;

                if (($HdefenceHex[$tid][$tx][$ty] == 1) && !($HdBaseSelfNoDefence) ) {
                    $defence = 1;
                } elsif ($HdefenceHex[$tid][$tx][$ty] == -1) {
                    $defence = 0;
                } else {

                    if(   (!($HdBaseSelfDefence)) 
                       && (   ($tL == $HlandDefence)
                           || (   ($tL == $HlandProcity)
                               && ($tLv < 160) )
                                                )) {
                        # 防衛施設、防衛都市に命中
                        my($defLv , $defHP ,$defper);

                        $defence = 1;
                        $defHP = 0;
                        $defLv = 0;

                        $defper = -1; # 確実に命中
                        if($tL == $HlandDefence) {
                            # 防衛施設に命中

                            $defLv = ($tLv & $HDefenceLevelMask) ;

                            if ($kind == $HcomMissileSPP) {
                                # SPPミサイル

                                if (   !($HdBaseSelfNoDefence) 
                                    ||  ($id != $tIsland->{'id'}) 
                                                                ) {
                                    $defper = $HdNoPerfectP;
                                    if($HdBaseNoPerfect){

                                        $defper = $HdNoPerfectP;
                                        if ( $defLv >=2 ) {
                                            $defHP = 0;
                                            $defHP = $lv >> $HDefenceHP_SHIFT;
                                            $defper = $defper - ( $defHP * 2);
                                        }
                                    }
                                }
                            }
                        }

                        if (   ($defLv >= 2)
                            && (random(100) < $defper) ) {

                            $defHP = $tLv >> $HDefenceHP_SHIFT;
                            $defHP = $defHP - 4;
                            $defHP = 0 if ( $defHP < 0 );
                            $tLandValue->[$tx][$ty] = $defLv + ( $defHP << $HDefenceHP_SHIFT ) ;
                        }

                        if ( $defHP <= 0 ) {
                            # フラグをクリア
                            $defence = 0;
                            my($i, $count, $sx, $sy);
                            for($i = 0; $i < 19; $i++) {
                                $sx = $tx + $ax[$i];
                                $sy = $ty + $ay[$i];

                                # 行による位置調整
                                $sx-- if(!($sy % 2) && ($ty % 2));
                                # 範囲内の場合
                                $HdefenceHex[$tid][$sx][$sy] = 0 if(($sx >= 0) && ($sx < $HislandSize) && ($sy >= 0) && ($sy < $HislandSize));
                            }
                            if(($tL == $HlandDefence) && ($kind != $HcomMissileST)) {
                                $island->{'ext'}[2]++; # 破壊した防衛施設の数
                            }
                        }

                    } elsif(countAround($tLand, $tx, $ty, 19, $HlandDefence)) {
                        if((!$HdBaseSelfNoDefence) || ($id != $tIsland->{'id'})) {
                            $HdefenceHex[$tid][$tx][$ty] = 1;
                            $defence = 1;
                            #$defence = 0 if($HdBaseNoPerfect && (random(100) < $HdNoPerfectP));
                        }

                    } elsif(countAround($tLand, $tx, $ty, 7, $HlandProcity)) {

                        if(!($HdProcitySelfNoDefence) || ($id != $tIsland->{'id'})) {
                            $HdefenceHex[$tid][$tx][$ty] = 1;
                            $defence = 1;
                            #$defence = 0 if($HdProcityNoPerfect && (random(100) < $HdNoPerfectP));
                        }

                    } elsif(countAround($tLand, $tx, $ty, 1, $HlandHouse)) {
                        $HdefenceHex[$tid][$tx][$ty] = 1;
                        $defence = 1;

                    } elsif(countAround($tLand, $tx, $ty, 7, $HlandShuto)) {
                        if(!($HdProcitySelfNoDefence) || ($id != $tIsland->{'id'})) {
                            $HdefenceHex[$tid][$tx][$ty] = 1;
                            $defence = 1;
                        }
                    } else {
                        $HdefenceHex[$tid][$tx][$ty] = -1;
                        $defence = 0;
                    }
                }

                if($defence == 1) {
                    # 空中爆破
                    $bouei++;
                    $tIsland->{'ext'}[7]++; # 防衛施設で弾いたミサイルの数
                    next;
                }

                if($tIsland->{'eis5'}) { # 防衛衛星がある場合
                    if(random(5000) < $tIsland->{'rena'}) {
                        $tIsland->{'eis5'} -= 2;
                        if($tIsland->{'eis5'} < 1) {
                            $tIsland->{'eis5'} = 0;
                            logEiseiEnd($target, $tName, $HeiseiName[5]);
                        }
                        $bouei++;
                        next;
                    }
                }

                # 「効果なし」hexを最初に判定
                if(($kind != $HcomMissileLR) &&                     # 地形隆起弾でなくて
                    ((($tL == $HlandSea) && ($tLv == 0)) ||         # 深い海
                    ((($tL == $HlandSea)     ||                     # 海または・・・
                      ($tL == $HlandSbase)    ||                      # 海底基地または・・・
                      ($tL == $HlandSeacity) ||                     # 海底都市または・・・
                      ($tL == $HlandSeatown) ||                     # 海底新都市または・・・
                      ($tL == $HlandUmishuto) ||                    # 海首都または・・・
                      ($tL == $HlandUmiamu)  ||                     # 海あみゅまたは・・・
                      ($tL == $HlandGold)    ||                      # 金山または・・・
                      ($tL == $HlandShrine)  ||                     # 時の神殿または・・・
                      ($tL == $HlandMountain))                      # 山で・・・
                     && ($kind != $HcomMissileLD)))){               # 陸破弾でもない

                    # 海底基地、海底都市、海底新都市の場合、海のフリ
                    if(isBehindSea($tL)) {
                        $tL = $HlandSea;
                    }
                    $tLname = landName($tL, $tLv, $tLv2);

                    # 無効化
                    $mukou++;
                    next;
                }

                # 弾の種類で分岐
                if ($kind == $HcomMissileLR) {
                    # 地形隆起弾

                    if (   ($tL == $HlandMountain)
                        || ($tL == $HlandGold)
                        || ($tL == $HlandShrine)
                                                 ) {
                        # 山、時の神殿に着弾した場合無効
                        $mukou++;
                        next;

                    } elsif (   ($tL == $HlandSbase)
                             || ($tL == $HlandSeacity)
                             || ($tL == $HlandSeatown)
                             || ($tL == $HlandUmishuto)
                             || ($tL == $HlandOil)
                             || ($tL == $HlandFune)
                             || ($tL == $HlandFrocity)
                             || ($tL == $HlandUmiamu)
                                                        ) {
                        # 海底基地、海底都市、海底新都市、油田、船、海あみゅなら、目的の場所を浅瀬にする
                        SetSeaShallowLand($tIsland,$tx,$ty);
                        logMsLSbase($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "隆起して浅瀬になりました。");
                        next;

                    } elsif($tL == $HlandRottenSea) {
                        # 腐海なら、目的の場所を山にする
                        SetMountain_Normal($tIsland,$tx,$ty);
                        logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "腐海は隆起し山になりました。");
                        next;

                    } elsif(($tL == $HlandSea) || ($tL == $HlandIce)) {
                        if(($tLv == 1) || ($tL == $HlandIce)){
                            # 浅瀬の場合
                            SetWasteLand_Normal($tIsland,$tx,$ty);     # $HlandWaste
                            $tIsland->{'area'}++;
                            logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "隆起し荒地となりました。");

                            my($seaCount) = countAround($tLand, $tx, $ty, 7, @Hseas);
                            if($seaCount <= 4) {
                            # 周りの海が3ヘックス以内なので、浅瀬にする
                                my($i, $sx, $sy);
                                for($i = 1; $i < 7; $i++) {
                                    $sx = $x + $ax[$i];
                                    $sy = $y + $ay[$i];

                                    # 行による位置調整
                                    $sx-- if(!($sy % 2) && ($y % 2));

                                    if(($sx >= 0) && ($sx < $HislandSize) && ($sy >= 0) && ($sy < $HislandSize) &&
                                        ($tLand->[$sx][$sy] == $HlandSea)) {
                                        # 範囲内の場合
                                        $tLandValue->[$sx][$sy] = 1;
                                    }
                                }
                            }
                            next;

                        } else {
                            # 海なら、目的の場所を浅瀬にする
                            SetSeaShallowLand($tIsland,$tx,$ty);
                            logMsLSbase($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "隆起して浅瀬になりました。");
                            next;
                        }

                    } elsif($tL == $HlandMonster){
                        my($mKind, $mName, $mHp) = monsterSpec($tLv);
                        if (isSeaMonster($mKind)){        # 海の怪獣
                            # 海なら、目的の場所を浅瀬にする
                            SetSeaShallowLand($tIsland,$tx,$ty);
                            logMsLSbase($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "隆起して浅瀬になりました。");
                            next;

                        }else{
                            # 怪獣なら
                            logMsLMonster($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "隆起し山が出来ました。");
                            # 山になる
                            SetMountain_Normal($tIsland,$tx,$ty);
                            next;
                        }
                    } elsif(   ($tL == $HlandTown)
                            || ($tL == $HlandMinato)
                            || ($tL == $HlandNewtown)
                            || ($tL == $HlandOnsen)
                            || ($tL == $HlandBigtown)
                                                        ) {
                        # 都市、港、ニュータウン、現代都市の場合
                        if(($land->[$bx][$by] == $HlandBase) ||
                            ($land->[$bx][$by] == $HlandSbase)) {
                            # 経験値
                            # まだ基地の場合のみ
                            $landValue->[$bx][$by] += int($tLv / 20);
                            $landValue->[$bx][$by] = $HmaxExpPoint if($landValue->[$bx][$by] > $HmaxExpPoint);
                        }
                        logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "隆起し山が出来ました。");
                        # 山になる
                        SetMountain_Normal($tIsland,$tx,$ty);
                        if (random(1000) < 22) {
                            SetMonument_Normal($tIsland,$tx,$ty,75);
                        }
                        next;
                    } else {
                        # その他
                        logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "隆起し山が出来ました。");
                        # 山になる
                        SetMountain_Normal($tIsland,$tx,$ty);
                        if (random(1000) < 22) {
                            SetMonument_Normal($tIsland,$tx,$ty,75);
                        }
                        next;
                    }
                    # 地形隆起弾ここまで

                } elsif($kind == $HcomMissileSS) {
                    # 核ミサイル
                    logMsSS($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint);
                    wideDamageli($target, $tName, $tLand, $tLandValue,$tLandValue2, $tx, $ty);

                } elsif($kind == $HcomMissileLD) {
                    # 陸地破壊弾
                    if (($tL == $HlandMountain) || ($tL == $HlandGold) || ($tL == $HlandShrine) || ($tL == $HlandOnsen)) {
                        # 山(荒地になる)
                        logMsMonster($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "消し飛び、荒地と化しました。");
                        # 荒地になる
                        SetWasteLand_Normal($tIsland,$tx,$ty);
                        next;

                    } elsif(($tL == $HlandSbase)    ||
                            ($tL == $HlandFune)    ||
                            ($tL == $HlandFrocity)  ||
                            ($tL == $HlandUmiamu)  ||
                            ($tL == $HlandSeatown) ||
                            ($tL == $HlandUmishuto) ||
                            ($tL == $HlandSeacity)) {
                        # 海底基地、船、海あみゅ、海底都市、海底新都市
                        logMsLSbase($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "跡形もなく吹き飛びました。");

                    } elsif ($tL == $HlandMonster) {
                        # 怪獣
                        my($mKind, $mName, $mHp) = monsterSpec($tLv);
                        if ($mKind == $Mons_Unbaba){
                            #ウンババには聞かない
                        }else{
                            logMsLMonster($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "水没しました。");
                        }
                    } elsif($tL == $HlandRottenSea) {
                        # 腐海
                        logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "腐海は海に沈みました。");
                    } elsif(($tL == $HlandSea) || ($tL == $HlandIce)) {
                        # 浅瀬
                        logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "海底がえぐられました。");
                    } else {
                        # その他
                        logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "陸地は水没しました。");
                    }

                    if (($tL == $HlandTown)    ||
                        ($tL == $HlandMinato)  ||
                        ($tL == $HlandNewtown) ||
                        ($tL == $HlandBigtown)) {
                        # 都市、港、ニュータウン、現代都市の場合
                        if(($land->[$bx][$by] == $HlandBase) ||
                            ($land->[$bx][$by] == $HlandSbase)) {
                            # 経験値
                            # まだ基地の場合のみ
                            $landValue->[$bx][$by] += int($tLv / 20);
                            $landValue->[$bx][$by] = $HmaxExpPoint if($landValue->[$bx][$by] > $HmaxExpPoint);
                        }
                    }

                    if ( !isSeaMonster($mKind) ){     #海の怪獣でない
                        # 浅瀬になる
                        $tIsland->{'area'}--;
                        SetSeaShallowLand($tIsland,$tx,$ty);
                        # でも油田、浅瀬、海底基地だったら海
                        if(($tL == $HlandOil)     ||
                            ($tL == $HlandSea)     ||
                            ($tL == $HlandSeacity) ||
                            ($tL == $HlandIce) ||
                            ($tL == $HlandSeatown) ||
                            ($tL == $HlandUmishuto)    ||
                            ($tL == $HlandFune)    ||
                            ($tL == $HlandFrocity)  ||
                            ($tL == $HlandUmiamu)  ||
                            ($tL == $HlandSbase)) {
                            SetSeaLand_Normal($tIsland,$tx,$ty);
                        }
                    }
                    # 陸地破壊弾ここまで

                } else {

                    # その他ミサイル
                    if (($tL == $HlandWaste) || ($tL == $HlandYougan)) {
                        $mukou++;

                    } elsif ($tL == $HlandRottenSea) {
                        # 腐海
                        if ($kind == $HcomMissileST) {
                            # ステルス
                            logMsNormalS($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "腐海は焼き払われました。");
                        } else {
                            # 通常
                            logMsNormal($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "腐海は焼き払われました。");
                        }

                    } elsif ($tL == $HlandMonster) {
                        # 怪獣
                        my ($mKind, $mName, $mHp) = monsterSpec($tLv);

                        # 硬化中?
                        if (isMonsterCuring($mKind)) {
                            # 硬化中
                            $kaijumukou++;
                            next;

                        } else {
                            # 硬化中じゃない

                            my ($special) = $HmonsterSpecial[$mKind];
                            my $rflag = random(1000)+$island->{'co4'}*100+$island->{'co99'}*100;
                            if((($special == 5) || ($mKind == 15)) && ($rflag < $HmonsterDefence)){
                                $kaijumukou++;
                                next;

                            } elsif(   ($mKind == $Mons_Mikael   && $rflag < 900)
                                    || ($mKind == $Mons_Ethereal && $rflag < 300)
                                    || ($mKind == $Mons_Satan    && $rflag < 200)
                                    || ($mKind == $Mons_Ice_scorpion && $rflag < 250)
                                    || ($mKind == $Mons_Volgenom && $rflag < 500)
                                    || ($mKind == $Mons_Kisinhei && $rflag < (500))
                                    || ($mKind == $Mons_Retro_inora && $rflag < 100)
                                    || ($mKind == $Mons_Uriel && $rflag < (100+random(400)))
                                    || ($mKind == $Mons_SuperTetra && $rflag < (800+random(50)))
                                    || ($mKind == $Mons_Alfr && $rflag < (400+random(400)))
                                    || ($mKind == $Mons_SlimeLegend && $rflag < 100)
                                    || ($mKind == $Mons_f20 && $rflag < (400+random(500)))
                                                                                            ) {
                                $kaijumukou++;
                                next;
                            }

                            if($mHp == 1) {
                                # 怪獣しとめた
                                if(($land->[$bx][$by] == $HlandBase) ||
                                    ($land->[$bx][$by] == $HlandSbase)) {
                                    # 経験値
                                    $landValue->[$bx][$by] += $HmonsterExp[$mKind];
                                    $landValue->[$bx][$by] = $HmaxExpPoint if($landValue->[$bx][$by] > $HmaxExpPoint);
                                }

                                if($kind == $HcomMissileST) {
                                    # ステルス
                                    logMsMonsterS($id, $target, $name, $tName, $comName, $mName, $point, $tPoint, "力尽き、倒れました。");
                                } else {
                                    # 通常
                                    logMsMonster($id, $target, $name, $tName, $comName, $mName, $point, $tPoint, "力尽き、倒れました。");
                                }

                                if ($mKind == $Mons_Omu) { # オームなら
                                    # 腐海発生
                                    my($point) = "($tx, $ty)";
                                    logRottenSeaBorn($id, $tName, $point);
                                    SetRottenSea($tIsland , $tx , $ty);
                                }

                                if ($mKind != $Mons_Omu) { # オームでない

                                    # 収入
                                    my ($value) = $HmonsterValue[$mKind];

                                    if ($value > 0) {

                                        if (   ( $tIsland->{'id'} <= 100)
                                            && (!$tIsland->{'BF_Flag'})
                                                                        ) {
                                            $tIsland->{'money'} += $value;
                                            logMsMonMoney($target, $mName, $value);

                                        } else {

                                            $island->{'money'} += $value;
                                            $island->{'landscore'} += $HmonsterBHP[$mKind] if ( $kind != $HcomMissileSPP );
                                            logMsMonMoney($id, $mName, $value);
                                        }

                                        if(!$tIsland->{'BF_Flag'}){

                                            Sinden_Omaturi($island , $HmonsterValue[$mKind] , 101);

                                            # 神社
                                            Jinja_Omaturi($island , $HmonsterValue[$mKind] , 101);
                                        }
                                    }
                                }

                                # 怪獣退治
                                TaijiPrize($island , $mKind);

                                next if ($mKind == $Mons_Omu);      # オームはここで終わりにする

                            } else {

                                $island->{'landscore'}++ if ( ($tIsland->{'BF_Flag'} == 1 ) && ( $kind != $HcomMissileSPP ));
                                # 怪獣生きてる
                                $kaijuhit++;
                                # HPが1減る
                                $tLandValue->[$tx][$ty]--;
                                next;
                            }
                        }

                    }
                    else {
                        # 通常地形
                        if ($kind == $HcomMissileST) {
                            # ステルス
                            logMsNormalS($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "一帯が壊滅しました。");
                        }
                        else {
                            # 通常
                            logMsNormal($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "一帯が壊滅しました。");
                            $island->{'ext'}[3]++ if ($tL == $HlandBase); # 撃破したミサイル基地の数
                        }
                    }

                    # 経験値
                    if (   ($tL == $HlandTown)
                        || ($tL == $HlandMinato)
                        || ($tL == $HlandNewtown)
                        || ($tL == $HlandProcity)
                        || ($tL == $HlandBigtown)
                        || ($tL == $HlandBettown)
                                                  ) {

                        if (   ($land->[$bx][$by] == $HlandBase)
                            || ($land->[$bx][$by] == $HlandSbase)  ) {

                            $landValue->[$bx][$by] += int($tLv / 20);
                            $boat += $tLv; # 通常ミサイルなので難民にプラス
                            $landValue->[$bx][$by] = $HmaxExpPoint if($landValue->[$bx][$by] > $HmaxExpPoint);
                        }
                    }

                    my ($mKind, $mName, $mHp) = monsterSpec($tLv);

                    # 荒地になる
                    if ($tL == $HlandMonster) {
                        MonsterDead( $tIsland , $tx , $ty , $mKind , 1 );
                    }else{
                        MonsterDown( $tIsland , $tx , $ty , $mKind , 1 );

                    }

                    if (   ($mKind == 17)
                        && ($tL == $HlandMonster) ) {
                        SetMonument_Normal($tIsland , $tx , $ty , 86);
                    }

                    # 魔法陣
                    if (   ( ($tL == $HlandMonument) && ($tLv == 25) )
                        && (random(10000) < $island->{'rena'}) && ($island->{'rena'} > 2000)
                                                                                            ) {

                        my ($lv2,$lv);
                        ($kind,$lv2) = MonsterSpawnKind($tIsland , 0);
                        $lv = ($kind << $Mons_Kind_Shift) + $HmonsterBHP[$kind] + random($HmonsterDHP[$kind]);
                        $tLand->[$tx][$ty] = $HlandMonster;
                        $tLandValue->[$tx][$ty] = $lv;
                        $tLandValue2->[$tx][$ty] = $lv2;
                        $tLandValue3->[$tx][$ty] = 0;
                        $tIsland->{'monsterlive'}++;
                        # 怪獣情報
                        my($mKind, $mName, $mHp) = monsterSpec($lv);

                        # メッセージ
                        logMonsComemagic($id, $tIsland->{'name'}, $mName, "($bx, $by)", '');
                    }

                    # ゲート
                    if (   ($tLv == 70)
                        && ($tL == $HlandMonument)  ) {

                        SetMonument_Normal($tIsland , $tx , $ty , 70);
                    }

                    # でも油田だったら海
                    if (   ($tL == $HlandOil)
                        || ($tL == $HlandFrocity)
                        || ($tL == $HlandUmicity)
                        || ($tL == $HlandOilCity)
                        || ($tL == $HlandFune) ) {

                        $tLand->[$tx][$ty] = $HlandSea;
                        $tLandValue->[$tx][$ty] = 0;

                    } elsif(($tL == $HlandNursery) || ($tL == $HlandIce)) {
                        # でも養殖場なら浅瀬
                        $tLand->[$tx][$ty] = $HlandSea;
                        $tLandValue->[$tx][$ty] = 1;
                    } elsif($tL == $HlandOnsen) {
                        # でも温泉なら山
                        $tLand->[$tx][$ty] = $HlandMountain;
                        $tLandValue->[$tx][$ty] = 0;
                    }
                }
            }

            # この基地のミサイル発射数を記憶する
            $island->{'missiles'}->[$bx][$by] = $missiles;
            # カウント増やしとく
            $count++;
        }

        # ログ
        if ($kind == $HcomMissileST) {
            # ステルス
            logMsTotalS($id, $target, $name, $tName, $comName, '', $point, $tPoint, $total, $mukou, $bouei, $kaijumukou, $kaijuhit, $fuhatu);
        } else {
            # 通常
            logMsTotal($id, $target, $name, $tName, $comName, '', $point, $tPoint, $total, $mukou, $bouei, $kaijumukou, $kaijuhit, $fuhatu);
        }

        if (!$flag) {
            # 基地が一つも無かった場合
            logMsNoBase($id, $name, $comName);
            return 0;
        }

        # 難民判定
        $boat = int($boat / 2);
        if ($boat && ($id != $target) && ($kind != $HcomMissileST)) {
            # 難民漂着
            my($achive); # 到達難民
            my($i);
            my($pop_limit);
            $achive = 0;

            for($i = 0; ($i < $HpointNumber && $boat > 0); $i++) {
                $bx = $Hrpx[$i];
                $by = $Hrpy[$i];

                if (   ($land->[$bx][$by] == $HlandTown)
                    || ($land->[$bx][$by] == $HlandNewtown)
                    || (($land->[$bx][$by] == $HlandBigtown) && ($island->{'yaku'} >= 4))
                    || (($land->[$bx][$by] == $HlandBettown) && ($island->{'yaku'} >= 6))
                                                                                            ) {

                    $pop_limit = $HTown_limit if($land->[$bx][$by] == $HlandTown);
                    $pop_limit = $HNewtown_limit if($land->[$bx][$by] == $HlandNewtown);
                    $pop_limit = $HBigtown_limit if($land->[$bx][$by] == $HlandBigtown);
                    $pop_limit = $HBettown_limit if($land->[$bx][$by] == $HlandBettown);

                    # 町の場合
                    my ($lv) = $landValue->[$bx][$by];
                    if ($boat > 50) {

                        $lv += 50;
                        $boat -= 50;
                        $achive += 50;
                    } else {

                        $lv += $boat;
                        $achive += $boat;
                        $boat = 0;
                    }

                    if ($lv > $pop_limit) {

                        $boat += ($lv - $pop_limit);
                        $achive -= ($lv - $pop_limit);
                        $lv = $pop_limit;
                    }

                    $landValue->[$bx][$by] = $lv;

                } elsif (   ($land->[$bx][$by] == $HlandPlains)
                         && ($landValue->[$bx][$by] == 0 )) {    # 難民漂着
                    # 平地の場合
                    if ( $landValue->[$bx][$by] == 0 ){
                        $land->[$bx][$by] = $HlandTown;

                        if($boat > 10) {
                            $landValue->[$bx][$by] = 5;
                            $boat -= 10;
                            $achive += 10;

                        } elsif($boat > 5) {
                            $landValue->[$bx][$by] = $boat - 5;
                            $achive += $boat;
                            $boat = 0;
                        }
                    }
                }
                last if($boat <= 0);
            }

            if ($achive > 0) {
                # 少しでも到着した場合、ログを吐く
                logMsBoatPeople($id, $name, $achive);
                $island->{'ext'}[4] += int($achive); # 救出した難民の合計人口

                # 難民の数が一定数以上なら、平和賞の可能性あり
                if ($achive >= 200) {

                    my ($prize) = $island->{'prize'};
                    my ($prize1, $prize2) = split(/\t/, $prize);
                    $prize1 =~ /([0-9]*),([0-9]*),(.*)/;
                    my ($flags) = $1;
                    my ($monsters) = $2;
                    my ($turns) = $3;

                    if (    (!($flags & 8))
                        &&  ($achive >= 200) ) {

                        $flags |= 8;
                        logPrize($id, $name, $Hprize[4]);
                    } elsif((!($flags & 16)) &&  $achive > 500){
                        $flags |= 16;
                        logPrize($id, $name, $Hprize[5]);
                    } elsif((!($flags & 32)) &&  $achive > 800){
                        $flags |= 32;
                        logPrize($id, $name, $Hprize[6]);
                    }
                    $island->{'prize'} = "$flags,$monsters,$turns\t$prize2";
                }
            }
        }

        if (   ($HanyMissileMode) ){  #複数ミサイル発射可能モード
            # 次のコマンドもミサイル系か？
            my ($kind2) = $comArray->[0]->{'kind'};
            if (   (   ($kind2 == $HcomMissileNM)
                    || ($kind2 == $HcomMissilePP)
                    || ($kind2 == $HcomMissileST)
                    || ($kind2 == $HcomMissileSPP)
                    || ($kind2 == $HcomMissileLD)
                    || ($kind2 == $HcomMissileLR) )
                && ($kind != $HcomMissileSS)
                                                ) {
                # ミサイル系

                # ミサイル発射数に残りがあるか調べる
                my($flag);
                $count--;
                while ($count < $HpointNumber) {
                    $bx = $Hrpx[$count];
                    $by = $Hrpy[$count];
                    if(($land->[$bx][$by] == $HlandBase) ||
                        ($land->[$bx][$by] == $HlandSbase)) {
                        $flag = expToLevel($land->[$bx][$by], $landValue->[$bx][$by]) - $island->{'missiles'}->[$bx][$by];
                        return 0 if($flag); # 残りがあればターン消費しない
                    }
                    $count++;
                }
            }
        }

        return 1;

    } elsif (   ($kind == $HcomSendMonster)
             || ($kind == $HcomSendPirates)) {
        # 怪獣派遣  海賊派遣
        my($aId, %amityFlag);
        foreach $aId (@{$island->{'allyId'}}) {
            foreach (@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}) {
                next if($_ == $id);
                $amityFlag{$_} = $HcampAtk;
            }
        }
        # 開発期間ならコマンドを無視
        if ($HarmisticeTurn && ($HislandTurn <= $HarmisticeTurn || $amityFlag{$target})) {
            # 攻撃が許可されていない
            logNotAvail($id, $name, $comName);
            return 0;
        }
        # ターゲット取得
        my ($tn) = $HidToNumber{$target};
        my ($tIsland) = $Hislands[$tn];
        my ($tName) = islandName($tIsland);

        unless(defined $tn) {
            # ターゲットがすでにない
            logNoAny($id, $name, $comName, "目標の${AfterName}に人が見当たらない");
            return 0;
        }

        if ($tIsland->{'predelete'}) {

            logNoAny($id, $name, $comName, '実行が許可されない');
            return 0;
        }

        # 自島の人口が少ないか、目標島の人口が少ないなら、実行は許可されない
        if (   ($tIsland->{'id'} != $id)
            && (!$tIsland->{'BF_Flag'})
            && (   ($island->{'pop'} < $HguardPop)
                || ($tIsland->{'pop'} < $HguardPop) )  ) {
            logNoAny($id, $name, $comName, '実行が許可されない');
            return 0;
        }

        $tIsland->{'monstersend'}++;

        my ($send) = $tIsland->{'monstersend'};
        my ($sendmo_kind , $sendmo_id);

        if ($kind == $HcomSendPirates) {

            $sendmo_kind = $tIsland->{'sendmo_kind'};
            $sendmo_kind->[$send] = $Mons_Pirates;
            logSecretMonsSend($id, $target, $name, $tName , '海賊');
        }else{
            $sendmo_kind = $tIsland->{'sendmo_kind'};
            $sendmo_kind->[$send] = $Mons_MechaInora;
            logMonsSend($id, $target, $name, $tName , '人造怪獣');
        }
        $sendmo_id = $tIsland->{'sendmo_id'};
        if ($tIsland->{'id'} != $id) {
            $sendmo_id->[$send] = $id;
        } else{
            $sendmo_id->[$send] = 0;
        }

        # メッセージ

        $island->{'money'} -= $cost;
        return 1;

    } elsif($kind == $HcomAlly) {
        # 同盟 加盟・脱退
        # ターゲット取得
        return if(!$HallyUse || !$HallyJoinComUse || $HarmisticeTurn);
        my ($tn) = $HidToNumber{$target};
        my ($tan) = $HidToAllyNumber{$target};
        if (   ($tn eq '')
            || ($tan eq '') ) {
            # ターゲットがすでにない
            logNoAny($id, $name, $comName, "目標の${AfterName}に人が見当たらない");
            return 0;
        }
        my $tName = islandName($Hislands[$tn]);
        if (defined $HidToAllyNumber{$id}) {
            logLeaderAlready($id, $name, $tName, $comName);
            return;
        }

        my $ally = $Hally[$tan];
        if ($HallyJoinOne && ($island->{'allyId'}[0] ne '') && ($island->{'allyId'}[0] != $ally->{'id'})) {
            logOtherAlready($id, $name, $tName, $comName);
            return;
        }
        my $allyMember = $ally->{'memberId'};
        my @newAllyMember = ();
        my $flag = 0;

        foreach (@$allyMember) {
            if (!(defined $HidToNumber{$_})) {
            }
            elsif($_ == $id) {
                $flag = 1;
            }
            else {
                push(@newAllyMember, $_);
            }
        }

        if ($flag) {
            logAllyEnd($id, $target, islandName($island), $ally->{'name'});

            my @newAlly = ();
            foreach (@{$island->{'allyId'}}) {
                if($_ != $ally->{'id'}) {
                    push(@newAlly, $_);
                }
            }

            $island->{'allyId'} = \@newAlly;
            $ally->{'score'} -= $island->{'pts'};
            $ally->{'number'}--;

        } else {
            logAlly($id, $target, islandName($island), $ally->{'name'});
            push(@newAllyMember, $id);
            push(@{$island->{'allyId'}}, $ally->{'id'});
            $ally->{'score'} += $island->{'pts'};
            $ally->{'number'}++;
        }
        $island->{'money'} -= $HcomCost[$HcomAlly];
        $ally->{'memberId'} = \@newAllyMember;
        return 1;

    } elsif ($kind == $HcomSell) {
        # 食料輸出
        # 輸出量決定
        $arg = 1 if(!$arg);
        my ($value) = min($arg * (-$cost), $island->{'food'});

        # 輸出ログ
        logSell($id, $name, $comName, $value);
        #$island->{'food'} -=  $value;
        food_product_Random_consumption($island , $value);
        $island->{'money'} += ($value / 10);
        return 0;

    } elsif (   ($kind == $HcomFood)
             || ($kind == $HcomMoney) ) {
        # 援助系
        my ($aId, %amityFlag);
        foreach $aId (@{$island->{'allyId'}}) {
            foreach (@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}) {
                next if($_ == $id);
                $amityFlag{$_} = $HcampAtk;
            }
        }
        # ターゲット取得
        my ($tn) = $HidToNumber{$target};
        my ($tIsland) = $Hislands[$tn];
        my ($tName) = islandName($tIsland);

        # 他の陣営には援助できない
        if ($HarmisticeTurn && $HcampAidOnly && !$amityFlag{$target}) {
            logAidFail($id, $target, $name, $tName, $comName);
            return 0;
        }

        # 自島の人口が少ないなら、実行は許可されない
        if (($tIsland->{'id'} != $id) && ($island->{'pop'} < $HguardPop)) {
            logNoAny($id, $name, $comName, "実行が許可されない");
            return 0;
        }

        # 預かりの島
        if ($tIsland->{'predelete'}) {
            logNoAny($id, $name, $comName, "実行が許可されない");
            return 0;
        }

        # 援助量決定
        $arg = 1 if(!$arg);
        my ($value, $str);
        if ($cost < 0) {
            $value = min($arg * (-$cost), $island->{'food'});
            $str = "${HtagFood_}$value$HunitFood${H_tagFood}";
        }
        else {
            $value = min($arg * ($cost), $island->{'money'});
            $str = "${HtagMoney_}$value$HunitMoney${H_tagMoney}";
        }

        # 援助ログ
        logAid($id, $target, $name, $tName, $comName, $str);

        if ($cost < 0) {
            food_export($island , $tIsland , $value);
        } else {
            $island->{'money'} -= $value;
            $tIsland->{'money'} += $value;
            $island->{'ext'}[1] += $value; # 貢献度
            $tIsland->{'ext'}[1] -= $value; # 貢献度
        }
        return 0;

    } elsif ($kind == $HcomGivefood) {
        # エサ
        if($landKind == $HlandMonster) {
            my ($mKind, $mName, $mHp) = monsterSpec($landValue->[$x][$y]);
            $lv += random(5) if($mHp < 10);
            $landValue->[$x][$y] = $lv;
        } elsif( (($landKind == $HlandCollege) && ($lv == 4))  ||
                 (($landKind == $HlandCollege) && ($lv == 96)) ||
                 (($landKind == $HlandCollege) && ($lv == 97)) ||
                 (($landKind == $HlandCollege) && ($lv == 98))    ) {

            my ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
            if (random(100) < 30) {
                $msap++;
                logGiveFoodUpdate($id,"AP",$msap);
            } elsif (random(100) < 30) {
                $msdp++;
                logGiveFoodUpdate($id,"DP",$msdp);
            } elsif (random(100) < 30) {
                $mssp++;
                logGiveFoodUpdate($id,"SP",$mssp);
            } else {
                $mshp++;
                $mshp = 15 if($mshp > 15);
                logGiveFoodUpdate($id,"HP",$mshp);
            }
            $island->{'eisei5'} = "$mshp,$msap,$msdp,$mssp,$mswin,$msexe,$tet";

        } else {
            # 不適当な地形
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        logLandSuc($id, $name, $comName, $point);

        # 金を差し引く
        $island->{'food'} += $cost;
        if ($arg > 1) {
            $arg--;
            slideBack($comArray, 0);
            $comArray->[0] = {
                'kind' => $kind,
                'target' => $target,
                'x' => $x,
                'y' => $y,
                'arg' => $arg
            };
        }
        return 1;

    } elsif ($kind == $HcomItemThrow) {
        # アイテム捨てる
        if ($arg > $HItem_MAX) {
            logItemisNoting($id, $name);
            return 0;
        }
        my ($item) = $island->{'item_land'};
        my ($item_lv) = $island->{'item_landValue'};
        my ($item_lv2) = $island->{'item_landValue2'};
        my ($item_lv3) = $island->{'item_landValue3'};

        if ($item->[$arg] == $HItem_Nothing){

            logItemisNoting($id, $name);
            return 0;

        }else{

            my ($itemname)= landName($item->[$arg], $item_lv->[$arg], $item_lv2->[$arg]);

            $item->[$arg] = $HItem_Nothing;
            $item_lv->[$arg] = $HItem_Nothing;
            $item_lv2->[$arg] = $HItem_Nothing;
            $item_lv3->[$arg] = $HItem_Nothing;

            logItemThrow($id, $name, $itemname);

            return 0;
        }
        return 0;   # 念のため

    } elsif ($kind == $HcomItemUse) {
        # アイテムおく
        if ($arg > $HItem_MAX) {
            logItemisNoting($id, $name);
            return 0;
        }

        my ($item) = $island->{'item_land'};
        my ($item_lv) = $island->{'item_landValue'};
        my ($item_lv2) = $island->{'item_landValue2'};
        my ($item_lv3) = $island->{'item_landValue3'};

        if ($item->[$arg] == $HItem_Nothing){
            logItemisNoting($id, $name);
            return 0;

        }
        else {
            my ($itemname) = landName($item->[$arg], $item_lv->[$arg], $item_lv2->[$arg]);

            if(   ($landKind == $HlandPlains)
               || ($landKind == $HlandSea)   ) {

                $land->[$x][$y] = $item->[$arg];
                $landValue->[$x][$y] = $item_lv->[$arg];
                $landValue2->[$x][$y] = $item_lv2->[$arg];
                $landValue3->[$x][$y] = $item_lv3->[$arg];

                $item->[$arg] = $HItem_Nothing;
                $item_lv->[$arg] = $HItem_Nothing;
                $item_lv2->[$arg] = $HItem_Nothing;
                $item_lv3->[$arg] = $HItem_Nothing;
                logItemPuton($id, $name, $point ,$itemname );

            }else{
                logItemDeny($id, $name, $point);
                return 0;
            }
        }
        return 0;

    } elsif ($kind == $HcomSave) {
        # 時の記憶
        return 0 unless($island->{'shr'});
        if (-e "${HdirName}/${id}.${HsubData}") {
            copy("${HdirName}/${id}.${HsubData}", "${HdirName}/savedata.$id");
            $island->{'money'} -= $cost;
            logSaveLoad($id, $name, $comName, "を行いました。");
            my ($sx, $sy);
            foreach $sy (0..$islandSize) {
                foreach $sx (0..$islandSize) {
                    $landValue->[$sx][$sy] = $HislandTurn if($land->[$sx][$sy] == $HlandShrine);
                }
            }
        } else {
            logSaveLoad($id, $name, $comName, "に失敗しました。");
            return 0;
        }
        return 1;

    } elsif($kind == $HcomLoad) {
        # 時の忘却
        return 0 unless($island->{'shr'});
        if (-e "${HdirName}/savedata.$id") {
            # 地形データの読み込み
            if (!open(IIN, "${HdirName}/savedata.$id")) {
                logSaveLoad($id, $name, $comName, "に失敗しました。");
                return 0;
            }
            my (@sland, @slandValue, $sline, $sx, $sy);
            foreach $sy (0..$islandSize) {
                $sline = <IIN>;
                foreach $sx (0..$islandSize) {
                    $sline =~ s/^(..)(......)(..)(....)(..)//;
                    $sland[$sx][$sy] = hex($1);
                    $slandValue[$sx][$sy] = hex($2);
                    $landValue2[$sx][$sy] = hex($3);
                    $landValue3[$sx][$sy] = hex($4);
                    $landValue->[$sx][$sy] = 0 if($land->[$sx][$sy] == $HlandShrine);
                }
            }
            close(IIN);
            $island->{'land'} = \@sland;
            $island->{'landValue'} = \@slandValue;
            unlink("${HdirName}/savedata.$id");
            logSaveLoad($id, $name, $comName, 'を行いました。');
            $island->{'money'} -= $cost;
            return 1;
        }
        else {
            logSaveLoad($id, $name, $comName, 'に失敗しました。');
            return 0;
        }

    } elsif($kind == $HcomGiveup) {
        # 放棄
        $island->{'dead'} = 1;
        OutAlly($island);
        logGiveup($id, $name);
        unlink("${HdirName}/${id}.${HsubData}");
        unlink("${HdirName}/savedata.$id") if(-e "${HdirName}/savedata.$id");
        return 1;
    }

    return 1;
}


#------------------------------------------------------------------------------------
# 解散
#------------------------------------------------------------------------------------
sub logDeleteAlly_forTurn {
    my ($name) = @_;
    logHistory("同盟『${HtagName_}${name}${H_tagName}』が${HtagDisaster_}解散！${H_tagDisaster}");
}


#------------------------------------------------------------------------------------
# 同盟から抜ける
#------------------------------------------------------------------------------------
sub OutAlly {
    my ($island) = @_;

        my ($target) = $island->{'allyId'}[0];
        my ($id) = $island->{'id'};

        my ($tn) = $HidToNumber{$target};
        my ($tan) = $HidToAllyNumber{$target};

        my $tName = islandName($Hislands[$tn]);

        my $ally = $Hally[$tan];


        if (   $HallyJoinOne
            && ($island->{'allyId'}[0] ne '')
                                              ) {
            #同盟に加盟している
        my $allyMember = $ally->{'memberId'};

            
            my @newAllyMember = ();
            my $flag = 0;

            foreach (@$allyMember) {
                if(!(defined $HidToNumber{$_})) {

                } elsif($_ == $id) {
                    $flag = 1;
                } else {
                    push(@newAllyMember, $_);
                }
            }

            if($flag) {
                logAllyEnd($id, $target, islandName($island), $ally->{'name'});

                my @newAlly = ();
                foreach (@{$island->{'allyId'}}) {
                    if($_ != $ally->{'id'}) {
                        push(@newAlly, $_);
                    }
                }

                $island->{'allyId'} = \@newAlly;
                $ally->{'score'} -= $island->{'pts'};
                $ally->{'number'}--;

                $ally->{'memberId'} = \@newAllyMember;
            }

        }
}


#------------------------------------------------------------------------------------
# 攻撃不可かチェック
#------------------------------------------------------------------------------------
sub NoAnyCheck {
    my($island,$tIsland) = @_;

    # 管理人預かり
    if ($tIsland->{'predelete'}) {
        return 1;
    }

    # 自島の人口が少ないか、目標島の人口が少ないなら、実行は許可されない
    if (   (!$tIsland->{'BF_Flag'})                 # 相手のバトルフィールドでない
        && ($tIsland->{'id'} != $island->{'id'})    # 自分のしまでない
        && (   ($island->{'pop'} < $HguardPop)      # 自分の島の人数がたりない
            || ($tIsland->{'pop'} < $HguardPop) )   # 相手の島の人数がたりない
                                                  ) {
        return 1;
    }

    return 0;
}


#------------------------------------------------------------------------------------
# 難民発生する町
#------------------------------------------------------------------------------------
sub isExpTown {
    my($land) = @_;


}


#------------------------------------------------------------------------------------
# 成長および単ヘックス災害
#------------------------------------------------------------------------------------
sub doEachHex {
    my ($island) = @_;

    my (@monsterMove);
    my (@funeMove);

    # 導出値
    my ($name) = islandName($island);
    my ($id) = $island->{'id'};
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};
    my ($reason);

    my ($TurndoEachHex);

    my ($zooflag) = 0;

    my ($msseigen, $kougekiseigen, $kougekiseigenm) = (0, 0, 0);

    # 増える人口のタネ値
    my ($addpop)  = 10;  # 村、町
    $addpop = 1 if($island->{'unemployed'} >= 100);     # 失業者が増えすぎると、人が増えない
    $addpop = 20 if($island->{'BF_Flag'} == 1);         # bf

    $TurndoEachHex->{'reason_mode'} = $Reason_Normal;

    my($addpop2) = 0; # 都市
    if($island->{'food'} < 0) {
        # 食料不足
        $addpop = -30;
        $reason = '食料不足';
        $TurndoEachHex->{'reason_mode'} = $Reason_FoodShort;

    } elsif(random(20) < $island->{'rot'}) {
        # 胞子！？
        $addpop = -10;
        $reason = '胞子';
        logRotsick($id, $name);
        $TurndoEachHex->{'reason_mode'} = $Reason_Rotten;

    } elsif(random(2) < $island->{'c21'}) {
        # 疫病！？
        $addpop = -3;
        food_product_Random_consumption($island , int($island->{'food'} / 2));

        $reason = '疫病';
        logSatansick($id, $name);
        $TurndoEachHex->{'reason_mode'} = $Reason_Plague;

    } elsif(   $island->{'fim'}
            && !random(100) ) {
        # 副作用？！
        $addpop = -20;
        logStarvefood($id, $name);
        $reason = '副作用';
        $TurndoEachHex->{'reason_mode'} = $Reason_SideEffect;

    } elsif($island->{'propaganda'}) {
        # 誘致活動中
        $addpop += 10;
        $addpop += 2 if ($island->{'yaku'} >= 3);
        $addpop += 3 if ($island->{'yaku'} >= 5);

        $addpop2 = 3;
        $addpop2 = 5 if ($island->{'yaku'} >= 3);
        $addpop2 = 6 if ($island->{'yaku'} >= 5);
    }
    $TurndoEachHex->{'reason'} = $reason;
    $TurndoEachHex->{'addpop'} = $addpop;
    $TurndoEachHex->{'addpop2'} = $addpop2;

    # ループ
    my ($x, $y, $i);
    my ($landKind);
    my ($lv, $lv2, $lv3);
    my ($lName);
    my ($monsterCount);

    my ($on_train) = 0;
    $on_train = random($island->{'train'});
    my ($train_sta) = 0;

    my ($this_pos);

    $island->{'happy'} = 100;
    $island->{'tax_income'} = -1;

    foreach $i (0..$pointNumber) {

        $x = $Hrpx[$i];
        $y = $Hrpy[$i];
        $landKind = $land->[$x][$y];
        $lv = $landValue->[$x][$y];
        $lv2 = $landValue2->[$x][$y];
        $lv3 = $landValue3->[$x][$y];
        $lName = landName($landKind, $lv,$lv2);

        $TurndoEachHex->{'y'} = $y;
        $TurndoEachHex->{'x'} = $x;

        $this_pos = "($x, $y)";

        if( 0 ){
            # 海をいれるとオーバーヘッドだった。

        }elsif(   ($landKind == $HlandTown)         # 町 イベント
               || ($landKind == $HlandMinato)       # 港 イベント
               || ($landKind == $HlandSeacity)      # 海底都市 イベント
               || ($landKind == $HlandUmicity)      # イベント
               || ($landKind == $HlandNewtown)      # イベント
               || ($landKind == $HlandInaka)        # イベント
                                                ) {

            {
                $monsterCount = CityAttack($island, $x, $y);
                $lv = $landValue->[$x][$y];

                if ($monsterCount > 0) {
                    if (($lv <= 0) ) {

                        if (   ($landKind == $HlandSeacity)
                            || ($landKind == $HlandUmicity)
                                                            ){
                            # 海に戻す
                            SetSeaLand_Normal($island, $x, $y);
                            next;

                        }else{
                            # 平地に戻す
                            SetWasteLand_Normal($island, $x, $y);
                            next;
                        }
                    }
                }

                if ($addpop < 0) {
                    # 不足
                    $lv -= (random(-$addpop) + 1);
                    if($lv <= 0) {

                        if (   ($landKind == $HlandTown)
                            || ($landKind == $HlandNewtown)
                            || ($landKind == $HlandInaka)
                                                            ) {                        # 平地に戻す
                            SetPlains_Normal($island , $x , $y);

                        } else {
                            if($landKind == $HlandMinato) {
                                SetWasteLand_Normal_val($island, $x, $y,4);   # 荒地に戻す
                            }else{
                                SetSeaLand_Normal($island, $x, $y);     # 海に戻す
                            }
                        }
                        my($tName) = landName($land->[$x][$y], $landValue->[$x][$y],$landValue2->[$x][$y]);
                        logPopDecrease($id, $name, $lName, $tName, $reason, $this_pos);
                        next;
                    }

                } else {
                    # 成長
                    my ($grstop);
                    $grstop = 100;      # 都市、海底、港
                    $grstop = $HUmicity_growstop if ($landKind == $HlandUmicity) ;
                    $grstop = $HNewtown_growstop if ($landKind == $HlandNewtown) ;
                    $grstop = $HInaka_growstop if ($landKind == $HlandInaka) ;

                    $lv = Town_Growup($lv , $addpop , $addpop2 , $grstop);
                }

                my ($poplimit);
                $poplimit = $HTown_limit;   # 都市、海底、港
                $poplimit = $HUmicity_limit if ($landKind == $HlandUmicity) ;
                $poplimit = $HNewtown_limit if ($landKind == $HlandNewtown) ;
                $poplimit = $HInaka_limit if ($landKind == $HlandInaka) ;

                $lv = $poplimit if($lv > $poplimit);
                $landValue->[$x][$y] = $lv;

                if (   ($landKind == $HlandTown)
                    || ($landKind == $HlandNewtown) ) {

                    my ($townCount) = countAround($land, $x, $y, 19, @Htowns);

                    $land->[$x][$y] = $HlandBigtown if(($landKind == $HlandTown) && ($townCount > 17) && !random(1000) && ($lv > 195));
                    $land->[$x][$y] = $HlandBigtown if(($landKind == $HlandNewtown) && ($townCount > 17) && (random(1000) < 3) && ($lv > 295));
                }

                if ($landKind == $HlandMinato) {        # みなと

                    if (random(1000) < 10 ) {
                        logFishing($id, $name, $lName , $this_pos);
                    }
                }
            }

        }elsif($landKind == $HlandPlains) {     # 平地イベント

            my ($bf_flag) = $island->{'BF_Flag'};

            if (   ($lv == 0) # 予定地でない。
                && (   ($bf_flag)
                    || (   (!($bf_flag))
                        && ($island->{'unemployed'} <= 10)  # 失業者が居る。
                        && (  $island->{'farm'} + $island->{'factory'}
                            + $island->{'factoryHT'} + $island->{'mountain'} > 5) ) )
                                                                              ) {

                my ($tflag) = ($id > 100) ? 1 : countGrow($land, $landValue, $x, $y, $bf_flag);

                if (!random(5) && $tflag) {
                    # 周りに農場、町があれば、ここも町になる
                    $land->[$x][$y] = $HlandTown;
                    $landValue->[$x][$y] = 1;
                    $landValue2->[$x][$y] = 0;
                    $landValue->[$x][$y] = 1 + random(10) if ($bf_flag);
                    if (random(1000) < $island->{'nto'}*3) {
                        $land->[$x][$y] = $HlandNewtown;
                        $landValue->[$x][$y] = 1;
                        $landValue2->[$x][$y] = 0;
                    }

                    if (!($bf_flag)) {
                        logPlains2Town($island, landName($land->[$x][$y], $landValue->[$x][$y],$landValue2->[$x][$y]) ,$this_pos);
                    }
                }
            }

            if (   ($island->{'BF_Flag'} == 1)
                && ($island->{'defcnt'} < 6) ) {

                if (!random(5)) {
                    if (   (!countAround($land, $x, $y, 19, $HlandDefence ) )
                        && (!countAround($land, $x, $y, 19, $HlandMonster ) ) ){

                        $land->[$x][$y] = $HlandDefence;
                        $landValue->[$x][$y] = 0;
                        $island->{'defcnt'}++;
                    }
                }
            }

        } elsif ($landKind == $HlandWaste) {         # 荒地イベント

            WastelandEvent($island,$x,$y);

        } elsif ($landKind == $HlandProcity) {       # イベント
            # 防災都市
            if ($addpop < 0) {
                # 不足
                $lv -= (random(-$addpop) + 1);
                if ($lv <= 0) {
                    # 平地に戻す
                    SetPlains_Normal($island , $x , $y);
                    logPopDecrease($id, $name, $lName, "平地", $reason, $this_pos);
                    next;
                }
            }
            else {
                # 成長
                $lv = Town_Growup( $lv , $addpop , $addpop2 , $HProcity_growstop );
            }

            $lv = min($lv , $HProcity_limit);

            $landValue->[$x][$y] = $lv;

            if ($lv == $HProcity_limit) {

                if ( ($island->{'monsterlive'}) ) {
                    ProCity_MonsterSmash($island,$x,$y);
                }
            }

        } elsif ($landKind == $HlandFiredept) {      # 消防署 イベント
            FiredeptlandEvent($island,$x,$y);

        } elsif ($landKind == $HlandKatorikun) {     # 香取君イベント

            if ( ($island->{'monsterlive'}) ) {
                ProCity_MonsterSmash($island,$x,$y);
            }

        } elsif ($landKind == $HlandBigtown) {            # 現代都市系 イベント

            $monsterCount = CityAttack($island, $x, $y);
            $lv = $landValue->[$x][$y];

            if ($monsterCount > 0) {
                if ($lv <= 0) {
                    # 平地に戻す
                    SetWasteLand_Normal_val($island , $x , $y,4);
                    logPopDecrease($id, $name, $lName, "荒地", "怪獣の攻撃", $this_pos);
                    next;
                }
            }

            my ($townCount)  = countAround($land, $x, $y, 19, @Htowns);
            my ($houseCount) = countAround($land, $x, $y, 7, $HlandHouse);
            if (   ($island->{'shu'} == 0) && ($houseCount == 1)
                && ($townCount > 16) && (random(1000) < 300) ) {

                $land->[$x][$y] = $HlandShuto;
                my ($onm);
                $onm = $island->{'onm'};
                $island->{'shutomessage'} = "$onmシティー";
                logShuto($id, $name, $lName, "$onmシティー", $this_pos);
                $island->{'shu'}++;
            }
            if ($addpop < 0) {
                # 不足
                $lv -= (random(-$addpop) + 1);
                if($lv <= 0) {
                    # 平地に戻す
                    SetPlains_Normal($island,$x , $y);
                    logPopDecrease($id, $name, $lName, "平地", $reason, $this_pos);
                    next;
                }

            }
            else {
                # 成長
                $lv = Town_Growup( $lv , $addpop , $addpop2 , 200 );
            }
            $lv = $HBigtown_limit if($lv > $HBigtown_limit);
            $landValue->[$x][$y] = $lv;

        } elsif ($landKind == $HlandSeatown) {               # 海底新都市系

            my ($townCount)  = countAround($land, $x, $y, 19, @Htowns);
            my ($houseCount) = countAround($land, $x, $y, 7, $HlandHouse);

            if (   ($island->{'shu'} == 0)
                && ($houseCount == 1)
                && ($townCount > 16)
                && (random(1000) < 300)) {

                $land->[$x][$y] = $HlandUmishuto;
                my($onm);
                $onm = $island->{'onm'};
                $island->{'shutomessage'} = "$onmシティー";
                logShuto($id, $name, $lName, $island->{'shutomessage'}, $this_pos);
                $island->{'shu'}++;
            }

            if ($addpop < 0) {
                # 不足
                $lv -= (random(-$addpop) + 1);
                if ($lv <= 0) {
                    # 平地に戻す
                    SetSeaLand_Normal($island, $x, $y);     # 海に戻す
                    logPopDecrease($id, $name, $lName, '海', $reason, $this_pos);
                    next;
                }

            } else {
                # 成長
                $lv = Town_Growup( $lv , $addpop , $addpop2 , 250 );
            }
            $lv = min($lv,$HSeatown_limit);
            $landValue->[$x][$y] = $lv;

        } elsif ($landKind == $HlandBettown) {   # 輝ける都市 イベント

            $monsterCount = CityAttack($island, $x, $y);
            $lv = $landValue->[$x][$y];
            if ($monsterCount > 0) {
                if ($lv <= 0) {
                    # 平地に戻す
                    SetWasteLand_Normal_val($island , $x , $y , 4);
                    logPopDecrease($id, $name, $lName, "荒地", "怪獣の攻撃", $this_pos);
                    next;
                }
            }

            if ($addpop < 0) {
                # 不足
                $lv -= (random(-$addpop) + 1);
                if ($lv <= 0) {
                    # 平地に戻す
                    SetPlains_Normal($island , $x , $y);
                    logPopDecrease($id, $name, $lName, "平地", $reason, $this_pos);
                    next;
                }
            } else {
                # 成長
                my($shutoCount) = countAround($land, $x, $y, 7, $HlandShuto, $HlandUmishuto);
                my($betCount) = countAround($land, $x, $y, 7, $HlandBettown);

                if(($island->{'shu'} > 0) &&
                    (($shutoCount > 0) || ($betCount > 1))) {
                    # 成長
                    $lv = Town_Growup( $lv , $addpop , $addpop2 , 1000 );
                }
            }
            $landValue->[$x][$y] = min($lv , $HBettown_limit);

        } elsif(   ($landKind == $HlandShuto)            # 首都系
                || ($landKind == $HlandUmishuto) ) {     # 首都系

            $monsterCount = CityAttack($island, $x, $y);
            $lv = $landValue->[$x][$y];
            if ($monsterCount > 0) {
                if ($lv <= 0) {
                    if($landKind == $HlandUmishuto) {
                        # 海に戻す
                        $land->[$x][$y] = $HlandSea;
                    } elsif($landKind == $HlandShuto) {
                        # 平地に戻す
                        SetPlains_Normal($island , $x , $y);
                    }
                    $landValue->[$x][$y] = 0;       #首都 reset
                    my ($tName) = landName($land->[$x][$y], $landValue->[$x][$y],$landValue2->[$x][$y]);
                    logPopDecrease($id, $name, $lName, $tName, "怪獣の攻撃", $this_pos);
                    next;
                }
            }

            if ($addpop < 0) {
                # 不足
                $lv -= (random(-$addpop) + 1);
                if ($lv <= 0) {
                    if ($landKind == $HlandUmishuto) {
                        # 海に戻す
                        $land->[$x][$y] = $HlandSea;
                    } elsif($landKind == $HlandShuto) {
                        # 平地に戻す
                        SetPlains_Normal($island , $x , $y);
                    }
                    $landValue->[$x][$y] = 0;
                    my ($tName) = landName($land->[$x][$y], $landValue->[$x][$y],$landValue2->[$x][$y]);
                    logPopDecrease($id, $name, $lName, $tName, $reason, $this_pos);
                    next;
                }

            } else {
                # 成長
                $lv = Town_Growup( $lv , $addpop , $addpop2 , $HShuto_growstop );
            }
            $landValue->[$x][$y] = min($lv , $HShuto_limit);

        } elsif(   ($landKind == $HlandRizort)          # リゾート系 イベント
                || ($landKind == $HlandBigRizort) ) {   # リゾート系 イベント

            if(   (   ($landKind == $HlandRizort)
                   && ($lv < 400)
                   && (random(100) < 25) )
               || (   ($landKind == $HlandBigRizort)
                   && ($lv < 1000)
                   && (random(100) < 30) ) ) {

                my (@order) = randomArray($HislandNumber);
                my ($migrate);

                # 観光先を探す
                my ($tIsland);
                my ($n) = min($HislandNumber, 5);
                my ($i);

                my ($seaCount) = countAround($land, $x, $y, 19, $HlandSea,$HlandStation);
                my ($forestCount) = countAround($land, $x, $y, 19, $HlandForest, $HlandMountain,$HlandOnsen);
                my ($parkCount) = countAround($land, $x, $y, 19, $HlandPark, $HlandKyujo, $HlandKyujokai);
                my ($umiamuCount) = countAround($land, $x, $y, 19, $HlandUmiamu,$HlandInoraLand);
                my ($sunahamaCount) = countAround($land, $x, $y, 19, $HlandSunahama,$HlandBeachPark);
                my ($rizortCount) = (countAround($land, $x, $y, 19, $HlandRizort, $HlandBigRizort));
                $migrate =   $seaCount * 2
                           + $forestCount * 3
                           + $parkCount * 4
                           + $umiamuCount * 7
                           + $sunahamaCount * 6
                           + $rizortCount * 5;

                for ($i = 0; $i < $n; $i++) { # ５島まで調べる
                    $tIsland = $Hislands[$order[$i]];

                    next if ($tIsland->{'BF_Flag'});        # バトルフィールドを除外
                    next if ($tIsland->{'predelete'});      # あずかりは除外

                    # 人口の多い島に観光する
                    if ($island->{'pop'} < $tIsland->{'pop'}) {
                        $lv += $migrate;
                        logKankouMigrate($id, $tIsland->{'id'}, $name, $lName, islandName($tIsland), $this_pos, $migrate);
                    }
                    last if ($employed <= 0);
                }

                $island->{'eisei2'} += $migrate;
                $island->{'pop'} += $migrate;
                $tIsland->{'pop'} -= $migrate;

                # 観光にきてくれた分人口減少
                my ($tLand) = $tIsland->{'land'};
                my ($tLandValue) = $tIsland->{'landValue'};
                my ($employed) = $migrate;
                my ($x, $y, $landKind, $lv);
                foreach $i (0..$pointNumber) {
                    $x = $Hrpx[$i];
                    $y = $Hrpy[$i];
                    $landKind = $tLand->[$x][$y];
                    $lv = $tLandValue->[$x][$y];

                    if(($lv > 1) && (($landKind == $HlandTown) ||
                        ($landKind == $HlandProcity) ||
                        ($landKind == $HlandMinato) ||
                        ($landKind == $HlandFrocity) ||
                        ($landKind == $HlandNewtown) ||
                        ($landKind == $HlandBigtown) ||
                        ($landKind == $HlandBettown) ||
                        ($landKind == $HlandUmicity) ||
                        ($landKind == $HlandOilCity) ||
                        ($landKind == $HlandOnsen) ||
                        ($landKind == $HlandRizort) ||
                        ($landKind == $HlandBigRizort) ||
                        ($landKind == $HlandShuto) ||
                        ($landKind == $HlandUmishuto) ||
                        ($landKind == $HlandSeatown) ||
                        ($landKind == $HlandSeacity) ||
                        ($landKind == $HlandInaka)
                            )) {
                        # 町
                        $n = min($lv - 1, $employed);
                        $tLandValue->[$x][$y] -= $n;
                        $employed -= $n;
                    }
                }
            }

            if($addpop < 0) {
                # 不足
                $lv -= (random(-$addpop) + 1);
                if($lv <= 0) {
                    # 平地に戻す
                    SetPlains_Normal($island , $x , $y);
                    next;
                }
            } else {
                # 成長
                $lv = Town_Growup( $lv , $addpop , $addpop2 , 10 );
            }

            if ($landKind == $HlandRizort) {

                $lv = min($lv , 400);
                my $value = $lv+$island->{'eis1'}+$island->{'eis2'}+$island->{'eis3'}+$island->{'eis5'}+int($island->{'fore'}/10)+int($island->{'rena'}/10)-$island->{'monsterlive'}*100;
                $island->{'money'} += $value if ($value > 0);

            } else {

                $lv = min($lv , 1000);
                $landValue->[$x][$y] = $lv;

                $monsterCount = CityAttack($island, $x, $y);
                $lv = $landValue->[$x][$y];
                if ($monsterCount > 0) {
                    if ($lv <= 0) {
                        # 平地に戻す
                        SetWasteLand_Normal_val($island,$x,$y,4);
                        logPopDecrease($id, $name, $lName, "荒地", "怪獣の攻撃", $this_pos);
                        next;
                    }
                }
            }
            $landValue->[$x][$y] = $lv;

        }
        elsif($landKind == $HlandHTFactory) {     # ハイテク企業イベント

            if (random(1000) < 5 ){
                logSpiderMan($id, $name, $lName ,$this_pos);
            }

            if ( $island->{'business'} > 0 ) {

                if ($island->{'pika'} > 0) {

                    my $wk = $HlandHTFactory_add;
                    if ($island->{'shtf'} > 0) {
                        if (random(100) < 70 ){
                            $wk = 0;
                        }
                    }
                    $landValue->[$x][$y] += $wk;
                    $landValue->[$x][$y] = $HlandHTFactory_limit if($landValue->[$x][$y] > $HlandHTFactory_limit);
                }
            }

        } elsif ($landKind == $HlandSHTF) {          # ハイテク企業 イベント

            if (random(1000) < 5 ){
                logSpiderMan($id, $name, $lName , $this_pos);
            }
            if ( $island->{'business'} > 0 ) {
                if ($island->{'pika'} > 0) {
                    $landValue->[$x][$y] += $HlandSHTF_add;
                    if ($landValue->[$x][$y] > $HlandSHTF_limit) {
                        $landValue->[$x][$y] = $HlandSHTF_limit;
                    }
                }
            }

        } elsif($landKind == $HlandOnsen) {         # 温泉イベント

            if($addpop < 0) {
                # 不足
                $lv -= (random(-$addpop) + 1);
                if($lv <= 0) {
                    # 山に戻す
                    SetMountain_Normal($island,$x,$y);
                    next;
                }
            } else {
                # 成長
                $lv = Town_Growup( $lv , $addpop , $addpop2 , 50 );
            }

            $lv = min( $lv , $HOnsen_limit);

            $landValue->[$x][$y] = $lv;

            if ($landKind == $HlandOnsen) {
                my ($nt) = countAround($land, $x, $y, 19, @Htowns);
                my ($value) = random($nt * 20 + $lv * 5 + int($island->{'pop'} / 20)) + random(100) + 100;
                if ($value > 0) {
                    $island->{'money'} += $value;

                    # 収入ログ
                    my ($str) = "$value$HunitMoney";
                    logOilMoney($id, $name, $lName, $this_pos, $str, "収益");
                }

                # 温泉枯渇判定
                if(!$HnoDisFlag && random(1000) < $HonsenRatio) {
                    # 枯渇
                    logDamageAny($id, $name, $lName, $this_pos, "枯渇したようです。");
                    $land->[$x][$y] = $HlandMountain;
                    $landValue->[$x][$y] = 0;
                }
            }

        } elsif( ($landKind == $HlandSea) ) {

            if ( ($lv == 1) ) {
                # 浅瀬

                my ($par) = $To_Sunahama_par;
                if (   ($island->{'weather'} == 0)
                    && ($island->{'temperature'} > 15) ) {
                    $par += 5;
                }

                if ($island->{'weather'} == 2) {
                    $par -= 5;
                }

                if (random(100) < $par) {
                    $land->[$x][$y] = $HlandSunahama;
                    $landValue->[$x][$y] = 0;
                }

                $par = $To_Ice_par;

                if ($island->{'temperature'} < 7) {
                    $par += 8;
                }

                if(random(100) < $par) {
                    $land->[$x][$y] = $HlandIce;
                    $landValue->[$x][$y] = 0;
                }
            }

        } elsif($landKind == $HlandBeachPark) {

            if ($island->{'temperature'} >= 22) {
                if ($island->{'weather'} != $HWeather_Rain) {
                    my($lv) = $landValue->[$x][$y];
                    if($lv > 0) {
                        my $value = $lv * 12 + random(200);
                        $island->{'money'} += $value;
                        # 収入ログ
                        logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", "収益");
                    }
                }
            }

            SunahamaToSea($island,$x,$y);

        } elsif($landKind == $HlandSunahama) {
            # 砂浜
            if ( !$landValue->[$x][$y] ){

                SunahamaToSea($island,$x,$y);
            }

        } elsif($landKind == $HlandIce) {
            # 氷河
            my($lv) = $landValue->[$x][$y];
            if($lv > 0) {
                if ($island->{'weather'} != $HWeather_Rain) {
                    my $value = $lv * 25 + random(501);
                    $island->{'money'} += $value;
                    # 収入ログ
                    logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", "収益");
                }
            }

            if(random(100) < $Ice_To_Sea_par) {
                logSkateDown($island, $lName, $x, $y) if($lv > 0);        #スケート場のみ
                $land->[$x][$y] = $HlandSea;
                $landValue->[$x][$y] = 1;
                $landValue2->[$x][$y] = 0;
            }

        } elsif($landKind == $HlandForest) {
            # 森
            ForestEvent($island,$x,$y);

            my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
            $island->{'happy'} += $happy;

        } elsif(   ($landKind == $HlandFarmchi)
                || ($landKind == $HlandFarmpic)
                || ($landKind == $HlandFarmcow) ){
            # 養鶏場、養豚場、牧場
            my($FarmCount) = countAround($land, $x, $y, 7, $HlandFarm,$HlandInaka);
            my(@rflag);

            if($landKind == $HlandFarmchi) {
                @rflag = (1, 8 + $FarmCount * 2, 5);
            } elsif($landKind == $HlandFarmpic){
                @rflag = (2, 4 + $FarmCount * 2, 3);
            } else {
                @rflag = (3, 4 + $FarmCount, 1);
            }

            my ($value) = $lv * $rflag[0];
            if ($landKind == $HlandFarmchi) {
                my ($egg , $niku) ;
                $egg = int($value / 4);
                $niku = $value - $egg;
                if ($egg) {
                    food_product_plus($island , 'tamago' , $egg);
                }
                food_product_plus($island , 'toriniku' , $niku);

            } elsif($landKind == $HlandFarmpic){
                food_product_plus($island , 'butaniku' , $value);

            } else {
                food_product_plus($island , 'gyuniku' , $value);
            }

            $lv += random($rflag[1]) + $rflag[2];
            $landValue->[$x][$y] = min($lv , $HLivestock_limit);

        } elsif($landKind == $HlandDefence) { # 防衛施設イベント
            my ($deflv);
            $deflv = $lv & $HDefenceLevelMask;

            if ( $deflv == 0 ) {

            }elsif ($deflv == 2) {
                $island->{'money'} -= $HDefenceTurnCost;
                $island->{'money'} = 0 if ( $island->{'money'} < 0 );
            }


        } elsif($landKind == $HlandOilCity) {       # 油田都市 イベント

            $monsterCount = CityAttack($island, $x, $y);
            $lv = $landValue->[$x][$y];

            if ($monsterCount > 0) {
                if($lv <= 0) {
                    # 壊される
                    SetSeaLand_Normal($island, $x, $y);     # 海に戻す
                    next;
                }
            }else{
                if($addpop < 0) {
                    # 不足
                    $lv -= (random(-$addpop) + 1);
                    if($lv <= 0) {
                        # 平地に戻す
                        SetSeaLand_Normal($island, $x, $y);     # 海に戻す
                        next;
                    }
                } else {
                    # 成長
                    $lv = Town_Growup( $lv , $addpop , $addpop2 , 2000 );
                }
                if($lv > 3000) {
                    $lv = 3000;
                }
                $landValue->[$x][$y] = $lv;

                if (!random(5)){
                    my ($value) = 1 + random(1200);
                    $island->{'oilincome'} += $value if($HlogOmit1);
                    # 収入ログ
                    logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", "収益") if(!$HlogOmit1);
                }
            }

        } elsif($landKind == $HlandOil) {       # 海底油田　イベント
            my($value, $str);
            $value = $HoilMoney + random(1001);
            $island->{'money'} += $value;

            $island->{'oilincome'} += $value if($HlogOmit1);
            # 収入ログ
            logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", "収益") if(!$HlogOmit1);

            # 枯渇判定
            if(!$HnoDisFlag && random(1000) < ( $HoilRatio + ($island->{'oil'}*2) ) ) {
                # 枯渇
                logDamageAny($id, $name, $lName, $this_pos, "枯渇したようです。");
                SetSeaLand_Normal($island, $x, $y);     # 海に戻す
            }

        } elsif($landKind == $HlandSeki) {
            # 関所
            if(random(1000) < 7) {
                my $value = $HoilMoney + random(1001);
                $island->{'money'} += $value;

                # 収入ログ
                logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", '関税収益');
            }

        } elsif(   ($landKind == $HlandPark)
                || ($landKind == $HlandInoraLand)
                || ($landKind == $HlandKyujo)
                || ($landKind == $HlandUmiamu) ) {
            # 遊園地、野球場、海あみゅ、いのらランド

            my ($value, $event, $closed) = (0, 0, 0);
            my ($inoraevent) = 0;

            if($landKind == $HlandPark) {
                # 遊園地
                $closed = 2;

                if ( $island->{'business'} > 0 ) {
                    $event = 3;
                    unless(($island->{'par'} + $island->{'inoraland'}) > 5) {
                        my ($Guest) = 45 + random(10);
                        $Guest -= (random(10)) if ($island->{'weather'} == $HWeather_Rain);
                        $Guest = (70 + random(10)) if ($island->{'weather'} == $HWeather_Sunny);

                        my($nv) = (countAround($land, $x, $y, 7, $HlandPark, $HlandKyujo, $HlandUmiamu,$HlandInoraLand));
                        my($nx) = 3 * ($nv + 10) / 10;
                        $value = int(int($island->{'pop'} / $Guest) * $nx * $Hmoney2Incom[0]/100);
                    }
                }

            } elsif($landKind == $HlandInoraLand) {                # いのらランド

                $closed = 0;
                if ( $island->{'business'} > 0 ) {
                    if ( $HislandTurn && !$InoraParkEvent) {
                        $event = 60; 
                        if(random(100) < $event) {
                            unless(($island->{'par'}) > 5) {

                                my ($Guest) = 20 + random(10);
                                $Guest -= (random(10)) if ($island->{'weather'} == $HWeather_Rain);
                                $Guest = (30 + random(10)) if ($island->{'weather'} == $HWeather_Sunny);

                                my ($nt) = (countAround($land, $x, $y, 19, @Htowns) - 3);
                                my ($np) = ( 1 + 3 * countAround($land, $x, $y, 19, $HlandPark));
                                my ($na) = ( 1 + 4 * countAround($land, $x, $y, 19, $HlandKyujo) );
                                my ($nqk) = (1 + 4 * countAround($land, $x, $y, 19, $HlandKyujokai) );
                                my ($nu) = ( 5 + random(5));
                                $value = int(($nt * $np * $na * $nqk * $nu + int($island->{'pop'} / $Guest)+ random(200)) * $Hmoney2Incom[$Hmonth]/100);
                                $inoraevent = 1;
                                $InoraParkEvent = 1;
                            }
                        }
                    }
                }

            } elsif($landKind == $HlandKyujo) {
                # 野球場
                $closed = 1;

                my ($Guest) = 20 + random(10);
                $Guest -= (random(10)) if ($island->{'weather'} == $HWeather_Rain);
                $Guest = (30 + random(10)) if ($island->{'weather'} == $HWeather_Sunny);

                unless(($island->{'kyu'} > 1) || ($island->{'amu'} > 1)) {
                    my($nt) = (countAround($land, $x, $y, 19, @Htowns) - 6);
                    my($np) = ( 1 + 2 * countAround($land, $x, $y, 19, $HlandPark));
                    my($na) = ( 1 + 3 * countAround($land, $x, $y, 19, $HlandUmiamu, $HlandInoraLand));
                    my($nu) = ( 10 + random(10));
                    $value = int(($nt * $np * $na * $nu + int($island->{'pop'} / $Guest)) * $Hmoney2Incom[0]/100);
                }

                if(random(100) < 3) {

                    my($value, $str);
                    $value = 500+ random(500);
                    $island->{'money'} += $value;
                    $str = "$value$HunitMoney";
                    # 収入ログ
                    logYusho($id, $name, $lName, $this_pos, $str);
                }

            } elsif($landKind == $HlandUmiamu) {    # 海あみゅ

                $closed = 0;
                $closed = 2 if( ($island->{'amu'} >= 4) );
                if ( $island->{'business'} > 0 ) {
                    unless(($island->{'kyu'} > 1) || ($island->{'amu'} > 1)) {

                        my ($Guest) = 20 + random(10);
                        $Guest -= (random(10)) if ($island->{'weather'} == $HWeather_Rain);
                        $Guest = (30 + random(10)) if ($island->{'weather'} == $HWeather_Sunny);

                        my($nt) = (countAround($land, $x, $y, 19, @Htowns) - 3);
                        my($np) = ( 1 + 3 * countAround($land, $x, $y, 19, $HlandPark));
                        my($na) = ( 1 + 4 * countAround($land, $x, $y, 19, $HlandKyujo , $HlandInoraLand) );
                        my($nqk) = (1 + 4 * countAround($land, $x, $y, 19, $HlandKyujokai) );
                        my($nu) = ( 5 + random(5));
                        $value = int(($nt * $np * $na * $nqk * $nu + int($island->{'pop'} / $Guest)+ random(200)) * $Hmoney2Incom[$Hmonth]/100);
                    }
                }
            }

            if($value > 0) {
                $island->{'money'} += $value;
                # 収入ログ
                if($HlogOmit1 && $event && (!$inoraevent) ) {
                    $island->{'parkincome'} += $value;
                } else {
                    logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", "収益");
                }
            }

            # イベント判定
            if (   ( $island->{'business'} > 0 )
                && (   ( (random(100) < $event) && ( $landKind != $HlandInoraLand) )   # 毎ターン 10% の確率でイベントが発生する
                    || ($inoraevent) ) ) {       # いのらランドのイベント

                if ($landKind == $HlandInoraLand) {

                    $value = int($island->{'pop'} / 40 * 10 * $Hmoney2Incom[0]/100); # 人口4千人ごとに1000トンの食料消費
                    food_product_consumption($island , $value);
                    logParkEvent($id, $name, $lName, $this_pos, "$value$HunitFood") if($value);

                } else {

                    $value = int($island->{'pop'} / 50 * 10 * $Hmoney2Incom[0]/100); # 人口5千人ごとに1000トンの食料消費
                    food_product_consumption($island , $value);
                    logParkEvent($id, $name, $lName, $this_pos, "$value$HunitFood") if($value);
                }
            }

            # 老朽化判定
            if (random(100) < $closed) {
                # 施設が老朽化したため閉園
                logDamageAny($id, $name, $lName, $this_pos, "施設が老朽化したため取り壊されました。");
                SetPlains_Normal($island , $x , $y);
                $land->[$x][$y] = $HlandSea if ($landKind == $HlandUmiamu);
                $landValue->[$x][$y] = 0;
                $landValue2->[$x][$y] = 0;
            }

        } elsif($landKind == $HlandStation) {

            if ($island->{'train'} < 5) {

                my ($i,$bx,$by);
                my ($fx,$fy);
                my ($check) = 0;

                foreach $i (0..$pointNumber) {

                    $fx = $Hrpx[$i];
                    $fy = $Hrpy[$i];

                    if (   (0)
                        || ($land->[$fx][$fy] == $HlandTown)
                        || ($land->[$fx][$fy] == $HlandNewtown)
                        || ($land->[$fx][$fy] == $HlandBigtown)
                        || ($land->[$fx][$fy] == $HlandMinato)
                                                                ) {
                        if ($landValue->[$fx][$fy] > 4) {
                            $check = 1;
                            last;
                        }
                    }

                    if (   (0)
                        || ($land->[$fx][$fy] == $HlandFactory)
                        || ($land->[$fx][$fy] == $HlandPark)
                        || ($land->[$fx][$fy] == $HlandUmiamu)
                                                                ) {
                        if ($landValue->[$fx][$fy] > 4) {
                            $check = 2;
                            last;
                        }
                    }

                }

                next if (!$check);

                for ($i = 0; $i < 19; $i++) {
                    $bx = $x + $ax[$i];
                    $by = $y + $ay[$i];

                    # 行による位置調整
                    $bx-- if(!($by % 2) && ($y % 2));

                    # 範囲内の場合
                    if (($bx >= 0) && ($bx < $HislandSize) && ($by >= 0) && ($by < $HislandSize)) {
                        if (random(100) < 30) {

                            if (   (   ($check == 1)
                                    && (   (   ($land->[$bx][$by] == $HlandTown)
                                            && ($landValue->[$bx][$by] < $HTown_limit) )
                                        || (   ($land->[$bx][$by] == $HlandNewtown)
                                            && ($landValue->[$bx][$by] < $HNewtown_limit) )
                                        || (   ($land->[$bx][$by] == $HlandProcity)
                                            && ($landValue->[$bx][$by] < $HProcity_limit) )
                                        || (   ($land->[$bx][$by] == $HlandBettown)
                                            && ($landValue->[$bx][$by] < $HBettown_limit) )
                                        || (   ($land->[$bx][$by] == $HlandShuto)
                                            && ($landValue->[$bx][$by] < $HShuto_limit) )
                                                                                          ) )
                                || (   ($check == 2)
                                    && (   (   ($land->[$bx][$by] == $HlandFactory)
                                            && ($landValue->[$bx][$by] < $HFactory_limit) )
                                        || (   ($land->[$bx][$by] == $HlandPark)
                                            && ($landValue->[$bx][$by] < $HPark_limit) )
                                        || (   ($land->[$bx][$by] == $HlandUmiamu)
                                            && ($landValue->[$bx][$by] < $HUmiamu_limit) )
                                                                                          ) )
                                                                                              ) {
                                my ($ra);
                                $ra = random(2) + 1;
                                $landValue->[$bx][$by] += $ra;
                                $landValue->[$fx][$fy] -= $ra;
                                $check = 5;

                                my ($value);
                                $value = $island->{'train'};
                                if ($value) {
                                    $island->{'money'} += $value;
                                    logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", '収益');
                                }
                                last;
                            }
                        }
                    }
                }
            }

        } elsif($landKind == $HlandMountain) {          # 山　イベント

            if ($lv > 0) {
                my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
                $island->{'happy'} -= $happy;
            }

        } elsif($landKind == $HlandKyujokai) {

            {
                $island->{'happy'} += 10;
                my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
                $island->{'happy'} -= $happy;
            }

            # 野球場改
            # イベント判定
            if (random(100) < 10) { # 毎ターン 30% の確率でイベントが発生する
                my ($Guest) = 45 + random(10);
                $Guest -= (random(10)) if ($island->{'weather'} == $HWeather_Sunny);
                $Guest = (70 + random(10)) if ($island->{'weather'} == $HWeather_Rain);
                # 野球場のイベント
                my ($value) = int($island->{'pop'} / $Guest) * 10; # 人口５千人ごとに1000トンの食料消費
                food_product_consumption($island , $value);
                logParkEvent($id, $name, $lName, $this_pos, "$value$HunitFood") if ($value > 0);
            }

            my ($escape) = 0;
            my ($i, $sx, $sy);
            my ($tkind);

            for ($i = 1; $i < 7; $i++) {
                $sx = $x + $ax[$i];
                $sy = $y + $ay[$i];

                # 行による位置調整
                $sx-- if(!($sy % 2) && ($y % 2));
                # 範囲外
                next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

                if (random(100) < 12) {
                    $tkind = $land->[$sx][$sy];
                    if (   ($tkind == $HlandTown)
                        || ($tkind == $HlandMinato)
                        || ($tkind == $HlandNewtown)
                        || ($tkind == $HlandBigtown)
                        || ($tkind == $HlandFrocity)
                        || ($tkind == $HlandShuto)
                        || ($tkind == $HlandBettown)
                        || ($tkind == $HlandRizort)
                        || ($tkind == $HlandBigRizort)
                        || ($tkind == $HlandOilCity)
                        || ($tkind == $HlandUmicity)
                                                        ) {
                        $escape++;
                        $landValue->[$sx][$sy]--;
                        if ($landValue->[$sx][$sy] <= 0 ) {
                            SetPlains_Normal($island , $sx , $sy);

                            if (   ($tkind == $HlandFrocity)
                                || ($tkind == $HlandOilCity)
                                || ($tkind == $HlandUmicity) ) {
                                $land->[$sx][$sy] = $HlandSea;
                            }
                        }
                    }
                }

            }
            logSouon($id, $name, $this_pos, $lName ,$escape) if ($escape);

            next if($HflagKai);     # 処理済み
            $HflagKai = 1;

            # 収入の算出
            unless(($island->{'kyu'} > 1) || ($island->{'amu'} > 1)) {

                my ($Guest) = 20 + random(10);
                $Guest -= (random(10)) if ($island->{'weather'} == $HWeather_Sunny);
                $Guest = (30 + random(10)) if ($island->{'weather'} == $HWeather_Rain);

                my($nt) = (countAround($land, $x, $y, 19, @Htowns) - 6);
                my($ns) = ( 1 + 2 * countAround($land, $x, $y, 19, $HlandPark));
                my($nr) = ( 1 + 3 * countAround($land, $x, $y, 19, $HlandUmiamu, $HlandInoraLand));
                my($nu) = ( 10 + random(10));
                my($value);
                $value = ($nt * $nu * $ns * $nr + int($island->{'pop'} / $Guest));
                if ($value > 0) {
                    $island->{'money'} += $value;
                    # 収入ログ
                    logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", "収益");
                }
            }

            # HakoniwaCup
            my ($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $island->{'eisei4'});
            my ($yosengameendm) = 0;
            my ($hcgameseigen) = 1;
            my ($turn) = $HislandTurn % 100;
            my ($otry) = 3;
            my ($turn1, $goal, $tgoal);

            if ((0 < $turn) && ($turn < 41)) {                  # 予選
                $turn1 = int(($turn + 9) / 10);
                $hcgameseigen = 3 unless($HislandNumber < 21);
                $otry = 5;

            } elsif((41 < $turn) && ($turn < 47)) {             # 準々決勝戦
                $turn1 = 6;

            } elsif((46 < $turn) && ($turn < 50)) {             # 準決勝戦
                $turn1 = 7;

            } elsif((49 < $turn) && ($turn < 52)) {             # 決勝戦
                $turn1 = 8;

            } elsif($turn == 0) {                               # 初期化

                HakoCup_TeamReset($island);
                $Hstsanka++;
                # 100ターン初の多目的で開催が行われる。
                if ($Hstsanka == 1) {
                    $island->{'stsankahantei'}++;
                }
            }

            # 初回戦？
            if (!$turn1) {
                if (   ($stshoka == 10)
                    || ($stshoka == 11)) {

                    my ($stup);
                    $stup = random(3);
                    if ($stup == 0) {
                        $sto++;             # 攻撃++
                    } elsif ($stup == 1) {
                        $std++;             # 守り++
                    } else {
                        $stk++;             # KP++
                    }
                }
                next;
            }

            if(   ($stshoka == $turn1)
               && ($Hyosengameend < $hcgameseigen)  ) {

                my($tIsland);
                my($i);

                my(@order) = randomArray($HislandNumber);

                foreach $i (0..$islandNumber) {

                    last if($yosengameendm);

                    $tIsland = $Hislands[$order[$i]];               #対戦相手を取り出す
                    next if ($island->{'id'} == $tIsland->{'id'});  #自分とは戦わない
                    next if ($tIsland->{'predelete'});              #預かりの場合は除外

                    my($tSto, $tStd, $tStk, $tStwin, $tStdrow, $tStlose, $tStwint, $tStdrowt, $tStloset, $tStyusho, $tStshoka) = split(/,/, $tIsland->{'eisei4'});

                    next if (($tStshoka != $turn1) || ($Hyosengameend >= $hcgameseigen));

                    my($uphey, $tuphey, $uppoint, $tuppoint, $value, $str, $str1, $str2);

                    $goal = 0;
                    $tgoal = 0;

                    foreach (1..$otry) {
                        if(   (random($sto) > random($tStd))            # 自 攻撃 > 相手 守り
                           && (random($sto) > random($tStk)) ) {        # 自 攻撃 > 相手 KP
                            $goal++;                                    # 自 得点++
                        }

                        next if($_ > 3);
                        if(   (random($tSto) > random($std))            # 相手 攻撃 > 自 守り
                           && (random($tSto) > random($stk))  ) {       # 相手 攻撃 > 自 KP
                            $tgoal++;                                   # 相手 得点++
                        }
                    }

                    if(   ($turn1 > 5)
                       && ($goal == $tgoal) ) {                         # 同点

                        if(random(100) < 60) {                          # 60 %
                            $goal++;                                    # 自 得点++
                        } else {
                            $tgoal++;                                   # 相手 得点++
                        }
                    }

                    $uphey    = int(($sto + $std + $stk) / 3);          # 自分の攻守KP の平均
                    $tuphey   = int(($tSto + $tStd + $tStk) / 3);       # 相手の攻守KP の平均
                    $uppoint  = int(($tuphey - $uphey) / 2) + 5;        # 相手-自分 /2 +5
                    $tuppoint = int(($uphey - $tuphey) / 2) + 5;        # 自分-相手 /2 +5

                    if ($turn1 == 8) {
                        $str1 = '決勝戦';
                        $str2 = '優勝';
                        $uppoint = 50;
                        $tuppoint = 50;

                    } elsif ($turn1 == 7) {
                        $str1 = '準決勝戦';
                        $str2 = '決勝進出';
                        $uppoint = 30;
                        $tuppoint = 30;

                    } elsif ($turn1 == 6) {
                        $str1 = '準々決勝戦';
                        $str2 = '準決勝進出';
                        $uppoint = 30;
                        $tuppoint = 30;

                    } else {
                        $str1 = "予選第${turn1}戦";
                        $str2 = '勝利';
                    }

                    my($stup) = random(3);          # 0 - 2

                    $Hyosengameend++;
                    $yosengameendm++;
                    $stshoka++;
                    $tStshoka++;

                    if($goal > $tgoal) {

                        $stwin++;
                        $stwint++;
                        $styusho++ if($turn1 == 8);
                        $tStlose++;
                        $tStloset++;
                        $tStshoka = $turn1 + 6 if($turn1 > 5);
                        $value = (($stwin * 3 + $stdrow) * 1000);
                        $value *= 2 if($turn1 == 8);
                        $island->{'money'} += $value;
                        $str = "$value$HunitMoney";
                        logHCwin($id, $name, $str2, $str);

                        if($stup == 0) {
                            $tSto += $tuppoint;
                            $tStd += $tuppoint if($turn1 < 5);
                        } elsif($stup == 1) {
                            $tStd += $tuppoint;
                            $tStk += $tuppoint if($turn1 < 5);
                        } else {
                            $tStk += $tuppoint;
                            $tSto += $tuppoint if($turn1 < 5);
                        }

                    } elsif($goal < $tgoal) {
                        $tStwin++;
                        $tStwint++;
                        $tStyusho++ if($turn1 == 8);
                        $stlose++;
                        $stloset++;
                        $stshoka = $turn1 + 6 if($turn1 > 5);
                        my($value);
                        $value = (($tStwin * 3 + $tStdrow) * 1000);
                        $value *= 2 if($turn1 == 8);
                        $tIsland->{'money'} += $value;
                        $str = "$value$HunitMoney";
                        logHCwin($tIsland->{'id'}, islandName($tIsland), $str2, $str);
                        if ($stup == 0) {
                            $sto += $uppoint;                       # 攻撃+
                            $std += $uppoint if($turn1 < 5);
                        } elsif($stup == 1) {
                            $std += $uppoint;
                            $stk += $uppoint if($turn1 < 5);
                        } else {
                            $stk += $uppoint;
                            $sto += $uppoint if($turn1 < 5);        # 攻撃+
                        }

                    } else {
                        $stdrow++;
                        $stdrowt++;
                        $tStdrow++;
                        $tStdrowt++;
                    }
                    logHCgame($id, $tIsland->{'id'}, $name, islandName($tIsland), $lName, "${str1}", $goal, $tgoal,$island->{'hakoteam'},$tIsland->{'hakoteam'});
                    if($turn1 == 8) {
                        if($goal > $tgoal) {
                            logHCwintop($id, $name, int($HislandTurn / 100) * 100);
                        } elsif($goal < $tgoal) {
                            logHCwintop($tIsland->{'id'}, islandName($tIsland), int($HislandTurn / 100) * 100);
                        }
                    }
                    $tIsland->{'eisei4'} = "$tSto,$tStd,$tStk,$tStwin,$tStdrow,$tStlose,$tStwint,$tStdrowt,$tStloset,$tStyusho,$tStshoka";
                }
            }

            if ((($turn == 10) && ($stshoka == 1)) ||
                (($turn == 20) && ($stshoka == 2)) ||
                (($turn == 30) && ($stshoka == 3)) ||
                (($turn == 40) && ($stshoka == 4))) {
                logHCantiwin($id, $name, "予選第${stshoka}戦");
                $stwin++;
                $stwint++;
                $stshoka++;
            }
            if (($turn1 == 6) && ($stshoka < 6)) {
                $stshoka = 11;
            }
            if (($turn == 46) && ($stshoka == 6)) {
                $stwin++;
                $stwint++;
                $stshoka++;
                logHCantiwin($id, $name, '準々決勝戦');
            }
            if(($turn == 49) && ($stshoka == 7)) {
                $stwin++;
                $stwint++;
                $stshoka++;
                logHCantiwin($id, $name, '準決勝戦');
            }
            if(($turn == 51) && ($stshoka == 8)) {
                $stwin++;
                $stwint++;
                $stshoka++;
                $styusho++;
                logHCantiwin($id, $name, '決勝戦');
                my($value);
                $value = (($stwin * 3 + $stdrow) * 1000)*2;
                $island->{'money'} += $value;
                logHCwin($id, $name, 'とりあえずの優勝', "$value$HunitMoney");
                $hcturn = int($HislandTurn/100)*100;
                logHCwintop($id, $name, $hcturn);
            }

            if(($turn == 52) && ($stshoka != 9)) {
                $stshoka = 10;
            }
            if(($stshoka == 10) || ($stshoka == 11)) {
                my($stup);
                $stup = random(3);
                if($stup == 0) {
                    $sto++;
                } elsif($stup == 1) {
                    $std++;
                } else {
                    $stk++;
                }
            }
            $island->{'eisei4'} = "$sto,$std,$stk,$stwin,$stdrow,$stlose,$stwint,$stdrowt,$stloset,$styusho,$stshoka";

        } elsif ($landKind == $HlandGold) {
            # 金山
            my $DepletionPar = 7;
            my $value = $lv * 25 + random(501);
            $island->{'money'} += $value;

            # 収入ログ
            logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", '収益');

            # 枯渇判定
            if(random(100) < $DepletionPar) {
                # 枯渇
                logGoldEnd($id, $name, $lName, $this_pos);
                $land->[$x][$y] = $HlandMountain;
            }

        } elsif ($landKind == $HlandRottenSea) {
            # 腐海
            if ( ($island->{'BF_Flag'} == $HBF_MONSTER_HOUSE) ) {
                $land->[$x][$y] = $HlandPlains;
                $landValue->[$x][$y] = 0;
                $landValue2->[$x][$y] = 0;

            }else {
                my ($i, $sx, $sy, $kind, $lv);
                for ($i = 1; $i < 7; $i++) {
                    $sx = $x + $ax[$i];
                    $sy = $y + $ay[$i];

                    # 行による位置調整
                    $sx-- if(!($sy % 2) && ($y % 2));
                    # 範囲外
                    next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

                    my $sL = $land->[$sx][$sy];
                    my $sLv = $landValue->[$sx][$sy];
                    my $sLv2 = $landValue2->[$sx][$sy];
                    my $lName = landName($sL, $sLv, $sLv2);
                    # 海、海基、海底都市、海底新都市、船、海あみゅ、油田、養殖場、腐海以外
                    unless (   ($sL == $HlandSea)
                            || ($sL == $HlandSbase)
                            || ($sL == $HlandIce)
                            || ($sL == $HlandSeacity)
                            || ($sL == $HlandSeatown)
                            || ($sL == $HlandUmishuto)
                            || ($sL == $HlandFune)
                            || ($sL == $HlandFrocity)
                            || ($sL == $HlandUmiamu)
                            || ($sL == $HlandOil)
                            || ($sL == $HlandUmicity)
                            || ($sL == $HlandNursery)
                            || ($sL == $HlandYougan)
                            || ($sL == $HlandOmamori)
                            || ($sL == $HlandOilCity)
                            || ($sL == $HlandEgg)
                            || ($sL == $HlandRottenSea)
                            || (   ($sL == $HlandMonster)
                                && (isSeaMonster($sLv)) )
                                                          ) {
                        my ($n) = countAround($land, $sx, $sy, 7, $HlandRottenSea);
                        my ($point) = "($sx, $sy)";

                        if (   (($n >= 4) && (random(100) < 30))    # 周囲に腐海が４マス以上あれば30% の確率で飲み込む
                            || ($n && (random(100) < 10))) {        # 周囲に腐海が１マス以上あれば10% の確率で飲み込む
                            
                            logDamageAny($id, $name, $lName, $point, '<B>腐海</B>に飲み込まれました。');
                            SetRottenSea($island , $sx , $sy);
                        }
                    }
                }
            }

            my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
            $island->{'happy'} -= ($happy * 2);

        } elsif ($landKind == $HlandHouse) {
            # 島主の家
            my ($hlv);
            my ($zeikin);
            my ($tax) = 0;

            foreach (0..9) {
                $hlv = 9 - $_;
                last if($island->{'pts'} > $HouseLevel[$hlv]);
            }

            $island->{'turntax'} = 0;

            $landValue->[$x][$y] = $hlv;
            $zeikin = int($island->{'pop'} * ($hlv + 1) * $island->{'eisei1'} / 100);
            if ($zeikin > 10000) {
                if ($HislandTurn % 5 == 0) {
                    $tax = 1;
                }
                $island->{'turntax'} = int($zeikin / 5);
            } elsif ($zeikin > 5000) {
                if ($HislandTurn % 2 == 0) {
                    $tax = 1;
                }
                $island->{'turntax'} = int($zeikin / 2);
            } else {
                if ($zeikin > 0) {
                    $tax = 1;
                }
                $island->{'turntax'} = $zeikin;
            }

            if ($tax) {

                $island->{'money'} += $zeikin;
                $island->{'tax_income'} = $zeikin;
                logSecret("${HtagMoney_}${zeikin}${HunitMoney}${H_tagMoney}の税収がありました。",$id);
            }

            my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
            $island->{'happy'} += $happy;

        } elsif ($landKind == $HlandCollege) {
            # 大学
            # 各要素の取り出し
            my ($clv) = $landValue->[$x][$y];

            if (($clv == 99) && !$island->{'c28'}) {
                logMstakeoff($id, $name, $lName,$this_pos);
                $land->[$x][$y] = $HlandPlains;
                $landValue->[$x][$y] = 0;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }

            # 修復
            if ($landValue2->[$x][$y] > 0) {
                $landValue2->[$x][$y]--;
            }

            my ($monsno) = $island->{'monsterlive'};
            next if(!$monsno);

            $monsterCount = countAroundMonster_wo_Pet($island, $x, $y, 7) if ($island->{'monsterlive'});
            if ($monsterCount) {
                logMonsAttacks($id, $name, $lName, $this_pos);
                $landValue2->[$x][$y] += 1 + random(2);
            }

            my ($take) = 0;
            my ($i, $sx, $sy, $monsArray, $monspnt);
            $monsArray = $island->{'monspnt'};

            if ($clv == 4) {        # 生物大学
                for ($i = 0; $i < $monsno; $i++){
                    $monspnt = $monsArray->[$i];
                    ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                    if ($land->[$sx][$sy] == $HlandMonster) {
                        # 対象となる怪獣の各要素取り出し
                        my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                        # my($tlv) = $landValue->[$sx][$sy];
                        if ($tKind == 28) {

                        }
                        else {
                            my($ssx, $ssy, $i, $landKind, $lv, $point);
                            for($i = 1; $i < 7; $i++) {
                                $ssx = $sx + $ax[$i];
                                $ssy = $sy + $ay[$i];
                                # 行による位置調整
                                $ssx-- if(!($ssy % 2) && ($sy % 2));
                                # 範囲外判定
                                next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));

                                if (   (!$take)
                                    && ($land->[$ssx][$ssy] == $HlandWaste)
                                    && (!$island->{'c28'})) {
                                    my($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
                                    my $kind = 28;
                                    $landValue->[$ssx][$ssy] = ($kind << $Mons_Kind_Shift) + $mshp;
                                    $land->[$ssx][$ssy] = $HlandMonster;
                                    $landValue2->[$ssx][$ssy] = 0;
                                    $landValue3->[$ssx][$ssy] = 0;
                                    logMstakeon($id, $name, '生物大学のマスコットいのら',$this_pos);

                                    $landValue->[$x][$y] = 99;
                                    $take++;
                                    $island->{'co99'}++;
                                    $island->{'monsterlive'}++;
                                    last;
                                }
                            }
                        }
                    }
                    last if($take);
                }

            } elsif($clv == 98) {       # 生物大学
                for ($i = 0; $i < $monsno; $i++){
                    $monspnt = $monsArray->[$i];
                    ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});

                    if ($land->[$sx][$sy] == $HlandMonster) {
                        # 対象となる怪獣の各要素取り出し
                        my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                        # my($tlv) = $landValue->[$sx][$sy];
                        # my($tspecial) = $HmonsterSpecial[$tKind];
                        if ($tKind == 30) {

                        } else {

                            my ($ssx, $ssy, $i, $landKind, $lv, $point);
                            for ($i = 1; $i < 7; $i++) {
                                $ssx = $sx + $ax[$i];
                                $ssy = $sy + $ay[$i];
                                # 行による位置調整
                                $ssx-- if (!($ssy % 2) && ($sy % 2));
                                # 範囲外判定
                                next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));

                                if (!$take && ($land->[$ssx][$ssy] == $HlandWaste) && !$island->{'c28'}) {
                                    my($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
                                    my ($kind) = 30;
                                    $land->[$ssx][$ssy] = $HlandMonster;
                                    $landValue->[$ssx][$ssy] = ($kind << $Mons_Kind_Shift) + $mshp;
                                    $landValue2->[$ssx][$ssy] = 0;
                                    $landValue3->[$ssx][$ssy] = 0;
                                    logMstakeon($id, $name, '超神獣テトラ',$this_pos);

                                    $landValue->[$x][$y] = 99;
                                    $take++;
                                    $island->{'co99'}++;
                                    $island->{'monsterlive'}++;
                                    last;
                                }
                            }
                        }
                    }
                    last if($take);
                }
            }

        } elsif ($landKind == $HlandShrine) {
            # 時の神殿
            if($landValue->[$x][$y]) {
                # サーバートラブルなどでデータがなくなっていれば値を０に
                unless(-e "${HdirName}/savedata.$id") {
                    $landValue->[$x][$y] = 0 ;
                    logSaveLoadVanish($id, $name);
                }
            }
            unless((countAround($land, $x, $y, 7, $HlandForest) == 6) &&
                    (countAround($land, $x, $y, 19, $HlandSea , $HlandFrocity) == 12)) {
                # 周囲1Hexすべて森、さらにその周囲すべてが海(か浅瀬)の条件が崩れる
                unlink("${HdirName}/savedata.$id") if(-e "${HdirName}/savedata.$id");
                $land->[$x][$y] = $HlandMountain;
                $landValue->[$x][$y] = 0;
                $landValue2->[$x][$y] = 0;
            }

        } elsif($landKind == $HlandEgg) {
            # 卵復活
            my ($molv) = $landValue->[$x][$y];
            my @rflag = (5, 3, 3, 5);
            my @mflag = ([5, 25, 35, 25], [3, 20, 40, 15], [3, 30, 40, 30], [10, 25, 30, 30]);
            if(random(100) < $rflag[$molv]) {
                my ($i, $sx, $sy);
                for($i = 0; $i < 7; $i++) {
                    $sx = $x + $ax[$i];
                    $sy = $y + $ay[$i];
                    # 行による位置調整
                    $sx-- if(!($sy % 2) && ($y % 2));
                    # 範囲外
                    next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

                    my $sLname = landName($land->[$sx][$sy], $landValue->[$sx][$sy], $landValue2->[$sx][$sy]);
                    my ($mKind, $mName, $mHp);
                    # 範囲による分岐
                    if ($i < 1) {
                        # 中心、および1ヘックス
                        if (random(100) < $mflag[$molv][0]) {
                            $mKind = $Mons_Mikael;  # ミカエル
                        } elsif(random(100) < $mflag[$molv][1]) {
                            $mKind = $Mons_Tetra;  # テトラ
                        } elsif(random(100) < $mflag[$molv][2]) {
                            $mKind = $Mons_SlimeLegend;  # スラレジェ
                        } elsif(random(100) < $mflag[$molv][3]) {
                            $mKind = $Mons_HaneHamu;  # はねはむ
                        } else {
                            $mKind = $Mons_Inora;  # いのら(はずれ)
                        }

                        $mHp = $HmonsterBHP[$mKind] + random($HmonsterDHP[$mKind]);
                        my $sLv = ($mKind << $Mons_Kind_Shift) + $mHp;
                        $land->[$sx][$sy] = $HlandMonster;
                        $landValue->[$sx][$sy] = $sLv;
                        $landValue2->[$sx][$sy] = 0;
                        $island->{'monsterlive'}++;
                        logEggBomb($id, $name, $sLname, $HmonsterName[$mKind], "($sx, $sy)");

                    } else {
                        # 2ヘックス
                        if (($landKind == $HlandSea) ||
                            ($landKind == $HlandOil) ||
                            ($landKind == $HlandMountain) ||
                            ($landKind == $HlandGold) ||
                            ($landKind == $HlandOnsen) ||
                            ($landKind == $HlandSeacity) ||
                            ($landKind == $HlandUmishuto) ||
                            ($landKind == $HlandSeatown) ||
                            ($landKind == $HlandUmiamu) ||
                            ($landKind == $HlandSbase)  ) {

                            # なにもなし
                        }else{
                            logEggDamage($id, $name, $sLname, "($sx, $sy)");
                            SetSeaLand_Normal($island, $sx, $sy);     # 海に戻す
                        }
                    }
                }
            }

        } elsif($landKind == $HlandMonument) {      #記念碑イベント
            # 各要素の取り出し
            my($molv) = $landValue->[$x][$y];

            if(($molv == 0) || ($molv == 10) || ($molv == 15) || ($molv == 16) || ($molv == 33)) {
                if(random(100) < 5) {
                    # みやげ
                    my $value = 1+ random(49);
                    $island->{'money'} += $value;
                    logMiyage($id, $name, $lName, $this_pos, "$value$HunitMoney") if($value);
                }

            } elsif($molv == 1) {
                if(random(100) < 1) {
                    # 収穫
                    my $value = int($island->{'pop'} / 100) * 10+ random(11); # 人口１万人ごとに1000トンの収穫
                    #$island->{'food'} += $value;
                    food_product_plus($island , 'yasai' ,$value);
                    logParkEventt($id, $name, $lName, $this_pos, "$value$HunitFood") if($value);
                }

            } elsif($molv == 84) {                # 古代遺跡

                if(random(100) < 75) {
                    # 収穫
                    my ($nt) = countAround($land, $x, $y, 19, @Htowns);
                    my $value = random($nt * 20 + $lv * 5 + int($island->{'pop'} / 20)) + random(100) + 100;
                    if ($value > 0) {
                        $island->{'money'} += $value;
                        # 収入ログ
                        logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", '収益');
                    }
                }

                if(($island->{'shr'} < 1) &&
                    (countAround($land, $x, $y, 7, $HlandForest) == 6) &&
                    (countAround($land, $x, $y, 19, $HlandSea) == 12)) {
                    # 周囲1Hexすべて森、さらにその周囲すべてが海(か浅瀬)なら「時の神殿」になる
                    $land->[$x][$y] = $HlandShrine;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                }

            } elsif($molv == 93) {                # 幸運

                Mikael_Luck($island , $this_pos , $landKind , $lName);

            } elsif($molv == 95) {
                if(random(100) < 20) {
                    # 収穫
                    my $value = 1 + random(1234);
                    $island->{'money'} += $value;
                    logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", '収益');

                }
            }

            my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
            $island->{'happy'} += $happy;

        } elsif($landKind == $HlandYougan) {           # 溶岩イベント
            $landValue->[$x][$y]--;
            if ($landValue->[$x][$y] <= 0) {
                $land->[$x][$y] = $HlandWaste;
                $landValue->[$x][$y] = 0 ;
                $landValue2->[$x][$y] = 0 ;
                $landValue3->[$x][$y] = 0 ;
            }

        } elsif($landKind == $HlandOmamori) {           # お守り

            if(!$landValue->[$x][$y]) {
                $land->[$x][$y] = $HlandPlains;
                $landValue->[$x][$y] = 0;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

            } else {
                $landValue->[$x][$y]--;
            }

        } elsif($landKind == $HlandZoo) {               # 動物園

            my ($zookazu);
            my ($zookazus);
            my ($m_syurui);      #怪獣種類

            my ($tmp);
            my (@mons_list);
            $tmp = $island->{'zoo'};
            chomp($tmp);

            @mons_list = split(/\,/,$tmp);

            my ($kazu);
            my ($valuef);

            ($zookazu, $zookazus, $m_syurui) = Get_ZooState($island);

            # 1島に1回
            if ($zooflag > 0) {

            } else {

                $zooflag = 1;       # 1島に1回

                my ($value);
                $value  = ($zookazus * 15) + ($m_syurui * 150);
                $valuef = $zookazu * 250;                       # 食料消費

                # 電力による収入の低下
                # 電力ないためマスク
                #if($island->{'shouhi'} > $island->{'ene'}) {
                #    $value = int($value/10);
                #}

                # 仕入れ処理
                # $s08 ＝ 政策 はないので 0
                if (random(100) < 60 + 0) {

                    my ($i,$sx,$sy);
                    my ($zlv) = (0);
                    # 島の動物園サイズを合計する。
                    for ($i = 0; $i < $HpointNumber; $i++) {
                        $sx = $Hrpx[$i];
                        $sy = $Hrpy[$i];
                        if ($land->[$sx][$sy] == $HlandZoo) {
                            $zlv += $landValue->[$sx][$sy];
                        }
                    }

                    # 仕入れる怪獣選択
                    my ($siire);
                    my ($flag , $plus);
                    $siire = random($#HmonsterName);

                    $flag = GetTaijiFlag($island , $siire);

                    if (   ($flag)                      # 倒したことある怪獣
                        && ($zlv > $zookazu)            # 怪獣がまだ飼えるかどうか。
                        && (random(100) < $HmonsterZoo[$siire])
                                                                ) {

                        $plus = ($mons_list[$siire]) ? ($mons_list[$siire] + 1) : 1 ;
                        logSiire($id, $name, $lName, "$HmonsterName[$siire]", "($x, $y)");
                        Write_ZooState($island , $siire , $plus );
                    }

                }

                if (($value > 0) && ($zookazu > 0)) {
                    $island->{'money'} += $value;
                    food_product_consumption($island , $valuef);
                    # 収入ログ
                    my($str) = "$value$HunitMoney";
                    my($str2) = "$valuef$HunitFood";
                    logOilMoney2($id, $name, $lName, $this_pos, $str, $str2);
                }
            }

            my ($escape_par) = int( ((($zookazus * 25) - $island->{'rena'}) / 10) );

            if ($escape_par < 0) {
                $escape_par = 0;
            }

            if (   ($island->{'rena'} < ($zookazus * 25))
                && (random(100) < 15 + $escape_par)
                                        ) {

                my ($nigekaiju);
                my ($lp);
                my ($limit) = random($zookazu * 2);

                for ($lp = 1 ; $lp < $limit ; $lp++) {

                    if ($mons_list[$lp] > 0) {
                        $lp++;
                        $nigekaiju = $lp;
                    }
                }

                if ($mons_list[$nigekaiju] > 0) {

                    $mons_list[$nigekaiju] -= 1;
                    $lv = Calc_MonsterLandValue($nigekaiju);
                    $land->[$x][$y] = $HlandMonster;
                    $landValue->[$x][$y] = $lv;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    $island->{'monsterlive'}++;
                    my($mKind, $mName, $mHp) = monsterSpec($lv);
                    logNige($id, $name, $lName, $mName, $this_pos);
                    logMonsMove($id, $name, $lName, $this_pos, $mName , "に踏み荒らされました。");
                    Write_ZooState($island , $nigekaiju , $mons_list[$nigekaiju]);
                }
            }

        } elsif($landKind == $HlandBigFood) {           # お守り

            BigFoodEvent($island,$x,$y);

        } elsif($landKind == $HlandFrocity) {

            $monsterCount = CityAttack($island, $x, $y);
            $lv = $landValue->[$x][$y];

            if ($monsterCount > 0) {

                if ($lv <= 0) {

                    SetSeaLand_Normal($island, $x, $y);     # 海に戻す
                    next;
                }
            }

            if($addpop < 0) {
                # 不足
                $lv -= (random(-$addpop) + 1);
                if($lv <= 0) {

                    SetSeaLand_Normal($island, $x, $y);     # 海に戻す
                    next;
                }
            } else {
                # 成長
                $lv = Town_Growup( $lv , $addpop , $addpop2 , 100 );
            }
            if($lv > $HFrocity_limit) {
                $lv = $HFrocity_limit;
            }
            $landValue->[$x][$y] = $lv;

            # 動く方向を決定
            my($d, $sx, $sy);
            my($i);

            for($i = 0; $i < 3; $i++) {
                $d = random(6) + 1;
                $sx = $x + $ax[$d];
                $sy = $y + $ay[$d];

                # 行による位置調整
                if((($sy % 2) == 0) && (($y % 2) == 1)) {
                    $sx--;
                }

                # 範囲外判定
                if (   ($sx < 0) || ($sx > $islandSize)
                    || ($sy < 0) || ($sy > $islandSize)) {
                    next;
                }

                if (countAround($land, $sx, $sy, 19, $HlandShrine) > 0){
                    next;
                }

                # 海、海基、海底都市、油田、怪獣、山、記念碑以外
                if(   ($land->[$sx][$sy] == $HlandSea) ) {
                    last;
                }
            }

            if($i == 3) {
                # 動かなかった
                next;
            }

            # 動いた先の地形によりメッセージ
            my($l) = $land->[$sx][$sy];
            my($lv) = $landValue->[$sx][$sy];
            my($lv2) = $landValue2->[$sx][$sy];
            my($lName) = landName($l, $lv,$lv2);
            my($point) = "($sx, $sy)";

            # 移動
            $land->[$sx][$sy] = $land->[$x][$y];
            $landValue->[$sx][$sy] = $landValue->[$x][$y];
            $landValue2->[$sx][$sy] = $landValue2->[$x][$y];
            $landValue3->[$sx][$sy] = $landValue3->[$x][$y];

            # もと居た位置を海に
            SetSeaLand_Normal($island, $x, $y);     # 海に戻す

        } elsif($landKind == $HlandTrain) {     # 線路

            my ($rail) = $lv & $Train_Mask;

            if ($on_train == $train_sta) {

                $rail = $rail | $Train_Exist;
            }

            $landValue->[$x][$y] = $rail;
            $train_sta++;

        } elsif($landKind == $HlandFune) {      #船イベント
            # 船
            # すでに動いた後
            next if($funeMove[$x][$y] == 2);

            # 各要素の取り出し
            my($funespe) = $HfuneSpecial[$lv];
            my($mvalue, $tvalue, $fvalue, $fvalue2, $movalue) = (0, 0, 0, 0, 0);

            my($sinkflag) = ((($lv > 7) && ($lv < 11) || ($lv == 19)) ? 5 : 30);

            # 沈没判定
            if(random(1000) < $sinkflag) {
                # 事故のため沈没
                logDamageAny($id, $name, $lName, $this_pos, '事故のため沈没しました。');
                SetSeaLand_Normal($island, $x, $y);     # 海に戻す

                # 保険収入
                $mvalue = 1+ random(399);
                $island->{'money'} += $mvalue;
                logHoken($id, $name, $lName, $this_pos, "$mvalue$HunitMoney");
                next;
            }

            if(!$lv) { # 小型漁船(修正)
                $lv = 1;
                $landValue->[$x][$y] = 1;
            }

            if($lv == 1) { # 小型漁船
                $mvalue = -5; # 維持費
                $fvalue = 290+ random(30); # 収穫

            } elsif($lv == 2) { # 中型漁船
                $mvalue = -20; # 維持費
                $fvalue = 490+ random(40); # 収穫

            } elsif($lv == 3) { # 海底探査船
                $mvalue = -300; # 維持費
                if(random(1000) < 5) {
                    # 財宝発見(維持費免除)
                    $tvalue = 1 + random(49999);
                }

            } elsif($lv == 4) { # 帆船
                $mvalue = int((150+ random(250)) * $Hmoney2Incom[$Hmonth]/100); # 観光収入
                $fvalue2 = -1000; # 維持食料

            } elsif($lv == 5) { # 大型漁船
                $mvalue = -60; # 維持費
                $fvalue = 690+ random(40); # 収穫

            } elsif($lv == 6) { # 高速漁船
                $mvalue = -30; # 維持費
                $fvalue = 490+ random(40); # 収穫

            } elsif($lv == 7) { # 海底探査船・改
                $mvalue = -500; # 維持費
                if(random(100) < 1) {
                    # 財宝発見(維持費免除)
                    $tvalue = 500 + random(99999);
                }

            } elsif ($lv == 8) { # 豪華客船TITANIC
                $mvalue = int((1500 + int($island->{'pop'} / 10) * 1) * $Hmoney2Incom[$Hmonth]/100);    # 観光収入
                $fvalue2 = -3000; # 維持食料

                if (random(100) < 10) {
                    # 氷山
                    $land->[$x][$y] = $HlandIce;
                    $landValue->[$x][$y] = 0;
                    $movalue = int($island->{'pop'} / 10) * 2;    # 映画化
                }

            } elsif ($lv == 9) { # 戦艦RENAS
                $mvalue = -100; # 維持費

                my ($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};

                if ($monsno > 0) {
                    my($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for($i = 0; $i < $monsno; $i++){
                        last if($kougekiseigen > 1);        # 戦艦RENASは 1島につき、2発の攻撃ができる。
                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if($land->[$sx][$sy] == $HlandMonster){
                            my $value = 100;
                            $island->{'money'} -= $value;

                            # 対象となる怪獣の各要素取り出し
                            my($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                            my($tlv) = $landValue->[$sx][$sy];

                            # 対象が硬化中なら効果なし
                            next if (isMonsterCuring($tKind));

                            logMonsAttackt($id, $name, $lName, $this_pos, $tName, $tPoint);
                            $kougekiseigen++;

                            # 対象の体力を減らす
                            $tHp--;

                            if($tHp > 1){
                                $tlv--;
                                $landValue->[$sx][$sy] = $tlv;
                            } else {
                                # 対象の怪獣が倒れて荒地になる
                                MonsterDead($island , $sx , $sy , $tKind , 0 );
                                # 報奨金
                                AddMonsterReward($island , $tKind);
                            }
                            next;
                        }
                    }
                }

            } elsif($lv == 10) {    # 戦艦ERADICATE
                $mvalue = -400;     # 維持費

                my ($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};
                if ($monsno > 0) {
                    my ($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};

                    for ($i = 0; $i < $monsno; $i++) {

                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster) {
                            my $value = 3000;
                            $island->{'money'} -= $value;

                            # 対象となる怪獣の各要素取り出し
                            my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                            logFuneAttack($id, $name, $lName, $this_pos, $tName, "($sx, $sy)");

                            my ($ssx, $ssy, $i, $sLandKind, $sLandName, $sLv, $sLv2 ,$point);

                            my ($lp);
                            for($lp = 0; $lp < 7; $lp++) {
                                $ssx = $sx + $ax[$lp];
                                $ssy = $sy + $ay[$lp];

                                # 行による位置調整
                                $ssx-- if(!($ssy % 2) && ($sy % 2));

                                # 範囲外判定
                                next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));
                                if ( countAround($land, $ssx, $ssy, 19, $HlandShrine) > 0 ){
                                    next;
                                }

                                $sLandKind = $land->[$ssx][$ssy];
                                $sLv = $landValue->[$ssx][$ssy];
                                $sLv2 = $landValue2->[$ssx][$ssy];
                                $sLandName = landName($sLandKind, $sLv, $sLv2);
                                $point = "($ssx, $ssy)";

                                # 範囲による分岐
                                if($lp < 1) {
                                    # 中心
                                    SetSeaShallowLand($island , $ssx,$ssy);
                                    $island->{'monsterlive'} -= 1;
                                    logDamageAny($id, $name, $sLandName, $point, "吹き飛び水没しました。");
                                } else {
                                    # 1ヘックス
                                    if (NoDamage_by_Bomb1HEX($sLandKind)) {
                                        # ダメージのない地形
                                    } else {
                                        SetWasteLand_Normal($island , $ssx,$ssy);
                                        if($sLandKind == $HlandMonster) {
                                            $island->{'monsterlive'} -= 1;
                                            logDamageAny($id, $name, $sLandName, $point, "消し飛びました。");
                                        } else {
                                            logDamageAny($id, $name, $sLandName, $point, "一瞬にして<B>荒地</B>と化しました。");
                                        }
                                    }
                                }
                            }
                            next;
                        }
                    }
                }

            } elsif($lv == 11) { # 漁船MASTER
                $mvalue = -60; # 維持費
                $fvalue = 690+ random(40); # 収穫

            } elsif($lv == 19) { # 新型戦艦

                $mvalue = -1000; # 維持費

                my ($heat) = 0;
                my($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};
                if($monsno > 0) {
                    my ($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for($i = 0; $i < $monsno; $i++){
                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster) {

                            my $value = 50000;
                            $island->{'money'} -= $value;
                            # 対象となる怪獣の各要素取り出し
                            my($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                            logFuneAttackSSS($id, $name, $lName, $this_pos, $tName, "($sx, $sy)");
                            $land->[$sx][$sy] = $HlandWaste;
                            $landValue->[$sx][$sy] = 0;
                            $heat++;

                            my $rena = $island->{'rena'};
                            if (random($rena) > (3000 + $heat * 1000)) {
                                logFuneAttackSSSR($id, $name, $lName, $this_pos, $tName, "($sx, $sy)");
                            } else {
                                logFuneAttackSSST($id, $name, $lName, $this_pos, $tName, "($sx, $sy)");
                                my ($ssx, $ssy, $i, $sLandKind, $sLandName, $sLv, $sLv2, $point);
                                my ($lp);
                                for ($i = 0; $i < 7; $i++) {
                                    $ssx = $x + $ax[$i];
                                    $ssy = $y + $ay[$i];

                                    # 行による位置調整
                                    $ssx-- if(!($ssy % 2) && ($y % 2));

                                    # 範囲外判定
                                    next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));
                                    if ( countAround($land, $ssx, $ssy, 19, $HlandShrine) > 0 ){
                                        next;
                                    }
                                    $sLandKind = $land->[$ssx][$ssy];
                                    $sLv = $landValue->[$ssx][$ssy];
                                    $sLv2 = $landValue2->[$ssx][$ssy];
                                    $sLandName = landName($sLandKind, $sLv, $sLv2);
                                    $point = "($ssx, $ssy)";

                                    # 範囲による分岐
                                    if($i < 1) {
                                        # 中心
                                        SetSeaShallowLand($island , $ssx,$ssy);
                                        $island->{'monsterlive'} -= 1;
                                        logDamageAny($id, $name, $sLandName, $point, "吹き飛び水没しました。");
                                    } else {
                                        # 1ヘックス
                                        if (NoDamage_by_Bomb1HEX($sLandKind)) {
                                            # ダメージのない地形
                                        } else {
                                            SetWasteLand_Normal($island , $ssx,$ssy);
                                            if($sLandKind == $HlandMonster) {
                                                my ($tKind, $tname, $thp) = monsterSpec($sLv);
                                                MonsterDead($island , $ssx , $ssy , $tKind , 0 );
                                                logDamageAny($id, $name, $sLandName, $point, "消し飛びました。");
                                            } else {
                                                SetWasteLand_Normal($island , $ssx,$ssy);
                                                logDamageAny($id, $name, $sLandName, $point, "一瞬にして<B>荒地</B>と化しました。");
                                            }
                                        }
                                    }
                                }
                                next;
                            }
                        }
                    }
                }
            }

            # 観光収入、維持費
            $island->{'money'} += $mvalue;
            logOilMoney($id, $name, $lName, $this_pos, "$mvalue$HunitMoney", "観光収入") if($mvalue > 0);
            # 財宝
            $island->{'money'} += $tvalue;
            logTansaku($id, $name, $lName, $this_pos, "$tvalue$HunitMoney") if($tvalue);
            # 映画化
            $island->{'money'} += $movalue;
            logDamageAny($id, $name, $lName, $this_pos, "氷山に激突し真っ二つになり沈没しました。") if($movalue);
            logTitanicEnd($id, $name, $lName, $this_pos, "$movalue$HunitMoney") if($movalue);
            # 漁船
            $fvalue = int($fvalue * $Hfood2Incom[$month]/100);
            $fvalue2 = int($fvalue2 * $HeatenFoodS[$month]/100);
            food_product_consumption($island , -$fvalue2);
            food_product_plus($island , 'seafood' , $fvalue);
            logParkEventf($id, $name, $lName, $this_pos, "$fvalue$HunitFood") if(($fvalue + $fvalue2 > 0) && !$HlogOmit1);
            $island->{'fishcatch'} += $fvalue if($HlogOmit1);
            $island->{'fishcatch'} += $fvalue2 if($HlogOmit1 == 2);

            # 動く方向を決定
            my($d, $sx, $sy);
            my($i);
            for($i = 0; $i < 3; $i++) {
                $d = random(6) + 1;
                $sx = $x + $ax[$d];
                $sy = $y + $ay[$d];

                # 行による位置調整
                $sx-- if(!($sy % 2) && ($y % 2));
                # 範囲外判定
                next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));
                if ( countAround($land, $sx, $sy, 19, $HlandShrine) > 0 ){
                    next;
                }
                # 海なら移動
                last if($land->[$sx][$sy] == $HlandSea);
            }

            # 動かなかった
            next if($i == 3);

            # 移動
            $land->[$sx][$sy] = $land->[$x][$y];
            $landValue->[$sx][$sy] = $landValue->[$x][$y];
            $landValue2->[$sx][$sy] = $landValue2->[$x][$y];
            $landValue3->[$sx][$sy] = $landValue3->[$x][$y];
            # もと居た位置を海に
            SetSeaLand_Normal($island, $x, $y);     # 海に戻す

            if ( $island->{'oil'} < 10 ){
                if( (($lv == 3) && (random(100) < 2)) || # 油田見っけ
                    (($lv == 7) && (random(100) < 4)) ) {
                    logTansakuoil($id, $name, $lName, $this_pos);
                    $land->[$x][$y] = $HlandOil;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    $island->{'oil'}++;
                }
            }

            # 移動済みフラグ
            if($funespe == 2) {
                # 移動済みフラグは立てない
            } elsif($funespe) {
                # 速い船
                $funeMove[$sx][$sy] = $funeMove[$x][$y] + 1;
            } else {
                # 普通の船
                $funeMove[$sx][$sy] = 2;
            }

        } elsif ($landKind == $HlandFactory) {              # 工場 イベント

            FactoryEvent($island , $x , $y);

            if ($landValue2->[$x][$y] == 0) {
                my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
                $island->{'happy'} -= $happy;
            }

        } elsif ($landKind == $HlandGomi) {                 # ゴミイベント

            my ($kaisyu);
            my ($gomi_const) = 1500;
            my ($gomi_minus) = 5;
            my ($gomi_limit) = 800000;

            if ($landValue->[$x][$y] < $gomi_limit) {

                $kaisyu = ($island->{'gomi'} < $gomi_const) ? $island->{'gomi'} : $gomi_const;

                $island->{'gomi'} -= $kaisyu;
                $landValue->[$x][$y] += $kaisyu;
            }
            $landValue->[$x][$y] -= $gomi_minus;

        } elsif ($landKind == $HlandFoodim) {              # 食物研究所 イベント

            my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
            $island->{'happy'} -= $happy;

        } elsif ($landKind == $HlandMonster) {           # 怪獣 イベント
            next if ($monsterMove[$x][$y] == 2);
            # すでに動いた後

            # 各要素の取り出し
            my ($mKind, $mName, $mHp) = monsterSpec($lv);
            my ($special) = $HmonsterSpecial[$mKind];

            # ----------------------------------------- #
            # 移動できなくてもできる行動
            #
            # ----------------------------------------- #

            if ($mKind == $Mons_hime_inora) { # ひめいのら
                my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
                $mon += 1;

                if (   ($mon != 3)
                    || ($mday != 3)) {

                    $land->[$x][$y]      = $HlandBigFood;
                    $landValue->[$x][$y] = (3 << $Food_Kind_Shift) + 5;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    logHimeKaeru($id, $name, $mName);
                }
            }

            # ワープする？
            if (   ($special == 14)
                || ($special == 15)
                || ($special == 16)
                || ($special == 20)     # ひめいのら
                                    ) {

                my ($r) = random(100);
                my ($warp_par) = 60;

                $r = 0 if ($special == 16);                     # special 16は必ずワープ
                $r = 0 if ($special == 20);                     # special 20　ひめいのらは必ずワープ
                $r = 0 if ($island->{'pop'} < $HguardPop);      # $HguardPop 以下は必ずワープ
                # ワープする
                if ($r < $warp_par) { # 60%

                    my ($tIsland) = $island;                    # 移動先の島

                    $r = random(100);
                    # 50%の確率で他の島にもワープ
                    if (($r < 50) && ($special != 16)) {
                        my ($tar);
                        my ($ch_flag) = 0;
                        for ($tar = 0; $tar < $HislandNumber; $i++) {
                            $tIsland = $Hislands[random($HislandNumber)];
                            next if($tIsland->{'predelete'});
                            next if(($special == 20) && ($tIsland->{'BF_Flag'}));
                            next if(($special == 20) && ($Island->{'id'} == $tIsland->{'id'}));
                            $ch_flag = 1;
                            last;
                        }
                        $tIsland = $island if(!$ch_flag);
                    }

                    my ($tId)   = $tIsland->{'id'};

                    # ワープ地点を決める
                    my ($i, $bx, $by);
                    my ($tLand)      = $tIsland->{'land'};
                    my ($tLandValue) = $tIsland->{'landValue'};
                    my ($tLandValue2) = $tIsland->{'landValue2'};
                    my ($tLandValue3) = $tIsland->{'landValue3'};
                    my ($warped) = 0;

                    foreach $i (0..$pointNumber) {
                        $bx = $Hrpx[$i];
                        $by = $Hrpy[$i];

                        if ($special == 16) {           # ワープする ほかの島なし 最大２歩
                            if (MonsterWarpLanding($tIsland, $tLand->[$bx][$by], $tLandValue->[$bx][$by] ,$bx ,$by) ){
                                $warped = 1;
                                last;
                            }
                        } elsif ($special == 20) {      # 島ワープ＋もち
                            if (MonsterWarpLandingForQueen($tIsland, $tLand->[$bx][$by],$tLandValue->[$bx][$by] ,$bx ,$by) ){
                                $warped = 1;
                                last;
                            }
                        } else {
                            if (MonsterWarpLanding($tIsland, $tLand->[$bx][$by],$tLandValue->[$bx][$by] ,$bx ,$by) ){
                                $warped = 1;
                                last;
                            }
                        }
                    }
                    next if($warped == 0);

                    my ($tName) = islandName($tIsland);

                    # ワープ！
                    logMonsWarp($id, $name, $this_pos, $mName);
                    $island->{'monsterlive'} -= 1;
                    logMonsCome($tId, $tName, $mName, "($bx, $by)", landName($tLand->[$bx][$by], $tLandValue->[$bx][$by], $tLandValue2->[$bx][$by]));
                    $tIsland->{'monsterlive'} += 1;

                    # 行き先情報
                    my ($tland_before) = $tLand->[$bx][$by];
                    my ($tlv_before) = $tLandValue->[$bx][$by];
                    my ($tlv2_before) = $tLandValue2->[$bx][$by];
                    my ($tlv3_before) = $tLandValue3->[$bx][$by];

                    # コピー
                    $tLand->[$bx][$by]      = $land->[$x][$y];
                    $tLandValue->[$bx][$by] = $landValue->[$x][$y];
                    $tLandValue2->[$bx][$by] = $landValue2->[$x][$y];
                    $tLandValue3->[$bx][$by] = $landValue3->[$x][$y];

                    if ($special == 20) {
                        $land->[$x][$y]      = $HlandBigFood;
                        $landValue->[$x][$y] = (3 << $Food_Kind_Shift) + 3;
                        $landValue2->[$x][$y] = 0;
                        $landValue3->[$x][$y] = 0;
                    }
                    elsif ($mKind == $Mons_EnderInora) {
                        $land->[$x][$y]      = $tland_before;
                        $landValue->[$x][$y] = $tlv_before;
                        $landValue2->[$x][$y] = $tlv2_before;
                        $landValue3->[$x][$y] = $tlv3_before;
                    }
                    else {
                        $land->[$x][$y]      = $HlandWaste;
                        $landValue->[$x][$y] = 0;
                        $landValue2->[$x][$y] = 0;
                        $landValue3->[$x][$y] = 0;
                    }

                    # 周囲の地形を巻き込む
                    if (($special == 15) && (random(100) < 50)) { # 50%

                        my ($sx, $sy, $tx, $ty, $sKind, $sLv, $tKind, $tLv, $tLv2);
                        for ($i = 1; $i < 7; $i++) {
                            $sx = $x + $ax[$i];
                            $sy = $y + $ay[$i];
                            $tx = $bx + $ax[$i];
                            $ty = $by + $ay[$i];

                            $sx-- if(!($sy % 2) && ($y % 2));
                            $tx-- if(!($ty % 2) && ($by % 2));

                            if (($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)) {
                                $sKind = $HlandSea;
                                $sLv   = 0;
                            } else {
                                $sKind = $land->[$sx][$sy];
                                $sLv   = $landValue->[$sx][$sy];
                            }
                            if (($tx < 0) || ($tx > $islandSize) || ($ty < 0) || ($ty > $islandSize)) {
                                $tKind = $HlandSea;
                                $tLv   = 0;
                                $tLv2  = 0;
                            } else {
                                $tKind = $tLand->[$tx][$ty];
                                $tLv   = $tLandValue->[$tx][$ty];
                                $tLv2  = $tLandValue2->[$tx][$ty];
                            }

                            if (($sx >= 0) && ($sx < $HislandSize) && ($sy >= 0) && ($sy < $HislandSize)) {
                                # 範囲内の場合
                                $land->[$sx][$sy]      = $tKind;
                                $landValue->[$sx][$sy] = $tLv;
                                logMonsWarpLand($id, $name, landName($tKind, $tLv, $tLv2), "($sx, $sy)");
                            }
                            if (($tx >= 0) && ($tx < $HislandSize) && ($ty >= 0) && ($ty < $HislandSize)) {
                                # 範囲内の場合
                                $tLand->[$tx][$ty]      = $sKind;
                                $tLandValue->[$tx][$ty] = $sLv;
                                logMonsWarpLand($tId, $tName, landName($sKind, $sLv, $tLv2), "($tx, $ty)");
                            }
                        }
                    }
                    next;
                }
                else {

                    # ワープしない
                }
            }

            if ($special == 12) {
                # 瀕死になると爆発して広域被害を発生させる怪獣
                if ($mHp <= 1) { # 残り体力１なら
                    # 瀕死になったので爆発する
                    logMonsExplosion($id, $name, $this_pos, $mName);
                    $island->{'monsterlive'} -= 1;
                    wideDamage($id, $name, $land, $landValue, $x, $y);
                    next;
                }
            }

            if ($special == 13) {
                # 仲間を呼ぶ怪獣
                if (random(100) < 50) { # 50%

                    # 種類を決める
                    my ($nLv, $nKind,$lv2);
                    ($nKind,$lv2) = MonsterSpawnKind($island , 0);

                    # 怪獣出現
                    logMonsHelpMe($id, $name, $mName, $this_pos);

                    # lvの値を決める
                    $nLv = ($nKind << $Mons_Kind_Shift) + $HmonsterBHP[$nKind] + random($HmonsterDHP[$nKind]);

                    # どこに現れるか決める
                    my ($bx, $by, $i);
                    my ($check);
                    my ($tar_land);
                    foreach $i (0..$pointNumber) {
                        $bx = $Hrpx[$i];
                        $by = $Hrpy[$i];
                        $check = 0;
                        if (isSeaMonster($nKind)) {
                            if ($land->[$bx][$by] == $HlandSea) {
                                $check = 1;
                            }
                        }
                        else {
                            if (   ($land->[$bx][$by] == $HlandTown)
                                || ($land->[$bx][$by] == $HlandWaste)
                                || ($land->[$bx][$by] == $HlandPlains) ){
                                $check = 1;
                            }
                        }

                        if ($check) {
                            # 地形名
                            my ($lName) = landName($land->[$bx][$by], $landValue->[$bx][$by],$landValue2->[$bx][$by]);

                            # そのヘックスを怪獣に
                            $land->[$bx][$by] = $HlandMonster;      #移動
                            $landValue->[$bx][$by] = $nLv;
                            $landValue2->[$bx][$by] = 0;
                            $landValue3->[$bx][$by] = 0;

                            # 怪獣情報
                            my ($nName) = (monsterSpec($nLv))[1];

                            # メッセージ
                            logMonsCome($id, $name, $nName, "($bx, $by)", $lName);
                            $island->{'monsterlive'} += 1;
                            last;
                        }
                    }
                }
            }

            if ($mKind == $Mons_Mikael) { # 天使ミカエル
                # 幸運
                Mikael_Luck($island , $this_pos , $landKind , $lName);
            }

            # レトロ
            if ($special == 19) {
                my ($par) = 20;
                if (random(100) < $par) {
                    RetroBeam($island , $mName);
                }
            }

            # 硬化中?
            if (isMonsterCuring($mKind)) {
                # 硬化中
                next;

            } elsif(   ($mKind == $Mons_Queen_inora) 
                    && (   ($HislandTurn % 2) == 0)
                        && ($mHp < 4)
                        && (random(100) < 70) ) { # 魔獣クイーンいのら
                logMonsBomb($id, $name, $lName, $this_pos, $mName);
                # 広域被害ルーチン
                wideDamage($id, $name, $land, $landValue, $x, $y);
                if (random(1000) < 250) {
                    $land->[$x][$y] = $HlandMonument;
                    $landValue->[$x][$y] = 78;
                }

            } elsif($mKind == $Mons_f20) { # 人造怪獣f02
                my ($tx, $ty, $tL, $tLv, $tLv2);
                # 発射
                $tx = random($HislandSize);
                $ty = random($HislandSize);
                $tL = $land->[$tx][$ty];
                $tLv = $landValue->[$tx][$ty];
                $tLv2 = $landValue2->[$tx][$ty];

                if (random(1000) < 600) {

                    if (   ($tL == $HlandSea)
                        || ($tL == $HlandMountain)
                        || ($tL == $HlandGold)
                        || ($tL == $HlandShrine)
                        || ($tL == $HlandSeacity)
                        || ($tL == $HlandOnsen)
                        || ($tL == $HlandIce)
                        || ($tL == $HlandUmishuto)
                        || ($tL == $HlandSeatown)
                        || ($tL == $HlandUmiamu)
                        || ($tL == $HlandSbase)
                                                ) {
                        logMekaAttack($id, $name, $mName, $this_pos, landName($tL, $tLv,$tLv2), "($tx, $ty)", "ミサイル");
                        next;
                    }

                    logMekaAttack($id, $name, $mName, $this_pos, landName($tL, $tLv,$tLv2), "($tx, $ty)", "ミサイル", "一帯が壊滅し");

                    if (   ($tL == $HlandOil)
                        || ($tL == $HlandFune)
                        || ($tL == $HlandNursery)
                        || ($tL == $HlandFrocity)
                        || ($tL == $HlandUmicity)
                        || ($tL == $HlandOilCity)
                                                    ) {
                        # 海になる地形
                        $land->[$tx][$ty] = $HlandSea;
                        $landValue->[$tx][$ty] = 0;
                        $landValue2->[$tx][$ty] = 0;
                        $landValue3->[$tx][$ty] = 0;

                    }
                    else {

                        $land->[$tx][$ty] = $HlandWaste;
                        $landValue->[$tx][$ty] = 1;
                        $landValue2->[$tx][$ty] = 0;
                        $landValue3->[$tx][$ty] = 0;
                    }

                }
                elsif (random(1000) < 400) {

                    logMekaAttack($id, $name, $mName, $this_pos, landName($tL, $tLv,$tLv2), "($tx, $ty)", "${HtagDisaster_}多弾頭ミサイル${H_tagDisaster}");
                    my ($ssx, $ssy, $i, $ssL, $ssLv, $ssLv2);
                    for ($i = 0; $i < 7; $i++) {
                        $ssx = $tx + $ax[$i];
                        $ssy = $ty + $ay[$i];

                        # 行による位置調整
                        $ssx-- if(!($ssy % 2) && ($ty % 2));

                        # 範囲外判定
                        next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));

                        $ssL = $land->[$ssx][$ssy];
                        $ssLv = $landValue->[$ssx][$ssy];
                        $ssLv2 = $landValue2->[$ssx][$ssy];

                        # 範囲による分岐
                        if ($i < 1) {
                            # 中心
                            if (   ($ssL == $HlandSea)
                                || ($ssL == $HlandSeacity)
                                || ($ssL == $HlandSeatown)
                                || ($ssL == $HlandUmishuto)
                                || ($ssL == $HlandUmiamu)
                                || ($ssL == $HlandSbase)
                                                            ) {
                                next;
                            }
                            logDamageAny($id, $name, landName($ssL, $ssLv,$ssLv2), "($ssx, $ssy)", "吹き飛び水没しました。");
                            SetSeaShallowLand($island,  $ssx , $ssy);
                        }
                        else {
                            # 1ヘックス
                            if (NoDamage_by_Bomb1HEX($sL) ) {
                                # ダメージのない地形
                                next;
                            }
                            elsif ($sL == $HlandMonster) {
                                my ($tKind, $tName, $tHp) = monsterSpec($ssLv);
                                logDamageAny($id, $name, landName($ssL, $ssLv,$ssLv2), "($ssx, $ssy)", "消し飛びました。");
                                MonsterDead($island , $ssx , $ssy , $tKind , 0);
                            }
                            else {
                                logDamageAny($id, $name, landName($ssL, $ssLv,$ssLv2), "($ssx, $ssy)", "一瞬にして<B>荒地</B>と化しました。");
                                SetWasteLand_Normal($island,  $ssx , $ssy);
                            }
                        }
                    }

                } elsif(random(1000) < 200) {
                    my($sx, $sy, $sL, $sLv, $sLv2);
                    # 落下
                    $sx = random($HislandSize);
                    $sy = random($HislandSize);
                    $sL = $land->[$sx][$sy];
                    $sLv = $landValue->[$sx][$sy];
                    $sLv2 = $landValue2->[$sx][$sy];
                    # メッセージ
                    logMekaAttack($id, $name, $mName, $this_pos, landName($sL, $sLv, $sLv2), "($sx, $sy)", "${HtagDisaster_}アトミック☆ボム${H_tagDisaster}", "大爆発し");
                    # 広域被害ルーチン
                    wideDamage($id, $name, $land, $landValue, $sx, $sy);
                }

            } elsif($mKind == $Mons_Uriel) { # 天使ウリエル

                my ($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};
                if ($monsno > 0) {
                    my($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for ($i = 0; $i < $monsno; $i++){
                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster) {
                            # 島に別の怪獣がいる場合、その怪獣を攻撃する

                            # 対象となる怪獣の各要素取り出し
                            my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                            my ($tlv) = $landValue->[$sx][$sy];

                            if (isMonsterCuring($tKind)) {
                                # 対象が硬化中なら効果なし
                                next;
                            }
                            if (random(1000) < 600) {
                                if (   ($tKind == 28)
                                    || ($tKind == 30)) {

                                    logItiAttackms($id, $name, $mName, $this_pos, $tName, "($sx, $sy)");
                                    my ($dmge) = random(4);
                                    $tHp -= $dmge;
                                    $tlv -= $dmge;
                                    $landValue->[$sx][$sy] = $tlv;

                                    if ($tHp < 1){
                                        # 対象の怪獣が倒れて荒地になる
                                        MonsterDead($island , $sx , $sy , $tKind , 0);
                                        # 報奨金
                                        AddMonsterReward($island , $tKind);
                                    }
                                } elsif ($tKind != $Mons_Uriel) { # 天使ウリエル
                                    logItiAttack($id, $name, $mName, $this_pos, $tName, "($sx, $sy)");

                                    # 対象の怪獣が倒れて荒地になる
                                    MonsterDead($island , $sx , $sy , $tKind , 0);
                                    # 報奨金
                                    AddMonsterReward($island , $tKind);
                                }
                            }
                        }
                    }

                    if (random(1000) < 600) {
                        my ($tx, $ty, $tL, $tLv,$tLv2);
                        # 発射
                        $tx = random($HislandSize);
                        $ty = random($HislandSize);
                        $tL = $land->[$tx][$ty];
                        $tLv = $landValue->[$tx][$ty];
                        $tLv2 = $landValue2->[$tx][$ty];

                        if (   ($tL == $HlandSea)
                            || ($tL == $HlandMountain)
                            || ($tL == $HlandShrine)
                            || ($tL == $HlandGold)
                                                    ) {
                            next;
                        }
                        SetSeaShallowLand($island, $tx , $ty);
                        logUrieruMeteo($id, $name, $mName, $this_pos, landName($tL, $tLv,$tLv2), "($tx, $ty)");
                        if (random(1000) < 100) {
                            $land->[$tx][$ty] = $HlandMonument;
                            $landValue->[$tx][$ty] = 79;
                            $landValue2->[$tx][$ty] = 0;
                        }
                    }
                }

            } elsif ($mKind == $Mons_Ice_scorpion) { # アイススコーピオン
                my ($i, $sx, $sy);
                foreach $i (0..$pointNumber) {
                    $sx = $Hrpx[$i];
                    $sy = $Hrpy[$i];
                    if ($land->[$sx][$sy] == $HlandMonster) {
                        # 島に別の怪獣がいる場合、その怪獣を攻撃する

                        # 対象となる怪獣の各要素取り出し
                        my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                        my ($tlv) = $landValue->[$sx][$sy];
                        # my($tSpecial) = $HmonsterSpecial[$tKind];

                        if (isMonsterCuring($tKind)) {
                            # 対象が硬化中なら効果なし
                            next;
                        }
                        if (random(1000) < 600) {
                            if (($tKind == $Mons_Mascot_inora) || ($tKind == $Mons_SuperTetra)) {
                                logIceAttack($id, $name, $mName, $this_pos, $tName, "($sx, $sy)");
                                my ($dmge) = random(4);
                                $tHp -= $dmge;
                                $tlv -= $dmge;
                                $landValue->[$sx][$sy] = $tlv;

                                if ($tHp < 1){
                                    # 対象の怪獣が倒れて氷河になる
                                    $land->[$sx][$sy] = $HlandIce;
                                    $landValue->[$sx][$sy] = 0;
                                    $landValue2->[$sx][$sy] = 0;
                                    $landValue3->[$sx][$sy] = 0;
                                    $island->{'monsterlive'} -= 1;
                                    # 報奨金
                                    AddMonsterReward($island,$tKind);
                                }
                            }
                            elsif($tKind != $Mons_Ice_scorpion) {
                                logIceAttack($id, $name, $mName, $this_pos, $tName, "($sx, $sy)");

                                # 対象の怪獣が倒れて氷河になる
                                $land->[$sx][$sy] = $HlandIce;
                                $landValue->[$sx][$sy] = 0;
                                $island->{'monsterlive'} -= 1;

                                if (random(1000) < 100) {
                                    $land->[$sx][$sy] = $HlandMonument;
                                    $landValue->[$sx][$sy] = 76;
                                }
                                # 報奨金
                                AddMonsterReward($island,$tKind);
                            }
                        }

                    } elsif(($land->[$sx][$sy] == $HlandBase) ||
                        ($land->[$sx][$sy] == $HlandDefence) ||
                        ($land->[$sx][$sy] == $HlandOil) ||
                        ($land->[$sx][$sy] == $HlandFune)) {
                        # 島にあるミサイル基地、防衛施設、油田、船舶を氷山か氷石にする

                        if (random(1000) < 200) {
                            my $tKind = $land->[$sx][$sy];
                            my $tlv = $landValue->[$sx][$sy];
                            my $tlv2 = $landValue2->[$sx][$sy];
                            logIceAttack($id, $name, $mName, $this_pos, landName($tKind, $tlv,$tlv2), "($sx, $sy)");
                            $land->[$sx][$sy] = $HlandIce;
                            $landValue->[$sx][$sy] = 0;
                            if (random(1000) < 100) {
                                $land->[$sx][$sy] = $HlandMonument;
                                $landValue->[$sx][$sy] = 76;
                            }
                        }
                    }
                }

            } elsif ($mKind == $Mons_Alfr) { # 魔術師アールヴ

                if (random(1000) < 300) {
                    logMgSpel($id, $name, $mName, "($x, $y)", "禁呪メテオ");
                    $HdisMeteo[$Hmonth] = 500;
                    my ($sx, $sy, $sL, $sLv, $sLv2, $first, $sName);
                    $first = 1;
                    while (!random(2) || $first) {
                        $first = 0;
                        # 落下
                        $sx = random($HislandSize);
                        $sy = random($HislandSize);
                        $sL = $land->[$sx][$sy];
                        $sLv = $landValue->[$sx][$sy];
                        $sLv2 = $landValue2->[$sx][$sy];
                        $sName = landName($sL, $sLv,$sLv2);

                        next if($sL == $HlandHugeMonster);

                        if ( ($sL == $HlandSea) && ($sLv == 0)){
                            # 海ポチャ
                            logMeteo($id, $name, $sName, "($sx, $sy)", "し");
                        }
                        elsif (($sL == $HlandMountain) || ($sL == $HlandGold) || ($sL == $HlandShrine) || ($sL == $HlandOnsen)){
                            # 山破壊
                            logMeteo($id, $name, $sName, "($sx, $sy)", "、<B>$sName</B>は消し飛び");
                            SetWasteLand_Normal($island,$sx,$sy);
                            next;
                        }
                        elsif (   ($sL == $HlandSbase)
                               || ($sL == $HlandSeacity)
                               || ($sL == $HlandSeatown)
                               || ($sL == $HlandUmishuto)
                               || ($sL == $HlandFrocity)
                               || ($sL == $HlandFune)
                               || ($sL == $HlandUmiamu)) {

                            logMeteo($id, $name, $sName, "($sx, $sy)", "、<B>$sName</B>は崩壊し");
                        }
                        elsif ($sL == $HlandMonster) {
                            $island->{'monsterlive'} -= 1;
                            logMeteoMonster($id, $name, $sName, "($sx, $sy)");
                        }
                        elsif (($sL == $HlandSea) || ($sL == $HlandIce)) {
                            # 浅瀬
                            logMeteo($id, $name, $sName, "($sx, $sy)", "、海底がえぐられ");
                        }
                        else {
                            logMeteo($id, $name, $sName, "($sx, $sy)", "、一帯が水没し");
                        }
                        SetSeaLand_Normal($island,$sx,$sy);
                    }
                }

                if (random(1000) < 200) {
                    logMgSpel($id, $name, $mName, "($x, $y)", "禁呪メテオ");
                    $HdisMeteo[$Hmonth] = 300;
                    my ($sx, $sy);
                    # 落下
                    $sx = random($HislandSize);
                    $sy = random($HislandSize);
                    # メッセージ
                    logHugeMeteo($id, $name, "($sx, $sy)");
                    # 広域被害ルーチン
                    wideDamage($id, $name, $land, $landValue, $sx, $sy);
                }

                if (random(1000) < 400) {
                    logMgSpel($id, $name, $mName, "($x, $y)", "クエイク");
                    $HdisEarthquake[0] = 500;
                    # 地震発生
                    logEarthquake($id, $name);
                    my ($sx, $sy, $sL, $sLv, $sLv2, $i);
                    foreach $i (0..$pointNumber) {
                        $sx = $Hrpx[$i];
                        $sy = $Hrpy[$i];
                        $sL = $land->[$sx][$sy];
                        $sLv = $landValue->[$sx][$sy];
                        $sLv2 = $landValue2->[$sx][$sy];

                        if ((($sL == $HlandTown) && ($sLv >= 100)) ||
                            (($sL == $HlandFoodim) && ($sLv < 480)) ||
                            (($sL == $HlandProcity) && ($sLv < 130)) ||
                            (($sL == $HlandNewtown) && ($sLv < 300)) ||
                            (($sL == $HlandBigtown) && ($sLv < 300)) ||
                            (($sL == $HlandHTFactory) && ($sLv < 500)) ||
                            (($sL == $HlandSHTF) && ($sLv < 500)) ||
                            ($sL == $HlandRizort) ||
                            ($sL == $HlandBigRizort) ||
                            ($sL == $HlandHaribote) ||
                            ($sL == $HlandTrain) ||
                            ($sL == $HlandPark) ||
                            ($sL == $HlandMinato) ||
                            ($sL == $HlandKyujo) ||
                            ($sL == $HlandKyujokai) ||
                            ($sL == $HlandKatorikun) ||
                            ($sL == $HlandOnsen) ||
                            ($sL == $HlandFactory)) {
                            # 1/4で壊滅
                            if (!random(4)) {
                                logDamageAny($id, $name, landName($sL, $sLv, $sLv2), "($sx, $sy)", "${HtagDisaster_}地震${H_tagDisaster}により壊滅しました。");
                                if ($sL == $HlandOnsen) {
                                    # 温泉は山に戻る
                                    SetMountain_Normal($island,$sx,$sy);
                                }
                                else {
                                    SetWasteLand_Normal($island,$sx,$sy);
                                }
                            }
                        }
                    }
                }

                my ($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};
                if ($monsno > 0) { # ドレイン
                    my ($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for ($i = 0; $i < $monsno; $i++) {
                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster){
                            my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                            my ($tlv) = $landValue->[$sx][$sy];
                            # my($tSpecial) = $HmonsterSpecial[$tKind];
                            if ($tKind != 19) {
                                if ($tHp > $mHp) {
                                    next if (isMonsterCuring($tKind));

                                    logMgDrain($id, $name, $mName, $tName, "($x, $y)");
                                    $tlv -= ($tHp-$mHp);
                                    $landValue->[$sx][$sy] = $tlv;
                                    $lv += ($tHp-$mHp) if($mHp < 9);
                                    $landValue->[$x][$y] = $lv;
                                }
                                next;
                            }
                        }
                    }
                    my ($nKind, $nName, $nHp) = monsterSpec($landValue->[$x][$y]);
                    $nKind = 21 if ($nKind > 21);
                    $nHp = 1 if ($nHp < 1);
                    $landValue->[$x][$y] = ($nKind << $Mons_Kind_Shift) + $nHp;
                }

            } elsif ($mKind == $Mons_Ethereal) { # 堕天使イセリア
                $lv += 2;
                $landValue->[$x][$y] = $lv;
                ($mKind, $mName, $mHp) = monsterSpec($lv);

                if (random(1000) < 200) {
                    food_product_Random_consumption($island , int($island->{'food'} / 2));
                    logFushoku($id, $name, $mName, "($x, $y)");
                }
                if ($mHp > 13) {
                    logUmlimit($id, $name, $mName, "($x, $y)");
                    # 広域被害ルーチン
                    wideDamage($id, $name, $land, $landValue, $x, $y);
                    my ($sx, $sy, $sL, $sLv, $sLv2, $i);
                    foreach $i (0..$pointNumber) {
                        $sx = $Hrpx[$i];
                        $sy = $Hrpy[$i];
                        $sL = $land->[$sx][$sy];
                        $sLv = $landValue->[$sx][$sy];
                        $sLv2 = $landValue2->[$sx][$sy];

                        if (   (($sL == $HlandTown) && ($sLv >= 100))
                            || (($sL == $HlandFoodim) && ($sLv < 480))
                            || (($sL == $HlandProcity) && ($sLv < 130))
                            || ($sL == $HlandHaribote)
                            || ($sL == $HlandTrain)
                            || ($sL == $HlandPark)
                            || ($sL == $HlandMinato)
                            || ($sL == $HlandKyujo)
                            || ($sL == $HlandKyujokai)
                            || ($sL == $HlandBase)
                            || ($sL == $HlandFactory) ) {
                            # 1/6で壊滅
                            if (!random(6)) {

                                logUmlimitDamage($id, $name, $mName, landName($sL, $sLv, $sLv2), "($sx, $sy)");
                                $land->[$sx][$sy] = $HlandWaste;
                                $landValue->[$sx][$sy] = 0;
                                $landValue2->[$sx][$sy] = 0;
                                $landValue3->[$sx][$sy] = 0;
                                if (random(1000) < 150) {
                                    $land->[$sx][$sy] = $HlandMonument;
                                    $landValue->[$sx][$sy] = 74;
                                    $landValue2->[$sx][$sy] = 0;
                                    $landValue3->[$sx][$sy] = 0;
                                }
                            }
                        }
                    }
                    # 魔王サタンに変身
                    $mKind = 21;
                    $lv = ($mKind << $Mons_Kind_Shift) + $HmonsterBHP[$mKind] + random($HmonsterDHP[$mKind]);
                    $land->[$x][$y] = $HlandMonster;
                    $landValue->[$x][$y] = $lv;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                }

            } elsif ($mKind == $Mons_Satan) { # 魔王サタン
                $lv += 3 if ($mHp < 9);
                $landValue->[$x][$y] = $lv;
                if (random(1000) < 150) {
                    $island->{'money'} -= int($island->{'money'} / 2);
                    logKyoukou($id, $name, $mName, "($x, $y)");
                }
                if (random(1000) < 200) {
                    food_product_All_Clear($island);
                    logFushoku($id, $name, $mName, "($x, $y)");
                }

                my ($i,$sx,$sy,$tkind);
                foreach $i (0..$pointNumber) {
                    $sx = $Hrpx[$i];
                    $sy = $Hrpy[$i];
                    $tkind = $land->[$sx][$sy];
                    if (   ($land->[$sx][$sy] == $HlandPlains)
                        || ($land->[$sx][$sy] == $HlandForest)
                        || ($land->[$sx][$sy] == $HlandNursery)
                        || ($land->[$sx][$sy] == $HlandFarmchi)
                        || ($land->[$sx][$sy] == $HlandFarmpic)
                        || ($land->[$sx][$sy] == $HlandFarmcow)
                        || ($land->[$sx][$sy] == $HlandRottenSea)) {
                        # 島にある平地、森、養殖場、養鶏場、養豚場、牧場、腐海を荒地か闇石か炎石にする
                        my ($tlv) = $landValue->[$sx][$sy];
                        my ($tlv2) = $landValue2->[$sx][$sy];
                        my ($tlv3) = $landValue3->[$sx][$sy];

                        if (random(1000) < 200) {
                            logHellAttack($id, $name, $mName, "($x, $y)", landName($tkind, $tlv, $tlv2), "($sx, $sy)");
                            if ($tkind == $HlandNursery) {

                                $land->[$sx][$sy] = $HlandSea;
                                $landValue->[$sx][$sy] = 1;
                                $landValue2->[$sx][$sy] = 0;
                            }
                            else {

                                SetWasteLand_Normal($island , $sx , $sy);
                            }
                            if (random(1000) < 100) {

                                $land->[$sx][$sy] = $HlandMonument;
                                $landValue->[$sx][$sy] = 78;
                            }
                            elsif (random(1000) < 100) {

                                $land->[$sx][$sy] = $HlandMonument;
                                $landValue->[$sx][$sy] = 74;
                            }
                        }
                    }
                }
            }
            elsif ($mKind == $Mons_SuperTetra) { # 超神獣テトラ

                if ($island->{'monsterlive'} == $island->{'c28'}) {
                    # テトラちゃんだけ？
                    if ($island->{'co99'} == 0) {
                        logMstakeiede($id, $name, "出撃中の超神獣テトラ","($x, $y)",landName($landKind, $lv,$lv2));
                    }
                    else {
                        my ($i,$sx,$sy);
                        foreach $i (0..$pointNumber) {
                            $sx = $Hrpx[$i];
                            $sy = $Hrpy[$i];
                            $landKind = $land->[$sx][$sy];
                            $lv = $landValue->[$sx][$sy];
                            $lv2 = $landValue2->[$sx][$sy];
                            $landName = landName($landKind, $lv,$lv2,$landValue3->[$sx][$sy]);

                            if (   ($land->[$sx][$sy] == $HlandCollege)
                                && ($lv == 99) ) {

                                $landValue->[$sx][$sy] = 98;
                                $island->{'monsterlive'} -= 1;
                                logMstakeokaeri($id, $name, "出撃中の超神獣テトラ","($sx, $sy)",$landName);
                                last;
                            }
                        }
                    }
                    SetWasteLand_Normal($island , $x , $y);
                }

                my ($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};
                if ($monsno > 0) {

                    my ($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for ($i = 0; $i < $monsno; $i++) {

                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster) {

                            if ($msseigen < 1) {
                                # 島に別の怪獣がいる場合、その怪獣を攻撃する

                                # 対象となる怪獣の各要素取り出し
                                my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                                my ($tlv) = $landValue->[$sx][$sy];
                                # my ($tSpecial) = $HmonsterSpecial[$tKind];

                                if (   ($tKind == $Mons_SuperTetra)
                                    || ($tKind == $Mons_hime_inora) ) {

                                }
                                else {
                                    my ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
                                    my ($m_str) = $HmonsterSTR[$tKind];

                                    $mHp = $mshp;

                                    my ($attackdamege , $counterdamege) = PetAttackCalc($island , 1);

                                    logMsAttackt($id, $name, "超神獣テトラ", $attackdamege, $counterdamege, $tName, $tPoint);
                                    $msseigen++;
                                    $tHp -= $attackdamege;
                                    $tlv -= $attackdamege;
                                    $landValue->[$sx][$sy] = $tlv;
                                    $mHp -= $counterdamege;
                                    $lv = Calc_MonsterLandValue_HP($mKind , $mHp);
                                    $landValue->[$x][$y] = $lv;

                                    if ($tHp < 1) {
                                        # 対象の怪獣が倒れて荒地になる
                                        MonsterDead( $island , $sx , $sy , $tKind , 0 );
                                        if ($tKind == $Mons_Mikael) {
                                            SetMonument_Normal($island , $sx , $sy , 93);
                                            logMsAttackmika($id, $name, "超神獣テトラ", $attackdamege, $counterdamege, $tName);
                                        }
                                        # 報奨金
                                        AddMonsterReward($island , $tKind);
                                        my ($value) = $HmonsterValue[$tKind];

                                        if (random(1000) < $value) {
                                            if (random(100) < 30) {
                                                $msap++;
                                            } elsif (random(100) < 30) {
                                                $msdp++;
                                            } elsif (random(100) < 30) {
                                                $mssp++;
                                            } else {
                                                $mshp++;
                                                $mshp = 15 if($mshp > 15);
                                            }
                                        }

                                        $msexe += $HmonsterExp[$tKind];
                                        $mswin ++;
                                        $island->{'eisei5'} = "$mshp,$msap,$msdp,$mssp,$mswin,$msexe,$tet";

                                        # 怪獣退治数
                                        TaijiPrize($island , $tKind);
                                    }

                                    if ($mHp < 1){
                                        # 超神獣テトラが倒れて荒地になる
                                        MonsterDead( $island , $x , $y , $mKind , 0 );
                                        # 報奨金
                                        AddMonsterReward($island , $mKind);
                                    }
                                }
                            }
                            else {
                                last;
                            }
                        }
                    }
                }

            } elsif ($mKind == $Mons_Tetra) { #神獣テトラ

                if ($island->{'monsterlive'} == 1){
                    # 今テトラちゃんだけ？
                    if ($island->{'co99'} == 0){

                    }
                    else {

                        my($i,$sx,$sy);
                        # 帰る大学を探す
                        foreach $i (0..$pointNumber) {
                            $sx = $Hrpx[$i];
                            $sy = $Hrpy[$i];
                            $landKind = $land->[$sx][$sy];
                            $lv = $landValue->[$sx][$sy];
                            if (   ($landKind == $HlandCollege)
                                && ($lv == 99) ) {

                                $landValue->[$sx][$sy] = 98;

                                # もといた場所を荒地に
                                $landName = landName($landKind, $lv,$landValue2->[$sx][$sy],$landValue3->[$sx][$sy]);
                                SetWasteLand_Normal($island , $x , $y);
                                logMstakeokaeri($id, $name, "テトラ","($sx, $sy)",$landName);
                                last;
                            }
                        }
                    }
                }

            } elsif ($mKind == $Mons_Mascot_inora) {

                if ($island->{'monsterlive'} == $island->{'c28'}) {
                    # マスコットいのらちゃんだけ？
                    if ($island->{'co99'} == 0){
                        logMstakeiede($id, $name, '出撃中のマスコットいのら',"($x, $y)",landName($landKind, $lv,$lv2));
                    } else {
                        my($i,$sx,$sy);
                        foreach $i (0..$pointNumber) {
                            $sx = $Hrpx[$i];
                            $sy = $Hrpy[$i];
                            $landKind = $land->[$sx][$sy];
                            $lv = $landValue->[$sx][$sy];
                            $lv2 = $landValue2->[$sx][$sy];
                            $landName = landName($landKind, $lv,$lv2,$landValue3->[$sx][$sy]);

                            if (   ($land->[$sx][$sy] == $HlandCollege)
                                && ($lv == 99) ){
                                $landValue->[$sx][$sy] = 4;
                                $island->{'monsterlive'} -= 1;
                                logMstakeokaeri($id, $name, '出撃中のマスコットいのら',"($sx, $sy)",$landName );
                                last;
                            }
                        }
                    }
                    SetWasteLand_Normal($island,$x,$y);     # $HlandWaste
                }

                my ($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};

                if ($monsno > 0) {
                    my ($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for ($i = 0; $i < $monsno; $i++) {

                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster){
                            if ($msseigen < 1) {
                                # 島に別の怪獣がいる場合、その怪獣を攻撃する

                                # 対象となる怪獣の各要素取り出し
                                my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                                my ($tlv) = $landValue->[$sx][$sy];
                                my ($tSpecial) = $HmonsterSpecial[$tKind];

                                if (   ($tKind == $Mons_Mascot_inora)
                                    || ($tKind == $Mons_hime_inora) ) {

                                }
                                else {
                                    my ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
                                    my ($m_str) = $HmonsterSTR[$tKind];

                                    $mHp = $mshp;

                                    my ($attackdamege , $counterdamege) = PetAttackCalc($island , 1);

                                    logMsAttackt($id, $name, 'マスコットいのら', $attackdamege, $counterdamege, $tName, $tPoint);
                                    $msseigen++;
                                    $tHp -= $attackdamege;
                                    $tlv -= $attackdamege;
                                    $landValue->[$sx][$sy] = $tlv;
                                    $mHp -= $counterdamege;
                                    $lv = Calc_MonsterLandValue_HP($mKind , $mHp);
                                    $landValue->[$x][$y] = $lv;

                                    if ($tHp < 1) {
                                        # 対象の怪獣が倒れて荒地になる
                                        MonsterDead( $island , $sx , $sy , $tKind , 0 );
                                        # 報奨金
                                        my ($value) = $HmonsterValue[$tKind];
                                        $island->{'money'} += $value;

                                        if (random(1000) < $value) {
                                            if (random(100) < 30) {
                                                $msap++;
                                            } elsif (random(100) < 30) {
                                                $msdp++;
                                            } elsif (random(100) < 30) {
                                                $mssp++;
                                            } else {
                                                $mshp++;
                                                $mshp = 15 if($mshp > 15);
                                            }
                                        }

                                        $msexe += $HmonsterExp[$tKind];
                                        $mswin ++;
                                        $island->{'eisei5'} = "$mshp,$msap,$msdp,$mssp,$mswin,$msexe,$tet";
                                        # 怪獣退治数
                                        TaijiPrize($island , $tKind);
                                        logMsMonMoney($id, $tName, $value);
                                    }
                                    if ($mHp < 1) {
                                        # マスコットいのらが倒れて荒地になる
                                        MonsterDead( $island , $x , $y , $mKind , 0 );
                                        # 報奨金
                                        AddMonsterReward($island , $mKind);
                                    }
                                }
                            }
                            else {
                                last;
                            }
                        }
                    }
                }
            }

            if (   ($special == 6)
                || ($mKind == $Mons_Mikael) ) { # 天使ミカエル

                my($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};
                if($monsno > 0) {
                    my($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for ($i = 0; $i < $monsno; $i++){
                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster){
                            # 島に別の怪獣がいる場合、その怪獣を攻撃する

                            # 対象となる怪獣の各要素取り出し
                            my ($sLv) = $landValue->[$sx][$sy];
                            my ($sKind, $sName, $sHp) = monsterSpec($sLv);
                            my ($sSpecial) = $HmonsterSpecial[$sKind];

                            if ($mHp > $sHp){ # 対象より体力が多かった場合
                                if (isMonsterCuring($sKind)) {
                                    # 対象が硬化中なら効果なし
                                    next;
                                }
                                last if ($kougekiseigenm > 1);

                                if ($mKind == 13) { # 天使ミカエル
                                    logMonsAttackt($id, $name, $mName, "($x, $y)", $sName, "($sx, $sy)");
                                }
                                else {
                                    logMonsAttack($id, $name, $mName, "($x, $y)", $sName, "($sx, $sy)");
                                }

                                $kougekiseigenm++;
                                # 対象の怪獣の体力を奪って自分の体力を回復
                                $sHp--;
                                if ($sHp > 0){
                                    # 対象の体力を減らす
                                    $sLv--;
                                    $landValue->[$sx][$sy] = $sLv;
                                }
                                else {
                                    # 対象の怪獣が倒れて荒地になる
                                    MonsterDead($island , $sx , $sy , $sKind , 0 );
                                    # 報奨金
                                    my($value) = $HmonsterValue[$sKind];
                                    $island->{'money'} += $value;
                                    logMsMonMoney($id, $sName, $value);
                                }
                                $lv++ if($mHp < 9);
                                $landValue->[$x][$y] = $lv;
                            }
                            # 対象より体力が低かった場合、何もしない
                        }
                    }
                    my ($nKind, $nName, $nHp) = monsterSpec($landValue->[$x][$y]);
                    $nKind = 30 if ($nKind > 30);
                    $nHp = 1 if ($nHp < 1);
                    $landValue->[$x][$y] = ($nKind << $Mons_Kind_Shift) + $nHp;
                }
            }

            if (   ($mKind == $Mons_Totten)
                || ($mKind == $Mons_Wario) ) {    # トッテン
                if ( (!random(2) ) ) {
                    my ($stole);
                    $stole = 500 +  random(99999);
                    $stole = 5000 + random(999999) if ( ($mKind == $Mons_Wario) ) ;

                    if ( $island->{'money'} > $stole ) {
                        logMonsMoneyStole($id, $name, $stole , $mName);
                        $island->{'money'} -= $stole;
                    }
                    else {
                        if ($mKind == $Mons_Wario) {

                            $stole = int ($stole / 2) ;
                            if ( $island->{'money'} > $stole ) {
                                logMonsMoneyStole($id, $name, $stole , $mName);
                                $island->{'money'} -= $stole;
                            }
                        }
                    }

                }
                else {
                    logMonsMoneyStoleMiss($id, $name, $mName);
                }
            }

            if ($mKind == $Mons_Wario) {
                if ( (!random(2) ) ) {
                    my ($stole);
                    $stole = 5000 + random(500000);

                    if ( $island->{'food'} > $stole ) {
                        logMonsFoodStole($id, $name, $stole , $mName);
                        food_product_Random_consumption($island , $stole);
                    }else{
                        if ($mKind == $Mons_Wario) {

                            $stole = int ($stole / 2) ;
                            if ( $island->{'food'} > $stole ) {
                                logMonsFoodStole($id, $name, $stole , $mName);
                                food_product_Random_consumption($island , $stole);
                            }else{
                                $stole = int($island->{'food'} / 10) ;

                                if ( $island->{'food'} > $stole ) {
                                    logMonsFoodStole($id, $name, $stole , $mName);
                                    food_product_Random_consumption($island , $stole);
                                }
                            }
                        }
                    }
                }else{
                    logMonsFoodStoleMiss($id, $name, $mName);
                }
            }

            if ($mKind == $Mons_Kisinhei) {
                if ($mHp < 5) {
                    if ($landValue3->[$x][$y] >= 100) {

                        my ($kaihuku) = int($landValue3->[$x][$y] / 100);
                        if (($mHp + $kaihuku) > 10) {

                            $kaihuku = 10 - $mHp;
                        }
                        $landValue3->[$x][$y] -= ($kaihuku * 100);
                        $landValue->[$x][$y] += $kaihuku;
                        logKishinhei_Kaihuku($island , "($x,$y)");
                    }
                }
            }

            # ----------------------------------------- #
            # 移動できなくてもできる行動
            # ここまで
            # ----------------------------------------- #

            # 動く方向を決定
            my ($d, $sx, $sy);
            my ($i);

            for ($i = 0; $i < 3; $i++) {

                $d = random(6) + 1;
                $sx = $x + $ax[$d];
                $sy = $y + $ay[$d];
                # 行による位置調整
                $sx-- if(!($sy % 2) && ($y % 2));
                # 範囲外判定
                next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

                my $l = $land->[$sx][$sy];
                my ($lva) = $landValue->[$sx][$sy];
                my $def = 0;

                $def = countAround($land, $sx, $sy, 19, $HlandDefence ) if ($island->{'BF_Flag'} == 1);

                if (isSeaMonster($mKind)) {
                    if (   ($l == $HlandSea)
                        || ( ($l == $HlandMine) && ($lva & $Hmine_SEA_FLAG))
                        || ( ($l == $HlandIce) && ($mKind == $Mons_Unbaba) )
                        || ( ($l == $HlandNursery) && ($mKind == $Mons_Unbaba) )
                        || ( ($l == $HlandFrocity) && ($mKind == $Mons_Unbaba) )
                        || ( ($l == $HlandMinato) && ($mKind == $Mons_Unbaba) )
                        || ( ($l == $HlandOil) && ($mKind == $Mons_Unbaba) )
                        || ( ($l == $HlandFune) && ($mKind == $Mons_Unbaba) )
                        || ( ($l == $HlandUmiamu) && ($mKind == $Mons_Unbaba) )
                            ){
                        #動ける
                        last;
                    }
                    else {
                        #うごかない
                    }

                }else{
                    # 海、海基、海底都市、油田、怪獣、山、記念碑以外
                    if (   (   (   ($l != $HlandSea)
                                && ($l != $HlandSbase)
                                && ($l != $HlandSeacity)
                                && ($l != $HlandSeatown)
                                && ($l != $HlandUmicity)
                                && ($l != $HlandOilCity)
                                && ($l != $HlandNursery)
                                && ($l != $HlandOil)
                                && ($l != $HlandBigtown)
                                && ($l != $HlandBettown)
                                && ($l != $HlandShuto)
                                && ($l != $HlandCollege)
                                && ($l != $HlandUmishuto)
                                && ($l != $HlandFrocity)
                                && ($l != $HlandBigRizort)
                                && ($l != $HlandOnsen)
                                && ($l != $HlandHouse)
                                && ($l != $HlandFune)
                                && ($l != $HlandUmiamu)
                                && ($l != $HlandGold)
                                && ($l != $HlandShrine)
                                && ($l != $HlandMountain)
                                && ($l != $HlandMonument)
                                && ($l != $HlandYougan)
                                && ($l != $HlandEgg)
                                && ($l != $HlandZoo)
                                && ($l != $HlandRottenSea)
                                && ($l != $HlandMonster) )
                            || (   ($l == $HlandMine)           # 地雷
                                && !($lva & $Hmine_SEA_FLAG) )  # 海じゃない
                            || (   ($l == $HlandYougan)         # 溶岩で
                                && ($mKind == 33) )             # 溶岩怪獣はOK
                        && ($def == 0 )
                                       ) ) {
                        last;
                    }
                }
            }
            # 動かなかった
            next if ($i == 3);

            if (   ($mKind == 28)
                || ($mKind == 30) ) {
                if ($land->[$sx][$sy] != $HlandWaste) {
                    next;
                }
            }

            # 動いた先の地形によりメッセージ
            my ($sL) = $land->[$sx][$sy];
            my ($sLv) = $landValue->[$sx][$sy];
            my ($sLv2) = $landValue2->[$sx][$sy];
            my ($sName) = landName($sL, $sLv, $sLv2);
            my ($point) = "($sx, $sy)";

            my($mi, $mx, $my);

            for($mi = 0; $mi < $island->{'monsterlive'}; $mi++){
                ($mx, $my) = ($island->{'monspnt'}->[$mi]->{x}, $island->{'monspnt'}->[$mi]->{y});
                if(($mx == $x) && ($my == $y)) {
                    $island->{'monspnt'}->[$mi] = { x => $sx, y => $sy };
                    last;
                }
            }

            # 移動前の処理
            if ($mKind == $Mons_Kisinhei) {
                my ($atk_kind);
                $atk_kind = $land->[$sx][$sy];

                foreach my $ta (@Htowns) {
                    if ($atk_kind == $ta) {
                        logKishinhei_kyusyu($island , $point ,$landValue->[$sx][$sy]);
                        $landValue3->[$x][$y] += $landValue->[$sx][$sy];
                        last;
                    }
                }
            }
            
            $land->[$sx][$sy] = $land->[$x][$y];
            $landValue->[$sx][$sy] = $landValue->[$x][$y];
            $landValue2->[$sx][$sy] = $landValue2->[$x][$y];
            $landValue3->[$sx][$sy] = $landValue3->[$x][$y];
            #移動前の地形を整形
            MonsterDown( $island , $x , $y , $mKind , 0 );

            # ---------------------------------- #
            # 怪獣での特殊効果                   #
            # elseif内に specialを入れないこと！ #
            # ---------------------------------- #
            if ($mKind == 11) { # 奇獣スライムなら(いのらを流用)

                if (   (   (random(1000) < 900)                 # ９０% の確率で分裂する
                        && ($island->{'monsterlive'} < 7) )
                    || (   (random(20000) < 400-$island->{'monsterlive'})
                        && ($island->{'monsterlive'} > 7))      # ９０% の確率で分裂する
                                                                ) {
                    lognewMonsterBorn($id, $name, "($x, $y)");
                    $lv =  Calc_MonsterLandValue($mKind);
                    $land->[$x][$y] = $HlandMonster;
                    $landValue->[$x][$y] = $lv;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    $island->{'monspnt'}->[$island->{'monsterlive'}] = { x => $x, y => $y };
                    $island->{'monsterlive'}++;
                }

            } elsif (   ($mKind == 15)       # 魔獣レイジラ,魔術師アールヴなら(いのらを流用)
                     || ($mKind == $Mons_Alfr)) {

                if ((random(1000) < 600) && ($island->{'monsterlive'} < 7)) { # ６０% の確率で召喚する(助けがくる)
                    my ($nKind) = random($HmonsterLevel3) + 1;
                    SetMonsterLand_Normal($island , $x , $y , $nKind);

                    my($nName) = $HmonsterName[$nKind];
                    if($mKind == 15) { # 魔獣レイジラ
                        lognewKaiju($id, $name, $nName, "($x, $y)");
                    }else{
                        logShoukan($id, $name, $mName, $nName, "($x, $y)");
                    }
                }

            }elsif (   ($mKind == 8)
                    && ($island->{'BF_Flag'} == 0) ) { # オームなら　ここから追加

                my ($RottenSeaBorn_Per) = 400;      #腐海発生率
                my ($Shedding_Per) = 200;           #脱皮発生率

                if(random(1000) < $RottenSeaBorn_Per) { # 40% の確率で腐海が生まれる
                    logRottenSeaBorn($id, $name, "($x, $y)");
                    SetRottenSea($island , $x , $y);

                } elsif(random(1000) < $Shedding_Per) { # 脱皮
                    logNuginugi($id, $name, "($x, $y)");
                    SetMonument_Normal($island , $x , $y , 87);
                    SetMonsterLand_Normal($island , $sx , $sy , $Mons_Omu);
                }

            }elsif ($mKind == 33) {        # 溶岩怪獣

                if (   ($mHp < 3)
                    && (random(100) < 50 ) ){
                    FiveHexFlame($island , $sx , $sy);

                }elsif (random(100) < 30) {
                    my ($tx, $ty);
                    $tx = random($HislandSize);
                    $ty = random($HislandSize);
                    logMgSpel($id, $name, $mName, "($x, $y)", "ヴォル");
                    Volcano($island,$tx,$ty);

                }elsif((random(100) < 50 )){
                    ThreeWayFlame($island , $sx , $sy);

                }elsif (random(100) < 50) {
                    my($i, $tx, $ty);
                    foreach $i (0..$pointNumber) {
                        $tx = $Hrpx[$i];
                        $ty = $Hrpy[$i];
                        my ($tkind) = $land->[$tx][$ty];
                        if($tkind == $HlandMonster) {
                            # 島に別の怪獣がいる場合、その怪獣を攻撃する

                            # 対象となる怪獣の各要素取り出し
                            my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$tx][$ty]);
                            my ($tlv) = $landValue->[$tx][$ty];
                            # my($tSpecial) = $HmonsterSpecial[$tKind];

                            if(isMonsterCuring($tKind)) {
                                # 対象が硬化中なら効果なし
                                next;
                            }
                            if (random(1000) < 600) {
                                if (   ($tKind == 28)
                                    || ($tKind == 30) ) {
                                    logFireAttack($id, $name, $mName, "($x, $y)", $tName, "($tx, $ty)");
                                    $dmge = random(4);
                                    $tHp -= $dmge;
                                    $tlv -= $dmge;
                                    $landValue->[$tx][$ty] = $tlv;

                                    if($tHp < 1){
                                        # 対象の怪獣が倒れて氷河になる
                                        $land->[$tx][$ty] = $HlandYougan;
                                        $landValue->[$tx][$ty] = 2+random(9);
                                        $island->{'monsterlive'} -= 1;
                                        # 報奨金
                                        my($value) = $HmonsterValue[$tKind];
                                        $island->{'money'} += $value;
                                        logMsMonMoney($id, $tName, $value);
                                    }

                                } elsif($tKind != 33) {
                                    logFireAttack($id, $name, $mName, "($x, $y)", $tName, "($tx, $ty)");

                                    # 対象の怪獣が倒れて氷河になる
                                    SetYoganLand($island, $tx , $ty);
                                    $island->{'monsterlive'} -= 1;

                                    if (random(1000) < 100) {
                                        SetMonument_Normal($island, $tx , $ty , 78);
                                    }
                                    # 報奨金
                                    my($value) = $HmonsterValue[$tKind];
                                    $island->{'money'} += $value;
                                    logMsMonMoney($id, $tName, $value);
                                }
                            }

                        } elsif (   ($tkind == $HlandBase)
                                 || ($tkind == $HlandDefence)
                                 || ($tkind == $HlandHaribote)
                                 || ($tkind == $HlandOil)
                                 || ($tkind == $HlandFune)
                                                            ) {
                            # 島にあるミサイル基地、防衛施設、油田、船舶を氷山か氷石にする
                            if (random(1000) < 200) {
                                my $tKind = $land->[$tx][$ty];
                                my $tlv = $landValue->[$tx][$ty];
                                my $tlv2 = $landValue2->[$tx][$ty];
                                logFireAttack($id, $name, $mName, "($x, $y)", landName($tKind, $tlv, $tlv2), "($tx, $ty)");
                                SetYoganLand($island, $tx , $ty);

                                if (random(1000) < 100) {
                                    SetMonument_Normal($island, $tx , $ty , 78);
                                }
                            }
                        }
                    }
                }

            }elsif ($mKind == $Mons_Pirates) {        # 海賊

                my ($flag);
                $flag = 0;

                my ($i, $ssx, $ssy, $ssL, $ssLv, $ssLv2);

                for ($i = 1; $i < 19; $i++) {
                    $ssx = $sx + $ax[$i];
                    $ssy = $sy + $ay[$i];

                    # 行による位置調整
                    $ssx-- if(!($ssy % 2) && ($sy % 2));
                    # 範囲外
                    next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));

                    $ssL = $land->[$ssx][$ssy];
                    $ssLv = $landValue->[$ssx][$ssy];
                    $ssLv2 = $landValue2->[$ssx][$ssy];

                    if ($i < 7) {

                        if (   ($ssL == $HlandTown)
                            || ($ssL == $HlandProcity)
                            || ($ssL == $HlandMinato)
                            || ($ssL == $HlandFrocity)
                            || ($ssL == $HlandNewtown)
                            || ($ssL == $HlandBigtown)
                            || ($ssL == $HlandBettown)
                            || ($ssL == $HlandUmicity)
                            || ($ssL == $HlandOilCity)
                            || ($ssL == $HlandInaka)
                            || ($ssL == $HlandOnsen)
                            || ($ssL == $HlandRizort)
                            || ($ssL == $HlandBigRizort)
                            || ($ssL == $HlandShuto)
                            || ($ssL == $HlandFactory)
                                                        ) {
                            if (random(100) < 77) {

                                my ($tarland) = landName($ssL, $ssLv, $ssLv2);
                                my ($tpoint) = "($ssx,$ssy)";
                                my ($tname) = islandName($island);
                                my ($bag) = random((1000-20)) + 20;

                                if ($island->{'money'} < $bag) {
                                    $bag = $island->{'money'};
                                }

                                if ($bag) {
                                    my($haken);
                                    my($haken_island);
                                    $haken = $island->{'landValue2'}->[$sx][$sy];
                                    #logOut("debug 海賊がお金をとった。", $id);
                                    logOut("${HtagName_}${tname}$tpoint${H_tagName}の<B>$tarland</B>は、海賊船から襲撃を受け${HtagMoney_}$bag$HunitMoney${H_tagMoney}持っていかれました。",$id);

                                    if ($haken != 0) {
                                        logSecret("${HtagName_}${tname}$tpoint${H_tagName}の海賊の働き${HtagMoney_}$bag$HunitMoney${H_tagMoney}。",$haken);
                                        $haken_island = $Hislands[$HidToNumber{$haken}];
                                        $haken_island->{'money'} += $bag;
                                    }
                                    $monsterMove[$sx][$sy] = 2;
                                }
                                last;
                            }
                        }

                    }else{
                        if (   ($ssL == $HlandTown)
                            || ($ssL == $HlandProcity)
                            || ($ssL == $HlandMinato)
                            || ($ssL == $HlandFrocity)
                            || ($ssL == $HlandNewtown)
                            || ($ssL == $HlandBigtown)
                            || ($ssL == $HlandBettown)
                            || ($ssL == $HlandUmicity)
                            || ($ssL == $HlandOilCity)
                            || ($ssL == $HlandInaka)
                            || ($ssL == $HlandOnsen)
                            || ($ssL == $HlandRizort)
                            || ($ssL == $HlandBigRizort)
                            || ($ssL == $HlandShuto)
                            || ($ssL == $HlandFactory)
                            || ($ssL == $HlandFarmchi)
                            || ($ssL == $HlandFarmpic)
                            || ($ssL == $HlandFarmcow)
                            || ($ssL == $HlandPark)
                            || ($ssL == $HlandNursery)
                            || ($ssL == $HlandFoodim)
                            || ($ssL == $HlandGold)
                            || ($ssL == $HlandInoraLand)
                            || ($ssL == $HlandBeachPark)
                                                        ) {
                            if (random(100) < 20) {

                                my ($tarland) = landName($ssL, $ssLv,$ssLv2);
                                my ($tpoint) = "($ssx,$ssy)";
                                my ($tname) = islandName($island);

                                logOut("${HtagName_}${tname}$tpoint${H_tagName}の<B>$tarland</B>は、海賊船からの大砲の襲撃を受けました。",$id);

                                $ssLv = ($ssLv / 4);
                                $landValue->[$ssx][$ssy] = $ssLv;

                                if ($ssLv <= 0) {
                                    $land->[$ssx][$ssy] = $HlandWaste;
                                    $landValue->[$ssx][$ssy] = 0;
                                    $landValue2->[$ssx][$ssy] = 0;
                                    if (   ($ssL == $HlandOnsen)
                                        || ($ssL == $HlandOnsen) ) {
                                        $land->[$ssx][$ssy] = $HlandMountain;
                                    }elsif ($ssL == $HlandNursery) {
                                        $land->[$ssx][$ssy] = $HlandSea;
                                        $landValue->[$ssx][$ssy] = 1;
                                    }
                                }
                                $monsterMove[$sx][$sy] = 2;
                                last;
                            }
                        }

                        if (   ($ssL == $HlandForest)
                            || ($ssL == $HlandOil)
                            || ($ssL == $HlandHaribote)
                            || ($ssL == $HlandFune)
                            || ($ssL == $HlandKyujo)
                            || ($ssL == $HlandSeki)
                            || ($ssL == $HlandCollege)
                            || ($ssL == $HlandKyujokai)
                            || ($ssL == $HlandKatorikun)
                            || ($ssL == $HlandFiredept)
                            || ($ssL == $HlandRocket)
                            || ($ssL == $HlandTrain)
                            || ($ssL == $HlandStation)
                                                        ) {
                            if (random(100) < 5) {
                                my ($tarland) = landName($ssL, $ssLv,$ssLv2);
                                my ($tpoint) = "($ssx,$ssy)";
                                my ($tname) = islandName($island);

                                logOut("${HtagName_}${tname}$tpoint${H_tagName}の<B>$tarland</B>は、海賊船からの大砲の襲撃を受けました。",$id);

                                $land->[$ssx][$ssy] = $HlandWaste;
                                $landValue->[$ssx][$ssy] = 0;
                                $landValue2->[$ssx][$ssy] = 0;
                                if (   ($ssL == $HlandOil)
                                    || ($ssL == $HlandFune) ) {
                                    $land->[$ssx][$ssy] = $HlandSea;
                                }
                                $monsterMove[$sx][$sy] = 2;
                                last;
                            }
                        }
                    }

                }

                if (random(100) < 5) {
                    my ($tpoint) = "($sx,$sy)";
                    my ($tname) = islandName($island);
                    SetSeaLand_Normal($island, $sx , $sy);
                    logOut("${HtagName_}${tname}$tpoint${H_tagName}の<b>海賊船</b>は、どこかへ去ってゆきました。",$id);
                }
            }
            # 怪獣限定の特殊効果ここまで

            # 怪獣が周囲を焼き尽くす能力・衝撃波
            if(   ($special == 7) 
               || ($special == 11)
               || ($mKind == 16)    # 魔獣クイーンいのら(周囲1Ｈｅｘ)
               || ($mKind == 13)
               || ($mKind == 18) ) { # 天使ミカエル,天使ウリエル(周囲2Ｈｅｘ)
                my $r = 7;
                $r = 19 if(($mKind == 13) || ($mKind == 18));
                my($i, $ssx, $ssy, $ssL, $ssLv,$ssLv2);
                for($i = 1; $i < $r; $i++) {
                    $ssx = $sx + $ax[$i];
                    $ssy = $sy + $ay[$i];

                    # 行による位置調整
                    $ssx-- if(!($ssy % 2) && ($sy % 2));
                    # 範囲外
                    next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));

                    $ssL = $land->[$ssx][$ssy];
                    $ssLv = $landValue->[$ssx][$ssy];
                    $ssLv2 = $landValue2->[$ssx][$ssy];

                    if (($ssL == $HlandSea) ||
                        ($ssL == $HlandSeacity) ||
                        ($ssL == $HlandSeatown) ||
                        ($ssL == $HlandUmishuto) ||
                        ($ssL == $HlandIce) ||
                        ($ssL == $HlandWaste) ||
                        ($ssL == $HlandUmiamu) ||
                        ($ssL == $HlandSbase)) {
                        # 海と海底基地は焼かれない
                        next;
                    } elsif(($ssL == $HlandOil) ||
                             ($ssL == $HlandFrocity) ||
                             ($ssL == $HlandUmicity) ||
                             ($ssL == $HlandOilCity) ||
                             ($ssL == $HlandFune)) {
                        # 油田・船は海に戻る
                        $land->[$ssx][$ssy] = $HlandSea; # 海になる
                        $landValue->[$ssx][$ssy] = 0;
                    } elsif($ssL == $HlandNursery) {
                        # 養殖場は海に戻る
                        $land->[$ssx][$ssy] = $HlandSea; # 海になる
                        $landValue->[$ssx][$ssy] = 1;
                    } elsif(($ssL == $HlandGold) ||
                             ($ssL == $HlandShrine) ||
                             ($ssL == $HlandOnsen) ||
                             (($ssL == $HlandMountain) && ($ssLv > 0))) {
                        # 金山・採掘場・時の神殿は山に戻る
                        SetMountain_Normal($island,$ssx,$ssy);  # 山になる

                    } elsif ($ssL == $HlandMonster) {
                        # 怪獣は
                        # 対象となる怪獣の各要素取り出し
                        my($tKind, $tName, $tHp) = monsterSpec($ssLv);
                        my($tlv) = $landValue->[$ssx][$ssy];
                        # my($tspecial) = $HmonsterSpecial[$tKind];
                        if (($tKind == 28) || ($tKind == 30)) {
                            my ($dmge) = random(4);
                            $tHp -= $dmge;
                            $tlv -= $dmge;
                            $landValue->[$ssx][$ssy] = $tlv;

                            if($tHp < 1){
                                # 対象の怪獣が倒れて荒地になる
                                MonsterDown($island , $ssx , $ssy , $tKind , 0);
                                # 報奨金
                                my($value) = $HmonsterValue[$tKind];
                                $island->{'money'} += $value;
                                logMsMonMoney($id, $tName, $value);
                            }
                        }
                    } else {
                        # 全てが焼き尽くされる
                        SetWasteLand_Normal($island , $ssx , $ssy);
                    }

                    # ログを作成する
                    if($special == 11) {
                        logMonsFireS($id, $name, landName($ssL, $ssLv,$ssLv2), "($ssx, $ssy)", $mName);
                    } else {
                        logMonsFire($id, $name, landName($ssL, $ssLv,$ssLv2), "($ssx, $ssy)", $mName);
                    }
                }
            }

            # フリーズストーム
            if (   ($special == 9)
                || ($mKind == $Mons_Ice_scorpion)) {
                my ($i, $ssx, $ssy, $kind, $lv);
                for ($i = 1; $i < 7; $i++) {
                    $ssx = $sx + $ax[$i];
                    $ssy = $sy + $ay[$i];

                    # 行による位置調整
                    if((($ssy % 2) == 0) && (($sy % 2) == 1)) {
                        $ssx--;
                    }

                    if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize)) {
                        # 範囲外
                        next;
                    }

                    $kind = $land->[$ssx][$ssy];
                    $lv   = $landValue->[$ssx][$ssy];

                    if (   (isBehindSea($kind))
                        || ($kind == $HlandIce)
                        || ($kind == $HlandUmiamu)
                                                    ) {
                        # 海と海底基地は焼かれない
                        next;

                    } elsif(   ($kind == $HlandOil)
                            || ($kind == $HlandFune)
                            || ($kind == $HlandFrocity)
                            || ($kind == $HlandUmicity)
                            || ($kind == $HlandOilCity)
                            || ($kind == $HlandNursery)) {
                        # 油田、船、海上都市、養殖場
                        $land->[$ssx][$ssy] = $HlandIce; # 氷河になる
                        $landValue->[$ssx][$ssy] = 0;
                    } elsif ($kind == $HlandMonster) {
                        # 怪獣は
                        # 対象となる怪獣の各要素取り出し
                        my($tKind, $tName, $tHp) = monsterSpec($landValue->[$ssx][$ssy]);
                        my($tlv) = $landValue->[$ssx][$ssy];
                        my($tspecial) = $HmonsterSpecial[$tKind];
                        if(   ($tKind == 28)
                           || ($tKind == 30) ) {
                            my ($dmge) = random(4);
                            $tHp -= $dmge;
                            $tlv -= $dmge;
                            $landValue->[$ssx][$ssy] = $tlv;
                            if($tHp < 1){
                                # 対象の怪獣が倒れて氷河になる
                                $land->[$ssx][$ssy] = $HlandIce;
                                $landValue->[$ssx][$ssy] = 0;
                                # 報奨金
                                my($value) = $HmonsterValue[$tKind];
                                $island->{'money'} += $value;
                                logMsMonMoney($id, $tName, $value);
                            }
                        }
                    } else {
                        # 全てが凍り付く
                        $land->[$ssx][$ssy] = $HlandIce; # 氷河になる
                        $landValue->[$ssx][$ssy] = 0;
                    }

                    # ログを作成する
                    logMonsCold($id, $name, landName($kind, $lv,$landValue2->[$ssx][$ssy]), "($ssx, $ssy)", $mName);
                }
            }

            if (   ($mKind == 14)
                && ($island->{'monsterlive'} < 7) ) { # スライムレジェンドの分裂

                my($i, $ssx, $ssy, $ssL, $ssLv);

                for($i = 1; $i < 7; $i++) {

                    $ssx = $sx + $ax[$i];
                    $ssy = $sy + $ay[$i];

                    # 行による位置調整
                    $ssx-- if(!($ssy % 2) && ($sy % 2));
                    # 範囲外
                    next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));

                    $ssL = $land->[$ssx][$ssy];
                    $ssLv = $landValue->[$ssx][$ssy];

                    unless (   ($ssL == $HlandSea)
                            || ($ssL == $HlandSeacity)
                            || ($ssL == $HlandIce)
                            || ($ssL == $HlandUmishuto)
                            || ($ssL == $HlandSeatown)
                            || ($ssL == $HlandOil)
                            || ($ssL == $HlandFune)
                            || ($ssL == $HlandNursery)
                            || ($ssL == $HlandUmiamu)
                            || ($ssL == $HlandMountain) 
                            || ($ssL == $HlandGold)
                            || ($ssL == $HlandShrine)
                            || ($ssL == $HlandOnsen)
                            || ($ssL == $HlandMonster)
                            || ($ssL == $HlandMonument)
                            || ($ssL == $HlandZoo)
                            || ($ssL == $HlandSbase) ) {
                        # 海系と海底基地、山系には分裂しない
                        # 分裂
                        my $nKind = $Mons_Slime;
                        $lv = Calc_MonsterLandValue($nKind);
                        $land->[$ssx][$ssy] = $HlandMonster;
                        $landValue->[$ssx][$ssy] = $lv;
                        $landValue2->[$x][$y] = 0;
                        $landValue2->[$ssx][$ssx] = 0;
                        $island->{'monspnt'}->[$island->{'monsterlive'}] = { x => $ssx, y => $ssy };
                        $island->{'monsterlive'}++;
                    }

                    if (random(1000) < 50) {
                        $land->[$ssx][$ssy] = $HlandMonument;
                        $landValue->[$ssx][$ssy] = 77;
                        $landValue2->[$x][$y] = 0;
                    }

                    # ログを作成する
                    lognewMonsterBorn($id, $name, "($ssx, $ssy)");
                }
            }

            # 移動済みフラグ
            if (   ($HmonsterSpecial[$mKind] == 2)
                || ($mKind == $Mons_Kisinhei)
                || ($mKind == $Mons_Pirates) ) {
                # 移動済みフラグは立てない

            } elsif (   ($HmonsterSpecial[$mKind] == 1)
                     || ($HmonsterSpecial[$mKind] == 16)
                                                    ) {
                # 速い怪獣
                $monsterMove[$sx][$sy] = $monsterMove[$x][$y] + 1;

            } else {
                # 普通の怪獣
                $monsterMove[$sx][$sy] = 2;
            }

            if (($sL == $HlandDefence) && $HdBaseAuto) {
                # 防衛施設を踏んだ
                logMonsMoveDefence($id, $name, $sName, $point, $mName);
                # 広域被害ルーチン
                wideDamage($id, $name, $land, $landValue, $sx, $sy);

            } elsif($sL == $HlandMine) {
                # 地雷を踏んだ
                my($da) = $sLv & $Hmine_DAMAGE_MASK;
                if($mHp < $da) {
                    # 死亡して死体が飛び散った
                    logMonsMine($id, $name, $sName, $point, $mName, "消し飛びました。");
                } elsif($mHp == $da) {
                    # 死亡して死体が残った
                    logMonsMine($id, $name, $sName, $point, $mName, "力尽き、倒れました。");

                    # 収入
                    my($value) = $HmonsterValue[$mKind];
                    if($value > 0) {
                        $island->{'money'} += $value;
                        logMsMonMoney($id, $mName, $value);
                    }

                    # 怪獣退治数
                    TaijiPrize($island , $mKind);

                } else {
                    # 生き残った
                    logMonsMine($id, $name, $sName, $point, $mName, "苦しそうに咆哮しました。");
                    $landValue->[$sx][$sy] -= $da;
                    next;
                }

                # 怪獣は荒地に
                MonsterDown( $island , $sx , $sy , $mKind , 1 );

            } else {
                # 移動ログ
                if ( $mKind == $Mons_Unbaba){
                    logMonsMove($id, $name, $sName, $point, $mName , "に飲み込まれてしまいました。") if (($sL != $HlandSea)&&($sLv != 0));

                } elsif($mKind == 32) {

                } else {
                    if (   ( ($sL != $HlandWaste) && ($sL != $HlandPlains) )
                        && (!$island->{'BF_Flag'}) ) {
                        logMonsMove($id, $name, $sName, $point, $mName , "に踏み荒らされました。");
                    }
                }
            }

        }

        # 火災判定
        my $fflag = 0;
        my $fdept = 0;

        if ($island->{'weather'} != $HWeather_Rain) {

            if((($landKind == $HlandTown) && ($lv > 30)) ||
                ($landKind == $HlandHaribote) ||
                ($landKind == $HlandMinato) ||
                ($landKind == $HlandFoodim) ||
                ($landKind == $HlandOnsen) ||
                ($landKind == $HlandKatorikun) ||
                ($landKind == $HlandCollege) ||
                ($landKind == $HlandHTFactory) ||
                ($landKind == $HlandSHTF) ||
                ($landKind == $HlandFiredept) ||
                ($landKind == $HlandFactory)) {
                $fflag = 1;

            } elsif(($landKind == $HlandNewtown) ||
                ($landKind == $HlandRizort) ||
                ($landKind == $HlandBigRizort) ||
                ($landKind == $HlandBettown) ||
                ($landKind == $HlandBigtown)) {
                $fflag = 2;
            }

            if(    ( $island->{'firedept'} )
                && (random(100) < $HFiredept_save )
                && (   (($landKind == $HlandTown) && ($lv > 30))
                    || ($landKind == $HlandMinato)
                    || ($landKind == $HlandFoodim)
                    || ($landKind == $HlandHTFactory)
                    || ($landKind == $HlandSHTF)
                    || ($landKind == $HlandFactory)
                    || ($landKind == $HlandNewtown)
                    || ($landKind == $HlandRizort)
                    || ($landKind == $HlandBigRizort)
                    || ($landKind == $HlandBettown)
                    || ($landKind == $HlandBigtown) )
                ){

                $fflag = 3;
            }
        }

        $fdept = $HFiredept_guard if ( $island->{'firedept'} );

        if($fflag) {
            my $rfflag = ($fflag == 1) ? random(1000) : random(750);
            my $ffflag = 1 if(!$HnoDisFlag && $rfflag < $HdisFire[0] - $fdept - int($island->{'eis1'}/20));

            if($ffflag) {
                # 周囲の森と記念碑を数える
                my $fw = countAround($land, $x, $y, 7, $HlandForest, $HlandProcity, $HlandHouse, $HlandMonument);
                $fw += countAround($land, $x, $y, 19, $HlandFiredept);
                $fw = 0 if($landKind == $HlandFiredept);
                unless($fw) {
                    # 無かった場合、火災で壊滅
                    my($l) = $land->[$x][$y];
                    my($lv) = $landValue->[$x][$y];
                    my($point) = "($x, $y)";

                    if($fflag == 2) {
                        logFirenot($id, $name, $lName, $point);
                        $landValue->[$x][$y] -= random(100) + 50;
                    }
                    if($fflag == 3) {
                        logFirenot($id, $name, $lName, $point);
                        $landValue->[$x][$y] -= random(50) + 10;
                    }
                    if($fflag == 1 || ($landValue->[$x][$y] <= 0)) {
                        logFire($id, $name, $lName, $point);
                        SetWasteLand_Normal_val($island , $x , $y , 4);

                        if ($l == $HlandOnsen) {
                            # 温泉は山に戻る
                            SetMountain_Normal($island,$x,$y);
                        }
                    }
                }
            }
        }
    }
}


#----------------------------------------------------------------------
sub PetAttackCalc {
    my ($island , $limit) = @_;  # 1で書き込み

    my ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
    my ($m_str) = $HmonsterSTR[$tKind];

    my ($attackdamege) = random($msap-$m_str);
    my ($counterdamege) = random($m_str-$msdp);
    if (random(5 + $m_str) > $mssp) {

        $attackdamege = 0;
    }
    elsif ($attackdamege < 1){

        $attackdamege = $limit;
    }
    if (random(5 + $m_str) < $mssp) {
        $counterdamege = 0;
    } elsif($counterdamege < 1) {
        $counterdamege = 1;
    }

    return ($attackdamege , $counterdamege);
}


#----------------------------------------------------------------------
sub AddMonsterReward {
    my ($island , $mkind) = @_;

    # 報奨金
    my ($value) = $HmonsterValue[$mkind];

    if ($value > 0) {
        my ($tName) = $HmonsterName[$mkind];
        my ($id) = $island->{'id'};
        $island->{'money'} += $value;
        logMsMonMoney($id, $tName, $value);
    }
}



#----------------------------------------------------------------------
# Mikael_Luck
#
sub Mikael_Luck {
    my ($island , $pos , $landkind , $lName) = @_;

    my ($name) = islandName($island);
    my ($id) = $island->{'id'};

    my $value = $HoilMoney + random(500); # 羽根収入
    $island->{'money'} += $value;

    if ($landkind == $HlandMonster) {
        logOilMoneyt($id, $name, $lName, $pos, "$value$HunitMoney", "収益");

    }else{
        if (STATUE_LOG_OMIT) {
            $island->{'statue_income'} += $value;
        }else{
            logMiyage($id, $name, $lName, $pos, "$value$HunitMoney");
        }
    }

    $value = int($island->{'pop'} / 20) + random(11); # 人口５千人ごとに1000トンの食料消費
    #$island->{'food'} += $value;
    food_product_plus($island , 'yasai' ,$value);
    if (STATUE_LOG_OMIT) {
        $island->{'statue_income_food'} += $value;
    }else{
        logParkEventt($id, $name, $lName, $pos, "$value$HunitFood") if($value);
    }
}

#----------------------------------------------------------------------
# たいじ
sub GetTaijiFlag {
    my($island, $mKind) = @_;

    my ($block) = int($mKind/32);
    my ($mMask);
    $mMask = ($mKind % 32);

    if (defined $island->{'taiji_list'}[$block]) {
        my ($flag) = $island->{'taiji_list'}[$block];

        if ($flag & (1 << $mMask) ){

            return 1;
        }
    }
    return 0;
}

#----------------------------------------------------------------------
# 未使用
#----------------------------------------------------------------------
sub FireConflagration {
    my ($island, $x ,$y) = @_;

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};

    my ($landKind) = $land->[$x][$y];
    my ($lv) = $landValue->[$x][$y];
    my ($lv2) = $landValue2->[$x][$y];

    # 火災判定
    my $fflag = 0;
    my $fdept = 0;

    if (   (   ($landKind == $HlandTown)
            && ($lv > 30) )
        || ($landKind == $HlandHaribote)
        || ($landKind == $HlandMinato)
        || ($landKind == $HlandFoodim)
        || ($landKind == $HlandOnsen)
        || ($landKind == $HlandKatorikun)
        || ($landKind == $HlandCollege)
        || ($landKind == $HlandHTFactory)
        || ($landKind == $HlandSHTF)
        || ($landKind == $HlandFiredept)
        || ($landKind == $HlandFactory)
                                        ) {
        $fflag = 1;

    } elsif (   ($landKind == $HlandNewtown)
             || ($landKind == $HlandRizort)
             || ($landKind == $HlandBigRizort)
             || ($landKind == $HlandBettown)
             || ($landKind == $HlandBigtown)
                                            ) {
        $fflag = 2;
    }

    if(    ( $island->{'firedept'} )
        && (random(100) < $HFiredept_save )
        && (   (($landKind == $HlandTown) && ($lv > 30))
            || ($landKind == $HlandMinato)
            || ($landKind == $HlandFoodim)
            || ($landKind == $HlandHTFactory)
            || ($landKind == $HlandSHTF)
            || ($landKind == $HlandFactory)
            || ($landKind == $HlandNewtown)
            || ($landKind == $HlandRizort)
            || ($landKind == $HlandBigRizort)
            || ($landKind == $HlandBettown)
            || ($landKind == $HlandBigtown) )
        ){

        $fflag = 3;
    }

    $fdept = $HFiredept_guard if ( $island->{'firedept'} );

    if($fflag) {
        my $rfflag = ($fflag == 1) ? random(1000) : random(750);
        my $ffflag = 1 if(!$HnoDisFlag && $rfflag < $HdisFire[0] - $fdept - int($island->{'eis1'}/20));

        if($ffflag) {
            # 周囲の森と記念碑を数える
            my $fw = countAround($land, $x, $y, 7, $HlandForest, $HlandProcity, $HlandHouse, $HlandMonument);
            $fw += countAround($land, $x, $y, 19, $HlandFiredept);
            $fw = 0 if($landKind == $HlandFiredept);
            unless($fw) {
                # 無かった場合、火災で壊滅
                my($l) = $land->[$x][$y];
                my($lv) = $landValue->[$x][$y];
                my($point) = "($x, $y)";
                my($lName) = landName($l, $lv,$landValue2->[$x][$y]);

                if ($fflag == 2) {
                    logFirenot($id, $name, $lName, $point);
                    $landValue->[$x][$y] -= random(100) + 50;
                }
                if ($fflag == 3) {
                    logFirenot($id, $name, $lName, $point);
                    $landValue->[$x][$y] -= random(50) + 10;
                }
                if ($fflag == 1 || ($landValue->[$x][$y] <= 0)) {
                    logFire($id, $name, $lName, $point);
                    SetWasteLand_Normal($island , $x , $y);

                    if ($l == $HlandOnsen) {
                        # 温泉は山に戻る
                        $land->[$x][$y] = $HlandMountain; # 海になる
                        $landValue->[$x][$y] = 0;
                    }
                }
            }
        }
    }
}


# ---------------------------------------------------------------------
# 爆風1HEXがノーダメージの地形
# ---------------------------------------------------------------------
sub NoDamage_by_Flame {
    my ($LandKind) = @_;

    if (   ($LandKind == $HlandMountain)
        || ($LandKind == $HlandOnsen)
        || ($LandKind == $HlandUmishuto)
        || ($LandKind == $HlandGold)
        || ($LandKind == $HlandShrine)
        || ($LandKind == $HlandSea)
        || ($LandKind == $HlandSbase)
        || ($LandKind == $HlandSeacity)
        || ($LandKind == $HlandSeatown)
        || ($LandKind == $HlandFune)
        || ($LandKind == $HlandUmiamu)
                                        ) {
        # ダメージのない地形
        return 1;
    }
    return 0;
}


# ---------------------------------------------------------------------
# 箱庭カップ勝率リセット
# ---------------------------------------------------------------------
sub HakoCup_TeamReset {
    my($island) = @_;

    if ($island->{'stadiumnum'}) {
        # HakoniwaCup
        my($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $island->{'eisei4'});
        my $turn = $HislandTurn % 100;

        if($turn == 0) {            # 初期化
            $stwin = 0;             # 勝ち数
            $stdrow = 0;            # 引き分け
            $stlose = 0;            # 負け数
            $stshoka = 1;

            $island->{'eisei4'} = "$sto,$std,$stk,$stwin,$stdrow,$stlose,$stwint,$stdrowt,$stloset,$styusho,$stshoka";
        }
    }
}


# ---------------------------------------------------------------------
# 砂浜
# ---------------------------------------------------------------------
sub SunahamaToSea {
    my($island, $x ,$y) = @_;
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($landValue2) = $island->{'landValue2'};


    my ($par) = $Sunahama_To_Sea_par;
    $par += (3 *$island->{'weather_chain'}) if ( $island->{'weather'} == $HWeather_Rain);
    $par -= (3 *$island->{'weather_chain'}) if ( $island->{'weather'} == $HWeather_Sunny);

    $par += (3) if (15 > $island->{'temperature'});
    $par -= (3) if (22 < $island->{'temperature'});

    if (random(100) < $par) {
        $land->[$x][$y] = $HlandSea;
        $landValue->[$x][$y] = 1;
        $landValue2->[$x][$y] = 0;
    }
}

# ---------------------------------------------------------------------
# 防衛都市、豚のかとりくん
# ---------------------------------------------------------------------
sub ProCity_MonsterSmash {
    my($island, $x ,$y) = @_;
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($name) = islandName($island);
    my($id) = $island->{'id'};
    my($i, $sx, $sy);

    for($i = 1; $i < 7; $i++) {
        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];
        # 行による位置調整
        $sx-- if(!($sy % 2) && ($y % 2));
        # 範囲外
        next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));
        if($land->[$sx][$sy] == $HlandMonster){
            # 周囲1Hexに別の怪獣がいる場合、その怪獣を攻撃する

            # 対象となる怪獣の各要素取り出し
            my($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);

            logBariaAttack($id, $name, $tName, "($sx, $sy)");
            # 対象の怪獣が倒れて荒地になる
            MonsterDead($island , $sx , $sy , $tKind , 1 );
        }
    }
}


# ---------------------------------------------------------------------
# 爆風1HEXがノーダメージの地形
# ---------------------------------------------------------------------
sub NoDamage_by_Bomb1HEX {
    my ($LandKind) = @_;

    if (   ($LandKind == $HlandWaste)
        || ($LandKind == $HlandMountain)
        || ($LandKind == $HlandIce)
        || ($LandKind == $HlandOnsen)
        || ($LandKind == $HlandUmishuto)
        || ($LandKind == $HlandFrocity)
        || ($LandKind == $HlandGold)
        || ($LandKind == $HlandShrine)
        || ($LandKind == $HlandSea)
        || ($LandKind == $HlandSbase)
        || ($LandKind == $HlandSeacity)
        || ($LandKind == $HlandSeatown)
        || ($LandKind == $HlandOil)
        || ($LandKind == $HlandFune)
        || ($LandKind == $HlandUmiamu)
                                        ) {
        # ダメージのない地形
        return 1;
    }
    return 0;
}


# ---------------------------------------------------------------------
# 怪獣ワープ可能な地形
# ---------------------------------------------------------------------
sub MonsterWarpLandingForQueen {
    my($island, $landkind, $landValue , $x , $y) = @_;

    my ($def)=0;

    if ( $island->{'BF_Flag'} == 1) {
        return 0;
    }

    if (   ($landkind == $HlandSea)         # 海
        || ($landkind == $HlandPlains)      # へいち
        || ($landkind == $HlandWaste)       # 荒れ地
                                        ) {
        return 1;
    }

    return 0;
}



# ---------------------------------------------------------------------
# 怪獣ワープ可能な地形
# ---------------------------------------------------------------------
sub MonsterWarpLanding {
    my($island, $landkind, $landValue , $x , $y) = @_;

    my ($def)=0;

    if ( $island->{'BF_Flag'} == 1) {
        my($land) = $island->{'land'};
        $def = countAround($land, $x, $y, 19, $HlandDefence);
    }

    if ($def > 0){
        return 0;
    }

    if (   ($landkind == $HlandTown)
        || ($landkind == $HlandPlains)
        || ($landkind == $HlandWaste)
        || ($landkind == $HlandForest)
        || ($landkind == $HlandFarm)
        || ($landkind == $HlandFactory)
        || ($landkind == $HlandBase)
        || ($landkind == $HlandDefence)
        || ($landkind == $HlandHaribote)
        || ($landkind == $HlandTrain)
        || ($landkind == $HlandFoodim)
        || ($landkind == $HlandNewtown)
        || ($landkind == $HlandBigtown)
        || ($landkind == $HlandFarmchi)
        || ($landkind == $HlandFarmpic)
        || ($landkind == $HlandFarmcow)
        || ($landkind == $HlandCollege)
        || ($landkind == $HlandSunahama)
        || ($landkind == $HlandBeachPark)
        || ($landkind == $HlandRizort)
        || ($landkind == $HlandBigRizort)
        || ($landkind == $HlandHTFactory)
        || ($landkind == $HlandSHTF)
        || ($landkind == $HlandBettown)
        || ($landkind == $HlandRocket)
                                        ) {
        return 1;
    }

    return 0;
}


#----------------------------------------------------------------------
# 人口から怪獣を選ぶ
# 対象の島 , sendも含めるか
#----------------------------------------------------------------------
sub MonsterSpawnKind {
    my($island , $send) = @_;

    # 怪獣出現
    # 種類を決める
    my ($kind, $pop, $temp,$chflag);
    my ($lv2);
    $lv2 = 0;
    $pop = $island->{'pop'};

    $temp = 0 ;
    $chflag = 1;

    if( ($island->{'id'} > 100) || 
        ($island->{'BF_Flag'} == 1) ) {
        $pop = $HdisMonsBorder3;
    }

    if ($send > 0 && $island->{'monstersend'} > 0) {
        # 人造
        my ($send) = $island->{'monstersend'};
        my ($sendmo_kind , $sendmo_id);
        $chflag = 0;

        $sendmo_kind = $island->{'sendmo_kind'};
        $kind = $sendmo_kind->[$send];

        $sendmo_id = $island->{'sendmo_id'};
        $lv2 = $sendmo_id->[$send];

        $island->{'monstersend'}--;

    } elsif ($send > 0 && $island->{'event_monstersend'}) {
        $island->{'event_monstersend'} = 0;
        $kind = 35; #ひめ
        $chflag = 0;

    } elsif ($pop >= $HdisMonsBorder5) {
        # level5まで
        $temp = random($HmonsterLevel5TABLE_NUM) + 1;
    } elsif ($pop >= $HdisMonsBorder4) {
        # level4まで
        $temp = random($HmonsterLevel4TABLE_NUM) + 1;
    } elsif ($pop >= $HdisMonsBorder3) {
        # level3まで
        $temp = random($HmonsterLevel3TABLE_NUM) + 1;
    } elsif ($pop >= $HdisMonsBorder2) {
        # level2まで
        $temp = random($HmonsterLevel2TABLE_NUM) + 1;
    } else {
        # level1のみ
        $temp = random($HmonsterLevel1TABLE_NUM) + 1;
    }
    if ($chflag) {
        $kind = $HmonsterTABLE[$temp];
    }

    if (   ( ($kind == 11) || (isSeaMonster($kind)))
        && ($island->{'BF_Flag'} == 1) ){
        $kind = 0;
    }

    return ($kind, $lv2);
}

#----------------------------------------------------------------------
# 怪獣購入で得られる怪獣
#----------------------------------------------------------------------
sub MonsterBuySpawn {

    my ($kind);
    $kind = random($HmonsterLevel3TABLE_NUM) + 1;
    $kind = $HmonsterTABLE[$kind];

    if (   (isSeaMonster($kind))    # 海の化け物
                          ) {
        $kind = 1;
    }
    return $kind;
}


#----------------------------------------------------------------------
# 海の怪獣かどうか
#----------------------------------------------------------------------
sub isSeaMonster {
    my($mKind) = @_;

    if (   ($mKind == $Mons_Unbaba)
        || ($mKind == 32)
        || (0)
                ){
        return 1;
    }
    return 0;
}


#----------------------------------------------------------------------
# 怪獣倒した後
#----------------------------------------------------------------------
sub MonsterDead {
    my ($island , $x , $y , $mKind , $WasteVal ) = @_;

    if ($mKind == $Mons_Kisinhei) {
        my ($landValue3) = $island->{'landValue3'};
        my ($val) = int(($landValue3->[$x][$y] / 500));
        $val = $val * 100;

        if ($val > 0) {
            food_product_plus($island , 'nazoniku' , $val);
            logKishinhei_down($island , "($x,$y)" , $val);
        }
    }

    $island->{'monsterlive'} -= 1 if ($island->{'monsterlive'}); #せこいけどガード
    MonsterDown( $island , $x , $y , $mKind , $WasteVal );
}


#----------------------------------------------------------------------
# 怪獣倒した後
#----------------------------------------------------------------------
sub MonsterDown {

    my ($island , $x , $y , $mKind , $WasteVal ) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    if (isSeaMonster($mKind)) {
        SetSeaLand_Normal($island , $x , $y);

    }else{

        if ($mKind == 33) {
            $land->[$x][$y] = $HlandYougan;
            $landValue->[$x][$y] = 1 + random(2);
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
        } else {
            $land->[$x][$y] = $HlandWaste;
            $landValue->[$x][$y] = $WasteVal;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
        }
    }
}

sub Food_Check_more_than {
    my($landkind) = @_;



}


#----------------------------------------------------------------------
# 海に見える土地
# 海底基地など
#----------------------------------------------------------------------
sub isBehindSea {
    my($landkind) = @_;

    if (   ($landkind == $HlandSeacity)
        || ($landkind == $HlandSeatown)
        || ($landkind == $HlandUmishuto)
        || ($landkind == $HlandSbase) ) {
        return 1;
    }
        return 0;

}


#----------------------------------------------------------------------
# たべものイベント
#----------------------------------------------------------------------
sub BigFoodEvent {
    my($island , $x , $y) = @_;# たべもの
    my($landValue) = $island->{'landValue'};
    my($baselv) = $landValue->[$x][$y];
    my($FoodHP) = $landValue->[$x][$y] & $Food_HP_MASK;
    my($Foodkind) = $landValue->[$x][$y] >> $Food_Kind_Shift;
    my($FoodName) = $BigFoodName[$Foodkind];

    my($point) = "($x,$y)";
    my($name) =islandName($island);

    my($land) = $island->{'land'};

    my($townCount) = countAround($land, $x, $y, 19, @Htowns);

    if ($townCount) {
        $FoodHP--;
        #$island->{'food'} += $townCount * 2;
        food_product_plus($island , 'yasai', ($townCount * 2) );
        if ($FoodHP > 0) {
            $landValue->[$x][$y] = ($Foodkind << $Food_Kind_Shift) | $FoodHP;
            logOut("${HtagName_}${name}$point${H_tagName}の<B>$FoodName</B>の体の一部が島民に食べられてしまい、<B>$FoodName</B>はダメージを受けました。",$island->{'id'} );

        }else{
            my($Foodva) = $BigFoodMoney[$Foodkind];
            logMsMonMoney($island->{'id'} , $FoodName , $Foodva);
            $island->{'money'} += $Foodva;
            $land->[$x][$y] = $HlandPlains;
            $landValue->[$x][$y] = 0;
        }
    }
}

# ---------------------------------------------------------------------
sub Write_ZooState {
    my ($island, $num , $val) = @_;

    my ($wdata) = '';
    my ($cnt);
    my ($canma) = '';
    my ($temp) = '';

    my ($tmp);
    my (@mons_list);
    my ($list_num);

    $tmp = $island->{'zoo'};
    chomp($tmp);

    @mons_list = split(/\,/,$tmp);

    if ($val < 0) {
        $val = 0;
    }

    $mons_list[$num] = $val;

    $list_num = $#mons_list;

    $list_num = ($list_num <= $num) ? $num : $list_num;

    for ($cnt = 0 ; $cnt <= $list_num ; $cnt++) {

        $temp = ($mons_list[$cnt] eq '') ? '0' : $mons_list[$cnt];

        if ($temp < 0) {
            $temp = 0;
        }

        $wdata .= $canma . $temp;
        $canma = ',';
    }

    chomp($wdata);
    $island->{'zoo'} = $wdata;
}


#----------------------------------------------------------------------
# 森イベント
#----------------------------------------------------------------------
sub ForestEvent {
    my($island , $x , $y) = @_;# 森
    my($landValue) = $island->{'landValue'};
    my($lv) = $landValue->[$x][$y];

    $landValue->[$x][$y]++ if($lv < $HForest_Limit); # 木を増やす
    if ( !random(3) ){
        $landValue->[$x][$y]++ if($lv < $HForest_Limit); # 木を増やす
    }
}

#----------------------------------------------------------------------
# FactoryEvent
#----------------------------------------------------------------------
sub FactoryEvent {
    my ($island , $x , $y) = @_;

    if (!$island->{'business'}) {
        return 0;
    }

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($lv2) = $landValue2->[$x][$y];

    if ($lv2 == 1) {
        if ($island->{'lumber_area'}) {

            my ($i , $fx,$fy);

            foreach $i (0..$pointNumber) {
                $fx = $Hrpx[$i];
                $fy = $Hrpy[$i];

                if (   ($land->[$fx][$fy] == $HlandForest)
                    && ($landValue->[$fx][$fy] >= $HForest_Limit) ) {

                    my ($cut) = $HForest_Limit - 5;
                    $landValue->[$fx][$fy] = 5;
                    my ($income) = $HtreeValue * $cut;
                    $island->{'money'} += $income;

                    my ($id) = $island->{'id'};
                    my ($name) = islandName($island);

                    my ($point) = "($x,$y)";
                    my ($fpoint) = "($fx,$fy)";

                    logSecret("${HtagName_}${name}$point${H_tagName}の<b>木工所</b>は${HtagName_}${fpoint}${H_tagName}の<b>森</b>を伐採し、${HtagMoney_}$income$HunitMoney${H_tagMoney}の収入がありました。",$id);
                    return 0;
                }
            }
        }
    }

    return 0;
}


#----------------------------------------------------------------------
# 荒地のイベント
#----------------------------------------------------------------------
sub WastelandEvent {
    my($island , $x , $y) = @_;

    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($landValue2) = $island->{'landValue2'};
    my($id) = $island->{'id'};

    # 荒れ地(BattleField)
    if(   (   ($id > 100)
           || (   ($land->[0][0] == $HlandMonument ) 
               && ($landValue->[0][0] == 70) ))
       && (!random(8) )) {

        if(!$landValue->[$x][$y]) {
            $land->[$x][$y] = $HlandPlains;
            $landValue2->[$x][$y]=0;
        } else {
            $landValue->[$x][$y]--;
        }
    }

    if (!$island->{'BF_Flag'}) {
        if (random(100) < 5) {
            WastelandEvent2($island,$x,$y);
        }
    }

}


#----------------------------------------------------------------------
# 荒地のイベント
#----------------------------------------------------------------------
sub WastelandEvent2 {
    my ($island , $x , $y) = @_;

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};

    my ($seaCount) = countAround($land, $x, $y, 7, @Hseas);

    # 荒れ地(BattleField)
    if($seaCount > 1) {
        if(!$landValue->[$x][$y]) {
            $landValue->[$x][$y] = 3;
        }
    }
}


#----------------------------------------------------------------------
# 消防署の土地イベント
#----------------------------------------------------------------------
sub FiredeptlandEvent {
    my ($island , $x , $y) = @_;

    if ( $island->{'money'} >= $HFiredept_cost ){
        $island->{'money'} -= $HFiredept_cost;

    }else{
        SetWasteLand_Normal($island , $x , $y);
    }
}

#----------------------------------------------------------------------
sub TaijiPrize {
    my ($island, $mKind) = @_;

    # デバッグ怪獣は除外
    if (grep {$_ == $mKind} @DebugMonster) {
        return;
    }

    # 怪獣退治数
    $island->{'taiji'}++;

    # 賞関係
    my ($prize) = $island->{'prize'};
    my ($prize1, $prize2) = split(/\t/, $prize);
    $prize1 =~ /([0-9]*),([0-9]*),(.*)/;
    my ($flags) = $1;
    my ($monsters) = $2;
    my ($turns) = $3;
    $monsters = $mKind if ( $mKind > $monsters);
    $island->{'prize'} = "$flags,$monsters,$turns\t$prize2";

    Set_taiji_list($island,$mKind);

}

#----------------------------------------------------------------------
sub Set_taiji_list {
    my ($island, $mKind) = @_;

    my ($block) = int($mKind/32);
    my ($tlist) = $island->{'taiji_list'}[$block];

    $tlist = $tlist | ( 1 << ($mKind % 32));

    $island->{'taiji_list'}[$block] = $tlist;
}


#----------------------------------------------------------------------
# 周囲の町、農場があるか判定
#----------------------------------------------------------------------
sub countGrow {
    my ($land, $landValue, $x, $y , $bf_flag) = @_;

    my ($i, $sx, $sy);
    for ($i = 1; $i < 7; $i++) {
        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # 行による位置調整
        $sx-- if(!($sy % 2) && ($y % 2));

        if(   (($sx >= 0) && ($sx < $HislandSize) && ($sy >= 0) && ($sy < $HislandSize))  # 範囲内の場合
           && (   ($land->[$sx][$sy] == $HlandTown)
               || ($land->[$sx][$sy] == $HlandProcity)
               || ($land->[$sx][$sy] == $HlandNewtown)
               || ($land->[$sx][$sy] == $HlandRizort)
               || ($land->[$sx][$sy] == $HlandBigRizort)
               || ($land->[$sx][$sy] == $HlandBettown)
               || ($land->[$sx][$sy] == $HlandBigtown)
               || ($land->[$sx][$sy] == $HlandHouse)
               || ($land->[$sx][$sy] == $HlandStation)
               || ($land->[$sx][$sy] == $HlandFarm) ) ) {

                return 1 if($landValue->[$sx][$sy] != 1);
        }

        if (   (   ($bf_flag == 1)
                && ($sx >= 0)
                && ($sx < $HislandSize)
                && ($sy >= 0)
                && ($sy < $HislandSize) )   # 範囲内の場合
            && ($land->[$sx][$sy] == $HlandDefence)
                                                    ) {
                return 1 ;
        }
    }
    return 0;
}


#----------------------------------------------------------------------
# 失業者はどこへ？
#----------------------------------------------------------------------
sub doIslandunemployed {
    my ($number, $island) = @_;

    # 導出値
    my ($name) = islandName($island);
    my ($id) = $island->{'id'};
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};

    # 失業者の移民
    if (   (   ($island->{'unemployed'} >= 100)
            || ($island->{'migrateByMons'}) )
        && (random(100) < 25) 
        && (!$island->{'BF_Flag'})  ) {

        # 失業者が１万人以上いると 25% の確率で移民を希望する
        my (@order) = randomArray($HislandNumber);
        my ($migrate);
        # 移民先を探す
        my ($tIsland);
        my ($n) = min($HislandNumber, 5);
        my ($i);
        my ($unemployed) = ($island->{'migrateByMons'}) ? int($island->{'pop'} * random(50) / 1000) : $island->{'unemployed'};
        my ($str) = ($island->{'migrateByMons'}) ? '巨大怪獣から逃れる' : '仕事を求める';

        for ($i = 0; $i < $n; $i++) { # ５島まで調べる
            $tIsland = $Hislands[$order[$i]];

            if ($tIsland->{'predelete'}) {
                next;
            }

            # 仕事のある島に移民する
            if ($tIsland->{'unemployed'} < 0) {
                $migrate = min($unemployed, -$tIsland->{'unemployed'});
                last;
            }
        }

        if ($i >= $n) {
            # 移民先が見つからなければ、暴動かデモ行進

            $migrate = random($unemployed - 100) + 100;
            $n = 0;
            my($x, $y, $landKind, $lv, $lv2);
            foreach $i (0..$pointNumber) {
                $x = $Hrpx[$i];
                $y = $Hrpy[$i];
                $landKind = $land->[$x][$y];
                $lv = $landValue->[$x][$y];
                $lv2 = $landValue2->[$x][$y];

                if(($landKind == $HlandFarm) ||
                    ($landKind == $HlandFactory) ||
                    ($landKind == $HlandHTFactory) ||
                    ($landKind == $HlandSHTF) ||
                    ($landKind == $HlandFarmchi) ||
                    ($landKind == $HlandFarmpic) ||
                    ($landKind == $HlandFarmcow) ||
                    ($landKind == $HlandCollege) ||
                    ($landKind == $HlandBase) ||
                    ($landKind == $HlandFoodim) ||
                    ($landKind == $HlandNursery) ||
                    (($landKind == $HlandMine) && (!($lv & $Hmine_DAMAGE_MASK))) ||
                    ($landKind == $HlandKatorikun) ||
                    ($landKind == $HlandPark) ||
                    ($landKind == $HlandKyujo) ||
                    ($landKind == $HlandYakusho) ||
                    ($landKind == $HlandKyujo) ||
                    ($landKind == $HlandKyujokai)) {
                    # 25% の確率で壊滅
                    if(random(100) < 25) {
                        $n++;
                        logUnemployedRiot($id, $name, landName($landKind, $lv,$lv2), $migrate, "($x, $y)", $str);
                        SetWasteLand_Normal($island , $x , $y);
                    }
                }
            }

            # 何も壊さないときはデモ行進を行う
            logUnemployedDemo($id, $name, $migrate, $str) if(!$n);

        } else {
            # 移民先が見つかったので移民
            my($tLand) = $tIsland->{'land'};
            my($tLandValue) = $tIsland->{'landValue'};
            my($tLandValue2) = $tIsland->{'landValue2'};

            {
                my($x, $y, $landKind, $lv, $lv2);
                foreach $i (0..$pointNumber) {
                    $x = $Hrpx[$i];
                    $y = $Hrpy[$i];
                    $landKind = $tLand->[$x][$y];
                    $lv = $tLandValue->[$x][$y];
                    $lv2 = $tLandValue2->[$x][$y];

                    if($landKind == $HlandSeki) {
                        logUnemployedReturn($id, $tIsland->{'id'}, $name, landName($landKind, $lv, $lv2), islandName($tIsland), $migrate, $str);
                        return 1;
                    }
                }
            }

            # 移民先の町に家を用意する
            my($employed) = $migrate;
            my($x, $y, $landKind, $lv, $lv2);
            foreach $i (0..$pointNumber) {
                $x = $Hrpx[$i];
                $y = $Hrpy[$i];
                $landKind = $tLand->[$x][$y];
                $lv = $tLandValue->[$x][$y];
                $lv2 = $tLandValue2->[$x][$y];

                if(($landKind == $HlandOnsen) ||    # 100
                    ($landKind == $HlandTown) ||    # 200
                    ($landKind == $HlandMinato) ||  # 200
                    ($landKind == $HlandSeacity) || # 200
                    ($landKind == $HlandFrocity) || # 200
                    ($landKind == $HlandNewtown) || # 300
                    (($landKind == $HlandBigtown)&&($island->{'yaku'} >= 4)) || # 500
                    (($landKind == $HlandBettown)&&($island->{'yaku'} >= 6)) || # 2000
                                 (0)           ) {
                    # 町
                    # my $nMax = ($landKind == $HlandNewtown) ? 300 : ($landKind == $HlandOnsen) ? 100 : 200;
                    my $nMax = 0;
                    $nMax = $HOnsen_limit  if($landKind == $HlandOnsen);    # 温泉
                    $nMax = $HTown_limit     if($landKind == $HlandTown);       # 町
                    $nMax = $HTown_limit  if($landKind == $HlandMinato);    # ニュータウン
                    $nMax = $HTown_limit     if($landKind == $HlandSeacity);       # 町
                    $nMax = $HFrocity_limit     if($landKind == $HlandFrocity);       # 町
                    $nMax = $HNewtown_limit  if($landKind == $HlandNewtown);    # ニュータウン
                    $nMax = $HBigtown_limit  if($landKind == $HlandBigtown);    # 現代都市系
                    $nMax = $HBettown_limit  if($landKind == $HlandBettown);    # 輝ける都市

                    $n = int(($nMax - $lv) / 2);
                    if ($n == 0) {

                        $n = min( ($nMax - $lv) , $employed);
                    }else{
                        $n = min(int($n + random($n)), $employed);
                    }
                    $employed -= $n;
                    $tLandValue->[$x][$y] += $n;

                } elsif( ($landKind == $HlandPlains) && ($lv == 0)) {
                    # 平地
                    $n = int(($HTown_limit - $lv) / 2);
                    $n = min(int($n + random($n)), $employed);
                    $employed -= $n;
                    $tLand->[$x][$y] = $HlandTown;
                    $tLandValue->[$x][$y] = $n;
                    logPlains2Town($tIsland, landName($HlandTown, $n, $lv2) ,"($x, $y)");
                }
                last if($employed <= 0);
            }

            $migrate -= $employed;
            $island->{'unemployed'} -= $migrate;
            $tIsland->{'unemployed'} += $migrate;
            $island->{'pop'} -= $migrate;
            $tIsland->{'pop'} += $migrate;

            # 今まで住んでいた家を処分する
            $employed = $migrate;
            foreach $i (0..$pointNumber) {
                $x = $Hrpx[$i];
                $y = $Hrpy[$i];
                $landKind = $land->[$x][$y];
                $lv = $landValue->[$x][$y];

                if (   ($lv > 1)
                    && (   ($landKind == $HlandTown)
                        || ($landKind == $HlandMinato)
                        || ($landKind == $HlandProcity)
                        || ($landKind == $HlandNewtown)
                        || ($landKind == $HlandFrocity)
                        || ($landKind == $HlandBettown)
                        || ($landKind == $HlandShuto)
                        || ($landKind == $HlandUmishuto)
                        || ($landKind == $HlandBigtown)
                        || ($landKind == $HlandSeatown)
                        || ($landKind == $HlandOnsen)
                        || ($landKind == $HlandSeacity)
                        || ($landKind == $HlandUmicity)
                        || ($landKind == $HlandOilCity)
                        || ($landKind == $HlandInaka)
                                                        )) {
                    # 町
                    $n = min($lv - 1, $employed);
                    $landValue->[$x][$y] -= $n;
                    $employed -= $n;
                }
                last if($employed <= 0);
            }

            if ($migrate) {
                logUnemployedMigrate($id, $tIsland->{'id'}, $name, islandName($tIsland), $migrate, $str);
                # 災難賞判定のために移民を記憶
                $island->{'migrate'} = $migrate if(!$island->{'migrateByMons'});
            }
        }
    }
}


#----------------------------------------------------------------------
# 島全体
#----------------------------------------------------------------------
sub doIslandProcess {
    my($number, $island) = @_;

    # 導出値
    my($name) = islandName($island);
    my($id) = $island->{'id'};
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    my $disdown    = 1;
    if ($HallyDisDown && ($island->{'allyId'}[0] ne '')) {
        $disdown   = $HallyDisDown;
    }
    my $pika2 = 0;

    # 収入ログ(まとめてログ出力)
    if ($HlogOmit1) {
        logOilMoney($id, $name, "油田", "", "総額$island->{'oilincome'}${HunitMoney}", "収益") if(($island->{'oilincome'} > 0));
        logOilMoney($id, $name, "遊園地", "", "総額$island->{'parkincome'}${HunitMoney}", "収益") if(($island->{'parkincome'} > 0));
        logParkEventf($id, $name, "漁業組合", "", "総漁獲高$island->{'fishcatch'}${HunitFood}") if(($island->{'fishcatch'} > 0));
    }

    # 収入ログ(ミカエル像)
    if (STATUE_LOG_OMIT) {
        if ($island->{'statue_income'} > 0 ) {
            logMiyage($id, $name, "幸福の女神像", "", "総額$island->{'statue_income'}$HunitMoney");
        }
        if ($island->{'statue_income_food'} > 0 ) {
            logParkEventt($id, $name, "幸福の女神", "", "$island->{'statue_income_food'}$HunitFood");
        }
    }

    if ($island->{'stsankahantei'} == 1) {
        $value = $Hstsanka*random(2000);
        $island->{'money'} += $value;
        logHCstart($id, $name, "$value$HunitMoney");
    }

    if($island->{'shtf'} > 0) {
        $pika2 = int($island->{'factory'}/2);
        if ($pika2 > 0) {
            $island->{'money'} -= $pika2;
            logFactoryHT($id, $name, "ハイテク企業", "$pika2${HunitMoney}") ;
        }

    }elsif($island->{'htf'} > 0) {
        $pika2 = int($island->{'pika'}/2);
        if ($pika2 > 0) {
            $island->{'money'} -= $pika2;
            logFactoryHT($id, $name, "ハイテク企業", "$pika2${HunitMoney}") ;
        }
    }

    # 津波判定
    if(   ($HpunishInfo{$id}->{punish} == 2)
       || (!$HnoDisFlag && random(1000) < int($HdisTsunami[0] * $disdown - $island->{'eis2'}/15)) ) {
        # 津波発生
        logTsunami($id, $name);

        my($x, $y, $landKind, $lv, $i);
        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];
            $lv = $landValue->[$x][$y];

            if(   ($landKind == $HlandTown)
               || (   ($landKind == $HlandProcity)
                   && ($lv < 110) )
               || ($landKind == $HlandFarm)
               || ($landKind == $HlandFarmchi)
               || ($landKind == $HlandFarmpic)
               || ($landKind == $HlandFarmcow)
               || ($landKind == $HlandFoodim)
               || ($landKind == $HlandFactory)
               || ($landKind == $HlandHTFactory)
               || ($landKind == $HlandSHTF)
               || ($landKind == $HlandCollege)
               || ($landKind == $HlandStation)
               || ($landKind == $HlandBase)
               || ($landKind == $HlandDefence)
               || ($landKind == $HlandPark)
               || ($landKind == $HlandMinato)
               || ($landKind == $HlandFune)
               || ($landKind == $HlandSeki)
               || ($landKind == $HlandMine)
               || ($landKind == $HlandZoo)
               || ($landKind == $HlandNursery)
               || ($landKind == $HlandKyujo)
               || ($landKind == $HlandKyujokai)
               || ($landKind == $HlandBettown)
               || ($landKind == $HlandRizort)
               || ($landKind == $HlandYakusho)
               || ($landKind == $HlandBigRizort)
               || ($landKind == $HlandShuto)
               || ($landKind == $HlandNewtown)
               || ($landKind == $HlandUmicity)
               || ($landKind == $HlandBigtown)
               || ($landKind == $HlandOilCity)
               || ($landKind == $HlandKatorikun) ) {

                # 1d12 <= (周囲の海 - 1) で崩壊
                my @seas = @Hseas;
                pop(@seas);
                if (random(12+$island->{'co5'}*5) < (countAround($land, $x, $y, 7, @seas) - 1)) {
                    logDamageAny($id, $name, landName($landKind, $lv,$landValue2->[$x][$y]), "($x, $y)", "${HtagDisaster_}津波${H_tagDisaster}により崩壊しました。");
                    if(   ($landKind == $HlandFune)
                       || ($landKind == $HlandUmicity)
                       || ($landKind == $HlandOilCity)
                                                    ) {
                        $land->[$x][$y] = $HlandSea;
                        $landValue->[$x][$y] = 0;
                        $landValue2->[$x][$y] = 0;
                        # でも養殖場なら浅瀬
                    } elsif($landKind == $HlandNursery) {
                        $land->[$x][$y] = $HlandSea;
                        $landValue->[$x][$y] = 1;
                        $landValue2->[$x][$y] = 0;
                    } else {

                        SetWasteLand_Normal($island , $x , $y);     # $HlandWaste
                    }
                }
            }
        }
    }

    # 地震判定
    if (   ($HpunishInfo{$id}->{punish} == 1)
        || (   (!$HnoDisFlag) 
            && (random(1000) < int(($island->{'prepare2'} + 1) * $HdisEarthquake[0] * $disdown - $island->{'eis2'}/15)) )
                                                                                                                        ) {
        # 地震発生
        logEarthquake($id, $name);
        $HdisTsunami[0] = $HdisTsunami[1];

        my($x, $y, $landKind, $lv,$lv2, $i);

        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];
            $lv = $landValue->[$x][$y];
            $lv2 = $landValue2->[$x][$y];

            if (
                 ($landKind == $HlandHaribote) ||
                 (($landKind == $HlandFoodim) && ($lv < 480)) || 
                 ($landKind == $HlandTrain) ||
                 ($landKind == $HlandPark) ||
                 ($landKind == $HlandOnsen) ||
                 ($landKind == $HlandStation) ||
                 ($landKind == $HlandKatorikun) ||
                 ($landKind == $HlandSeki) ||
                 ($landKind == $HlandRocket) ||
                 ($landKind == $HlandDefence) ||
                 ($landKind == $HlandFactory)
                                                ) {
                # 1/4で壊滅
                if (!random(4+$island->{'co5'}*5)) {
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}地震${H_tagDisaster}により壊滅しました。");
                    SetWasteLand_Normal($island , $x , $y);

                    if ($landKind == $HlandOnsen) {
                        # 温泉は山に戻る
                        $land->[$x][$y] = $HlandMountain; # 海になる
                        $landValue->[$x][$y] = 0;
                        $landValue2->[$x][$y] = 0;
                    }
                    next;
                }
            }

            if (   (($landKind == $HlandTown) && ($lv >= 100))
                || (($landKind == $HlandProcity) && ($lv < 130))
                || (($landKind == $HlandMinato) && ($lv >= 100))
                || (($landKind == $HlandNewtown) && ($lv >= 100))
                || (($landKind == $HlandBigRizort) && ($lv >= 100))
                || (($landKind == $HlandRizort) && ($lv >= 100))
                || (($landKind == $HlandBigtown) && ($lv >= 100))
                || (($landKind == $HlandBettown) && ($lv >= 100))
                || (($landKind == $HlandShuto) && ($lv >= 100))
                                                    ) {
                # 1/4で壊滅
                if(!random(4+$island->{'co5'}*5)) {

                    if (countAround($land, $x, $y, 7, $HlandPlains,$HlandKyujo,$HlandYakusho,$HlandKyujokai,$HlandMonument,$HlandFiredept,$HlandCollege) ) {
                        logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}地震${H_tagDisaster}により被害を受けました。");
                        $landValue->[$x][$y] -= random(30)+10;

                    }else{

                        logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}地震${H_tagDisaster}により壊滅しました。");
                        $landValue->[$x][$y] -= random(100)+50;

                    }
                    if($landValue->[$x][$y] <= 0) {
                        # 平地に戻す
                        SetWasteLand_Normal($island , $x , $y);
                        if ($landKind == $HlandOnsen) {
                            # 温泉は山に戻る
                            $land->[$x][$y] = $HlandMountain; # 山になる
                            $landValue->[$x][$y] = 0;
                            $landValue2->[$x][$y] = 0;
                        }
                        logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}地震${H_tagDisaster}により壊滅しました。");
                        next;
                    }
                }
            }

            if (   (0)
                || (($landKind == $HlandHTFactory) && ($lv >= 10))
                || (($landKind == $HlandSHTF) && ($lv >= 10))
                || (($landKind == $HlandUmishuto) && ($lv >= 100))
                || (($landKind == $HlandSeatown) && ($lv >= 100))
                || (($landKind == $HlandSeacity) && ($lv >= 100))
                || (($landKind == $HlandUmicity) && ($lv >= 100))
                || (($landKind == $HlandOilCity) && ($lv >= 100))
                || (($landKind == $HlandUmiamu) && ($lv >= 10))
                || (($landKind == $HlandInoraLand) && ($lv >= 10))
                                                                    ) {
                # 1/4で壊滅
                if (!random(3+$island->{'co5'}*5)) {
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}地震${H_tagDisaster}により被害を受けました。");
                    $landValue->[$x][$y] -= random(100)+50;
                }
                if ($landValue->[$x][$y] <= 0) {
                    # 平地に戻す
                    SetWasteLand_Normal($island , $x , $y);
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}地震${H_tagDisaster}により壊滅しました。");
                    next;
                }
            }

            if (   ($landKind == $HlandFarmchi)
                || ($landKind == $HlandFarmpic)
                || ($landKind == $HlandFarmcow)
                                                    ) {

                if (!random(6)) {
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}地震${H_tagDisaster}により被害を受けました。");
                    $landValue->[$x][$y] -= random(400)+50;
                }

                if ($landValue->[$x][$y] <= 0) {
                    # 平地に戻す
                    SetWasteLand_Normal($island , $x , $y);
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}地震${H_tagDisaster}により壊滅しました。");
                    next;
                }
            }
        }
    }

    # 重税にきれる住民
    if (random(100) < int(($island->{'eisei1'} - 10 - random(5)) * $disdown)) {
        # 不足メッセージ
        logKire($id, $name);

        my($x, $y, $landKind, $lv, $i);
        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];
            $lv = $landValue->[$x][$y];

            if (   ($landKind == $HlandFarm)
                || ($landKind == $HlandCollege)
                || ($landKind == $HlandFactory)
                || ($landKind == $HlandHTFactory)
                || ($landKind == $HlandSHTF)
                || ($landKind == $HlandNursery)
                || ($landKind == $HlandBase)
                || ($landKind == $HlandKatorikun)
                || ($landKind == $HlandPark)
                || ($landKind == $HlandKyujo)
                || ($landKind == $HlandZoo)
                || ($landKind == $HlandKyujokai)
                || ($landKind == $HlandDefence)
                || ($landKind == $HlandYakusho)
                || ($landKind == $HlandHouse)
                                                ) {
                # 1/4で壊滅
                if (random(100) < $island->{'eisei1'}) {
                    logKireDamage($id, $name, landName($landKind, $lv,$landValue2->[$x][$y]), "($x, $y)");
                    SetWasteLand_Normal($island , $x , $y);
                    # でも養殖場なら浅瀬
                    if ($landKind == $HlandNursery) {
                        $land->[$x][$y] = $HlandSea;
                        $landValue->[$x][$y] = 1;
                        $landValue2->[$x][$y] = 0;
                    }
                }
            }

            if(($landKind == $HlandTown) ||
                ($landKind == $HlandMinato) ||
                ($landKind == $HlandFoodim) ||
                ($landKind == $HlandProcity) ||
                ($landKind == $HlandFarmchi) ||
                ($landKind == $HlandFarmpic) ||
                ($landKind == $HlandFarmcow)) {
                # 1/4で壊滅
                if(random(100) < $island->{'eisei1'}-30) {
                    logKireDamage($id, $name, landName($landKind, $lv,$landValue2->[$x][$y]), "($x, $y)");
                    SetWasteLand_Normal($island , $x , $y);
                }
            }

            if (($landKind == $HlandSbase) ||
                ($landKind == $HlandSeacity) ||
                ($landKind == $HlandUmiamu) ||
                ($landKind == $HlandFrocity)) {
                # 1/4で壊滅
                if (random(100) < $island->{'eisei1'}-60) {
                    logKireDamage($id, $name, landName($landKind, $lv,$landValue2->[$x][$y]), "($x, $y)");
                    $land->[$x][$y] = $HlandSea;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                }
            }
        }
    }

    # 食料不足
    my ($landKind, $lv , $wo);
    $landKind = $land->[$x][$y];
    $lv = $landValue->[$x][$y];

    $wo = 0;
    if (   ($landKind == $HlandMonument)
        && ($lv == 70)) {
        $wo = 1;
    }

    if (($island->{'food'} <= 0) && ($id <= 100) && (!$wo)) {
        # 不足メッセージ
        logStarve($id, $name);
        food_product_All_Clear($island);

        my ($x, $y, $i);

        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];
            $lv = $landValue->[$x][$y];

            if (   ($landKind == $HlandFarm)
                || ($landKind == $HlandFoodim)
                || ($landKind == $HlandFarmchi)
                || ($landKind == $HlandFarmpic)
                || ($landKind == $HlandFarmcow)
                || ($landKind == $HlandFactory)
                || ($landKind == $HlandHTFactory)
                || ($landKind == $HlandSHTF)
                || ($landKind == $HlandCollege)
                || ($landKind == $HlandNursery)
                || ($landKind == $HlandBase)
                || ($landKind == $HlandMine)
                || ($landKind == $HlandZoo)
                || ($landKind == $HlandYakusho)
                || ($landKind == $HlandKatorikun)
                || ($landKind == $HlandStation)
                || ($landKind == $HlandDefence)
                                                ) {
                # 1/4で壊滅
                if(!random(4)) {
                    logSvDamage($id, $name, landName($landKind, $lv, $landValue2->[$x][$y]), "($x, $y)");
                    SetWasteLand_Normal($island , $x , $y);

                    # でも養殖場なら浅瀬
                    if($landKind == $HlandNursery) {
                        $land->[$x][$y] = $HlandSea;
                        $landValue->[$x][$y] = 1;
                        $landValue2->[$x][$y] = 0;
                    }
                }
            }
        }
    }

    # 怪獣判定
    my ($real) = ($HislandTurn + 8) % 12 ;
    my ($r, $pop, $num );

    $island->{'event_monstersend'} = 0;

    {
        if ($HDayEvent_Edge) {
            my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
            $mon += 1;
            if (($mon == 3) && ($mday == 3)) {
                $island->{'event_monstersend'} = 1;
                $HDayEvent_Edge--;
            }
        }
    }

    $num = 0;
    if( ($island->{'id'} > 100) || 
        (($land->[0][0] == $HlandMonument) && ($landValue->[0][0] == 70) ) ) {
        $r = random(10000);
        $r = -1 if( $island->{'monsterlive'} < 40 ) ;
        $pop = $HdisMonsBorder3;
        $num = random(4) + random(4) + random(4) + 1;
    } else {
        $r = random(10000);
        $pop = $island->{'pop'};
    }

    $r = $HdisMonster[$real] * $island->{'area'} if ($HnoDisFlag);
    $r = $HdisMonster[$real] * $island->{'area'} if ($island->{'omamori'});
    $r = 0 if ($HpunishInfo{$id}->{punish} == 3);

    my ($sea_build) = $island->{'sea_build'};

    do {
        $num-- ;
        if(   (   ($r < int($HdisMonster[$real] * $disdown * $island->{'area'})) 
               && ($pop >= $HdisMonsBorder1)) 
           || ($island->{'monstersend'} > 0)
           || ($island->{'event_monstersend'} > 0) ) {

            # 怪獣出現
            # 種類を決める
            my ($kind,$lv2);

            if (   ($island->{'BF_Flag'} == 1)
                || ($island->{'monstersend'} > 0)
                || ($island->{'event_monstersend'} > 0) ) {

                ($kind,$lv2) = MonsterSpawnKind($island , 1);
            }
            elsif (   (   ($sea_build < 20)
                       && (random(100) < 90) ) ) {

                ($kind,$lv2) = MonsterSpawnKind($island , 1);
            }
            else {
                $kind = (random(2)) ? $Mons_Unbaba : $Mons_Pirates ;
                $lv2 = 0;
            }

            my ($lv) = Calc_MonsterLandValue($kind);

            # どこに現れるか決める
            my ($bx, $by, $i, $def , $tar_kind);
            my ($escape) = 1;

            foreach $i (0..$pointNumber) {
                $bx = $Hrpx[$i];
                $by = $Hrpy[$i];
                $def = 0;
                $def = countAround($land, $bx, $by, 19, $HlandDefence) if ($island->{'BF_Flag'} == 1) ;

                $tar_kind = $land->[$bx][$by];

                if (   (   (   ($kind != $Mons_Unbaba)
                            && ($kind != $Mons_hime_inora)
                            && ($kind != $Mons_Pirates)
                            && (   ($tar_kind == $HlandTown)        # 町系
                                || ($tar_kind == $HlandNewtown)     # ニュータウン
                                || ($tar_kind == $HlandBigtown)     # 現代都市
                                || ($tar_kind == $HlandBettown)     # 輝ける都市
                                || ($tar_kind == $HlandRizort)      # リゾート地
                                || ($tar_kind == $HlandBigRizort)   # 臨海リゾートホテル
                                || ($tar_kind == $HlandForest)      # 森
                                || ($tar_kind == $HlandWaste)       # 荒地
                                || ($tar_kind == $HlandFarm)        # 農場
                                || ($tar_kind == $HlandTrain)       # 線路
                                || ($tar_kind == $HlandHaribote)    # ハリボテ
                                || ($tar_kind == $HlandFactory)     # 工場
                                || ($tar_kind == $HlandRocket)      # ロケット
                                                                 ))
                        || (   ($kind == $Mons_Unbaba)
                            && (   ($tar_kind == $HlandSea)         # 海
                                || ($tar_kind == $HlandOil)         # 海底油田
                                || ($tar_kind == $HlandMinato)      # 港
                                || ($tar_kind == $HlandFune)        # 船舶
                                || ($tar_kind == $HlandNursery)     # 養殖場
                                || ($tar_kind == $HlandFrocity)     # フロート
                                || ($tar_kind == $HlandSbase)       # 海底基地
                                || ($tar_kind == $HlandSeacity)     # 海底都市
                                || ($tar_kind == $HlandUmiamu)      # 海あみゅ
                                || ($tar_kind == $HlandIce)         # 氷河
                                || (($tar_kind == $HlandSunahama) && (!$lv))   # 砂浜
                                                                 ))
                        || (   ($kind == $Mons_Pirates)
                            && (   ($tar_kind == $HlandSea)         # 海
                                                                 ))
                        || (   ($kind == $Mons_hime_inora)
                            && (   ($tar_kind == $HlandSea)         # 海
                                || ($tar_kind == $HlandWaste)       # 荒地
                                || ($tar_kind == $HlandPlains)      # 平地
                                                                 ))
                                                                    )
                    && ($def == 0)          # BF用
                                     ) {

                    if ( (isSeaMonster($kind)) ) {
                        if (countAround($land, $bx, $by, 7, $HlandForest) > 0 ){
                            next;
                        }
                    }

                    my ($mlv3) = 0;

                    if ($kind == $Mons_Kisinhei) {

                        my ($atk_kind);
                        my ($temp);
                        $mlv3 = $landValue3->[$bx][$by];
                        my ($atkx , $atky);
                        for ($i = 1; $i < 7; $i++) {
                            $atkx = $bx + $ax[$i];
                            $atky = $by + $ay[$i];

                            # 行による位置調整
                            $atkx-- if(!($atky % 2) && ($by % 2));

                            # 範囲内の場合
                            if (($atkx >= 0) && ($atkx < $HislandSize) && ($atky >= 0) && ($atky < $HislandSize)) {

                                $atk_kind = ($land->[$atkx][$atky]);

                                foreach my $ta (@Htowns) {
                                    if ($atk_kind == $ta) {
                                        if ($landValue->[$atkx][$atky] > 4) {
                                            $temp = ($landValue->[$atkx][$atky] >> 1);
                                            $landValue->[$atkx][$atky] -= $temp;
                                            $mlv3 += $temp;
                                        }
                                    }
                                }
                            }
                        }
                        logKishinhei_kyusyu($island , "($bx , $by)" , $mlv3);
                    }

                    # 地形名
                    my($lName) = landName($tar_kind, $landValue->[$bx][$by], $landValue2->[$bx][$by]);
                    # そのヘックスを怪獣に
                    $land->[$bx][$by] = $HlandMonster;
                    $landValue->[$bx][$by] = $lv;
                    $landValue2->[$bx][$by] = 0;
                    $landValue3->[$bx][$by] = $mlv3;
                    $escape = 0 ;

                    # ツイッターbot用 BFは除外
                    if (!$island->{'BF_Flag'}) {
                        $Appearance_monster = $HmonsterImage[$kind];
                    }

                    # 怪獣情報
                    $mName = $HmonsterName[$kind];

                    # メッセージ
                    logMonsCome($id, $name, $mName, "($bx, $by)", $lName);
                    last;
                }
            }

            if ($escape) {
                $island->{'monstersend'} = 0;
                $num = 0;
                last;
            }
        }
    } while( ( $island->{'monstersend'} > 0 ) || ($num > 0) );


    # 地盤沈下判定
    if (    (   ($HpunishInfo{$id}->{punish} == 4) 
             || (!$HnoDisFlag && random(1000) < int($HdisFalldown[0] * $disdown))) 
         && ($island->{'area'} > $HdisFallBorder)
         && (!$island->{'BF_Flag'}) ) {

        # 地盤沈下発生
        logFalldown($id, $name);

        my ($x, $y, $landKind, $lv, $lv2, $i);
        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];
            $lv2 = $landValue2->[$x][$y];
            $lv = $landValue->[$x][$y];

            if (($landKind != $HlandSea) &&
                ($landKind != $HlandSbase) &&
                ($landKind != $HlandIce) &&
                ($landKind != $HlandSeacity) &&
                ($landKind != $HlandSeatown) &&
                ($landKind != $HlandFune) &&
                ($landKind != $HlandUmishuto) &&
                ($landKind != $HlandUmiamu) &&
                ($landKind != $HlandOil) &&
                ($landKind != $HlandGold) &&
                ($landKind != $HlandShrine) &&
                ($landKind != $HlandOnsen) &&
                ($landKind != $HlandMountain)) {

                # 周囲に海があれば、値を-1に
                my @seas = @Hseas;
                pop(@seas);
                pop(@seas);
                if (countAround($land, $x, $y, 7, @seas)) {
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "海の中へ沈みました。");
                    $land->[$x][$y] = -1;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                }
            }
        }

        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];

            if($landKind == -1) {
                # -1になっている所を浅瀬に
                $land->[$x][$y] = $HlandSea;
                $landValue->[$x][$y] = 1;
            } elsif($landKind == $HlandSea) {
                # 浅瀬は海に
                $landValue->[$x][$y] = 0;
            }
        }
    }

    # 台風判定
    if(    ($HpunishInfo{$id}->{punish} == 5)
        || (    (!$HnoDisFlag)
             && (random(1000) < int($HdisTyphoon[$Hmonth] * $disdown - $island->{'eis1'}/10)) ) ) {
        # 台風発生
        logTyphoon($id, $name);

        my($x, $y, $landKind, $lv, $lv2, $i);
        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];
            $lv  = $landValue->[$x][$y];
            $lv2 = $landValue2->[$x][$y];

            if (   ($landKind == $HlandFarm)
                || ($landKind == $HlandHaribote)
                || ($landKind == $HlandTrain)
                                                ) {
                # 1d12 <= (6 - 周囲の森) で崩壊
                if(random(12+$island->{'co5'}*5) < (6 - countAround($land, $x, $y, 7, $HlandForest, $HlandMonument))) {
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}台風${H_tagDisaster}で飛ばされました。");
                    $land->[$x][$y] = $HlandPlains;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    if (   ($landKind == $HlandFarm)
                        && ($lv2 == 2) ) {
                        $land->[$x][$y] = $HlandSunahama;
                    }

                    if (random(1000) < 100) {
                        $land->[$x][$y] = $HlandMonument;
                        $landValue->[$x][$y] = 77;
                    }
                }
            }

            if(   (   ($landKind == $HlandFune)
                   || ($landKind == $HlandNursery) )
               && (random(100+$island->{'co5'}*50) < 10) ) {
                logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}台風${H_tagDisaster}によって破損しました。");
                $land->[$x][$y] = $HlandSea;
                $landValue->[$x][$y] = 1;
                $landValue2->[$x][$y] = 0;
            }
        }
    }

    my($def_flag);
    # 巨大隕石判定
    if(   ($HpunishInfo{$id}->{punish} == 6)
       || (   (!$HnoDisFlag)
           && (random(1000) < int($HdisHugeMeteo[$Hmonth] * $disdown - $island->{'eis3'}/50)) )) {
        my($x, $y, $landKind, $lv, $point);

        # 落下
        $x = random($HislandSize);
        $y = random($HislandSize);

        $HSpaceDebri -= $HSpaceDebri_meteo;     #スペースデブリ

        if ($HpunishInfo{$id}->{punish} == 6) {
            $x = $HpunishInfo{$id}->{x};
            $y = $HpunishInfo{$id}->{y};
        }
        $landKind = $land->[$x][$y];
        $lv = $landValue->[$x][$y];
        $point = "($x, $y)";

        $def_flag = 0;
        if ( $landKind == $HlandDefence ) {
            my($defLv , $defHP );
            $defHP = 0;
            $defLv = 0;
            $defLv = ($lv & $HDefenceLevelMask);

            if ( $defLv >= 2 ) {
                $def_flag = 1;
                $defHP = $lv >> $HDefenceHP_SHIFT;
                $defHP = $defHP - 3;
                $defHP = 0 if ( $defHP < 0 );
                $landValue->[$x][$y] = 2 + ( $defHP << $HDefenceHP_SHIFT ) ;
            }

            if ( $defHP <= 0 ) {
                logMeteoDef($id, $name, $lName, $point, "し、直撃し");
                $def_flag = 0;
            }

        }else{
            $def_flag = countAround_DefBase($land,$landValue, $x, $y, 19, 1);
        }

        if( $def_flag ){
            logMeteoDef($id, $name, $lName, $point, "しましたが、防衛基地・改に守られ");
            next;
        }

        # メッセージ
        logHugeMeteo($id, $name, $point);

        # 広域被害ルーチン
        wideDamage($id, $name, $land, $landValue, $x, $y);
        if (random(1000) < 100) {
            $land->[$x][$y] = $HlandMonument;
            $landValue->[$x][$y] = 79;
        }
    }

    # 巨大ミサイル判定
    BigMissileRoutine($island);

    Flood($island);

    # 隕石判定
    my ($rnd) = random(1000);
    if (   ($HpunishInfo{$id}->{punish} == 7)
        || (   (!$HnoDisFlag)
            && ($rnd < int($HdisMeteo[0] * $disdown)))) {

        if ($rnd < int($HdisMeteo[0] * $disdown - $island->{'eis3'}/40)) {
            Meteo_disaster($island);
        }else{
            logMeteo_Safe($island);
        }
    }

    # ポッキーの日
    Pockey_Event($island);

    # 噴火判定
    if(   ($HpunishInfo{$id}->{punish} == 8)
       || (!$island->{'BF_Flag'})
           && (!$HnoDisFlag && random(1000) < int($HdisEruption[0] * $disdown - $island->{'eis2'}/40))) {

        my($x, $y);

        $x = random($HislandSize);
        $y = random($HislandSize);
        if ($HpunishInfo{$id}->{punish} == 8) {
            $x = $HpunishInfo{$id}->{x};
            $y = $HpunishInfo{$id}->{y};
        }

        Volcano($island,$x,$y);
    }

    # 人工衛星エネルギー減少
    Satellite_Energy($island);

    Satellite_Irregular_Attack($island);

    # 役所の掃除を始める
    if ($island->{'yaku'}){
        Yakusyo_clean($island);
    }
}


#----------------------------------------------------------------------
sub isPockeyDay {
    my($mon , $mday) = @_;

    if (   ($mon == 11)
        && ($mday == 11) ) {

        return 1;
    }
    return 0;
}

#----------------------------------------------------------------------

sub Pockey_Event {
    my ($island) = @_;

    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $mon += 1;

    if ($HDayEvent_Edge) {

        if (isPockeyDay($mon , $mday) ) {
            logOut("isPockeyDay" , 1);

            my ($x,$y);
            my ($i);
            my ($landKind);
            my ($lv);
            my ($land) = $island->{'land'};
            my ($landValue) = $island->{'landValue'};

            for ($i = 0; $i < $HpointNumber; $i++){

                $x = $Hrpx[$i];
                $y = $Hrpy[$i];
                $landKind = $land->[$x][$y];
                $lv = $landValue->[$x][$y];

                if (   ($landKind == $HlandPlains)
                    || ($landKind == $HlandWaste)
                    || (($landKind == $HlandSea) && ($lv != 0) ) ) {

                    my ($point) = "($x, $y)";
                    my ($lv2) = $island->{'landValue2'};
                    my ($lv3) = $island->{'landValue3'};
                    # ポッキー
                    my($mKind) = 4 + random(4);
                    $lv = ($mKind << $Food_Kind_Shift) + (5) ; #チョコレート HP5
                    $ItemName = landName($HlandBigFood, $lv, 0);

                    $land->[$x][$y] = $HlandBigFood;
                    $landValue->[$x][$y] = $lv;
                    $lv2->[$x][$y] = 0;
                    $lv3->[$x][$y] = 0;

                    my ($name) = islandName($island);

                    logOut("${HtagName_}${name}${point}${H_tagName}に宇宙から<B>$ItemName</B>が送られました。",$island->{'id'} );

                    last;
                }
            }
        }
    }


}

#----------------------------------------------------------------------
sub Satellite_Irregular_Attack {
    my ($island) = @_;

    my ($name) = islandName($island);
    my ($id) = $island->{'id'};
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    #my ($landValue2) = $island->{'landValue2'};
    #my ($landValue3) = $island->{'landValue3'};


    if ($island->{'eis6'}) {
        my ($i, $sx, $sy);
        for ($i = 0; $i < $HpointNumber; $i++){
            $sx = $Hrpx[$i];
            $sy = $Hrpy[$i];
            if ($land->[$sx][$sy] == $HlandMonster){
                # 怪獣がいる場合、その怪獣を攻撃する
                # 対象となる怪獣の各要素取り出し
                my($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                my($tlv) = $landValue->[$sx][$sy];
                #my($tspecial) = $HmonsterSpecial[$tKind];
                $point = int($island->{'rena'}/1000);
                logIreAttackt($id, $name, "イレギュラー", $point, $tName, $tPoint);

                $island->{'eis6'} -= 10;

                $tHp -= int($island->{'rena'}/1000);
                $tlv -= int($island->{'rena'}/1000);
                $landValue->[$sx][$sy] = $tlv;
                if($tHp < 1){
                    # 対象の怪獣が倒れて荒地になる
                    MonsterDead($island , $sx , $sy , $tKind , 0 );
                    # 報奨金
                    my($value) = $HmonsterValue[$tKind];
                    $island->{'money'} += $value;
                    logMsMonMoney($id, $tName, $value);
                }
                next;
            }
        }
    }
}


#----------------------------------------------------------------------
sub Meteo_disaster {
    my($island) = @_;

    my($name) = islandName($island);
    my($id) = $island->{'id'};
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($landValue2) = $island->{'landValue2'};
    my($landValue3) = $island->{'landValue3'};

    # 隕石判定

    my($x, $y, $landKind, $lv, $lName, $point, $first);
    my($def_flag);

    $first = 1;
    while (!random(2) || $first) {
        $first = 0;

        # スペースデブリが減る
        $HSpaceDebri -= $HSpaceDebri_meteo;

        # 落下
        $x = random($HislandSize);
        $y = random($HislandSize);
        $landKind = $land->[$x][$y];
        $lv = $landValue->[$x][$y];
        $point = "($x, $y)";
        $lName = landName($landKind, $lv,$landValue2->[$x][$y]);

        $def_flag = 0;
        if ( $landKind == $HlandDefence ) {
            my($defLv , $defHP );
            $defHP = 0;
            $defLv = 0;
            $defLv = ($lv & $HDefenceLevelMask);

            if ( $defLv >= 2 ) {
                $def_flag = 1;
                $defHP = $lv >> $HDefenceHP_SHIFT;
                $defHP = $defHP - 3;
                $defHP = 0 if ( $defHP < 0 );
                $landValue->[$x][$y] = 2 + ( $defHP << $HDefenceHP_SHIFT ) ;
            }

            if ( $defHP <= 0 ) {
                logMeteoDef($id, $name, $lName, $point, "し、直撃し");
                $def_flag = 0;
            }

        }else{
            $def_flag = countAround_DefBase($land,$landValue, $x, $y, 19, 1);
        }

        if ($def_flag) {
            logMeteoDef($id, $name, $lName, $point, "しましたが、防衛基地・改に守られ");
            next;

        } elsif (($landKind == $HlandSea) && !$lv){
            # 海ポチャ
            logMeteo($id, $name, $lName, $point, "し");

        } elsif (   ($landKind == $HlandMountain)
                 || ($landKind == $HlandGold)
                 || ($landKind == $HlandShrine)
                 || ($landKind == $HlandOnsen)  ) {
            # 山、金山、時の神殿破壊
            logMeteo($id, $name, $lName, $point, "、<B>$lName</B>は消し飛び");
            $land->[$x][$y] = $HlandWaste;
            $landValue->[$x][$y] = 2;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            next;

        } elsif(($landKind == $HlandSbase) ||
                ($landKind == $HlandSeacity) ||
                ($landKind == $HlandSeatown) ||
                ($landKind == $HlandFune) ||
                ($landKind == $HlandNursery) ||
                ($landKind == $HlandUmishuto) ||
                ($landKind == $HlandFrocity) ||
                ($landKind == $HlandOilCity) ||
                ($landKind == $HlandUmicity) ||
                ($landKind == $HlandOil) ||
                ($landKind == $HlandUmiamu)
                                            ) {
            logMeteo($id, $name, $lName, $point, "、<B>$lName</B>は崩壊し");

        } elsif($landKind == $HlandMonster) {
            logMeteoMonster($id, $name, $lName, $point);

        } elsif(($landKind == $HlandSea) || ($landKind == $HlandIce)) {
            # 浅瀬
            logMeteo($id, $name, $lName, $point, "、海底がえぐられ");

        } else {

            if (random(100) < 20) {
                logMeteo($id, $name, $lName, $point, "、<B>$lName</B>は消し飛び");
                $land->[$x][$y] = $HlandWaste;
                $landValue->[$x][$y] = 2;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                next;

            }else{

                logMeteo($id, $name, $lName, $point, "、一帯が水没し");
            }
        }
        $land->[$x][$y] = $HlandSea;
        $landValue->[$x][$y] = 0;
        $landValue2->[$x][$y] = 0;
        if (random(1000) < 50) {
            $land->[$x][$y] = $HlandMonument;
            $landValue->[$x][$y] = 79;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
        }
    }

}


#----------------------------------------------------------------------
sub BigMissileRoutine {
    my($island) = @_;

    # 巨大ミサイル判定
    while($island->{'bigmissile'}) {
        $island->{'bigmissile'}--;
        my($x, $y, $landKind, $lv, $point);

        # 落下
        $x = random($HislandSize);
        $y = random($HislandSize);
        $landKind = $land->[$x][$y];
        $lv = $landValue->[$x][$y];
        $point = "($x, $y)";

        # メッセージ
        logMonDamage($id, $name, $point);

        # 広域被害ルーチン
        wideDamage($id, $name, $land, $landValue, $x, $y);
    }

}


#----------------------------------------------------------------------
# 洪水
#----------------------------------------------------------------------
sub Flood {
    my ($island) = @_;

    {
        my ($chain) = $island->{'weather_chain'};
        my ($weather) = $island->{'weather'};

        if (   ($weather == $HWeather_Rain)
            && ($chain > 5) ) {

            my ($name) = islandName($island);
            my ($id) = $island->{'id'};
            my ($land) = $island->{'land'};
            my ($landValue) = $island->{'landValue'};
            my ($landValue2) = $island->{'landValue2'};
            my ($landValue3) = $island->{'landValue3'};

            my ($par) = $chain;
            if (random(100) < $par) {

                logOut("${HtagName_}${name}${H_tagName}で大規模な${HtagDisaster_}洪水${H_tagDisaster}が発生！！",$id);

                my ($i, $sx, $sy);
                my ($lk);
                my ($lv, $lv2);
                my ($tar_landname);
                my ($tar_pos);
                for ($i = 0; $i < $HpointNumber; $i++) {
                    $sx = $Hrpx[$i];
                    $sy = $Hrpy[$i];

                    $tar_pos = "($sx, $sy)";

                    if ( !countAround($land, $sx, $sy, 7, $HlandForest) ) {

                        $lk = $land->[$sx][$sy];
                        $lv = $landValue->[$sx][$sy];
                        $lv2 = $landValue2->[$sx][$sy];
                        $tar_landname = landName($lk, $lv, $lv2);


                        if (   ($lk == $HlandSea) && ($lv)      # 浅瀬
                            && (random(100) < 50) ) {

                            logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}洪水${H_tagDisaster}により被害を受けました。");
                            $landValue->[$sx][$sy] = 0;         # 海へ
                            $landValue2->[$sx][$sy] = 0;
                            $landValue3->[$sx][$sy] = 0;
                        }
                        elsif (   ($lk == $HlandSunahama) && (!$lv)     # 砂浜
                               && (random(100) < 50) ) {

                            logDamageAny($id, $name, $tar_landname, $tar_pos, "海の中へ沈みました。");
                            $land->[$sx][$sy] = $HlandSea;
                            $landValue->[$sx][$sy] = 1;
                            $landValue2->[$sx][$sy] = 0;
                            $landValue3->[$sx][$sy] = 0;
                        }
                        elsif (   ($lk == $HlandMinato)
                               && (random(100) < 2) ) {

                            $lv -= random(20)+1;

                            if ($lv < 0) {

                                logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}洪水${H_tagDisaster}により壊滅しました。");
                                $land->[$sx][$sy] = $HlandSea;
                                $landValue->[$sx][$sy] = 1;
                                $landValue2->[$sx][$sy] = 0;
                                $landValue3->[$sx][$sy] = 0;

                            }else{
                                logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}洪水${H_tagDisaster}により被害を受けました。");
                                $landValue->[$sx][$sy] = $lv;
                            }
                        }
                        elsif (   (   ($lk == $HlandMountain)
                                   && ($lv > 0) )
                               && (random(100) < 2)
                                                    ) {

                            $lv -= random(20)+1;

                            if ($lv < 0) {
                                logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}洪水${H_tagDisaster}により壊滅しました。");
                                $landValue->[$sx][$sy] = 0;
                                $landValue2->[$sx][$sy] = 0;
                                $landValue3->[$sx][$sy] = 0;

                            }else{
                                logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}洪水${H_tagDisaster}により被害を受けました。");
                                $landValue->[$sx][$sy] = $lv;
                            }
                        }
                        elsif (   (   ($lk == $HlandTown)
                                   || ($lk == $HlandNewtown)
                                   || ($lk == $HlandBigtown)
                                   || ($lk == $HlandFactory)
                                   || (($lk == $HlandFoodim) && ($lv < 480))
                                   || ($lk == $HlandRizort)
                                   || ($lk == $HlandInaka)
                                                            )
                               && (random(100) < 2) ) {

                            $lv -= random(6)+1;

                            if ($lv < 0) {
                                logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}洪水${H_tagDisaster}により壊滅しました。");
                                $landValue->[$sx][$sy] = 0;
                                $landValue2->[$sx][$sy] = 0;
                                $landValue3->[$sx][$sy] = 0;

                            }else{
                                logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}洪水${H_tagDisaster}により被害を受けました。");
                                $landValue->[$sx][$sy] = $lv;
                            }
                        }
                        elsif (   (   ($lk == $HlandFrocity)
                                   || ($lk == $HlandOilCity)
                                   || ($lk == $HlandUmicity)
                                                            )
                               && (random(100) < 2) ) {

                            $lv -= random(30)+7;

                            if ($lv < 0) {
                                logDamageAny($id, $name, landName($lk, $lv, $lv2), "($sx, $sy)", "${HtagDisaster_}洪水${H_tagDisaster}により壊滅しました。");
                                $land->[$sx][$sy] = $HlandSea;
                                $landValue->[$sx][$sy] = 0;
                                $landValue2->[$sx][$sy] = 0;
                                $landValue3->[$sx][$sy] = 0;

                            }else{
                                logDamageAny($id, $name, landName($lk, $lv, $lv2), "($sx, $sy)", "${HtagDisaster_}洪水${H_tagDisaster}により被害を受けました。");
                                $landValue->[$sx][$sy] = $lv;
                            }
                        }
                    }
                }
            }
        }
    }

}



#----------------------------------------------------------------------
# 噴火判定
#----------------------------------------------------------------------
sub Volcano {
    my($island, $x,$y) = @_;

    my($name) = islandName($island);
    my($id) = $island->{'id'};
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($landValue2) = $island->{'landValue2'};

    {
        my($sx, $sy, $i, $landKind, $lv, $point);

        $landKind = $land->[$x][$y];
        $lv = $landValue->[$x][$y];
        $point = "($x, $y)";

            logEruption($id, $name, landName($landKind, $lv,$landValue2->[$x][$y]), $point);
            $land->[$x][$y] = $HlandMountain;
            $landValue->[$x][$y] = 0;
            if (random(1000) < 100) {
                $land->[$x][$y] = $HlandMonument;
                $landValue->[$x][$y] = 75;          # 地石
                $landValue2->[$x][$y] = 0;
            } elsif (random(1000) < 50) {
                $land->[$x][$y] = $HlandMonument;
                $landValue->[$x][$y] = 78;          # 炎石01
                $landValue2->[$x][$y] = 0;
            }

        for($i = 1; $i < 7; $i++) {
            $sx = $x + $ax[$i];
            $sy = $y + $ay[$i];

            # 行による位置調整
            $sx-- if(!($sy % 2) && ($y % 2));

            if (($sx >= 0) && ($sx < $HislandSize) && ($sy >= 0) && ($sy < $HislandSize)) {
                # 範囲内の場合
                $landKind = $land->[$sx][$sy];
                $lv = $landValue->[$sx][$sy];
                $point = "($sx, $sy)";
                if (   ($landKind == $HlandSea)
                    || ($landKind == $HlandOil)
                    || ($landKind == $HlandFune)
                    || ($landKind == $HlandUmiamu)
                    || ($landKind == $HlandIce)
                    || ($landKind == $HlandFrocity)
                    || ($landKind == $HlandUmishuto)
                    || ($landKind == $HlandSeacity)
                    || ($landKind == $HlandSeatown)
                    || ($landKind == $HlandSbase)
                                                    ) {
                    # 海の場合
                    if(($lv == 1) || ($landKind == $HlandIce)) {
                        # 浅瀬
                        logEruption2($id, $name, landName($landKind, $lv,$landValue2->[$sx][$sy]), $point, "陸地になりました。");
                    } else {
                        logEruption2($id, $name, landName($landKind, $lv,$landValue2->[$sx][$sy]), $point, "海底が隆起、浅瀬になりました。");
                        $land->[$sx][$sy] = $HlandSea;
                        $landValue->[$sx][$sy] = 1;
                        next;
                    }
                } elsif(   ($landKind == $HlandMountain)
                        || ($landKind == $HlandMonster)
                        || ($landKind == $HlandGold)
                        || ($landKind == $HlandShrine)
                        || ($landKind == $HlandOnsen)
                        || ($landKind == $HlandWaste) ) {

                    if (   ($landKind == $HlandWaste)
                        && (!random(5))
                                        ) {
                        $land->[$sx][$sy] = $HlandYougan;
                        $landValue->[$sx][$sy] = 3 + random(10);
                        $landValue2->[$sx][$sy] = 0;
                    }

                    next;
                } else {
                    # それ以外の場合
                    logEruption2($id, $name, landName($landKind, $lv,$landValue2->[$sx][$sy]), $point, "壊滅しました。");
                }

                if (random(1000) < 50) {
                    $land->[$sx][$sy] = $HlandMonument;
                    $landValue->[$sx][$sy] = 75;
                    $landValue2->[$sx][$sy] = 0;
                } elsif (!random(5)) {
                    $land->[$sx][$sy] = $HlandYougan;
                    $landValue->[$sx][$sy] = 3 + random(10);
                    $landValue2->[$sx][$sy] = 0;
                }else{

                    SetWasteLand_Normal($island,$sx,$sy);       # HlandWaste
                }
            }
        }
    }
}


#----------------------------------------------------------------------
# 人工衛星エネルギー減少
#----------------------------------------------------------------------
sub Satellite_Energy {
    my($island) = @_;

    my($name) = islandName($island);
    my($id) = $island->{'id'};

    # 人工衛星エネルギー減少
    my($kind, $i);
    for($i = 1; $i < 7; $i++) {
        $kind = 'eis' . $i;
        if($island->{$kind}) {
            $island->{$kind} -= 1;
            $island->{$kind} -= random(2) if( !random(10) ) ;
            if($island->{$kind} < 1) {
                $island->{$kind} = 0;
                logEiseiEnd($id, $name, $HeiseiName[$i]);
            }
        }
    }
}

#----------------------------------------------------------------------
# 役所の掃除を始める
#----------------------------------------------------------------------
sub Yakusyo_clean {
    my($island) = @_;

    my($name) = islandName($island);
    my($id) = $island->{'id'};
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($landValue2) = $island->{'landValue2'};

    # 役所の掃除を始める
    if ($island->{'yaku'}){
        my($x, $y, $i);
        foreach $i (0..$pointNumber) {

            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            my ($landKind) = $land->[$x][$y];
            my ($lv) = $landValue->[$x][$y];
            my ($lv2) = $landValue2->[$x][$y];
            my ($lName) = landName($landKind, $lv,$lv2);

            my ($work) = 0;

            if ($landKind == $HlandWaste) {         #荒地　役所　イベント

                if ( ( $island->{'yaku'} >= 2)
                    && ($island->{'money'} > $HYakusho_Narasi2)
                    && ($island->{'yaku_work'} & $HYakushoWorkSeiti) ) {

                    $land->[$x][$y] = $HlandPlains;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    $island->{'money'} -= $HYakusho_Narasi2;
                    $work = 1;
                }
            }
            if( ($land->[$x][$y] == $HlandPlains) && ($landValue->[$x][$y] == 0) ) {    #平地 役所

                if (   ( $island->{'yaku'} > 0)
                    && ($island->{'money'} > $HYakusho_Narasi)
                    && ($island->{'yaku_work'} & $HYakushoWorkYotei) ) {

                    $land->[$x][$y] = $HlandPlains;
                    $landValue->[$x][$y] = 1;
                    $landValue2->[$x][$y] = 0;
                    $island->{'money'} -= $HYakusho_Narasi;
                    $work = 2;
                }
            }

            if ( $work == 1 ) {
                logYakusho_Prepare($id, $name, $lName ,"($x, $y)");
            }elsif( $work == 2){
                logYakusho_Plains2($id, $name, $lName ,"($x, $y)");
            }else{
                #なにもしない
            }
        }
    }
}

#----------------------------------------------------------------------
# 賞関係と増加率処理
#----------------------------------------------------------------------
sub doPrize {
    my($number, $island) = @_;

    # 導出値
    my ($name) = islandName($island);
    my ($id) = $island->{'id'};

    # 食料があふれてたら換金
    if($island->{'food'} > $HmaximumFood) {
        my ($amarifood) = int($island->{'food'} - $HmaximumFood);
        my ($salefood) = int(($island->{'food'} - $HmaximumFood) / 10);
        $island->{'money'} += $salefood;
        food_product_Random_consumption($island , $amarifood);
        food_product_overheadcut($island);
        logFoodsute($id , $name ,$amarifood , $salefood);
    }

    # 収入チェック
    $island->{'pika'} = $island->{'money'} - $island->{'oldMoney'};

    # 金があふれてたら切り捨て
    if($island->{'money'} > $HmaximumMoney) {

        my ($over) = $HmaximumMoney - $island->{'money'};

        $island->{'money'} = $HmaximumMoney;

        if (   ($island->{'eisei1'} > 0)
            && ($island->{'tax_income'} != -1)
            && ( $island->{'tax_income'} < ($over)) ) {

            if (random(100) < 5) {

                logZeikin_fuman($id , islandName($island));
            }
        }
    }

    # 同盟関連処理
    if ($HallyNumber) {
        my($gnp) = int($island->{'money'} - $island->{'oldMoney'} + ($island->{'food'} - $island->{'oldFood'})/10);
        foreach (@{$island->{'allyId'}}) {
            ${Hally[$HidToAllyNumber{$_}]->{'ext'}[2]} += $gnp;
        }
    }

    # 各種の値を計算
    estimate($number);

    # 繁栄、災難賞
    my ($pop) = $island->{'pop'};
    my ($damage) = $island->{'oldPop'} - $pop - $island->{'migrate'}; # 移民は災難にいれない
    my ($prize) = $island->{'prize'};
    my ($prize1, $prize2) = split(/\t/, $prize);
    $prize1 =~ /([0-9]*),([0-9]*),(.*)/;
    my ($flags) = $1;
    my ($monsters) = $2;
    my ($turns) = $3;

    $island->{'hamu'} = $island->{'pop'} - $island->{'oldPop'};
    $island->{'monta'} = $island->{'pts'} - $island->{'oldPts'};
    $island->{'old_food'} = $island->{'food'} - $island->{'lastFood'};
    $island->{'old_area'} = $island->{'area'} - $island->{'lastarea'};

    $island->{'gomi'} = $island->{'gomi'} + ($pop);

    $island->{'gomi'} = 0 if ($island->{'gomi'} < 0);
    $island->{'gomi'} = 0 if (!($HislandTurn % 50));

    # 繁栄賞
    if((!($flags & 1)) &&  $pop >= 3000){
        $flags |= 1;
        logPrize($id, $name, $Hprize[1]);

        Sinden_Omaturi($island , 0 , 3001);

        # 神社
        Jinja_Omaturi($island , 0 , 3001);

    } elsif((!($flags & 2)) &&  $pop >= 5000){
        $flags |= 2;
        logPrize($id, $name, $Hprize[2]);

        Sinden_Omaturi($island , 0 , 4001);

        # 神社
        Jinja_Omaturi($island , 0 , 4001);

    } elsif((!($flags & 4)) &&  $pop >= 10000){
        $flags |= 4;
        logPrize($id, $name, $Hprize[3]);

        Sinden_Omaturi($island , 0 , 5001);

        # 神社
        Jinja_Omaturi($island , 0 , 5001);
    }

    # 災難賞
    if((!($flags & 64)) &&  $damage >= 500){
        $flags |= 64;
        logPrize($id, $name, $Hprize[7]);
    } elsif((!($flags & 128)) &&  $damage >= 1000){
        $flags |= 128;
        logPrize($id, $name, $Hprize[8]);
    } elsif((!($flags & 256)) &&  $damage >= 2000){
        $flags |= 256;
        logPrize($id, $name, $Hprize[9]);
    }

    $island->{'prize'} = "$flags,$monsters,$turns\t$prize2";
}


#----------------------------------------------------------------------
# レーザー攻撃
#----------------------------------------------------------------------
sub LazerAttack {
    my($island, $tisland, $x, $y, ,$comName ,$monName) = @_;

    my ($id) = $island->{'id'};
    my ($target) = $tisland->{'id'};
    my ($tLand) = $tisland->{'land'};
    my ($tLandValue) = $tisland->{'landValue'};
    my ($tLandValue2) = $tisland->{'tLandValue2'};

    my ($tL) = $tLand->[$x][$y];
    my ($tLv) = $tLandValue->[$x][$y];
    my ($tLv2) = $tLandValue2->[$x][$y];
    my ($tLname) = landName($tL, $tLv,$tLv2);
    my ($point) = "($x, $y)";
    my ($tPoint) = "($x, $y)";
    my ($name) = islandName($island);
    my ($tName) = islandName($tisland);
    my ($tmKind, $tmName, $tmHp) = monsterSpec($tLv);

    my ($defcnt);
    my ($def_lz);
    $defcnt = 0;
    $def_lz = 0;

    $defcnt = countAround_DefBase($tLand,$tLandValue, $x, $y, 19, 2);

    if ( ($tL == $HlandDefence) ) {
        # 防衛基地に対する攻撃

        my ($deflv , $defHP) = GetDefenceSpec($tLv);
        my ($defLv);

        if ($defLv >= 2) {

            if ($defHP) {
                #HPがある場合のみ防御
                $def_lz = 1;
                $tLandValue->[$x][$y] -= ( 1 << $HDefenceHP_SHIFT) ;
            }
        }

    }elsif ($defcnt > 0){
        # 防衛基地があった
        $def_lz = 1;

        my($i,$sx,$sy);
        # まわりの防衛基地を探す
        for($i = 1; $i < 19; $i++) {
            $sx = $x + $ax[$i];
            $sy = $y + $ay[$i];

            my ($defLv , $defHP) = GetDefenceSpec($tLandValue->[$sx][$sy]);

            if(   ($tLand->[$sx][$sy] == $HlandDefence)
               && ($defLv >= 2)
               && ($defHP > 0)
                                ){

                $tLandValue->[$sx][$sy] = 2 + ( ($defHP-1) << $HDefenceHP_SHIFT);
                last;
            }
        }
    }

    if ( $def_lz == 0 ) {
        if (   ($tL == $HlandSea)
            || ($tL == $HlandWaste)
            || ($tL == $HlandMountain)
            || ($tL == $HlandGold)
            || ($tL == $HlandShrine)
            || ($tL == $HlandSeacity)
            || ($tL == $HlandSeatown)
            || ($tL == $HlandUmishuto)
            || ($tL == $HlandUmiamu)
            || ($tL == $HlandSbase)
                                    ) {
            # 効果のない地形
            logLzr($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "暖かくなりました。");

        } elsif (   ($tL == $HlandYougan)
                                            ) {
            logLzr($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "さらに熱くなりました。");

        } elsif (   ($tL == $HlandOil)
                 || ($tL == $HlandNursery)
                 || ($tL == $HlandUmicity)
                 || ($tL == $HlandOilCity)
                 || ($tL == $HlandFrocity)
                 || ($tL == $HlandIce)
                 || ($tL == $HlandFune)
                                        ) {

            logLzr($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "焼き払われました。");
            SetSeaLand_Normal($tisland,$x,$y);

        } elsif (($tL == $HlandMonster) && ($tmKind == 35)) {      # ひめいのらは無敵

            # 効果のない地形
            logLzr($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "「あつっ！」とびっくりしました。");

        } elsif ($tL == $HlandOnsen) {

            logLzr($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "焼き払われました。");
            SetMountain_Normal($tisland,$x,$y);

        } else {

            logLzr($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "焼き払われました。");
            if ((($tL == $HlandMonster) && (isSeaMonster($tmKind)))) {

                SetSeaLand_Normal($tisland,$x,$y);

            }else{

                SetWasteLand_Normal($tisland,$x,$y);
            }

            if (random(1000) < 100) {
                SetMonument_Normal($tisland,$x,$y,79);
            }
        }

    }else{

        logLzrFail($id, $target, $name, $tName, $comName, $tPoint);
    }
}


#----------------------------------------------------------------------
# 海系の土地
#----------------------------------------------------------------------
sub is_SeaGroup_woSea {
    my($landKind) = @_;

    my ($ret) = 0;
    if ($landKind == $HlandSea) {

    }else{
        $ret = is_SeaGroup($landKind);
    }

    return ($ret);
}


#----------------------------------------------------------------------
sub is_SeaGroup {

    my ($landKind) = $_;

    if (   ($landKind == $HlandSea)
        || ($landKind == $HlandSbase)
        || ($landKind == $HlandSeatown)
        || ($landKind == $HlandSeacity)
        || ($landKind == $HlandUmicity)
        || ($landKind == $HlandOil)
        || ($landKind == $HlandOilCity)
        || ($landKind == $HlandUmishuto)
        || ($landKind == $HlandFune)
        || ($landKind == $HlandFrocity)
        || ($landKind == $HlandUmiamu)
        || ($landKind == $HlandIce)
                                     ) {
        return (1);
    }

    return (0);
}


#----------------------------------------------------------------------
# 広域被害ルーチン
#----------------------------------------------------------------------
sub wideDamage {
    my($id, $name, $land, $landValue, $x, $y) = @_;

    my($sx, $sy, $i, $landKind, $landName, $lv, $lv2, $point);

    my ($island) = $Hislands[$HidToNumber{$id}];

    my ($landValue2) = $island->{'landValue2'};

    for($i = 0; $i < 19; $i++) {
        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # 行による位置調整
        $sx-- if(!($sy % 2) && ($y % 2));
        # 範囲外判定
        next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

        $landKind = $land->[$sx][$sy];
        $lv  = $landValue->[$sx][$sy];
        $lv2 = $landValue2->[$sx][$sy];
        $landName = landName($landKind, $lv,$lv2);
        $point = "($sx, $sy)";

        # 範囲による分岐
        if ($i < 7) {
            # 中心、および1ヘックス
            if ($landKind == $HlandSea) {
                $landValue->[$sx][$sy] = 0;
                $landValue2->[$sx][$sy] = 0;
                next;
            } elsif(is_SeaGroup_woSea($landKind)) {
                logDamageAny($id, $name, $landName, $point, "跡形もなくなりました。");
                $land->[$sx][$sy] = $HlandSea;
                $landValue->[$sx][$sy] = 0;

            } else {
                if ($landKind == $HlandMonster) {
                    my($mKind, $mName, $mHp) = monsterSpec($lv);
                    next if((($mKind == 20) && !$i) || (($mKind == 21) && !$i));
                    logWideDamageMonsterSea($id, $name, $landName, $point);
                } else {
                    logDamageAny($id, $name, $landName, $point, "<B>水没</B>しました。");
                }
                $land->[$sx][$sy] = $HlandSea;
                $landValue2->[$sx][$sy] = 0;
                if(!$i) {
                    # 海
                    $landValue->[$sx][$sy] = 0;
                } else {
                    # 浅瀬
                    $landValue->[$sx][$sy] = 1;
                }
            }
        } else {
            # 2ヘックス
            if( ($landKind == $HlandWaste) ||
                ($landKind == $HlandMountain) ||
                ($landKind == $HlandGold) ||
                ($landKind == $HlandShrine) ||
                ($landKind == $HlandSea) ||
                ($landKind == $HlandSbase) ||
                ($landKind == $HlandSeacity) ||
                ($landKind == $HlandSeatown) ||
                ($landKind == $HlandUmishuto) ||
                ($landKind == $HlandOil) ||
                ($landKind == $HlandUmiamu)) {
                # ダメージのない地形
                next;
            } elsif(   ($landKind == $HlandOnsen)
                                                    ) {
                logDamageAny($id, $name, $landName, $point, "消し飛びました。");
                SetMountain_Normal($island,$sx,$sy);

            } elsif(   ($landKind == $HlandIce)
                    || ($landKind == $HlandFune)
                    || ($landKind == $HlandFrocity)
                    || ($landKind == $HlandUmicity)
                    || ($landKind == $HlandOilCity)
                                                    ) {
                logDamageAny($id, $name, $landName, $point, "消し飛びました。");
                $land->[$sx][$sy] = $HlandSea;
                $landValue->[$sx][$sy] = 0;
                $landValue2->[$sx][$sy] = 0;

            } elsif($landKind == $HlandMonster) {
                logDamageAny($id, $name, $landName, $point, "消し飛びました。");
                SetWasteLand_Normal($island,$sx,$sy);
            } else {
                logDamageAny($id, $name, $landName, $point, "一瞬にして<B>荒地</B>と化しました。");
                SetWasteLand_Normal($island,$sx,$sy);
            }
        }
    }
}


#----------------------------------------------------------------------
# 広域被害ルーチン・ミニ2
#----------------------------------------------------------------------
sub wideDamageli2 {
    my ($target, $tx, $ty) = @_;

    my ($tName, $tLand, $tLandValue, $tLandValue2, $tLandValue3);

    my ($tName) = islandName($target);

    $tLand       = $target->{'land'};
    $tLandValue  = $target->{'landValue'};
    $tLandValue2 = $target->{'landValue2'};
    $tLandValue3 = $target->{'landValue3'};

    my ($sx, $sy, $i, $tL, $landName, $tLv, $tLv2, $point);

    for($i = 0; $i < 19; $i++) {
        $sx = $tx + $ax[$i];
        $sy = $ty + $ay[$i];

        # 行による位置調整
        $sx-- if(!($sy % 2) && ($ty % 2));
        # 範囲外判定
        next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

        $tL = $tLand->[$sx][$sy];
        $tLv = $tLandValue->[$sx][$sy];
        $tLv2 = $tLandValue2->[$sx][$sy];
        $landName = landName($tL, $tLv, $tLv2);
        $point = "($sx, $sy)";

        if (   ($tL == $HlandSea)
            || ($tL == $HlandWaste)
            || ($tL == $HlandSeacity)
            || ($tL == $HlandSeatown)
            || ($tL == $HlandUmishuto)
            || ($tL == $HlandUmiamu)
            || ($tL == $HlandSbase) ) {
            next;

        } elsif(   ($tL == $HlandFune)
                || ($tL == $HlandFrocity)
                || ($tL == $HlandUmicity)
                || ($tL == $HlandOilCity)
                || ($tL == $HlandOil) ) {
            logDamageAny($target, $tName, $landName, $point, "消し飛びました。");
            SetSeaLand_Normal($target,$sx,$sy);

        } elsif (   ($tL == $HlandIce)
                 || ($tL == $HlandSeki)
                 || ($tL == $HlandNursery) ) {
            logDamageAny($target, $tName, $landName, $point, "消し飛びました。");
            SetSeaShallowLand($target,$sx,$sy);

        }
        elsif ($tL == $HlandMonster) {

            my ($mKind, $mName, $mHp) = monsterSpec($lv);
            logDamageAny($target, $tName, $landName, $point, "消し飛びました。");
            if (isSeaMonster($mKind)) {
                SetSeaLand_Normal($target,$sx,$sy);
            }
            else {
                SetWasteLand_Normal($target,$sx,$sy);
            }
        }
        else {
            logDamageAny($target, $tName, $landName, $point, "一瞬にして<B>荒地</B>と化しました。");
            $tLand->[$sx][$sy] = $HlandWaste;
            SetWasteLand_Normal($target,$sx,$sy);
        }
    }
}


#----------------------------------------------------------------------
# 広域被害ルーチン・ミニ
#----------------------------------------------------------------------
sub wideDamageli {

    my ($target, $tName, $tLand, $tLandValue, $tLandValue2, $tx, $ty) = @_;

    my ($sx, $sy, $i, $tL, $landName, $tLv, $tLv2, $point);

    for($i = 0; $i < 19; $i++) {
        $sx = $tx + $ax[$i];
        $sy = $ty + $ay[$i];

        # 行による位置調整
        $sx-- if(!($sy % 2) && ($ty % 2));
        # 範囲外判定
        next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

        $tL = $tLand->[$sx][$sy];
        $tLv = $tLandValue->[$sx][$sy];
        $tLv2 = $tLandValue2->[$sx][$sy];
        $landName = landName($tL, $tLv, $tLv2);
        $point = "($sx, $sy)";

        if (   ($tL == $HlandSea)
            || ($tL == $HlandWaste)
            || ($tL == $HlandSeacity)
            || ($tL == $HlandSeatown)
            || ($tL == $HlandIce)
            || ($tL == $HlandUmishuto)
            || ($tL == $HlandUmiamu)
            || ($tL == $HlandSbase) ) {
            next;

        } elsif(   ($tL == $HlandFune)
                || ($tL == $HlandFrocity)
                || ($tL == $HlandUmicity)
                || ($tL == $HlandOilCity)
                || ($tL == $HlandOil)
                                            ) {
            logDamageAny($target, $tName, $landName, $point, "消し飛びました。");
            $tLand->[$sx][$sy] = $HlandSea;
            $tLandValue->[$sx][$sy] = 0;
            $tLandValue2->[$sx][$sy] = 0;

        } elsif($tL == $HlandMonster) {
            logDamageAny($target, $tName, $landName, $point, "消し飛びました。");
            $tLand->[$sx][$sy] = $HlandWaste;
            $tLandValue->[$sx][$sy] = 0;
            $tLandValue2->[$sx][$sy] = 0;

        } else {
            logDamageAny($target, $tName, $landName, $point, "一瞬にして<B>荒地</B>と化しました。");
            $tLand->[$sx][$sy] = $HlandWaste;
            $tLandValue->[$sx][$sy] = 0;
            $tLandValue2->[$sx][$sy] = 0;
        }
    }
}

#----------------------------------------------------------------------
# 海底の建物
#----------------------------------------------------------------------
sub isUnderSea {
    my ($land) = @_;

    if (   (0)
        || ($land == $HlandSbase)
        || ($land == $HlandSeacity)
        || ($land == $HlandUmiamu)
        || ($land == $HlandSeatown)
        || ($land == $HlandUmishuto)
                                        ) {
        return 1;
    }

    return 0;
}


#----------------------------------------------------------------------
# 地形の呼び方
#----------------------------------------------------------------------
sub landName2 {
    my ($island, $x, $y) = @_;

    my ($land) = $island->{'land'};
    my ($land_kind) = $land->[$x][$y];

    my ($landValue) = $island->{'landValue'};
    my ($lv) = $landValue->[$x][$y];

    my ($landValue2) = $island->{'landValue2'};
    my ($lv2) = $landValue2->[$x][$y];

    my ($landValue3) = $island->{'landValue3'};
    my ($lv3) = $landValue3->[$x][$y];

    return landName($land , $lv, $lv2 , $lv3);
}

sub landName {
    my ($land, $lv, $lv2) = @_;

    if($land == $HlandSea) {
        if($lv == 1) {
            return '浅瀬';
        } else {
            return '海';
        }
    } elsif($land == $HlandIce) {
        if($lv > 0) {
            return '天然スケート場';
        } else {
            return '氷河';
        }
    } elsif($land == $HlandWaste) {
        return '荒地';
    } elsif($land == $HlandInaka) {
        return 'いなか';
    } elsif($land == $HlandPlains) {
        return '平地';
    } elsif($land == $HlandTown) {
        if($lv < 30) {
            return '村';
        } elsif($lv < 100) {
            return '町';
        } else {
            return '都市';
        }
    } elsif($land == $HlandProcity) {
        return '防災都市';
    } elsif($land == $HlandNewtown) {
        return 'ニュータウン';
    } elsif($land == $HlandBigtown) {
        return '現代都市';
    } elsif($land == $HlandBettown) {
        return '輝ける都市';
    } elsif($land == $HlandSeatown) {
        return '海底新都市';
    } elsif($land == $HlandRizort) {
        return 'リゾート地';
    } elsif($land == $HlandBigRizort) {
        return '臨海リゾートホテル';
    } elsif($land == $HlandShuto) {
        return '首都';
    } elsif($land == $HlandUmishuto) {
        return '海底首都';
    } elsif($land == $HlandForest) {
        return '森';
    } elsif($land == $HlandFarm) {
        return '農場';
    } elsif($land == $HlandFoodim) {
        if($lv < 480) {
            return '食物研究所';
        } else {
            return '防災型食物研究所';
        }
    } elsif($land == $HlandFarmchi) {
        return '養鶏場';
    } elsif($land == $HlandFarmpic) {
        return '養豚場';
    } elsif($land == $HlandFarmcow) {
        return '牧場';

    } elsif($land == $HlandCollege) {
        if($lv == 0) {
            return '農業大学';
        } elsif($lv == 1) {
            return '工業大学';
        } elsif($lv == 2) {
            return '総合大学';
        } elsif($lv == 3) {
            return '軍事大学';
        } elsif($lv == 4) {
            return '生物大学(待機中)';
        } elsif($lv == 98) {
            return '生物大学(待機中)';
        } elsif($lv == 96) {
            return '生物大学(出禁中)';
        } elsif($lv == 97) {
            return '生物大学(出禁中)';
        } elsif($lv == 99) {
            return '生物大学(出動中)';
        } else {
            return '気象大学';
        }

    } elsif($land == $HlandFactory) {
        return '工場';
    } elsif($land == $HlandHTFactory) {
        return 'ハイテク多国籍企業';
    } elsif($land == $HlandSHTF) {
        return 'ハイテク多国籍企業・改';
    } elsif($land == $HlandBase) {
        return 'ミサイル基地';
    } elsif($land == $HlandDefence) {
        if($lv == 1) {
            return '防衛施設・改';
        } else {
            return '防衛施設';
        }
    } elsif($land == $HlandMountain) {
        if($lv) {
            return '採掘場';
        } else {
            return '山';
        }
    } elsif($land == $HlandGold) {
        return '金山';
    } elsif($land == $HlandOnsen) {
        return '温泉街';
    } elsif($land == $HlandMonster) {
        my($name) = (monsterSpec($lv))[1];
        return $name;
    } elsif($land == $HlandSbase) {
        return '海底基地';
    } elsif($land == $HlandSeacity) {
        return '海底都市';
    } elsif($land == $HlandOil) {
        return '海底油田';
    } elsif($land == $HlandEgg) {
        return 'タマゴ';
    } elsif($land == $HlandMonument) {
        return $HmonumentName[$lv];
    } elsif($land == $HlandHaribote) {
        return 'ハリボテ';
    } elsif($land == $HlandTrain) {
        return '線路';
    } elsif($land == $HlandPark) {
        return '遊園地';
    } elsif($land == $HlandMinato) {
        return '港町';
    } elsif($land == $HlandFune) {
        return $HfuneName[$lv];
    } elsif($land == $HlandFrocity) {
        return '海上都市';
    } elsif($land == $HlandBeachPark) {
        return '海水浴場';
    } elsif($land == $HlandSunahama) {
        if($lv > 0) {
            return '砂丘';
        }else{
            return '砂浜';
        }
    } elsif($land == $HlandMine) {
        return '地雷';
    } elsif($land == $HlandNursery) {
        return '養殖場';
    } elsif($land == $HlandKyujo) {
        return '野球場';
    } elsif($land == $HlandKyujokai) {
        return '多目的スタジアム';
    } elsif($land == $HlandUmiamu) {
        return '海あみゅ';
    } elsif($land == $HlandSeki) {
        return '関所';
    } elsif($land == $HlandRottenSea) {
        return '腐海';
    } elsif($land == $HlandUmicity) {
        return '海都市';
    } elsif($land == $HlandOilCity) {
        return '油田都市';
    } elsif($land == $HlandYakusho) {
        return '島役所';
    } elsif($land == $HlandInoraLand) {
        return 'いのらランド';
    } elsif($land == $HlandYougan) {
        return '溶岩地帯';
    } elsif($land == $HlandShrine) {
        if($lv) {
            return "時の神殿(ターン${lv})";
        } else {
            return '時の神殿';
        }
    } elsif($land == $HlandHouse) {
        if($lv == 0) {
            return '小屋';
        } elsif($lv == 1) {
            return '簡易住宅';
        } elsif($lv == 2) {
            return '住宅';
        } elsif($lv == 3) {
            return '高級住宅';
        } elsif($lv == 4) {
            return '豪邸';
        } elsif($lv == 5) {
            return '大豪邸';
        } elsif($lv == 6) {
            return '高級豪邸';
        } elsif($lv == 7) {
            return '城';
        } elsif($lv == 8) {
            return '巨城';
        } else {
            return '黄金城';
        }
    } elsif($land == $HlandBigFood) {
        my($Foodkind) = $lv >> $Food_Kind_Shift;
        my($FoodName) = $BigFoodName[$Foodkind];

        return $FoodName;
    } elsif($land == $HlandRocket) {
        return 'ロケット';
    } elsif($land == $HlandZoo) {
        return '動物園';
    } elsif($land == $HlandStation) {
        return '駅';
    } elsif($land == $HlandOmamori) {
        return 'おまもり';
    } elsif($land == $HlandFiredept) {
        return '消防署';
    } elsif($land == $HlandKatorikun) {
        return '豚の香取くん';
    }
}


#----------------------------------------------------------------------
# 人口その他の値を算出
#----------------------------------------------------------------------
sub estimate {
    my ($number) = $_[0];

    my ($island);
    $island = $Hislands[$number];

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};

    my ($pop, $area, $farm, $factory, $mountain)
     = (0, 0, 0, 0, 0, 0);
    my  ($monslive, $monslivetype, $hmonslivetype, $missiles)
      = (0, 0, 0, 0);
    my  ($kei, $rena, $fore, $tare, $zipro, $leje)
      = (0, 0, 0, 0, 0, 0);
    my  ($oil, $bas, $kyu, $amu, $par, $fim, $rot, $sci, $sba, $pro, $kin, $shr, $nto, $m26, $m27, $m17, $c21)
      = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    my  ($c11, $c13, $c28, $co0, $co1, $co2, $co3, $co4, $co5, $co99, $hou, $shu, $sin, $jin)
      = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    my  ($m74, $m75, $m76, $m77, $m78, $m79, $m84, $m93, $ky2, $htf, $m95)
      = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    my (@monspnt);
    my ($shtf) = (0);           # ハイテク改
    my ($factoryHT) = 0;
    my ($yaku) = (0);
    my ($effect) = (0);
    my ($inoralandnum) = (0);   # いのらランド
    my ($train) = (0);          # 線路の数
    my ($zoocnt) = 0;              # 動物園
    my ($zoo_capacity) = 0;
    my ($forest_area) = 0;
    my ($lumber_area) = 0;
    my ($gomi_herasu) = 0;
    my ($park_work) = 0;
    my ($kome_work , $nazoniku_work , $yasai_work , $seafood_work)
        = (0,0,0,0);
    my ($kudamono_work , $sio_work)
        = (0,0);
    my ($hot) = 0;
    my ($mwork , $hwork , $lwork) = (0,0,0);
    my ($sea_build) = 0;
    my ($sightsee) = 0;

    my ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
    $tet = 0;
    # 数える
    my ($i, $x, $y, $kind, $value,$value2);
    $island->{'BF_Flag'} = 0;           # 回避のため、毎回BFを解除しておく 
    $island->{'stadiumnum'} = 0;
    $island->{'defcnt'} = 0 ;
    $island->{'omamori'} = 0 ;
    $island->{'firedept'} = 0;
    $island->{'BF_Missile'} = 0;
    $island->{'yaku_work'} &= 0xFF ^ $HYakushoWorkExist ;

    my (@foodkind);

    foreach $i (0..$pointNumber) {
        $x = $Hrpx[$i];
        $y = $Hrpy[$i];
        $kind = $land->[$x][$y];
        $value2 = $landValue2->[$x][$y];
        $value = $landValue->[$x][$y];
        my($mKind, $mName, $mHp) = monsterSpec($value);

        if(   ($kind != $HlandSea)
           && ($kind != $HlandSbase)
           && ($kind != $HlandIce)
           && ($kind != $HlandFrocity)
           && ($kind != $HlandFune)
           && ($kind != $HlandNursery)
           && ($kind != $HlandUmicity)
           && ($kind != $HlandUmiamu)
           && ($kind != $HlandOilCity)
           && ($kind != $HlandSeacity)
           && ($kind != $HlandSeatown)
           && ($kind != $HlandUmishuto)
           && ($kind != $HlandOil) ){

            $yaku = $value if ($kind == $HlandYakusho);

            if ($kind == $HlandYakusho){
                $island->{'yaku_work'} |= $HYakushoWorkExist;
            }

            if (($kind == $HlandTown) ||
                ($kind == $HlandProcity) ||
                ($kind == $HlandMinato)) {
                # 町
                $area++;
                $pop += $value;
                $pro++ if($kind == $HlandProcity);

            } elsif (   ($kind == $HlandFarm)
                     || ($kind == $HlandFoodim)) {
                # 農場
                $area++;
                $farm += $value;
                $fim++ if(($kind == $HlandFoodim) && ($value < 480));
                if($kind == $HlandFoodim) {
                    $nazoniku_work += $value;
                    $foodkind[5] = 1;
                }

                if (($kind == $HlandFarm)){
                    if($value2 == 1){
                        $kudamono_work += $value;
                        $foodkind[9] = 1;

                    } elsif($value2 == 2) {
                        $sio_work += $value;
                        $foodkind[10] = 1;

                    }else{
                        $kome_work += $value;
                        $foodkind[1] = 1;
                    }
                }

            } elsif($kind == $HlandInaka) {
                # いなか
                $area++;
                $pop += $value;
                my($fm) = int($value / 10) + 1 ;
                $farm += $fm;
                $yasai_work += $fm;
                $foodkind[0] = 1;


            } elsif($kind == $HlandFarmchi) {
                # 養鶏場
                $area++;
                $tare += $value;
                $factory += int($value/100)+1;
                $foodkind[2] = 1;

            } elsif($kind == $HlandFarmpic) {
                # 養豚場
                $area++;
                $zipro += $value;
                $factory += int($value/80)+1;
                $foodkind[3] = 1;

            } elsif($kind == $HlandFarmcow) {
                # 牧場
                $area++;
                $leje += $value;
                $factory += int($value/50)+1;
                $foodkind[4] = 1;

            } elsif(   ($kind == $HlandFactory)
                    || ($kind == $HlandHTFactory) ) {
                # 工場
                $area++;
                $factory += $value;
                $htf++  if ($kind == $HlandHTFactory);

            } elsif ($kind == $HlandPark) {
                $area++;
                $par++;
                $park_work += $value;

            } elsif ($kind == $HlandSHTF) {
                $area++;
                $factoryHT += $value;
                $shtf++

            } elsif(($kind == $HlandMountain) ||
                    ($kind == $HlandGold)) {
                # 山、金山
                $area++;
                $mountain += $value;
                $kin++ if($kind == $HlandGold);

            } elsif($kind == $HlandForest) {
                # 森
                $area++;
                $forest_area++;
                $lumber_area++;
                $fore += $value;

            } elsif($kind == $HlandNewtown) {
                # ニュータウン
                $area++;
                $pop += $value;
                my ($nwork) =  int($value/15);
                $factory += $nwork;
                $nto++; # ニュータウン

            } elsif($kind == $HlandBigtown) {
                # 現代都市
                $area++;
                $pop += $value;
                $mwork =  int($value/20);
                $lwork =  int($value/30);
                $factory += $mwork;
                $farm += $lwork;
                $yasai_work += $lwork;
                $foodkind[0] = 1;

            } elsif($kind == $HlandDefence) {
                $area++;
                $island->{'defcnt'} ++ ;

            } elsif($kind == $HlandBettown) {
                # 輝ける都市
                $area++;
                $pop += $value;

            } elsif($kind == $HlandRizort) {
                # リゾート地
                $area++;
                $pop += $value;

            } elsif($kind == $HlandBigRizort) {
                # リゾート地
                $area++;
                $pop += $value;

            } elsif($kind == $HlandOnsen) {
                $area++;
                $pop += $value;
                $hot++;

            } elsif($kind == $HlandHouse) {
                $area++;
                $hou++;

            } elsif($kind == $HlandShuto) {
                $area++;
                $pop += $value;
                $shu++;

            } elsif($kind == $HlandBase) {
                # 基地
                $area++;
                $bas += $value;
                $rena += $value;
                $missiles += expToLevel($kind, $value);

            } elsif( ($kind == $HlandRocket) ) {
                $area++;
                $m17++;

            } elsif( ($kind == $HlandKatorikun) ) {
                $area++;

            } elsif( ($kind == $HlandMonument) ) {
                $area++;
                $kei++;

                if(0) {

                } elsif($value == 26) {
                    $sin++;
                } elsif($value == 27) {
                    $jin++;

                } elsif($value == 42) {
                    # 駅
                    $land->[$x][$y] = $HlandStation;
                    $landValue->[$x][$y] = 0;

                } elsif($value == 86) {
                    $m26++;
                } elsif($value == 87) {
                    $m27++;
                } elsif($value == 70) {     #gate
                    $island->{'BF_Flag'} = $HBF_MONSTER_HOUSE;
                    food_product_plus($island , 'yasai' ,500000);

                } elsif($value == 71) {     #gate
                    food_product_plus($island , 'yasai' ,500000);
                    $island->{'money'} = 2000000;
                    $pop++;
                    $island->{'trade_max'} = 1;

                } elsif($value == 74) {
                    $m74++;

                } elsif($value == 75) {
                    $m75++;
                } elsif($value == 76) {
                    $m76++;
                } elsif($value == 77) {
                    $m77++;
                } elsif($value == 78) {
                    $m78++;
                } elsif($value == 79) {
                    $m79++;
                } elsif($value == 84) {
                    $m84++;
                } elsif($value == 93) {
                    $m93++;

                } elsif($value == 95) {
                    $m95++;
                    $oil++;
                    $area--;    #海なので、++を取り消す

                } elsif($value == 80) {
                    # ここで置き換え
                    $land->[$x][$y] = $HlandEgg;
                    $landValue->[$x][$y] = 0;
                } elsif($value == 81) {
                    # ここで置き換え
                    $land->[$x][$y] = $HlandEgg;
                    $landValue->[$x][$y] = 1;
                } elsif($value == 82) {
                    # ここで置き換え
                    $land->[$x][$y] = $HlandEgg;
                    $landValue->[$x][$y] = 2;
                } elsif($value == 83) {
                    # ここで置き換え
                    $land->[$x][$y] = $HlandEgg;
                    $landValue->[$x][$y] = 3;

                } elsif($value == 28) {
                    # ここで置き換え
                    $landValue->[$x][$y] = 13;

                } elsif($value == 17) {
                    $m17++;
                    # ここで置き換え
                    $land->[$x][$y] = $HlandRocket;
                    $landValue->[$x][$y] = 0;
                }

            } elsif($kind == $HlandCollege) {
                $area++;
                if ($value2 == 0) {
                    if($value == 0) {
                        $co0++;             #農業大学
                    } elsif($value == 1) {
                        $co1++;             #工業大学
                    } elsif($value == 2) {
                        $co0++;             #総合大学
                        $co1++;
                        $co2++;
                    } elsif($value == 3) {
                        $co3++;             #軍事大学
                    } elsif($value == 5) {
                        $co5++;             # 気象大学
                    }

                }

                # 生物大学(空き)
                if ($value == 99) {
                    $co99++;
                } elsif(($value == 98) || ($value == 97)){
                        $co4++;
                        $tet++;

                } elsif(($value == 4) || ($value == 96)) {
                        $co4++;             # 生物大学
                }

            } elsif ($kind == $HlandMonster) {
                $area++;
                my ($special) = $HmonsterSpecial[$mKind];
                if ($mKind == 11) {
                    $c11++;
                } elsif($mKind == 13) {
                    $c13++;
                } elsif($mKind == 21) {
                    $c21++;
                } elsif($mKind == 28) {
                    $c28++;
                } elsif($mKind == 30) {
                    $c28++;
                    $tet++;
                }
                if ($special == 17) {
                    $effect |= $g_Island_Chaff;
                }
                if ($special == 19) {
                    $effect |= $g_Island_Retro;
                }

                $monslive++;
                push(@monspnt, { x => $x, y => $y });
                $monslivetype = $mKind;

            } elsif($kind == $HlandKyujokai) {
                $area++;
                $kyu++;
                $ky2++;
                $island->{'stadiumnum'}++;

            } elsif($kind == $HlandKyujo) {
                $area++;
                $kyu++;

            } elsif($kind == $HlandRottenSea) {
                $area++;
                $rot++;

            } elsif($kind == $HlandOmamori) {
                $area++;
                $island->{'omamori'} = 1;

            } elsif($kind == $HlandYougan) {
                $area++;
            } elsif($kind == $HlandFiredept) {
                $area++;
                $island->{'firedept'}++;

            } elsif($kind == $HlandShrine) {
                $area++;
                $shr++;

            } elsif($kind == $HlandInoraLand) {
                $area++;
                $inoralandnum++;
                $park_work += $value;

            } elsif($kind == $HlandZoo) {
                $area++;
                $zoocnt++;
                $zoo_capacity += $value;

            }else{
                $area++;
            }

        } elsif($kind == $HlandNursery) {
            # 養殖場は農場の一種
            $farm += $value;
            $seafood_work += $value;
            $foodkind[6] = 1;

        } elsif($kind == $HlandUmicity) {
            # 海都市
            $pop += $value;
            $mwork =  int($value/30);
            $hwork =  int($value/30);

            $factoryHT += $hwork;
            $factory += $mwork;
            $sea_build++;

        } elsif($kind == $HlandOilCity) {
            # 油田都市
            $pop += $value;
            $mwork =  int($value/40);
            $oil++;
            $factory += $mwork;
            $sea_build++;

        } elsif($kind == $HlandUmiamu) {
            # 海あみゅ
            $amu++;
            $park_work += $value;
            $sea_build++;

        } elsif($kind == $HlandIce) {
            # 規模なし

        } elsif($kind == $HlandSeacity) {
            # 海底都市
            $pop += $value;
            $sci++;

        } elsif ($kind == $HlandFrocity) {
            $pro++;
            $pop += $value;

        } elsif ($kind == $HlandUmishuto) {
            $pop += $value;
            $shu++;
            $sea_build++;

        } elsif ($kind == $HlandTrain) {
            $train++;

        } elsif ($kind == $HlandBigFood) {
            $foodkind[8] = 1;

        } elsif($kind == $HlandSeatown) {
            # 海底新都市
            $pop += $value;
            my ($owork) =  int($value/40);
            $factory += $owork;
            $farm += $owork;
            $yasai_work += $owork;
            $sci += 2;
            $foodkind[0] = 1;
            $sea_build++;

        } elsif($kind == $HlandSbase) {
            # 海底基地
            $bas += $value;
            $rena += $value;
            $sba++;
            $missiles += expToLevel($kind, $value);
            $sea_build++;

        } elsif($kind == $HlandOil) {
            $oil++;
            $sea_build++;

        } elsif($kind == $HlandFune) {
            $foodkind[7] = 1 if ($HfuneFood[$value]);
            #$sightsee++;
        }
    }

    # 遊園地類の規模を商業に追加
    $factory += $park_work;

    # 代入
    $island->{'pop'} = $pop;
    $island->{'area'} = $area;
    $island->{'farm'} = $farm;
    $island->{'factory'} = $factory;
    $island->{'park_work'} = $park_work;
    $island->{'factoryHT'} = $factoryHT;
    $island->{'mountain'} = $mountain;
    $island->{'yaku'}      = $yaku;
    $island->{'oil'} = $oil;
    $island->{'bas'} = $bas;
    $island->{'kyu'} = $kyu;
    $island->{'ky2'} = $ky2;
    $island->{'amu'} = $amu;
    $island->{'par'} = $par;
    $island->{'fim'} = $fim;
    $island->{'rot'} = $rot;
    $island->{'sci'} = $sci;
    $island->{'sba'} = $sba;
    $island->{'pro'} = $pro;
    $island->{'kin'} = $kin;
    $island->{'shr'} = $shr;
    $island->{'nto'} = $nto;
    $island->{'m26'} = $m26;
    $island->{'m27'} = $m27;
    $island->{'m17'} = $m17;
    $island->{'c11'} = $c11;
    $island->{'c13'} = $c13;
    $island->{'c21'} = $c21;
    $island->{'c28'} = $c28;
    $island->{'co0'} = $co0;
    $island->{'co1'} = $co1;
    $island->{'co2'} = $co2;
    $island->{'co3'} = $co3;
    $island->{'co4'} = $co4;
    $island->{'co5'} = $co5;
    $island->{'co99'} = $co99;
    $island->{'tet'} = $tet;
    $island->{'hot'} = $hot;
    $island->{'hou'} = $hou;
    $island->{'shu'} = $shu;
    $island->{'sin'} = $sin;
    $island->{'jin'} = $jin;
    $island->{'m74'} = $m74;
    $island->{'m75'} = $m75;
    $island->{'m76'} = $m76;
    $island->{'m77'} = $m77;
    $island->{'m78'} = $m78;
    $island->{'m79'} = $m79;
    $island->{'m84'} = $m84;
    $island->{'m93'} = $m93;
    $island->{'htf'} = $htf;        # ハイテク
    $island->{'shtf'} = $shtf;
    $island->{'inoraland'} = $inoralandnum;
    $island->{'effect'} = $effect;
    $island->{'train'} = $train;
    $island->{'zoo_cnt'} = $zoocnt;
    $island->{'zoo_capacity'} = $zoo_capacity;
    $island->{'gomi_herasu'} = 0;

    $island->{'kome_work'} = $kome_work;
    $island->{'seafood_work'} = $seafood_work;
    $island->{'nazoniku_work'} = $nazoniku_work;
    $island->{'yasai_work'} = $yasai_work;

    $island->{'kudamono_work'} = $kudamono_work;
    $island->{'sio_work'} = $sio_work;
    $island->{'sea_build'} = $sea_build;

    # 島主の家判定
    $island->{'eisei1'} = 0 if(!$hou);

    # 首都判定
    if(!$shu) {
        $island->{'shutomessage'} = 555;
    } elsif($island->{'shutomessage'} == 555) {
        $island->{'shutomessage'} = '';
    }

    # 通算観光者
    $island->{'eisei2'} = 0 if($island->{'eisei2'} < 0);

    my($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = map { int($_) } split(/,/, $island->{'eisei4'});
    $kachiten = $stwin*3 + $stdrow;
    $island->{'kachiten'} = $kachiten;

    if(!$ky2) {
#       $island->{'eisei4'} = "0,0,0,0,0,0,0,0,0,0,0";
        $island->{'eisei4'} = "0,0,0,0,0,0,$stwint,$stdrowt,$stloset,$styusho,0";
    } else {
        $island->{'eisei4'} = "$sto,$std,$stk,$stwin,$stdrow,$stlose,$stwint,$stdrowt,$stloset,$styusho,$stshoka";
    }

    $island->{'monsterlive'} = $monslive; # 怪獣出現数
    $island->{'monsterlivetype'} = $monslivetype; # 怪獣出現種類
    $island->{'hmonsterlivetype'} = $hmonslivetype; # 怪獣出現種類
    $island->{'monspnt'} = \@monspnt; # 怪獣出現座標
    $island->{'missiles'} = $missiles; # ミサイル発射可能数

    $island->{'kei'} = $kei;
    $island->{'rena'} = $rena + $co2*100 + $co3*500 + $msexe;
    $island->{'fore'} = $fore;
    $island->{'tare'} = $tare;
    $island->{'zipro'} = $zipro;
    $island->{'leje'} = $leje;
    $island->{'forest_area'} = $forest_area;
    $island->{'lumber_area'} = $lumber_area;

    # マスコット判定
    if(!$co4 && !$co99 && !$c28) {
        $island->{'eisei5'} = "0,0,0,0,0,0,0";
    } elsif($co4 && !$mshp) {
        $island->{'eisei5'} = "3,5,5,5,0,0,0";
    } else {
        $island->{'eisei5'} = "$mshp,$msap,$msdp,$mssp,$mswin,$msexe,$tet";
    }
    $island->{'eisei6'} = "$c13,$shu,$m26,$m27,$m74,$m75,$m76,$m77,$m78,$m79,$m84,$m93,$m95";

    # 失業者数
    $island->{'unemployed'} = $pop - ($farm + $factory + $mountain + $factoryHT) * 10;

    my $ep1 = ($island->{'eis1'}) ?  (100 + $island->{'eis1'}*2) : 0;
    my $ep2 = ($island->{'eis2'}) ?  (300 + $island->{'eis2'}*2) : 0;
    my $ep3 = ($island->{'eis3'}) ?  (500 + $island->{'eis3'}*2) : 0;
    my $ep4 = ($island->{'eis4'}) ?  (900 + $island->{'eis4'}*2) : 0;
    my $ep5 = ($island->{'eis5'}) ? (1500 + $island->{'eis5'}*2) : 0;
    my $ep6 = ($island->{'eis6'}) ? (2000 + $island->{'eis6'}*2) : 0;

    $island->{'absent'} = 0 if ( ($land->[0][0] == $HlandMonument) && ($landValue->[0][0] == 71)) ;
    $island->{'absent'} = 0 if ($Hdebug);

    # 食料ポイント  2個目からポイントなので、先に1点引いとく
    my ($foodkindPoint) = -20;

    my ($FoodKind_cnt) = 0;
    foreach (@foodkind){
        $foodkindPoint += 20 if ($_);
        $FoodKind_cnt++ if ($_);
    }

    if ( $FoodKind_cnt > 2) {
        my ($fktemp) =$FoodKind_cnt - 2;
        $foodkindPoint += (((($fktemp * $fktemp) + $fktemp ) / 2) * 5);
    }

    # 動物園
    if (!$zoocnt) {
        $island->{'zoo'} = 0;
        $island->{'zoo_Mons_cnt'} = 0;
    }else{
        my ($zookazu, $zookazus, $m_syurui) = Get_ZooState($island);
        $island->{'zoo_Mons_cnt'} = $zookazu;
    }

    $foodkindPoint = 0 if ( $foodkindPoint < 0);

    # 総合Point
    $island->{'pts'} = int(  $pop + $island->{'money'}/100
                           + $island->{'food'}/100 + ($farm*2 + $factory + $mountain*2 + int(($factoryHT * 25)/10))
                           + $bas + $area*5 + $sci*30 + $pro*20 + $sba*10 + $amu*10 + $oil*500
                           + $kin*500 + $m26*300 + $m27*200 + $m74*250 + $m75*250 + $m76*250
                           + $m77*250 + $m78*250 + $m79*250 + $m93*500 + int($tare/15)
                           + int($zipro/12) + int($leje/10)
                           + ($m95 * 500)
                           + $ep1 + $ep2 + $ep3 + $ep4 + $ep5 + $ep6 + $hou*500 + $foodkindPoint);

    $island->{'pts'} = 0 if( ($land->[0][0] == $HlandMonument) && ($landValue->[0][0] == 71)) ;
    $island->{'pts'} = 1 if( ($land->[0][0] == $HlandMonument) && ($landValue->[0][0] == 70)) ;

    $island->{'tha_diff'} = $island->{'pts'} - $island->{'tha_point'}

}


#----------------------------------------------------------------------
# 怪獣の landvalueを算出
#----------------------------------------------------------------------
sub Calc_MonsterLandValue {
    my ($mKind) = @_;

    return ($mKind << $Mons_Kind_Shift) + $HmonsterBHP[$mKind] + random($HmonsterDHP[$mKind]);
}


#----------------------------------------------------------------------
# 怪獣の landvalueを算出
#----------------------------------------------------------------------
sub Calc_MonsterLandValue_HP {
    my ($mKind , $hp) = @_;

    return ($mKind << $Mons_Kind_Shift) + $hp;
}


#----------------------------------------------------------------------
# 幸福度の調査
#----------------------------------------------------------------------
sub Calc_Happiness_Town {
    my ($island , $x , $y , $range) = @_;

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};

    my ($i,$sx,$sy);
    my ($pop) = 0;
    my ($score) = 0;

    for ($i = 0; $i < $range; $i++) {

        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # 行による位置調整
        $sx-- if(!($sy % 2) && ($y % 2));

        if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)) {
            # 範囲外の場合
        } else {
            # 範囲内の場合
            if (grep {$_ == $land->[$sx][$sy]} @Htowns) {
                $pop += $landValue->[$sx][$sy];
            }
        }
    }

    $score += int(($pop/100));

    return ($score);
}


#----------------------------------------------------------------------
# ゲートの有無を調べる
#----------------------------------------------------------------------
sub CheckGate {
    my ($island) = @_;

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};

    if ($land->[0][0] == $HlandMonument && $landValue->[0][0] == 70) {
        return 1;
    }

    return 0;
}


#----------------------------------------------------------------------
# まちの成長をまとめたつもり
#----------------------------------------------------------------------
sub Town_Growup {
    my($lv, $adpop, $adpop2, $stop ) = @_;

    # 成長
    if($lv < $stop ) {
        $lv += random($adpop) + 1;
        if($lv > $stop) {
            $lv = $stop;
        }

    } else {
        # 都市になると成長遅い
        if($adpop2 > 0) {
            $lv += random($adpop2) + 1;
        }
    }

    return ($lv);
}


#----------------------------------------------------------------------
# 範囲内の地形を数える(New)
#----------------------------------------------------------------------
sub countAround {
    my ($land, $x, $y, $range, @kind) = @_;

    my ($i, $count, $sx, $sy, @list);
    $count = 0;
    for($i = 0; $i < $range; $i++) {
        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # 行による位置調整
        $sx-- if(!($sy % 2) && ($y % 2));

        if (($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)) {
            # 範囲外の場合
            # 海に加算
            $list[$HlandSea]++;
        } else {
            # 範囲内の場合
            $list[$land->[$sx][$sy]]++;
        }
    }
    foreach (@kind){
        $count += ($list[$_]) ? ($list[$_]) : 0;
    }
    return $count;
}


#----------------------------------------------------------------------
# 範囲内の怪獣を数える
#----------------------------------------------------------------------
sub countAroundMonster_wo_Pet {
    my ($island, $x, $y, $range) = @_;
    my ($i, $count, $sx, $sy);
    $count = 0;

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};

    my ($mKind, $mName, $mHp);
    for($i = 1; $i < $range; $i++) {
        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # 行による位置調整
        $sx-- if(!($sy % 2) && ($y % 2));

        if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)) {
            # 範囲外の場合
        } else {

            # 範囲内の場合
            if ($land->[$sx][$sy] == $HlandMonster) {
                ($mKind, $mName, $mHp) = monsterSpec($landValue->[$sx][$sy]);
                unless (   ($mKind == $Mons_SuperTetra)
                        || ($mKind == 28)
                                                            ) {
                    return 1;
                }
            }
        }
    }

    return 0;
}


#----------------------------------------------------------------------
# 範囲内の防衛基地を数える(New)
#----------------------------------------------------------------------
sub countAround_DefBase {
    my($land, $landValue, $x, $y, $range, $tvalue) = @_;
    my($i, $count, $sx, $sy,$deflv);
    $count = 0;
    for($i = 0; $i < $range; $i++) {
        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # 行による位置調整
        $sx-- if(!($sy % 2) && ($y % 2));
        if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)) {
            # 範囲外
        } else {

            $deflv = $landValue->[$sx][$sy] & $HDefenceLevelMask ;
            if(   ($land->[$sx][$sy] == $HlandDefence)
               && ($deflv >= $tvalue) ) {
                $count++;
            }
        }
    }
    return $count;
}


#----------------------------------------------------------------------
# 0から(n - 1)までの数字が一回づつ出てくる数列を作る
#----------------------------------------------------------------------
sub randomArray {
    my($n) = @_;
    my(@list, $i);

    # 初期値
    $n = 1 if($n == 0);
    @list = (0..$n-1);

    # シャッフル
    for ($i = $n; --$i; ) {
        my($j) = int(rand($i+1));
        next if($i == $j);
        @list[$i,$j] = @list[$j,$i];
    }

    return @list;
}


#----------------------------------------------------------------------
# 歴代最多人口記録
#----------------------------------------------------------------------
sub islandReki {
    my($line, $i, $id, $pop, $turn, $name, $n, $island, @rekidai, $reki);
    my $j = 0;

    if(!open(RIN, "<${HdirName}/rekidai.dat")) {
        rename("${HdirName}/rekidai.tmp", "${HdirName}/rekidai.dat");
        if(!open(RIN, "${HdirName}/rekidai.dat")) {
            # 人口順にソート
            my @idx = (0..$#Hislands);
            @idx = sort {   $Hislands[$b]->{'field'} <=> $Hislands[$a]->{'field'}
                         || $Hislands[$b]->{'pop'} <=> $Hislands[$a]->{'pop'}
                         || $a <=> $b } @idx;
            open(ROUT, ">${HdirName}/rekidai.tmp");
            foreach $i ($HbfieldNumber..$islandNumber) {# 現存する島すべてを記録
                $island = $Hislands[$idx[$i]];
                $id = $island->{'id'};
                $name = islandName($island);
                $pop = $island->{'pop'};
                print ROUT "$id,$pop,$HislandTurn,$name\n";
            }
            close(ROUT);
            rename("${HdirName}/rekidai.tmp", "${HdirName}/rekidai.dat");
            return;
        }
    }

    while($line = <RIN>) {
        $line =~ /^([0-9]*),([0-9]*),([0-9]*),(.*)$/;
        ($id, $pop, $turn, $name) = ($1, $2, $3, $4);
        if(defined $HidToNumber{$id}) {
            $HidToNumberR{$id} = $j;
            $rekidai[$j]->{'id'} = $id;
        }
        $rekidai[$j]->{'pop'} = $pop;
        $rekidai[$j]->{'turn'} = $turn;
        $rekidai[$j]->{'name'} = $name;
        $j++;
    }
    close(RIN);

    foreach $i ($HbfieldNumber..$islandNumber) {
        $island = $Hislands[$i];
        $id = $island->{'id'};
        $name = $island->{'name'};
        $pop = $island->{'pop'};
        $n = $HidToNumberR{$id};
        if(defined $n) {
            if($pop > $rekidai[$n]->{'pop'}) {
                $rekidai[$n]->{'pop'} = $pop;
                $rekidai[$n]->{'turn'} = $HislandTurn;
                $rekidai[$n]->{'name'} = $name;
            }
        } else {
            $rekidai[$j]->{'id'} = $id;
            $rekidai[$j]->{'pop'} = $pop;
            $rekidai[$j]->{'turn'} = $HislandTurn;
            $rekidai[$j]->{'name'} = $name;
            $j++;
        }
    }

    # 人口が同じときは直前のターンの順番のまま
    my @idx = (0..$#rekidai);
    @idx = sort { $rekidai[$b]->{'pop'} <=> $rekidai[$a]->{'pop'} || $a <=> $b } @idx;
    @rekidai = @rekidai[@idx];

    open(ROUT, ">${HdirName}/rekidai.tmp");
    my $recordNo = ($HmaxIsland < 15) ? 15 : $HmaxIsland;
    for($i = 0; $i < $recordNo; $i++) { # 最大で島の最大数と同じだけ記録。最低で15島。
        $reki = $rekidai[$i];
        $n = $i + 1;
        if(defined $reki->{'pop'}) {
            ($id, $pop, $turn, $name) = ($reki->{'id'}, $reki->{'pop'}, $reki->{'turn'}, $reki->{'name'});
            print ROUT "$id,$pop,$turn,$name\n";
        }
    }
    close(ROUT);
    unlink("${HdirName}/rekidai.dat");
    rename("${HdirName}/rekidai.tmp", "${HdirName}/rekidai.dat");
}


#----------------------------------------------------------------------
# ログをまとめる
#----------------------------------------------------------------------
sub logMatome {
    my($island, $flag, $kind) = @_;

    my($sno, $i, $sArray, $spnt, $x, $y, $point);
    $sno = $island->{$kind};
    $point = '';
    if($sno > 0) {
        if($flag == 1) {
            $kind .= 'pnt';
            $sArray = $island->{$kind};
            for($i = 0; $i < $sno; $i++) {
                $spnt = $sArray->[$i];
                last if($spnt eq "");
                ($x, $y) = ($spnt->{x}, $spnt->{y});
                $point .= "($x, $y)";
                $point .= "<br>　　　" unless(($i+1)%20);
            }
        }
        $point .= "の<B>$snoケ所</B>" if($i > 1 || $flag != 1);
    }
    unless($point eq "") {
        if(($flag == 1) && ($sno > 1)) {
            logLandSucMatome($island->{'id'}, islandName($island), '整地', "$point");
        } else {
            logLandSuc($island->{'id'}, islandName($island), '整地', "$point");
        }
    }
}


#----------------------------------------------------------------------
# ログへの出力
# 第1引数:メッセージ
# 第2引数:当事者
# 第3引数:相手
# 通常ログ
#----------------------------------------------------------------------
sub logOut {
    push(@HlogPool,"0,$HislandTurn,$_[1],$_[2],$_[0]");
}

# 遅延ログ
sub logLate {
    push(@HlateLogPool,"0,$HislandTurn,$_[1],$_[2],$_[0]");
}

# 機密ログ
sub logSecret {
    push(@HsecretLogPool,"1,$HislandTurn,$_[1],$_[2],$_[0]");
}

# 記録ログ
sub logHistory {
    open(HOUT, ">>${HdirName}/hakojima.his");
    print HOUT "$HislandTurn,$_[0]\n";
    close(HOUT);
}

# Hakoniwa Cupログ
sub logHcup {
    open(COUT, ">>${HdirName}/hakojima.lhc");
    print COUT "$HislandTurn,$_[0]\n";
    close(COUT);
}

#----------------------------------------------------------------------
# 記録ログ調整
#----------------------------------------------------------------------
sub logHistoryTrim {
    open(HIN, "${HdirName}/hakojima.his");
    my (@line, $l, $count);
    $count = 0;
    while($l = <HIN>) {
        chomp($l);
        push(@line, $l);
        $count++;
    }
    close(HIN);

    if($count > $HhistoryMax) {
        open(HOUT, ">${HdirName}/hakojima.his");
        my($i);
        for($i = ($count - $HhistoryMax); $i < $count; $i++) {
            print HOUT "$line[$i]\n";
        }
        close(HOUT);
    }
}

#----------------------------------------------------------------------
# Hakoniwa Cupログ調整
#----------------------------------------------------------------------
sub logHcupTrim {
# Hakoniwa Cupログ保持行数(※戦績表示のためカット)
#$HhcMax = 300; # 優勝するまで削除しないなら、これくらいかな？(どうせ100で割り切れるターンごとに全削除されます)
    open(CIN, "${HdirName}/hakojima.lhc");
    my(@line, $l, $count);
    $count = 0;
    while($l = <CIN>) {
        chomp($l);
        push(@line, $l);
        $count++;
    }
    close(CIN);

    if($count > $HhcMax) {
        open(COUT, ">${HdirName}/hakojima.lhc");
        my($i);
        for($i = ($count - $HhcMax); $i < $count; $i++) {
            print COUT "$line[$i]\n";
        }
        close(COUT);
    }
}

#----------------------------------------------------------------------
# ログ書き出し
#----------------------------------------------------------------------
sub logFlush {
    open(LOUT, ">${HdirName}/hakojima.log0");

    # 全部逆順にして書き出す
    my($i);
    for($i = $#HsecretLogPool; $i >= 0; $i--) {
        print LOUT $HsecretLogPool[$i];
        print LOUT "\n";
    }
    for($i = $#HlateLogPool; $i >= 0; $i--) {
        print LOUT $HlateLogPool[$i];
        print LOUT "\n";
    }
    for($i = $#HlogPool; $i >= 0; $i--) {
        print LOUT $HlogPool[$i];
        print LOUT "\n";
    }
    close(LOUT);
}

#----------------------------------------------------------------------
# ログ書き出し(分割更新)
#----------------------------------------------------------------------
sub tempLogFlush {

    open(LOUT, ">>${HdirName}/secret.tmp");
    # そのまま書き出す
    my($i);
    for($i =0 ; $i <= $#HsecretLogPool; $i++) {
        print LOUT $HsecretLogPool[$i];
        print LOUT "\n";
    }
    close(LOUT);
    open(LOUT, ">>${HdirName}/late.tmp");
    for($i = 0; $i <= $#HlateLogPool; $i++) {
        print LOUT $HlateLogPool[$i];
        print LOUT "\n";
    }
    close(LOUT);
    open(LOUT, ">>${HdirName}/log.tmp");
    for($i = 0; $i <= $#HlogPool; $i++) {
        print LOUT $HlogPool[$i];
        print LOUT "\n";
    }
    close(LOUT);
}

#----------------------------------------------------------------------
# ファイルを丸ごとコピー
#----------------------------------------------------------------------
sub copy {
    my($src, $dest) = @_;

    open(FS, "<$src")  || die $!;
    open(FD, ">$dest") || die $!;
    binmode(FS); # Windowsローカルでは必要
    binmode(FD); # Windowsローカルでは必要

    my $buf;
    while (read(FS, $buf, 1024 * 8) > 0) {
        print FD $buf;
    }
    close(FD);
    close(FS);
}

#----------------------------------------------------------------------
# ディレクトリ消し
#----------------------------------------------------------------------
sub myrmtree {
    my($dn) = @_;
    opendir(DIN, "$dn/");
    my($fileName);
    while($fileName = readdir(DIN)) {
        unlink("$dn/$fileName");
    }
    closedir(DIN);
    rmdir($dn);
}

1;
