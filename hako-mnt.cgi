#!/usr/bin/perl
# ↑はサーバーに合わせて変更して下さい。

#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# メンテナンスツール(ver1.01)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------

# 初期設定用ファイルを読み込む
require './hako-init.cgi';
require './hako-io.cgi';
require './init-server.cgi';

# hako-mente.cgi を初めてブラウザで開くと、マスタパスワードと特殊パスワードの
# 入力を要求されます。ここで入力されたパスワードは暗号化され、パスワードファイル
# に記憶されます。

# パスワードを変更する場合は、FTP で接続してパスワードファイルを削除してください。
# その後、hako-mente.cgi をブラウザで開いてパスワードの設定を行います。
# この操作でゲームデータが壊れることはありません。ゲーム中でも変更できます。

# ――――――――――――――――――――――――――――――
# 各種設定値
# ――――――――――――――――――――――――――――――

# このファイル
my($thisFile) = './hako-mente.cgi';

# use Time::Localが使えない環境では、'use Time::Local'の行を消して下さい。
# かわりにこのファイルの一番最後でコメントアウトしてあるTime::Local の互換関数
# sub timelocalを使って下さい。

use Time::Local;

# ――――――――――――――――――――――――――――――
# 設定項目は以上
# ――――――――――――――――――――――――――――――
my $title   = 'Hakoniwa R.A. メンテナンスツール';

# 大きい文字
my ($HtagBig_) = '<span class="big">';
my ($H_tagBig) = '</span>';
# ――――――――――――――――――――――――――――――
# メイン
# ――――――――――――――――――――――――――――――

# 各種変数
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
  <title>箱庭諸島ＲＡ メンテナンスツール</title>
  <meta http-equiv="Content-Type" content="text/html; charset=EUC-JP">
  <meta name="theme-color" content="#99FF99">
  <link rel="shortcut icon" href="./img/fav.ico">
  <link rel="stylesheet" type="text/css" href="${efileDir}/$HcssFile">
</head>
<body>
END

if (-e $HpasswordFile) {
    # パスワードファイルがある
    open(PIN, "<$HpasswordFile") || die $!;
    chomp($HmasterPassword = <PIN>); # マスタパスワードを読み込む
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
    # 現在の時間を取得
    my ($now) = time;
    $now = $now - ($now % ($HunitTime));

    open(OUT, ">$HdirName/$HmainData"); # ファイルを開く
    print OUT "0\n";         # ターン数0
    print OUT "$now\n";      # 開始時間
    print OUT "0\n";         # 島の数
    print OUT "1\n";         # 次に割り当てるID

    # ファイルを閉じる
    close(OUT);
}


# ----------------------------------------------------
#
# setupMode
#
sub setupMode {
    if (!($mpass1 && $mpass2) || ($mpass1 ne $mpass2)) {
        print "${HtagBig_}マスタパスワードが入力されていないか間違っています${H_tagBig}";
        return;
    }
    if (!($spass1 && $spass2) || ($spass1 ne $spass2)) {
        print "${HtagBig_}特殊パスワードが入力されていないか間違っています${H_tagBig}";
        return;
    }

    if (-e $HpasswordFile) {
        # セキュリティーホールのチェック
        print "${HtagBig_}すでにパスワードが設定されています${H_tagBig}";
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
    print "${HtagBig_}パスワードを設定しました${H_tagBig}";
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
        # パスワードファイルがない
        print <<END;
<h2>マスタパスワードと特殊パスワードを決めてください。</h2>
<p>※入力ミスを防ぐために、それぞれ２回ずつ入力してください。</p><b>マスタパスワード：</b><br>
(1) <input type="password" name="MPASS1" value="$mpass1">&nbsp;&nbsp;(2) <INPUT type="password" name="MPASS2" value="$mpass2"><br>
<br>
<b>特殊パスワード：</b><br>
(1) <INPUT type="password" name="SPASS1" value="$spass1">&nbsp;&nbsp;(2) <INPUT type="password" name="SPASS2" value="$spass2"><br>
<br>
<input type="submit" value="done" name="SETUP">
END
        return;
    }
    $inputPass = $HdefaultPassword if ($inputPass eq '');
    print <<END;
<b>マスタパスワード：</b><input type="password" size="32" maxlength="32" name="PASSWORD" value="$inputPass">
<input type="submit" value="管理人室に入る" name="ADMIN">
END

    opendir(DIN, "./");

    # 現役データ
    if (-d "${HdirName}") {
        dataPrint("");
    } else {
        print <<END;
  <hr>
  <input type="submit" value="新しいデータを作る" name="NEW">
END
    }

    # バックアップデータ
    my ($dn);
    while ($dn = readdir(DIN)) {
        if ($dn =~ /^${HdirName}.bak(.*)/) {
            dataPrint($1);
        }
    }
    closedir(DIN);
}


# ----------------------------------------------------
# 管理人室
sub adminMode {
    print <<END;
<h1>箱庭諸島ＲＡ 管理人室</h1>
<hr>
END
    if ($Hbbs eq "${HbaseDir}/hako-yy-bbs.cgi") {
        print "[<A HREF=\"$Hbbs\" target=\"_blank\">掲示板</A>(<A HREF=\"$Hbbs?id=0&cpass=${inputPass}\" target=\"_blank\">管理モード</A>)] ";
    }
    else {
        print "[<A HREF=\"$Hbbs\" target=\"_blank\">掲示板</A>] ";
    }
    print <<END;
[<a href="$HthisFile?Rekidai=0" target="_blank">歴代最多人口記録</a>] 
[<a href="$HthisFile?Rank=0" target="_blank">ランキング</a>] 
END
    if (!$HhtmlLogMode || !(-e "${HhtmlDir}/hakolog.html") || $Hgzip) {
        print "[<a href=\"${HbaseDir}/history.cgi?Event=0\" target=\"_blank\">最近の出来事</a>] ";
    }
    else {
        print "[<a href=\"${htmlDir}/hakolog.html\" target=\"_blank\">最近の出来事</a>] ";
    }
    print <<END;
<hr>
<h3><span class="attention">※以下の作業は、更新間際に行うと非常に危険です！</span></h3>
END

    print <<END;
<h2><a href="${HlbbsFile}?pass=" target="_blank">観光者通信一覧表</A>(<A HREF="${HlbbsFile}?pass=${inputPass}" target="_blank">管理人モード</A>)</H2>
<ul>
  <li>lbbslist.cgiを設置している場合、全参加者の観光者通信を覗く事ができます。<br>
  <li>このスクリプトは、サーバに負荷がかかると思われる為、頻繁にアクセスしたり、リロードなどの行為はできるだけ控えるようにしましょう。
  <li>管理人モードで入ると、極秘通信を見ることができます。管理人権限だからと言ってあんまり覗いちゃダメよ。<br>注：COOKIEにマスターパスワード喰ってると普通にアクセスしても「管理人モード」になります。
</ul>
END

    print <<END if (USE_EX_LBBS);
<h2><a href="${HlbbsDir}/view.cgi" target="_blank">外部簡易掲示板を閲覧する</A>(<A HREF="${HlbbsDir}/view.cgi?admin=${HviewPass}" target="_blank">管理人モード</A>)</H2>
<ul>
  <li>初期設定(hako-init.cgi)で「外部簡易掲示板を使用する」ようにしていなければ、見ても仕方がありません。
  <li>view.cgiの設定でオーナーチェックをオンにしている場合、「閲覧」では投稿できないようになります。また、「index更新」のボタンを押さなければ、一覧は最新のデータにはなりません。
  <li>管理人モードでアクセスすると、各掲示板の管理人の機能が使えるようになります。（管理人としてのクッキーを食べてしまいますので、操作後の投稿には十分お気をつけ下さい）
</ul>
END

    print <<END;
<h2><a href="JavaScript:void(0)" onClick="document.AXESLOG.target='newWindow';document.AXESLOG.submit();return false;">アクセスログを見る</a></h2>
<form name="AXESLOG" action="${HaxesFile}" method="post">
  <input type="hidden" name="password" value="${inputPass}">
  <input type="hidden" name="mode" value="analyze">
  <input type="hidden" name="category" value="a">
</form>
<ul>
<li>メインスクリプト(hako-main.cgi)の設定で「アクセスログをとる」ようにしていなければ、見ることができません。
<li>ログを残す動作による負荷増はバカになりませんので、箱庭本体の動作にも影響があることを覚悟して下さい。
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
<a href="JavaScript:void(0)" onClick="document.ALLYBBS.target='newWindow';document.ALLYBBS.submit();return false;">同盟掲示板へ</a></H2>
</FORM>
<ul>
<li>「同盟掲示板」を閲覧できます。
<li>投稿すると、名前が「海戦運営本部」になります。
</ul>

<form name="DEADBBS" action="${HmenteFile}" method="POST">
  <input type="hidden" name="PASSWORD" value="${inputPass}">
  <select name=ALLYID>${allyList}</select>
  <input type="hidden" name="ALLYLOG">
  <h2><a href="JavaScript:void(0)" onClick="document.DEADBBS.submit();return false;">同盟掲示板ログを消滅ログへ移行</a></h2>
</form>
<ul>
<li>同盟の削除は上の「陣営(同盟)の作成・設定変更」で可能です。<BR>
「陣営(同盟)の作成・設定変更」の場合は、「発見の記録」に解散ログが表示されて、同盟掲示板のログはそのまま保存されます。<BR>
こちらは、同盟はそのままで、同盟掲示板のログを消滅ログへ移行させます。
<li>消滅ログはhako-yy-bbs.cgiの上部にリンクされます。<BR>
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
					$deadallyList .= "<OPTION VALUE=\"$dally\">$daName($HallyTopName：$diName ターン$dturnに消滅)\n"
				}
				print <<END if(@dead > 0);
<form name="DELBBS" action="${HmenteFile}" method="POST">
  <select name=DEADALLY>${deadallyList}</select>
  <input type="hidden" name="PASSWORD" value="${inputPass}">
  <input type="hidden" value='消滅ログの削除' name="DELLOG">
  <h2><a href="JavaScript:void(0)" onClick="document.DELBBS.submit();return false;">消滅ログの削除</a></H2>
</form>
<ul>
  <li>同盟掲示板の消滅ログを削除します。
</ul>
END
			}
		}
		print <<END;
<h2><a href="${HthisFile}?JoinA=${inputPass}">陣営(同盟)の作成・設定変更</a></h2>
<ul>
  <li>「陣営戦モード」を有効にしている場合は、ここから陣営(同盟)を新規作成してください。
  <li>陣営(同盟)と島を選択して変更ボタンを押すと、陣営(同盟)の参謀(盟主)を任命することができます。
</ul>
END
    }
    else {
        print "掲示板なし";
    }

    print <<END if($HuseAmity || $HallyUse || $HarmisticeTurn);
<h2><a href="${HthisFile}?ASetup=${inputPass}">友好国・同盟(陣営)の所属変更</a></h2>
<ul>
  <li>友好国設定や同盟所属の変更を行います。
</ul>
END

    print <<END;
<h2><a href="${HthisFile}?Pdelete=${inputPass}">参加${AfterName}を管理人あずかりにする</a></h2>
<ul>
  <li>あずかりになった${AfterName}は、ターン処理(収入処理・コマンド処理・成長・災害・失業者移民)されなくなります。
  <li>他の${AfterName}からの攻撃はすべて受けつけてしまいます。
  <li>あずかり中の島が「放棄」もしくは「強制削除」された場合、あずかりのＩＤデータは、次のあずかり処理を行うまでそのまま残ります。
</ul>
END

    print <<END;
<h2><a href="${HthisFile}?Lchange=${inputPass}">参加${AfterName}の地形データを変更する</a></h2>
<ul>
  <li>荒らしの被害や、サーバートラブル、スクリプトのバグなどで、地形データが不本意な状態になってしまった${AfterName}を救済します。
  <li>座標１つずつの処理なので、部分的な救済措置しかできません。全体的な変更は直接データを改変した方が早いでしょう。
  <li>また、人口、農場規模などの数値データへの反映はターン更新処理が行われてからになるので、注意してください。
  <li>「地形」と「地形の値」についての知識がなければ使用は難しいかもしれません。たとえば「海」で値を１にすると「浅瀬」になったり、都市の人口の表示上の数値とデータ上の数値の違い(10000人が100と記録されていたりするので)や、農場や工場の発展規模でとりうる数値が決まっていることなど(hako-make.cgiのsub landCheckで簡易チェックをするようにしています)。
</ul>
END

    print <<END;
<h2><a href="${HthisFile}?Rename=0" target="_blank">参加${AfterName}を強制削除する</A></H2>
<ul>
  <li>「${AfterName}の名前とパスワードの変更」画面で、該当の${AfterName}の名前を「無人」${AfterName}または「沈没」${AfterName}にしてください。
  <li>その際、パスワード欄には「特殊パスワード」を入力しなければなりません。
  <li>「無人」${AfterName}にすると「発見の記録」に、「海神の<B>怒りに触れ</B>陸地はすべて<span class=attention>沈没しました。</span>」というログが残ります。
  <li>「沈没」${AfterName}の場合はログを出しません。
</ul>
END

    print <<END;
<h2><a href="${HthisFile}?Present=">参加${AfterName}にプレゼントを贈る</A></H2>
<ul>
  <li>「発見の記録」にログが残るイベントとして援助を行うことができます。
  <li>表示されたフォームに必要な値やメッセージを入力して、パスワードに「特殊パスワード」を入れ、「プレゼントを贈る」ボタンを押せばプレゼント完了です。
  <li>ログにはHTMLタグも使えますが、間違ったログの削除ができませんので、慎重に入力してください。あらかじめブラウザで表示テストを行っておいたほうがいいでしょう。「発見の記録」に変なログが残ると、ちょっと恥ずかしいです。
  <li>プレゼントの結果として金や食料の保有量が制限値を超えることがあります。次回のターン進行で制限値に切り捨てられますが、そのターンだけは持っているだけ使えます。
例えば保有量が20000になっている場合、このままターン進行すると9999に切り捨てられます。しかし、このターンで掘削を99回行った場合には、費用19800が引かれて200だけが残ります。
</ul>
END

    print <<END;
<h2><a href="${HthisFile}?Punish=${inputPass}">参加${AfterName}に制裁を加える</A></H2>
<ul>
  <li>制裁は指定した自然災害を必ず発生させます。例えば「Ａ${AfterName}に地盤沈下」という指示を出すと次のターンで地盤沈下します。
  <li>巨大隕石と噴火は座標指定が可能で、必ずその座標に発生します。どうしようもないプレイヤーを排除するときに効果的に使えます。
  <li>この改造は、「荒らしというほどではないが箱庭の雰囲気を悪化させるような行為をするプレイヤー」や、「管理人の決めたローカルルールに違反していて改善の見込みがないプレイヤー」など、箱庭の運営上好ましくないと判断されたプレイヤーに自然災害を恣意的に発生させるものです。
  <li>管理人が好ましくないと判断したプレイヤーとは掲示板などで話し合うべきですが、時には、そうした話し合いでは全く埒があかないこともあります。そういう場合、参加${AfterName}の間で「あの${AfterName}を潰そう」という機運が盛り上がったりしますが、後味はかなり悪いです。
  <li>管理人によっては「あの${AfterName}は荒らしと認定しますので攻撃してください」と全${AfterName}攻撃を認めることもあるようですが、なかなかそこまでの対応は難しいものです。強制的に${AfterName}を放棄させる処置はまだ穏便ですが、放棄された${AfterName}のプレイヤーがあとあとまで抗議してくることもあります。
  <li>そういうときに、「実にいい位置に巨大隕石」とか「運悪く地盤沈下」とかがあれば、あまり揉めずに問題${AfterName}は弱体化します。やりすぎると箱庭の雰囲気が悪くなりますので注意が必要です。
</ul>
END

    print <<END;
<h2><a href="${HthisFile}?Bfield=${inputPass}">Battle Fieldを作成する</A></H2>
<ul>
  <li>人口０になっても沈没しない${AfterName}を作成します。いわば「演習${AfterName}」ですが、経験値や難民稼ぎにはなります(平和系向き)。
  <li>あらかじめ「新しい${AfterName}を探す」によって${AfterName}を作成しておかなければなりませんので、最大登録数を越えた状態の場合は一時的にそれを変更して増やしておかなければならないでしょう。面倒ですが、今のところ仕様です。
  <li>荒らしの${AfterName}や重複登録の${AfterName}をBattle Fieldに変更することもできますね。
  <li>また、Battle Fieldにしている${AfterName}を元に戻すこともできますが、${AfterName}の登録数が最大の場合はできません。
  <li><b>Battle Fieldの仕様</b>
  <ul>
    <li>農場がなくても食料不足にはならない。
    <li>荒れ地はかなり高確率で平地になり、平地は森や都市に接していなくても村が発生する。
    <li>怪獣出現確率は通常の２倍で、人口にかかわらず常にレベル２。
    <li>怪獣を倒した時の報奨金は、倒した島のものになる。
  </ul>
</ul>
END

    print <<END;
<form name="BFDEVELOP" action="${HthisFile}" method="POST">
  <input type="hidden" name="PASSWORD" value="${inputPass}">
  <input type="hidden" name="dummy" value="dummy">
  <h2><a href="JavaScript:void(0)" onClick="document.BFDEVELOP.target='newWindow';document.BFDEVELOP.submit();return false;">Battle Fieldの開発画面に入る</a></h2>
</form>
<ul>
  <li>トップページの島リストでBattle Fieldが選べるようになります。
  <li>Battle Fieldを作成していなければ、ごく普通のトップページが表示されるだけです。
</ul>
END

}


# ----------------------------------------------------
# 同盟掲示板ログを消滅ログへ移行
sub allyLogMain {
	# 島データの読みこみ
	if(!readIslandsFile()) {
		print "データ読み込みエラー発生！<HR>";
		return;
	}
	my $an = $HidToAllyNumber{$HallyID};
	if(defined $an) {
		my $n = $HidToNumber{$HallyID};
		my $name = $Hislands[$n]->{'name'} . $AfterName;
		$name = "${HallyTopName}不在" if !(defined $n);
		if($dellcheck) {
			if(make_pastlog($HallyID, $name)) {
				print "移行成功！　<a href='${HbaseDir}/hako-yy-bbs.cgi'>掲示板へ</a><HR>";
			} else {
				print "掲示板ログがみつからない。または、移行失敗！<HR>";
			}
		} else {
			my $allyName = $Hally[$an]->{'name'};
			print <<END;
<H2>$allyNameの同盟掲示板ログを消滅ログへ移行しますか？</H2>
<H2><FORM name="DEADBBS" action="${HmenteFile}" method=POST>
<INPUT type=hidden name=DELLOK value="1">
<INPUT type=hidden name=PASSWORD value="${inputPass}">
<INPUT type=hidden name=ALLYID value="${HallyID}">
<INPUT type=hidden name=ALLYLOG>
<a href="JavaScript:void(0)" onClick="document.DEADBBS.submit();return false;">はい</a>　<a href="${HmenteFile}?ADMIN=${inputPass}">いいえ</a></H2>
END
		}
		return;
	} else {
		print "同盟がみつかりません！<HR>";
		$dellcheck = 1;
	}
	return;
}


# ----------------------------------------------------
# 消滅ログ削除
sub dellogMode {
	if($dellcheck) {
		my $logfile = "${HlogdirName}/${deadally}$Hlogfile_name";
		unlink($logfile) if (-f $logfile);
		# 盟主ログファイル
		my $logfile2 = "${HlogdirName}/${deadally}$Hlogfile2_name";
		unlink($logfile2) if (-f $logfile2);
		# カウンタファイル
		if($Hcounter) {
			my $cntfile = "${HlogdirName}/${deadally}$Hcntfile_name";
			unlink($cntfile) if (-f $cntfile);
		}
		# 過去ログ用NOファイル
		if($Hpastkey) {
			my $nofile  = "${HlogdirName}/${deadally}$Hnofile_name";
			my $count;
			if (-f $nofile) {
				# 過去NOを開く
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
			$deadallyList = "$daName($HallyTopName：$diName ターン$dturnに消滅)\n";
			last if($dally eq $deadally);
			$deadallyList = '';
		}
		if($deadallyList eq '') {
			$dellcheck = 1;
			return;
		}
		
		print <<END if(@dead > 0);
<H2>$deadallyListの消滅ログを削除しますか？</H2>
<H2><FORM name="DELBBS" action="${HmenteFile}" method=POST>
<INPUT type=hidden name=DELLOK value="1">
<INPUT type=hidden name=DEADALLY value="${deadally}">
<INPUT type=hidden name=PASSWORD value="${inputPass}">
<INPUT type=hidden value='消滅ログの削除' name="DELLOG">
<a href="JavaScript:void(0)" onClick="document.DELBBS.submit();return false;">はい</a>　<a href="${HmenteFile}?ADMIN=${inputPass}">いいえ</a></H2>
END
	}
	return;
}


# ----------------------------------------------------
# 表示モード
sub dataPrint {
	my($suf) = @_;

	print "<HR>";
	if($suf eq "") {
		open(IN, "${HdirName}/$HmainData");
		print "<H1>現役データ</H1>";
	} else {
		open(IN, "${HdirName}.bak$suf/$HmainData");
		print "<H1>バックアップ$suf</H1>";
	}

	my($lastTurn);
	$lastTurn = <IN>;
	my($lastTime);
	$lastTime = <IN>;

	my($timeString) = timeToString($lastTime);

	print <<END;
	<B>ターン$lastTurn</B><BR>
	<B>最終更新時間</B>:$timeString<BR>
	<B>最終更新時間(秒数表示)</B>:1970年1月1日から$lastTime 秒<BR>
	<INPUT TYPE="submit" VALUE="このデータを削除" NAME="DELETE$suf">
END

    if ($suf eq "") {
        my($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) = gmtime($lastTime + $Hjst);
        $mon++;
        $year += 1900;

        print <<END;
    <h2>最終更新時間の変更</h2>
    <input type="text" SIZE=4 NAME="YEAR" value="$year">年
    <input type="text" SIZE=2 NAME="MON" value="$mon">月
    <input type="text" SIZE=2 NAME="DATE" value="$date">日
    <input type="text" SIZE=2 NAME="HOUR" value="$hour">時
    <input type="text" SIZE=2 NAME="MIN" value="$min">分
    <input type="text" SIZE=2 NAME="NSEC" value="$sec">秒
    <input type="submit" VALUE="変更" NAME="NTIME"><BR>
    1970年1月1日から<INPUT TYPE="text" SIZE=32 NAME="SSEC" VALUE="$lastTime">秒
    <INPUT TYPE="submit" VALUE="秒指定で変更" NAME="STIME">

END
    } else {
        print <<END;
    <input type="submit" value="このデータを現役に" name="CURRENT$suf">
END
    }
}

# ----------------------------------------------------
sub timeToString {
    my ($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) = gmtime($_[0] + $Hjst);
    $mon++;
    $year += 1900;

    return "${year}年 ${mon}月 ${date}日 ${hour}時 ${min}分 ${sec}秒";
}

# ----------------------------------------------------
# CGIの読みこみ
sub cgiInput {
	my($line);

	# 入力を受け取る
	$line = <>;
	$line =~ tr/+/ /;
	$line =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

	# GETのやつも受け取る
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
# ファイルのコピー
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
# パスチェック
sub passCheck {
	if(checkMasterPassword($inputPass)) {
		return 1;
	} else {
		tempWrongPassword(); # パスワード違い
		print "</BODY></HTML>";
		exit(0);
	}
}

# Time::Local の互換関数
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
#cookie入力
sub cookieInput {
    my($cookie);
#   $cookie = jcode::euc($ENV{'HTTP_COOKIE'}); # jcode使用時
    $cookie = $ENV{'HTTP_COOKIE'};
    if ($cookie =~ /${HthisFile}OWNISLANDPASSWORD=\(([^\)]*)\)/) {
        $HdefaultPassword = $1;
    }
}

# ----------------------------------------------------
#cookie出力
sub cookieOutput {
    my ($cookie, $info);

    # 消える期限の設定
    my ($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) =
        gmtime(time + 14 * 86400); # 現在 + 14日

    # 2ケタ化
    $year += 1900;
    $date = "0$date" if ($date < 10);
    $hour = "0$hour" if ($hour < 10);
    $min  = "0$min" if ($min < 10);
    $sec  = "0$sec" if ($sec < 10);

    # 曜日を文字に
    $day = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")[$day];

    # 月を文字に
    $mon = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")[$mon];

    # パスと期限のセット
    $info = "; expires=$day, $date\-$mon\-$year $hour:$min:$sec GMT\n";
    $cookie = '';
    
    if($inputPass) {
        $cookie .= "Set-Cookie: ${HthisFile}OWNISLANDID=(0) $info";
        $cookie .= "Set-Cookie: ${HthisFile}OWNISLANDPASSWORD=($inputPass) $info";
    }
    out($cookie);
}

1;
