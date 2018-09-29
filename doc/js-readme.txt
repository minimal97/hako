----------------------------------------------------------------------------
●ＪＡＶＡスクリプト版箱庭諸島「あっぽー」Ver.1.00 ●
----------------------------------------------------------------------------
＜配布サイト＞

  オリジナル箱庭諸島２
    http://t.pos.to/hako/
    (http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html)

　ＪＡＶＡスクリプト版箱庭諸島「あっぽー」
　　あっぽー庵箱庭諸島 -- http://appoh.execweb.cx/hakoniwa/

----------------------------------------------------------------------------
＜作者について＞

　hako-main.cgi hako-tum.cgi hako-top.cgi hako-map.cgi
  hako-mente.cgi hako-readme.txt
　　徳岡宏樹氏(tokuoka@taurus.bekkoame.ne.jp)

　hako-js.cgi 及び 上記CGIの改変
　　あっぽー　(caa95880@pop06.odn.ne.jp)

----------------------------------------------------------------------------
＜このスクリプトの特徴＞
サーバーへの負担軽滅のための改造がほとんどです。 

●ＪＡＶＡスクリプトによる一括送信機能
  一括送信だけでなく、入力したコマンドを移動させて順番を変えることもできます。

●観光画面から他の島へジャンプ
  観光通信に島選択ボタンがありトップページに戻らないでも他の島へ移動できます。

●擬似ＭＡＰ作成ツール用データ自動生成
  開発画面に入り、左側の「表示」リンクをクリックすると選択した島の
  擬似ＭＡＰ作成ツール用データが自動生成されます。
  擬似ＭＡＰ作成ツールは、作者であるＭＫｕｄｏさんのホームページ で、
  配布されています。

●目標捕捉
  開発画面から「表示」リンクをクリックして攻撃目標の島のＭＡＰを開き、
  座標入力を補助します。（ Watson氏作）

●「埋め立て＋整地（または地ならし）」
       「整地（または地ならし）＋植林」コマンド追加
  通常開発画面の方も少しは入力しやすくなるように「整地自動入力」や
  「地ならし自動入力」の他に「浅瀬自動埋め立て」
  「埋め立て＋整地（または地ならし）」などを追加しました。
  指定した地点に「埋め立て」と「整地（地ならし）」コマンドを
  セットで入れてくれます。

●「最近の出来事」のログをＨＴＭＬファイルにして表示
  更新が終わると自動的にＨＴＭＬファイルに書き込まれ表示されます。
  また、サーバートラブルなどでＨＴＭＬファイルが作成されなかった場合でも
  島名変更のところで島名に「ログ」と入力し、特集パスワードを入力すると
  ＨＴＭＬファイルが作成されます。 

----------------------------------------------------------------------------
＜使用条件＞
　箱庭諸島2のスクリプトについては、自己責任で使用する限り、基本的には
　自由に利用してもらってかまいません。改造した物を再配布は、
  後述の条件に従ってください。

　また詳しくは、hako-redeme.txtの使用条件に従ってください。

----------------------------------------------------------------------------
　再配布条件
このスクリプトを改造し、再配布するときは、以下の条件を守ってください。

　・無料配布であること
　・hako-readme.txt 及び js-readme.txt を改変せずに添付すること
　・hako-redeme.txtに書いてある再配布条件を守ること
　・再配布条件としてこの条件と同等の物とすること。

上記の条件さえ守っていただければ、再配布は、自由です。

----------------------------------------------------------------------------

すでに設置している箱庭に組み込む場合は、下のように改造して下さい。


＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
＜hako-js.cgi＞
地形を追加したり、防衛施設を森にしている場合は、hako-map.cgiと同様、
hako-js.cgi の
sub landStringJava も修正しないとなりません。

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
＜hako-main.cgi＞

# 「戻る」リンク
$HtempBack = "<A HREF=\"$HthisFile\">${HtagBig_}トップへ戻る${H_tagBig}</A>";
# この下に追加
$Body = "<BODY $htmlBody>";

－－－－－－－－－－
# COOKIE出力
cookieOutput();

# ヘッダ出力
tempHeader();
# ↑これは消して下↓のを追加
if($HmainMode eq 'owner' && $HjavaMode eq 'java' ||
   $HmainMode eq 'commandJava' || # コマンド入力モード
   $HmainMode eq 'comment' && $HjavaMode eq 'java' || #コメント入力モード
   $HmainMode eq 'lbbs' && $HjavaMode eq 'java') { #コメント入力モード
	$Body = "<BODY onload=\"init()\" $htmlBody>";
   	require('hako-js.cgi');
    require('hako-map.cgi');
	# ヘッダ出力
	tempHeaderJava($bbs, $toppage,$imageDir);
	if($HmainMode eq 'commandJava') {
    	# 開発モード
    	commandJavaMain();
	} elsif($HmainMode eq 'comment') {
    	# コメント入力モード
    	commentMain();
	} elsif($HmainMode eq 'lbbs') {
	    # ローカル掲示板モード
    	localBbsMain();
	}else{
	    ownerMain();
	}
	# フッタ出力
	tempFooter();
	# 終了
	exit(0);
}elsif($HmainMode eq 'landmap'){
   	require('hako-js.cgi');
    require('hako-map.cgi');
	$Body = "<BODY $htmlBody>";
	# ヘッダ出力
	tempHeaderJava($bbs, $toppage,$imageDir);
    # 観光モード
    printIslandJava();
	# フッタ出力
	tempFooter();
	# 終了
	exit(0);
}else{
	# ヘッダ出力
	tempHeader();
}
－－－－－－－－－－
    # メッセージ
    if($line =~ /MESSAGE=([^\&]*)\&/) {
	$Hmessage = cutColumn($1, 80);
    }

# この下に下のを追加
    # Ｊａｖａスクリプトモード
	if($line =~ /JAVAMODE=(cgi|java)/) {
	$HjavaMode = $1;
	}

    if($line =~ /CommandJavaButton([0-9]+)=/) {
	# コマンド送信ボタンの場合（Ｊａｖａスクリプト）
	$HcurrentID = $1;
	$defaultID = $1;
    }
－－－－－－－－－－
    } elsif($getLine =~ /Sight=([0-9]*)/) {
	$HmainMode = 'print';
	$HcurrentID = $1;
# この下に下のを追加
    } elsif($getLine =~ /IslandMap=([0-9]*)/) {
	$HmainMode = 'landmap';
	$HcurrentID = $1;
－－－－－－－－－－
    } elsif($line =~ /MessageButton([0-9]*)/) {
	$HmainMode = 'comment';
	$HcurrentID = $1;
# この下に下のを追加
    } elsif($line =~ /CommandJavaButton/) {
	$HmainMode = 'commandJava';
	$line =~ /COMARY=([^\&]*)\&/;
	$HcommandComary = $1;
－－－－－－－－－－
<BASE HREF="$imageDir/">
</HEAD>
<BODY $htmlBody>
<A HREF="http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html">箱庭諸島スクリプト配布元</A><HR>

#これを下のように変更

<BASE HREF="$imageDir/">
</HEAD>
$Body
<A HREF="http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html">箱庭諸島スクリプト配布元</A><HR>
－－－－－－－－－－

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
＜hako-map.cgi＞

    # 観光画面
    tempPrintIslandHead(); # ようこそ!!
    islandInfo(); # 島の情報
    islandMap(0); # 島の地図、観光モード
#これを追加
    islandJamp();   # 島の移動

－－－－－－－－－－
    # 開発画面
    tempOwner(); # 「開発計画」

#これ↑を消して下↓のように変更

	if($HjavaMode eq 'java') {
	    tempOwnerJava(); # 「Javaスクリプト開発計画」
	}else{               # 「通常モード開発計画」
		tempOwner();
	}
－－－－－－－－－－
    # ○○島ローカル掲示板
    if($HuseLbbs) {
	tempLbbsHead();     # ローカル掲示板
	tempLbbsInputOW();   # 書き込みフォーム
	tempLbbsContents(); # 掲示板内容
    }

#これ↑を下↓のように変更

    # ○○島ローカル掲示板
    if($HuseLbbs) {
	tempLbbsHead();     # ローカル掲示板
		if($HjavaMode eq 'java') {  # Javaスクリプト用書き込みフォーム
			tempLbbsInputJava();
		}else{ tempLbbsInputOW(); } # 通常モードの書き込みフォーム
	tempLbbsContents(); # 掲示板内容
    }

－－－－－－－－－－
    out(<<END);
<CENTER>
<TABLE BORDER>
<TR>
<TD $HbgInputCell >
<CENTER>
<FORM action="$HthisFile" method=POST>
<INPUT TYPE=submit VALUE="計画送信" NAME=CommandButton$Hislands[$HcurrentNumber]->{'id'}>

#これ↑を下↓のように変更

    out(<<END);
<CENTER>
<TABLE BORDER>
<TR valign=top>
<TD $HbgInputCell >
<CENTER>
<FORM name="myForm" action="$HthisFile" method=POST>
<INPUT TYPE=submit VALUE="計画送信" NAME=CommandButton$Hislands[$HcurrentNumber]->{'id'}>
－－－－－－－－－－
    out(<<END);
</SELECT>
<HR>
<B>目標の島</B><BR>
<SELECT NAME=TARGETID>

#これ↑を下↓のように変更

    out(<<END);
</SELECT>
<HR>
<B>目標の島</B>：
<B><A HREF=JavaScript:void(0); onClick="jump(myForm)"> 表\示 </A></B><BR>
<SELECT NAME=TARGETID>
－－－－－－－－－－

function ns(x) {
    document.forms[0].elements[2].options[x].selected = true;
    return true;
}

#この上の処理の次の行に下の処理を追加。

function jump(theForm) {
  var sIndex = theForm.TARGETID.selectedIndex;
  var url = theForm.TARGETID.options[sIndex].value;
  if (url != "" ) window.open("$HthisFile?IslandMap=" +url,"", "menubar=yes,toolbar=no,location=no,directories=no,status=yes,scrollbars=yes,resizable=yes,width=450,height=630");
}

－－－－－－－－－－
hako-map.cgiの一番下の方に下の処理を追加。


# 島の移動
sub islandJamp {
    $HtargetList = getIslandList($HcurrentID);
    out(<<END);
<CENTER>
<SCRIPT LANGUAGE="JavaScript">
function jump(theForm) {
  var sIndex = theForm.urlsel.selectedIndex;
  var url = theForm.urlsel.options[sIndex].value;
  if (url != "" ) location.href = "$HthisFile?Sight=" +url;
}
</SCRIPT>
<TABLE align=center border=0>
<TR><TD>
<FORM name="urlForm">
<SELECT NAME="urlsel">
$HtargetList<BR>
</SELECT>
</TD>
<TD><input type="button" value=" GO " onClick="jump(this.form)"></TD>
</TR></TABLE>
</form>
</CENTER>
END
}


＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
＜hako-top.cgi＞

<H1>${HtagHeader_}自分の島へ${H_tagHeader}</H1>
<FORM action="$HthisFile" method="POST">
あなたの島の名前は？<BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT><BR>

パスワードをどうぞ！！<BR>
<INPUT TYPE="password" NAME="PASSWORD" VALUE="$HdefaultPassword" SIZE=32 MAXLENGTH=32><BR>
<INPUT TYPE="submit" VALUE="開発しに行く" NAME="OwnerButton"><BR>
</FORM>

#これ↑を下↓のように変更

<H1>${HtagHeader_}自分の島へ${H_tagHeader}</H1>
<FORM name="Island" action="$HthisFile" method="POST">
あなたの島の名前は？<BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT><BR>
<Script Language="JavaScript">
<!--
function develope(){
	if(document.Island.CHBOX.checked)
		document.Island.target = "_blank";
	else
		document.Island.target = "";
		return true;
}
//-->
</Script>
パスワードをどうぞ！！<BR>
<INPUT TYPE="password" NAME="PASSWORD" VALUE="$HdefaultPassword" SIZE=32 MAXLENGTH=32><BR>
<INPUT TYPE="radio" NAME=JAVAMODE VALUE=cgi checked>通常モード
<INPUT TYPE="radio" NAME=JAVAMODE VALUE=java>Javaスクリプトモード<BR>
<INPUT TYPE="submit" VALUE="開発しに行く" NAME="OwnerButton" onClick="develope()">
<INPUT TYPE="checkbox" NAME="CHBOX" VALUE="on" $chbox>新しい画面で開発
</FORM>


－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
＜最近の出来事のＨＴＭＬ出力＞

hako-main.cgi の一番下の方に下の処理を追加。

#----------------------------------------------------------------------
# ＨＴＭＬ生成
#----------------------------------------------------------------------
sub logPrintHtml {
	my($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) = localtime(time);
	$mon++;
	my($sss) = "${mon}月${date}日 ${hour}時${min}分${sec}秒";

	$html1=<<_HEADER_;
<HTML><HEAD>
<TITLE>
最近の出来事
</TITLE>
<BASE HREF="$imageDir/">
</HEAD>
<BODY $htmlBody>
<H1>${HtagHeader_}最近の出来事${H_tagHeader}</H1>
<FORM>
最新更新日：$sss・・
<INPUT TYPE="button" VALUE=" 再読込み" onClick="location.reload()">
</FORM>
<hr>
_HEADER_

$html3=<<_HEADER_;
<HR>
</BODY>
</HTML>
_HEADER_
	my($i);
	for($i = 0; $i < $HtopLogTurn; $i++) {
		$id =0;
		$mode = 0;
		my($set_turn) = 0;
		open(LIN, "${HdirName}/hakojima.log$i");
		my($line, $m, $turn, $id1, $id2, $message);
		while($line = <LIN>) {
			$line =~ /^([0-9]*),([0-9]*),([0-9]*),([0-9]*),(.*)$/;
			($m, $turn, $id1, $id2, $message) = ($1, $2, $3, $4, $5);

			# 機密関係
			if($m == 1) {
				if(($mode == 0) || ($id1 != $id)) {
				# 機密表示権利なし
				next;
				}
				$m = '<B>(機密)</B>';
			} else {
				$m = '';
			}

			# 表示的確か
			if($id != 0) {
				if(($id != $id1) &&	($id != $id2)) {
					next;
				}
			}

			# 表示
			if($set_turn == 0){
				$html2 .= "<NOBR><B>=====[<FONT SIZE=4 COLOR=BLUE>ターン$turn </FONT>]================================================</B><NOBR><BR>\n";
				$set_turn++;
			}
			$html2 .= "<NOBR>${HtagNumber_}★${H_tagNumber}:$message</NOBR><BR>\n";
		}
		close(LIN);
	}
	open(HTML, ">hakolog.html");
	print HTML jcode::sjis($html1);
	print HTML jcode::sjis($html2);
	print HTML jcode::sjis($html3);
	close (HTML);
	chmod(0666,"hakolog.html");
}
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
hako-turn.cgi

    # ログ書き出し
    logFlush();

    # 記録ログ調整
    logHistoryTrim();

	# 最近の出来事ＨＴＭＬ出力  ←これを追加
	logPrintHtml();

    # トップへ
    topPageMain();
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

    # パスワードチェック
    if($HoldPassword eq $HspecialPassword) {
	# 特殊パスワード
	$island->{'money'} = 9999;
	$island->{'food'} = 9999;
    } elsif(!checkPassword($island->{'password'},$HoldPassword)) {
	# password間違い
	unlock();
	tempWrongPassword();
	return;
    }

#これ↑を下↓のように変更

    # パスワードチェック
    if($HoldPassword eq $HspecialPassword) {
	# 特殊パスワード
	if($HcurrentName =~ /^ログ$/) {
	    # 最近の出来事強制出力
		logPrintHtml();
		unlock();
    	tempChange();
	    return;
	}else {
	    # 食糧/資金maxモード
		#$island->{'money'} = 9999;
		#$island->{'food'} = 9999;
	}
    } elsif(!checkPassword($island->{'password'},$HoldPassword)) {
	# password間違い
	unlock();
	tempWrongPassword();
	return;
    }


=*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*=
ver1.1 への改造方法

上の ver1.00 の改造が終った後に、下の改造を行なって下さい。
hako-js.cgi は、ver1.1のに差し替えて下さい。

＜hako-main.cgi＞
# コマンド
$HcommandTotal = 33; # コマンドの種類

#↑この下に、これ↓を追加

# コマンド分割
# このコマンド分割だけは、自動入力系のコマンドは設定しないで下さい。
@HcommandDivido = 
	(
	'開発,0,10',  # 計画番号00～10
	'建設,11,30', # 計画番号11～30
	'攻撃,31,40', # 計画番号31～40
	'運営,41,60'  # 計画番号41～60
	);
# 注意：スペースは入れないように
# ○→	'開発,0,10',  # 計画番号00～10
# ×→	'開発, 0  ,10  ',  # 計画番号00～10

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
下のように変更。
「ver1.1より追加」とある部分（２ヶ所）と<BODY>タグの部分を変更。

if($HmainMode eq 'owner' && $HjavaMode eq 'java' ||
   $HmainMode eq 'commandJava' || # コマンド入力モード
   $HmainMode eq 'command2' || # コマンド入力モード（ver1.1より追加・自動系用）
   $HmainMode eq 'comment' && $HjavaMode eq 'java' || #コメント入力モード
   $HmainMode eq 'lbbs' && $HjavaMode eq 'java') { #コメント入力モード
	$Body = "<BODY onload=\"SelectList('');init()\" $htmlBody>";
   	require('hako-js.cgi');
    require('hako-map.cgi');
	# ヘッダ出力
	tempHeaderJava($bbs, $toppage,$imageDir);
	if($HmainMode eq 'commandJava') {
    	# 開発モード
    	commandJavaMain();
	} elsif($HmainMode eq 'command2') {
    	# 開発モード２（自動系コマンド用（ver1.1より追加・自動系用））
	    commandMain();
	} elsif($HmainMode eq 'comment') {
    	# コメント入力モード
    	commentMain();

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    # Ｊａｖａスクリプトモード
	if($line =~ /JAVAMODE=(cgi|java)/) {
	$HjavaMode = $1;
	}

#↑この下に、これ↓を追加

	if($getLine =~ /JAVAMODE=(cgi|java)/) {
	$HjavaMode = $1;
	}
    # コマンドのポップアップメニューを開く？
	if($line =~ /MENUOPEN=([a-zA-Z]*[0-9]*)/) {
	$HmenuOpen = $1;
	}

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

    } elsif($line =~ /CommandButton/) {
	$HmainMode = 'command';

	# コマンドモードの場合、コマンドの取得
	$line =~ /NUMBER=([^\&]*)\&/;

#これ↑を、下のように変更

    } elsif($line =~ /CommandButton/) {
	if($HjavaMode eq 'java'){
	$HmainMode = 'command2';
	}else{
	$HmainMode = 'command';
	}

	# コマンドモードの場合、コマンドの取得
	$line =~ /NUMBER=([^\&]*)\&/;

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    if($cookie =~ /${HthisFile}KIND=\(([^\)]*)\)/) {
	$HdefaultKind = $1;
    }

#この↑下に、これ↓を追加

    if($cookie =~ /${HthisFile}JAVAMODESET=\(([^\)]*)\)/) {
	$HjavaModeSet = $1;
    }
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

    if($HcommandKind) {
	# 自動系以外
	$cookie .= "Set-Cookie: ${HthisFile}KIND=($HcommandKind) $info";
    }

#↑この下に、これ↓を追加

    if($HjavaMode) {
	$cookie .= "Set-Cookie: ${HthisFile}JAVAMODESET=($HjavaMode) $info";
    }

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
＜hako-top.cgi＞


	# 次回更新時間表示
    my($now) = time;
    $aaa = $HislandLastTime + $HunitTime;
    my($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) = localtime(time);
	$mon++;
    my($sss) = "${mon}月 ${date}日 ${hour}時 ${min}分 ${sec}秒";
    my($sec2, $min2, $hour2, $date2, $mon2, $year2, $day2, $yday2, $dummy2) = localtime($aaa);
	$mon2++;
    my($bbb) = "${mon2}月${date2}日${hour2}時${min2}分";

#↑この下に、これ↓を追加

    if ($HjavaModeSet eq 'java') {
		$radio = ""; $radio2 = "CHECKED";
	}else{
		$radio = "CHECKED";	$radio2 = "";
	}

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
下のように変更。


<H1>${HtagHeader_}自分の島へ${H_tagHeader}</H1>
<SCRIPT language="JavaScript">
<!--
function newdevelope(){
	newWindow = window.open("", "newWindow");
	document.Island.target = "newWindow";
	document.Island.submit();
}
function develope(){
	document.Island.target = "";
}
//-->
</SCRIPT>
<FORM name="Island" action="$HthisFile" method="POST">
あなたの島の名前は？<BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT><BR>
パスワードをどうぞ！！<BR>
<INPUT TYPE="hidden" NAME="OwnerButton">
<INPUT TYPE="password" NAME="PASSWORD" VALUE="$HdefaultPassword" SIZE=32 MAXLENGTH=32><BR>
<INPUT TYPE="radio" NAME=JAVAMODE VALUE=cgi $radio>通常モード
<INPUT TYPE="radio" NAME=JAVAMODE VALUE=java $radio2>Javaスクリプトモード<BR>
<INPUT TYPE="submit" VALUE="開発しに行く" onClick="develope()">　
<INPUT TYPE="button" VALUE="新しい画面" onClick="newdevelope()">
</FORM>

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
＜hako-map.cgi＞

function jump(theForm) {
  var sIndex = theForm.TARGETID.selectedIndex;
  var url = theForm.TARGETID.options[sIndex].value;
  if (url != "" ) window.open("$HthisFile?IslandMap=" +url,"", "menubar=yes,toolbar=no,location=no,directories=no,status=yes,scrollbars=yes,resizable=yes,width=450,height=630");
}

#これ↑を、下のように変更（「j_mode」の記述を２ヶ所入れる）

function jump(theForm, j_mode) {
	var sIndex = theForm.TARGETID.selectedIndex;
	var url = theForm.TARGETID.options[sIndex].value;
	if (url != "" ) window.open("$HthisFile?IslandMap=" +url+"&JAVAMODE="+j_mode, "", "menubar=yes,toolbar=no,location=no,directories=no,status=yes,scrollbars=yes,resizable=yes,width=450,height=630");
}

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

<B><A HREF=JavaScript:void(0); onClick="jump(myForm)"> 表\示 </A></B><BR>

#これ↑を、下のように変更

<B><A HREF=JavaScript:void(0); onClick="jump(myForm, '$HjavaMode')"> 表\示 </A></B><BR>

