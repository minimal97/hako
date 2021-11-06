#----------------------------------------------------------------------
# Ȣ����� ver2.20
# �رĲ��̺����⥸�塼��(���ζ�˴���ꥸ�ʥ�)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
# Ȣ�����Υڡ���: http://t.pos.to/hako/
#----------------------------------------------------------------------
# �����ζ�˴�� ver1.0.0 by ������ http://t.pos.to/ozzy/
# ���Ѿ���Ȣ�����˽ऺ�롥�ܤ�������°��readme.txt�ե�����򻲾�
#----------------------------------------------------------------------
#                            ���ζ�˴ 2nd
#                                 v1.0
#                     by ���� webgame@oyoyo.ne.jp
#                   http://www.oyoyo.ne.jp/webgame/
#������������������������������������������������������������������������
#                           ���ζ�˴ ����
#                                 v1.2
#                     by ���� webgame@oyoyo.ne.jp
#                   http://www.oyoyo.ne.jp/webgame/
#������������������������������������������������������������������������

#----------------------------------------------------------------------
# �رĲ���
#----------------------------------------------------------------------
# �ᥤ��
sub campMain {
    my ($bbswrite) = @_;  # 1�ǽ񤭹���

    if ($bbswrite == 1) {

        campbbswrite();
    }

    $HcurrentCamp = $Hally[$HidToAllyNumber{$HcurrentCampID}];

    # �ѥ����
    if ($HcampPassward ne $HcurrentCamp->{'Takayan'}) {

        tempWrongPassword();        # password�ְ㤤
        unlock ();                  # ����
        return;
    }

    tempPrintCampHead (); # ��������
    campAllIslandsInfo(); # �رĤ�°�������ξ���
    camp_comment();
    campLbbsContents();
    # ����
    unlock ();
}

#----------------------------------------------------------------------
# �ƥ�ץ졼�Ȥ���¾
#----------------------------------------------------------------------

# �����ر� ��������
sub tempPrintCampHead {
    out(<<END);
<div align='center'>
  $HtempBack<br><br>
  <h1>${HtagName_}��<font color="$HcurrentCamp->{'color'}"><b>$HcurrentCamp->{'mark'}</b></font>$HcurrentCamp->{'name'}��${H_tagName} ��������</h1><br>
�رĥѥ���ɡ���<b>$HcurrentCamp->{'Takayan'}</b>��<br><br>
END

    out(<<END) if ($HallyBbs);
<a style="text-decoration:none" href="javascript:void(0)" onClick="document.allyForm.action='${HbaseDir}/${HallyBbsScript}';document.allyForm.submit();return false;">
  <h1><small>${HtagName_}<font color="$HcurrentCamp->{'color'}"><b>$HcurrentCamp->{'mark'}</b></font>$HcurrentCamp->{'name'}${H_tagName}�����ļ���</small></h1>
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
    islandJamp(1);   # ��ΰ�ư
    out('<hr>');
    campLbbsInputOW();
    out('</div>');
}


#----------------------------------------------------------------------
# ������Ǽ�������
sub campLbbsContents {

    out(<<END);

<table border>
  <tr>
    <th>�ֹ�</th>
    <th>��Ģ����</th>
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
                            $speaker = "($sName$AfterName)��$wallyName";
                        }
                    }
                    else {

                        my ($wally) = $HidToAllyNumber{$bbsmsg[1]};
                        my ($fromally) = $Hally[$wally];
                        my ($wallyName) = "<font color=\"$fromally->{'color'}\"><b>$fromally->{'mark'}</b></font>$fromally->{'name'}";
                        $speaker = "($sName$AfterName��$wallyName)";
                    }
                }
                else {

                    $speaker = "($sName$AfterName)";
                }
            }

            out(<<END);
  <tr>
    <td align='center'>$HtagNumber_$bbslinecnt$H_tagNumber</td>
    <td>$HtagLbbsSS_$bbsmsg[5]��$bbsmsg[3] �� $Hmsgtemp<span class='lbbsST'><b><small>$speaker</small></b></span>$H_tagLbbsSS</td>
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
# ������Ǽ������ϥե����� owner mode��
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
    # out("<b>��</b>̾�����ѹ����Ƥ��ͭ��̾���Ȥ��ޤ���");

    out(<<END);
  <table border>
    <tr>
      <th>̾��<small>(����${HlengthLbbsName}���ޤ�)</small></th>
      <th colspan="2">����<small>(����${HlengthLbbsMessage}���ޤ�)</small></th>
    </tr>
    <tr>
      <td><input type="text" size="32" maxlength="32" name="LBBSNAME" readonly="readonly" value="$HdefaultName"></td>
      <td colspan="2"><input type="text" size="80" name="LBBSMESSAGE"></td>
    </tr>
    <tr>
      <th>�ѥ����</th>
      <th colspan="2">ư��</th>
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
        <input type="submit" value="�񤭹���" NAME="CAMPCHAT=${HcurrentCampID}">
      </td>
      <td align="right">
<!-- input type="submit" value="�������" name="LbbsButtonDL$HcurrentID"-->
($HallyTopName�Τ�)�ɤ�Ʊ���˸����ơ�
        <select name="SENDALLY" $alistread>
$allyList
        </select>
        <input type="hidden" name="dummy" value="">
      </td>
    </tr>
  </table>
  <left>
    <input type="submit" value="�����" name="camp=${HcurrentCampID}">
  </left>
</form>
END
}


#----------------------------------------------------------------------
# ��Υ��ޥ���ɤ߹���(�رĲ��̺�����)
sub readCommands {

    my ($id) = @_;
    my (@command);
    my ($line);

    open(IIN, "${HdirName}/${id}.${HsubData}");
    foreach $y (0..$islandSize) {
        $line = <IIN>; # �ΤƤ�     �ޥåץǡ���
    }
    $line = <IIN>; # �ΤƤ�      ����ʪ�ǡ���

    # ���ޥ��
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

    # ���ޥ�ɤΤ��֤�
    return \@command,
}


#----------------------------------------------------------------------
# �����ɽ��
sub campAllIslandsInfo {

    # �ơ��֥�إå��ν񤭽Ф�
    campTableHeader();

    # �رĤ�°������Υ��ޥ�ɤΤ��ɤ߽Ф�
    {
        my ($id);
        foreach $id (@{ $HcurrentCamp->{'memberId'} }) {
            $Hislands[$HidToNumber{$id}]->{'command'} = readCommands($id);
        }
    }

    # ����ξ���񤭽Ф�
    {
        my ($i);
        foreach $i (0..$islandNumber) {
            if ($HcurrentCampID == $Hislands[$i]->{'allyId'}[0]) {
                campIslandInfo($Hislands[$i], $i+1-$HbfieldNumber); # �رĤ�°������Τ�
            }
        }
    }
    # �ơ��֥�եå��ν񤭽Ф�
    campTableFooter();

}


#----------------------------------------------------------------------
sub campIslandInfo {
    my ($island, $rank) = @_;

    # ����ɽ��
    my ($id) = $island->{'id'};
    my ($name) = islandName($island);
    my ($farm) = $island->{'farm'};
    my ($factory) = $island->{'factory'};
    my ($factoryHT) = $island->{'factoryHT'};
    my ($mountain) = $island->{'mountain'};
    my ($contribution) = int($island->{'ext'}[1] / 10); # �׸���
    $farm = ($farm == 0) ? "��ͭ����" : "${farm}0$HunitPop";
    $factory = ($factory == 0) ? "��ͭ����" : "${factory}0$HunitPop";
    $mountain = ($mountain == 0) ? "��ͭ����" : "${mountain}0$HunitPop";

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
      <th $HbgTitleCell>${HtagTH_}���${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}${AfterName}${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}�͸�${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}�׸�${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}���${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}����${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}����${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}���쵬��${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}���쵬��${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}HT����${H_tagTH}</th>
      <th $HbgTitleCell>${HtagTH_}�η��쵬��${H_tagTH}</th>
    </tr>
END
}

#----------------------------------------------------------------------
# Ʊ�� BBS
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
