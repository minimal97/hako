#!/usr/bin/perl

# patchworked by neo_otacky. for ����JS RAJS
# ��lbbslist.cgi?pass=[�ޥ����ѥ�]�ǥ�����������ȡ�������Ĥ��ޤ���
# ����Ƥ���������̾�ϴ�����̾�ǡ���̾�ϡִ����͡פˤʤ�ޤ���
# �������å����˥ޥ����ѥ�����äƤ���ϡ����̤˥����������������OK!
#---------------------------------------------------------------------
#	
#	���ۤ�Ȣ��������Ǽ��Ĥ����ɽ��
#
#	������ : 2001/10/06 (ver0.10)
#	������ : �饹�ƥ��� <nayupon@mail.goo.ne.jp>
#
#	�����Ԥ���̱��ȯ����ƨ���ʤ��褦�����ǳ�ǧ���뤿��Τ�ΤǤ���
#	lbbslist.cgi?pass=�ޥ����ѥ����ǥ�����������ȶ����̿��⸫��ޤ���
#
#	��������
#	2001/10/20 V0.20 �Ƕ��ȯ���򿧤��Ѥ���ɽ���Ǥ���褦�ˤ�����
#	2001/12/31 V0.30 ������������config.cgi���������褦�ˤ�����
#	2002/01/13 V0.31 version4�б�
#	2002/02/03 V0.40 CSS���̥ե����뤫���ɤ߹���褦�ˤ�����
#	2002/04/17 V0.41 ���ɽ����Ĥ�����������ץȤ�����Ū�˸�ľ����
#	2002/07/27 V0.50 �����̿����б��������ܤβ�������
#	2002/10/28 V0.60 �������륷�����դ�����
#
#---------------------------------------------------------------------
#	��������ץȤϰʲ��򸵤˺������ޤ���
#
#	���÷���ݥ���ȡܳ����޶⡡��󥭥�ɽ��
#	������ : Watson <watson@catnip.freemail.ne.jp>
#---------------------------------------------------------------------
require "./html_template.pl";
BEGIN {
    # Perl 5.004 �ʾ夬ɬ��
    require 5.004;

########################################
    # ���顼ɽ��
    $SIG{__WARN__} = $SIG{__DIE__} =
    sub {
        my($msg) = @_;

        $msg =~ s/\n/<br>/g;
        print STDOUT <<END;
Content-type: text/html; charset=EUC-JP

<p><big><tt><b>ERROR:</b><br>$msg</tt></big></p>
END
        exit(-1);
    };
########################################
}
#---------------------------------------------------------------------
#	�������
#---------------------------------------------------------------------
# ��������ѥե�������ɤ߹���
require './hako-init.cgi';
require './hako-io.cgi';
require './init-game.cgi';

# �����Ѥ���ɽ�����륿����
$kyoutyouturn = 100;

#----------------------------
#	HTML�˴ؤ�������
#----------------------------
# �֥饦���Υ����ȥ�С���̾��
$title = '�Ѹ����̿�����';

# ��Ƭ�Υ�å�����(HTML��)
$headKill = <<"EOF";
<h1>$Htitle �Ѹ����̿�����ɽ�ʴ����ѡ�</h1>
EOF

# ���̤ο����طʤ�����(HTML)
$body = '<body bgcolor=#EEFFFF>';

# ���̤Ρ����ץ����(URL)
$bye = $HthisFile;

# ���̾���ʤ�
$HtagName_ = '<span class="islName">';
$H_tagName = '</span>';
# ���ɽ�ˤ����븫����
$HtagTH_ = '<span class="head">';
$H_tagTH = '</span>';

$HbgTitleCell   = 'class=TitleCell';   # ���ɽ���Ф�
$HbgNumberCell  = 'class=NumberCell';  # ���ɽ���
$HbgNameCell    = 'class=NameCell';    # ���ɽ���̾��
$HbgInfoCell    = 'class=InfoCell';    # ���ɽ��ξ���
$HbgCommentCell = 'class=CommentCell'; # ���ɽ��������
#�����ޤ�-------------------------------------------------------------

if (-e $HpasswordFile) {
	# �ѥ���ɥե����뤬����
	open(PIN, "<$HpasswordFile") || die $!;
	chomp($HmasterPassword = <PIN>); # �ޥ����ѥ���ɤ��ɤ߹���
	close(PIN);
}
&cookieInput;
&cgiInput;

my ($mode) = 0;
if ($HdefaultPassword ne '') {
	if (checkMasterPassword($HdefaultPassword)) {
		$mode = 1;
	} else {
		if ($HskinName ne '') {
			$baseSKIN = $HskinName;
		} else {
			$baseSKIN = "${efileDir}/$HcssFile";
		}
		&htmlHeader;
		tempWrongPassword(); # �ѥ���ɰ㤤
		&htmlFooter;
		exit(0);
	}
}
my ($bye2) = (!$mode) ? '' : "[<A HREF=\"$HmenteFile?ADMIN=$HdefaultPassword\">���ƥʥ󥹤�</A>] ";

if (!(&readIslandsFile(-1))) {
    &htmlHeader;
    &htmlError;
}
else {
    &htmlHeader;
    if ($HmainMode eq 'news') {
        &newsMain;
    }
    out("<DIV align='center'>");
    out($headKill);
    out("��������ץȤϡ������Ф���٤�������Ȼפ��뤿��Ȣ�����Τ����󥯤�ĥ�äƤ��ޤ���<br>");
    out("���ˤ˥������������ꡢ����ɤʤɤι԰٤ϤǤ������������褦�ˡ�<br>");
    out("<table border><tr><td>");
    foreach $i (0..$islandNumber) {
        &tempLbbsContents($i);
    }
    out("<TR><TD colspan=2 class='M'><P align='center'>${AfterName}��̾���򥯥�å�����ȡ��Ѹ����뤳�Ȥ��Ǥ��ޤ���</P></TD></TR>");
    # �إå��Υ����Ȥ�񤭴�������(hako-init.cgi�ǥ����ȥ����Ȥ��Ƥ�����ʬ��Ϣư)
    # &tempNews if($mode);
    out("</TABLE>");
    out("</DIV>");
}
&htmlFooter;
#��λ
exit(0);


#���֥롼����---------------------------------------------------------
#--------------------------------------------------------------------
#	POST or GET�����Ϥ��줿�ǡ�������
#--------------------------------------------------------------------
sub cgiInput {
    my ($line, $getLine);
    $line = <>;
    $line =~ tr/+/ /;
    $line =~ s/%([a-fA-F0-9]{2})/pack(H2, $1)/eg;

    # GET�Τ�Ĥ�������
    $getLine = $ENV{'QUERY_STRING'};

    if ($getLine =~ /pass=([^\&]*)/) {
        # �ǽ�ε�ư
        $HdefaultPassword = $1;
    }
    elsif ($line =~ /NewsComment=([^\&]*)\&/) {

        $HdefaultPassword = $1;
        $line =~ s/(.*)NEWS=//g;
        $HnewsComment = $line;
        $HmainMode = 'news';
    }
}


#---------------------------------------------------------------------
# cookie����
#---------------------------------------------------------------------
sub cookieInput {
    my ($cookie);
#   $cookie = jcode::euc($ENV{'HTTP_COOKIE'}); # jcode���ѻ�
    $cookie = $ENV{'HTTP_COOKIE'};
    if ($cookie =~ /${HthisFile}OWNISLANDPASSWORD=\(([^\)]*)\)/) {
        $HdefaultPassword = $1;
    }
}


#---------------------------------------------------------------------
#	�ؿ�̾ : htmlHeader
#	����ǽ : HTML�Υإå���ʬ�����
#	������ : �ʤ�
#	����� : �ʤ�
#---------------------------------------------------------------------
sub htmlHeader {
	if ($HskinName ne '') {
		$baseSKIN = $HskinName;
	} else {
		$baseSKIN = "${efileDir}/$HcssFile";
	}

	if ($ENV{'HTTP_ACCEPT_ENCODING'}=~/gzip/ && $Hgzip == 1) {

		print qq{Content-type: text/html; charset=EUC-JP\n};
		print qq{Content-encoding: gzip\n\n};
		open(STDOUT,"| $HpathGzip/gzip -1 -c");
		print " " x 2048 if($ENV{HTTP_USER_AGENT}=~/MSIE/);
		print qq{<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\n\n};
	} else {
		print qq{Content-type: text/html; charset=EUC-JP\n\n};
		print qq{<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\n\n};
	}

    out(<<END);
<HTML>
<HEAD>
<TITLE>
$title
</TITLE>
<link rel="stylesheet" type="text/css" href="${baseSKIN}">
</HEAD>
$body<DIV ID='BodySpecial'>
END
    html_template::PrintHeader();

    # ��ʬ�Υ����ȤʤɤؤΥ�󥯤��ɲä�����Ϣ����ɲä��Ƥ���������
    # ���ߤˢ��˥�󥯤��ɲä��ʤ��ǲ�������JavaScript ���顼�θ����ˤʤ뤳�Ȥ�����ޤ���

    out(<<END) if(defined $HleftTime);
<HR><FORM name=TIME style="margin: 1px 0px;">
<H1 style="display:inline;"><SMALL><B>������</B> </SMALL>$HislandTurn</H1>
<INPUT type=text name=TIME size=52 readonly class="timer">
</FORM>
<HR></DIV>
${bye2}<A HREF="$bye">[���]</A><br><br>
END
}


#---------------------------------------------------------------------
#	�ؿ�̾ : htmlFooter
#	����ǽ : HTML�Υեå���ʬ�����
#	������ : �ʤ�
#	����� : �ʤ�
#---------------------------------------------------------------------
sub htmlFooter {
	out(<<END);
<HR>
<DIV ID='LinkFoot'>
$Hfooter
<BR></DIV>
END
##### �ɲ� ����20020307
	if($Hperformance) {
		my($uti, $sti, $cuti, $csti) = times();
		$uti += $cuti;
		$sti += $csti;
		my($cpu) = $uti + $sti;

	#	   ���ե�����񤭽Ф�(�ƥ��ȷ�¬�ѡ����ʤϥ����Ȥˤ��Ƥ����Ƥ�������)
	#	   open(POUT,">>cpu-h.log");
	#	   print POUT "CPU($cpu) : user($uti) system($sti)\n";
	#	   close(POUT);

        out(<<END);
<DIV align="right">
<SMALL>CPU($cpu) : user($uti) system($sti)</SMALL>
</DIV>
END
    }
#####
    out(<<END);
</DIV></BODY>
</HTML>
END
}


#---------------------------------------------------------------------
#	�ؿ�̾ : htmlError
#	����ǽ : HTML�Υ��顼��å������ν���
#	������ : �ʤ�
#	����� : �ʤ�
#---------------------------------------------------------------------
sub htmlError{
	out("<H2>���顼��ȯ�����ޤ���</H2>\n");
}


#---------------------------------------------------------------------
#	�ؿ�̾ : tempLbbsContents
#	����ǽ : ������Ǽ�������
#	������ : �ʤ�
#	����� : �ʤ�
#---------------------------------------------------------------------
sub tempLbbsContents {
	my ($number) = $_[0];
	my ($island) = $Hislands[$number];
	my ($name) = islandName($island);
	my ($id) = $island->{'id'};
	my ($owner) = $island->{'ownername'};
	my ($lbbs) = $island->{'lbbs'};
	my ($comment) = $island->{'comment'};
	my ($line);
	out(<<END);
<TR><TH $HbgTitleCell>${HtagTH_}${AfterName}̾${H_tagTH}</TH>
<TD $HbgNameCell>
<A STYlE=\"text-decoration:none\" HREF="${HthisFile}?Sight=${id}" TARGET=_blank>
${HtagName_}$name${H_tagName}
</A>
</TD><TH $HbgTitleCell>${HtagTH_}���${H_tagTH}</TH>
<TD $HbgInfoCell>$owner</TD></TR>
<TR><TH $HbgTitleCell>${HtagTH_}������${H_tagTH}</TH><TD $HbgCommentCell colspan=3>$comment</TD></TR>
END

	if ($mode) {
		out(<<END);
<TR>
<TD colspan=4>
<FORM action="$HthisFile" method="POST">
<INPUT TYPE="hidden" NAME="LBBSNAME" VALUE="$HadminName">
<INPUT TYPE="hidden" NAME="ISLANDID2" VALUE="0">
com:<INPUT TYPE="text" SIZE=40 NAME="LBBSMESSAGE">
pass:<INPUT TYPE="password" SIZE=16 MAXLENGTH=16 NAME=PASSWORD VALUE="$HdefaultPassword">
<INPUT TYPE="radio" NAME="LBBSTYPE" VALUE="PUBLIC" CHECKED>����<br>
<INPUT TYPE="radio" NAME="LBBSTYPE" VALUE="SECRET"><span class='lbbsST'>����</span>
<INPUT TYPE="submit" VALUE="��Ģ����" NAME="LbbsButtonAD$id">
�ֹ�
<SELECT NAME=NUMBER>
END
		# ȯ���ֹ�
		my ($j, $i);
		for ($i = 0; $i < $HlbbsMax; $i++) {
			$j = $i + 1;
			out("<OPTION VALUE=$i>$j\n");
		}
		out("<OPTION VALUE=$HlbbsMax>��\n");
		out(<<END);
</SELECT>
<INPUT TYPE="submit" VALUE="���" NAME="LbbsButtonDA$id">
</TD>
</TR>
</FORM>
END
	}

    my ($i,$j,$str1,$turn);
    my ($speaker);
    for ($i = 0; $i < $HlbbsMax; $i++) {
        $line = $lbbs->[$i];
        if ($line =~ /([0-9]*)\<(.*)\<([0-9]*)\>(.*)\>(.*)$/) {
            my ($m, $iName, $os, $tan, $com) = ($1, $2, $3, $4, $5);
            $j = $i + 1;
            out("<TR><TD $HbgNameCell align=center><span class='number'>$j</span></TD>");
            my ($sName, $sID) = split(/,/, $iName);
            my ($sNo) = $HidToNumber{$sID};

            if ($sName ne '') {
                if (defined $sNo) {

                    $speaker = "<span class='lbbsST'><B><SMALL>(<A STYlE=\"text-decoration:none\" HREF=\"$HthisFile?Sight=$sID\" TARGET=_blank>$sName</A>)</SMALL></B></span>";
                }
                else {

                    $speaker = "<span class='lbbsST'><B><SMALL>($sName)</SMALL></B></span>";
                }
            }

            if ($tan =~ /^([0-9]*)��/) {

                $turn = $1;
            }

            if ($turn >= $HislandTurn - $kyoutyouturn) {

                out("<TD class='RankingCell' colspan=3>");
            }
            else {

                out("<TD $HbgInfoCell colspan=3>");
            }

            if ($os == 0) {
                # �Ѹ���
                if ($m == 0) {
                    # ����
                    out("<span class='lbbsSS'>$tan > $com</span> $speaker</TD></TR>");
                }
                else {
                    # ����
                    if (!$mode) {
                        # �Ѹ���
                        out("<DIV align='center'><span class='lbbsST'>- ���� -</span></DIV></TD></TR>");
                    }
                    else {
                        # �����ʡ�
                        out("<span class='lbbsSS'>$tan >(��) $com</span> $speaker</TD></TR>");
                    }
                }
            }
            else {
                # ���
                out("<span class='lbbsOW'>$tan > $com</span> $speaker</TD></TR>");
            }
        }
    }
    out(<<END);
</TD></TR>
END

    out(<<END);
<TR></TR>
<TR></TR>
END
}


#---------------------------------------------------------------------
sub tempNews {
	out(<<END);
<TR></TR>
<TR></TR>
<FORM name="f01" action="$HlbbsFile" method="POST">
<TR><TD colspan=4><big><B>�������ѹ�(�ȥåץڡ����κǾ������ľ��)</B></big>
��<INPUT TYPE="hidden" VALUE="$HdefaultPassword" NAME="NewsComment">
��<INPUT TYPE="submit" VALUE="�ѹ�">
</TD></TR>
<TR><TD colspan=4>
<SCRIPT LANGUAGE=javascript>
<!--
function chk01(str){
//  var str1 = str.replace(/\<|\>/g,"");
  return str1;
}
//-->
</SCRIPT>
<P ALIGN="center">
<TABLE BORDER=2><TR><TD style="border-style:inset;">
<textarea name="NEWS" cols=80 rows=5 WRAP="soft">$Hnews</textarea><BR>
</TD></TR></TABLE>
��������Preview��������
<TABLE BORDER=2><TR><TD style="border-style:inset;">
<span ID="outputN1"></span><br>
<SCRIPT LANGUAGE=javascript>
<!--
outputN1.setExpression("innerHTML","f01.NEWS.value");
//-->
</SCRIPT>
</TD></TR></TABLE>
</TD>
</FORM>
</TR>
END
}


#---------------------------------------------------------------------
sub newsMain {
    if (!$mode){
        &htmlError;
        &htmlFooter;
        #��λ
        exit(0);
    }

    if ($HnewsComment eq '') {

        unlink('./news.cgi') if(-e "./news.cgi");
    }
    else {

        jcode::convert(\$HnewsComment, 'euc');
        my ($rn) = "\n";
        $HnewsComment =~ s/\r$rn/$rn/eg;
        open(NEWS, ">./news.cgi");
        print NEWS $HnewsComment;
        close(NEWS);
    }
    $Hnews = $HnewsComment;
}