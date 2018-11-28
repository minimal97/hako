# ����ˤ� -uRAniwa-: http://snow.prohosting.com/awinokah/
#----------------------------------------------------------------------
# Ȣ����� ver2.30
# ������Ǽ��ĥ⥸�塼��(ver1.00)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
#������������������������������������������������������������������������
#							  Ȣ����� 2nd
#								  v1.5
#							 Ȣ����� ����
#								  v1.3
#					  by ���� webgame@oyoyo.ne.jp
#					http://www.oyoyo.ne.jp/webgame/
#������������������������������������������������������������������������
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
    if ($HlbbsMode < 2 || $HlbbsMode == 5) {
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
            tempHeader() if($HlbbsMode == 5 || $HlbbsMode == 7);
            unlock();
            tempWrongPassword();
            return;
        }

        # �����ʡ�̾������
        # $HlbbsName = $island->{'owner'};
    } elsif ($HlbbsMode == 0) {
        # �Ѹ��ԥ⡼��
        my($sIsland);

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
			my($cost) = ($HlbbsType eq 'PUBLIC') ? $HlbbsMoneyPublic : $HlbbsMoneySecret;
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
			my $name = islandName($sIsland);
			$speaker = $name . ',' . $HspeakerID;
		} else {
			# ƿ̾
			$speaker = $ENV{'REMOTE_HOST'};
			$speaker = $ENV{'REMOTE_ADDR'} if ($speaker eq '');
		}

	} elsif ($HlbbsMode == 2) {
		# �Ѹ��Ժ���⡼��
		my($sIsland);

		# id�������ֹ�����
		my($number) = $HidToNumber{$HspeakerID};
		$sIsland = $Hislands[$number];

		# �ʤ��������礬�ʤ����
		if($number eq '') {
			unlock();
			tempProblem();
			return;
		}

		# ID�����å�
		$lbbs->[$HcommandPlanNumber] =~ /[0-9]*\<.*,([0-9]*)\<[0-9]*\>.*\>.*$/;
		my $wId = $1;
		if($wId != $HspeakerID) {
			# ID�ְ㤤
			unlock();
			tempWrong("���ʤ���ȯ���ǤϤ���ޤ���");
			return;
		}

		# �ѥ���ɥ����å�
		if(!checkPassword($sIsland,$HinputPassword)) {
			# password�ְ㤤
			unlock();
			tempWrongPassword();
			return;
		}
	} elsif ($HlbbsMode == 4) {
		# �Ѹ��Զ����̿���ǧ�⡼��
		my($sIsland);

		# id�������ֹ�����
		my($number) = $HidToNumber{$HspeakerID};
		$sIsland = $Hislands[$number];

		# �ʤ��������礬�ʤ����
		if($number eq '') {
			unlock();
			tempProblem();
			return;
		}

		# �ѥ���ɥ����å�
		if(!checkPassword($sIsland,$HinputPassword)) {
			# password�ְ㤤
			unlock();
			tempWrongPassword();
			return;
		}
	}

	# �⡼�ɤ�ʬ��
	if($HlbbsMode == 4) {
		printIslandMain();
		return;
	} elsif($HlbbsMode == 2 || $HlbbsMode == 3 || $HlbbsMode == 7) {
		# ����⡼��
		if(($HlbbsMode == 3 || $HlbbsMode == 7) && ($HcommandPlanNumber == $HlbbsMax)) {
			foreach (0..($HlbbsMax - 1)) {
				$lbbs->[$_] = '0<<0>>';
			}
		} else {
			# ��å����������ˤ��餹
			slideBackLbbsMessage($lbbs, $HcommandPlanNumber);
		}
		tempLbbsDelete() if($HlbbsMode != 7);
	} else {
		# ��Ģ�⡼��
		$speaker = "������,0" if($HlbbsMode == 5);
		if ($HlbbsType ne 'SECRET') {
			# ������ƿ̾
			$speaker = "0<$speaker";
		} else {
			# ����
			$speaker = "1<$speaker";
		}
		# ��å���������ˤ��餹
		slideLbbsMessage($lbbs);

		# ��å������񤭹���
		my($message);
		if($HlbbsMode == 1) {
			$message = '1';
		} else {
			$message = '0';
		}
		$HlbbsName = "$HislandTurn��" . htmlEscape($HlbbsName);
		$HlbbsMessage = htmlEscape($HlbbsMessage);
		$lbbs->[0] = "$speaker<$message>$HlbbsName>$HlbbsMessage";

		tempLbbsAdd() if($HlbbsMode != 5);
	}

	# �ǡ����񤭽Ф�
	writeIslandsFile($HcurrentID);

	# ��ȤΥ⡼�ɤ�
	if($HlbbsMode % 2 == 0) {
		printIslandMain();
	} elsif($HlbbsMode == 5 || $HlbbsMode == 7) {
		tempHeader() if($jumpTug !~ /location/);
		print $jumpTug;
		unlock();
		exit;
	} else {
		ownerMain();
	}
}

#----------------------------------------------------------------------
# ������Ǽ��ĤΥ�å��������ĸ��ˤ��餹
sub slideLbbsMessage {
    my ($lbbs) = @_;

    my ($i);
    pop(@$lbbs);
    unshift(@$lbbs, $lbbs->[0]);
}


#----------------------------------------------------------------------
# ������Ǽ��ĤΥ�å������������ˤ��餹
sub slideBackLbbsMessage {
    my ($lbbs, $number) = @_;

    my ($i);
    splice(@$lbbs, $number, 1);
    $lbbs->[$HlbbsMax - 1] = '0<<0>>';
}


#----------------------------------------------------------------------
# �ƥ�ץ졼�Ȥ���¾
#----------------------------------------------------------------------
sub tempLbbsMain {
    my($mode) = @_;

    out('<DIV ID="localBBS">');
    tempLbbsHead();     # ������Ǽ���
    # �񤭹��ߥե�����
    if ($mode) {
        tempLbbsInputOW();
    } else {
        tempLbbsInput();
    }
    tempLbbsContents(); # �Ǽ�������
    out('</DIV>');
}


#----------------------------------------------------------------------
# ������Ǽ���
sub tempLbbsHead {
    out(<<END);
<HR>
${HtagBig_}<span class='Nret'>${HtagName_}${HcurrentName}${H_tagName}</span><span class='Nret'>�Ѹ����̿�</span>${H_tagBig}<BR>
END
}


#----------------------------------------------------------------------
# ������Ǽ������ϥե�����
sub tempLbbsInput {
    out(<<END);
<FORM action="$HthisFile" method="POST">
END
    if ($HlbbsMoneyPublic + $HlbbsMoneySecret > 0) {
        # ȯ����ͭ��
        out('<DIV align="center"><B>��</B>');
        out("�����̿���<B>$HlbbsMoneyPublic$HunitMoney</B>�Ǥ���") if ($HlbbsMoneyPublic > 0);
        out("�����̿���<B>$HlbbsMoneySecret$HunitMoney</B>�Ǥ���") if ($HlbbsMoneySecret > 0);
        out('</DIV>');
    }
    my $col = ' colspan=2' if(!$HlbbsAnon);

    # out("<B>��</B>${AfterName}����äƤ�������̾�����ѹ����Ƥ��ͭ��̾���Ȥ��ޤ���");

    out(<<END);
<TABLE BORDER>
<TR>
<TH>̾��<small>(����${HlengthLbbsName}���ޤ�)</small></TH>
<TH$col>����<small>(����${HlengthLbbsMessage}���ޤ�)</small></TH>
<TH>�̿���ˡ</TH>
</TR>
<TR>
<TD><INPUT type="text" size="30" MAXLENGTH="30" name="LBBSNAME" value="$HdefaultName"></TD>
<TD$col><INPUT type="text" SIZE="70" name="LBBSMESSAGE"></TD>
<TD>
<INPUT type="radio" name="LBBSTYPE" value="PUBLIC" CHECKED>����<br>
<INPUT type="radio" name="LBBSTYPE" value="SECRET">����
</TD>
</TR>
<TR>
<TH>�ѥ����</TH>
<TH>${AfterName}̾</TH>
<TH$col>ư��</TH>
</TR>
<TR>
<TD><INPUT type="password" size="16" MAXLENGTH=16 name="PASSWORD" value="$HdefaultPassword"></TD>
<TD>
<SELECT name="ISLANDID2">$HislandList</SELECT>
END
    out(<<END) if ($HlbbsAnon);
<INPUT type="radio" name="LBBSTYPE" value="ANON">�Ѹ���
END

    out(<<END);
</TD>
<TD><DIV align='center'>
<INPUT type="submit" value="��Ģ����" name="LbbsButtonSS$HcurrentID">
<INPUT type="submit" value="�����ǧ" name="LbbsButtonCK$HcurrentID">
</DIV></TD>
END
    if (!$HlbbsAnon) {
        out(<<END);
<TD align="right">
�ֹ�
<SELECT name="NUMBER">
END
        {
            # ȯ���ֹ�
            my($j, $i);
            for($i = 0; $i < $HlbbsMax; $i++) {
                $j = $i + 1;
                out("<OPTION value=$i>$j\n");
            }
        }
        out(<<END);
</SELECT><br>
<INPUT type="submit" value="���" name="LbbsButtonDS$HcurrentID">
</TD>
END
    }
    out(<<END);
</TR>
</TABLE>
</FORM>
END
}

#----------------------------------------------------------------------
# ������Ǽ������ϥե����� owner mode��
sub tempLbbsInputOW {

	out(<<END);
<FORM action="$HthisFile" method="POST">
<INPUT type="hidden" NAME=JAVAMODE value="$HjavaMode">
END
	# out("<B>��</B>̾�����ѹ����Ƥ��ͭ��̾���Ȥ��ޤ���");

	out(<<END);
<TABLE BORDER>
<TR>
<TH>̾��<small>(����${HlengthLbbsName}���ޤ�)</small></TH>
<TH COLSPAN=2>����<small>(����${HlengthLbbsMessage}���ޤ�)</small></TH>
</TR>
<TR>
<TD><INPUT type="text" SIZE="32" MAXLENGTH="32" NAME="LBBSNAME" value="$HdefaultName"></TD>
<TD COLSPAN=2><INPUT type="text" SIZE="80" NAME="LBBSMESSAGE"></TD>
</TR>
<TR>
<TH>�ѥ����</TH>
<TH COLSPAN=2>ư��</TH>
</TR>
<TR>
<TD><INPUT type="password" SIZE="16" MAXLENGTH="16" NAME="PASSWORD" value="$HdefaultPassword"></TD>
<TD align=right>
<INPUT type="submit" VALUE="��Ģ����" NAME="LbbsButtonOW$HcurrentID">
</TD>
<TD align=right>
�ֹ�
<SELECT NAME=NUMBER>
END
    {
    	# ȯ���ֹ�
    	my($j, $i);
    	for($i = 0; $i < $HlbbsMax; $i++) {
    		$j = $i + 1;
    		out("<OPTION VALUE=$i>$j\n");
    	}
    	out("<OPTION VALUE=$HlbbsMax>��\n");
    }
	out(<<END);
</SELECT>
<INPUT type="submit" VALUE="�������" NAME="LbbsButtonDL$HcurrentID">
</TD>
</TR>
</TABLE>
</FORM>
END
}

#----------------------------------------------------------------------
# ������Ǽ�������
sub tempLbbsContents {
    my ($lbbs, $line);
    $lbbs = $Hislands[$HcurrentNumber]->{'lbbs'};
    out(<<END);
<TABLE BORDER>
<TR>
<TH>�ֹ�</TH>
<TH>��Ģ����</TH>
</TR>
END

    my ($i , $j);
    my ($speaker);
    my ($sNo);
    my ($sName, $sID);

    for ($i = 0; $i < $HlbbsMax; $i++) {
        $line = $lbbs->[$i];
        if ($line =~ /([0-9]*)\<(.*)\<([0-9]*)\>(.*)\>(.*)$/) {
            $j = $i + 1;
            out("<TR><TD align='center'>$HtagNumber_$j$H_tagNumber</TD>");

#           $speaker = "<span class='lbbsST'><B><SMALL>($2)</SMALL></B></span>" if ($HlbbsSpeaker && ($2 ne ''));
            ($sName, $sID) = split(/,/, $2);
            $sNo = $HidToNumber{$sID} if (defined $sID);
            $speaker = '';
            if ($HlbbsSpeaker && ($sName)) {
                if(defined $sNo){
                    $speaker = "<span class='lbbsST'><B><SMALL>(<A STYlE=\"text-decoration:none\" HREF=\"$HthisFile?Sight=$sID\">$sName</A>)</SMALL></B></span>";
                } else {
                    $speaker = "<span class='lbbsST'><B><SMALL>($sName)</SMALL></B></span>";
                }
            }
            if ($3 == 0) {
                # �Ѹ���
                if ($1 == 0) {
                    # ����
                    out("<TD>$HtagLbbsSS_$4 > $5$H_tagLbbsSS $speaker</TD></TR>");
				} else {
					# ����
					if (($HmainMode ne 'owner') &&(($HspeakerID eq '') || ($sID != $HspeakerID))) {
						# �Ѹ���
						out("<TD><DIV align='center'><span class='lbbsST'>- ���� -</span></DIV></TD></TR>");
					} else {
						# �����ʡ�
						out("<TD>$HtagLbbsSS_$4 >(��) $5$H_tagLbbsSS $speaker</TD></TR>");
                    }
                }
            } else {
                # ���
                out("<TD>$HtagLbbsOW_$4 > $5$H_tagLbbsOW $speaker</TD></TR>");
            }
        }
    }

    out(<<END);
</TD></TR></TABLE>
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
${HtagBig_}��Ģ���Ƥ������ޤ�����${H_tagBig}<HR>
END
}

#----------------------------------------------------------------------
# ���ޥ����Ͽ
sub tempLbbsAdd {
    out(<<END);
${HtagBig_}��Ģ��Ԥ��ޤ�����${H_tagBig}<HR>
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
