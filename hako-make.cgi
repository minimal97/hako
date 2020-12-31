#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# 新規作成モジュール(ver1.00)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
#----------------------------------------------------------------------

# 周囲5ヘックスの座標
#  周囲0ヘックスまで調査する場合、0番目のデータまでを調べる
#  周囲1ヘックスまで調査する場合、6番目のデータまでを調べる
#  周囲2ヘックスまで調査する場合、18番目のデータまでを調べる
#  周囲3ヘックスまで調査する場合、36番目のデータまでを調べる
#  周囲4ヘックスまで調査する場合、60番目のデータまでを調べる
#  周囲5ヘックスまで調査する場合、90番目のデータまでを調べる
# 例）周囲2ヘックスまで調査(1番目〜18番目のデータで調査)
#  for($i = 1; $i <= 18; $i++) {	 # 中心($x,$y)を含まず
#     $sx = $x + $ax[$i];
#     $sy = $y + $ay[$i];
#     # Y方向の補正(HEXマップなので必要)
#     $sy-- if((($sy % 2) == 0) && (($y % 2) == 1));
#     next if(($sx < 0) || ($sx > $islandSize)
#          || ($sy < 0) || ($sy > $islandSize));
#     if($land->[$sx][$sy] == $HlandSea) { # 海？
#         ....略....
#     }
#  }
require './hako-const.cgi';
require './hako-ally.cgi';
require './server_config.pm';


#----------------------------------------------------------------------
# 島の新規作成モード
#----------------------------------------------------------------------
# メイン
sub newIslandMain {
    # 不正アクセスをチェック
    if ($HadminJoinOnly) {
        unless($ENV{HTTP_REFERER}  =~ /^$HthisFile/) {
            unlock();
            tempHeader();
            tempNewIslandillegal();
            return;
        }
    }

    # 名前があるかチェック
    if ($HcurrentName eq '') {
        unlock();
        tempHeader();
        tempNewIslandNoName();
        return;
    }

    # 名前が正当かチェック
    if ($HcurrentName =~ /[,\?\(\)\<\>\$]|^無人|^沈没$/) {
        # 使えない名前
        unlock();
        tempHeader();
        tempNewIslandBadName();
        return;
    }

    # 名前の重複チェック
    if (nameToNumber($HcurrentName) != -1) {
        # すでに発見ずみ
        unlock();
        tempHeader();
        tempNewIslandAlready();
        return;
    }

    # passwordの存在判定
    if ($HinputPassword eq '') {
        # password無し
        unlock();
        tempHeader();
        tempNewIslandNoPassword();
        return;
    }

    # 確認用パスワード
    if ($HinputPassword2 ne $HinputPassword) {
        # password間違い
        unlock();
        tempHeader();
        tempWrongPassword();
        return;
    }

    # 新しい島の番号を決める
    $HcurrentNumber = $HislandNumber;
    $HislandNumber++;
    $islandNumber++;
    $Hislands[$HcurrentNumber] = makeNewIsland();
    my ($island) = $Hislands[$HcurrentNumber];

    # IDの使い回し
    my ($safety) = 0;
    while (defined $HidToNumber{$HislandNextID}) {
        $HislandNextID ++;
        $HislandNextID = 1 if($HislandNextID > 100);
        $safety++;
        last if($safety == 100);
    }

    # 各種の値を設定
    $island->{'name'} = $HcurrentName;
    $island->{'id'} = $HislandNextID;
    $island->{'landscore'} = 0;
    $HislandNextID ++;
    $HislandNextID = 1 if($HislandNextID > 100);
    $island->{'absent'} = $HgiveupTurn - 6;
    $island->{'BF_Flag'} = 0;
	$island->{'comment'} = '(未登録)';
	$island->{'password'} = encode($HinputPassword);
	$island->{'eisei1'} = 0;
	$island->{'eisei2'} = 0;
	$island->{'eisei3'} = 0;
	$island->{'eisei4'} = '0,0,0,0,0,0,0,0,0,0,0';
	$island->{'eisei5'} = '0,0,0,0,0,0,0';
	$island->{'eisei6'} = '0,0,0,0,0,0,0,0,0,0,0,0';
	$island->{'eis1'}   = 0;
	$island->{'eis2'}   = 0;
	$island->{'eis3'}   = 0;
	$island->{'eis4'}   = 0;
	$island->{'eis5'}   = 0;
	$island->{'eis6'}   = 0;
	$island->{'ext'}    = '0,0,0,0,0,0,0,0';
	$island->{'army'}   = 0;
	$island->{'taiji'}  = 0;
	$island->{'onm'}    = htmlEscape($HcurrentOwnerName);
	$island->{'ownername'} = htmlEscape($HcurrentOwnerName);
	$island->{'id1'}    = $HislandNextID;
	$island->{'kei'}    = 0;
	$island->{'rena'}   = 0;
	$island->{'shr'}    = 0;
    $island->{'shrturn'} = 0;
	$island->{'fore'}   = 0;
	$island->{'pika'}   = 0;
	$island->{'hamu'}   = 0;
	$island->{'monta'}  = 0;
	$island->{'tare'}   = 0;
	$island->{'zipro'}  = 0;
	$island->{'leje'}   = 0;
    $island->{'zoo'} = 0;
	$island->{'shutomessage'}   = 555;
    $island->{'weather'} = 0;
    $island->{'tha_point'} = 0;
    $island->{'happy'} = 100;

    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $mon += 1;
    $island->{'temperature'} = $HTemperatureAve[$mon];

    if ($HeasyMode) {
        if (random(100) < 50) {
            $island->{'eis1'} = 200;
        }
        else {
            $island->{'eis2'} = 200;
        }
    }
    # 人口その他算出
    estimate($HcurrentNumber);
    #if($HarmisticeTurn) {
    #   my $ally = $Hally[$campNum];
    #   $ally->{'score'} += $island->{'pts'};
    #   push(@{$ally->{'memberId'}}, $island->{'id'});
    #   $ally->{'number'}++;
    #   push(@{$island->{'allyId'}}, $ally->{'id'});
    #}
    $HidToNumber{$island->{'id'}} = $HcurrentNumber;
    islandSort('pts', 1);
    if ($HarmisticeTurn) {
        allyOccupy();
        allySort();
    }

    # データ書き出し
    writeIslandsFile($island->{'id'});
    logDiscover($HcurrentName); # ログ

    $HcurrentID = $HislandNextID - 1;
    $HmainMode = 'owner';
    $HjavaMode = 'java';
    # COOKIE出力
    cookieOutput();

    # 開放
    unlock();

    # 発見画面
    tempHeader();
    tempNewIslandHead($HcurrentName); # 発見しました!!
    foreach (0..$HcurrentNumber) {
        if ($Hislands[$_]->{'id'} == $island->{'id'}) {
            $HcurrentNumber = $_;
            last;
        }
    }
    axeslog() if($HtopAxes >= 1);
    islandInfo(); # 島の情報
    islandMap(1); # 島の地図、ownerモード
}

# 新しい島を作成する
sub makeNewIsland {
    # 地形を作る
    my ($land, $landValue) = makeNewLand();

    # 初期コマンドを生成
    my (@command, $i);
    for ($i = 0; $i < $HcommandMax; $i++) {
        $command[$i] = {
            'kind' => $HcomDoNothing,
            'target' => 0,
            'x' => 0,
            'y' => 0,
            'arg' => 0
        };
    }

    # 初期掲示板を作成
    my (@lbbs);
    for ($i = 0; $i < LBBS_MAX; $i++) {
        $lbbs[$i] = "0<<0>>";
    }

    # 島にして返す
    return {
        'land' => $land,
        'landValue' => $landValue,
        'command' => \@command,
        'lbbs' => \@lbbs,
        'money' => (!$HarmisticeTurn || !$HislandTurn ? $HinitialMoney : $HinitialMoney2),
        'food' =>  (!$HarmisticeTurn || !$HislandTurn ? $HinitialFood : $HinitialFood2),
        'kome' =>  (!$HarmisticeTurn || !$HislandTurn ? $HinitialFood : $HinitialFood2),
        'prize' => '0,0,',
        'monsterlive' => 0,
        'monsterlivetype' => 0,
        'hmonsterlivetype' => 0,
        'missiles' => 0,
        'ext' => '0,0,0,0,0,0,0,0',
    };
}

# 新しい島の地形を作成する
sub makeNewLand {
    # 基本形を作成
    my (@land, @landValue, $x, $y, $i);

    # 海に初期化
    foreach $y (0..$islandSize) {
        foreach $x (0..$islandSize) {
            $land[$x][$y] = $HlandSea;
            $landValue[$x][$y] = 0;
        }
    }

    # 中央の4*4に荒地を配置
    my ($center) = ISLAND_SIZE / 2 - 1;
    for ($y = $center - 1; $y < $center + 3; $y++) {
        for ($x = $center - 1; $x < $center + 3; $x++) {
            $land[$x][$y] = $HlandWaste;
        }
    }

    # 8*8範囲内に陸地を増殖
    for ($i = 0; $i < 120; $i++) {
        # ランダム座標
        $x = random(8) + $center - 3;
        $y = random(8) + $center - 3;

        if (countAround(\@land, $x, $y, 7, $HlandSea) != 7){
            # 周りに陸地がある場合、浅瀬にする
            # 浅瀬は荒地にする
            # 荒地は平地にする
            if ($land[$x][$y] == $HlandWaste) {
                $land[$x][$y] = $HlandPlains;
                $landValue[$x][$y] = 0;

            } elsif($land[$x][$y] == $HlandSea) {
                if ($landValue[$x][$y] == 1) {
                    $land[$x][$y] = $HlandWaste;
                    $landValue[$x][$y] = 0;
                } else {
                    $landValue[$x][$y] = 1;
                }
            }
        }
    }

    # 森を作る
    my ($count) = 0;
    while ($count < 4) {
        # ランダム座標
        $x = random(4) + $center - 1;
        $y = random(4) + $center - 1;

        # そこがすでに森でなければ、森を作る
        if ($land[$x][$y] != $HlandForest) {
            $land[$x][$y] = $HlandForest;
            $landValue[$x][$y] = 5; # 最初は500本
            $count++;
        }
    }

    # 町を作る
    $count = 0;
    while ($count < 2) {
        # ランダム座標
        $x = random(4) + $center - 1;
        $y = random(4) + $center - 1;

        # そこが森か町でなければ、町を作る
        if (   ($land[$x][$y] != $HlandTown)
            && ($land[$x][$y] != $HlandForest)) {
            $land[$x][$y] = $HlandTown;
            $landValue[$x][$y] = 5; # 最初は500人
            $count++;
        }
    }

    # 山を作る
    $count = 0;
    while ($count < 1) {
        # ランダム座標
        $x = random(4) + $center - 1;
        $y = random(4) + $center - 1;

        # そこが森か町でなければ、町を作る
        if (($land[$x][$y] != $HlandTown) &&
           ($land[$x][$y] != $HlandForest)) {
            $land[$x][$y] = $HlandMountain;
            $landValue[$x][$y] = 0; # 最初は採掘場なし
            $count++;
        }
    }

    # 基地を作る
    $count = 0;
    while ($count < 1) {
        # ランダム座標
        $x = random(4) + $center - 1;
        $y = random(4) + $center - 1;

        # そこが森か町か山でなければ、基地
        if ( ($land[$x][$y] != $HlandTown) &&
             ($land[$x][$y] != $HlandForest) &&
             ($land[$x][$y] != $HlandMountain) ) {

            $land[$x][$y] = $HlandBase;
            $landValue[$x][$y] = 0;
            $count++;
        }
    }

	return (\@land, \@landValue) if(!$HeasyMode);

	# ニュータウンを作る
	$count = 0;
	while($count < 1) {
		# ランダム座標
		$x = random(4) + $center - 1;
		$y = random(4) + $center - 1;

		# そこが森か町か山でなければ、基地
		if(($land[$x][$y] != $HlandTown) &&
			($land[$x][$y] != $HlandForest) &&
			($land[$x][$y] != $HlandBase) &&
			($land[$x][$y] != $HlandMountain)) {
			$land[$x][$y] = $HlandNewtown;
			$landValue[$x][$y] = 10;
			$count++;
		}
	}

	# 大学を作る
	$count = 0;
	while($count < 1) {
		# ランダム座標
		$x = random(4) + $center - 1;
		$y = random(4) + $center - 1;

		# そこが森か町か山でなければ、基地
		if(($land[$x][$y] != $HlandTown) &&
			($land[$x][$y] != $HlandForest) &&
			($land[$x][$y] != $HlandBase) &&
			($land[$x][$y] != $HlandNewtown) &&
			($land[$x][$y] != $HlandMountain)) {
			$land[$x][$y] = $HlandCollege;
			$landValue[$x][$y] = random(3);

			$count++;
		}
	}

    # 港を作る
    $count = 0;
    while ($count < 1) {
        # ランダム座標
        $x = random(4) + $center - 1;
        $y = random(4) + $center - 1;

        # 周りに陸があるかチェック
        my ($seaCount) =	countAround($land, $x, $y, 7, $HlandSea);
        if ($seaCount != 0) {
            # そこが森か町か山でなければ、基地
            if(($land[$x][$y] != $HlandTown) &&
				($land[$x][$y] != $HlandForest) &&
				($land[$x][$y] != $HlandBase) &&
				($land[$x][$y] != $HlandNewtown) &&
				($land[$x][$y] != $HlandCollege) &&
				($land[$x][$y] != $HlandMountain)) {
				$land[$x][$y] = $HlandMinato;
				$landValue[$x][$y] = 5;
				$count++;
            }
        }
    }

    return (\@land, \@landValue);
}


#----------------------------------------------------------------------
# 情報変更モード
#----------------------------------------------------------------------
# メイン
sub changeMain {
    # idから島を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];
    my ($flag) = 0;

    # パスワードチェック
    if (checkSpecialPassword($HoldPassword)) {
        # 特殊パスワード
        if ($HcurrentName =~ /^ログ$/) {
            # 最近の出来事強制出力
            logPrintHtml();
            unlock();
            tempChange();
            return;
        } elsif($HcurrentName =~ /^無人$/) {
            # 島削除モード
            deleteIsland(1);
            return;
		} elsif($HcurrentName =~ /^沈没$/) {
			# 島削除モード
			deleteIsland(0);
			return;
		} elsif(!checkMasterPassword($HoldPassword)) {
			# 食糧/資金maxモード
			$island->{'money'} = $HmaximumMoney;
			$island->{'food'}  = $HmaximumFood;
		}
	} elsif(!checkPassword($island,$HoldPassword)) {
		# password間違い
		unlock();
		tempWrongPassword();
		return;
	}

	# 確認用パスワード
	if($HinputPassword2 ne $HinputPassword) {
		# password間違い
		unlock();
		tempWrongPassword();
		return;
	}

	if($HcurrentName ne '') {
		# 島名変更の場合
		# 島名が正当かチェック
		if($HcurrentName =~ /[,\?\(\)\<\>\$]|^無人|^沈没$/) {
			# 使えない名前
			unlock();
			tempNewIslandBadName();
			return;
		}

		# 名前の重複チェック
		if(nameToNumber($HcurrentName) != -1) {
			# すでに発見ずみ
			unlock();
			tempNewIslandAlready();
			return;
		}

		if($island->{'money'} < $HcostChangeName) {
			# 金が足りない
			unlock();
			tempChangeNoMoney();
			return;
		}

		# 代金
		unless(checkSpecialPassword($HoldPassword)) {
			$island->{'money'} -= $HcostChangeName;
		}

		# 名前を変更
		logChangeName($island->{'name'}, $HcurrentName);
		$island->{'name'} = $HcurrentName;
		$flag = 1;
	}

	if ($HcurrentOwnerName ne '') {
		# オーナー名変更の場合
		# オーナー名が正当かチェック
		if($HcurrentOwnerName =~ /[,\?\(\)\<\>\$]/) {
			# 使えない名前
			unlock();
			tempNewIslandBadOwnerName();
			return;
		}

		if($island->{'money'} < $HcostChangeName) {
			# 金が足りない
			unlock();
			tempChangeNoMoney();
			return;
		}

		# 代金
		unless(checkSpecialPassword($HoldPassword)) {
			$island->{'money'} -= $HcostChangeName;
		}

		# オーナー名を変更
		logChangeOwnerName($island->{'name'}, $HcurrentOwnerName);
		$island->{'onm'} = $HcurrentOwnerName;
		$flag = 1;
	}

	# password変更の場合
	if($HinputPassword ne '') {
		# パスワードを変更
		$island->{'password'} = encode($HinputPassword);
		$flag = 1;
	}

	if(($flag == 0) && !checkSpecialPassword($HoldPassword)) {
		# どちらも変更されていない
		unlock();
		tempChangeNothing();
		return;
	}

	# データ書き出し
	writeIslandsFile($HcurrentID);
	unlock();

	# 変更成功
	tempChange();
}

# 島の名前から番号を得る(IDじゃなくて番号)
sub nameToNumber {
	my($name) = @_;

	# 全島から探す
	my($i);
	foreach $i (0..$islandNumber) {
		if($Hislands[$i]->{'name'} eq $name) {
			return $i;
		}
	}

	# 見つからなかった場合
	return -1;
}


#----------------------------------------------------------------------
# ＨＴＭＬ生成
#----------------------------------------------------------------------
sub logPrintHtml {
	my($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) = gmtime(time + $Hjst);
	$mon++;
	my($sss) = "${mon}月${date}日 ${hour}時${min}分${sec}秒";

	$html1=<<_HEADER_;
<HTML><HEAD>
<TITLE>
最近の出来事
</TITLE>
<BASE HREF="$htmlDir/">
<link rel="stylesheet" type="text/css" href="${efileDir}/$HcssFile">
</HEAD>
<BODY $htmlBody><DIV ID='BodySpecial'>
<DIV ID='RecentlyLog'>
<H1>最近の出来事</H1>
<FORM>
最新更新日：$sss・・
<INPUT TYPE="button" VALUE=" 再読込み" onClick="location.reload()">
</FORM>
<hr>
_HEADER_

$html3=<<_FOOTER_;
</DIV><HR></DIV></BODY></HTML>
_FOOTER_
	my($i);
	for($i = 0; $i < $HhtmlLogTurn; $i++) {
		$id =0;
		$mode = 0;
		my($set_turn) = 0;
		open(LIN, "${HdirName}/hakojima.log$i");
		my($line, $m, $turn, $id1, $id2, $message);
		while($line = <LIN>) {
			$line =~ /^([0-9]*),([0-9]*),([0-9]*),([0-9]*),(.*)$/;
			($m, $turn, $id1, $id2, $message) = ($1, $2, $3, $4, $5);

			# 機密関係
			if($m) {
				next if(!$mode || ($id1 != $id)); # 機密表示権利なし
				$m = '<B>(機密)</B>';
			} else {
				$m = '';
			}

			# 表示的確か
			if($id) {
				next if(($id != $id1) && ($id != $id2));
			}

			# 表示
			if(!$set_turn){
				if(!$Hseason) {
					$html2 .= "<B>=====[<span class=number><FONT SIZE=4> ターン$turn </FONT></span>]================================================</B><BR>\n";
				} else {
					# 季節の表示
					my @seasonName = ('<span class=winter>冬</span>','<span class=spring>春</span>','<span class=summer>夏</span>','<span class=autumn>秋</span>');
					my $month = ($turn % 12) + 1;
					my $year  = ($turn / 12) + 1;
					my $calender = sprintf('<span class=month><FONT SIZE=2><small>%s</small> %d年 %d月 </FONT></span>' , $Halmanac, $year, $month);
					$calender .= "<span class='season'>$seasonName[int(($month - 1) / 3)]</span>";
					$html2 .= "<B>=====[<span class=number><FONT SIZE=4> <small>ターン$turn</small> </FONT></span>]=============================$calender</B><BR>\n";
				}
				$set_turn++;
			}
			$html2 .= "${HtagNumber_}★${H_tagNumber}:$message<BR>\n";
		}
		close(LIN);
	}
	open(HTML, ">${HhtmlDir}/hakolog.html");
#	print HTML jcode::sjis($html1);
#	print HTML jcode::sjis($html2);
#	print HTML jcode::sjis($html3);
	print HTML $html1;
	print HTML $html2;
	print HTML $html3;
	close (HTML);
	chmod(0666,"${HhtmlDir}/hakolog.html");
}


#----------------------------------------------------------------------
# Battle Field
#----------------------------------------------------------------------
# メイン
sub bfpointMain {

	# 開放
	unlock();

    my $bfpoint;

	my @HCislands = @Hislands;
	my @idx = (0..$#Hislands);
	@idx = sort { $Hislands[$b]->{'landscore'} <=> $Hislands[$a]->{'landscore'} ||
                 $b <=> $a } @idx;

	@HCislands = @HCislands[@idx];

	out(<<END);
<CENTER>$HtempBack</CENTER><BR>
<H1>Battle Field のルール(まだ作りかけ)</H1><br>
・怪獣を倒すと、自分の島に賞金が贈られます。（1点：${HBF_Point_Value}${HunitMoney}）<br>
・SPPミサイル以外を当てると、BFポイントが1点もらえます。<br>
・怪獣を倒した場合、少し多めにBFポイントがもらえます。<br>
<DIV ID='Successive'>
<H1>Battle Field 戦績</H1>
<table border=0 width=50%>
<TR>
<TH $HbgTitleCell align=center >${HtagTH_}順位${H_tagTH}</TH>
<TH $HbgTitleCell align=center >${HtagTH_}${AfterName}名${H_tagTH}</TH>
<TH $HbgTitleCell align=center >${HtagTH_}ポイント${H_tagTH}</TH>
</TR>
END

    my ($lName);
    my ($rank);
    my ($zeroflag) = @Hislands;

    $rank = 0;      # すぐ++ するので 0
	foreach $i (0..$#Hislands) {

        next if($HCislands[$i]->{'BF_Flag'});
        $rank ++;
        $bfpoint = $HCislands[$i]->{'landscore'};
        $lName = $HCislands[$i]->{'name'};

	out(<<END);

<tr>
    <TD $HbgNumberCell align=right >${HtagNumber_}$rank${H_tagNumber}</TD>
    <TD $HbgNameCell align=right >${HtagName_}$lName${AfterName}${H_tagName}</TD>

    <TD $HbgNumberCell align=right >${HtagWin_}$bfpoint${H_tagWin}</TD>
</tr><!-- $i / $HCislands[$i]->{'id'} $zeroflag -->
END
	}
	out(<<END);
    </table><br>
END


}
#----------------------------------------------------------------------
# HakoniwaCup戦績
#----------------------------------------------------------------------
# メイン
sub hcdataMain {
	foreach $i (0..$islandNumber) {
		my @hcdata = split(/,/, $Hislands[$i]->{'eisei4'});
		$Hislands[$i]->{'hcdata'} = \@hcdata;
		if($hcdata[10] >= 10) {
			$Hislands[$i]->{'hcover'} = 1;
		}
		if($hcdata[3] + $hcdata[4] + $hcdata[5] > 4) {
			$Hislands[$i]->{'hctmnt'} = $hcdata[3] + $hcdata[4] + $hcdata[5];
		}
	}

	my @HCislands = @Hislands;
	my @idx = (0..$#Hislands);
	@idx = sort { $Hislands[$a]->{'field'} <=> $Hislands[$b]->{'field'} ||
					$Hislands[$a]->{'hcover'} <=> $Hislands[$b]->{'hcover'} ||
					$Hislands[$b]->{'hctmnt'} <=> $Hislands[$a]->{'hctmnt'} ||
					$Hislands[$b]->{'hcdata'}[10] <=> $Hislands[$a]->{'hcdata'}[10] ||
					$Hislands[$b]->{'hcdata'}[3] <=> $Hislands[$a]->{'hcdata'}[3] ||
					$Hislands[$b]->{'hcdata'}[4] <=> $Hislands[$a]->{'hcdata'}[4] ||
					$Hislands[$a]->{'hcdata'}[5] <=> $Hislands[$b]->{'hcdata'}[5] ||
					$Hislands[$b]->{'hcdata'}[6] <=> $Hislands[$a]->{'hcdata'}[6] ||
					$Hislands[$b]->{'hcdata'}[7] <=> $Hislands[$a]->{'hcdata'}[7] ||
					$Hislands[$a]->{'hcdata'}[8] <=> $Hislands[$b]->{'hcdata'}[8] ||
					$a <=> $b
				} @idx;
	@HCislands = @HCislands[@idx];
	my $hcturn = int($HislandTurn/100)*100;
	my($turn1, $str);
	my $turn = $HislandTurn%100;
#	if((0 <= $turn) && ($turn <= 40)) {
#		$turn1 = int(($turn + 9) / 10);
#	} elsif($turn == 41) {
#		$turn1 = 5;
#	} elsif((41 < $turn) && ($turn <= 45)) {
#		$turn1 = 6;
#	} elsif((45 < $turn) && ($turn <= 48)) {
#		$turn1 = 7;
#	} elsif((48 < $turn) && ($turn < 50)) {
#		$turn1 = 8;
#	} else {
#		$turn1 = 9;
#	}
#	if($turn1 == 9) {
#		$str = '[最終結果]';
#	} elsif($turn1 == 8) {
#		$str = '[決勝戦]';
#	} elsif($turn1 == 7) {
#		$str = '[準決勝戦]';
#	} elsif($turn1 == 6) {
#		$str = '[準々決勝戦]';
#	} elsif($turn1 == 5) {
#		$str = '[決勝トーナメント開始！]';
#	} else {
#		$str = '[予選]';
#	}
	# 開放
	unlock();

	out(<<END);
<CENTER>$HtempBack</CENTER><BR>
<DIV ID='Successive'>
<H1>HakoniwaCup $hcturn 戦績<BR>${str}</H1>
<table border=0 width=50%><TR>
<TH $HbgTitleCell align=center rowspan=2>${HtagTH_}順位${H_tagTH}</TH>
<TH $HbgTitleCell align=center rowspan=2>${HtagTH_}${AfterName}名${H_tagTH}</TH>
<TH $HbgTitleCell align=center rowspan=2>${HtagTH_}チーム名${H_tagTH}</TH>
<TH $HbgTitleCell align=center rowspan=2>${HtagTH_}勝${H_tagTH}</TH>
<TH $HbgTitleCell align=center rowspan=2>${HtagTH_}負${H_tagTH}</TH>
<TH $HbgTitleCell align=center rowspan=2>${HtagTH_}分${H_tagTH}</TH>
<TH $HbgTitleCell align=center colspan=4>${HtagTH_}総計${H_tagTH}</TH>
<TH $HbgTitleCell align=center colspan=3>${HtagTH_}能力${H_tagTH}</TH>
</TR><TR>
<TH $HbgTitleCell align=center>${HtagTH_}優勝回数${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}勝${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}負${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}分${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}攻撃${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}守備${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}キーパー${H_tagTH}</TH>
</TR>
END
	my %hcLog = hclogSet();
	my $n = 0;
	foreach $i (0..$islandNumber) {
		my $hcdata = $HCislands[$i]->{'hcdata'};
		my($sto,$std,$stk,$stwin,$stdrow,$stlose,$stwint,$stdrowt,$stloset,$styusho,$stshoka) = @$hcdata;
		next if($stshoka == 0);
        next if ($HCislands[$i]->{'predelete'});
#		next if($stwin + $stdrow + $stlose == 0);
		$n++;
		my $juni = $n;
#		if(($turn1 >= 5) && ($n > 8)) {
#			$juni = '予選落ち';
#		} elsif(($turn1 > 6) && ($n > 4)) {
#			$juni = 'ベスト８';
#		} elsif(($turn1 > 7) && ($n > 2)) {
#			$juni = 'ベスト４';
#		} elsif($turn1 > 8) {
#			if($n == 1) {
#				$juni = '優勝';
#			} elsif($n == 2) {
#				$juni = '準優勝';
#			}
#		}
		my $id = $HCislands[$i]->{'id'};
		my $name = islandName($HCislands[$i]);
		my $kekka = $hcLog{$name};
        my $team = "${HtagName_}$HCislands[$i]->{'hakoteam'}${H_tagName}";
		$kekka = '　' if($kekka eq '');
		$name = "<A STYlE=\"text-decoration:none\" HREF=\"${HthisFile}?Sight=${id}\" alt=\"ID=${id}\" title=\"ID=${id}\">${HtagName_}$name${H_tagName}</A>";
		out("<TR><TH></TH></TR>") if($n == 9);
		out(<<END);
<tr>
<TD $HbgNumberCell align=right rowspan=2>${HtagNumber_}$juni${H_tagNumber}</TD>
<TD $HbgNameCell align=right rowspan=2>$name</TD>
<TD $HbgNameCell align=right rowspan=2>$team</TD>
<TD $HbgPoinCell align=right rowspan=2>${HtagWin_}$stwin${H_tagWin}</TD>
<TD $HbgInfoCell align=right rowspan=2>${HtagLose_}$stlose${H_tagLose}</TD>
<TD $HbgInfoCell align=right rowspan=2>$stdrow</TD>
<TD $HbgInfoCell align=right>$styusho</TD>
<TD $HbgInfoCell align=right>$stwint</TD>
<TD $HbgInfoCell align=right>$stloset</TD>
<TD $HbgInfoCell align=right>$stdrowt</TD>
<TD $HbgInfoCell align=right>$sto</TD>
<TD $HbgInfoCell align=right>$std</TD>
<TD $HbgInfoCell align=right>$stk</TD>
</tr>
<tr>
<TD $HbgTotoCell align=left colspan=7>$kekka</TD>
</tr>
END
	}
	if(!$n) {
		out(<<END);
<tr><TH colspan=12>データがありません！</TH></tr>
END
	}
	out(<<END);
</table>
※『多目的スタジアム』を失うなどしてデータが初期化された場合は、<BR>
実際の試合結果と順位が異なる場合があります。ご了承下さい。
</DIV>
END
}

# 対戦表示
sub hclogSet {
	my($line, $turn, $message);
	my %hcLog;
	if(!open(LIN, "${HdirName}/hakojima.lhc")) {
		return %hcLog;
	}
	while($line = <LIN>) {
		chomp($line);
		($turn, $message) = split(/,/, $line);
		next unless($message =~ /^<span class="islName">Hakoniwa Cup (.*)<\/span>、(.*)$/);
		my ($no, $kekka) = ($1, $2);
		next unless($kekka =~ /^<span class="([\w]*)">(.*)島代表(.*)<\/span><B>VS<\/B><span class="([\w]*)">(.*)島代表(.*)<\/span> ⇒ (.*)$/);
		my($wl1, $name1, $tname1, $wl2, $name2, $tname2, $score) = ($1, $2, $3, $4, $5,$6,$7);
		if($no !~ /決勝/) {
			$score =~ /^<span class="([\w]*)">([0-9]*)<\/span><B>−<\/B><span class="([\w]*)">([0-9]*)<\/span>$/;
			$hcLog{$name1} = '予選' if($hcLog{$name1} eq '');
			$hcLog{$name2} = '予選' if($hcLog{$name2} eq '');
			$hcLog{$name1} .= " <span class=\"$wl1\"><a title=\"$no($2-$4)\">$name2島</a></span>";
			$hcLog{$name2} .= " <span class=\"$wl2\"><a title=\"$no($2-$4)\">$name1島</a></span>";
		} else {
			if($no =~ /準々決勝/) {
				$hcLog{$name1} .= "\n<BR>";
				$hcLog{$name2} .= "\n<BR>";
			}
			$score =~ /^<span class="([\w]*)">([0-9]*)<\/span><B>−<\/B><span class="([\w]*)">([0-9]*)<\/span>$/;
			$hcLog{$name1} .= " <B>${no}vs</B><span class=\"$wl1\"><a title=\"$no($2-$4)\">$name2島</a></span>";
			$hcLog{$name2} .= " <B>${no}vs</B><span class=\"$wl2\"><a title=\"$no($2-$4)\">$name1島</a></span>";
		}
	}

	close(LIN);
	return %hcLog;
}

#----------------------------------------------------------------------
# 新しい島を探す
#----------------------------------------------------------------------
# メイン
sub newIslandTop {
	# 開放
	unlock();

	# 管理人だけが新しい島を探せる？
	if ($HadminJoinOnly) {
		# マスタパスワードチェック
		unless (checkMasterPassword($HinputPassword)) {
			# password間違い
			tempWrongPassword();
			return;
		}
	}
	
	out(<<END);
<CENTER>$HtempBack</CENTER><BR>
<DIV ID='newIsland'>
<H1>新しい${AfterName}を探す</H1>
    <span class="rednews">島の作成はひとり、1島までです。<br>同じIPアドレスが割り当てられた島を見つけたら、沈めます。<br>家族など、同じIPアドレスになる場合は、先に連絡してください。</span>
END

	if(($HislandNumber - $HbfieldNumber < $HmaxIsland) && ($HmaxIsland <= 100)) {
		out(<<END);
<FORM action="$HthisFile" method="POST">
END
		if ($HcampSelectRule == 2) {
			my $allyList;
			foreach (0..$#Hally) {
				next if ($Hally[$_]->{'number'} >= ($HmaxIsland / $HallyNumber));
				my $s = '';
				$s = ' SELECTED' if($_ == 0);
				$allyList .= "<OPTION VALUE=\"$_\"$s>$Hally[$_]->{'name'}\n";
			}
			out(<<END);
陣営名を選択して下さい<BR>
<SELECT NAME="CAMPNUMBER">
$allyList
<OPTION VALUE=\"-1\">どこでも良い
</SELECT><BR>
END
		}
		out(<<END);
どんな名前をつける予定？<small>(全角${HlengthIslandName}字まで)</small><BR>
<INPUT TYPE="text" NAME="ISLANDNAME" SIZE=32 MAXLENGTH=32>${AfterName}<BR>
あなたの名前は？<small>(全角${HlengthOwnerName}字まで)</small><BR>
<INPUT TYPE="text" NAME="OWNERNAME" SIZE=32 MAXLENGTH=32><BR>
パスワードは？<BR>
<INPUT TYPE="password" NAME="PASSWORD" SIZE=32 MAXLENGTH=32><BR>
念のためパスワードをもう一回<BR>
<INPUT TYPE="password" NAME="PASSWORD2" SIZE=32 MAXLENGTH=32><BR>

<INPUT TYPE="submit" VALUE="探しに行く" NAME="NewIslandButton">
</FORM>
</DIV>
END
	} else {
	out(<<END);
		${AfterName}の数が最大数です・・・現在登録できません。<br>
		HislandNumber:${HislandNumber}<br>
		HbfieldNumber:${HbfieldNumber}<br>
		HmaxIsland:${HmaxIsland}<br>
		HarmisticeTurn:${HarmisticeTurn}<br>
		HallyNumber:${HallyNumber}
</DIV>
END
	}
}

#----------------------------------------------------------------------
# 島の名前とパスワードの変更
#----------------------------------------------------------------------
# メイン
sub renameIslandMain {
    # 開放
    unlock();

    out(<<END);
<CENTER>$HtempBack</CENTER><BR>
<DIV ID='changeInfo'>
<H1>${AfterName}の名前とパスワードの変更</H1>
<table border=0 width=50%><tr><td class="M"><P>
(注意)${AfterName}の名前の変更には$HcostChangeName${HunitMoney}かかります。(他は無料)
</P>
<FORM action="$HthisFile" method="POST">
どの${AfterName}ですか？<BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>
<BR>
どんな名前に変えますか？(変更する場合のみ)<small>(全角${HlengthIslandName}字まで)</small><BR>
<input type="text" NAME="ISLANDNAME" SIZE=32 MAXLENGTH=32>${AfterName}<BR>
あなたの名前を変えますか？(変更する場合のみ)<small>(全角${HlengthOwnerName}字まで)</small><BR>
<input type="text" NAME="OWNERNAME" SIZE=32 MAXLENGTH=32><BR>
パスワードは？(必須)<BR>
<input type="password" name="OLDPASS" size=32 maxlength=32><BR>
新しいパスワードは？(変更する時のみ)<BR>
<input type="password" name="PASSWORD" size=32 maxlength=32><BR>
念のためパスワードをもう一回(変更する時のみ)<BR>
<input type="password" name="PASSWORD2" size=32 maxlength=32><BR>
<input type="submit" value="変更する" name="ChangeInfoButton">
</form>
</td></tr></table></div>
END
}


#----------------------------------------------------------------------
# 人口その他の値を算出（縮小版）
sub estimate {
	my ($number) = $_[0];
	my ($island);
	my ($pop, $area, $missiles, $fore) = (0, 0, 0, 0);

	# 地形を取得
	$island = $Hislands[$number];
	my ($land) = $island->{'land'};
	my ($landValue) = $island->{'landValue'};

	# 数える
	my($x, $y, $kind, $value);
	foreach $y (0..$islandSize) {
		foreach $x (0..$islandSize) {
			$kind = $land->[$x][$y];
			$value = $landValue->[$x][$y];
			if($kind != $HlandSea) {
				$area++;
				if($kind == $HlandTown) {
					# 町
					$pop += $value;
				} elsif($kind == $HlandForest) {
					$fore += $value;
				}
			}

			if ($kind == $HlandBase) {
				$missiles++;
			}
		}
	}

	# 代入
	$island->{'pop'}		= $pop;
	$island->{'area'}		= $area;
	$island->{'missiles'}	= $missiles; # ミサイル発射可能数
	$island->{'fore'}		= $fore;

	# 失業者数
	$island->{'unemployed'} = $pop;

	# 総合Point
	$island->{'pts'} = int($pop + $island->{'money'}/100 + $island->{'food'}/100 + $area*5);

}

#----------------------------------------------------------------------
# 範囲内の地形を数える（コピー）(New)
sub countAround {
    my ($land, $x, $y, $range, @kind) = @_;

    my (@ax) = (0,1,1,1,0,-1,0,1,2,2,2,1,0,-1,-1,-2,-1,-1,0,2
            ,2,3,3,3,2,2,1,0,-1,-2,-2,-3,-2,-2,-1,0,1,2,3,3
            ,4,4,4,3,3,2,1,0,-1,-2,-2,-3,-3,-4,-3,-3,-2,-2,-1,0
            ,1,3,3,4,4,5,5,5,4,4,3,3,2,1,0,-1,-2,-3,-3,-4
            ,-4,-5,-4,-4,-3,-3,-2,-1,0,1,2);
    my (@ay) = (0,-1,0,1,1,0,-1,-2,-1,0,1,2,2,2,1,0,-1,-2,-2,-3
            ,-2,-1,0,1,2,3,3,3,3,2,1,0,-1,-2,-3,-3,-3,-4,-3,-2
            ,-1,0,1,2,3,4,4,4,4,4,3,2,1,0,-1,-2,-3,-4,-4,-4
            ,-4,-5,-4,-3,-2,-1,0,1,2,3,4,5,5,5,5,5,5,4,3,2
            ,1,0,-1,-2,-3,-4,-5,-5,-5,-5,-5);

    my ($sea, $count, $sx, $sy, @list);
    foreach (@kind){
        $list[$_] = 1;
    }

    $sea = 0;
    $count = 0;
    $range--;
    foreach(0..$range) {
        $sx = $x + $ax[$_];
        $sy = $y + $ay[$_];

        # 行による位置調整
        $sx-- if(!($sy % 2) && ($y % 2));

        if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)){
            # 範囲外の場合
            # 海に加算
            $sea++;
        } elsif($list[$land->[$sx][$sy]]) {
            # 範囲内の場合
            $count++;
        }
    }
    $count += $sea if($list[$HlandSea]);    # 海なら加算

    return $count;
}

#----------------------------------------------------------------------
# 管理人モード
#----------------------------------------------------------------------
# 島の強制削除(情報変更で)
sub deleteIsland {
    my ($num) = @_;

    my ($island) = $Hislands[$HidToNumber{$HcurrentID}];

    my $aNum = $HidToAllyNumber{$HcurrentID};
    if (defined $aNum) {
        require('./hako-ally.cgi');
		logDeleteAlly($Hally[$aNum]->{'name'});
		$Hally[$aNum]->{'dead'} = 1;
		$HallyNumber--;
	}

	foreach (@{$island->{'allyId'}}) {
		my $ally = $Hally[$HidToAllyNumber{$_}];
		my $allyMember = $ally->{'memberId'};
		my @newAllyMember = ();
		foreach (@$allyMember) {
			if(!(defined $HidToNumber{$_})) {
			} elsif($_ == $HcurrentID) {
				$ally->{'score'} -= $island->{'pts'};
				$ally->{'number'}--;
			} else {
				push(@newAllyMember, $_);
			}
		}
		$ally->{'memberId'} = \@newAllyMember;
	}
	# 島テーブルの操作
	$island->{'dead'} = 1;
	$island->{'pts'} = 0;
	$island->{'pop'} = 0;
	$island->{'field'} = 0;

	allyOccupy();
	allySort();
	islandSort('pts');

	logDeleteIsland($tmpid, $island->{'name'}) if($num);

	# メインデータの操作
	$HislandNumber--;
	$islandNumber--;
	writeIslandsFile($HcurrentID);

	unlink("${HdirName}/${HcurrentID}.${HsubData}");
	unlock();
	tempDeleteIsland($island->{'name'});
}

#----------------------------------------------------------------------
# BattleField作成モード
sub bfieldMain {
	if (!$HbfieldMode) {
		# 開放
		unlock();

		# テンプレート出力
		tempBfieldPage();
	} else {
		# パスワードチェック
		if(checkSpecialPassword($HdefaultPassword)) {
			# 特殊パスワード

			# idから島を取得
			$HcurrentNumber = $HidToNumber{$HcurrentID};
			my($island) = $Hislands[$HcurrentNumber];
			my($name) = islandName($island);
			my($id) = $island->{'id'};

			my $bId, $str;
			my $safety = 0;
			if($id < 100) {
				if ($HbfieldNumber > 9) {
					# Battle Fieldの数が最大(最大で10)
					tempBfieldNG('最大登録数オーバー');
					unlock();
					return;
				}

				# 設定
				for($bId = 101; $bId <= 120; $bId++) {
					last if(!(defined $HidToNumber{$bId}));
				}
				$island->{'id'} = $bId;
				$str = '通常の島 → Battle Field';
			} else {
				if ($HislandNumber - $HbfieldNumber >= $HmaxIsland) {
					# 通常の島の数が最大
					tempBfieldNG("${AfterName}がいっぱい");
					unlock();
					return;
				}
				# 解除
				while(defined $HidToNumber{$HislandNextID}) {
					$HislandNextID ++;
					$HislandNextID = 1 if($HislandNextID > 100);
					$safety++;
					last if($safety == 100);
				}
				$island->{'id'} = $HislandNextID;
				$HislandNextID ++;
				$HislandNextID = 1 if($HislandNextID > 100);
				$str ='Battle Field → 通常の島';
			}

			if (($bId > 121) || ($safety == 100)) {
				# 変更のためのIDが設定できず
				tempBfieldNG('IDシークエラー');
				unlock();
				return;
			}
			# データ書き出し
			writeIslandsFile($HcurrentID);
			rename("${HdirName}/${id}.${HsubData}", "${HdirName}/${island->{'id'}}.${HsubData}");

			unlock();

			# 変更成功
			tempBfieldOK($name, $str);
		} else {
			# password間違い
			unlock();
			tempWrongPassword();
			return;
		}
	}
}

#----------------------------------------------------------------------
# BattleField作成モードのトップページ
sub tempBfieldPage {
    out(<<END);
<CENTER>$HtempBack</CENTER>
<H1>Battle Fieldを作成</H1>

<FORM action="$HthisFile" method="POST">
<B>Battle Field設定を変更する${AfterName}は？</B><BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>
<INPUT TYPE="hidden" VALUE="$HdefaultPassword" NAME="Bfield">
<INPUT TYPE="submit" VALUE="設定変更" NAME="BfieldButton"><BR>
</FORM>
END
}

#----------------------------------------------------------------------
# BattleField作成完了
sub tempBfieldOK {
    my ($name, $str) = @_;

    out(<<END);
${HtagBig_}$name${AfterName}のBattle Field設定を変更しました。<br>$str${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# BattleField作成失敗
sub tempBfieldNG {
    my ($str) = @_;

    out(<<END);
${HtagBig_}Battle Fieldの設定エラー($str)。${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# 管理人によるプレゼントモード
sub presentMain {
	if (!$HpresentMode) {
		# 開放
		unlock();

		# テンプレート出力
		tempPresentPage();
	} else {
		# パスワードチェック
		if(checkSpecialPassword($HoldPassword)) {
			# 特殊パスワード

			if (!$HpresentMoney && !$HpresentFood) {
				# 金も食料もない
				tempPresentEmpty();
				unlock();
				return;
			}

			# idから島を取得
			$HcurrentNumber = $HidToNumber{$HcurrentID};
			my($island) = $Hislands[$HcurrentNumber];
			my($name)   = islandName($island);

			$island->{'money'} += $HpresentMoney;
			$island->{'money'} = 0 if ($island->{'money'} < 0);
			$island->{'food'}  += $HpresentFood;
			$island->{'food'} = 0 if ($island->{'food'} < 0);

			logPresent($HcurrentID, $name, $HpresentLog);

			# データ書き出し
			writeIslandsFile($HcurrentID);
			unlock();

			# 変更成功
			tempPresentOK($name);
		} else {
			# password間違い
			unlock();
			tempWrongPassword();
			return;
		}
	}
}


#----------------------------------------------------------------------
# プレゼントモードのトップページ
sub tempPresentPage {

    out(<<END);
<CENTER>$HtempBack</CENTER>
<H1>参加${AfterName}にプレゼントを贈る</H1>

<FORM action="$HthisFile" method="POST">
<B>プレゼントを受け取る${AfterName}は？</B><BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT><BR>
<BR>
<B>プレゼントの内容は？(マイナス値も可能)</B><BR>
<INPUT TYPE="text" NAME="PRESENTMONEY" VALUE="0" SIZE=16 MAXLENGTH=16>$HunitMoney<BR>
<INPUT TYPE="text" NAME="PRESENTFOOD"  VALUE="0" SIZE=16 MAXLENGTH=16>$HunitFood<BR>
<BR>
<B>ログメッセージは？(省略可能。先頭に${AfterName}名が挿入されます)</B><BR>
○○${AfterName}<INPUT TYPE="text" NAME="PRESENTLOG"  VALUE="" SIZE=128 MAXLENGTH=256><BR>
<BR>
<B>マスターパスワードは？</B><BR>
<INPUT TYPE="password" NAME="OLDPASS" VALUE="$HdefaultPassword" SIZE=32 MAXLENGTH=32><BR>
<INPUT TYPE="submit" VALUE="プレゼントを贈る" NAME="PresentButton"><BR>
</FORM>
END
}

#----------------------------------------------------------------------
# プレゼント完了
sub tempPresentOK {
    my ($name) = @_;
    out(<<END);
${HtagBig_}$name${AfterName}にプレゼントを贈りました${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# プレゼント内容がおかしい
sub tempPresentEmpty {
    out(<<END);
${HtagBig_}プレゼントの内容がおかしいようです${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# 管理人による制裁モード
sub punishMain {
	if(checkSpecialPassword($HdefaultPassword)) {
		# 特殊パスワード
		if ($HpunishMode) {
			my(%punish);
			if (open(Fpunish, "<${HdirName}/punish.dat")) {
				local(@_);
				while (<Fpunish>) {
					chomp;
					@_ = split(',');
					my($obj);
					$obj->{id} = shift;
					$obj->{punish} = shift;
					$obj->{x} = shift;
					$obj->{y} = shift;
					$punish{$obj->{id}} = $obj;
				}
				close(Fpunish);
			}

			if (open(Fpunish, ">${HdirName}/punish.dat")) {
				{
					my($obj);
					$obj->{id} = $HcurrentID;
					$obj->{punish} = $HpunishID;
					$obj->{x} = $HcommandX;
					$obj->{y} = $HcommandY;
					$punish{$obj->{id}} = $obj;
				}

				my($key, $obj);
				while (($key, $obj) = each %punish) {
					next if ($obj->{punish} == 0);
					print Fpunish
						$obj->{id} . ','.
						$obj->{punish} . ','.
						$obj->{x} . ','.
						$obj->{y} . "\n";
				}
				close(Fpunish);
			}
		}

		unlock();

		# テンプレート出力
		tempPunishPage();

	} else {
		# パスワードが一致しなければトップページへ
		require('./hako-top.cgi');
		unlock();
		# テンプレート出力
		tempTopPage();
	}
}

#----------------------------------------------------------------------
# 制裁モードのトップページ
sub tempPunishPage {
	my(@punishName) =
		(
		 'なし', # 0
		 '地震', # 1
		 '津波', # 2
		 '怪獣（人口条件クリア時のみ）', # 3
		 '地盤沈下（面積条件クリア時のみ）', # 4
		 '台風', # 5
		 '巨大隕石（座標指定）', # 6
		 '隕石', # 7
		 '噴火（座標指定）', # 8
		 );

	out(<<END);
<CENTER>$HtempBack</CENTER>
<H2>参加${AfterName}に制裁を加える</H2>

<UL>
    <LI>「ルールに違反した」と思う前に、「そのルールは誰もが読める場所に書いてあるか？」を確認しましょう。<br>
    <LI>制裁を加えるのはたやすいことですが、本当に管理人としての立場で行っているか考えましょう。<br>
    <LI>制裁を加えなければならないほど被害が大きいか考えましょう。軽い気持ちで攻撃する人はいつでもいるものです。<br>
    <LI><span class=attention>制裁の存在は極秘にしましょう。</span>制裁が明らかになると他のプレイヤーとの信頼関係も崩れます。<br>
</UL>

<FORM name="lcForm" action="$HthisFile" method="POST">
<INPUT TYPE="hidden" VALUE="$HdefaultPassword" NAME="Punish">
<B>制裁を加える${AfterName}は？</B><BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>
<INPUT TYPE="button" VALUE="マップを開く" onclick="printIsland();">
<BR><BR>
<B>座標は？（座標指定できる制裁でのみ有効）</B><BR>
<B>(</B><SELECT NAME=POINTX>
END

    my ($i);
    foreach $i (0..$islandSize) {
        if ($i == $HdefaultX) {
            out("<OPTION VALUE=$i SELECTED>$i\n");
        }
        else {
            out("<OPTION VALUE=$i>$i\n");
        }
    }

    out(<<END);
</SELECT><B>, </B><SELECT NAME=POINTY>
END

    foreach $i (0..$islandSize) {
        if ($i == $HdefaultY) {
            out("<OPTION VALUE=$i SELECTED>$i\n");
        } else {
            out("<OPTION VALUE=$i>$i\n");
        }
    }

    out(<<END);
</SELECT><B>)</B><BR>
<BR>
<B>制裁の内容は？</B><BR>
<SELECT NAME="PUNISHID">
<OPTION VALUE="0">$punishName[0]
<OPTION VALUE="1">$punishName[1]
<OPTION VALUE="2">$punishName[2]
<OPTION VALUE="3">$punishName[3]
<OPTION VALUE="4">$punishName[4]
<OPTION VALUE="5">$punishName[5]
<OPTION VALUE="6">$punishName[6]
<OPTION VALUE="7">$punishName[7]
<OPTION VALUE="8">$punishName[8]
</SELECT><BR>
<BR>
<INPUT TYPE="submit" VALUE="制裁を加える" NAME="PunishButton"><BR>
</FORM>
<SCRIPT Language="JavaScript">
<!--

function printIsland() {
  var iid;
  with (document.forms[0].elements[1]) {
    iid = options[selectedIndex].value;
  }
  window.open("$HthisFile?Sight=" + iid + "&ADMINMODE=1", "punish", "toolbar=0,location=0,directories=0,menubar=0,status=1,scrollbars=1,resizable=1,width=450,height=630");
}
//-->
</SCRIPT>
END

	if (open(Fpunish, "<${HdirName}/punish.dat")) {
		out('<HR>');
		out("<TABLE BORDER><TR><TH>${AfterName}名</TH><TH>制裁内容</TH><TH>座標</TH></TR>");
		local(@_);
		my($island);
		while (<Fpunish>) {
			chomp;
			@_ = split(',');
			my($obj);
			$obj->{id} = shift;
			$obj->{punish} = shift;
			$obj->{x} = shift;
			$obj->{y} = shift;

			$HcurrentNumber = $HidToNumber{$obj->{id}};
			$island = $Hislands[$HcurrentNumber];
			my $name = islandName($island);
			out("<TR><TD>${name}</TD><TD>$punishName[$obj->{punish}]</TD><TD>($obj->{x}, $obj->{y})</TD></TR>");
		}
		out('</TABLE>');
		close(Fpunish);
	}
}

#----------------------------------------------------------------------
# 管理人による地形変更モード
sub lchangeMain {
    if (checkSpecialPassword($HdefaultPassword)) {
        # 特殊パスワード
        if ($HlchangeMode) {
            # idから島を取得
            $HcurrentNumber = $HidToNumber{$HcurrentID};
            my ($island) = $Hislands[$HcurrentNumber];
            my ($land) = $island->{'land'};
            my ($landValue) = $island->{'landValue'};
            my ($landValue2) = $island->{'landValue2'};
            my ($landValue3) = $island->{'landValue3'};

			# 地形の値の整合性をチェック(チェックしたくない場合はコメントアウトして下さい)
#			if(!landCheck($HlchangeKIND, $HlchangeVALUE)) {
#				tempBadValue();
#				unlock();
#				return;
#			}

            $land->[$HcommandX][$HcommandY] = $HlchangeKIND;
            $landValue->[$HcommandX][$HcommandY] = $HlchangeVALUE;
            $landValue2->[$HcommandX][$HcommandY] = $HlchangeVALUE2;
            $landValue3->[$HcommandX][$HcommandY] = $HlchangeVALUE3;

			# データ書き出し
			writeIslandsFile($HcurrentID);
			unlock();

			# 変更成功
			tempLchangeOK(islandName($island));
		}
		unlock();
		# テンプレート出力
		tempLchangePage();
	} else {
		# パスワードが一致しなければトップページへ
		require('./hako-top.cgi');
		unlock();
		# テンプレート出力
		tempTopPage();
	}
}

#----------------------------------------------------------------------
# 地形変更モードのトップページ
sub tempLchangePage {
    require './init-server.cgi';
    out(<<END);
<CENTER>$HtempBack</CENTER>
<H1>参加${AfterName}の地形データを変更する</H1>

<DL>
<DT>・「地形の値」についての知識がなければ、使用は難しいかもしれません。</DT>
<DT>・特に「怪獣」については、知識があっても難しいと思います。<br>ちなみに、(地形の値)＝(怪獣の種類)×１６＋(怪獣の生命力)ですが、種類は３０まで生命力は１５までです。</DT>
<!---
<DT>・「地形」に対して<B>「地形の値」が適切であるかどうか簡易判定をしています</B>ので、注意してください。</DT>
--->
</DL><BR>

<FORM name='mcalc'>
<a HREF="JavaScript:void(0);" onClick='Mons_calc(); return 1;'>計算</a>
種類：<INPUT TYPE="text" SIZE=6 NAME="MONSKIND" VALUE="0">
体力：<INPUT TYPE="text" SIZE=6 NAME="MONSHP" VALUE="1">
答え：<INPUT TYPE="text" SIZE=6 NAME="MONS_VAL" VALUE="">
</form>
<BR><BR>
<FORM name="lcForm" action="$HthisFile" method="POST">
<INPUT TYPE="hidden" VALUE="$HdefaultPassword" NAME="Lchange">
<B>地形を変更する${AfterName}は？</B><BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>
<INPUT TYPE="button" VALUE="マップを開く" onclick="printIsland(); return 1;">
<BR><BR>
<B>座標は？</B><BR>
<B>(</B><SELECT NAME=POINTX>
END

	my($i);
	foreach $i (0..$islandSize) {
		if($i == $HdefaultX) {
			out("<OPTION VALUE=$i SELECTED>$i\n");
		} else {
			out("<OPTION VALUE=$i>$i\n");
		}
	}

	out(<<END);
</SELECT><B>, </B><SELECT NAME=POINTY>
END

	foreach $i (0..$islandSize) {
		if($i == $HdefaultY) {
			out("<OPTION VALUE=$i SELECTED>$i\n");
		} else {
			out("<OPTION VALUE=$i>$i\n");
		}
	}

	out(<<END);
</SELECT><B>)</B><BR>
<BR>
<B>地形は？</B><BR>
<SELECT NAME="LCHANGEKIND">
<OPTION VALUE="$HlandPlains">平地
<OPTION VALUE="$HlandSea">海
<OPTION VALUE="$HlandWaste">荒地
<OPTION VALUE="$HlandTown">町系
<OPTION VALUE="$HlandSunahama">砂浜
<OPTION VALUE="$HlandIce">氷河
<OPTION VALUE="$HlandForest">森
<OPTION VALUE="$HlandFarm">農場
<OPTION VALUE="$HlandInaka">いなか
<OPTION VALUE="$HlandFactory">工場
<OPTION VALUE="$HlandMonument">記念碑
<OPTION VALUE="$HlandDefence">防衛施設
<OPTION VALUE="$HlandMountain">山
<OPTION VALUE="$HlandMonster">怪獣
<OPTION VALUE="$HlandBettown">輝ける都市
<OPTION VALUE="$HlandNewtown">ニュータウン
<OPTION VALUE="$HlandBigtown">現代都市
<OPTION VALUE="$HlandSbase">海底基地
<OPTION VALUE="$HlandOil">海底油田
<OPTION VALUE="$HlandSeacity">海底都市
<OPTION VALUE="$HlandSeatown">海底新都市
<OPTION VALUE="$HlandUmicity">海都市
<OPTION VALUE="$HlandOilCity">油田都市
<OPTION VALUE="$HlandFrocity">海上都市
<OPTION VALUE="$HlandUmishuto">海底首都
<OPTION VALUE="$HlandPark">遊園地
<OPTION VALUE="$HlandInoraLand">いのらランド
<OPTION VALUE="$HlandMinato">港
<OPTION VALUE="$HlandFune">船舶
<OPTION VALUE="$HlandNursery">養殖場
<OPTION VALUE="$HlandKyujo"> 野球場
<OPTION VALUE="$HlandUmiamu"> 海あみゅ
<OPTION VALUE="$HlandFoodim">食物研究所
<OPTION VALUE="$HlandProcity">防災都市
<OPTION VALUE="$HlandGold">金山
<OPTION VALUE="$HlandSeki">関所
<OPTION VALUE="$HlandRottenSea">腐海
<OPTION VALUE="$HlandFarmchi">養鶏場
<OPTION VALUE="$HlandFarmpic">養豚場
<OPTION VALUE="$HlandFarmcow">牧場
<OPTION VALUE="$HlandCollege">大学
<OPTION VALUE="$HlandOnsen">温泉
<OPTION VALUE="$HlandHouse">島主の家
<OPTION VALUE="$HlandShuto">首都
<OPTION VALUE="$HlandRizort">リゾート地
<OPTION VALUE="$HlandKyujokai">多目的スタジアム
<OPTION VALUE="$HlandBigRizort">臨海リゾートホテル
<OPTION VALUE="$HlandHTFactory">ハイテク企業
<OPTION VALUE="$HlandSHTF">ハイテク企業・改
<OPTION VALUE="$HlandYakusho">島役所
<OPTION VALUE="$HlandMine">地雷
<OPTION VALUE="$HlandHaribote">ハリボテ
<OPTION VALUE="$HlandBase">ミサイル基地
<OPTION VALUE="$HlandKatorikun">豚の香取君
<OPTION VALUE="$HlandEgg">卵
<OPTION VALUE="$HlandHospital">病院
<OPTION VALUE="$HlandFiredept">消防署
<OPTION VALUE="$HlandOmamori">お守
<OPTION VALUE="$HlandRocket">ロケット
<OPTION VALUE="$HlandShrine">時の神殿
<OPTION VALUE="$HlandYougan">溶岩地帯
<OPTION VALUE="$HlandBigFood">たべもの
<OPTION VALUE="$HlandTrain">せんろ
<OPTION VALUE="$HlandStation">駅
<OPTION VALUE="$HlandZoo">動物園
<OPTION VALUE="$HlandBeachPark">海水浴場
<OPTION VALUE="$HlandGomi">ゴミおきば
<OPTION VALUE="$HlandGomiFactory">ゴミ処理場
<OPTION VALUE="$HlandBoueki">貿易
</SELECT><BR>
<BR>
<B>地形の値は？(LandValue)</B><BR>
<INPUT TYPE="text" SIZE="6" NAME="LCHANGEVALUE" VALUE="0"><BR>
<B>地形の値2は？(LandValue2)</B><BR>
<INPUT TYPE="text" SIZE="6" NAME="LCHANGEVALUE2" VALUE="0"><BR>
<B>地形の値3は？(LandValue3)</B><BR>
<INPUT TYPE="text" SIZE="6" NAME="LCHANGEVALUE3" VALUE="0"><BR>
<BR>
<INPUT TYPE="submit" VALUE="変更する" NAME="LchangeButton"><BR>
</FORM>
<SCRIPT Language="JavaScript">
<!--

function printIsland() {
	var iid;
	with (document.forms[1].elements[1]) {
		iid = options[selectedIndex].value;
	}
	window.open("$HthisFile?Sight=" + iid + "&ADMINMODE=1", "lcmap", "toolbar=0,location=0,directories=0,menubar=0,status=1,scrollbars=1,resizable=1,width=450,height=630");
}

function Mons_calc(){
  Kind = document.mcalc.MONSKIND.value;
  HP = document.mcalc.MONSHP.value;
  document.mcalc.MONS_VAL.value = (Kind << $Mons_Kind_Shift ) + (HP & $Mons_HP_MASK);
}

//-->
</SCRIPT>
END

    my ($l,$mkind);
    out("<TABLE BORDER><TR><TH>番号</TH><TH>怪獣</TH><TH>名前</TH><TH>体力</TH><TH>残骸の値段</TH><TH>経験値</TH></TR>");

    $mkind = 0;
    foreach $l (@HmonsterName) {
        out(<<END);
<TR><TD>$mkind</TD><TD><img src='./${HMapImgDir}$HmonsterImage[$mkind]'></TD><TD>$HmonsterName[$mkind]</TD><TD>$HmonsterBHP[$mkind]</TD><TD>$HmonsterValue[$mkind]</TD><TD>$HmonsterExp[$mkind]</TD></TR>
END
        $mkind++;
    }
    out('</TABLE>');

}

#----------------------------------------------------------------------
# 地形変更完了
sub tempLchangeOK {
	my($name) = @_;
	out(<<END);
${HtagBig_}$nameの地形を変更しました${H_tagBig}
<HR>
END
}

#----------------------------------------------------------------------
# 地形の値がおかしい
sub tempBadValue {
	out(<<END);
${HtagBig_}地形の値がおかしいようです${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# 地形の値をチェック
sub landCheck {
	my($land, $lv) = @_;
	if($land == $HlandSea) {
		return 0 if(($lv < 0) || ($lv > 1));
	} elsif($land == $HlandWaste) {
		return 0 if(($lv < 0) || ($lv > 1));
	} elsif($land == $HlandPlains) {
		return 0 if($lv != 0);
	} elsif($land == $HlandTown) {
		return 0 if(($lv < 1) || ($lv > 200));
	} elsif($land == $HlandProcity) {
		return 0 if(($lv < 1) || ($lv > 200));
	} elsif($land == $HlandNewtown) {
		return 0 if(($lv < 1) || ($lv > 300));
	} elsif($land == $HlandBigtown) {
		return 0 if(($lv < 1) || ($lv > 500));
	} elsif($land == $HlandSeatown) {
		return 0 if(($lv < 1) || ($lv > 400));
	} elsif($land == $HlandForest) {
		return 0 if(($lv < 1) || ($lv > 200));
	} elsif($land == $HlandFarm) {
		return 0 if(($lv < 10) || ($lv > 50));
#		return if(($lv - 10) % 2 != 0);
	} elsif($land == $HlandFoodim) {
		return 0 if(($lv < 30) || ($lv > 500));
#		return if(($lv - 30) % 10 != 0);
	} elsif($land == $HlandFarmchi) {
		return 0 if(($lv < 1) || ($lv > 4000));
	} elsif($land == $HlandFarmpic) {
		return 0 if(($lv < 1) || ($lv > 4000));
	} elsif($land == $HlandFarmcow) {
		return 0 if(($lv < 1) || ($lv > 4000));
	} elsif($land == $HlandFactory) {
		return 0 if(($lv < 30) || ($lv > 100));
#		return if(($lv - 30) % 10 != 0);
	} elsif($land == $HlandBase) {
		return 0 if(($lv < 0) || ($lv > $HmaxExpPoint));
	} elsif($land == $HlandDefence) {
		return 0 if($lv != 0);
	} elsif($land == $HlandMountain) {
		return 0 if(($lv < 0) || ($lv > 200));
#		return if($lv % 5 != 0);
	} elsif($land == $HlandGold) {
		return 0 if(($lv < 0) || ($lv > 200));
#		return if($lv % 5 != 0);
	} elsif($land == $HlandShrine) {
		return 0 if($lv != 0);
	} elsif($land == $HlandMonster) {
		my($kind, $name, $hp) = monsterSpec($lv);
		return 0 if(($hp < 0) || ($hp > 15) || ($kind < 0) || ($kind > 30));
	} elsif($land == $HlandSbase) {
		return 0 if(($lv < 0) || ($lv > $HmaxExpPoint));
	} elsif($land == $HlandSeacity) {
		return 0 if(($lv < 1) || ($lv > 200));
	} elsif($land == $HlandOil) {
		return 0 if($lv != 0);
	} elsif($land == $HlandMonument) {
		return 0 if(($lv < 0) || ($lv > 94));
	} elsif($land == $HlandHaribote) {
		return 0 if($lv != 0);
	} elsif($land == $HlandPark) {
		return 0 if(($lv < 10) || ($lv > 100));
#		return if(($lv - 10) % 30 != 0);
	} elsif($land == $HlandMinato) {
		return 0 if(($lv < 1) || ($lv > 200));
	} elsif($land == $HlandFune) {
		return 0 if(($lv < 1) || ($lv > 11));
	} elsif($land == $HlandMine) {
		return 0 if(($lv < 0) || ($lv > 9));
	} elsif($land == $HlandNursery) {
		return 0 if(($lv < 20) || ($lv > 100));
#		return if(($lv - 20) % 5 != 0);
	} elsif($land == $HlandKyujo) {
		return 0 if($lv != 0);
	} elsif($land == $HlandUmiamu) {
		return 0 if(($lv < 50) || ($lv > 1000));
#		return if(($lv - 50) % 30 != 0);
	} elsif($land == $HlandSeki) {
		return 0 if($lv != 0);
	} elsif($land == $HlandRottenSea) {
		return 0 if($lv != 1);
	}

	return 1;
}

#----------------------------------------------------------------------
# 管理人によるあずかりモード
sub preDeleteMain {
	if(checkSpecialPassword($HdefaultPassword)) {
		# 特殊パスワード
		if($HpreDeleteMode) {
			my @newID = ();
			my $flag = 0;
			foreach (@HpreDeleteID) {
				if(!(defined $HidToNumber{$_})) {
				} elsif($_ == $HcurrentID) {
					$flag = 1;
				} else {
					push(@newID, $_);
				}
			}
			@HpreDeleteID = @newID;
			push(@HpreDeleteID, $HcurrentID) if(!$flag);

			# データ書き出し
			writeIslandsFile($HcurrentID);
			unlock();
			if($flag) {
				tempPreDeleteEnd(islandName($Hislands[$HidToNumber{$HcurrentID}]));
			} else {
				tempPreDelete(islandName($Hislands[$HidToNumber{$HcurrentID}]));
			}
		}
		unlock();
		# テンプレート出力
		tempPdeleteMain();
	} else {
		# パスワードが一致しなければトップページへ
		require('./hako-top.cgi');
		unlock();
		# テンプレート出力
		tempTopPage();
	}
}

#----------------------------------------------------------------------
# あずかりモードのトップページ
sub tempPdeleteMain {

    out(<<END);
<CENTER>$HtempBack</CENTER>
<H1>参加${AfterName}を管理人あずかりにする</H1>

<DL>
<DT>・あずかりになった${AfterName}は、ターン処理(収入処理・コマンド処理・成長・災害・失業者移民)されなくなります。</DT>
<DT>・賞関係は処理されますし、他の${AfterName}からの攻撃はすべて受けつけてしまいます。</DT>
<DT>・あずかり中の島が「放棄」もしくは「強制削除」された場合、あずかりのＩＤデータは、次のあずかり処理を行うまでそのまま残ります。</DT>
</DL>

<FORM name="pdForm" action="$HthisFile" method="POST">
<INPUT TYPE="hidden" VALUE="$HdefaultPassword" NAME="Pdelete">
<B>管理人あずかりにする${AfterName}は？</B><BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>
<BR>
<INPUT TYPE="submit" VALUE="設定・解除" NAME="PdeleteButton"><BR>
</FORM>
<TABLE BORDER><TR><TH>あずかり中の${AfterName}</TH></TR>
END

    if ($HpreDeleteID[0] eq '') {
        out("<TR><TH>管理人あずかりの${AfterName}はありません！</TH></TR>");
    } else {
        my($name);
        foreach (@HpreDeleteID) {
            next if(!(defined $HidToNumber{$_}));
            $name = islandName($Hislands[$HidToNumber{$_}]);
            out("<TR><TD>$name</TD></TR>");
        }
    }
    out("</TABLE>");
}

#----------------------------------------------------------------------
# 管理人あずかり設定
sub tempPreDelete {
    my($name) = @_;

    out(<<END);
${HtagBig_}$name${AfterName}を管理人あずかりにしました${H_tagBig}
<HR>
END
}

#----------------------------------------------------------------------
# 管理人あずかり解除
sub tempPreDeleteEnd {
	my($name) = @_;
	out(<<END);
${HtagBig_}$name${AfterName}の管理人あずかりを解除しました${H_tagBig}
<HR>
END
}
#----------------------------------------------------------------------
# ログテンプレート
#----------------------------------------------------------------------
# 記録ログ
sub logHistory {
	open(HOUT, ">>${HdirName}/hakojima.his");
	print HOUT "$HislandTurn,$_[0]\n";
	close(HOUT);
}

#----------------------------------------------------------------------
# 発見
sub logDiscover {
	my($name) = @_;
	logHistory("${HtagName_}${name}${AfterName}${H_tagName}が発見される。");
}

#----------------------------------------------------------------------
# 島名の変更
sub logChangeName {
	my($name1, $name2) = @_;
	logHistory("${HtagName_}${name1}${AfterName}${H_tagName}、名称を${HtagName_}${name2}${AfterName}${H_tagName}に変更する。");
}

#----------------------------------------------------------------------
# オーナー名の変更
sub logChangeOwnerName {
	my($name1, $name2) = @_;
	logHistory("${HtagName_}${name1}${AfterName}${H_tagName}、オーナーを${HtagName_}${name2}${H_tagName}に変更する。");
}

#----------------------------------------------------------------------
# 不正アクセス
sub tempNewIslandillegal {
	out(<<END);
${HtagBig_}怪しいことはおやめくださいm(_ _)m${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# 島がいっぱいな場合
sub tempNewIslandFull {
	out(<<END);
${HtagBig_}申し訳ありません、${AfterName}が一杯で登録できません！！${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 新規で名前がない場合
sub tempNewIslandNoName {
	out(<<END);
${HtagBig_}${AfterName}につける名前が必要です。${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 新規で名前が不正な場合
sub tempNewIslandBadName {
	out(<<END);
${HtagBig_}',?()<>\$'とか入ってたり、「無人${AfterName}」「沈没${AfterName}」とかいった変な名前はやめましょうよ〜${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 新規でオーナー名が不正な場合
sub tempNewIslandBadOwnerName {
	out(<<END);
${HtagBig_}',?()<>\$'が入っている名前はやめましょう。${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# すでにその名前の島がある場合
sub tempNewIslandAlready {
	out(<<END);
${HtagBig_}その${AfterName}ならすでに発見されています。${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# パスワードがない場合
sub tempNewIslandNoPassword {
	out(<<END);
${HtagBig_}パスワードが必要です。${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 島を発見しました!!
sub tempNewIslandHead {
	out(<<END);
<CENTER>
${HtagBig_}${AfterName}を発見しました！！${H_tagBig}<BR>
${HtagBig_}${HtagName_}「${HcurrentName}${AfterName}」${H_tagName}と命名します。${H_tagBig}<BR>
コマンドの入力は、一度トップに戻って、「開発しに行く」ボタンからどうぞ！<BR>
$HtempBack<BR>
</CENTER>
<!-- この SCRIPT は「島を発見した画面でマップをクリックするとエラーになる」バグの修正用 -->
<SCRIPT Language="JavaScript">
<!--
function ps(x, y) {
	return true;
}
//-->
</SCRIPT>
END
}


#----------------------------------------------------------------------
# 名前変更失敗
sub tempChangeNothing {
	out(<<END);
${HtagBig_}名前、パスワードともに空欄です${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 名前変更資金足りず
sub tempChangeNoMoney {
	out(<<END);
${HtagBig_}資金不足のため変更できません${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 名前変更成功
sub tempChange {
	out(<<END);
${HtagBig_}変更完了しました${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 強制削除ログ
sub logDeleteIsland {
	my($id, $name) = @_;
#	logHistory("${HtagName_}${name}${H_tagName}、<B>管理人権限により</B><span class=attention>退場</span>となる。");
#	logHistory("${HtagName_}${name}${H_tagName}に、突然<B>天罰が降り</B>あっというまに<span class=attention>海に沈没し</span>跡形もなくなりました。");
	logHistory("${HtagName_}${name}${H_tagName}は、海神の<B>怒りに触れ</B>陸地はすべて<span class=attention>沈没しました。</span>");
}


#----------------------------------------------------------------------
# 島の強制削除(スペシャルモード)
sub tempDeleteIsland {
	my($name) = @_;
	out(<<END);
${HtagBig_}${name}を強制削除しました。${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# プレゼント
sub logPresent {
	my($id, $name, $log) = @_;
	logHistory("${HtagName_}${name}島${H_tagName}$log") if ($log ne '');
}

1;

