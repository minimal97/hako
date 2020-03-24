#!/usr/bin/perl

# patchworked by neo_otacky. for 海戦JS RAJS
# 　lbbslist.cgi?pass=[マスタパス]でアクセスすると、投稿欄もつきます。
# 　投稿する時の投稿名は管理者名で、島名は「管理人」になります。
# 　注！クッキーにマスタパスを喰ってる場合は、普通にアクセスするだけでOK!
#---------------------------------------------------------------------
#	
#	究想の箱庭　ローカル掲示板を一覧表示
#
#	作成日 : 2001/10/06 (ver0.10)
#	作成者 : ラスティア <nayupon@mail.goo.ne.jp>
#
#	管理者が島民の発言を逃さないよう一覧で確認するためのものです。
#	lbbslist.cgi?pass=マスタパス　でアクセスすると極秘通信も見れます。
#
#	修正履歴
#	2001/10/20 V0.20 最近の発言を色を変えて表示できるようにした。
#	2001/12/31 V0.30 共通設定部をconfig.cgiから取り込むようにした。
#	2002/01/13 V0.31 version4対応
#	2002/02/03 V0.40 CSSを別ファイルから読み込むようにした。
#	2002/04/17 V0.41 負荷表示をつけた。スクリプトを全体的に見直し。
#	2002/07/27 V0.50 極秘通信に対応。見た目の改善等。
#	2002/10/28 V0.60 スタイルシート辺りを改良
#
#---------------------------------------------------------------------
#	当スクリプトは以下を元に作成しました
#
#	怪獣撃退ポイント＋獲得賞金　ランキング表示
#	作成者 : Watson <watson@catnip.freemail.ne.jp>
#---------------------------------------------------------------------
require "./html_template.pl";
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
#	初期設定
#---------------------------------------------------------------------
# 初期設定用ファイルを読み込む
require './hako-init.cgi';
require './hako-io.cgi';
require './init-game.cgi';

# 色を変えて表示するターン
$kyoutyouturn = 100;

#----------------------------
#	HTMLに関する設定
#----------------------------
# ブラウザのタイトルバーの名称
$title = '観光者通信一覧';

# 冒頭のメッセージ(HTML書式)
$headKill = <<"EOF";
<h1>$Htitle 観光者通信一覧表（管理用）</h1>
EOF

# 画面の色や背景の設定(HTML)
$body = '<body bgcolor=#EEFFFF>';

# 画面の「戻る」リンク先(URL)
$bye = $HthisFile;

# 島の名前など
$HtagName_ = '<span class="islName">';
$H_tagName = '</span>';
# 順位表における見だし
$HtagTH_ = '<span class="head">';
$H_tagTH = '</span>';

$HbgTitleCell   = 'class=TitleCell';   # 順位表見出し
$HbgNumberCell  = 'class=NumberCell';  # 順位表順位
$HbgNameCell    = 'class=NameCell';    # 順位表島の名前
$HbgInfoCell    = 'class=InfoCell';    # 順位表島の情報
$HbgCommentCell = 'class=CommentCell'; # 順位表コメント欄
#ここまで-------------------------------------------------------------

if (-e $HpasswordFile) {
	# パスワードファイルがある
	open(PIN, "<$HpasswordFile") || die $!;
	chomp($HmasterPassword = <PIN>); # マスタパスワードを読み込む
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
		tempWrongPassword(); # パスワード違い
		&htmlFooter;
		exit(0);
	}
}
my ($bye2) = (!$mode) ? '' : "[<A HREF=\"$HmenteFile?ADMIN=$HdefaultPassword\">メンテナンスへ</A>] ";

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
    out("当スクリプトは、サーバに負荷がかかると思われるため箱庭本体からリンクを張っていません。<br>");
    out("頻繁にアクセスしたり、リロードなどの行為はできるだけ控えるように！<br>");
    out("<table border><tr><td>");
    foreach $i (0..$islandNumber) {
        &tempLbbsContents($i);
    }
    out("<TR><TD colspan=2 class='M'><P align='center'>${AfterName}の名前をクリックすると、観光することができます。</P></TD></TR>");
    # ヘッダのコメントを書き換える場合(hako-init.cgiでコメントアウトしている部分と連動)
    # &tempNews if($mode);
    out("</TABLE>");
    out("</DIV>");
}
&htmlFooter;
#終了
exit(0);


#サブルーチン---------------------------------------------------------
#--------------------------------------------------------------------
#	POST or GETで入力されたデータ取得
#--------------------------------------------------------------------
sub cgiInput {
    my ($line, $getLine);
    $line = <>;
    $line =~ tr/+/ /;
    $line =~ s/%([a-fA-F0-9]{2})/pack(H2, $1)/eg;

    # GETのやつも受け取る
    $getLine = $ENV{'QUERY_STRING'};

    if ($getLine =~ /pass=([^\&]*)/) {
        # 最初の起動
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
# cookie入力
#---------------------------------------------------------------------
sub cookieInput {
    my ($cookie);
#   $cookie = jcode::euc($ENV{'HTTP_COOKIE'}); # jcode使用時
    $cookie = $ENV{'HTTP_COOKIE'};
    if ($cookie =~ /${HthisFile}OWNISLANDPASSWORD=\(([^\)]*)\)/) {
        $HdefaultPassword = $1;
    }
}


#---------------------------------------------------------------------
#	関数名 : htmlHeader
#	機　能 : HTMLのヘッダ部分を出力
#	引　数 : なし
#	戻り値 : なし
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

    # 自分のサイトなどへのリンクを追加する場合は↑に追加してください。
    # むやみに↓にリンクを追加しないで下さい。JavaScript エラーの原因になることがあります。

    out(<<END) if(defined $HleftTime);
<HR><FORM name=TIME style="margin: 1px 0px;">
<H1 style="display:inline;"><SMALL><B>ターン</B> </SMALL>$HislandTurn</H1>
<INPUT type=text name=TIME size=52 readonly class="timer">
</FORM>
<HR></DIV>
${bye2}<A HREF="$bye">[戻る]</A><br><br>
END
}


#---------------------------------------------------------------------
#	関数名 : htmlFooter
#	機　能 : HTMLのフッタ部分を出力
#	引　数 : なし
#	戻り値 : なし
#---------------------------------------------------------------------
sub htmlFooter {
	out(<<END);
<HR>
<DIV ID='LinkFoot'>
$Hfooter
<BR></DIV>
END
##### 追加 親方20020307
	if($Hperformance) {
		my($uti, $sti, $cuti, $csti) = times();
		$uti += $cuti;
		$sti += $csti;
		my($cpu) = $uti + $sti;

	#	   ログファイル書き出し(テスト計測用　普段はコメントにしておいてください)
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
#	関数名 : htmlError
#	機　能 : HTMLのエラーメッセージの出力
#	引　数 : なし
#	戻り値 : なし
#---------------------------------------------------------------------
sub htmlError{
	out("<H2>エラーが発生しました</H2>\n");
}


#---------------------------------------------------------------------
#	関数名 : tempLbbsContents
#	機　能 : ローカル掲示板内容
#	引　数 : なし
#	戻り値 : なし
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
<TR><TH $HbgTitleCell>${HtagTH_}${AfterName}名${H_tagTH}</TH>
<TD $HbgNameCell>
<A STYlE=\"text-decoration:none\" HREF="${HthisFile}?Sight=${id}" TARGET=_blank>
${HtagName_}$name${H_tagName}
</A>
</TD><TH $HbgTitleCell>${HtagTH_}島主${H_tagTH}</TH>
<TD $HbgInfoCell>$owner</TD></TR>
<TR><TH $HbgTitleCell>${HtagTH_}コメント${H_tagTH}</TH><TD $HbgCommentCell colspan=3>$comment</TD></TR>
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
<INPUT TYPE="radio" NAME="LBBSTYPE" VALUE="PUBLIC" CHECKED>公開<br>
<INPUT TYPE="radio" NAME="LBBSTYPE" VALUE="SECRET"><span class='lbbsST'>極秘</span>
<INPUT TYPE="submit" VALUE="記帳する" NAME="LbbsButtonAD$id">
番号
<SELECT NAME=NUMBER>
END
		# 発言番号
		my ($j, $i);
		for ($i = 0; $i < $HlbbsMax; $i++) {
			$j = $i + 1;
			out("<OPTION VALUE=$i>$j\n");
		}
		out("<OPTION VALUE=$HlbbsMax>全\n");
		out(<<END);
</SELECT>
<INPUT TYPE="submit" VALUE="削除" NAME="LbbsButtonDA$id">
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

            if ($tan =~ /^([0-9]*)：/) {

                $turn = $1;
            }

            if ($turn >= $HislandTurn - $kyoutyouturn) {

                out("<TD class='RankingCell' colspan=3>");
            }
            else {

                out("<TD $HbgInfoCell colspan=3>");
            }

            if ($os == 0) {
                # 観光者
                if ($m == 0) {
                    # 公開
                    out("<span class='lbbsSS'>$tan > $com</span> $speaker</TD></TR>");
                }
                else {
                    # 極秘
                    if (!$mode) {
                        # 観光客
                        out("<DIV align='center'><span class='lbbsST'>- 極秘 -</span></DIV></TD></TR>");
                    }
                    else {
                        # オーナー
                        out("<span class='lbbsSS'>$tan >(秘) $com</span> $speaker</TD></TR>");
                    }
                }
            }
            else {
                # 島主
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
<TR><TD colspan=4><big><B>コメント変更(トップページの最上部リンク直下)</B></big>
　<INPUT TYPE="hidden" VALUE="$HdefaultPassword" NAME="NewsComment">
　<INPUT TYPE="submit" VALUE="変更">
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
↓↓↓　Preview　↓↓↓
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
        #終了
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