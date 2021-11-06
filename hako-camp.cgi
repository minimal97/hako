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

        tempWrongPassword();        # password間違い
        unlock ();                  # 開放
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
<div align='center'>
  $HtempBack<br><br>
  <h1>${HtagName_}「<font color="$HcurrentCamp->{'color'}"><b>$HcurrentCamp->{'mark'}</b></font>$HcurrentCamp->{'name'}」${H_tagName} 作戦本部</h1><br>
陣営パスワード：『<b>$HcurrentCamp->{'Takayan'}</b>』<br><br>
END

    out(<<END) if ($HallyBbs);
<a style="text-decoration:none" href="javascript:void(0)" onClick="document.allyForm.action='${HbaseDir}/${HallyBbsScript}';document.allyForm.submit();return false;">
  <h1><small>${HtagName_}<font color="$HcurrentCamp->{'color'}"><b>$HcurrentCamp->{'mark'}</b></font>$HcurrentCamp->{'name'}${H_tagName}作戦会議室へ</small></h1>
</a>
<form name="allyForm" action="" method="POST" target="_blank">
  <input type="hidden" name="ally" value="$HcurrentCampID">
  <input type="hidden" name="cpass" value="$HcurrentCamp->{'password'}">
  <input type="hidden" name="jpass" value="$HcampPassward">
  <input type="hidden" name="id" value="$HcurrentID">
</form>
END

out(<<END);
$Hislands[$HidToNumber{$HcurrentID}]->{'ally_turn'}
</div>
END
}


#----------------------------------------------------------------------
sub camp_comment {

    local ($Hbbsislandname);

    $HdefaultName = $Hislands[$HidToNumber{$HcurrentID}]->{'onm'};
    $Hbbsislandname = $Hislands[$HidToNumber{$HcurrentID}]->{'name'};
    out(<<END);
<div id='localBBS'>
  <hr>
END
    require('./hako-map.cgi');
    islandJamp(1);   # 島の移動
    out('<hr>');
    campLbbsInputOW();
    out('</div>');
}


#----------------------------------------------------------------------
# ローカル掲示板内容
sub campLbbsContents {

    out(<<END);

<table border>
  <tr>
    <th>番号</th>
    <th>記帳内容</th>
  </tr>
END
    my ($Hmsgtemp);
    if (-e "$HallychatData$HcurrentCampID.cht") {

        open(DATAFILE, "< $HallychatData$HcurrentCampID.cht") or die("Error");
        my ($bbslinecnt) = 1;
        my ($bbsline);
        my (@bbsmsg);

        while ($bbsline = <DATAFILE>) {
            @bbsmsg = split(/\,/,$bbsline);
            #unshift(@lines, "$sendto,$HcurrentCampID,$HcurrentID,$HlbbsName,$HlbbsMessage,$Hlbbsturn,$Hlbbssendisland,\n");

            my ($sNo) = $HidToNumber{$bbsmsg[2]};
            my ($sName) = $bbsmsg[6];
            $Hmsgtemp = $bbsmsg[4];
            $Hmsgtemp = htmlEscape($Hmsgtemp);

            if ($bbsmsg[3] && ($sName ne '')) {

                if (defined $sNo) {

                    if ($HcurrentCampID == $bbsmsg[1]) {

                        if ($bbsmsg[1] == $bbsmsg[0]) {

                            $speaker = "($sName$AfterName)";
                        }
                        else {

                            my ($wally) = $HidToAllyNumber{$bbsmsg[0]};
                            my ($fromally) = $Hally[$wally];
                            my ($wallyName) = "<font color=\"$fromally->{'color'}\"><b>$fromally->{'mark'}</b></font>$fromally->{'name'}";
                            $speaker = "($sName$AfterName)＞$wallyName";
                        }
                    }
                    else {

                        my ($wally) = $HidToAllyNumber{$bbsmsg[1]};
                        my ($fromally) = $Hally[$wally];
                        my ($wallyName) = "<font color=\"$fromally->{'color'}\"><b>$fromally->{'mark'}</b></font>$fromally->{'name'}";
                        $speaker = "($sName$AfterName：$wallyName)";
                    }
                }
                else {

                    $speaker = "($sName$AfterName)";
                }
            }

            out(<<END);
  <tr>
    <td align='center'>$HtagNumber_$bbslinecnt$H_tagNumber</td>
    <td>$HtagLbbsSS_$bbsmsg[5]：$bbsmsg[3] ＞ $Hmsgtemp<span class='lbbsST'><b><small>$speaker</small></b></span>$H_tagLbbsSS</td>
  </tr>
END
            $bbslinecnt ++;
        }
    }
    else {
        out(<<END);
  <tr>
    <td>1</td>
    <td>-</td>
  </tr>
END
    }

    out(<<END);
</TD></TR></TABLE>
END
}


#----------------------------------------------------------------------
# ローカル掲示板入力フォーム owner mode用
sub campLbbsInputOW {

    my ($alistread);
    $alistread = '';
    $alistread = ' disabled' if ($HcurrentCampID != $HcurrentID);

    my ($allyname, $allyList);
    my ($max) = 201;
    if ($HallyNumber) {
        my ($s);
        foreach (0..$#Hally) {
            $s = '';
            $s = ' selected' if ($_ == $HidToAllyNumber{$HcurrentCampID});
            $allyList .= "<option value=\"$Hally[$_]->{'id'}\"$s>$Hally[$_]->{'name'}\n";
            $max = $Hally[$_]->{'id'} + 1 if ($max <= $Hally[$_]->{'id'});
        }
    }

    out(<<END);
<form action="$HthisFile" method="POST">
  <input type="hidden" name="JAVAMODE" value="$HjavaMode">
END
    # out("<b>※</b>名前を変更しても所有者名が使われます。");

    out(<<END);
  <table border>
    <tr>
      <th>名前<small>(全角${HlengthLbbsName}字まで)</small></th>
      <th colspan="2">内容<small>(全角${HlengthLbbsMessage}字まで)</small></th>
    </tr>
    <tr>
      <td><input type="text" size="32" maxlength="32" name="LBBSNAME" readonly="readonly" value="$HdefaultName"></td>
      <td colspan="2"><input type="text" size="80" name="LBBSMESSAGE"></td>
    </tr>
    <tr>
      <th>パスワード</th>
      <th colspan="2">動作</th>
    </tr>
    <tr>
      <td><input type="password" size="16" maxlength="16" name="PASSWORD" value="$HinputPassword"></td>
      <td align="right">
        <input type="hidden" name="ally" value="$HcurrentCampID">
        <input type="hidden" name="cpass" value="$HcurrentCamp->{'password'}">
        <input type="hidden" name="jpass" value="$HcampPassward">
        <input type="hidden" name="id" value="$HcurrentID">
        <input type="hidden" name="wturn" value="$HislandTurn">
        <input type="hidden" name="wislandname" value="$Hbbsislandname">
        <input type="submit" value="書き込む" NAME="CAMPCHAT=${HcurrentCampID}">
      </td>
      <td align="right">
<!-- input type="submit" value="削除する" name="LbbsButtonDL$HcurrentID"-->
($HallyTopNameのみ)どの同盟に向けて：
        <select name="SENDALLY" $alistread>
$allyList
        </select>
        <input type="hidden" name="dummy" value="">
      </td>
    </tr>
  </table>
  <left>
    <input type="submit" value="リロード" name="camp=${HcurrentCampID}">
  </left>
</form>
END
}


#----------------------------------------------------------------------
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
    my ($i);
    my ($cnum) = ($HcampCommandTurnNumber);

    for ($i = 0; $i < $cnum; $i++) {
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


#----------------------------------------------------------------------
# 情報の表示
sub campAllIslandsInfo {

    # テーブルヘッダの書き出し
    campTableHeader();

    # 陣営に属する島のコマンドのみ読み出し
    {
        my ($id);
        foreach $id (@{ $HcurrentCamp->{'memberId'} }) {
            $Hislands[$HidToNumber{$id}]->{'command'} = readCommands($id);
        }
    }

    # 各島の情報書き出し
    {
        my ($i);
        foreach $i (0..$islandNumber) {
            if ($HcurrentCampID == $Hislands[$i]->{'allyId'}[0]) {
                campIslandInfo($Hislands[$i], $i+1-$HbfieldNumber); # 陣営に属する島のみ
            }
        }
    }
    # テーブルフッタの書き出し
    campTableFooter();

}


#----------------------------------------------------------------------
sub campIslandInfo {
    my ($island, $rank) = @_;

    # 情報表示
    my ($id) = $island->{'id'};
    my ($name) = islandName($island);
    my ($farm) = $island->{'farm'};
    my ($factory) = $island->{'factory'};
    my ($factoryHT) = $island->{'factoryHT'};
    my ($mountain) = $island->{'mountain'};
    my ($contribution) = int($island->{'ext'}[1] / 10); # 貢献度
    $farm = ($farm == 0) ? "保有せず" : "${farm}0$HunitPop";
    $factory = ($factory == 0) ? "保有せず" : "${factory}0$HunitPop";
    $mountain = ($mountain == 0) ? "保有せず" : "${mountain}0$HunitPop";

    if ($island->{'absent'}  == 0) {
        $name = "${HtagName_}$name${H_tagName}";
    }
    else {
        $name = "${HtagName2_}$name($island->{'absent'})${H_tagName2}";
    }

    out(<<END);
    <tr>
      <td $HbgNumberCell rowspan="2" align="center">${HtagNumber_}$rank${H_tagNumber}</td>
      <td $HbgNameCell rowspan="2" align="left">
        <a style=\"text-decoration:none\" href="${HthisFile}?SightC=${id}" target="_blank">
          $name
        </a>
      </td>
      <td $HbgInfoCell align="right">$island->{'pop'}$HunitPop</td>
      <td $HbgInfoCell align="right">$contribution</td>
      <td $HbgInfoCell align="right">$island->{'money'}$HunitMoney</td>
      <td $HbgInfoCell align="right">$island->{'food'}$HunitFood</td>
      <td $HbgInfoCell align="right">$island->{'area'}$HunitArea</td>
      <td $HbgInfoCell align="right">${farm}</td>
      <td $HbgInfoCell align="right">${factory}</td>
      <td $HbgInfoCell align="right">${factoryHT}</td>
      <td $HbgInfoCell align="right">${mountain}</td>
    </tr>
    <tr>
      <td $HbgCommentCell colspan="9" valign="top">
        ${HtagTH_}
END

    my ($cnum) = ($HcampCommandTurnNumber);

    if ($Hislands[$HidToNumber{$HcurrentID}]->{'ally_turn'} < 5) {
        $cnum = 0;
    }

    {
        my ($command) = $island->{'command'};
        for ($i = 0; $i < $cnum; $i++) {
            tempCommand($i, $command->[$i], $island->{'shr'}, 0);
        }
    }
    out(<<END);
        ${H_tagTH}
      </td>
    </tr>
END
}


#----------------------------------------------------------------------
sub campTableHeader {

    out(<<END);
<div align='center'>
  <table border>
    <tr>
      <th $HbgTitleCell>${HtagTH_}順位${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}${AfterName}${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}人口${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}貢献${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}資金${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}食料${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}面積${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}農場規模${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}工場規模${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}HT規模${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}採掘場規模${H_tagTH}</th>
    </tr>
END
}

#----------------------------------------------------------------------
# 同盟 BBS
#----------------------------------------------------------------------
sub campbbswrite {

    my ($sendto) = ($HAnoSend) ? $HAnoSendto : $HcurrentCampID;

    if (1) {

        open(IN, "$HallychatData$sendto.cht");
        my (@lines) = <IN>;
        close(IN);
        while ($HAllylbbsMax <= @lines) { pop @lines; }

        unshift(@lines, "$sendto,$HcurrentCampID,$HcurrentID,$HlbbsName,$HlbbsMessage,$Hlbbsturn,$Hlbbssendisland,\n");

        if (open(OUT, ">$HallychatData$sendto.cht")) {

            foreach $line (@lines) {
                print OUT $line;
            }
            close(OUT);
        }
        else {
            tempProblem();
            return;
        }

        if ($sendto != $HcurrentCampID){
            open(IN, "$HallychatData$HcurrentCampID.cht");
            my (@lines) = <IN>;
            close(IN);
            while ($HAllylbbsMax <= @lines) { pop @lines; }
            unshift(@lines, "$sendto,$HcurrentCampID,$HcurrentID,$HlbbsName,$HlbbsMessage,$Hlbbsturn,$Hlbbssendisland,\n");
            if (open(OUT, ">$HallychatData$HcurrentCampID.cht")) {

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
}


#----------------------------------------------------------------------
sub campTableFooter {

    out(<<END);
  </table>
</div>
END
}

1;
