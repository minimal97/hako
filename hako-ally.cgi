#----------------------------------------------------------------------
# Ȣ����� ver2.30
# ���������⥸�塼��(ver1.00)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
#----------------------------------------------------------------------
#
#   ������Ʊ���ˤ�����ꤽ���ʤ�Τ�ʬ��
#       ���ѥ��åƥ�
#
#----------------------------------------------------------------------
# make �� include
# require './hako-const.cgi';

#----------------------------------------------------------------------
# �����ѹ��⡼��
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Ʊ����̾������ID������
sub aNameToId {
    my ($name) = @_;

    # ���礫��õ��
    my ($i);
    for ($i = 0; $i < $HallyNumber; $i++) {
        if ($Hally[$i]->{'name'} eq $name) {
            return $Hally[$i]->{'id'};
        }
    }

    # ���Ĥ���ʤ��ä����
    return (-1);
}


#----------------------------------------------------------------------
# Ʊ���Υޡ�������ID������
sub aMarkToId {
    my ($mark) = @_;

    # ���礫��õ��
    my ($i);
    for ($i = 0; $i < $HallyNumber; $i++) {
        if ($Hally[$i]->{'mark'} eq $mark) {
            return $Hally[$i]->{'id'};
        }
    }

    # ���Ĥ���ʤ��ä����
    return -1;
}


#----------------------------------------------------------------------
# Ʊ���ο��������⡼��
#----------------------------------------------------------------------
# �������ѹ��ᥤ��
sub makeAllyMain {

    my ($adminMode) = 0;
    # �ѥ���ɥ����å�
    if (checkSpecialPassword($HoldPassword)) {
        $adminMode = 1;
        if ($HallyID > 200) {
            my $max = $HallyID;
            if ($HallyNumber) {
                foreach (0..$#Hally) {
                    $max = $Hally[$_]->{'id'} + 1 if($max <= $Hally[$_]->{'id'});
                }
            }

            $HcurrentID = $max;
        } elsif(defined $HcurrentAnumber) {
            $HcurrentID = $Hally[$HcurrentAnumber]->{'id'};
        } else {
            unlock();
            out("${HtagBig_}����or�ѹ��Ǥ��ޤ���<br>${adminMode}/${HcurrentAnumber}/${HallyID}<br>${H_tagBig}$HtempBack");
            return;
        }
    }

    # Ʊ��̾�����뤫�����å�
    if ($HallyName eq '') {
        unlock();
        $AfterName = 'Ʊ��';
        tempNewIslandNoName();
        return;
    }

    # Ʊ��̾�������������å�
    if ($HallyName =~ /[,\?\(\)\<\>\$]|^̵��|^����$/) {
        # �Ȥ��ʤ�̾��
        unlock();
        tempNewIslandBadOwnerName();
        return;
    }

    # ̾���ν�ʣ�����å�
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    if (!($adminMode && ($HallyID ne '') && ($HallyID < 200)) &&
        ((nameToNumber($HallyName) != -1) ||
        ((aNameToId($HallyName) != -1) && (aNameToId($HallyName) != $HcurrentID)))) {
        # ���Ǥ˷�������
        unlock();
        tempNewAllyAlready();
        return;
    }

    # �ޡ����ν�ʣ�����å�
    if (!($adminMode && ($HallyID ne '') && ($HallyID < 200)) &&
        ((aMarkToId($HallyMark) != -1) && (aMarkToId($HallyMark) != $HcurrentID))) {
        # ���Ǥ˻��Ѥ���
        unlock();
        tempMarkAllyAlready();
        return;
    }

    # password��Ƚ��
    my ($island) = $Hislands[$HcurrentNumber];
    if (!$adminMode && !checkPassword($island,$HinputPassword)) {
        unlock();
        tempWrongPassword();
        return;
    }

    if (!$adminMode && $island->{'money'} < $HcostMakeAlly) {
        unlock();
        tempNoMoney();
        return;
    }

    my ($n) = $HidToAllyNumber{$HcurrentID};

    if (defined $n) {
        if (   ($adminMode)
            && ($HallyID ne '')
            && ($HallyID < 200) ) {

            my $allyMember = $Hally[$n]->{'memberId'};
            my $aIsland = $Hislands[$HidToNumber{$HallyID}];
            my ($flag) = 0;

            foreach (@$allyMember) {
                if ($_ == $HallyID) {
                    $flag = 1;
                    last;
                }
            }

            if (!$flag) {
                $flag = 2 if(@{$aIsland->{'allyId'}}[0] eq '');
            }

            if (!$flag) {
                unlock();
                out("${HtagBig_}�ѹ��Ǥ��ޤ���${H_tagBig}$HtempBack");
                return;
            }

            $Hally[$n]->{'id'}       = $HallyID;
            $Hally[$n]->{'oName'}    = $aIsland->{'name'};
            if ($flag == 2) {
                $Hally[$n]->{'password'} = $aIsland->{'password'};
                $Hally[$n]->{'score'}    = $aIsland->{'pts'};
                $Hally[$n]->{'number'}++;
                push(@{$Hally[$n]->{'memberId'}}, $aIsland->{'id'});
                push(@{$aIsland->{'allyId'}}, $aIsland->{'id'});
            }
        } else {
            # ���Ǥ˷������ߤʤ��ѹ�
            logChangeAlly($Hally[$n]->{'name'}, $HallyName) if(!$adminMode && ($Hally[$n]->{'name'} ne $HallyName));
        }

    } else {
        # ¾�����Ʊ�������äƤ�����ϡ������Ǥ��ʤ�
        my ($flag) = 0;
        for ($i = 0; $i < $HallyNumber; $i++) {
            my ($allyMember) = $Hally[$i]->{'memberId'};
            foreach (@$allyMember) {
                if ($_ == $HcurrentID) {
                    $flag = 1;
                    last;
                }
            }
            last if ($flag);
        }

        if ($flag) {
            unlock();
            tempOtherAlready();
            return;
        }

        # ����
        $n = $HallyNumber;
        $Hally[$n]->{'id'} = $HcurrentID;
        my @memberId = ();
        if ($HallyID < 200) {

            $Hally[$n]->{'oName'}    = $island->{'name'};
            $Hally[$n]->{'password'} = $island->{'password'};
            $Hally[$n]->{'number'}   = 1;
            @memberId = ($HcurrentID);
            $Hally[$n]->{'score'}    = $island->{'pts'};

        } else {
            $Hally[$n]->{'oName'}    = '';
            $Hally[$n]->{'password'} = encode($HinputPassword);
            $Hally[$n]->{'number'}   = 0;
            $Hally[$n]->{'score'}    = 0;
        }

        $Hally[$n]->{'Takayan'}  = makeRandomString();
        $Hally[$n]->{'occupation'} = 0;
        $Hally[$n]->{'memberId'} = \@memberId;
        $island->{'allyId'} =  \@memberId;
        my @ext = (0, 0, 0);
        $Hally[$n]->{'ext'}      = \@ext;
        $HidToAllyNumber{$HcurrentID} = $n;
        $HallyNumber++;
        logMakeAlly($HallyName, islandName($island)) if(!$adminMode); # ��
    }

    # Ʊ���γƼ���ͤ�����
    $Hally[$n]->{'name'}     = $HallyName;
    $Hally[$n]->{'mark'}     = $HallyMark;
    $Hally[$n]->{'color'}    = "#${HallyColor}";

    # ���Ѥ򤤤�����
    $island->{'money'} -= $HcostMakeAlly if(!$adminMode);
    # �ǡ����񤭽Ф�
    allyOccupy();
    allySort();
    writeIslandsFile();
    $HislandList = getIslandList($HcurrentID, 0);

    # ����
    unlock();
    # �ȥåפ�
    topPageMain();
}


#----------------------------------------------------------------------
# ���Ǥˤ���̾����Ʊ����������
sub tempNewAllyAlready {
    out(<<END);
${HtagBig_}����Ʊ���ʤ餹�Ǥ˷�������Ƥ��ޤ���${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# ���Ǥˤ��Υޡ�����Ʊ����������
sub tempMarkAllyAlready {
    out(<<END);
${HtagBig_}���Υޡ����Ϥ��Ǥ˻��Ѥ���Ƥ��ޤ���${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# �̤�Ʊ����������Ƥ���
sub tempLeaderAlready {
    out(<<END);
${HtagBig_}����ϡ���ʬ��Ʊ���ʳ��ˤϲ����Ǥ��ޤ���${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# ���֤��Ƥ����������ʤ���
sub tempAbsent {
    out(<<END);
${HtagBig_}�����������줿�硢�⤷���ϡ�10�����������饳�ޥ�ɤ���ⷫ����ä����ᡢ�����Ǥ��ޤ���${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# �̤�Ʊ���˲������Ƥ���
sub tempOtherAlready {
    out(<<END);
${HtagBig_}�ҤȤĤ�Ʊ���ˤ��������Ǥ��ޤ���${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# ���­�ꤺ
sub tempNoMoney {
    out(<<END);
${HtagBig_}�����­�Ǥ�(/_<��)${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# ��
sub deleteAllyMain {

    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];
    my ($n) = $HidToAllyNumber{$HcurrentID};
    my ($adminMode) = 0;

    # �ѥ���ɥ����å�
    if (checkSpecialPassword($HoldPassword)) {

        $n = $HcurrentAnumber;
        $HcurrentID = $Hally[$n]->{'id'};
        $adminMode = 1;

    } else {

        # password��Ƚ��
        if (!checkPassword($island,$HinputPassword)) {
            unlock();
            tempWrongPassword();
            return;
        }

        if (!checkPassword($Hally[$n],$HinputPassword)) {
            unlock();
            tempWrongPassword();
            return;
        }

        # ǰ�Τ���ID������å�
        if ($Hally[$n]->{'id'} != $HcurrentID) {
            unlock();
            tempWrongAlly();
            return;
        }
    }

    # HarmisticeTurn �����
    my $allyMember = $Hally[$n]->{'memberId'};
    if (   $adminMode
        && (   (@{$allyMember}[0] ne '')
            || !(defined $n))
                                ){
        unlock();
        out("${HtagBig_}����Ǥ��ޤ���${H_tagBig}$HtempBack");
        out("n = ${n} / allyMember : @{$allyMember}[0]");
        return;
    }

    foreach (@$allyMember) {
        my($island, $aId, @newId);
        $island = $Hislands[$HidToNumber{$_}];
        @newId = ();

        foreach $aId (@{$island->{'allyId'}}) {
            if ($aId != $HcurrentID) {
                push(@newId, $aId);
            }
        }
        $island->{'allyId'} = \@newId;
    }

    logDeleteAlly($Hally[$n]->{'name'}) if(!$adminMode);
    $Hally[$n]->{'dead'} = 1;
    $HidToAllyNumber{$HcurrentID} = undef;
    $HallyNumber--;
    unlink("${HallychatData}$HcurrentID.cht") if(-e "${HallychatData}$HcurrentID.cht");     # ����åȥǡ�������

    # �ǡ����񤭽Ф�
    allyOccupy();
    allySort();
    writeIslandsFile();
    $HislandList = getIslandList($HcurrentID, 0);

    # ����
    unlock();
    # �ȥåפ�
    topPageMain();
}


#----------------------------------------------------------------------
# �ºݤκ��
sub DeleteAlly{


}


#----------------------------------------------------------------------
# ID�����å��ˤҤä�����
sub tempWrongAlly {

    out(<<END);
${HtagBig_}���ʤ�������ǤϤʤ��Ȼפ���${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# ������æ��
sub joinAllyMain {

    # password��Ƚ��
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];
    if (!checkPassword($island,$HinputPassword)) {
        unlock();
        tempWrongPassword();
        return;
    }

    # �ۤ���Ʊ���˻��ä��Ƥ��롣
    if (defined $HidToAllyNumber{$HcurrentID}) {
        unlock();
        tempLeaderAlready();
        return;
    }

    # �������ޤ��ϡ����ֵ�̣��Ʊ���ϤǤ��ʤ���
    if ($island->{'absent'} > 10) {
        unlock();
        tempAbsent();
        return;
    }

    my $ally = $Hally[$HcurrentAnumber];
    if(   ($HallyJoinOne)
       && ($island->{'allyId'}[0] != 0 )
       && ($island->{'allyId'}[0] != $ally->{'id'}) ) {
        unlock();
        tempOtherAlready();
        return;
    }

    my ($allyMember) = $ally->{'memberId'};
    my @newAllyMember = ();
    my ($flag) = 0;

    foreach (@$allyMember) {

        if (!(defined $HidToNumber{$_})) {
        } elsif($_ == $HcurrentID) {
            $flag = 1;
        } else {
            push(@newAllyMember, $_);
        }
    }

    if ($flag) {
        my @newAlly = ();
        logAllyEnd(islandName($island), $ally->{'name'});

        foreach (@{$island->{'allyId'}}) {
            if ($_ != $ally->{'id'}) {
                push(@newAlly, $_);
            }
        }
        $island->{'allyId'} = \@newAlly;
        $ally->{'score'} -= $island->{'pts'};
        $ally->{'number'}--;

    } else {

        logAlly(islandName($island), $ally->{'name'});
        push(@newAllyMember, $HcurrentID);
        push(@{$island->{'allyId'}}, $ally->{'id'});
        $ally->{'score'} += $island->{'pts'};
        $ally->{'number'}++;
    }
    $island->{'ally_turn'} = 0;
    $island->{'money'} -= $HcomCost[$HcomAlly];
    $ally->{'memberId'} = \@newAllyMember;
    # �ǡ����񤭽Ф�
    allyOccupy();
    allySort();
    writeIslandsFile();
    $HislandList = getIslandList($HcurrentID, 0);

    # ����
    unlock();
    # �ȥåפ�
    topPageMain();
}


#----------------------------------------------------------------------
# ����
sub logMakeAlly {
    my ($name, $owner) = @_;
    logHistory("Ʊ����${HtagName_}${name}${H_tagName}�٤�${HtagName_}${owner}${H_tagName}�ˤ�ä�${HtagNumber_}����${H_tagNumber}����롣");
}


#----------------------------------------------------------------------
# �ѹ�
sub logChangeAlly {
    my ($oldname, $newname) = @_;
    logHistory("Ʊ����${HtagName_}${oldname}${H_tagName}�פ���${HtagName_}${newname}${H_tagName}�٤�̾���ѹ���");
}


#----------------------------------------------------------------------
# ��
sub logDeleteAlly {
    my ($name) = @_;
    logHistory("Ʊ����${HtagName_}${name}${H_tagName}�٤�${HtagDisaster_}�򻶡�${H_tagDisaster}");
}


#----------------------------------------------------------------------
# ����
sub logAlly {
    my ($name, $allyName) = @_;
    logHistory("${HtagName_}${name}${H_tagName}����${HtagName_}${allyName}${H_tagName}�٤�${HtagNumber_}����${H_tagNumber}��");
}


#----------------------------------------------------------------------
# æ��
sub logAllyEnd {
    my ($name, $allyName) = @_;
    logHistory("${HtagName_}${name}${H_tagName}����${HtagName_}${allyName}${H_tagName}�٤���${HtagDisaster_}æ�ࡪ${H_tagDisaster}");
}


#----------------------------------------------------------------------
# Ʊ���η������ѹ����򻶡�������æ��
#----------------------------------------------------------------------
# �������ѹ����򻶡�������æ��
sub newAllyTop {

    my ($adminMode) = 0;
    # �ѥ���ɥ����å�
    if (checkSpecialPassword($HdefaultPassword)) {
        $adminMode = 1;
        $HislandList = getIslandList($Hislands[$HbfieldNumber]->{'id'}, 1);
    }
    # ����
    unlock();
    my ($jsIslandList, $name, $id, $i);

    foreach $i (0..$islandNumber) {
        $name = htmlEscape($Hislands[$i]->{'name'});
        $id = $Hislands[$i]->{'id'};
        $jsIslandList .= "island[$id] = \"$name\"\;\n";
    }

    my ($allyname, $markList, @colorList, @allycolor, $allyList, 
        $jsAllyList, $jsAllyIdList, $jsAllyMarkList, $jsAllyColorList);
    my ($defaultMark, $defaultAllyId);
    my ($n) = $HidToAllyNumber{$defaultID};
    if ($n eq '') {
        $allyname = '';
        $defaultMark = $Hally[0];
        $defaultAllyId= '';
    } else {
        $allyname = $Hally[$n]->{'name'};
        $defaultMark = $Hally[$n]->{'mark'};
        $defaultAllyId = $Hally[$n]->{'id'};
    }

    foreach (0..$#HallyMark) {
        my ($s) = '';
        $s = ' SELECTED' if($HallyMark[$_] eq $defaultMark);
        $markList .= "<OPTION VALUE=\"$HallyMark[$_]\"$s>$HallyMark[$_]\n"
    }

    foreach $i (1..6) {
        if ($n eq '') {
            $allycolor[$i] = 0;
        } else {
            $allycolor[$i] = substr($Hally[$n]->{'color'}, $i, 1);
        }
        foreach (0..9,A..F) {
            my ($s) = '';
            $s = ' SELECTED' if($_ eq $allycolor[$i]);
            $colorList[$i] .= "<OPTION VALUE=\"$_\"$s>$_\n"
        }
    }

    my $max = 201;

    if ($HallyNumber) {
        $jsAllyList = "ally = [";
        $jsAllyIdList = "allyID = [";
        $jsAllyMarkList = "allyMark = [";
        $jsAllyColorList = "allyColor = [";

        foreach (0..$#Hally) {
            my ($s) = '';
            $s = ' SELECTED' if($Hally[$_]->{'id'} == $defaultAllyId);
            $allyList .= "<OPTION VALUE=\"$_\"$s>$Hally[$_]->{'name'}\n";
            $jsAllyList .= "'$Hally[$_]->{'name'}'";
            $jsAllyIdList .= "$Hally[$_]->{'id'}";
            $jsAllyMarkList .= "'$Hally[$_]->{'mark'}'";
            $jsAllyColorList .= "[";

            foreach $i (1..6) {
                $jsAllyColorList .= '\'' . substr($Hally[$_]->{'color'}, $i, 1) . '\'';
                $jsAllyColorList .= ',' if($i < 6);
            }

            $jsAllyColorList .= "]";
            if ($_ < $#Hally) {
                $jsAllyList .= ",\n";
                $jsAllyIdList .= ",\n";
                $jsAllyMarkList .= ",\n";
                $jsAllyColorList .= ",\n";
            }
            $max = $Hally[$_]->{'id'} + 1 if($max <= $Hally[$_]->{'id'});
        }
        $jsAllyList .= "];\n";
        $jsAllyIdList .= "];\n";
        $jsAllyMarkList .= "];\n";
        $jsAllyColorList .= "];\n";
    }
    my $str1 = $adminMode ? '(���ƥʥ�)' : $HallyJoinComUse ? '' : '��������æ��';
    my $str2 = $adminMode ? '' : 'onChange=colorPack() onClick=colorPack()';
    my $makeCost = $HcostMakeAlly ? "${HcostMakeAlly}${HunitMoney}" : '̵��';
    my $keepCost = $HcostKeepAlly ? "${HcostKeepAlly}${HunitMoney}" : '̵��';
    my $joinCost = $HcomCost[$HcomAlly] ? "${$HcomCost[$HcomAlly]}${HunitMoney}" : '̵��';
    my $joinStr = $HallyJoinComUse ? '' : "������æ��κݤ����Ѥϡ�${HtagMoney_}$joinCost${H_tagMoney}�Ǥ���<BR>";
    my $str3 = $adminMode ? "�ü�ѥ���ɤϡ���ɬ�ܡ�<BR>
<INPUT TYPE=\"password\" NAME=\"OLDPASS\" VALUE=\"$HdefaultPassword\" SIZE='32' MAXLENGTH='32' class='f'><BR>Ʊ��" : "<span class='attention'>(���)</span><BR>
Ʊ���η������ѹ������Ѥϡ�${HtagMoney_}${makeCost}${H_tagMoney}�Ǥ���<BR>
�ޤ����西����ɬ�פȤ����ݻ����${HtagMoney_}$keepCost${H_tagMoney}�Ǥ���<BR>
�ʰݻ����Ʊ���˽�°����${AfterName}�Ƕ�������ô���뤳�Ȥˤʤ�ޤ���<BR>
$joinStr
</P>
���ʤ�����ϡ���ɬ�ܡ�a<BR>
<SELECT NAME=\"ISLANDID\" $str2>
$HislandList
</SELECT><BR>���ʤ�";

    out(<<END);
<DIV align='center'>$HtempBack</DIV><BR>
<DIV ID='changeInfo'>
<H1>Ʊ���η������ѹ�����${str1}</H1>
<table border=0 width="50%"><tr><td class="M"><P>
<FORM name="AcForm" action="$HthisFile" method="POST">
$str3�Υѥ���ɤϡ���ɬ�ܡ�<BR>
<INPUT TYPE="text" NAME="PASSWORD" SIZE="32" VALUE="$HdefaultPassword" MAXLENGTH="32" class="f">
END

    if ($HallyNumber) {
        my $str4 = $adminMode ? '���������ѹ�' : $HallyJoinComUse ? '' : '��������æ��';
        my $str5 = ($adminMode || $HallyJoinComUse) ? '' : '<INPUT TYPE="submit" VALUE="������æ��" NAME="JoinAllyButton">';
        out(<<END);
<BR>
<BR><B><FONT SIZE=4>�β�${str4}��</FONT></B>
<BR>�ɤ�Ʊ���Ǥ�����<BR>
<SELECT NAME="ALLYNUMBER" onChange=allyPack() onClick=allyPack()>
$allyList
</SELECT>
<BR>
<INPUT TYPE="submit" VALUE="��" NAME="DeleteAllyButton">
$str5
<BR>
END
    }

    my $str7 = $adminMode ? "��������ѹ�(��Υ�˥塼��Ʊ��������)<BR> or Ʊ���ο�������(��Υ�˥塼��̵��)<BR><SELECT NAME=\"ALLYID\"><OPTION VALUE=\"$max\">��������\n$HislandList</SELECT><BR>" : '<BR><B><FONT SIZE=4>�η������ѹ���</FONT></B><BR>';
    out(<<END);
<BR>
$str7
Ʊ����̾�����ѹ���<small>(����${HlengthAllyName}���ޤ�)</small><BR>
<INPUT TYPE="text" NAME="ALLYNAME" VALUE="$allyname" SIZE="32" MAXLENGTH="32"><BR>
�ޡ������ѹ���<BR>
<SELECT NAME="MARK" onChange=colorPack() onClick=colorPack()>
$markList
</SELECT>
<ilayer name="PARENT_CTBL" width="100%" height="100%">
   <layer name="CTBL" width="200"></layer>
   <span id="CTBL"></span>
</ilayer>
<BR>
�ޡ����ο������ɡ��ѹ���<BR><TABLE BORDER=0><TR>
<TD align='center'>RED</TD>
<TD align='center'>GREEN</TD>
<TD align='center'>BLUE</TD>
</TR><TR>
<TD><SELECT NAME="COLOR1" onChange=colorPack() onClick=colorPack()>
$colorList[1]</SELECT><SELECT NAME="COLOR2" onChange=colorPack() onClick=colorPack()>
$colorList[2]</SELECT></TD>
<TD><SELECT NAME="COLOR3" onChange=colorPack() onClick=colorPack()>
$colorList[3]</SELECT><SELECT NAME="COLOR4" onChange=colorPack() onClick=colorPack()>
$colorList[4]</SELECT></TD>
<TD><SELECT NAME="COLOR5" onChange=colorPack() onClick=colorPack()>
$colorList[5]</SELECT><SELECT NAME="COLOR6" onChange=colorPack() onClick=colorPack()>
$colorList[6]</SELECT></TD>
</TR></TABLE>
<INPUT TYPE="submit" VALUE="����(�ѹ�)" NAME="NewAllyButton">
<SCRIPT language="JavaScript">
<!--
END
    if (!$adminMode) {
        out(<<END);
function colorPack() {
	var island = new Array(128);
$jsIslandList
	a = document.AcForm.COLOR1.value;
	b = document.AcForm.COLOR2.value;
	c = document.AcForm.COLOR3.value;
	d = document.AcForm.COLOR4.value;
	e = document.AcForm.COLOR5.value;
	f = document.AcForm.COLOR6.value;
	mark = document.AcForm.MARK.value;
	number = document.AcForm.ISLANDID.value;

	str = "#" + a + b + c + d + e + f;
//	document.AcForm.AcColorValue.value = str;
	str = 'ɽ������ץ롧��<B><span class="number"><FONT color="' + str +'">' + mark + '</FONT></B>'
	  + island[number] + '${AfterName}</span>��';
	
	if(document.getElementById){
		document.getElementById("CTBL").innerHTML = str;
	} else if(document.all){
		el = document.all("CTBL");
		el.innerHTML = str;
	} else if(document.layers) {
		lay = document.layers["PARENT_CTBL"].document.layers["CTBL"];
		lay.document.open();
		lay.document.write(str);
		lay.document.close(); 
	}

	return true;
}
function allyPack() {
$jsAllyList
$jsAllyMarkList
$jsAllyColorList
	document.AcForm.ALLYNAME.value = ally[document.AcForm.ALLYNUMBER.value];
	document.AcForm.MARK.value     = allyMark[document.AcForm.ALLYNUMBER.value];
	document.AcForm.COLOR1.value   = allyColor[document.AcForm.ALLYNUMBER.value][0];
	document.AcForm.COLOR2.value   = allyColor[document.AcForm.ALLYNUMBER.value][1];
	document.AcForm.COLOR3.value   = allyColor[document.AcForm.ALLYNUMBER.value][2];
	document.AcForm.COLOR4.value   = allyColor[document.AcForm.ALLYNUMBER.value][3];
	document.AcForm.COLOR5.value   = allyColor[document.AcForm.ALLYNUMBER.value][4];
	document.AcForm.COLOR6.value   = allyColor[document.AcForm.ALLYNUMBER.value][5];
	colorPack();
	return true;
}
END
    } else {
        out(<<END);
function colorPack() {
	var island = new Array(128);
$jsIslandList
	a = document.AcForm.COLOR1.value;
	b = document.AcForm.COLOR2.value;
	c = document.AcForm.COLOR3.value;
	d = document.AcForm.COLOR4.value;
	e = document.AcForm.COLOR5.value;
	f = document.AcForm.COLOR6.value;
	mark = document.AcForm.MARK.value;

	str = "#" + a + b + c + d + e + f;
//	document.AcForm.AcColorValue.value = str;
	str = 'ɽ������ץ롧��<B><span class="number"><FONT color="' + str +'">' + mark + '</FONT></B>'
	  + '����פ�${AfterName}</span>��';
	
	if(document.getElementById){
		document.getElementById("CTBL").innerHTML = str;
	} else if(document.all){
		el = document.all("CTBL");
		el.innerHTML = str;
	} else if(document.layers) {
		lay = document.layers["PARENT_CTBL"].document.layers["CTBL"];
		lay.document.open();
		lay.document.write(str);
		lay.document.close(); 
	}

	return true;
}
function allyPack() {
$jsAllyList
$jsAllyIdList
$jsAllyMarkList
$jsAllyColorList
	document.AcForm.ALLYID.value   = allyID[document.AcForm.ALLYNUMBER.value];
	document.AcForm.ALLYNAME.value = ally[document.AcForm.ALLYNUMBER.value];
	document.AcForm.MARK.value     = allyMark[document.AcForm.ALLYNUMBER.value];
	document.AcForm.COLOR1.value   = allyColor[document.AcForm.ALLYNUMBER.value][0];
	document.AcForm.COLOR2.value   = allyColor[document.AcForm.ALLYNUMBER.value][1];
	document.AcForm.COLOR3.value   = allyColor[document.AcForm.ALLYNUMBER.value][2];
	document.AcForm.COLOR4.value   = allyColor[document.AcForm.ALLYNUMBER.value][3];
	document.AcForm.COLOR5.value   = allyColor[document.AcForm.ALLYNUMBER.value][4];
	document.AcForm.COLOR6.value   = allyColor[document.AcForm.ALLYNUMBER.value][5];
	colorPack();
	return true;
}
END
	}
	out(<<END);
colorPack();
//-->
</SCRIPT>
</FORM>
</td></tr></table></DIV>
END
}


#----------------------------------------------------------------------
# ���祳���ȥ⡼��
sub allyPactMain {
    if (!$HallyPactMode) {
        # ����
        unlock();
        # �ƥ�ץ졼�Ƚ���
        tempAllyPactPage();
    } else {
        # �ѥ���ɥ����å�
        my $ally = $Hally[$HidToAllyNumber{$HcurrentID}];
        if (checkPassword($ally, $HdefaultPassword)) {

            $HallyComment =~ s/[\x00-\x1f\,]//g;
            $ally->{'comment'} = htmlEscape($HallyComment);
            $ally->{'title'} = htmlEscape($HallyTitle);
            $ally->{'message'} = htmlEscape($HallyMessage, 1);
            # �ǡ����񤭽Ф�
            writeAllyFile();
            unlock();
            # �ѹ�����
            tempAllyPactOK($ally->{'name'});
        } else {
            # password�ְ㤤
            unlock();
            tempWrongPassword();
            return;
        }
    }
}


#----------------------------------------------------------------------
# ���祳���ȥ⡼�ɤΥȥåץڡ���
sub tempAllyPactPage {
    my $ally = $Hally[$HidToAllyNumber{$HcurrentID}];
    my $allyMessage = $ally->{'message'};
    $allyMessage =~ s/<br>/\n/g;
    $allyMessage =~ s/&amp;/&/g;
    $allyMessage =~ s/&lt;/</g;
    $allyMessage =~ s/&gt;/>/g;
    $allyMessage =~ s/&quot;/\"/g; #"

    out(<<END);
<DIV align='center'>$HtempBack</DIV><BR>
<DIV ID='changeInfo'>
<H1>�������ѹ���$ally->{'name'}��</H1>
<table border=0 width="50%"><tr><td class="M">
<FORM action="$HthisFile" method="POST">
<B>����ѥ���ɤϡ�</B><BR>
<INPUT TYPE="password" NAME="Allypact" VALUE="$HdefaultPassword" SIZE=32 MAXLENGTH=32 class=f>
<INPUT TYPE="hidden"  NAME="ISLANDID" VALUE="$ally->{'id'}">
<INPUT TYPE="submit" VALUE="����" NAME="AllypactButton"><BR>
<B>������</B><small>(����${HlengthAllyComment}���ޤǡ��ȥåץڡ����Ρֳ�Ʊ���ξ��������ɽ������ޤ�)</small><BR>
<INPUT TYPE="text" NAME="ALLYCOMMENT"  VALUE="$ally->{'comment'}" SIZE="100" MAXLENGTH="50"><BR>
<BR>
<B>��å�����������ʤ�</B>(��Ʊ���ξ������ξ��ɽ������ޤ�)<BR>
�����ȥ�<small>(����${HlengthAllyTitle}���ޤ�)</small><BR>
<INPUT TYPE="text" NAME="ALLYTITLE"  VALUE="$ally->{'title'}" SIZE="100" MAXLENGTH="50"><BR>
��å�����<small>(����${HlengthAllyMessage}���ޤ�)</small><BR>
<TEXTAREA COLS=50 ROWS=16 NAME="ALLYMESSAGE" WRAP="soft">$allyMessage</TEXTAREA>
<BR>
�֥����ȥ�פ����ˤ���ȡ����礫��Υ�å������٤Ȥ��������ȥ�ˤʤ�ޤ���<BR>
�֥�å������פ����ˤ���ȡ�Ʊ���ξ������ˤϲ���ɽ������ʤ��ʤ�ޤ���
</FORM>
</td></tr></table>
</DIV>
END
}


#----------------------------------------------------------------------
# ���祳�����ѹ���λ
sub tempAllyPactOK {
    my($name) = @_;
    out(<<END);
${HtagBig_}$name${AfterName}�Υ����Ȥ��ѹ����ޤ�����${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# Ʊ��(�ر�)����
#----------------------------------------------------------------------
sub amitySetupMain() {
    if (!$HasetupMode) {
        # ����
        unlock();

        # �ƥ�ץ졼�Ƚ���
        tempAmitySetupPage();

    } else {
        # �ѥ���ɥ����å�
        if (checkSpecialPassword($HdefaultPassword)) {
            # �ü�ѥ����
            my ($id, $aId);
            foreach (0..$islandNumber) {
                undef $Hislands[$_]->{'allyId'};
            }

            foreach (0..($HallyNumber - 1)) {
                undef $Hally[$_]->{'memberId'};
                undef $Hally[$_]->{'number'};
                undef $Hally[$_]->{'score'};
                my $aId = $Hally[$_]->{'id'};
                if (defined $HidToNumber{$aId}) {
                    push(@{$Hally[$_]->{'memberId'}}, $Hally[$_]->{'id'});
                    $Hally[$_]->{'score'} += $Hislands[$HidToNumber{$aId}]->{'pts'};
                    push(@{$Hislands[$HidToNumber{$aId}]->{'allyId'}}, $aId);
                }
            }

            foreach (@HallyChange) {
                ($id, $aId) = split(/-/, $_);
                $Hally[$HidToAllyNumber{$aId}]->{'score'} += $Hislands[$HidToNumber{$id}]->{'pts'};
                next if($id == $aId);
                push(@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}, $id);
                push(@{$Hislands[$HidToNumber{$id}]->{'allyId'}}, $aId);
            }

            foreach (0..($HallyNumber - 1)) {
                $Hally[$_]->{'number'} = @{$Hally[$_]->{'memberId'}};
            }
            allyOccupy();
            allySort();
            writeIslandsFile();
            unlock();
            # �ѹ�����
            tempAmitySetupPage();
        } else {
            # password�ְ㤤
            unlock();
            tempWrongPassword();
            return;
        }
    }
}


#----------------------------------------------------------------------
# Ʊ��(�ر�)����ڡ���
sub tempAmitySetupPage() {
    # ����
    unlock();

    out(<<END);
<DIV align='center'>$HtempBack</DIV><BR>
<DIV ID='campInfo'>
<H1>Ʊ��(�ر�)��°����</H1>
<FORM action="$HthisFile" method="POST">
<INPUT TYPE="hidden" VALUE="$HdefaultPassword" NAME="ASetup">
<TABLE BORDER><TR>
<TH $HbgTitleCell align="center" rowspan="2">${HtagTH_}����${H_tagTH}<BR><INPUT TYPE="submit" VALUE="�ѹ�" NAME="AmityChangeButton"></TD>
END

    foreach (0..$islandNumber) {
        $Hislands[$_]->{'ally'} = $Hislands[$_]->{'allyId'}[0];
    }

    my @idx = (0..$#Hislands);
    @idx = sort {
                $Hislands[$b]->{'field'} <=> $Hislands[$a]->{'field'} || # �Хȥ�ե������ͥ��
                $Hislands[$b]->{'ally'} <=> $Hislands[$a]->{'ally'} || # Ʊ���ǥ�����
                $a <=> $b # $kind��Ʊ���ʤ�����Τޤ�
           } @idx;

    my $aStr = ($HarmisticeTurn) ? '�ر�' : 'Ʊ��';
    out("<TH $HbgTitleCell align='center' colspan='$HallyNumber'>${HtagTH_}${aStr}${H_tagTH}</TH>") if($HallyNumber);
    out("</TR><TR>\n");
    my ($number, $island, $name, $ally);

    foreach (0..($HallyNumber - 1)) {
        $ally = $Hally[$_];
        $name = "<FONT COLOR=\"$ally->{'color'}\"><B>$ally->{'mark'}</B></FONT>$ally->{'name'}";
        out(<<END);
<TD class='T'>$name</TD>
END
    }
    out("</TR>\n");

    foreach (0..$islandNumber) {
        $island = $Hislands[$idx[$_]];
        $name = islandName($island);
        my($id, $amity, $aId);
        $id = $island->{'id'};
        out("<TR><TH $HbgTitleCell>$name</TH>");

        for ($i = 0; $i < $HallyNumber; $i++) {
            $ally  = $Hally[$i];
            $aId = $ally->{'id'};
            my $member = $Hally[$i]->{'memberId'};
            my $flag = 1;
            foreach (@$member) {
                if ($id == $_) {
                    $flag = 0;
                    last;
                }
            }

            if ($flag) {
                out("<TH><input type='checkbox' name='ally' value='$id-$aId'></TH>");
            } else {
                out("<TH><input type='checkbox' name='ally' value='$id-$aId' CHECKED></TH>");
            }
        }
        out("</TR>\n");
    }
    out(<<END);
</TABLE><INPUT TYPE="hidden" VALUE="dummy" NAME="AmityChange"></FORM></DIV>
END
}


#----------------------------------------------------------------------
# ���ƥ�ץ졼��
#----------------------------------------------------------------------
# ������̾�����ʤ����
sub tempNewIslandNoName {
    out(<<END);
${HtagBig_}${AfterName}�ˤĤ���̾����ɬ�פǤ���${H_tagBig}$HtempBack
END
}


# �����ǥ����ʡ�̾���ʤ����
sub tempNewIslandNoOwnerName {
    out(<<END);
${HtagBig_}���ʤ���̾����ɬ�פǤ���${H_tagBig}$HtempBack
END
}


# �����ǥ����ʡ�̾�������ʾ��
sub tempNewIslandBadOwnerName {
    out(<<END);
${HtagBig_}',?()<>\$'�����äƤ���̾���Ϥ��ޤ��礦��${H_tagBig}$HtempBack
END
}

1;
