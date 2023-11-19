# ����ˤ� -uRAniwa-: http://snow.prohosting.com/awinokah/
#----------------------------------------------------------------------
# Ȣ����� ver2.30
# ������Ǽ��ĥ⥸�塼��(ver1.00)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
#����������������������������������������������������������������������
#                             Ȣ����� 2nd
#                                 v1.5
#                            Ȣ����� ����
#                                 v1.3
#                    by ���� webgame@oyoyo.ne.jp
#                   http://www.oyoyo.ne.jp/webgame/
#����������������������������������������������������������������������
#----------------------------------------------------------------------
# ������Ǽ��ĥ⡼��
#----------------------------------------------------------------------
# �ᥤ��
sub localBbsMain {
    # id�������ֹ�����
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];

    # �إå�����
    tempHeader() if ($HjavaMode ne 'java' && $HlbbsMode < 5);

    # �ʤ��������礬�ʤ����
    if ($HcurrentNumber eq '') {
        unlock();
        tempProblem();
        return;
    }

    # ����⡼�ɤ���ʤ���̾������å��������ʤ����
    if (   ($HlbbsMode < 2)
        || ($HlbbsMode == 5) ) {

        if (   ($HlbbsName eq '')
            || ($HlbbsMessage eq '')) {

            tempHeader() if ($HlbbsMode == 5);
            unlock();
            tempLbbsNoMessage();
            return;
        }
    }

    my ($speaker);
    my ($lbbs);
    $lbbs = $island->{'lbbs'};

    # �Ѹ��ԥ⡼�ɤ���ʤ����ϥѥ���ɥ����å�
    if ($HlbbsMode % 2 == 1) {
        if (!checkPassword($island,$HinputPassword)) {
            # password�ְ㤤
            tempHeader() if ($HlbbsMode == 5 || $HlbbsMode == 7);
            unlock();
            tempWrongPassword();
            return;
        }

        # �����ʡ�̾������
        # $HlbbsName = $island->{'owner'};
    }
    elsif ($HlbbsMode == 0) {
        # �Ѹ��ԥ⡼��
        my ($sIsland);

        if ($HlbbsType ne 'ANON') {
            # �����ȶ���

            # id�������ֹ�����
            my ($number) = $HidToNumber{$HspeakerID};
            $sIsland = $Hislands[$number];

            # �ʤ��������礬�ʤ����
            if ($number eq '') {
                unlock();
                tempProblem();
                return;
            }

            # �ѥ���ɥ����å�
            if (!checkPassword($sIsland,$HinputPassword)) {
                # password�ְ㤤
                unlock();
                tempWrongPassword();
                return;
            }

            # �����ʡ�̾������
            # $HlbbsName = $sIsland->{'owner'};

            # �̿����Ѥ�ʧ��
            my ($cost) = ($HlbbsType eq 'PUBLIC') ? $HlbbsMoneyPublic : $HlbbsMoneySecret;
            if ($sIsland->{'money'} < $cost) {
                # ������­
                unlock();
                tempLbbsNoMoney();
                return;
            }
            $sIsland->{'money'} -= $cost;
        }

        # ȯ���Ԥ򵭲�����
        if ($HlbbsType ne 'ANON') {
            # �����ȶ���
            my ($name) = islandName($sIsland);
            $speaker = $name . ',' . $HspeakerID;
        }
        else {
            # ƿ̾
            $speaker = $ENV{'REMOTE_HOST'};
            $speaker = $ENV{'REMOTE_ADDR'} if ($speaker eq '');
        }
    }
    elsif ($HlbbsMode == 2) {
        # �Ѹ��Ժ���⡼��
        my ($sIsland);

        # id�������ֹ�����
        my ($number) = $HidToNumber{$HspeakerID};
        $sIsland = $Hislands[$number];

        # �ʤ��������礬�ʤ����
        if ($number eq '') {
            unlock();
            tempProblem();
            return;
        }

        # ID�����å�
        $lbbs->[$HcommandPlanNumber] =~ /[0-9]*\<.*,([0-9]*)\<[0-9]*\>.*\>.*$/;
        my ($wId) = $1;
        if ($wId != $HspeakerID) {
            # ID�ְ㤤
            unlock();
            tempWrong("���ʤ���ȯ���ǤϤ���ޤ���");
            return;
        }

        # �ѥ���ɥ����å�
        if (!checkPassword($sIsland,$HinputPassword)) {
            # password�ְ㤤
            unlock();
            tempWrongPassword();
            return;
        }
    }
    elsif ($HlbbsMode == 4) {
        # �Ѹ��Զ����̿���ǧ�⡼��
        my ($sIsland);

        # id�������ֹ�����
        my ($number) = $HidToNumber{$HspeakerID};
        $sIsland = $Hislands[$number];

        # �ʤ��������礬�ʤ����
        if ($number eq '') {
            unlock();
            tempProblem();
            return;
        }

        # �ѥ���ɥ����å�
        if (!checkPassword($sIsland,$HinputPassword)) {
            # password�ְ㤤
            unlock();
            tempWrongPassword();
            return;
        }
    }

    # �⡼�ɤ�ʬ��
    if ($HlbbsMode == 4) {
        printIslandMain();
        return;
    }
    elsif (   ($HlbbsMode == 2)
           || ($HlbbsMode == 3)
           || ($HlbbsMode == 7) ) {
        # ����⡼��
        if (   ($HlbbsMode == 3 || $HlbbsMode == 7)
            && ($HcommandPlanNumber == LBBS_MAX)) {
			foreach (0..($HlbbsMax - 1)) {
				$lbbs->[$_] = '0<<0>>';
			}
		}
        else {
            # ��å����������ˤ��餹
            slideBackLbbsMessage($lbbs, $HcommandPlanNumber);
        }
        tempLbbsDelete() if ($HlbbsMode != 7);
    }
    else {
        # ��Ģ�⡼��
        $speaker = "������,0" if ($HlbbsMode == 5);
        if ($HlbbsType ne 'SECRET') {
            # ������ƿ̾
            $speaker = "0<$speaker";
        }
        else {
            # ����
            $speaker = "1<$speaker";
        }
        # ��å���������ˤ��餹
        slideLbbsMessage($lbbs);

        # ��å������񤭹���
        my ($message);
        if ($HlbbsMode == 1) {
            $message = '1';
        }
        else {
            $message = '0';
        }
        $HlbbsName = "$HislandTurn��" . htmlEscape($HlbbsName);
        $HlbbsMessage = htmlEscape($HlbbsMessage);
        $lbbs->[0] = "$speaker<$message>$HlbbsName>$HlbbsMessage";

        tempLbbsAdd() if ($HlbbsMode != 5);
    }

    # �ǡ����񤭽Ф�
    writeIslandsFile($HcurrentID);

    # ��ȤΥ⡼�ɤ�
    if ($HlbbsMode % 2 == 0) {

        printIslandMain();
    }
    elsif (   ($HlbbsMode == 5)
           || ($HlbbsMode == 7) ) {

        tempHeader() if ($jumpTug !~ /location/);
        print $jumpTug;
        unlock();
        exit;
    }
    else {

        ownerMain();
    }
}

#----------------------------------------------------------------------
# ������Ǽ��ĤΥ�å��������ĸ��ˤ��餹
sub slideLbbsMessage {
    my ($lbbs) = @_;

    pop(@$lbbs);
    unshift(@$lbbs, $lbbs->[0]);
}


#----------------------------------------------------------------------
# ������Ǽ��ĤΥ�å������������ˤ��餹
sub slideBackLbbsMessage {
    my ($lbbs, $number) = @_;

    splice(@$lbbs, $number, 1);
    $lbbs->[$HlbbsMax - 1] = '0<<0>>';
}


#----------------------------------------------------------------------
# �ƥ�ץ졼�Ȥ���¾
#----------------------------------------------------------------------
sub tempLbbsMain {
    my ($mode) = @_;

    out('<div id="localBBS" align="center">');
    tempLbbsHead();     # ������Ǽ���
    out('</div>');
    out('  <div id="localBBS" align="left">');
    # �񤭹��ߥե�����
    if ($mode) {
        tempLbbsInputOW();
    }
    else {
        tempLbbsInput();
    }
    tempLbbsContents(); # �Ǽ�������
    out('</div>');
}


#----------------------------------------------------------------------
# ������Ǽ���
sub tempLbbsHead {
    out(<<END);
<hr>
${HtagBig_}<span class='Nret'>${HtagName_}${HcurrentName}${H_tagName}</span><span class='Nret'>�Ѹ����̿�</span>${H_tagBig}<br>
END
}


#----------------------------------------------------------------------
# ������Ǽ������ϥե�����
sub tempLbbsInput {
    out(<<END);
<form action="$HthisFile" method="POST">
END
    if ($HlbbsMoneyPublic + $HlbbsMoneySecret > 0) {
        # ȯ����ͭ��
        out('<div align="center"><b>��</b>');
        out("�����̿���<b>$HlbbsMoneyPublic$HunitMoney</b>�Ǥ���") if ($HlbbsMoneyPublic > 0);
        out("�����̿���<b>$HlbbsMoneySecret$HunitMoney</b>�Ǥ���") if ($HlbbsMoneySecret > 0);
        out('</div>');
    }
    my $col = ' colspan=2' if(!$HlbbsAnon);

    # out("<b>��</b>${AfterName}����äƤ�������̾�����ѹ����Ƥ��ͭ��̾���Ȥ��ޤ���");

    out(<<END);
  <table border>
    <tr>
      <th>̾��<small>(����${HlengthLbbsName}���ޤ�)</small></th>
      <th $col>����<small>(����${HlengthLbbsMessage}���ޤ�)</small></th>
      <th>�̿���ˡ</th>
    </tr>
    <tr>
      <td>
        <input type="text" size="30" MAXLENGTH="30" name="LBBSNAME" value="$HdefaultName">
      </td>
      <td $col>
        <input type="text" size="70" name="LBBSMESSAGE">
      </td>
      <td>
        <input type="radio" name="LBBSTYPE" value="PUBLIC" checked>����<br>
        <input type="radio" name="LBBSTYPE" value="SECRET">����
      </td>
    </tr>
    <tr>
      <th>�ѥ����</th>
      <th>${AfterName}̾</th>
      <th $col>ư��</th>
    </tr>
    <tr>
      <td>
        <input type="password" size="16" maxlength='16' name="PASSWORD" value="$HdefaultPassword">
      </td>
      <td>
        <select name="ISLANDID2">$HislandList</select>
END
    out(<<END) if ($HlbbsAnon);
        <input type="radio" name="LBBSTYPE" value="ANON">�Ѹ���
END

    out(<<END);
      </td>
      <td>
        <div align='center'>
          <input type="submit" value="��Ģ����" name="LbbsButtonSS$HcurrentID">
          <input type="submit" value="�����ǧ" name="LbbsButtonCK$HcurrentID">
        </div>
      </td>
END
    if (!$HlbbsAnon) {
        out(<<END);
      <td align="right">
�ֹ�
        <select name="NUMBER">
END
        {
            # ȯ���ֹ�
            my ($j, $i);
            for($i = 0; $i < $HlbbsMax; $i++) {
                $j = $i + 1;
                out("<option value=$i>$j\n");
            }
        }
        out(<<END);
        </select><br>
        <input type="submit" value="���" name="LbbsButtonDS$HcurrentID">
      </td>
END
    }
    out(<<END);
    </tr>
  </table>
</form>
END
}

#----------------------------------------------------------------------
# ������Ǽ������ϥե����� owner mode��
sub tempLbbsInputOW {

    out(<<END);
<form action="$HthisFile" method="POST">
<input type="hidden" name="JAVAMODE" value="$HjavaMode">
<table border>
  <tr>
    <th>̾��<small>(����${HlengthLbbsName}���ޤ�)</small></th>
    <th colspan="2">����<small>(����${HlengthLbbsMessage}���ޤ�)</small></th>
  </tr>
  <tr>
    <td><input type="text" size="32" maxlength="32" name="LBBSNAME" value="$HdefaultName"></td>
    <td colspan="2"><input type="text" SIZE="80" name="LBBSMESSAGE"></td>
  </tr>
  <tr>
    <th>�ѥ����</th>
    <th colspan="2">ư��</th>
  </tr>
  <tr>
    <td><input type="password" size="16" maxlength="16" name="PASSWORD" value="$HdefaultPassword"></td>
    <td align="right">
      <input type="submit" value="��Ģ����" name="LbbsButtonOW$HcurrentID">
    </td>
    <td align="right">
�ֹ�
      <select name="NUMBER">
END
    {
        # ȯ���ֹ�
        my ($j, $i);
    	for($i = 0; $i < $HlbbsMax; $i++) {
            $j = $i + 1;
            out("<OPTION VALUE=$i>$j\n");
        }
    	out("<OPTION VALUE=$HlbbsMax>��\n");
    }
    out(<<END);
      </select>
      <input type="submit" value="�������" name="LbbsButtonDL$HcurrentID">
    </td>
  </tr>
</table>
</form>
END
}

#----------------------------------------------------------------------
# ������Ǽ�������
sub tempLbbsContents {
    my ($lbbs, $line);
    $lbbs = $Hislands[$HcurrentNumber]->{'lbbs'};
    out(<<END);
<table border>
  <tr>
    <th>�ֹ�</th>
    <th>��Ģ����</th>
  </tr>
END

    my ($i , $j);
    my ($speaker);
    my ($sNo);
    my ($sName, $sID);

    for ($i = 0; $i < $HlbbsMax; $i++) {
        $line = $lbbs->[$i];
        if ($line =~ /([0-9]*)\<(.*)\<([0-9]*)\>(.*)\>(.*)$/) {
            $j = $i + 1;
            out("<tr><td align='center'>$HtagNumber_$j$H_tagNumber</td>");

#           $speaker = "<span class='lbbsST'><B><SMALL>($2)</SMALL></B></span>" if ($HlbbsSpeaker && ($2 ne ''));
            ($sName, $sID) = split(/,/, $2);
            $sNo = $HidToNumber{$sID} if (defined $sID);
            $speaker = '';
            if (   ($HlbbsSpeaker)
                && ($sName)) {

                if (defined $sNo) {
                    $speaker = "\n      <span class='lbbsST'><b><small>(<a style=\"text-decoration:none\" href=\"$HthisFile?Sight=$sID\">$sName</a>)</small></b></span>\n";
                }
                else {
                    $speaker = "\n      <span class='lbbsST'><b><small>($sName)</small></b></span>\n";
                }
            }
            out("    <td>\n");
            if ($3 == 0) {
                # �Ѹ���
                if ($1 == 0) {
                    # ����
                    out("      $HtagLbbsSS_$4 &gt; $5$H_tagLbbsSS $speaker\n");
                }
                else {
                    # ����
                    if (   ($HmainMode ne 'owner')
                        && (($HspeakerID eq '') || ($sID != $HspeakerID))) {
                        # �Ѹ���
                        out("<div class='t_center'><span class='lbbsST'>- ���� -</span></div>");
                    }
                    else {
                        # �����ʡ�
                        out("      $HtagLbbsSS_$4 &gt;(��) $5$H_tagLbbsSS $speaker\n");
                    }
                }
            }
            else {
                # ���
                out("      $HtagLbbsOW_$4 &gt; $5$H_tagLbbsOW $speaker\n");
            }
            out(<<END);
    </td>
  </tr>
END
        }
    }

    out(<<END);
</table>
END
}

#----------------------------------------------------------------------
# ������Ǽ��Ĥ�̾������å��������ʤ����
sub tempLbbsNoMessage {
    out(<<END);
${HtagBig_}̾���ޤ������Ƥ��󤬶���Ǥ���${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# �񤭤��ߺ��
sub tempLbbsDelete {
    out(<<END);
${HtagBig_}��Ģ���Ƥ������ޤ�����${H_tagBig}<hr>
END
}

#----------------------------------------------------------------------
# ���ޥ����Ͽ
sub tempLbbsAdd {
    out(<<END);
${HtagBig_}��Ģ��Ԥ��ޤ�����${H_tagBig}<hr>
END
}

#----------------------------------------------------------------------
# �̿����­�ꤺ
sub tempLbbsNoMoney {
    out(<<END);
${HtagBig_}�����­�Τ��ᵭĢ�Ǥ��ޤ���${H_tagBig}$HtempBack
END
}

1;
