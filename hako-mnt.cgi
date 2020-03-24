#!/usr/bin/perl
# ���ϥ����С��˹�碌���ѹ����Ʋ�������

#----------------------------------------------------------------------
# Ȣ����� ver2.30
# ���ƥʥ󥹥ġ���(ver1.01)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------

# ��������ѥե�������ɤ߹���
require './hako-init.cgi';
require './hako-io.cgi';
require './init-server.cgi';

# hako-mente.cgi ����ƥ֥饦���ǳ����ȡ��ޥ����ѥ���ɤ��ü�ѥ���ɤ�
# ���Ϥ��׵ᤵ��ޤ������������Ϥ��줿�ѥ���ɤϰŹ沽���졢�ѥ���ɥե�����
# �˵�������ޤ���

# �ѥ���ɤ��ѹ�������ϡ�FTP ����³���ƥѥ���ɥե�����������Ƥ���������
# ���θ塢hako-mente.cgi ��֥饦���ǳ����ƥѥ���ɤ������Ԥ��ޤ���
# �������ǥ�����ǡ���������뤳�ȤϤ���ޤ��󡣥�������Ǥ��ѹ��Ǥ��ޤ���

# ������������������������������������������������������������
# �Ƽ�������
# ������������������������������������������������������������

# ���Υե�����
my($thisFile) = './hako-mente.cgi';

# use Time::Local���Ȥ��ʤ��Ķ��Ǥϡ�'use Time::Local'�ιԤ�ä��Ʋ�������
# �����ˤ��Υե�����ΰ��ֺǸ�ǥ����ȥ����Ȥ��Ƥ���Time::Local �θߴ��ؿ�
# sub timelocal��ȤäƲ�������

use Time::Local;

# ������������������������������������������������������������
# ������ܤϰʾ�
# ������������������������������������������������������������
my $title   = 'Hakoniwa R.A. ���ƥʥ󥹥ġ���';

# �礭��ʸ��
my ($HtagBig_) = '<span class="big">';
my ($H_tagBig) = '</span>';
# ������������������������������������������������������������
# �ᥤ��
# ������������������������������������������������������������

# �Ƽ��ѿ�
my ($mainMode);
my ($mpass1, $mpass2, $spass1, $spass2);
my ($inputPass);
my ($inputPass);
my ($deleteID);
my ($currentID);
my ($ctYear);
my ($ctMon);
my ($ctDate);
my ($ctHour);
my ($ctMin);
my ($ctSec);

cookieInput();
cgiInput();
cookieOutput();

print <<END;
Content-type: text/html

<html>
<head>
  <title>Ȣ�����ң� ���ƥʥ󥹥ġ���</title>
  <meta http-equiv="Content-Type" content="text/html; charset=EUC-JP">
  <meta name="theme-color" content="#99FF99">
  <link rel="shortcut icon" href="./img/fav.ico">
  <link rel="stylesheet" type="text/css" href="${efileDir}/$HcssFile">
</head>
<body>
END

if (-e $HpasswordFile) {
    # �ѥ���ɥե����뤬����
    open(PIN, "<$HpasswordFile") || die $!;
    chomp($HmasterPassword = <PIN>); # �ޥ����ѥ���ɤ��ɤ߹���
    close(PIN);
}

if ($mainMode eq 'delete') {
    if(passCheck()) {
        deleteMode();
    }
} elsif ($mainMode eq 'current') {
    if (passCheck()) {
        currentMode();
    }
} elsif ($mainMode eq 'time') {
    if (passCheck()) {
        timeMode();
    }
} elsif ($mainMode eq 'stime') {
    if (passCheck()) {
        stimeMode();
    }
} elsif ($mainMode eq 'new') {
    if (passCheck()) {
        newMode();
    }
} elsif ($mainMode eq 'setup') {
    setupMode();
} elsif ($mainMode eq 'allylog') {
    if (passCheck()) {
        allyLogMain();
    }
} elsif ($mainMode eq 'dellog') {
    if (passCheck()) {
        dellogMode();
    }
}

if (($mainMode eq 'admin' || $dellcheck) && (passCheck())) {
    adminMode();
} elsif (($mainMode ne 'allylog') && ($mainMode ne 'dellog')) {
    mainMode();
}
print <<END;
</form>
</body>
</html>
END

# ----------------------------------------------------
#
# myrmtree
#
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


# ----------------------------------------------------
#
# currentMode
#
sub currentMode {
    myrmtree "${HdirName}";
    mkdir("${HdirName}", $HdirMode);
    opendir(DIN, "${HdirName}.bak$currentID/");
    my ($fileName);
    while ($fileName = readdir(DIN)) {
        fileCopy("${HdirName}.bak$currentID/$fileName", "${HdirName}/$fileName");
    }
    closedir(DIN);
}


# ----------------------------------------------------
#
# deleteMode
#
sub deleteMode {
    if ($deleteID eq '') {
        myrmtree "${HdirName}";
    } else {
        myrmtree "${HdirName}.bak$deleteID";
    }
    unlink "hakojimalockflock";
}


# ----------------------------------------------------
#
# newMode
#
sub newMode {
    mkdir($HdirName, $HdirMode);
    # ���ߤλ��֤����
    my ($now) = time;
    $now = $now - ($now % ($HunitTime));

    open(OUT, ">$HdirName/$HmainData"); # �ե�����򳫤�
    print OUT "0\n";         # �������0
    print OUT "$now\n";      # ���ϻ���
    print OUT "0\n";         # ��ο�
    print OUT "1\n";         # ���˳�����Ƥ�ID

    # �ե�������Ĥ���
    close(OUT);
}


# ----------------------------------------------------
#
# setupMode
#
sub setupMode {
    if (!($mpass1 && $mpass2) || ($mpass1 ne $mpass2)) {
        print "${HtagBig_}�ޥ����ѥ���ɤ����Ϥ���Ƥ��ʤ����ְ�äƤ��ޤ�${H_tagBig}";
        return;
    }
    if (!($spass1 && $spass2) || ($spass1 ne $spass2)) {
        print "${HtagBig_}�ü�ѥ���ɤ����Ϥ���Ƥ��ʤ����ְ�äƤ��ޤ�${H_tagBig}";
        return;
    }

    if (-e $HpasswordFile) {
        # �������ƥ����ۡ���Υ����å�
        print "${HtagBig_}���Ǥ˥ѥ���ɤ����ꤵ��Ƥ��ޤ�${H_tagBig}";
        return;
    }

    $mpass1 = crypt($mpass1, 'ma');
    $spass1 = crypt($spass1, 'sp');

    open(OUT, ">$HpasswordFile") || die $!;
    print OUT <<END;
$mpass1
$spass1
END
    close(OUT);
    print "${HtagBig_}�ѥ���ɤ����ꤷ�ޤ���${H_tagBig}";
}


# ----------------------------------------------------
#
# timeMode
#
sub timeMode {
    $ctMon--;
    $ctYear -= 1900;
    $ctSec = timelocal($ctSec, $ctMin, $ctHour, $ctDate, $ctMon, $ctYear);
    stimeMode();
}

# ----------------------------------------------------
#
# stimeMode
#
sub stimeMode {
    my ($t) = $ctSec;
    open(IN, "${HdirName}/$HmainData");
    my (@lines);
    @lines = <IN>;
    close(IN);

    $lines[1] = "$t\n";

    open(OUT, ">${HdirName}/$HmainData");
    print OUT @lines;
    close(OUT);
}


# ----------------------------------------------------
#
# mainMode
#
sub mainMode {
    print <<END;
<form action="$HmenteFile" method="POST">
<h1>$title</h1>
END

    unless (-e $HpasswordFile) {
        # �ѥ���ɥե����뤬�ʤ�
        print <<END;
<h2>�ޥ����ѥ���ɤ��ü�ѥ���ɤ���Ƥ���������</h2>
<p>�����ϥߥ����ɤ�����ˡ����줾�죲�󤺤����Ϥ��Ƥ���������</p><b>�ޥ����ѥ���ɡ�</b><br>
(1) <input type="password" name="MPASS1" value="$mpass1">&nbsp;&nbsp;(2) <INPUT type="password" name="MPASS2" value="$mpass2"><br>
<br>
<b>�ü�ѥ���ɡ�</b><br>
(1) <INPUT type="password" name="SPASS1" value="$spass1">&nbsp;&nbsp;(2) <INPUT type="password" name="SPASS2" value="$spass2"><br>
<br>
<input type="submit" value="done" name="SETUP">
END
        return;
    }
    $inputPass = $HdefaultPassword if ($inputPass eq '');
    print <<END;
<b>�ޥ����ѥ���ɡ�</b><input type="password" size="32" maxlength="32" name="PASSWORD" value="$inputPass">
<input type="submit" value="�����ͼ�������" name="ADMIN">
END

    opendir(DIN, "./");

    # ����ǡ���
    if (-d "${HdirName}") {
        dataPrint("");
    } else {
        print <<END;
  <hr>
  <input type="submit" value="�������ǡ�������" name="NEW">
END
    }

    # �Хå����åץǡ���
    my ($dn);
    while ($dn = readdir(DIN)) {
        if ($dn =~ /^${HdirName}.bak(.*)/) {
            dataPrint($1);
        }
    }
    closedir(DIN);
}


# ----------------------------------------------------
# �����ͼ�
sub adminMode {
    print <<END;
<h1>Ȣ�����ң� �����ͼ�</h1>
<hr>
END
    if ($Hbbs eq "${HbaseDir}/hako-yy-bbs.cgi") {
        print "[<A HREF=\"$Hbbs\" target=\"_blank\">�Ǽ���</A>(<A HREF=\"$Hbbs?id=0&cpass=${inputPass}\" target=\"_blank\">�����⡼��</A>)] ";
    }
    else {
        print "[<A HREF=\"$Hbbs\" target=\"_blank\">�Ǽ���</A>] ";
    }
    print <<END;
[<a href="$HthisFile?Rekidai=0" target="_blank">�����¿�͸���Ͽ</a>] 
[<a href="$HthisFile?Rank=0" target="_blank">��󥭥�</a>] 
END
    if (!$HhtmlLogMode || !(-e "${HhtmlDir}/hakolog.html") || $Hgzip) {
        print "[<a href=\"${HbaseDir}/history.cgi?Event=0\" target=\"_blank\">�Ƕ�ν����</a>] ";
    }
    else {
        print "[<a href=\"${htmlDir}/hakolog.html\" target=\"_blank\">�Ƕ�ν����</a>] ";
    }
    print <<END;
<hr>
<h3><span class="attention">���ʲ��κ�Ȥϡ������ֺݤ˹Ԥ������˴��Ǥ���</span></h3>
END

    print <<END;
<h2><a href="${HlbbsFile}?pass=" target="_blank">�Ѹ����̿�����ɽ</A>(<A HREF="${HlbbsFile}?pass=${inputPass}" target="_blank">�����ͥ⡼��</A>)</H2>
<ul>
  <li>lbbslist.cgi�����֤��Ƥ����硢�����üԤδѸ����̿������������Ǥ��ޤ���<br>
  <li>���Υ�����ץȤϡ������Ф���٤�������Ȼפ���١����ˤ˥������������ꡢ����ɤʤɤι԰٤ϤǤ������������褦�ˤ��ޤ��礦��
  <li>�����ͥ⡼�ɤ�����ȡ������̿��򸫤뤳�Ȥ��Ǥ��ޤ��������͸��¤�����ȸ��äƤ���ޤ������������衣<br>��COOKIE�˥ޥ������ѥ���ɶ��äƤ�����̤˥����������Ƥ�ִ����ͥ⡼�ɡפˤʤ�ޤ���
</ul>
END

    print <<END if (USE_EX_LBBS);
<h2><a href="${HlbbsDir}/view.cgi" target="_blank">�����ʰ׷Ǽ��Ĥ��������</A>(<A HREF="${HlbbsDir}/view.cgi?admin=${HviewPass}" target="_blank">�����ͥ⡼��</A>)</H2>
<ul>
  <li>�������(hako-init.cgi)�ǡֳ����ʰ׷Ǽ��Ĥ���Ѥ���פ褦�ˤ��Ƥ��ʤ���С����Ƥ����������ޤ���
  <li>view.cgi������ǥ����ʡ������å��򥪥�ˤ��Ƥ����硢�ֱ����פǤ���ƤǤ��ʤ��褦�ˤʤ�ޤ����ޤ�����index�����פΥܥ���򲡤��ʤ���С������Ϻǿ��Υǡ����ˤϤʤ�ޤ���
  <li>�����ͥ⡼�ɤǥ�����������ȡ��ƷǼ��Ĥδ����ͤε�ǽ���Ȥ���褦�ˤʤ�ޤ����ʴ����ͤȤ��ƤΥ��å����򿩤٤Ƥ��ޤ��ޤ��Τǡ��������ƤˤϽ�ʬ������Ĥ���������
</ul>
END

    print <<END;
<h2><a href="JavaScript:void(0)" onClick="document.AXESLOG.target='newWindow';document.AXESLOG.submit();return false;">�����������򸫤�</a></h2>
<form name="AXESLOG" action="${HaxesFile}" method="post">
  <input type="hidden" name="password" value="${inputPass}">
  <input type="hidden" name="mode" value="analyze">
  <input type="hidden" name="category" value="a">
</form>
<ul>
<li>�ᥤ�󥹥���ץ�(hako-main.cgi)������ǡ֥�����������Ȥ�פ褦�ˤ��Ƥ��ʤ���С����뤳�Ȥ��Ǥ��ޤ���
<li>����Ĥ�ư��ˤ��������ϥХ��ˤʤ�ޤ���Τǡ�Ȣ�����Τ�ư��ˤ�ƶ������뤳�Ȥ�и礷�Ʋ�������
</ul>
END

	if ($HallyUse || $HarmisticeTurn) {
		if($HallyBbs) {
			readAllyFile();
			if($HallyNumber) {
				my $allyList;
				foreach (0..$#Hally) {
					my $s = '';
					$s = ' selected' if(!$_);
					$allyList .= "<option value=\"$Hally[$_]->{'id'}\"$s>$Hally[$_]->{'name'}\n"
				}
				print <<END;
<H2><FORM name="ALLYBBS" action="${HbaseDir}/$HallyBbsScript" method=POST>
<select name=ally>${allyList}</select>
<INPUT type=hidden name=id value="0">
<INPUT type=hidden name=cpass value="${inputPass}">
<a href="JavaScript:void(0)" onClick="document.ALLYBBS.target='newWindow';document.ALLYBBS.submit();return false;">Ʊ���Ǽ��Ĥ�</a></H2>
</FORM>
<ul>
<li>��Ʊ���Ǽ��ġפ�����Ǥ��ޤ���
<li>��Ƥ���ȡ�̾�����ֳ��ﱿ�������פˤʤ�ޤ���
</ul>

<form name="DEADBBS" action="${HmenteFile}" method="POST">
  <input type="hidden" name="PASSWORD" value="${inputPass}">
  <select name=ALLYID>${allyList}</select>
  <input type="hidden" name="ALLYLOG">
  <h2><a href="JavaScript:void(0)" onClick="document.DEADBBS.submit();return false;">Ʊ���Ǽ��ĥ�����ǥ��ذܹ�</a></h2>
</form>
<ul>
<li>Ʊ���κ���Ͼ�Ρֿر�(Ʊ��)�κ����������ѹ��פǲ�ǽ�Ǥ���<BR>
�ֿر�(Ʊ��)�κ����������ѹ��פξ��ϡ���ȯ���ε�Ͽ�פ˲򻶥���ɽ������ơ�Ʊ���Ǽ��ĤΥ��Ϥ��Τޤ���¸����ޤ���<BR>
������ϡ�Ʊ���Ϥ��Τޤޤǡ�Ʊ���Ǽ��ĤΥ�����ǥ��ذܹԤ����ޤ���
<li>���ǥ���hako-yy-bbs.cgi�ξ����˥�󥯤���ޤ���<BR>
</ul>
END
			}
			if(-f "${HlogdirName}/dead${HallyData}") {
				open(DIN, "${HlogdirName}/dead${HallyData}") || die $!;
				my @dead = <DIN>;
				close(DIN);
				my $deadallyList;
				foreach (@dead) {
					my($dally, $daName, $diName) = split(/\,/, $_);
					my($did, $dturn) = split(/-/, $dally);
					$daName =~ s/<[^<]*>//g;
					$deadallyList .= "<OPTION VALUE=\"$dally\">$daName($HallyTopName��$diName ������$dturn�˾���)\n"
				}
				print <<END if(@dead > 0);
<form name="DELBBS" action="${HmenteFile}" method="POST">
  <select name=DEADALLY>${deadallyList}</select>
  <input type="hidden" name="PASSWORD" value="${inputPass}">
  <input type="hidden" value='���ǥ��κ��' name="DELLOG">
  <h2><a href="JavaScript:void(0)" onClick="document.DELBBS.submit();return false;">���ǥ��κ��</a></H2>
</form>
<ul>
  <li>Ʊ���Ǽ��Ĥξ��ǥ��������ޤ���
</ul>
END
			}
		}
		print <<END;
<h2><a href="${HthisFile}?JoinA=${inputPass}">�ر�(Ʊ��)�κ����������ѹ�</a></h2>
<ul>
  <li>�ֿر���⡼�ɡפ�ͭ���ˤ��Ƥ�����ϡ���������ر�(Ʊ��)�򿷵��������Ƥ���������
  <li>�ر�(Ʊ��)��������򤷤��ѹ��ܥ���򲡤��ȡ��ر�(Ʊ��)�λ���(����)��Ǥ̿���뤳�Ȥ��Ǥ��ޤ���
</ul>
END
    }
    else {
        print "�Ǽ��Ĥʤ�";
    }

    print <<END if($HuseAmity || $HallyUse || $HarmisticeTurn);
<h2><a href="${HthisFile}?ASetup=${inputPass}">ͧ����Ʊ��(�ر�)�ν�°�ѹ�</a></h2>
<ul>
  <li>ͧ���������Ʊ����°���ѹ���Ԥ��ޤ���
</ul>
END

    print <<END;
<h2><a href="${HthisFile}?Pdelete=${inputPass}">����${AfterName}������ͤ�������ˤ���</a></h2>
<ul>
  <li>��������ˤʤä�${AfterName}�ϡ����������(�������������ޥ�ɽ�������Ĺ���ҳ������ȼ԰�̱)����ʤ��ʤ�ޤ���
  <li>¾��${AfterName}����ι���Ϥ��٤Ƽ����Ĥ��Ƥ��ޤ��ޤ���
  <li>������������礬�������פ⤷���ϡֶ�������פ��줿��硢��������Σɣĥǡ����ϡ����Τ������������Ԥ��ޤǤ��Τޤ޻Ĥ�ޤ���
</ul>
END

    print <<END;
<h2><a href="${HthisFile}?Lchange=${inputPass}">����${AfterName}���Ϸ��ǡ������ѹ�����</a></h2>
<ul>
  <li>�Ӥ餷���ﳲ�䡢�����С��ȥ�֥롢������ץȤΥХ��ʤɤǡ��Ϸ��ǡ��������ܰդʾ��֤ˤʤäƤ��ޤä�${AfterName}��ߺѤ��ޤ���
  <li>��ɸ���Ĥ��Ĥν����ʤΤǡ���ʬŪ�ʵߺ����֤����Ǥ��ޤ�������Ū���ѹ���ľ�ܥǡ�������Ѥ��������ᤤ�Ǥ��礦��
  <li>�ޤ����͸������쵬�Ϥʤɤο��ͥǡ����ؤ�ȿ�Ǥϥ����󹹿��������Ԥ��Ƥ���ˤʤ�Τǡ���դ��Ƥ���������
  <li>���Ϸ��פȡ��Ϸ����͡פˤĤ��Ƥ��μ����ʤ���л��Ѥ��񤷤����⤷��ޤ��󡣤��Ȥ��Сֳ��פ��ͤ򣱤ˤ���ȡ������פˤʤä��ꡢ�ԻԤο͸���ɽ����ο��ͤȥǡ�����ο��ͤΰ㤤(10000�ͤ�100�ȵ�Ͽ����Ƥ����ꤹ��Τ�)�䡢����乩���ȯŸ���ϤǤȤꤦ����ͤ���ޤäƤ��뤳�Ȥʤ�(hako-make.cgi��sub landCheck�Ǵʰץ����å��򤹤�褦�ˤ��Ƥ��ޤ�)��
</ul>
END

    print <<END;
<h2><a href="${HthisFile}?Rename=0" target="_blank">����${AfterName}�����������</A></H2>
<ul>
  <li>��${AfterName}��̾���ȥѥ���ɤ��ѹ��ײ��̤ǡ�������${AfterName}��̾�����̵�͡�${AfterName}�ޤ��ϡ����ס�${AfterName}�ˤ��Ƥ���������
  <li>���κݡ��ѥ������ˤϡ��ü�ѥ���ɡפ����Ϥ��ʤ���Фʤ�ޤ���
  <li>��̵�͡�${AfterName}�ˤ���ȡ�ȯ���ε�Ͽ�פˡ��ֳ�����<B>�ܤ�˿���</B>Φ�ϤϤ��٤�<span class=attention>���פ��ޤ�����</span>�פȤ��������Ĥ�ޤ���
  <li>�����ס�${AfterName}�ξ��ϥ���Ф��ޤ���
</ul>
END

    print <<END;
<h2><a href="${HthisFile}?Present=">����${AfterName}�˥ץ쥼��Ȥ�£��</A></H2>
<ul>
  <li>��ȯ���ε�Ͽ�פ˥����Ĥ륤�٥�ȤȤ��Ʊ����Ԥ����Ȥ��Ǥ��ޤ���
  <li>ɽ�����줿�ե������ɬ�פ��ͤ��å����������Ϥ��ơ��ѥ���ɤˡ��ü�ѥ���ɡפ����졢�֥ץ쥼��Ȥ�£��ץܥ���򲡤��Хץ쥼��ȴ�λ�Ǥ���
  <li>���ˤ�HTML������Ȥ��ޤ������ְ�ä����κ�����Ǥ��ޤ���Τǡ����Ť����Ϥ��Ƥ������������餫����֥饦����ɽ���ƥ��Ȥ�ԤäƤ������ۤ��������Ǥ��礦����ȯ���ε�Ͽ�פ��Ѥʥ����Ĥ�ȡ�����ä��Ѥ��������Ǥ���
  <li>�ץ쥼��Ȥη�̤Ȥ��ƶ�俩������ͭ�̤������ͤ�Ķ���뤳�Ȥ�����ޤ�������Υ�����ʹԤ������ͤ��ڤ�ΤƤ��ޤ��������Υ���������ϻ��äƤ�������Ȥ��ޤ���
�㤨����ͭ�̤�20000�ˤʤäƤ����硢���Τޤޥ�����ʹԤ����9999���ڤ�ΤƤ��ޤ��������������Υ�����Ƿ����99��Ԥä����ˤϡ�����19800���������200�������Ĥ�ޤ���
</ul>
END

    print <<END;
<h2><a href="${HthisFile}?Punish=${inputPass}">����${AfterName}�����ۤ�ä���</A></H2>
<ul>
  <li>���ۤϻ��ꤷ�������ҳ���ɬ��ȯ�������ޤ����㤨�С֣�${AfterName}�����������פȤ����ؼ���Ф��ȼ��Υ�����������������ޤ���
  <li>������Ф�ʮ�ФϺ�ɸ���꤬��ǽ�ǡ�ɬ�����κ�ɸ��ȯ�����ޤ����ɤ����褦��ʤ��ץ쥤�䡼���ӽ�����Ȥ��˸���Ū�˻Ȥ��ޤ���
  <li>���β�¤�ϡ��ֹӤ餷�Ȥ����ۤɤǤϤʤ���Ȣ���ʷ�ϵ��򰭲�������褦�ʹ԰٤򤹤�ץ쥤�䡼�פ䡢�ִ����ͤη�᤿������롼��˰�ȿ���Ƥ��Ʋ����θ����ߤ��ʤ��ץ쥤�䡼�פʤɡ�Ȣ��α��ľ幥�ޤ����ʤ���Ƚ�Ǥ��줿�ץ쥤�䡼�˼����ҳ������Ū��ȯ���������ΤǤ���
  <li>�����ͤ����ޤ����ʤ���Ƚ�Ǥ����ץ쥤�䡼�ȤϷǼ��Ĥʤɤ��ä��礦�٤��Ǥ��������ˤϡ����������ä��礤�Ǥ�����Կ�������ʤ����Ȥ⤢��ޤ�������������硢����${AfterName}�δ֤ǡ֤���${AfterName}���٤����פȤ�������������夬�ä��ꤷ�ޤ�������̣�Ϥ��ʤ갭���Ǥ���
  <li>�����ͤˤ�äƤϡ֤���${AfterName}�ϹӤ餷��ǧ�ꤷ�ޤ��Τǹ��⤷�Ƥ��������פ���${AfterName}�����ǧ��뤳�Ȥ⤢��褦�Ǥ������ʤ��ʤ������ޤǤ��б����񤷤���ΤǤ�������Ū��${AfterName}��������������֤Ϥޤ����ؤǤ������������줿${AfterName}�Υץ쥤�䡼�����Ȥ��Ȥޤǹ��Ĥ��Ƥ��뤳�Ȥ⤢��ޤ���
  <li>���������Ȥ��ˡ��ּ¤ˤ������֤˵�����СפȤ��ֱ��������������פȤ�������С����ޤ���᤺������${AfterName}�ϼ��β����ޤ�����ꤹ�����Ȣ���ʷ�ϵ��������ʤ�ޤ��Τ���դ�ɬ�פǤ���
</ul>
END

    print <<END;
<h2><a href="${HthisFile}?Bfield=${inputPass}">Battle Field���������</A></H2>
<ul>
  <li>�͸����ˤʤäƤ����פ��ʤ�${AfterName}��������ޤ�������Сֱ齬${AfterName}�פǤ������и��ͤ���̱�Ԥ��ˤϤʤ�ޤ�(ʿ�·ϸ���)��
  <li>���餫����ֿ�����${AfterName}��õ���פˤ�ä�${AfterName}��������Ƥ����ʤ���Фʤ�ޤ���Τǡ�������Ͽ����ۤ������֤ξ��ϰ��Ū�ˤ�����ѹ��������䤷�Ƥ����ʤ���Фʤ�ʤ��Ǥ��礦�����ݤǤ��������ΤȤ�����ͤǤ���
  <li>�Ӥ餷��${AfterName}���ʣ��Ͽ��${AfterName}��Battle Field���ѹ����뤳�Ȥ�Ǥ��ޤ��͡�
  <li>�ޤ���Battle Field�ˤ��Ƥ���${AfterName}�򸵤��᤹���Ȥ�Ǥ��ޤ�����${AfterName}����Ͽ��������ξ��ϤǤ��ޤ���
  <li><b>Battle Field�λ���</b>
  <ul>
    <li>���줬�ʤ��Ƥ⿩����­�ˤϤʤ�ʤ���
    <li>�Ӥ��ϤϤ��ʤ���Ψ��ʿ�Ϥˤʤꡢʿ�ϤϿ����ԻԤ��ܤ��Ƥ��ʤ��Ƥ�¼��ȯ�����롣
    <li>���ýи���Ψ���̾�Σ��ܤǡ��͸��ˤ�����餺��˥�٥룲��
    <li>���ä��ݤ��������󾩶�ϡ��ݤ�����Τ�Τˤʤ롣
  </ul>
</ul>
END

    print <<END;
<form name="BFDEVELOP" action="${HthisFile}" method="POST">
  <input type="hidden" name="PASSWORD" value="${inputPass}">
  <input type="hidden" name="dummy" value="dummy">
  <h2><a href="JavaScript:void(0)" onClick="document.BFDEVELOP.target='newWindow';document.BFDEVELOP.submit();return false;">Battle Field�γ�ȯ���̤�����</a></h2>
</form>
<ul>
  <li>�ȥåץڡ�������ꥹ�Ȥ�Battle Field�����٤�褦�ˤʤ�ޤ���
  <li>Battle Field��������Ƥ��ʤ���С��������̤Υȥåץڡ�����ɽ�����������Ǥ���
</ul>
END

}


# ----------------------------------------------------
# Ʊ���Ǽ��ĥ�����ǥ��ذܹ�
sub allyLogMain {
	# ��ǡ������ɤߤ���
	if(!readIslandsFile()) {
		print "�ǡ����ɤ߹��ߥ��顼ȯ����<HR>";
		return;
	}
	my $an = $HidToAllyNumber{$HallyID};
	if(defined $an) {
		my $n = $HidToNumber{$HallyID};
		my $name = $Hislands[$n]->{'name'} . $AfterName;
		$name = "${HallyTopName}�Ժ�" if !(defined $n);
		if($dellcheck) {
			if(make_pastlog($HallyID, $name)) {
				print "�ܹ���������<a href='${HbaseDir}/hako-yy-bbs.cgi'>�Ǽ��Ĥ�</a><HR>";
			} else {
				print "�Ǽ��ĥ����ߤĤ���ʤ����ޤ��ϡ��ܹԼ��ԡ�<HR>";
			}
		} else {
			my $allyName = $Hally[$an]->{'name'};
			print <<END;
<H2>$allyName��Ʊ���Ǽ��ĥ�����ǥ��ذܹԤ��ޤ�����</H2>
<H2><FORM name="DEADBBS" action="${HmenteFile}" method=POST>
<INPUT type=hidden name=DELLOK value="1">
<INPUT type=hidden name=PASSWORD value="${inputPass}">
<INPUT type=hidden name=ALLYID value="${HallyID}">
<INPUT type=hidden name=ALLYLOG>
<a href="JavaScript:void(0)" onClick="document.DEADBBS.submit();return false;">�Ϥ�</a>��<a href="${HmenteFile}?ADMIN=${inputPass}">������</a></H2>
END
		}
		return;
	} else {
		print "Ʊ�����ߤĤ���ޤ���<HR>";
		$dellcheck = 1;
	}
	return;
}


# ----------------------------------------------------
# ���ǥ����
sub dellogMode {
	if($dellcheck) {
		my $logfile = "${HlogdirName}/${deadally}$Hlogfile_name";
		unlink($logfile) if (-f $logfile);
		# ������ե�����
		my $logfile2 = "${HlogdirName}/${deadally}$Hlogfile2_name";
		unlink($logfile2) if (-f $logfile2);
		# �����󥿥ե�����
		if($Hcounter) {
			my $cntfile = "${HlogdirName}/${deadally}$Hcntfile_name";
			unlink($cntfile) if (-f $cntfile);
		}
		# ������NO�ե�����
		if($Hpastkey) {
			my $nofile  = "${HlogdirName}/${deadally}$Hnofile_name";
			my $count;
			if (-f $nofile) {
				# ���NO�򳫤�
				open(NO,"$nofile") || die $!;
				$count = <NO>;
				close(NO);
			}
			unlink($nofile);
			foreach (1..$count) {
				my $pastfile = sprintf("%s/%04d\.%s\.cgi", $HpastdirName,$_,$deadally);
				unlink($pastfile) if (-f $pastfile);
			}
		}
		open(DIN, "${HlogdirName}/dead${HallyData}") || die $!;
		my @dead = <DIN>;
		close(DIN);
		open(DOUT, ">${HlogdirName}/dead${HallyData}") || die $!;
		foreach (@dead) {
			my($dally, $daName, $diName) = split(/\,/, $_);
			next if($dally eq $deadally);
            print DOUT $_;
        }
        close(DOUT);

	} else {
		open(DIN, "${HlogdirName}/dead${HallyData}") || die $!;
		my @dead = <DIN>;
		close(DIN);
		my $deadallyList;
		foreach (@dead) {
			my($dally, $daName, $diName) = split(/\,/, $_);
			my($did, $dturn) = split(/-/, $dally);
			$deadallyList = "$daName($HallyTopName��$diName ������$dturn�˾���)\n";
			last if($dally eq $deadally);
			$deadallyList = '';
		}
		if($deadallyList eq '') {
			$dellcheck = 1;
			return;
		}
		
		print <<END if(@dead > 0);
<H2>$deadallyList�ξ��ǥ��������ޤ�����</H2>
<H2><FORM name="DELBBS" action="${HmenteFile}" method=POST>
<INPUT type=hidden name=DELLOK value="1">
<INPUT type=hidden name=DEADALLY value="${deadally}">
<INPUT type=hidden name=PASSWORD value="${inputPass}">
<INPUT type=hidden value='���ǥ��κ��' name="DELLOG">
<a href="JavaScript:void(0)" onClick="document.DELBBS.submit();return false;">�Ϥ�</a>��<a href="${HmenteFile}?ADMIN=${inputPass}">������</a></H2>
END
	}
	return;
}


# ----------------------------------------------------
# ɽ���⡼��
sub dataPrint {
	my($suf) = @_;

	print "<HR>";
	if($suf eq "") {
		open(IN, "${HdirName}/$HmainData");
		print "<H1>����ǡ���</H1>";
	} else {
		open(IN, "${HdirName}.bak$suf/$HmainData");
		print "<H1>�Хå����å�$suf</H1>";
	}

	my($lastTurn);
	$lastTurn = <IN>;
	my($lastTime);
	$lastTime = <IN>;

	my($timeString) = timeToString($lastTime);

	print <<END;
	<B>������$lastTurn</B><BR>
	<B>�ǽ���������</B>:$timeString<BR>
	<B>�ǽ���������(�ÿ�ɽ��)</B>:1970ǯ1��1������$lastTime ��<BR>
	<INPUT TYPE="submit" VALUE="���Υǡ�������" NAME="DELETE$suf">
END

    if ($suf eq "") {
        my($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) = gmtime($lastTime + $Hjst);
        $mon++;
        $year += 1900;

        print <<END;
    <h2>�ǽ��������֤��ѹ�</h2>
    <input type="text" SIZE=4 NAME="YEAR" value="$year">ǯ
    <input type="text" SIZE=2 NAME="MON" value="$mon">��
    <input type="text" SIZE=2 NAME="DATE" value="$date">��
    <input type="text" SIZE=2 NAME="HOUR" value="$hour">��
    <input type="text" SIZE=2 NAME="MIN" value="$min">ʬ
    <input type="text" SIZE=2 NAME="NSEC" value="$sec">��
    <input type="submit" VALUE="�ѹ�" NAME="NTIME"><BR>
    1970ǯ1��1������<INPUT TYPE="text" SIZE=32 NAME="SSEC" VALUE="$lastTime">��
    <INPUT TYPE="submit" VALUE="�û�����ѹ�" NAME="STIME">

END
    } else {
        print <<END;
    <input type="submit" value="���Υǡ��������" name="CURRENT$suf">
END
    }
}

# ----------------------------------------------------
sub timeToString {
    my ($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) = gmtime($_[0] + $Hjst);
    $mon++;
    $year += 1900;

    return "${year}ǯ ${mon}�� ${date}�� ${hour}�� ${min}ʬ ${sec}��";
}

# ----------------------------------------------------
# CGI���ɤߤ���
sub cgiInput {
	my($line);

	# ���Ϥ�������
	$line = <>;
	$line =~ tr/+/ /;
	$line =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

	# GET�Τ�Ĥ�������
	$getLine = $ENV{'QUERY_STRING'};

	if($line =~ /DELETE([0-9]*)/) {
		$mainMode = 'delete';
		$deleteID = $1;
	} elsif($line =~ /CURRENT([0-9]*)/) {
		$mainMode = 'current';
		$currentID = $1;
	} elsif($line =~ /NEW/) {
		$mainMode = 'new';
	} elsif($line =~ /ALLYLOG/) {
		$mainMode = 'allylog';
		if($line =~ /ALLYID=([0-9]*)\&/) {
			$HallyID = $1;
		}
		if($line =~ /DELLOK=([0-9])\&/) {
			$dellcheck = $1;
		}
	} elsif($line =~ /DELLOG/) {
		$mainMode = 'dellog';
		$line =~ /DEADALLY=([0-9]*\-[0-9]*)\&/;
		$deadally = $1;
		if($line =~ /DELLOK=([0-9])\&/) {
			$dellcheck = $1;
		}
	} elsif($line =~ /ADMIN/) {
		$mainMode = 'admin';
	} elsif($getLine =~ /ADMIN=([^\&]*)/) {
		$mainMode = 'admin';
		$inputPass = $1;
	} elsif($line =~ /SETUP/) {
		$mainMode = 'setup';
		if($line =~ /MPASS1=([^\&]*)\&/) {
			$mpass1 = $1;
		}
		if($line =~ /MPASS2=([^\&]*)\&/) {
			$mpass2 = $1;
		}
		if($line =~ /SPASS1=([^\&]*)\&/) {
			$spass1 = $1;
		}
		if($line =~ /SPASS2=([^\&]*)\&/) {
			$spass2 = $1;
		}
	} elsif($line =~ /NTIME/) {
		$mainMode = 'time';
		if($line =~ /YEAR=([0-9]*)/) {
			$ctYear = $1; 
		}
		if($line =~ /MON=([0-9]*)/) {
			$ctMon = $1; 
		}
		if($line =~ /DATE=([0-9]*)/) {
			$ctDate = $1; 
		}
		if($line =~ /HOUR=([0-9]*)/) {
			$ctHour = $1; 
		}
		if($line =~ /MIN=([0-9]*)/) {
			$ctMin = $1; 
		}
		if($line =~ /NSEC=([0-9]*)/) {
			$ctSec = $1; 
		}
	} elsif($line =~ /STIME/) {
		$mainMode = 'stime';
		if($line =~ /SSEC=([0-9]*)/) {
			$ctSec = $1; 
		}
	}

	if($line =~ /PASSWORD=([^\&]*)\&/) {
		$inputPass = $1;
	}
}

# ----------------------------------------------------
# �ե�����Υ��ԡ�
sub fileCopy {
	my($src, $dist) = @_;
	open(IN, $src);
	open(OUT, ">$dist");
	while(<IN>) {
		print OUT;
	}
	close(IN);
	close(OUT);
}

# ----------------------------------------------------
# �ѥ������å�
sub passCheck {
	if(checkMasterPassword($inputPass)) {
		return 1;
	} else {
		tempWrongPassword(); # �ѥ���ɰ㤤
		print "</BODY></HTML>";
		exit(0);
	}
}

# Time::Local �θߴ��ؿ�
# sub timelocal {
#	my($sec, $min, $hour, $day, $mon, $year) = @_;
#
#	$year += 1900;
#	$mon++;
#	if ($mon <= 2) { $mon += 12; $year--; }
#
#	my $days = $year * 365 + int($year / 4) - int($year / 100) + int($year / 400)
#	+ $mon * 30 + int(($mon + 1) * 3 / 5) + $day - 33 - 719528; # 719528 = 1970/1/1
#
#	return (($days * 24 + $hour) * 60 + $min) * 60 + $sec - $Hjst;
# }

# ----------------------------------------------------
#cookie����
sub cookieInput {
    my($cookie);
#   $cookie = jcode::euc($ENV{'HTTP_COOKIE'}); # jcode���ѻ�
    $cookie = $ENV{'HTTP_COOKIE'};
    if ($cookie =~ /${HthisFile}OWNISLANDPASSWORD=\(([^\)]*)\)/) {
        $HdefaultPassword = $1;
    }
}

# ----------------------------------------------------
#cookie����
sub cookieOutput {
    my ($cookie, $info);

    # �ä�����¤�����
    my ($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) =
        gmtime(time + 14 * 86400); # ���� + 14��

    # 2������
    $year += 1900;
    $date = "0$date" if ($date < 10);
    $hour = "0$hour" if ($hour < 10);
    $min  = "0$min" if ($min < 10);
    $sec  = "0$sec" if ($sec < 10);

    # ������ʸ����
    $day = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")[$day];

    # ���ʸ����
    $mon = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")[$mon];

    # �ѥ��ȴ��¤Υ��å�
    $info = "; expires=$day, $date\-$mon\-$year $hour:$min:$sec GMT\n";
    $cookie = '';
    
    if($inputPass) {
        $cookie .= "Set-Cookie: ${HthisFile}OWNISLANDID=(0) $info";
        $cookie .= "Set-Cookie: ${HthisFile}OWNISLANDPASSWORD=($inputPass) $info";
    }
    out($cookie);
}

1;
