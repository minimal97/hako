#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# 初期設定用スクリプト(ver1.02)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Hakoniwa R.A. ver1.11
# 初期設定用スクリプト(箱庭諸島 ver2.30)
# 使用条件、使用方法等は、read-renas.txtファイルを参照
#
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------

# jcode.plをrequire
require './jcode.pl';
require './init-server.cgi';

#----------------------------------------------------------------------
# 各種設定値
# (これ以降の部分の各設定値を、適切な値に変更してください)
#----------------------------------------------------------------------

# デバッグモード(1だと、「ターンを進める」ボタンが使用できる)
our $Hdebug = 1;

# メインスクリプト
our $HthisFile = "${HbaseDir}/hako-main.cgi";

# 箱庭メンテナンス・スクリプト
our $HmenteFile = "${HbaseDir}/hako-mente.cgi";

# アクセス解析スクリプト
our $HaxesFile = "${HbaseDir}/analyzer.cgi";

# ゲームのタイトル文字
our $HtitleTag = '箱庭'; # ウィンドウのタイトル
our $Htitle    = '箱庭'; # トップ画面のタイトル

# 観光者通信一覧表（管理用）
our $HlbbsFile = "${HbaseDir}/lbbslist.cgi";
our $jumpTug = "<meta HTTP-EQUIV='refresh' CONTENT='0; URL=\"${HlbbsFile}\"'></body></html>\n\n";
#$jumpTug = "Location: $HlbbsFile\n\n";

# ヘッダのリンク(利用規約により、箱庭諸島スクリプト配布元へのリンクは消してはいけません)
our $Hheader =<<"_H_E_A_D_E_R_";
<div class="HeadFootLink">
<small>[<A TITLE="現在は配布していません" HREF="http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html" target="_blank">箱庭諸島スクリプト配布元</A>]
<span class='Nret'>[<A HREF="$Htoppage">トップページ</A>]</span>
<span class='Nret'>[<A HREF="../frm/">miniverse</A>]</span>
<span class='Nret'>[<A TITLE="ソースコードを公開していただけました" HREF="http://uhyohyohyo.sakura.ne.jp/" target="_blank">多趣旨の国</A>]</span>
<span class='Nret'>[<A TITLE="使うかもしれん" HREF="http://www.propel.ne.jp/~yysky/gallery/" target="_blank">箱庭諸島の素材屋さん</A>]</span>
</small>
</div>
_H_E_A_D_E_R_

# フッタのリンク
our $Hfooter =<<"_F_O_O_T_E_R_";
管理者:$HadminName
_F_O_O_T_E_R_

# 新しい島を探せるのは管理人だけ？
# （管理人だけの場合は $HjoinGiveupTurn を小さくしてください）
our $HadminJoinOnly = 0;

# ヘッダのコメント(負荷を考えると直接hako-top.cgiをいじった方が吉)
# lbbslist.cgiでコメントアウトしている「&tempNews if($mode);」と連動し、lbbslist.cgiでnews.cgiを書き換えることが可能。
#if(-e "./news.cgi") {
#	open(NEWS, "./news.cgi");
#	my @news = <NEWS>;
#	close(NEWS);
#	$Hnews = join(/\n/, @news);
#	chomp($Hnews);
#}
#$Hheader .= $Hnews;
#----------------------------------------
# ゲームの進行やファイルなど
#----------------------------------------
# 1ターンが何秒か
our $HunitTime = 7200; # 3時間

# ターン更新間隔を細かく設定するか？(0:しない、1:する)
our $HflexTimeSet = 0;
use constant INIT_FLEX_TIME_SET    => 0;
# する場合は、ターン更新間隔(時間単位で設定してください)をコンマ区切りで設定してください。
# ０ターンから１ターンへの更新間隔が@HflexTimeの最初の数値(時間)になります。
# xターンからx+1ターンまでの更新間隔 は (xを設定した個数で割ったあまり+1)番目の数値
# ※プレイヤーが混乱しないようきちんと告知してあげてください。
our @HflexTime = (3, 3, 3, 3, 9, 3);

# 島の最大数(最大で100)
our $HmaxIsland = 40;

# 島の大きさ(変更できないかも)
our $HislandSize = 20;

# 新しい島を探せるのは管理人だけ？(0:しない、1:する)
# （管理人だけの場合は $HjoinGiveupTurn を小さくしてください）
our $HadminJoinOnly = 0;

# コマンド入力限界数
# (ゲームが始まってから変更すると、データファイルの互換性が無くなります。)
our $HcommandMax = 40;

# ローカル掲示板行数を使用するかどうか(0:使用しない、1:使用する)
our $HuseLbbs = 1;

# ローカル掲示板行数
our $HlbbsMax = 20;

# 外部簡易掲示板を使用するか(0:使用しない、1:使用する)
our $HuseExlbbs = 0;
# 使用する場合、以下を設定
# 外部簡易掲示板のアドレス(lbbs.cgi,view.cgiの置いてあるディリクトリ)
# 最後にスラッシュ(/)は付けない。
our $HlbbsDir = "${HbaseDir}/lbbs";
# view.cgiのマスターパスワード
our $HviewPass = '0123';
# 注！外部簡易掲示板は別途用意する必要があります。

# 名前の後ろにつくヤツ（初めは”島”）
our $AfterName = '島';

# gzipを使用して圧縮伝送する？ 0 : 未使用  1 : 使用
our $Hgzip = 0;

# gzipのインストール先
our $HpathGzip = '/usr/bin';

# ログファイル保持ターン数
our $HlogMax = 20; 

#「最近の出来事」に表示するログのターン数（ログファイル保持ターン数より大きくできません）
our $HtopLogTurn = 20;

#「最近の出来事」をHTML化するか(0:しない、1:する)
our $HhtmlLogMake = 0;

# HTML化する場合は、以下を設定
# HTMLファイル(hakolog.html)を置くディレクトリ
# my($htmlDir) = 'http://サーバー/ディレクトリ';
# 最後にスラッシュ(/)は付けない。
our $htmlDir = "${HbaseDir}";
# $HbaseDirから$htmlDirへの相対パス。最後にスラッシュ(/)は付けない。
our $HhtmlDir = '.';
# HTMLページに表示するログのターン数（ログファイル保持ターン数より大きくできません）
our $HhtmlLogTurn = 8;
#「最近のできごと」をHTMLで表示するか(0:しない、1:する)
#「最近のできごと」をHTML化しない場合は0にして下さい。
our $HhtmlLogMode = 0;

# 各島の「近況」をhistory.cgiで表示するか？(0:しない、1:する)
our $HuseHistory1 = 1; # 自島(開発画面)
our $HuseHistory2 = 1; # 他島(観光画面など)

# 季節を導入しますか?(0:しない、1:する)
# 設定する場合は、hako-main.cgiの災害のところで月ごとの発生率も設定されます。
our $Hseason = 0;

# 暦名(西暦とか平成とかいうやつです。いらなければ""にしておいてね)
our $Halmanac = "${HadminName}歴";

# 季節ごとに画像を変更するか?(0:しない、1:する)
our $HseaonImgSet = 0;
use constant SEASON_IMAGE_SET    => 0;
# する場合は、画像フォルダの中に季節ごとのフォルダを用意してください。
# フォルダの名前を以下で設定します。月ごとに画像を変更することも可能です。
# ※一部だけの変更でも、季節フォルダそれぞれに、すべての画像をいれる必要があります。
#   ローカル設定も１つのフォルダ(たとえば'img')の中に季節のフォルダを作っておいて、
#   'img'の中にはland0.gifひとつだけ入れておいて、それで設定すればうまくいきます。
# 0:季節なし    0, 1月, 2月, 3月, 4月, 5月, 6月, 7月, 8月, 9月,10月,11月,12月
our @HseasonImg = ('','','','','','','','','','','','','');

# 負荷計測するか？(0:しない、1:する)
our $Hperformance = 1;
use constant USE_PERFORMANCE    => 1;

# オーナー・パスワードの暗号化(0:しない 1:する)
our $cryptOn = 1;

#----------------------------------------
# 同盟
#----------------------------------------
# 同盟作成を許可するか？(0:しない、1:する、2:管理者のみ)
our $HallyUse = 1;
use constant ALLY_USE    => 1;

# ひとつの同盟にしか加盟できないようにするか？(0:しない、1:する)
our $HallyJoinOne = 1;
use constant ALLY_JOIN_ONE    => 1;

# 加盟・脱退をコマンドで行うようにする？(0:しない、1:する)
our $HallyJoinComUse = 0;

# 同盟に加盟することで通常災害発生確率が減少？(0:しない)
# 対象となる災害：地震、津波、台風、隕石、巨大隕石、噴火
our $HallyDisDown = 0; # 設定する場合、通常時に対する倍率を設定。(例)0.5なら半減。2なら倍増(^^;;;

# 同盟データの名前
our $HallyData = 'adata.cgi';

# 同盟データの名前
our $HallychatDataName = "chatlog";
our $HallychatData = "${HdirName}/${HallychatDataName}";

# 同盟掲示板としてＢＢＳを使用する 1:する 0:しない
our $HallyBbs = 0;
# ＢＢＳのスクリプト名
our $HallyBbsScript = "hako-yy-bbs.cgi"; # YY-BOARD ver5.03 by KENT
# ログ保存用ディリクトリの名前
our $HlogdirName  = 'log';
# ログファイル名：必ず変更。拡張子は「.cgi」に
our $Hlogfile_name = 'allybbs.cgi';   # 通常ログ用
our $Hlogfile2_name = 'stuffcom.cgi'; # 重要投稿用
# ミニカウンタの設置 (0:no 1:テキスト 2:GIF画像)
our $Hcounter = 1;
# カウンタファイル名
our $Hcntfile_name = 'count.cgi';
# 過去ログ生成 (0=no 1=yes)
our $Hpastkey = 1;
# 過去ログ用NOファイル名
our $Hnofile_name  = 'pastno.cgi';
# 過去ログのディレクトリ
our $HpastdirName = 'past';
# YY-BOARDの詳細設定はhako-yy-ini.cgiで行って下さい。

our $HcostMakeAlly = 1000; # 同盟の結成・変更にかかる費用
our $HcostKeepAlly =  100; # 同盟の維持費(加盟している島で均等に負担)

# 同盟のマーク
our @HallyMark = (
	'Б','Г','Д','Ж','Й',
	'Ф','Ц','Ш','Э','Ю',
	'Я','б','Θ','Σ','Ψ',
	'Ω','ゑ','ゐ','¶','‡',
	'†','♪','♭','♯','‰',
	'Å','∽','∇','∂','∀',
	'⇔','∨','〒','£','¢',
	'＠','★','♂','♀','＄',
	'￥','℃','仝','〆',
);

# 重要投稿メッセージ欄のタイトル「〜からのメッセージ」「〜モード」
our $HallyTopName = '盟主'; # 陣営戦モードの時などは「参謀」にできます。

# 同盟(陣営)外への援助 1:不許可 0:許可
our $HcampAidOnly = 0;

# 同盟への攻撃 1:不許可 0:許可
our $HcampAtk = 0;

# ローカル掲示板行数
our $HAllylbbsMax = 100;

#----------------------------------------------------------------------
# 陣営戦モード(調整中)
#----------------------------------------------------------------------
# 停戦期間
our $HarmisticeTurn = 1; # 0にすれぱオフになります

# 停戦期間中のターン更新間隔
our $HarmisticeTime = 21600; # 3時間

# 勝利条件
our $HfinishOccupation = 70; # 占有率がこの値以上になったら終了

# 陣営預かりに移行するターン数
our $HpreGiveupTurn = 100;

# 陣営の選択の方法
# 0: 島数が最も少なく、順位が最下位の陣営
# 1: ランダム("合計の島数/陣営の数"を超えない)
# 2: 選択可能("合計の島数/陣営の数"を超えない)
our $HcampSelectRule = 0;

# 陣営の消滅
our $HcampDeleteRule = 0; # 1:陣営消滅ルールあり、0:なし

# 陣営作戦本部コマンド表示数
our $HcampCommandTurnNumber = 5;

# 初期資金
our $HinitialMoney2 = 3000; # ゲーム開始後の登録

# 初期食料
our $HinitialFood2 = 3000; # ゲーム開始後の登録

#----------------------------------------------------------------------
# サバイバルモード(規定ターンごとに最下位の島が沈没します)
#----------------------------------------------------------------------
# サバイバルモードに入るターン(設定数値の次のターンから有効)
our $HsurvivalTurn = 0; # 0にすればオフになります

# 何ターンごとに最下位の島が滅ぶか(戦闘期間のみ)
our $HturnDead = 10;

#----------------------------------------
# アクセスログ関連設定
#----------------------------------------
# COOKIEによるIDチェックをするか？(0:しない、1:する)
# 「する」にすると、同一ＰＣで複数の島を管理する時、COOKIEを削除しなければ別の島の開発画面に入れなくなります。
# 簡易重複対策なわけですが、島ごとにブラウザを変えることですぐにやぶられちゃいます(/_<。)
our $checkID = 0;

# COOKIEによる「画像のローカル設定」もチェックする？(0:しない、1:する)
our $checkImg = 0;  #画像のローカル設定

# COOKIEチェック（上の２つの設定）を免除する島のID
# 例：@freepass = (2, 7, 12);
our @freepass = ();

# パスワード・エラーの画面に警告文を表示するか？(0:しない、1:する)
our $HpassError = 0;

# アクセスログをとるか？(0:とらない、1:開発画面に入る時、2:トップページ)
our $HtopAxes = 1;
# 1or2にした場合、以下を設定
# ログファイル名
our $HaxesLogfile = './axes.log';
# 最大記録件数
our $HaxesMax = 1000;
# ホスト取得方法(0:gethostbyaddr関数を使わない、1:gethostbyaddr関数を使う)
our $gethostbyaddr = 0;

#----------------------------------------------------------------------
# 特別な定数
# (ゲーム中に値を変更してはいけません。データが壊れます)
#----------------------------------------------------------------------
# ターン分割更新（一度に更新する島の数）
# ！この設定は危険ですので、0:未設定のままにしておいてください。
# 　設定変更によってデータの破損が起こったり、サーバー管理者とトラブルが生じる可能性があります。
our $HsepTurn = 0; # 0:未設定・・・未設定のまま、変更しないでくださいm(_ _)m
our $Hrefresh = 3; # リフレッシュ時間(秒)

# 座標の最大値
our $islandSize = $HislandSize - 1;

1;
