#----------------------------------------------------------------------
# 箱庭諸島 RA JS ver4.xx
# ゲーム設定モジュール(ver1.00)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# うらにわ -uRAniwa-: http://snow.prohosting.com/awinokah/
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# 各種設定値
# (これ以降の部分の各設定値を、適切な値に変更してください)
#----------------------------------------------------------------------
#----------------------------------------
# ゲームの進行やファイルなど
#----------------------------------------
# ゲーム終了ターン数
# 0 にすれば自動終了しません
$HgameLimitTurn = 0;
use constant INIT_GAME_LIMIT_TURN   => 0;

# リアルタイマーの使用(0:使用しない、1:使用する)
#$Hrealtimer = 1;
use constant INIT_REAL_TIMER    => 1;

# トップページに表示する島の数
# （これより増えると複数ページに分けられます）
our $HviewIslandCount = 50;
use constant INIT_VIEW_ISLAND_COUNT => 50;

# バックアップを何ターンおきに取るか
$HbackupTurn = 1;

# バックアップを何回分残すか
$HbackupTimes = 12;

# 発見ログ保持行数(10より大きくすると表示が崩れます。下の数値で調整して下さい)
$HhistoryMax = 6;
use constant INIT_HISTORY_MAX => 6;

# 記事表示部の最大の高さ。
# heightの指定値を超えるとスクロールバーが表示されます。
$HdivHeight = 150; # <DIV style="overflow:auto; height:${HdivHeight}px;">

# Hakoniwa Cupログ記事表示部の最大の高さ。
# heightの指定値を超えるとスクロールバーが表示されます。
$HdivHeight2 = 150; # <DIV style="overflow:auto; height:${HdivHeight2}px;">

# 放棄コマンド自動入力ターン数
$HgiveupTurn = 72;

# 攻撃系、援助系、怪獣出現から島が守られる基準人口
# （この人口を超えるまで開発しかできない）
$HguardPop = 500; # ５万人

# ローカル掲示板への匿名発言を許可するか(0:禁止、1:許可)
$HlbbsAnon = 0;
use constant INIT_LBBS_ANONYMOUS => 0;

# ローカル掲示板の発言に発言者の名前を表示するか(0:表示しない、1:表示する)
$HlbbsSpeaker = 1;
use constant INIT_LBBS_SPEAKER    => 1;

# ローカル掲示板のログを移行するか(0:移行しない、1:移行する)
# (稼働中の掲示板ログを極秘発言対応に移行することができます)
$HlbbsOldToNew = 1;
use constant INIT_LBBS_OLD_TO_NEW    => 1;

# 他島のローカル掲示板に発言するための費用(0:無料 1:有料)
$HlbbsMoneyPublic =   0; # 公開
$HlbbsMoneySecret = 100; # 極秘

# 射程内に怪獣・腐海がなければ、ミサイルを発射中止にするか？(0:しない、1:する)
$HtargetMonster = 0;

# STミサイルを使うか？(0:禁止)
$HuseMissileST = 1;

# 怪獣派遣を使うか？(0:禁止)
$HuseSendMonster = 1;
use constant INIT_USE_SEND_MONSTER    => 1;

# 記念碑発射を使うか？(0:禁止)
$HuseBigMissile = 0;
use constant INIT_BIG_MISSILE    => 0;

# バトルフィールドを攻撃できるミサイルの種類
@HkindBFM = (31); # 許可するミサイル発射コマンドの数値
# 全てOKの場合 普  PP  SPP  ST  核  隆  壊
@HkindBFM = (31, 32,  36, 33, 37, 38, 34);

# 他人から資金を見えなくするか(0:見えない 1:見える 2:100の位で四捨五入 3:1000の位で四捨五入)
$HhideMoneyMode = 1;
use constant INIT_HIDE_MONEY_MODE    => 1;

# 他人からミサイル発射可能数を見えなくするか(0:見えない 1:見える 2:10の位で四捨五入)
# $HhideMissileMode = 0;
use constant INIT_HIDE_MISSILE_MODE    => 0;

# 軍事物資がなければミサイル発射できない設定を使うか(0:使わない 1:使う)
$HuseArmSupply = 0;
use constant INIT_USE_ARM_SUPPLY    => 0;

# 軍事物資調達をターン消費なしにするか(0:しない 1:する)
# $HnoturnArmSupply = 0;

# 複数のミサイル発射コマンドを一括実行できるようにするか(0:できない 1:できる)
$HanyMissileMode = 1;

# 油田、遊園地、漁船系の収入(収穫)ログを１本化するか？(0:しない 1:する(維持食料を差し引く) 2:する(維持食料を引かない))
$HlogOmit1 = 1;

# 女神像ログを１本化するか？(0:しない 1:する)
use constant STATUE_LOG_OMIT    => 1;

# 整地ログを１本化するか？(0:しない 1:座標あり 2:座標なし)
$HlogOmit2 = 1;

# 新規作成時に、大学・港町・ニュータウン１つずつと人工衛星１つを最初からもっているか (0: いいえ  1: はい)
$HeasyMode = 0;

# JavaScriptの一部を外部ファイル化するか？(0:しない 1:する)
# $HextraJs = 0;
use constant EXTRA_JS    => 0;

#----------------------------------------
# 資金、食料などの設定値と単位
#----------------------------------------
# 初期資金
$HinitialMoney = 2000;

# 初期食料
$HinitialFood = 200;

# 最大資金
$HmaximumMoney = 9999999;

# 最大食料
$HmaximumFood  = 999999;
use constant INIT_MAXIMUM_FOOD    => 999999;

# お金の単位
$HunitMoney = '億円';

# 食料の単位
$HunitFood = '00トン';

# 人口の単位
$HunitPop = '00人';

# 広さの単位
$HunitArea = '00万坪';

# 木の数の単位
$HunitTree = '00本';

# 木の単位当たりの売値
$HtreeValue = 5;

# 名前変更のコスト
$HcostChangeName = 500;

# 人口1単位あたりの食料消費量
$HeatenFood = 0.2;

# ミサイルの数の単位
$HunitMissile = '発';

# 怪獣の数の単位
$HunitMonster = '匹';
#----------------------------------------
# 基地の経験値
#----------------------------------------
# 経験値の最大値
$HmaxExpPoint = 200; # ただし、最大でも255まで

# レベルの最大値
$maxBaseLevel  = 5; # ミサイル基地
$maxSBaseLevel = 4; # 海底基地

# 経験値がいくつでレベルアップか
@baseLevelUp  = (20, 60, 120, 200);	# ミサイル基地
@sBaseLevelUp = (50, 100, 200);		# 海底基地

#----------------------------------------
# 島主の家のランク
#----------------------------------------
our @HouseLevel;
$HouseLevel[1] = 15000; # 簡易住宅
$HouseLevel[2] = 20000; # 住宅
$HouseLevel[3] = 25000; # 高級住宅
$HouseLevel[4] = 30000; # 豪邸
$HouseLevel[5] = 35000; # 大豪邸
$HouseLevel[6] = 40000; # 高級豪邸
$HouseLevel[7] = 45000; # 城
$HouseLevel[8] = 50000; # 巨城
$HouseLevel[9] = 55000; # 黄金城

#----------------------------------------
# 防衛施設の自爆
#----------------------------------------
# 怪獣に踏まれた時自爆するなら1、しないなら0
$HdBaseAuto = 0;

# 自島が撃ったミサイルは防衛されないようにするなら1、しないなら0
$HdBaseSelfNoDefence	= 1; # 防衛施設
$HdProcitySelfNoDefence	= 1; # 防衛都市

# 防衛施設が100%の防衛をしないようにするなら1、しないなら0
$HdBaseNoPerfect	=  1; # 防衛施設
$HdProcityNoPerfect	=  0; # 防衛都市
$HdNoPerfectP		= 30; # 防衛に失敗する確率(10%)

# 防衛施設直撃のミサイルも防衛するなら1、しないなら0
$HdBaseSelfDefence = 0; # 防衛施設 & 防衛都市


#----------------------------------------------------------------------
# その他拡張用の設定(基本的には，変更不可)
#----------------------------------------------------------------------
# ext[0] 陣営id (未使用)
# ext[1] 功績point
# ext[2] 破壊した防衛施設の数
# ext[3] 破壊したミサイル基地の数
# ext[4] 救出した難民の合計人口
# ext[5] 受けたミサイル数
# ext[6] 発射したミサイル数
# ext[7] 防衛施設で弾いたミサイル数
#----------------------------------------
# 入力文字数の制限(全角文字数で指定)
#----------------------------------------
# 文字制限をオーバーした時、処理を中断するか？(0:しない 1:する)
$HlengthAlert = 0;

$HlengthIslandName  = 15;   # 島の名前
$HlengthOwnerName   = 15;   # 島の所有者の名前
$HlengthMessage     = 40;   # トップページに表示される各島のコメント
$HlengthLbbsName    = 15;   # 「観光掲示板」の投稿者名
$HlengthLbbsMessage = 40;   # 「観光掲示板」の投稿
$HlengthYoso        = 30;   # 予想欄
$HlengthShuto       = 15;   # 首都名
$HlengthTeam        = 15;   # 首都名
$HlengthAllyName    = 15;   # 同盟の名前
$HlengthAllyComment = 40;   # 「各同盟の状況」欄に表示される盟主のコメント
$HlengthAllyTitle   = 30;   # 「同盟の情報」欄の上に表示される盟主メッセージのタイトル
$HlengthAllyMessage = 1500; # 「同盟の情報」欄の上に表示される盟主メッセージ
$HlengthPresentLog  = 100;  # 管理人によるプレゼントモードのメッセージ
#----------------------------------------
# 外見関係
#----------------------------------------
# タグ
# タイトル文字
$HtagTitle_ = '<h1 class="title">';
$H_tagTitle = '</h1>';

# 大きい文字
$HtagBig_ = '<span class="big">';
$H_tagBig = '</span>';

# 島の名前など
$HtagName_ = '<span class="islName">';
$H_tagName = '</span>';

# 薄くなった島の名前
$HtagName2_ = '<span class="islName2">';
$H_tagName2 = '</span>';

# 順位の番号など
$HtagNumber_ = '<span class="number">';
$H_tagNumber = '</span>';

# 順位表における見だし
$HtagTH_ = '<span class="head">';
$H_tagTH = '</span>';

# toto表における見だし
$HtagtTH_ = '<span class="headToTo">';
$H_tagtTH = '</span>';

# 開発計画の名前
$HtagComName_ = '<span class="command">';
$H_tagComName = '</span>';

# 災害
$HtagDisaster_ = '<span class="disaster">';
$H_tagDisaster = '</span>';

# ローカル掲示板、観光者の書いた文字
$HtagLbbsSS_ = '<span class="lbbsSS">';
$H_tagLbbsSS = '</span>';

# ローカル掲示板、島主の書いた文字
$HtagLbbsOW_ = '<span class="lbbsOW">';
$H_tagLbbsOW = '</span>';

# お金
$HtagMoney_ = '<span class="money">';
$H_tagMoney = '</span>';

# 食料
$HtagFood_ = '<span class="food">';
$H_tagFood = '</span>';

# 箱庭カップ勝利
$HtagWin_ = '<span class="HCwin">';
$H_tagWin = '</span>';

# 箱庭カップ敗北
$HtagLose_ = '<span class="HClose">';
$H_tagLose = '</span>';

# 通常の文字色
$HnormalColor_ = '<span class="normal">';
$H_normalColor = '</span>';

# 順位表、セルの属性
$HbgTitleCell   = 'class=TitleCell';   # 順位表見出し
$HbgNumberCell  = 'class=NumberCell';  # 順位表順位
$HbgNameCell    = 'class=NameCell';    # 順位表島の名前
$HbgInfoCell    = 'class=InfoCell';    # 順位表島の情報
$HbgCommentCell = 'class=CommentCell'; # 順位表コメント欄
$HbgInputCell   = 'class=InputCell';   # 開発計画フォーム
$HbgMapCell     = 'class=MapCell';     # 開発計画地図
$HbgCommandCell = 'class=CommandCell'; # 開発計画入力済み計画
$HbgPoinCell    = 'class=PoinCell';    # Point欄
$HbgTotoCell    = 'class=TotoCell';    # toto欄

1;
