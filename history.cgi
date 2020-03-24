#!/usr/bin/perl
# �ң��Ѥ˲�¤
#---------------------------------------------------------------------
#   ���ۤ�Ȣ���Ƕ�ν�����ȺǶ��ŷ���������ɽ��
#
#   ������ : 2001/11/25 (ver0.10)
#   ������ : �饹�ƥ��� <nayupon@mail.goo.ne.jp>
#---------------------------------------------------------------------
#use strict "vars";
use strict "refs";
#use strict "subs";
use Time::HiRes;

require './server_config.pm';

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
#    �������
#---------------------------------------------------------------------
# ��������ѥե�������ɤ߹���
require './hako-init.cgi';
require './hako-io.cgi';

#----------------------------
#    HTML�˴ؤ�������
#----------------------------
# �֥饦���Υ����ȥ�С���̾��
$title = '�Ƕ�ν����';

# ���̤ο����طʤ�����(HTML)
$body = '<body bgcolor=#EEFFEE>';

# ���̤Ρ����ץ����(URL)
$bye = './hako-main.cgi';

#�ᥤ��롼����-------------------------------------------------------
cookieInput();
cgiInput();
unless(($ENV{HTTP_REFERER}  =~ /$server_config::HbaseDir/) || $HcurrentID) {
    if ($HskinName ne '' ) {
        $baseSKIN = $HskinName;
    }
    else {
        $baseSKIN = "${efileDir}/$HcssFile";
    }
    print qq{Content-type: text/html; charset=EUC-JP\n\n};
    out(<<END);
<html>
  <head>
    <title>$title</title>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="theme-color" content="#99FF99">
    <link rel="shortcut icon" href="./img/fav.ico">
    <link rel="stylesheet" type="text/css" href="${baseSKIN}">
  </head>
$body
  <h1>�����ʥ��������Ǥ�</h1>
$server_config::HbaseDir / $ENV{HTTP_REFERER} / $HcurrentID
  </body>
</html>
END
    exit(0);
}
if (-e $HpasswordFile) {
    # �ѥ���ɥե����뤬����
    open(PIN, "<$HpasswordFile") || die $!;
    chomp($HmasterPassword  = <PIN>); # �ޥ����ѥ���ɤ��ɤ߹���
    chomp($HspecialPassword = <PIN>); # �ü�ѥ���ɤ��ɤ߹���
    close(PIN);
}
if ($HhtmlLogMake && ($HcurrentID == 0)) {
    unless (-e "${HhtmlDir}/hakolog.html") {
        # �Ƕ�ν�����ȣԣͣ̽���
        logPrintHtml();
        tempRefresh(3, '��������Ǥ������Τޤޤ��Ф餯���Ԥ�������');
    }
    else {
        tempRefresh(0, '���Ф餯���Ԥ�������');
    }
}
else {
    if (!readIslandsFile()) {
        tempHeader();
        htmlError();
    }
    else {
        $HislandList = getIslandList($HcurrentID);
        tempHeader();
        out("<div id='RecentlyLog'>\n");

        $HcurrentNumber = $HidToNumber{$HcurrentID};
        my ($island) = $Hislands[$HcurrentNumber];
        $HcurrentName = islandName($island);
        # �Ƕ�ν����
        if ($HMode == 99) {
            if ($HcurrentID == 0) {
                logFilePrintAll();
            }
            else {
                tempIslandHeader($HcurrentID, $HcurrentName);
                # �ѥ����
                if (checkPassword($island, $HinputPassword) && ($HcurrentID eq $defaultID)) {
                    logPrintLocal(1);
                }
                else {
                    # password�㤦
                    logPrintLocal(0);
                }
            }
        }
        else {
            if ($HcurrentID == 0) {
                logFilePrint($HMode, $HcurrentID, 0);
            }
            else {
                tempIslandHeader($HcurrentID, $HcurrentName);
                # �ѥ����
                if (checkPassword($island, $HinputPassword) && ($HcurrentID eq $defaultID)) {
                    logFilePrint($HMode, $HcurrentID, 1);
                }
                else {
                    # password�ְ㤤
                    logFilePrint($HMode, $HcurrentID, 0);
                }
            }
        }
        out("</div>\n");
    }
}
tempFooter();
#��λ
exit(0);

#���֥롼����---------------------------------------------------------
#---------------------------------------------------------------------
#    �ؿ�̾ : htmlError
#    ����ǽ : HTML�Υ��顼��å������ν���
#    ������ : �ʤ�
#    ����� : �ʤ�
#---------------------------------------------------------------------
sub htmlError{
    out("<h2>���顼��ȯ�����ޤ���</h2>\n");
}
#--------------------------------------------------------------------
#    POST or GET�����Ϥ��줿�ǡ�������
#--------------------------------------------------------------------
sub cgiInput {
    my($line, $getLine);

    # ���Ϥ������ä����ܸ쥳���ɤ�EUC��
    $line = <>;
    $line =~ tr/+/ /;
    $line =~ s/%([a-fA-F0-9]{2})/pack('H2', $1)/eg;
#   jcode::convert(\$line, 'euc');
    $line =~ s/[\x00-\x1f\,]//g;

    # GET�Τ�Ĥ�������
    $getLine = $ENV{'QUERY_STRING'};

    if ($line =~ /ID=([0-9]*)/) {
        $HcurrentID = $1;
    }
    if ($line =~ /PASSWORD=([^\&]*)/) {
        $HinputPassword = $1;
    }
    if ($getLine =~ /ID=([0-9]*)/) {
        $HcurrentID = $1;
    }
    if ($getLine =~ /PASSWORD=([^\&]*)/) {
        $HinputPassword = $1;
    }
    if ($getLine =~ /Event=([0-9]*)/) {
        $HMode = $1;
    }
    else {
        $HMode = 0;
    }
}
#cookie����
sub cookieInput {

    my ($cookie) = $ENV{'HTTP_COOKIE'};
    my ($HthisFile) = "$server_config::HbaseDir/hako-main.cgi";
    my ($HHistoryFile) = "$server_config::HbaseDir/history.cgi";

    if ($cookie =~ /${HthisFile}OWNISLANDID=\(([^\)]*)\)/) {
        $defaultID = $1;
    }
    if ($cookie =~ /${HthisFile}OWNISLANDPASSWORD=\(([^\)]*)\)/) {
        $HdefaultPassword = $1;
    }
    if ($cookie =~ /${HthisFile}SKIN=\(([^\)]*)\)/) {
        $HskinName = $1;
    }
    if ($cookie =~ /${HHistoryFile}ID=\(([^\)]*)\)/) {
        $HcurrentID = $1;
    }
}

#---------------------------------------------------------------------
#    HTML�Υإå��ȥեå���ʬ�����
#---------------------------------------------------------------------
# �إå�
sub tempHeader {
    if($HskinName ne '' ){
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
    }
    else {
        print qq{Content-type: text/html; charset=EUC-JP\n\n};
        print qq{<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\n\n};
    }

    out(<<END);
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html;charset=EUC-JP">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="theme-color" content="#99FF99">
  <link rel="shortcut icon" href="./img/fav.ico">
  <title>$title</title>
  <link rel="stylesheet" type="text/css" href="${baseSKIN}">
</head>
$body<div id='BodySpecialForHistory' width='100%'>
<div id='LinkHead'>
  <hr>
</div>
END
# <A HREF="$bye">[���]</A><br>
    out(<<END);
<span class="big"><a href=href=\"#\" onclick=\"window.close()\">[�Ĥ���]</a></span><br>
END
    logDekigoto();
    out(<<END);
<hr>
<form name="recentForm" action="$server_config::HbaseDir/history.cgi" method="post" style="margin  : 2px 0px;">
<b>[�Ƕ�ν����]</b><br>
<!-- <A href="history.cgi?Event=99">��ALL��</A> -->
END
    my ($i, $turn);
    out("<span class='HistoryTurnList'>");
    for ($i = 0;$i < $HtopLogTurn;$i++) {
        $turn = $HislandTurn - $i;
        last unless($turn > 0);
        out("<A HREF='history.cgi?Event=${i}'>");
        if ($i == 0) {
            out("[������${turn}(����)]<br>");
        } else {
            out("[${turn}]");
        }
        out('</A> ');
        out("<br>\n") if($i != 0 && ($i % 10) == 0 ); 
    }
    out('</span>');

    out(<<END);
  <br>
  <select name="ID">$HislandList</select>
  <input type="hidden" name="PASSWORD" value="$HinputPassword">
  <input type="submit" value="�򸫤�">
</form>
END

}

# �եå�
sub tempFooter {
    out(<<END);
<hr>
<div class='LinkFoot' align='center'>
  <small>�ۡ���ڡ���(<a href="$Htoppage">��</a>)</small>
END

##### �ɲ� ����20020307
    if (USE_PERFORMANCE) {
        my ($uti, $sti, $cuti, $csti) = times();
        $uti += $cuti;
        $sti += $csti;
        my ($cpu) = $uti + $sti;
        my ($timea) = sprintf("%.3f",Time::HiRes::time - $Hakoniwa_start_time);

    #       ���ե�����񤭽Ф�(�ƥ��ȷ�¬�ѡ����ʤϥ����Ȥˤ��Ƥ����Ƥ�������)
    #       open(POUT,">>cpu-h.log");
    #       print POUT "CPU($cpu) : user($uti) system($sti)\n";
    #       close(POUT);

        out(<<END);
<div align="right">
  <small>CPU($cpu) : user($uti) system($sti)/t:$timea</small>
</div>
END
    }
#####
    out(<<END);
</div>
</div></body>
</html>
END
}
# html����ե�å���
sub tempRefresh {
    my($delay, $str) = @_;

    unless($Hgzip == 1) {
        print qq{Content-type: text/html; charset=EUC-JP\n\n};
        print qq{<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\n\n};
        out(<<END);
<html>
<head>
  <title>HTML��</title>
  <meta http-equiv='refresh' content='$delay; url="${htmlDir}/hakolog.html"'>
</head>
<body><div id='BodySpecial'>
<h2>$str</h2>
END
    }
    else {
        open(IN, "<${HhtmlDir}/hakolog.html") || die $!;
        @buffer = <IN>;
        close(IN);
        if($ENV{'HTTP_ACCEPT_ENCODING'}=~/gzip/) {
            print qq{Content-type: text/html;\n};
            print qq{Content-encoding: gzip\n\n};
            open(STDOUT,"| $HpathGzip/gzip -1 -c");
            print " " x 2048 if($ENV{HTTP_USER_AGENT}=~/MSIE/);
        } else {
            print qq{Content-type: text/html;\n\n};
        }
        print @buffer;
    }
}

# ��ǡ����Υץ�������˥塼��
sub getIslandList {
    my ($select) = @_;

    my ($list, $name, $id, $s, $i);

    #��ꥹ�ȤΥ�˥塼
    $list = '';
    my ($predel);
    foreach $i (0..$islandNumber) {
        $name = islandName($Hislands[$i]);
        $name =~ s/<[^<]*>//g;
        $predel = ($Hislands[$i]->{'predelete'}) ? '[��]' : '';
        $id = $Hislands[$i]->{'id'};
        if($id eq $select) {
            $s = 'selected';
        } else {
            $s = '';
        }
        $list .= "<option value=\"$id\" $s>${predel}${name}\n";
    }
    return $list;
}

#---------------------------------------------------------------------
#    ��ζᶷ�Υ��
#---------------------------------------------------------------------
# �إå�
sub tempIslandHeader {
my($id, $name) = @_;

    if(checkPassword($Hislands[$HidToNumber{$id}]->{'password'}, $HinputPassword) && ($HcurrentID eq $defaultID)) {
        out(<<END);
<hr>
<font color=\"#FF0000\"><b>[${name}�ζᶷ]</b></font>
END
    } else {
        out(<<END);
<hr>
<b>[${name}�ζᶷ]</b>��
END
    }

    if($HinputPassword eq '') {
        out("<A HREF='history.cgi?ID=${id}&Event=99'><br>��ALL��</A>");
    } else {
        out("<A HREF='history.cgi?ID=${id}&PASSWORD=${HinputPassword}&Event=99'><br>��ALL��</A>");
    }
    my ($i, $turn);
    for($i = 0;$i < $HtopLogTurn;$i++) {
        $turn = $HislandTurn - $i;
        return unless($turn > 0);
        if($HinputPassword eq '') {
            out("<A HREF='history.cgi?ID=${id}&Event=${i}'>");
        } else {
            out("<A HREF='history.cgi?ID=${id}&PASSWORD=${HinputPassword}&Event=${i}'>");
        }
        if($i == 0) {
            out("[������${turn}(����)]<br>");
        } else {
            out("[${turn}]");
        }
        out("</A>");
        out("<br>\n") if($i != 0 && ($i % 10) == 0 ); 
    }
    out("<HR>\n");
}
#---------------------------------------------------------------------
#    ���ե����륿���ȥ�
#---------------------------------------------------------------------
sub logDekigoto {
    out(<<END);
<h1>�Ƕ�ν����</h1>
END
}


#---------------------------------------------------------------------
#    ���ե���������ɽ��
#---------------------------------------------------------------------
sub logFilePrintAll {
    my ($i);
    for($i = 0; $i < $HtopLogTurn; $i++) {
        logFilePrint($i, 0, 0);
    }
}


#---------------------------------------------------------------------
# ���̥�ɽ��
#---------------------------------------------------------------------
sub logPrintLocal {
    my ($mode) = @_;
    my ($i);
    for($i = 0; $i < $HtopLogTurn; $i++) {
        logFilePrint($i, $HcurrentID, $mode);
    }
}


#---------------------------------------------------------------------
#    �ե������ֹ����ǥ�ɽ�� #�ң���
#---------------------------------------------------------------------
sub logFilePrint {
    my ($fileNumber, $id, $mode) = @_;
    my ($set_turn) = 0;
    open(LIN, "${HdirName}/hakojima.log$_[0]");
    my ($line, $m, $turn, $id1, $id2, $message);

    while ($line = <LIN>) {
        $line =~ /^([0-9]*),([0-9]*),([0-9]*),([0-9]*),(.*)$/;
        ($m, $turn, $id1, $id2, $message) = ($1, $2, $3, $4, $5);

        # ��̩�ط�
        if ($m == 1) {
            if (($mode == 0) || ($id1 != $id)) {
                # ��̩ɽ�������ʤ�
                next;
            }
            $m = '<b>(��̩)</b>:';
        } else {
            $m = '';
        }

        # ɽ��Ū�Τ�
        if ($id != 0) {
            if(($id != $id1) &&
               ($id != $id2)) {
                next;
            }
        }

        if(!$set_turn){
            if(!$Hseason) {
                out("<b>=====[<span class='number'><font size='4'> ������$turn </font></span>]=====</b><br>\n");
            } else {
                # �����ɽ��
                my @seasonName = ('<span class="winter">��</span>','<span class="spring">��</span>','<span class="summer">��</span>','<span class="autumn">��</span>');
                my ($month) = ($turn % 12) + 1;
                my ($year)  = ($turn / 12) + 1;
                my ($calender) = sprintf('<span class=month><FONT SIZE=2><small>%s</small> %dǯ %d�� </FONT></span>' , $Halmanac, $year, $month);
                $calender .= "<span class='season'>$seasonName[int(($month - 1) / 3)]</span>";
                out("<b>=====[<span class='number'><font size='4'> <small>������$turn</small> </font></span>]=====$calender</b><br>\n");
            }
            $set_turn++;
        }
        out('��'.${m}.$message."<br>\n");
    }

    close(LIN);
}


#----------------------------------------------------------------------
# �ȣԣͣ�����
#----------------------------------------------------------------------
sub logPrintHtml {
    my ($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) = gmtime(time + $Hjst);
    $mon++;
    my ($sss) = "${mon}��${date}�� ${hour}��${min}ʬ${sec}��";

    $html1=<<_HEADER_;
<html><head>
  <title>�Ƕ�ν����</title>
  <base href="$htmlDir/">
  <link rel="stylesheet" type="text/css" href="${efileDir}/$HcssFile">
</head>
<body $htmlBody><DIV ID='BodySpecial'>
  <div id='RecentlyLog'>
    <h1>�Ƕ�ν����</h1>
    <form>
�ǿ���������$sss����
      <input type="button" value=" ���ɹ���" onClick="location.reload()">
    </form>
    <hr>
_HEADER_

$html3=<<_FOOTER_;
</div><hr></div></body></html>
_FOOTER_
    my ($i);
    my ($id);
    my ($mode);
    my ($set_turn) = 0;
    my ($line, $m, $turn, $id1, $id2, $message);
    for ($i = 0; $i < $HhtmlLogTurn; $i++) {
        $id =0;
        $mode = 0;
        $set_turn = 0;
        open(LIN, "${HdirName}/hakojima.log$i");
        while($line = <LIN>) {
            $line =~ /^([0-9]*),([0-9]*),([0-9]*),([0-9]*),(.*)$/;
            ($m, $turn, $id1, $id2, $message) = ($1, $2, $3, $4, $5);

            # ��̩�ط�
            if ($m) {
                next if(!$mode || ($id1 != $id)); # ��̩ɽ�������ʤ�
                $m = '<B>(��̩)</B>';
            } else {
                $m = '';
            }

            # ɽ��Ū�Τ�
            if ($id) {
                next if(($id != $id1) && ($id != $id2));
            }

            # ɽ��
            if (!$set_turn) {
                if(!$Hseason) {
                    $html2 .= "<B>=====[<span class='number'><font size='4'> ������$turn </font></span>]================================================</B><BR>\n";
                } else {
                    # �����ɽ��
                    my @seasonName = ('<span class=winter>��</span>','<span class=spring>��</span>','<span class=summer>��</span>','<span class=autumn>��</span>');
                    my $month = ($turn % 12) + 1;
                    my $year  = ($turn / 12) + 1;
                    my $calender = sprintf('<span class=month><font size=2><small>%s</small> %dǯ %d�� </FONT></span>' , $Halmanac, $year, $month);
                    $calender .= "<span class='season'>$seasonName[int(($month - 1) / 3)]</span>";
                    $html2 .= "<B>=====[<span class=number><font size=4> <small>������$turn</small> </FONT></span>]=============================$calender</B><BR>\n";
                }
                $set_turn++;
            }
            $html2 .= "<span class='number'>��</span>:$message<BR>\n";
        }
        close(LIN);
    }
    open(HTML, ">${HhtmlDir}/hakolog.html");
#    print HTML jcode::sjis($html1);
#    print HTML jcode::sjis($html2);
#    print HTML jcode::sjis($html3);
    print HTML $html1;
    print HTML $html2;
    print HTML $html3;
    close (HTML);
    chmod(0666,"${HhtmlDir}/hakolog.html");
}
