#----------------------------------------------------------------------
# Ȣ����� ver2.30
# ���������⥸�塼��(ver1.00)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
#----------------------------------------------------------------------

# ����5�إå����κ�ɸ
#  ����0�إå����ޤ�Ĵ�������硢0���ܤΥǡ����ޤǤ�Ĵ�٤�
#  ����1�إå����ޤ�Ĵ�������硢6���ܤΥǡ����ޤǤ�Ĵ�٤�
#  ����2�إå����ޤ�Ĵ�������硢18���ܤΥǡ����ޤǤ�Ĵ�٤�
#  ����3�إå����ޤ�Ĵ�������硢36���ܤΥǡ����ޤǤ�Ĵ�٤�
#  ����4�إå����ޤ�Ĵ�������硢60���ܤΥǡ����ޤǤ�Ĵ�٤�
#  ����5�إå����ޤ�Ĵ�������硢90���ܤΥǡ����ޤǤ�Ĵ�٤�
# ��˼���2�إå����ޤ�Ĵ��(1���ܡ�18���ܤΥǡ�����Ĵ��)
#  for($i = 1; $i <= 18; $i++) {	 # �濴($x,$y)��ޤޤ�
#     $sx = $x + $ax[$i];
#     $sy = $y + $ay[$i];
#     # Y����������(HEX�ޥåפʤΤ�ɬ��)
#     $sy-- if((($sy % 2) == 0) && (($y % 2) == 1));
#     next if(($sx < 0) || ($sx > $islandSize)
#          || ($sy < 0) || ($sy > $islandSize));
#     if($land->[$sx][$sy] == $HlandSea) { # ����
#         ....ά....
#     }
#  }
require './hako-const.cgi';
require './hako-ally.cgi';
require './server_config.pm';


#----------------------------------------------------------------------
# ��ο��������⡼��
#----------------------------------------------------------------------
# �ᥤ��
sub newIslandMain {
    # ������������������å�
    if ($HadminJoinOnly) {
        unless($ENV{HTTP_REFERER}  =~ /^$HthisFile/) {
            unlock();
            tempHeader();
            tempNewIslandillegal();
            return;
        }
    }

    # ̾�������뤫�����å�
    if ($HcurrentName eq '') {
        unlock();
        tempHeader();
        tempNewIslandNoName();
        return;
    }

    # ̾���������������å�
    if ($HcurrentName =~ /[,\?\(\)\<\>\$]|^̵��|^����$/) {
        # �Ȥ��ʤ�̾��
        unlock();
        tempHeader();
        tempNewIslandBadName();
        return;
    }

    # ̾���ν�ʣ�����å�
    if (nameToNumber($HcurrentName) != -1) {
        # ���Ǥ�ȯ������
        unlock();
        tempHeader();
        tempNewIslandAlready();
        return;
    }

    # password��¸��Ƚ��
    if ($HinputPassword eq '') {
        # password̵��
        unlock();
        tempHeader();
        tempNewIslandNoPassword();
        return;
    }

    # ��ǧ�ѥѥ����
    if ($HinputPassword2 ne $HinputPassword) {
        # password�ְ㤤
        unlock();
        tempHeader();
        tempWrongPassword();
        return;
    }

    # ����������ֹ�����
    $HcurrentNumber = $HislandNumber;
    $HislandNumber++;
    $islandNumber++;
    $Hislands[$HcurrentNumber] = makeNewIsland();
    my ($island) = $Hislands[$HcurrentNumber];

    # ID�λȤ���
    my ($safety) = 0;
    while (defined $HidToNumber{$HislandNextID}) {
        $HislandNextID ++;
        $HislandNextID = 1 if($HislandNextID > 100);
        $safety++;
        last if($safety == 100);
    }

    # �Ƽ���ͤ�����
    $island->{'name'} = $HcurrentName;
    $island->{'id'} = $HislandNextID;
    $island->{'landscore'} = 0;
    $HislandNextID ++;
    $HislandNextID = 1 if($HislandNextID > 100);
    $island->{'absent'} = $HgiveupTurn - 6;
    $island->{'BF_Flag'} = 0;
	$island->{'comment'} = '(̤��Ͽ)';
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
    # �͸�����¾����
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

    # �ǡ����񤭽Ф�
    writeIslandsFile($island->{'id'});
    logDiscover($HcurrentName); # ��

    $HcurrentID = $HislandNextID - 1;
    $HmainMode = 'owner';
    $HjavaMode = 'java';
    # COOKIE����
    cookieOutput();

    # ����
    unlock();

    # ȯ������
    tempHeader();
    tempNewIslandHead($HcurrentName); # ȯ�����ޤ���!!
    foreach (0..$HcurrentNumber) {
        if ($Hislands[$_]->{'id'} == $island->{'id'}) {
            $HcurrentNumber = $_;
            last;
        }
    }
    axeslog() if($HtopAxes >= 1);
    islandInfo(); # ��ξ���
    islandMap(1); # ����Ͽޡ�owner�⡼��
}

# ����������������
sub makeNewIsland {
    # �Ϸ�����
    my ($land, $landValue) = makeNewLand();

    # ������ޥ�ɤ�����
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

    # ����Ǽ��Ĥ����
    my (@lbbs);
    for ($i = 0; $i < LBBS_MAX; $i++) {
        $lbbs[$i] = "0<<0>>";
    }

    # ��ˤ����֤�
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

# ����������Ϸ����������
sub makeNewLand {
    # ���ܷ������
    my (@land, @landValue, $x, $y, $i);

    # ���˽����
    foreach $y (0..$islandSize) {
        foreach $x (0..$islandSize) {
            $land[$x][$y] = $HlandSea;
            $landValue[$x][$y] = 0;
        }
    }

    # �����4*4�˹��Ϥ�����
    my ($center) = ISLAND_SIZE / 2 - 1;
    for ($y = $center - 1; $y < $center + 3; $y++) {
        for ($x = $center - 1; $x < $center + 3; $x++) {
            $land[$x][$y] = $HlandWaste;
        }
    }

    # 8*8�ϰ����Φ�Ϥ�����
    for ($i = 0; $i < 120; $i++) {
        # �������ɸ
        $x = random(8) + $center - 3;
        $y = random(8) + $center - 3;

        if (countAround(\@land, $x, $y, 7, $HlandSea) != 7){
            # �����Φ�Ϥ������硢�����ˤ���
            # �����Ϲ��Ϥˤ���
            # ���Ϥ�ʿ�Ϥˤ���
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

    # ������
    my ($count) = 0;
    while ($count < 4) {
        # �������ɸ
        $x = random(4) + $center - 1;
        $y = random(4) + $center - 1;

        # ���������Ǥ˿��Ǥʤ���С�������
        if ($land[$x][$y] != $HlandForest) {
            $land[$x][$y] = $HlandForest;
            $landValue[$x][$y] = 5; # �ǽ��500��
            $count++;
        }
    }

    # Į����
    $count = 0;
    while ($count < 2) {
        # �������ɸ
        $x = random(4) + $center - 1;
        $y = random(4) + $center - 1;

        # ����������Į�Ǥʤ���С�Į����
        if (   ($land[$x][$y] != $HlandTown)
            && ($land[$x][$y] != $HlandForest)) {
            $land[$x][$y] = $HlandTown;
            $landValue[$x][$y] = 5; # �ǽ��500��
            $count++;
        }
    }

    # ������
    $count = 0;
    while ($count < 1) {
        # �������ɸ
        $x = random(4) + $center - 1;
        $y = random(4) + $center - 1;

        # ����������Į�Ǥʤ���С�Į����
        if (($land[$x][$y] != $HlandTown) &&
           ($land[$x][$y] != $HlandForest)) {
            $land[$x][$y] = $HlandMountain;
            $landValue[$x][$y] = 0; # �ǽ�Ϻη���ʤ�
            $count++;
        }
    }

    # ���Ϥ���
    $count = 0;
    while ($count < 1) {
        # �������ɸ
        $x = random(4) + $center - 1;
        $y = random(4) + $center - 1;

        # ����������Į�����Ǥʤ���С�����
        if ( ($land[$x][$y] != $HlandTown) &&
             ($land[$x][$y] != $HlandForest) &&
             ($land[$x][$y] != $HlandMountain) ) {

            $land[$x][$y] = $HlandBase;
            $landValue[$x][$y] = 0;
            $count++;
        }
    }

	return (\@land, \@landValue) if(!$HeasyMode);

	# �˥塼���������
	$count = 0;
	while($count < 1) {
		# �������ɸ
		$x = random(4) + $center - 1;
		$y = random(4) + $center - 1;

		# ����������Į�����Ǥʤ���С�����
		if(($land[$x][$y] != $HlandTown) &&
			($land[$x][$y] != $HlandForest) &&
			($land[$x][$y] != $HlandBase) &&
			($land[$x][$y] != $HlandMountain)) {
			$land[$x][$y] = $HlandNewtown;
			$landValue[$x][$y] = 10;
			$count++;
		}
	}

	# ��ؤ���
	$count = 0;
	while($count < 1) {
		# �������ɸ
		$x = random(4) + $center - 1;
		$y = random(4) + $center - 1;

		# ����������Į�����Ǥʤ���С�����
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

    # ������
    $count = 0;
    while ($count < 1) {
        # �������ɸ
        $x = random(4) + $center - 1;
        $y = random(4) + $center - 1;

        # �����Φ�����뤫�����å�
        my ($seaCount) =	countAround($land, $x, $y, 7, $HlandSea);
        if ($seaCount != 0) {
            # ����������Į�����Ǥʤ���С�����
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
# �����ѹ��⡼��
#----------------------------------------------------------------------
# �ᥤ��
sub changeMain {
    # id����������
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];
    my ($flag) = 0;

    # �ѥ���ɥ����å�
    if (checkSpecialPassword($HoldPassword)) {
        # �ü�ѥ����
        if ($HcurrentName =~ /^��$/) {
            # �Ƕ�ν������������
            logPrintHtml();
            unlock();
            tempChange();
            return;
        } elsif($HcurrentName =~ /^̵��$/) {
            # �����⡼��
            deleteIsland(1);
            return;
		} elsif($HcurrentName =~ /^����$/) {
			# �����⡼��
			deleteIsland(0);
			return;
		} elsif(!checkMasterPassword($HoldPassword)) {
			# ����/���max�⡼��
			$island->{'money'} = $HmaximumMoney;
			$island->{'food'}  = $HmaximumFood;
		}
	} elsif(!checkPassword($island,$HoldPassword)) {
		# password�ְ㤤
		unlock();
		tempWrongPassword();
		return;
	}

	# ��ǧ�ѥѥ����
	if($HinputPassword2 ne $HinputPassword) {
		# password�ְ㤤
		unlock();
		tempWrongPassword();
		return;
	}

	if($HcurrentName ne '') {
		# ��̾�ѹ��ξ��
		# ��̾�������������å�
		if($HcurrentName =~ /[,\?\(\)\<\>\$]|^̵��|^����$/) {
			# �Ȥ��ʤ�̾��
			unlock();
			tempNewIslandBadName();
			return;
		}

		# ̾���ν�ʣ�����å�
		if(nameToNumber($HcurrentName) != -1) {
			# ���Ǥ�ȯ������
			unlock();
			tempNewIslandAlready();
			return;
		}

		if($island->{'money'} < $HcostChangeName) {
			# �⤬­��ʤ�
			unlock();
			tempChangeNoMoney();
			return;
		}

		# ���
		unless(checkSpecialPassword($HoldPassword)) {
			$island->{'money'} -= $HcostChangeName;
		}

		# ̾�����ѹ�
		logChangeName($island->{'name'}, $HcurrentName);
		$island->{'name'} = $HcurrentName;
		$flag = 1;
	}

	if ($HcurrentOwnerName ne '') {
		# �����ʡ�̾�ѹ��ξ��
		# �����ʡ�̾�������������å�
		if($HcurrentOwnerName =~ /[,\?\(\)\<\>\$]/) {
			# �Ȥ��ʤ�̾��
			unlock();
			tempNewIslandBadOwnerName();
			return;
		}

		if($island->{'money'} < $HcostChangeName) {
			# �⤬­��ʤ�
			unlock();
			tempChangeNoMoney();
			return;
		}

		# ���
		unless(checkSpecialPassword($HoldPassword)) {
			$island->{'money'} -= $HcostChangeName;
		}

		# �����ʡ�̾���ѹ�
		logChangeOwnerName($island->{'name'}, $HcurrentOwnerName);
		$island->{'onm'} = $HcurrentOwnerName;
		$flag = 1;
	}

	# password�ѹ��ξ��
	if($HinputPassword ne '') {
		# �ѥ���ɤ��ѹ�
		$island->{'password'} = encode($HinputPassword);
		$flag = 1;
	}

	if(($flag == 0) && !checkSpecialPassword($HoldPassword)) {
		# �ɤ�����ѹ�����Ƥ��ʤ�
		unlock();
		tempChangeNothing();
		return;
	}

	# �ǡ����񤭽Ф�
	writeIslandsFile($HcurrentID);
	unlock();

	# �ѹ�����
	tempChange();
}

# ���̾�������ֹ������(ID����ʤ����ֹ�)
sub nameToNumber {
	my($name) = @_;

	# ���礫��õ��
	my($i);
	foreach $i (0..$islandNumber) {
		if($Hislands[$i]->{'name'} eq $name) {
			return $i;
		}
	}

	# ���Ĥ���ʤ��ä����
	return -1;
}


#----------------------------------------------------------------------
# �ȣԣͣ�����
#----------------------------------------------------------------------
sub logPrintHtml {
	my($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) = gmtime(time + $Hjst);
	$mon++;
	my($sss) = "${mon}��${date}�� ${hour}��${min}ʬ${sec}��";

	$html1=<<_HEADER_;
<HTML><HEAD>
<TITLE>
�Ƕ�ν����
</TITLE>
<BASE HREF="$htmlDir/">
<link rel="stylesheet" type="text/css" href="${efileDir}/$HcssFile">
</HEAD>
<BODY $htmlBody><DIV ID='BodySpecial'>
<DIV ID='RecentlyLog'>
<H1>�Ƕ�ν����</H1>
<FORM>
�ǿ���������$sss����
<INPUT TYPE="button" VALUE=" ���ɹ���" onClick="location.reload()">
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

			# ��̩�ط�
			if($m) {
				next if(!$mode || ($id1 != $id)); # ��̩ɽ�������ʤ�
				$m = '<B>(��̩)</B>';
			} else {
				$m = '';
			}

			# ɽ��Ū�Τ�
			if($id) {
				next if(($id != $id1) && ($id != $id2));
			}

			# ɽ��
			if(!$set_turn){
				if(!$Hseason) {
					$html2 .= "<B>=====[<span class=number><FONT SIZE=4> ������$turn </FONT></span>]================================================</B><BR>\n";
				} else {
					# �����ɽ��
					my @seasonName = ('<span class=winter>��</span>','<span class=spring>��</span>','<span class=summer>��</span>','<span class=autumn>��</span>');
					my $month = ($turn % 12) + 1;
					my $year  = ($turn / 12) + 1;
					my $calender = sprintf('<span class=month><FONT SIZE=2><small>%s</small> %dǯ %d�� </FONT></span>' , $Halmanac, $year, $month);
					$calender .= "<span class='season'>$seasonName[int(($month - 1) / 3)]</span>";
					$html2 .= "<B>=====[<span class=number><FONT SIZE=4> <small>������$turn</small> </FONT></span>]=============================$calender</B><BR>\n";
				}
				$set_turn++;
			}
			$html2 .= "${HtagNumber_}��${H_tagNumber}:$message<BR>\n";
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
# �ᥤ��
sub bfpointMain {

	# ����
	unlock();

    my $bfpoint;

	my @HCislands = @Hislands;
	my @idx = (0..$#Hislands);
	@idx = sort { $Hislands[$b]->{'landscore'} <=> $Hislands[$a]->{'landscore'} ||
                 $b <=> $a } @idx;

	@HCislands = @HCislands[@idx];

	out(<<END);
<CENTER>$HtempBack</CENTER><BR>
<H1>Battle Field �Υ롼��(�ޤ���꤫��)</H1><br>
�����ä��ݤ��ȡ���ʬ����˾޶⤬£���ޤ�����1����${HBF_Point_Value}${HunitMoney}��<br>
��SPP�ߥ�����ʳ������Ƥ�ȡ�BF�ݥ���Ȥ�1����館�ޤ���<br>
�����ä��ݤ�����硢����¿���BF�ݥ���Ȥ���館�ޤ���<br>
<DIV ID='Successive'>
<H1>Battle Field ����</H1>
<table border=0 width=50%>
<TR>
<TH $HbgTitleCell align=center >${HtagTH_}���${H_tagTH}</TH>
<TH $HbgTitleCell align=center >${HtagTH_}${AfterName}̾${H_tagTH}</TH>
<TH $HbgTitleCell align=center >${HtagTH_}�ݥ����${H_tagTH}</TH>
</TR>
END

    my ($lName);
    my ($rank);
    my ($zeroflag) = @Hislands;

    $rank = 0;      # ����++ ����Τ� 0
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
# HakoniwaCup����
#----------------------------------------------------------------------
# �ᥤ��
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
#		$str = '[�ǽ����]';
#	} elsif($turn1 == 8) {
#		$str = '[�辡��]';
#	} elsif($turn1 == 7) {
#		$str = '[��辡��]';
#	} elsif($turn1 == 6) {
#		$str = '[�ࡹ�辡��]';
#	} elsif($turn1 == 5) {
#		$str = '[�辡�ȡ��ʥ��ȳ��ϡ�]';
#	} else {
#		$str = '[ͽ��]';
#	}
	# ����
	unlock();

	out(<<END);
<CENTER>$HtempBack</CENTER><BR>
<DIV ID='Successive'>
<H1>HakoniwaCup $hcturn ����<BR>${str}</H1>
<table border=0 width=50%><TR>
<TH $HbgTitleCell align=center rowspan=2>${HtagTH_}���${H_tagTH}</TH>
<TH $HbgTitleCell align=center rowspan=2>${HtagTH_}${AfterName}̾${H_tagTH}</TH>
<TH $HbgTitleCell align=center rowspan=2>${HtagTH_}������̾${H_tagTH}</TH>
<TH $HbgTitleCell align=center rowspan=2>${HtagTH_}��${H_tagTH}</TH>
<TH $HbgTitleCell align=center rowspan=2>${HtagTH_}��${H_tagTH}</TH>
<TH $HbgTitleCell align=center rowspan=2>${HtagTH_}ʬ${H_tagTH}</TH>
<TH $HbgTitleCell align=center colspan=4>${HtagTH_}���${H_tagTH}</TH>
<TH $HbgTitleCell align=center colspan=3>${HtagTH_}ǽ��${H_tagTH}</TH>
</TR><TR>
<TH $HbgTitleCell align=center>${HtagTH_}ͥ�����${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}��${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}��${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}ʬ${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}����${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}����${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}�����ѡ�${H_tagTH}</TH>
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
#			$juni = 'ͽ�����';
#		} elsif(($turn1 > 6) && ($n > 4)) {
#			$juni = '�٥��ȣ�';
#		} elsif(($turn1 > 7) && ($n > 2)) {
#			$juni = '�٥��ȣ�';
#		} elsif($turn1 > 8) {
#			if($n == 1) {
#				$juni = 'ͥ��';
#			} elsif($n == 2) {
#				$juni = '��ͥ��';
#			}
#		}
		my $id = $HCislands[$i]->{'id'};
		my $name = islandName($HCislands[$i]);
		my $kekka = $hcLog{$name};
        my $team = "${HtagName_}$HCislands[$i]->{'hakoteam'}${H_tagName}";
		$kekka = '��' if($kekka eq '');
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
<tr><TH colspan=12>�ǡ���������ޤ���</TH></tr>
END
	}
	out(<<END);
</table>
����¿��Ū����������٤򼺤��ʤɤ��ƥǡ�������������줿���ϡ�<BR>
�ºݤλ���̤Ƚ�̤��ۤʤ��礬����ޤ�����λ����������
</DIV>
END
}

# ����ɽ��
sub hclogSet {
	my($line, $turn, $message);
	my %hcLog;
	if(!open(LIN, "${HdirName}/hakojima.lhc")) {
		return %hcLog;
	}
	while($line = <LIN>) {
		chomp($line);
		($turn, $message) = split(/,/, $line);
		next unless($message =~ /^<span class="islName">Hakoniwa Cup (.*)<\/span>��(.*)$/);
		my ($no, $kekka) = ($1, $2);
		next unless($kekka =~ /^<span class="([\w]*)">(.*)����ɽ(.*)<\/span><B>VS<\/B><span class="([\w]*)">(.*)����ɽ(.*)<\/span> �� (.*)$/);
		my($wl1, $name1, $tname1, $wl2, $name2, $tname2, $score) = ($1, $2, $3, $4, $5,$6,$7);
		if($no !~ /�辡/) {
			$score =~ /^<span class="([\w]*)">([0-9]*)<\/span><B>��<\/B><span class="([\w]*)">([0-9]*)<\/span>$/;
			$hcLog{$name1} = 'ͽ��' if($hcLog{$name1} eq '');
			$hcLog{$name2} = 'ͽ��' if($hcLog{$name2} eq '');
			$hcLog{$name1} .= " <span class=\"$wl1\"><a title=\"$no($2-$4)\">$name2��</a></span>";
			$hcLog{$name2} .= " <span class=\"$wl2\"><a title=\"$no($2-$4)\">$name1��</a></span>";
		} else {
			if($no =~ /�ࡹ�辡/) {
				$hcLog{$name1} .= "\n<BR>";
				$hcLog{$name2} .= "\n<BR>";
			}
			$score =~ /^<span class="([\w]*)">([0-9]*)<\/span><B>��<\/B><span class="([\w]*)">([0-9]*)<\/span>$/;
			$hcLog{$name1} .= " <B>${no}vs</B><span class=\"$wl1\"><a title=\"$no($2-$4)\">$name2��</a></span>";
			$hcLog{$name2} .= " <B>${no}vs</B><span class=\"$wl2\"><a title=\"$no($2-$4)\">$name1��</a></span>";
		}
	}

	close(LIN);
	return %hcLog;
}

#----------------------------------------------------------------------
# ���������õ��
#----------------------------------------------------------------------
# �ᥤ��
sub newIslandTop {
	# ����
	unlock();

	# �����ͤ��������������õ���롩
	if ($HadminJoinOnly) {
		# �ޥ����ѥ���ɥ����å�
		unless (checkMasterPassword($HinputPassword)) {
			# password�ְ㤤
			tempWrongPassword();
			return;
		}
	}
	
	out(<<END);
<CENTER>$HtempBack</CENTER><BR>
<DIV ID='newIsland'>
<H1>������${AfterName}��õ��</H1>
    <span class="rednews">��κ����ϤҤȤꡢ1��ޤǤǤ���<br>Ʊ��IP���ɥ쥹��������Ƥ�줿��򸫤Ĥ����顢����ޤ���<br>��²�ʤɡ�Ʊ��IP���ɥ쥹�ˤʤ���ϡ����Ϣ���Ƥ���������</span>
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
�ر�̾�����򤷤Ʋ�����<BR>
<SELECT NAME="CAMPNUMBER">
$allyList
<OPTION VALUE=\"-1\">�ɤ��Ǥ��ɤ�
</SELECT><BR>
END
		}
		out(<<END);
�ɤ��̾����Ĥ���ͽ�ꡩ<small>(����${HlengthIslandName}���ޤ�)</small><BR>
<INPUT TYPE="text" NAME="ISLANDNAME" SIZE=32 MAXLENGTH=32>${AfterName}<BR>
���ʤ���̾���ϡ�<small>(����${HlengthOwnerName}���ޤ�)</small><BR>
<INPUT TYPE="text" NAME="OWNERNAME" SIZE=32 MAXLENGTH=32><BR>
�ѥ���ɤϡ�<BR>
<INPUT TYPE="password" NAME="PASSWORD" SIZE=32 MAXLENGTH=32><BR>
ǰ�Τ���ѥ���ɤ�⤦���<BR>
<INPUT TYPE="password" NAME="PASSWORD2" SIZE=32 MAXLENGTH=32><BR>

<INPUT TYPE="submit" VALUE="õ���˹Ԥ�" NAME="NewIslandButton">
</FORM>
</DIV>
END
	} else {
	out(<<END);
		${AfterName}�ο���������Ǥ�������������Ͽ�Ǥ��ޤ���<br>
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
# ���̾���ȥѥ���ɤ��ѹ�
#----------------------------------------------------------------------
# �ᥤ��
sub renameIslandMain {
    # ����
    unlock();

    out(<<END);
<CENTER>$HtempBack</CENTER><BR>
<DIV ID='changeInfo'>
<H1>${AfterName}��̾���ȥѥ���ɤ��ѹ�</H1>
<table border=0 width=50%><tr><td class="M"><P>
(���)${AfterName}��̾�����ѹ��ˤ�$HcostChangeName${HunitMoney}������ޤ���(¾��̵��)
</P>
<FORM action="$HthisFile" method="POST">
�ɤ�${AfterName}�Ǥ�����<BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>
<BR>
�ɤ��̾�����Ѥ��ޤ�����(�ѹ�������Τ�)<small>(����${HlengthIslandName}���ޤ�)</small><BR>
<input type="text" NAME="ISLANDNAME" SIZE=32 MAXLENGTH=32>${AfterName}<BR>
���ʤ���̾�����Ѥ��ޤ�����(�ѹ�������Τ�)<small>(����${HlengthOwnerName}���ޤ�)</small><BR>
<input type="text" NAME="OWNERNAME" SIZE=32 MAXLENGTH=32><BR>
�ѥ���ɤϡ�(ɬ��)<BR>
<input type="password" name="OLDPASS" size=32 maxlength=32><BR>
�������ѥ���ɤϡ�(�ѹ�������Τ�)<BR>
<input type="password" name="PASSWORD" size=32 maxlength=32><BR>
ǰ�Τ���ѥ���ɤ�⤦���(�ѹ�������Τ�)<BR>
<input type="password" name="PASSWORD2" size=32 maxlength=32><BR>
<input type="submit" value="�ѹ�����" name="ChangeInfoButton">
</form>
</td></tr></table></div>
END
}


#----------------------------------------------------------------------
# �͸�����¾���ͤ򻻽Сʽ̾��ǡ�
sub estimate {
	my ($number) = $_[0];
	my ($island);
	my ($pop, $area, $missiles, $fore) = (0, 0, 0, 0);

	# �Ϸ������
	$island = $Hislands[$number];
	my ($land) = $island->{'land'};
	my ($landValue) = $island->{'landValue'};

	# ������
	my($x, $y, $kind, $value);
	foreach $y (0..$islandSize) {
		foreach $x (0..$islandSize) {
			$kind = $land->[$x][$y];
			$value = $landValue->[$x][$y];
			if($kind != $HlandSea) {
				$area++;
				if($kind == $HlandTown) {
					# Į
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

	# ����
	$island->{'pop'}		= $pop;
	$island->{'area'}		= $area;
	$island->{'missiles'}	= $missiles; # �ߥ�����ȯ�Ͳ�ǽ��
	$island->{'fore'}		= $fore;

	# ���ȼԿ�
	$island->{'unemployed'} = $pop;

	# ���Point
	$island->{'pts'} = int($pop + $island->{'money'}/100 + $island->{'food'}/100 + $area*5);

}

#----------------------------------------------------------------------
# �ϰ�����Ϸ��������ʥ��ԡ���(New)
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

        # �Ԥˤ�����Ĵ��
        $sx-- if(!($sy % 2) && ($y % 2));

        if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)){
            # �ϰϳ��ξ��
            # ���˲û�
            $sea++;
        } elsif($list[$land->[$sx][$sy]]) {
            # �ϰ���ξ��
            $count++;
        }
    }
    $count += $sea if($list[$HlandSea]);    # ���ʤ�û�

    return $count;
}

#----------------------------------------------------------------------
# �����ͥ⡼��
#----------------------------------------------------------------------
# ��ζ������(�����ѹ���)
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
	# ��ơ��֥�����
	$island->{'dead'} = 1;
	$island->{'pts'} = 0;
	$island->{'pop'} = 0;
	$island->{'field'} = 0;

	allyOccupy();
	allySort();
	islandSort('pts');

	logDeleteIsland($tmpid, $island->{'name'}) if($num);

	# �ᥤ��ǡ��������
	$HislandNumber--;
	$islandNumber--;
	writeIslandsFile($HcurrentID);

	unlink("${HdirName}/${HcurrentID}.${HsubData}");
	unlock();
	tempDeleteIsland($island->{'name'});
}

#----------------------------------------------------------------------
# BattleField�����⡼��
sub bfieldMain {
	if (!$HbfieldMode) {
		# ����
		unlock();

		# �ƥ�ץ졼�Ƚ���
		tempBfieldPage();
	} else {
		# �ѥ���ɥ����å�
		if(checkSpecialPassword($HdefaultPassword)) {
			# �ü�ѥ����

			# id����������
			$HcurrentNumber = $HidToNumber{$HcurrentID};
			my($island) = $Hislands[$HcurrentNumber];
			my($name) = islandName($island);
			my($id) = $island->{'id'};

			my $bId, $str;
			my $safety = 0;
			if($id < 100) {
				if ($HbfieldNumber > 9) {
					# Battle Field�ο�������(�����10)
					tempBfieldNG('������Ͽ�������С�');
					unlock();
					return;
				}

				# ����
				for($bId = 101; $bId <= 120; $bId++) {
					last if(!(defined $HidToNumber{$bId}));
				}
				$island->{'id'} = $bId;
				$str = '�̾���� �� Battle Field';
			} else {
				if ($HislandNumber - $HbfieldNumber >= $HmaxIsland) {
					# �̾����ο�������
					tempBfieldNG("${AfterName}�����äѤ�");
					unlock();
					return;
				}
				# ���
				while(defined $HidToNumber{$HislandNextID}) {
					$HislandNextID ++;
					$HislandNextID = 1 if($HislandNextID > 100);
					$safety++;
					last if($safety == 100);
				}
				$island->{'id'} = $HislandNextID;
				$HislandNextID ++;
				$HislandNextID = 1 if($HislandNextID > 100);
				$str ='Battle Field �� �̾����';
			}

			if (($bId > 121) || ($safety == 100)) {
				# �ѹ��Τ����ID������Ǥ���
				tempBfieldNG('ID���������顼');
				unlock();
				return;
			}
			# �ǡ����񤭽Ф�
			writeIslandsFile($HcurrentID);
			rename("${HdirName}/${id}.${HsubData}", "${HdirName}/${island->{'id'}}.${HsubData}");

			unlock();

			# �ѹ�����
			tempBfieldOK($name, $str);
		} else {
			# password�ְ㤤
			unlock();
			tempWrongPassword();
			return;
		}
	}
}

#----------------------------------------------------------------------
# BattleField�����⡼�ɤΥȥåץڡ���
sub tempBfieldPage {
    out(<<END);
<CENTER>$HtempBack</CENTER>
<H1>Battle Field�����</H1>

<FORM action="$HthisFile" method="POST">
<B>Battle Field������ѹ�����${AfterName}�ϡ�</B><BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>
<INPUT TYPE="hidden" VALUE="$HdefaultPassword" NAME="Bfield">
<INPUT TYPE="submit" VALUE="�����ѹ�" NAME="BfieldButton"><BR>
</FORM>
END
}

#----------------------------------------------------------------------
# BattleField������λ
sub tempBfieldOK {
    my ($name, $str) = @_;

    out(<<END);
${HtagBig_}$name${AfterName}��Battle Field������ѹ����ޤ�����<br>$str${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# BattleField��������
sub tempBfieldNG {
    my ($str) = @_;

    out(<<END);
${HtagBig_}Battle Field�����ꥨ�顼($str)��${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# �����ͤˤ��ץ쥼��ȥ⡼��
sub presentMain {
	if (!$HpresentMode) {
		# ����
		unlock();

		# �ƥ�ץ졼�Ƚ���
		tempPresentPage();
	} else {
		# �ѥ���ɥ����å�
		if(checkSpecialPassword($HoldPassword)) {
			# �ü�ѥ����

			if (!$HpresentMoney && !$HpresentFood) {
				# ��⿩����ʤ�
				tempPresentEmpty();
				unlock();
				return;
			}

			# id����������
			$HcurrentNumber = $HidToNumber{$HcurrentID};
			my($island) = $Hislands[$HcurrentNumber];
			my($name)   = islandName($island);

			$island->{'money'} += $HpresentMoney;
			$island->{'money'} = 0 if ($island->{'money'} < 0);
			$island->{'food'}  += $HpresentFood;
			$island->{'food'} = 0 if ($island->{'food'} < 0);

			logPresent($HcurrentID, $name, $HpresentLog);

			# �ǡ����񤭽Ф�
			writeIslandsFile($HcurrentID);
			unlock();

			# �ѹ�����
			tempPresentOK($name);
		} else {
			# password�ְ㤤
			unlock();
			tempWrongPassword();
			return;
		}
	}
}


#----------------------------------------------------------------------
# �ץ쥼��ȥ⡼�ɤΥȥåץڡ���
sub tempPresentPage {

    out(<<END);
<CENTER>$HtempBack</CENTER>
<H1>����${AfterName}�˥ץ쥼��Ȥ�£��</H1>

<FORM action="$HthisFile" method="POST">
<B>�ץ쥼��Ȥ�������${AfterName}�ϡ�</B><BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT><BR>
<BR>
<B>�ץ쥼��Ȥ����Ƥϡ�(�ޥ��ʥ��ͤ��ǽ)</B><BR>
<INPUT TYPE="text" NAME="PRESENTMONEY" VALUE="0" SIZE=16 MAXLENGTH=16>$HunitMoney<BR>
<INPUT TYPE="text" NAME="PRESENTFOOD"  VALUE="0" SIZE=16 MAXLENGTH=16>$HunitFood<BR>
<BR>
<B>����å������ϡ�(��ά��ǽ����Ƭ��${AfterName}̾����������ޤ�)</B><BR>
����${AfterName}<INPUT TYPE="text" NAME="PRESENTLOG"  VALUE="" SIZE=128 MAXLENGTH=256><BR>
<BR>
<B>�ޥ������ѥ���ɤϡ�</B><BR>
<INPUT TYPE="password" NAME="OLDPASS" VALUE="$HdefaultPassword" SIZE=32 MAXLENGTH=32><BR>
<INPUT TYPE="submit" VALUE="�ץ쥼��Ȥ�£��" NAME="PresentButton"><BR>
</FORM>
END
}

#----------------------------------------------------------------------
# �ץ쥼��ȴ�λ
sub tempPresentOK {
    my ($name) = @_;
    out(<<END);
${HtagBig_}$name${AfterName}�˥ץ쥼��Ȥ�£��ޤ���${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# �ץ쥼������Ƥ���������
sub tempPresentEmpty {
    out(<<END);
${HtagBig_}�ץ쥼��Ȥ����Ƥ����������褦�Ǥ�${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# �����ͤˤ�����ۥ⡼��
sub punishMain {
	if(checkSpecialPassword($HdefaultPassword)) {
		# �ü�ѥ����
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

		# �ƥ�ץ졼�Ƚ���
		tempPunishPage();

	} else {
		# �ѥ���ɤ����פ��ʤ���Хȥåץڡ�����
		require('./hako-top.cgi');
		unlock();
		# �ƥ�ץ졼�Ƚ���
		tempTopPage();
	}
}

#----------------------------------------------------------------------
# ���ۥ⡼�ɤΥȥåץڡ���
sub tempPunishPage {
	my(@punishName) =
		(
		 '�ʤ�', # 0
		 '�Ͽ�', # 1
		 '����', # 2
		 '���áʿ͸���說�ꥢ���Τߡ�', # 3
		 '�������������Ѿ�說�ꥢ���Τߡ�', # 4
		 '����', # 5
		 '������Сʺ�ɸ�����', # 6
		 '���', # 7
		 'ʮ�Сʺ�ɸ�����', # 8
		 );

	out(<<END);
<CENTER>$HtempBack</CENTER>
<H2>����${AfterName}�����ۤ�ä���</H2>

<UL>
    <LI>�֥롼��˰�ȿ�����פȻפ����ˡ��֤��Υ롼���ï�⤬�ɤ����˽񤤤Ƥ��뤫���פ��ǧ���ޤ��礦��<br>
    <LI>���ۤ�ä���ΤϤ��䤹�����ȤǤ����������˴����ͤȤ��Ƥ�Ω��ǹԤäƤ��뤫�ͤ��ޤ��礦��<br>
    <LI>���ۤ�ä��ʤ���Фʤ�ʤ��ۤ��ﳲ���礭�����ͤ��ޤ��礦���ڤ��������ǹ��⤹��ͤϤ��ĤǤ⤤���ΤǤ���<br>
    <LI><span class=attention>���ۤ�¸�ߤ϶���ˤ��ޤ��礦��</span>���ۤ����餫�ˤʤ��¾�Υץ쥤�䡼�Ȥο���ط�������ޤ���<br>
</UL>

<FORM name="lcForm" action="$HthisFile" method="POST">
<INPUT TYPE="hidden" VALUE="$HdefaultPassword" NAME="Punish">
<B>���ۤ�ä���${AfterName}�ϡ�</B><BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>
<INPUT TYPE="button" VALUE="�ޥåפ򳫤�" onclick="printIsland();">
<BR><BR>
<B>��ɸ�ϡ��ʺ�ɸ����Ǥ������ۤǤΤ�ͭ����</B><BR>
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
<B>���ۤ����Ƥϡ�</B><BR>
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
<INPUT TYPE="submit" VALUE="���ۤ�ä���" NAME="PunishButton"><BR>
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
		out("<TABLE BORDER><TR><TH>${AfterName}̾</TH><TH>��������</TH><TH>��ɸ</TH></TR>");
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
# �����ͤˤ���Ϸ��ѹ��⡼��
sub lchangeMain {
    if (checkSpecialPassword($HdefaultPassword)) {
        # �ü�ѥ����
        if ($HlchangeMode) {
            # id����������
            $HcurrentNumber = $HidToNumber{$HcurrentID};
            my ($island) = $Hislands[$HcurrentNumber];
            my ($land) = $island->{'land'};
            my ($landValue) = $island->{'landValue'};
            my ($landValue2) = $island->{'landValue2'};
            my ($landValue3) = $island->{'landValue3'};

			# �Ϸ����ͤ�������������å�(�����å��������ʤ����ϥ����ȥ����Ȥ��Ʋ�����)
#			if(!landCheck($HlchangeKIND, $HlchangeVALUE)) {
#				tempBadValue();
#				unlock();
#				return;
#			}

            $land->[$HcommandX][$HcommandY] = $HlchangeKIND;
            $landValue->[$HcommandX][$HcommandY] = $HlchangeVALUE;
            $landValue2->[$HcommandX][$HcommandY] = $HlchangeVALUE2;
            $landValue3->[$HcommandX][$HcommandY] = $HlchangeVALUE3;

			# �ǡ����񤭽Ф�
			writeIslandsFile($HcurrentID);
			unlock();

			# �ѹ�����
			tempLchangeOK(islandName($island));
		}
		unlock();
		# �ƥ�ץ졼�Ƚ���
		tempLchangePage();
	} else {
		# �ѥ���ɤ����פ��ʤ���Хȥåץڡ�����
		require('./hako-top.cgi');
		unlock();
		# �ƥ�ץ졼�Ƚ���
		tempTopPage();
	}
}

#----------------------------------------------------------------------
# �Ϸ��ѹ��⡼�ɤΥȥåץڡ���
sub tempLchangePage {
    require './init-server.cgi';
    out(<<END);
<CENTER>$HtempBack</CENTER>
<H1>����${AfterName}���Ϸ��ǡ������ѹ�����</H1>

<DL>
<DT>�����Ϸ����͡פˤĤ��Ƥ��μ����ʤ���С����Ѥ��񤷤����⤷��ޤ���</DT>
<DT>���äˡֲ��áפˤĤ��Ƥϡ��μ������äƤ��񤷤��Ȼפ��ޤ���<br>���ʤߤˡ�(�Ϸ�����)��(���äμ���)�ߣ�����(���ä���̿��)�Ǥ���������ϣ����ޤ���̿�Ϥϣ����ޤǤǤ���</DT>
<!---
<DT>�����Ϸ��פ��Ф���<B>���Ϸ����͡פ�Ŭ�ڤǤ��뤫�ɤ����ʰ�Ƚ��򤷤Ƥ��ޤ�</B>�Τǡ���դ��Ƥ���������</DT>
--->
</DL><BR>

<FORM name='mcalc'>
<a HREF="JavaScript:void(0);" onClick='Mons_calc(); return 1;'>�׻�</a>
���ࡧ<INPUT TYPE="text" SIZE=6 NAME="MONSKIND" VALUE="0">
���ϡ�<INPUT TYPE="text" SIZE=6 NAME="MONSHP" VALUE="1">
������<INPUT TYPE="text" SIZE=6 NAME="MONS_VAL" VALUE="">
</form>
<BR><BR>
<FORM name="lcForm" action="$HthisFile" method="POST">
<INPUT TYPE="hidden" VALUE="$HdefaultPassword" NAME="Lchange">
<B>�Ϸ����ѹ�����${AfterName}�ϡ�</B><BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>
<INPUT TYPE="button" VALUE="�ޥåפ򳫤�" onclick="printIsland(); return 1;">
<BR><BR>
<B>��ɸ�ϡ�</B><BR>
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
<B>�Ϸ��ϡ�</B><BR>
<SELECT NAME="LCHANGEKIND">
<OPTION VALUE="$HlandPlains">ʿ��
<OPTION VALUE="$HlandSea">��
<OPTION VALUE="$HlandWaste">����
<OPTION VALUE="$HlandTown">Į��
<OPTION VALUE="$HlandSunahama">����
<OPTION VALUE="$HlandIce">ɹ��
<OPTION VALUE="$HlandForest">��
<OPTION VALUE="$HlandFarm">����
<OPTION VALUE="$HlandInaka">���ʤ�
<OPTION VALUE="$HlandFactory">����
<OPTION VALUE="$HlandMonument">��ǰ��
<OPTION VALUE="$HlandDefence">�ɱһ���
<OPTION VALUE="$HlandMountain">��
<OPTION VALUE="$HlandMonster">����
<OPTION VALUE="$HlandBettown">�������Ի�
<OPTION VALUE="$HlandNewtown">�˥塼������
<OPTION VALUE="$HlandBigtown">�����Ի�
<OPTION VALUE="$HlandSbase">�������
<OPTION VALUE="$HlandOil">��������
<OPTION VALUE="$HlandSeacity">�����Ի�
<OPTION VALUE="$HlandSeatown">���쿷�Ի�
<OPTION VALUE="$HlandUmicity">���Ի�
<OPTION VALUE="$HlandOilCity">�����Ի�
<OPTION VALUE="$HlandFrocity">�����Ի�
<OPTION VALUE="$HlandUmishuto">�������
<OPTION VALUE="$HlandPark">ͷ����
<OPTION VALUE="$HlandInoraLand">���Τ����
<OPTION VALUE="$HlandMinato">��
<OPTION VALUE="$HlandFune">����
<OPTION VALUE="$HlandNursery">�ܿ���
<OPTION VALUE="$HlandKyujo"> ����
<OPTION VALUE="$HlandUmiamu"> �����ߤ�
<OPTION VALUE="$HlandFoodim">��ʪ�����
<OPTION VALUE="$HlandProcity">�ɺ��Ի�
<OPTION VALUE="$HlandGold">�⻳
<OPTION VALUE="$HlandSeki">�ؽ�
<OPTION VALUE="$HlandRottenSea">�峤
<OPTION VALUE="$HlandFarmchi">�ܷܾ�
<OPTION VALUE="$HlandFarmpic">���ھ�
<OPTION VALUE="$HlandFarmcow">�Ҿ�
<OPTION VALUE="$HlandCollege">���
<OPTION VALUE="$HlandOnsen">����
<OPTION VALUE="$HlandHouse">���β�
<OPTION VALUE="$HlandShuto">����
<OPTION VALUE="$HlandRizort">�꥾������
<OPTION VALUE="$HlandKyujokai">¿��Ū����������
<OPTION VALUE="$HlandBigRizort">�׳��꥾���ȥۥƥ�
<OPTION VALUE="$HlandHTFactory">�ϥ��ƥ����
<OPTION VALUE="$HlandSHTF">�ϥ��ƥ���ȡ���
<OPTION VALUE="$HlandYakusho">�����
<OPTION VALUE="$HlandMine">����
<OPTION VALUE="$HlandHaribote">�ϥ�ܥ�
<OPTION VALUE="$HlandBase">�ߥ��������
<OPTION VALUE="$HlandKatorikun">�ڤι�路
<OPTION VALUE="$HlandEgg">��
<OPTION VALUE="$HlandHospital">�±�
<OPTION VALUE="$HlandFiredept">���ɽ�
<OPTION VALUE="$HlandOmamori">����
<OPTION VALUE="$HlandRocket">���å�
<OPTION VALUE="$HlandShrine">���ο���
<OPTION VALUE="$HlandYougan">�ϴ�����
<OPTION VALUE="$HlandBigFood">���٤��
<OPTION VALUE="$HlandTrain">�����
<OPTION VALUE="$HlandStation">��
<OPTION VALUE="$HlandZoo">ưʪ��
<OPTION VALUE="$HlandBeachPark">�������
<OPTION VALUE="$HlandGomi">���ߤ�����
<OPTION VALUE="$HlandGomiFactory">���߽�����
<OPTION VALUE="$HlandBoueki">�ǰ�
</SELECT><BR>
<BR>
<B>�Ϸ����ͤϡ�(LandValue)</B><BR>
<INPUT TYPE="text" SIZE="6" NAME="LCHANGEVALUE" VALUE="0"><BR>
<B>�Ϸ�����2�ϡ�(LandValue2)</B><BR>
<INPUT TYPE="text" SIZE="6" NAME="LCHANGEVALUE2" VALUE="0"><BR>
<B>�Ϸ�����3�ϡ�(LandValue3)</B><BR>
<INPUT TYPE="text" SIZE="6" NAME="LCHANGEVALUE3" VALUE="0"><BR>
<BR>
<INPUT TYPE="submit" VALUE="�ѹ�����" NAME="LchangeButton"><BR>
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
    out("<TABLE BORDER><TR><TH>�ֹ�</TH><TH>����</TH><TH>̾��</TH><TH>����</TH><TH>�ĳ�������</TH><TH>�и���</TH></TR>");

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
# �Ϸ��ѹ���λ
sub tempLchangeOK {
	my($name) = @_;
	out(<<END);
${HtagBig_}$name���Ϸ����ѹ����ޤ���${H_tagBig}
<HR>
END
}

#----------------------------------------------------------------------
# �Ϸ����ͤ���������
sub tempBadValue {
	out(<<END);
${HtagBig_}�Ϸ����ͤ����������褦�Ǥ�${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# �Ϸ����ͤ�����å�
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
# �����ͤˤ�뤢������⡼��
sub preDeleteMain {
	if(checkSpecialPassword($HdefaultPassword)) {
		# �ü�ѥ����
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

			# �ǡ����񤭽Ф�
			writeIslandsFile($HcurrentID);
			unlock();
			if($flag) {
				tempPreDeleteEnd(islandName($Hislands[$HidToNumber{$HcurrentID}]));
			} else {
				tempPreDelete(islandName($Hislands[$HidToNumber{$HcurrentID}]));
			}
		}
		unlock();
		# �ƥ�ץ졼�Ƚ���
		tempPdeleteMain();
	} else {
		# �ѥ���ɤ����פ��ʤ���Хȥåץڡ�����
		require('./hako-top.cgi');
		unlock();
		# �ƥ�ץ졼�Ƚ���
		tempTopPage();
	}
}

#----------------------------------------------------------------------
# ��������⡼�ɤΥȥåץڡ���
sub tempPdeleteMain {

    out(<<END);
<CENTER>$HtempBack</CENTER>
<H1>����${AfterName}������ͤ�������ˤ���</H1>

<DL>
<DT>����������ˤʤä�${AfterName}�ϡ����������(�������������ޥ�ɽ�������Ĺ���ҳ������ȼ԰�̱)����ʤ��ʤ�ޤ���</DT>
<DT>���޴ط��Ͻ�������ޤ�����¾��${AfterName}����ι���Ϥ��٤Ƽ����Ĥ��Ƥ��ޤ��ޤ���</DT>
<DT>��������������礬�������פ⤷���ϡֶ�������פ��줿��硢��������Σɣĥǡ����ϡ����Τ������������Ԥ��ޤǤ��Τޤ޻Ĥ�ޤ���</DT>
</DL>

<FORM name="pdForm" action="$HthisFile" method="POST">
<INPUT TYPE="hidden" VALUE="$HdefaultPassword" NAME="Pdelete">
<B>�����ͤ�������ˤ���${AfterName}�ϡ�</B><BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>
<BR>
<INPUT TYPE="submit" VALUE="���ꡦ���" NAME="PdeleteButton"><BR>
</FORM>
<TABLE BORDER><TR><TH>�����������${AfterName}</TH></TR>
END

    if ($HpreDeleteID[0] eq '') {
        out("<TR><TH>�����ͤ��������${AfterName}�Ϥ���ޤ���</TH></TR>");
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
# �����ͤ�����������
sub tempPreDelete {
    my($name) = @_;

    out(<<END);
${HtagBig_}$name${AfterName}������ͤ�������ˤ��ޤ���${H_tagBig}
<HR>
END
}

#----------------------------------------------------------------------
# �����ͤ���������
sub tempPreDeleteEnd {
	my($name) = @_;
	out(<<END);
${HtagBig_}$name${AfterName}�δ����ͤ�������������ޤ���${H_tagBig}
<HR>
END
}
#----------------------------------------------------------------------
# ���ƥ�ץ졼��
#----------------------------------------------------------------------
# ��Ͽ��
sub logHistory {
	open(HOUT, ">>${HdirName}/hakojima.his");
	print HOUT "$HislandTurn,$_[0]\n";
	close(HOUT);
}

#----------------------------------------------------------------------
# ȯ��
sub logDiscover {
	my($name) = @_;
	logHistory("${HtagName_}${name}${AfterName}${H_tagName}��ȯ������롣");
}

#----------------------------------------------------------------------
# ��̾���ѹ�
sub logChangeName {
	my($name1, $name2) = @_;
	logHistory("${HtagName_}${name1}${AfterName}${H_tagName}��̾�Τ�${HtagName_}${name2}${AfterName}${H_tagName}���ѹ����롣");
}

#----------------------------------------------------------------------
# �����ʡ�̾���ѹ�
sub logChangeOwnerName {
	my($name1, $name2) = @_;
	logHistory("${HtagName_}${name1}${AfterName}${H_tagName}�������ʡ���${HtagName_}${name2}${H_tagName}���ѹ����롣");
}

#----------------------------------------------------------------------
# ������������
sub tempNewIslandillegal {
	out(<<END);
${HtagBig_}���������ȤϤ���᤯������m(_ _)m${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# �礬���äѤ��ʾ��
sub tempNewIslandFull {
	out(<<END);
${HtagBig_}����������ޤ���${AfterName}�����դ���Ͽ�Ǥ��ޤ��󡪡�${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# ������̾�����ʤ����
sub tempNewIslandNoName {
	out(<<END);
${HtagBig_}${AfterName}�ˤĤ���̾����ɬ�פǤ���${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# ������̾���������ʾ��
sub tempNewIslandBadName {
	out(<<END);
${HtagBig_}',?()<>\$'�Ȥ����äƤ��ꡢ��̵��${AfterName}�ס�����${AfterName}�פȤ����ä��Ѥ�̾���Ϥ��ޤ��礦���${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# �����ǥ����ʡ�̾�������ʾ��
sub tempNewIslandBadOwnerName {
	out(<<END);
${HtagBig_}',?()<>\$'�����äƤ���̾���Ϥ��ޤ��礦��${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# ���Ǥˤ���̾�����礬������
sub tempNewIslandAlready {
	out(<<END);
${HtagBig_}����${AfterName}�ʤ餹�Ǥ�ȯ������Ƥ��ޤ���${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# �ѥ���ɤ��ʤ����
sub tempNewIslandNoPassword {
	out(<<END);
${HtagBig_}�ѥ���ɤ�ɬ�פǤ���${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# ���ȯ�����ޤ���!!
sub tempNewIslandHead {
	out(<<END);
<CENTER>
${HtagBig_}${AfterName}��ȯ�����ޤ�������${H_tagBig}<BR>
${HtagBig_}${HtagName_}��${HcurrentName}${AfterName}��${H_tagName}��̿̾���ޤ���${H_tagBig}<BR>
���ޥ�ɤ����Ϥϡ����٥ȥåפ���äơ��ֳ�ȯ���˹Ԥ��ץܥ��󤫤�ɤ�����<BR>
$HtempBack<BR>
</CENTER>
<!-- ���� SCRIPT �ϡ����ȯ���������̤ǥޥåפ򥯥�å�����ȥ��顼�ˤʤ�ץХ��ν����� -->
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
# ̾���ѹ�����
sub tempChangeNothing {
	out(<<END);
${HtagBig_}̾�����ѥ���ɤȤ�˶���Ǥ�${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# ̾���ѹ����­�ꤺ
sub tempChangeNoMoney {
	out(<<END);
${HtagBig_}�����­�Τ����ѹ��Ǥ��ޤ���${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# ̾���ѹ�����
sub tempChange {
	out(<<END);
${HtagBig_}�ѹ���λ���ޤ���${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# ���������
sub logDeleteIsland {
	my($id, $name) = @_;
#	logHistory("${HtagName_}${name}${H_tagName}��<B>�����͸��¤ˤ��</B><span class=attention>���</span>�Ȥʤ롣");
#	logHistory("${HtagName_}${name}${H_tagName}�ˡ�����<B>ŷȳ���ߤ�</B>���äȤ����ޤ�<span class=attention>�������פ�</span>�׷���ʤ��ʤ�ޤ�����");
	logHistory("${HtagName_}${name}${H_tagName}�ϡ�������<B>�ܤ�˿���</B>Φ�ϤϤ��٤�<span class=attention>���פ��ޤ�����</span>");
}


#----------------------------------------------------------------------
# ��ζ������(���ڥ����⡼��)
sub tempDeleteIsland {
	my($name) = @_;
	out(<<END);
${HtagBig_}${name}����������ޤ�����${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# �ץ쥼���
sub logPresent {
	my($id, $name, $log) = @_;
	logHistory("${HtagName_}${name}��${H_tagName}$log") if ($log ne '');
}

1;

