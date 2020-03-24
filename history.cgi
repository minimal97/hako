#!/usr/bin/perl
# ＲＡ用に改造
#---------------------------------------------------------------------
#   究想の箱庭　最近の出来事と最近の天気の履歴を表示
#
#   作成日 : 2001/11/25 (ver0.10)
#   作成者 : ラスティア <nayupon@mail.goo.ne.jp>
#---------------------------------------------------------------------
#use strict "vars";
use strict "refs";
#use strict "subs";
use Time::HiRes;

require './server_config.pm';

BEGIN {
    # Perl 5.004 以上が必要
    require 5.004;

########################################
    # エラー表示
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
#    初期設定
#---------------------------------------------------------------------
# 初期設定用ファイルを読み込む
require './hako-init.cgi';
require './hako-io.cgi';

#----------------------------
#    HTMLに関する設定
#----------------------------
# ブラウザのタイトルバーの名称
$title = '最近の出来事';

# 画面の色や背景の設定(HTML)
$body = '<body bgcolor=#EEFFEE>';

# 画面の「戻る」リンク先(URL)
$bye = './hako-main.cgi';

#メインルーチン-------------------------------------------------------
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
  <h1>不正なアクセスです</h1>
$server_config::HbaseDir / $ENV{HTTP_REFERER} / $HcurrentID
  </body>
</html>
END
    exit(0);
}
if (-e $HpasswordFile) {
    # パスワードファイルがある
    open(PIN, "<$HpasswordFile") || die $!;
    chomp($HmasterPassword  = <PIN>); # マスタパスワードを読み込む
    chomp($HspecialPassword = <PIN>); # 特殊パスワードを読み込む
    close(PIN);
}
if ($HhtmlLogMake && ($HcurrentID == 0)) {
    unless (-e "${HhtmlDir}/hakolog.html") {
        # 最近の出来事ＨＴＭＬ出力
        logPrintHtml();
        tempRefresh(3, 'ログ作成中です。そのまましばらくお待ち下さい');
    }
    else {
        tempRefresh(0, 'しばらくお待ち下さい');
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
        # 最近の出来事
        if ($HMode == 99) {
            if ($HcurrentID == 0) {
                logFilePrintAll();
            }
            else {
                tempIslandHeader($HcurrentID, $HcurrentName);
                # パスワード
                if (checkPassword($island, $HinputPassword) && ($HcurrentID eq $defaultID)) {
                    logPrintLocal(1);
                }
                else {
                    # password違う
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
                # パスワード
                if (checkPassword($island, $HinputPassword) && ($HcurrentID eq $defaultID)) {
                    logFilePrint($HMode, $HcurrentID, 1);
                }
                else {
                    # password間違い
                    logFilePrint($HMode, $HcurrentID, 0);
                }
            }
        }
        out("</div>\n");
    }
}
tempFooter();
#終了
exit(0);

#サブルーチン---------------------------------------------------------
#---------------------------------------------------------------------
#    関数名 : htmlError
#    機　能 : HTMLのエラーメッセージの出力
#    引　数 : なし
#    戻り値 : なし
#---------------------------------------------------------------------
sub htmlError{
    out("<h2>エラーが発生しました</h2>\n");
}
#--------------------------------------------------------------------
#    POST or GETで入力されたデータ取得
#--------------------------------------------------------------------
sub cgiInput {
    my($line, $getLine);

    # 入力を受け取って日本語コードをEUCに
    $line = <>;
    $line =~ tr/+/ /;
    $line =~ s/%([a-fA-F0-9]{2})/pack('H2', $1)/eg;
#   jcode::convert(\$line, 'euc');
    $line =~ s/[\x00-\x1f\,]//g;

    # GETのやつも受け取る
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
#cookie入力
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
#    HTMLのヘッダとフッタ部分を出力
#---------------------------------------------------------------------
# ヘッダ
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
# <A HREF="$bye">[戻る]</A><br>
    out(<<END);
<span class="big"><a href=href=\"#\" onclick=\"window.close()\">[閉じる]</a></span><br>
END
    logDekigoto();
    out(<<END);
<hr>
<form name="recentForm" action="$server_config::HbaseDir/history.cgi" method="post" style="margin  : 2px 0px;">
<b>[最近の出来事]</b><br>
<!-- <A href="history.cgi?Event=99">【ALL】</A> -->
END
    my ($i, $turn);
    out("<span class='HistoryTurnList'>");
    for ($i = 0;$i < $HtopLogTurn;$i++) {
        $turn = $HislandTurn - $i;
        last unless($turn > 0);
        out("<A HREF='history.cgi?Event=${i}'>");
        if ($i == 0) {
            out("[ターン${turn}(現在)]<br>");
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
  <input type="submit" value="を見る">
</form>
END

}

# フッタ
sub tempFooter {
    out(<<END);
<hr>
<div class='LinkFoot' align='center'>
  <small>ホームページ(<a href="$Htoppage">■</a>)</small>
END

##### 追加 親方20020307
    if (USE_PERFORMANCE) {
        my ($uti, $sti, $cuti, $csti) = times();
        $uti += $cuti;
        $sti += $csti;
        my ($cpu) = $uti + $sti;
        my ($timea) = sprintf("%.3f",Time::HiRes::time - $Hakoniwa_start_time);

    #       ログファイル書き出し(テスト計測用　普段はコメントにしておいてください)
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
# html化リフレッシュ
sub tempRefresh {
    my($delay, $str) = @_;

    unless($Hgzip == 1) {
        print qq{Content-type: text/html; charset=EUC-JP\n\n};
        print qq{<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\n\n};
        out(<<END);
<html>
<head>
  <title>HTML化</title>
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

# 島データのプルダウンメニュー用
sub getIslandList {
    my ($select) = @_;

    my ($list, $name, $id, $s, $i);

    #島リストのメニュー
    $list = '';
    my ($predel);
    foreach $i (0..$islandNumber) {
        $name = islandName($Hislands[$i]);
        $name =~ s/<[^<]*>//g;
        $predel = ($Hislands[$i]->{'predelete'}) ? '[預]' : '';
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
#    島の近況のリンク
#---------------------------------------------------------------------
# ヘッダ
sub tempIslandHeader {
my($id, $name) = @_;

    if(checkPassword($Hislands[$HidToNumber{$id}]->{'password'}, $HinputPassword) && ($HcurrentID eq $defaultID)) {
        out(<<END);
<hr>
<font color=\"#FF0000\"><b>[${name}の近況]</b></font>
END
    } else {
        out(<<END);
<hr>
<b>[${name}の近況]</b>　
END
    }

    if($HinputPassword eq '') {
        out("<A HREF='history.cgi?ID=${id}&Event=99'><br>【ALL】</A>");
    } else {
        out("<A HREF='history.cgi?ID=${id}&PASSWORD=${HinputPassword}&Event=99'><br>【ALL】</A>");
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
            out("[ターン${turn}(現在)]<br>");
        } else {
            out("[${turn}]");
        }
        out("</A>");
        out("<br>\n") if($i != 0 && ($i % 10) == 0 ); 
    }
    out("<HR>\n");
}
#---------------------------------------------------------------------
#    ログファイルタイトル
#---------------------------------------------------------------------
sub logDekigoto {
    out(<<END);
<h1>最近の出来事</h1>
END
}


#---------------------------------------------------------------------
#    ログファイル全て表示
#---------------------------------------------------------------------
sub logFilePrintAll {
    my ($i);
    for($i = 0; $i < $HtopLogTurn; $i++) {
        logFilePrint($i, 0, 0);
    }
}


#---------------------------------------------------------------------
# 個別ログ表示
#---------------------------------------------------------------------
sub logPrintLocal {
    my ($mode) = @_;
    my ($i);
    for($i = 0; $i < $HtopLogTurn; $i++) {
        logFilePrint($i, $HcurrentID, $mode);
    }
}


#---------------------------------------------------------------------
#    ファイル番号指定でログ表示 #ＲＡ用
#---------------------------------------------------------------------
sub logFilePrint {
    my ($fileNumber, $id, $mode) = @_;
    my ($set_turn) = 0;
    open(LIN, "${HdirName}/hakojima.log$_[0]");
    my ($line, $m, $turn, $id1, $id2, $message);

    while ($line = <LIN>) {
        $line =~ /^([0-9]*),([0-9]*),([0-9]*),([0-9]*),(.*)$/;
        ($m, $turn, $id1, $id2, $message) = ($1, $2, $3, $4, $5);

        # 機密関係
        if ($m == 1) {
            if (($mode == 0) || ($id1 != $id)) {
                # 機密表示権利なし
                next;
            }
            $m = '<b>(機密)</b>:';
        } else {
            $m = '';
        }

        # 表示的確か
        if ($id != 0) {
            if(($id != $id1) &&
               ($id != $id2)) {
                next;
            }
        }

        if(!$set_turn){
            if(!$Hseason) {
                out("<b>=====[<span class='number'><font size='4'> ターン$turn </font></span>]=====</b><br>\n");
            } else {
                # 季節の表示
                my @seasonName = ('<span class="winter">冬</span>','<span class="spring">春</span>','<span class="summer">夏</span>','<span class="autumn">秋</span>');
                my ($month) = ($turn % 12) + 1;
                my ($year)  = ($turn / 12) + 1;
                my ($calender) = sprintf('<span class=month><FONT SIZE=2><small>%s</small> %d年 %d月 </FONT></span>' , $Halmanac, $year, $month);
                $calender .= "<span class='season'>$seasonName[int(($month - 1) / 3)]</span>";
                out("<b>=====[<span class='number'><font size='4'> <small>ターン$turn</small> </font></span>]=====$calender</b><br>\n");
            }
            $set_turn++;
        }
        out('・'.${m}.$message."<br>\n");
    }

    close(LIN);
}


#----------------------------------------------------------------------
# ＨＴＭＬ生成
#----------------------------------------------------------------------
sub logPrintHtml {
    my ($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) = gmtime(time + $Hjst);
    $mon++;
    my ($sss) = "${mon}月${date}日 ${hour}時${min}分${sec}秒";

    $html1=<<_HEADER_;
<html><head>
  <title>最近の出来事</title>
  <base href="$htmlDir/">
  <link rel="stylesheet" type="text/css" href="${efileDir}/$HcssFile">
</head>
<body $htmlBody><DIV ID='BodySpecial'>
  <div id='RecentlyLog'>
    <h1>最近の出来事</h1>
    <form>
最新更新日：$sss・・
      <input type="button" value=" 再読込み" onClick="location.reload()">
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

            # 機密関係
            if ($m) {
                next if(!$mode || ($id1 != $id)); # 機密表示権利なし
                $m = '<B>(機密)</B>';
            } else {
                $m = '';
            }

            # 表示的確か
            if ($id) {
                next if(($id != $id1) && ($id != $id2));
            }

            # 表示
            if (!$set_turn) {
                if(!$Hseason) {
                    $html2 .= "<B>=====[<span class='number'><font size='4'> ターン$turn </font></span>]================================================</B><BR>\n";
                } else {
                    # 季節の表示
                    my @seasonName = ('<span class=winter>冬</span>','<span class=spring>春</span>','<span class=summer>夏</span>','<span class=autumn>秋</span>');
                    my $month = ($turn % 12) + 1;
                    my $year  = ($turn / 12) + 1;
                    my $calender = sprintf('<span class=month><font size=2><small>%s</small> %d年 %d月 </FONT></span>' , $Halmanac, $year, $month);
                    $calender .= "<span class='season'>$seasonName[int(($month - 1) / 3)]</span>";
                    $html2 .= "<B>=====[<span class=number><font size=4> <small>ターン$turn</small> </FONT></span>]=============================$calender</B><BR>\n";
                }
                $set_turn++;
            }
            $html2 .= "<span class='number'>★</span>:$message<BR>\n";
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
