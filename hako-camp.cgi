#----------------------------------------------------------------------
# 箱庭諸島 ver2.20
# 陣営画面作成モジュール(帝国の興亡オリジナル)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
# 箱庭諸島のページ: http://t.pos.to/hako/
#----------------------------------------------------------------------
# 「帝国の興亡」 ver1.0.0 by おじー http://t.pos.to/ozzy/
# 使用条件は箱庭諸島に準ずる．詳しくは付属のreadme.txtファイルを参照
#----------------------------------------------------------------------
#                            帝国の興亡 2nd
#                                 v1.0
#                     by 親方 webgame@oyoyo.ne.jp
#                   http://www.oyoyo.ne.jp/webgame/
#――――――――――――――――――――――――――――――――――――
#                           帝国の興亡 海戦
#                                 v1.2
#                     by 親方 webgame@oyoyo.ne.jp
#                   http://www.oyoyo.ne.jp/webgame/
#――――――――――――――――――――――――――――――――――――

#----------------------------------------------------------------------
# 陣営画面
#----------------------------------------------------------------------
# メイン
sub campMain {
    my ($bbswrite) = @_;  # 1で書き込み

    if ($bbswrite == 1) {

        campbbswrite();
    }

    $HcurrentCamp = $Hally[$HidToAllyNumber{$HcurrentCampID}];

    # パスワード
    if ($HcampPassward ne $HcurrentCamp->{'Takayan'}) {
        # password間違い
        tempWrongPassword();
        unlock ();      # 開放
        return;
    }

    tempPrintCampHead (); # 作戦本部
    campAllIslandsInfo(); # 陣営に属する諸島の情報
    camp_comment();
    campLbbsContents();
    # 開放
    unlock ();
}

#----------------------------------------------------------------------
# テンプレートその他
#----------------------------------------------------------------------

# ○○陣営 作戦本部
sub tempPrintCampHead {
    out(<<END);
<DIV align='center'>
$HtempBack<BR><BR>
${HtagBig_}${HtagName_}「<FONT COLOR="$HcurrentCamp->{'color'}"><B>$HcurrentCamp->{'mark'}</B></FONT>$HcurrentCamp->{'name'}」${H_tagName} 作戦本部${H_tagBig}<BR>
陣営パスワード：『<B>$HcurrentCamp->{'Takayan'}</B>』<BR><BR>
END

    out(<<END) if($HallyBbs);
<A STYlE="text-decoration:none" HREF="JavaScript:void(0)" onClick="document.allyForm.action='${HbaseDir}/${HallyBbsScript}';document.allyForm.submit();return false;">
${HtagBig_}<small>${HtagName_}<FONT COLOR="$HcurrentCamp->{'color'}"><B>$HcurrentCamp->{'mark'}</B></FONT>$HcurrentCamp->{'name'}${H_tagName}作戦会議室へ</A></small>${H_tagBig}
<FORM name="allyForm" action="" method="POST" target="_blank">
<INPUT type="hidden" name="ally" value="$HcurrentCampID">
<INPUT type="hidden" name="cpass" value="$HcurrentCamp->{'password'}">
<INPUT type="hidden" name="jpass" value="$HcampPassward">
<INPUT type="hidden" name="id" value="$HcurrentID">
</FORM>
END
    out("$Hislands[$HidToNumber{$HcurrentID}]->{'ally_turn'}");
    out('</DIV>');
}


sub camp_comment {

    local ( $Hbbsislandname  );

    $HdefaultName = $Hislands[$HidToNumber{$HcurrentID}]->{'onm'};
    $Hbbsislandname = $Hislands[$HidToNumber{$HcurrentID}]->{'name'};
    out("<DIV ID='localBBS'>");
    out('<hr>');
    require('./hako-map.cgi');
    islandJamp(1);   # 島の移動
    out('<hr>');
    campLbbsInputOW();
    out('</DIV>');
}

# ローカル掲示板内容
sub campLbbsContents {

    out(<<END);
<TABLE BORDER>
<TR>
 <TH>番号</TH>
 <TH>記帳内容</TH>
</TR>
END
    my ($Hmsgtemp);
    if (-e "$HallychatData$HcurrentCampID.cht") {

        open(DATAFILE, "< $HallychatData$HcurrentCampID.cht") or die("Error");
        my ($bbslinecnt) = 1;
        my ($bbsline);

        while ($bbsline = <DATAFILE>){
            @bbsmsg = split(/\,/,$bbsline);
            #unshift(@lines, "$sendto,$HcurrentCampID,$HcurrentID,$HlbbsName,$HlbbsMessage,$Hlbbsturn,$Hlbbssendisland,\n");

            my $sNo = $HidToNumber{$bbsmsg[2]};
            my $sName = $bbsmsg[6];
            $Hmsgtemp = $bbsmsg[4];
            $Hmsgtemp = htmlEscape($Hmsgtemp);

            if ($bbsmsg[3] && ($sName ne '')) {

                if (defined $sNo) {

                    if ( $HcurrentCampID == $bbsmsg[1] ) {

                        if ( $bbsmsg[1] == $bbsmsg[0] ) {
                            $speaker = "<span class='lbbsST'><B><SMALL>($sName$AfterName)</SMALL></B></span>";

                        }else{

                            my $wally = $HidToAllyNumber{$bbsmsg[0]};
                            my $fromally = $Hally[$wally];
                            my $wallyName = "<FONT COLOR=\"$fromally->{'color'}\"><B>$fromally->{'mark'}</B></FONT>$fromally->{'name'}";
                            $speaker = "<span class='lbbsST'><B><SMALL>($sName$AfterName)＞$wallyName</SMALL></B></span>";

                        }

                    }else{

                        my $wally = $HidToAllyNumber{$bbsmsg[1]};
                        my $fromally = $Hally[$wally];
                        my $wallyName = "<FONT COLOR=\"$fromally->{'color'}\"><B>$fromally->{'mark'}</B></FONT>$fromally->{'name'}";
                        $speaker = "<span class='lbbsST'><B><SMALL>($sName$AfterName：$wallyName)</SMALL></B></span>";
                    }

                } else {

                    $speaker = "<span class='lbbsST'><B><SMALL>($sName$AfterName)</SMALL></B></span>";
                }
            }

            out(<<END);
    <TR>
        <TD align=center>$HtagNumber_$bbslinecnt$H_tagNumber</TD>
        <TD>$HtagLbbsSS_$bbsmsg[5]：$bbsmsg[3] ＞ $Hmsgtemp$speaker$H_tagLbbsSS</TD>
    </TR>
END
        $bbslinecnt ++;
        }
    } else {
        out(<<END);
<TR>
    <TD>1</TD>
    <TD>-</TD>
</TR>
END

    }

    out(<<END);
</TD></TR></TABLE>
END
}


# ローカル掲示板入力フォーム owner mode用
sub campLbbsInputOW {
    my ($alistread);
            $alistread = '';
            $alistread = ' disabled' if ( $HcurrentCampID != $HcurrentID);

    my($allyname, $allyList);

    my ($max) = 201;
    if ($HallyNumber) {
        my ($s);
        foreach (0..$#Hally) {
            $s = '';
            $s = ' SELECTED' if($_ == $HidToAllyNumber{$HcurrentCampID});
            $allyList .= "<OPTION VALUE=\"$Hally[$_]->{'id'}\"$s>$Hally[$_]->{'name'}\n";
            $max = $Hally[$_]->{'id'} + 1 if($max <= $Hally[$_]->{'id'});
        }
    }

    out(<<END);
<FORM action="$HthisFile" method="POST">
<INPUT TYPE="hidden" NAME="JAVAMODE" VALUE="$HjavaMode">
END
    # out("<B>※</B>名前を変更しても所有者名が使われます。");


    out(<<END);
<TABLE BORDER>
<TR>
<TH>名前<small>(全角${HlengthLbbsName}字まで)</small></TH>
<TH COLSPAN=2>内容<small>(全角${HlengthLbbsMessage}字まで)</small></TH>
</TR>
<TR>
<TD><INPUT TYPE="text" SIZE="32" MAXLENGTH="32" NAME="LBBSNAME" readonly="readonly" VALUE="$HdefaultName"></TD>
<TD COLSPAN=2><INPUT TYPE="text" SIZE="80" NAME="LBBSMESSAGE"></TD>
</TR>
<TR>
<TH>パスワード</TH>
<TH COLSPAN=2>動作</TH>
</TR>
<TR>
<TD><INPUT TYPE="password" SIZE="16" MAXLENGTH="16" NAME="PASSWORD" VALUE="$HinputPassword"></TD>
<TD align=right>
<INPUT type="hidden" name="ally" value="$HcurrentCampID">
<INPUT type="hidden" name="cpass" value="$HcurrentCamp->{'password'}">
<INPUT type="hidden" name="jpass" value="$HcampPassward">
<INPUT type="hidden" name="id" value="$HcurrentID">
<INPUT type="hidden" name="wturn" value="$HislandTurn">
<INPUT type="hidden" name="wislandname" value="$Hbbsislandname">
<INPUT TYPE="submit" VALUE="書き込む" NAME="CAMPCHAT=${HcurrentCampID}">
</TD>
<TD align=right>
<!-- INPUT TYPE="submit" VALUE="削除する" NAME="LbbsButtonDL$HcurrentID"-->
($HallyTopNameのみ)どの同盟に向けて：
<SELECT NAME="SENDALLY" $alistread>
$allyList
</SELECT>
<INPUT type="hidden" name="dummy" value="">
</TD>
</TR>
</TABLE>
<LEFT><INPUT TYPE="submit" VALUE="リロード" NAME="camp=${HcurrentCampID}"></LEFT>
</FORM>
END
}

# 島のコマンド読み込み(陣営画面作成用)
sub readCommands {

	my ($id) = @_;
	my (@command);
    my ($line);

	open(IIN, "${HdirName}/${id}.${HsubData}");
	foreach $y (0..$islandSize) {
		$line = <IIN>; # 捨てる     マップデータ
	}
    $line = <IIN>; # 捨てる      持ち物データ

	# コマンド
	my($i);
	my($cnum) = ($HcampCommandTurnNumber);

	for($i = 0; $i < $cnum; $i++) {
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

	close(IIN);

	# コマンドのみ返す
	return \@command,
}

# 情報の表示
sub campAllIslandsInfo {

    # テーブルヘッダの書き出し
    campTableHeader();

    # 陣営に属する島のコマンドのみ読み出し
    my($id);
    foreach $id (@{ $HcurrentCamp->{'memberId'} }) {
        $Hislands[$HidToNumber{$id}]->{'command'} = readCommands($id);
    }

    # 各島の情報書き出し
    my ($i);
    foreach $i (0..$islandNumber) {
        if ($HcurrentCampID == $Hislands[$i]->{'allyId'}[0]) {
            campIslandInfo($Hislands[$i], $i+1-$HbfieldNumber); # 陣営に属する島のみ
        }
    }
    # テーブルフッタの書き出し
    campTableFooter();

}

sub campIslandInfo {

	my($island, $rank) = @_;

	# 情報表示
	my($id) = $island->{'id'};
	my($name) = islandName($island);
	my($farm) = $island->{'farm'};
	my($factory) = $island->{'factory'};
	my($factoryHT) = $island->{'factoryHT'};
	my($mountain) = $island->{'mountain'};
	my($contribution) = int($island->{'ext'}[1] / 10); # 貢献度
	$farm = ($farm == 0) ? "保有せず" : "${farm}0$HunitPop";
	$factory = ($factory == 0) ? "保有せず" : "${factory}0$HunitPop";
	$mountain = ($mountain == 0) ? "保有せず" : "${mountain}0$HunitPop";

	if($island->{'absent'}  == 0) {
		$name = "${HtagName_}$name${H_tagName}";
	} else {
		$name = "${HtagName2_}$name($island->{'absent'})${H_tagName2}";
	}

	out(<<END);
<TR>
<TD $HbgNumberCell ROWSPAN=2 align=center>${HtagNumber_}$rank${H_tagNumber}</TD>
<TD $HbgNameCell ROWSPAN=2 align=left>

<A STYlE=\"text-decoration:none\" HREF="${HthisFile}?SightC=${id}" target="_blank">
$name
</A>
</TD>
<TD $HbgInfoCell align=right>$island->{'pop'}$HunitPop</TD>
<TD $HbgInfoCell align=right>$contribution</TD>
<TD $HbgInfoCell align=right>$island->{'money'}$HunitMoney</TD>
<TD $HbgInfoCell align=right>$island->{'food'}$HunitFood</TD>
<TD $HbgInfoCell align=right>$island->{'area'}$HunitArea</TD>
<TD $HbgInfoCell align=right>${farm}</TD>
<TD $HbgInfoCell align=right>${factory}</TD>
<TD $HbgInfoCell align=right>${factoryHT}</TD>
<TD $HbgInfoCell align=right>${mountain}</TD>
</TR>
END

	out("<TR><TD $HbgCommentCell COLSPAN=9 valign=top>${HtagTH_}\n");
	my($cnum) = ($HcampCommandTurnNumber);

    if ($Hislands[$HidToNumber{$HcurrentID}]->{'ally_turn'} < 5) {
        $cnum = 0;
    }

    my($command) = $island->{'command'};
	for($i = 0; $i < $cnum; $i++) {
		tempCommand($i, $command->[$i], $island->{'shr'}, 0);
	}
}

sub campTableHeader {
	out(<<END);

<DIV align='center'>
<TABLE BORDER>
<TR>
<TH $HbgTitleCell>${HtagTH_}順位${H_tagTH}</TH>
<TH $HbgTitleCell>${HtagTH_}${AfterName}${H_tagTH}</TH>
<TH $HbgTitleCell>${HtagTH_}人口${H_tagTH}</TH>
<TH $HbgTitleCell>${HtagTH_}貢献${H_tagTH}</TH>
<TH $HbgTitleCell>${HtagTH_}資金${H_tagTH}</TH>
<TH $HbgTitleCell>${HtagTH_}食料${H_tagTH}</TH>
<TH $HbgTitleCell>${HtagTH_}面積${H_tagTH}</TH>
<TH $HbgTitleCell>${HtagTH_}農場規模${H_tagTH}</TH>
<TH $HbgTitleCell>${HtagTH_}工場規模${H_tagTH}</TH>
<TH $HbgTitleCell>${HtagTH_}HT規模${H_tagTH}</TH>
<TH $HbgTitleCell>${HtagTH_}採掘場規模${H_tagTH}</TH>
</TR>
END
}

#----------------------------------------------------------------------
# 同盟 BBS
#----------------------------------------------------------------------
sub campbbswrite {

    my $sendto = $HcurrentCampID;

    if ( $HAnoSend ) {

        $sendto = $HAnoSendto;
    }

    if ( 1 ) {
    	my @lines;

    	open(IN, "$HallychatData$sendto.cht");
    	my @lines = <IN>;
    	close(IN);
    	while ($HAllylbbsMax <= @lines) { pop @lines; }

    	unshift(@lines, "$sendto,$HcurrentCampID,$HcurrentID,$HlbbsName,$HlbbsMessage,$Hlbbsturn,$Hlbbssendisland,\n");

    	if(open(OUT, ">$HallychatData$sendto.cht")){
    		foreach $line (@lines) {
    			print OUT $line;
    		}
    		close(OUT);
    	} else {
    		tempProblem();
    		return;
    	}

        if ($sendto != $HcurrentCampID){
            open(IN, "$HallychatData$HcurrentCampID.cht");
            my @lines = <IN>;
            close(IN);
            while ($HAllylbbsMax <= @lines) { pop @lines; }
            unshift(@lines, "$sendto,$HcurrentCampID,$HcurrentID,$HlbbsName,$HlbbsMessage,$Hlbbsturn,$Hlbbssendisland,\n");
        	if(open(OUT, ">$HallychatData$HcurrentCampID.cht")){
        		foreach $line (@lines) {
        			print OUT $line;
        		}
        		close(OUT);
            } else {
                tempProblem();
                return;
            }
        }



    }

}


#----------------------------------------------------------------------
sub campTableFooter {
	out(<<END);

</TABLE>
</DIV>
END
}

1;
