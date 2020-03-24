#----------------------------------------------------------------------
# 箱庭諸島 Hakoniwa R.A. JS ver4.xx
# サーバー設定モジュール(ver1.00)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# うらにわ -uRAniwa-: http://snow.prohosting.com/awinokah/
#----------------------------------------------------------------------

require './server_config.pm';
#----------------------------------------
# サーバー
#----------------------------------------
# このファイルを置くディレクトリ(最後にスラッシュ(/)は付けない。)
$HbaseDir = $server_config::HbaseDir;

# 画像ファイルを置くディレクトリ(最後にスラッシュ(/)は付けない。)
$HimageDir = "$server_config::HbaseDir";

# 画像ファイル　こっちは 最後にスラッシュ必要
$HStatImgDir = "$server_config::HbaseDir/img/";

# 画像ファイル　こっちは 最後にスラッシュ必要
$HSatelliteImgDir = "$server_config::HbaseDir/img/satellite/";

# 画像ファイル　こっちは 最後にスラッシュ必要
$HMapImgDir = './img/land/';

# 箱庭スキンの設定へのリンクをトップページに表示するか
# $HcssSetting = 0;
# use constant SERVER_CSS_SETTING    => 0;

# 設定用CSSフォルダ
$HcssDir = 'css'; # フォルダ名のみ(データフォルダと同様の扱いになります)
# 注！「外部ファイル(css,js)を置くディレクトリ」の中に作っておいて下さい。


# 外部ファイル(css,js)を置くディレクトリ
$efileDir = "${HbaseDir}/${HcssDir}";

# $HbaseDirから$efileDirへの相対パス(『ローカル設定』できるようにしたい場合は、このままでいいでしょう)
$HefileDir = '.';

# CSSファイルの名前
our $HcssFile = 'style.css?v=1.2.6';

# パスワードファイル名
# マスタパスワードと特殊パスワードは暗号化されてパスワードファイルに記憶されています。
$HpasswordFile = 'passwd.cgi';

# GMT に対する JST の時差（サーバの時刻が狂っている時だけ調整してください）
$Hjst = 32400; # 9時間

# 管理者名 バトルフィールドの名前など
$HadminName = '管理者の名前';

# 管理者のメールアドレス
# $Hemail = '管理者@どこか.どこか.どこか';

# 掲示板アドレス
#$Hbbs = 'http://サーバー/掲示板.cgi';
# 通常の掲示板もYY-BOARDを利用する場合
$Hbbs = "${HbaseDir}/hako-yy-bbs.cgi";

# ホームページのアドレス
$Htoppage = 'http://www.geocities.jp/minimal97/index.html';

# 「詳しい変更点」のページ
# $helpHenko = "${HbaseDir}/henko_new.html";

#----------------------------------------
# データ
#----------------------------------------
# ディレクトリのパーミッション
# 通常は0755でよいが、0777、0705、0704等でないとできないサーバーもあるらしい
$HdirMode = 0777;

# データディレクトリの名前
# ここで設定した名前のディレクトリ以下にデータが格納されます。
# デフォルトでは'data'となっていますが、セキュリティのため
# なるべく違う名前に変更してください。
$HdirName = 'data';

# メインデータの名前
$HmainData = 'hakojima.dat';

# 島データの名前(この前に'島ID'がつきます)
$HsubData = 'island.cgi';
#！注：ver4.48以前からの移行のため、下にそれまでの'島データの名前'を入れて下さい。
$HsubDataold = 'island';

# データの書き込み方

# ロックの方式
# 1 ディレクトリ
# 2 システムコール(可能ならば最も望ましい)
# 3 シンボリックリンク
# 4 通常ファイル(あまりお勧めでない)
# $HlockMode = 1;
# use constant SERVER_LOCK_MODE    => 1;

# (注)
# 4を選択する場合には、'key-free'という、パーミション666の空のファイルを、
# このファイルと同位置に置いて下さい。

# 以下の３項目の設定について

# 新規ゲームなら 1 がお勧めです。
# オリジナル(010713モデル)から移行する場合は、
# オーナーデータとミサイル発射可能数データを0にし、怪獣出現データはオリジナルの設定にあわせてください。
# また、バージョンアップの際の設定は、以前のものと同じ設定にしてください。

# オーナーデータをどこに保存するか (0: howner.dat  1: $HmainData)
# $HnewGameO = 1;

# 怪獣出現データをどこに保存するか (0: monslive.dat  1: $HmainData)
$HnewGame = 1;

# ミサイル発射可能数データをどこに保存するか (0: missiles.dat  1: $HmainData)
$HnewGameM = 1;

1;
