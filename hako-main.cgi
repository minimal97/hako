#!/usr/bin/perl
# ↑はサーバーに合わせて変更して下さい。
# perl5用です。
# Hakoniwa R.A. JS.(based on 020610model)
my ($versionInfo) = "version4.49";        #ここもうメンテしてない。。。
#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# メインスクリプト(ver1.02)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# Hakoniwa R.A. ver2.11
# メインスクリプト(箱庭諸島 ver2.30)
# 使用条件、使用方法等は、read-renas.txtファイルを参照
#
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------
#use strict 'vars';
require "./html_template.pl";
BEGIN {
########################################
# エラー表示
$SIG{__WARN__} =
sub {
    my ($msg) = @_;

    print STDOUT <<END;
Content-type: text/html

<p><big><tt>WARNNING: $msg</tt></big></p>
END
};

$SIG{__DIE__} =
sub {
    my ($msg) = @_;

    open(ERR_OUT , "> error.log");
    print ERR_OUT "ERROR: $msg";
    chmod(0644,"error.log");

    print STDOUT <<END;
Content-type: text/html

<p><big><tt>ERROR: $msg</tt></big></p>
END
exit(-1);
};

$SIG{KILL} =
sub {
    my ($msg) = @_;

    print STDOUT <<END;
Content-type: text/html

<p><big><tt>KILL: $msg</tt></big></p>
END
exit(-1);
};
########################################
}
# 初期設定用ファイルを読み込む
require './hako-const.cgi';
require './hako-init.cgi';
require './hako-io.cgi';
require './init-game.cgi';
require './server_config.pm';

use constant MAIN_WIIU_AXES_FILE    => 'ipfile.dat';

our ($Hakoniwa_start_time);
if (USE_PERFORMANCE) {
    use Time::HiRes;  
    $Hakoniwa_start_time = Time::HiRes::time;
}

    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    our %Hday = ('year' => $year , 'month' => $mon+1, 'day' => $mday  ,'hour' => $hour , 'min' => $min , 'sec' => $sec);

#----------------------------------------------------------------------
# 以下、好みによって設定する部分
#----------------------------------------------------------------------
# 異常終了基準時間
# (ロック後何秒で、強制解除するか)
my ($unlockTime) = 120;
use constant MAIN_UNLOCK_TIME    => 120;

#----------------------------------------------------------------------
# 好みによって設定する部分は以上
#----------------------------------------------------------------------


#----------------------------------------------------------------------
# これ以降のスクリプトは、変更されることを想定していませんが、
# いじってもかまいません。
# コマンドの名前、値段などは解りやすいと思います。
#----------------------------------------------------------------------
my ($WiiUaxesFile) = 'ipfile.dat';
our ($debug_msg) = '';
our ($HAnoSend) = 0;
our ($HadminMode) = 0;

#----------------------------------------------------------------------
# 各種定数
#----------------------------------------------------------------------
# 地形番号
require './hako-land_const.cgi';


# =============================================================================
# 計画番号の設定
# 整地系
our $HcomPrepare    = 01; #  1 整地
our $HcomPrepare2   = 02; #  2 地ならし
our $HcomReclaim    = 03; #  3 埋め立て
our $HcomDestroy    = 04; #  4 掘削
our $HcomSellTree   = 05; #  5 伐採

our $HcomMinato     = 06; #  6 港開発
our $HcomFune       = 07; #  7 造船
our $HcomSeki       = 10; #  8 関所建設

# 作る系
our $HcomPlant      = 11; #  9 植林
our $HcomFarm       = 12; # 10 農場整備
our $HcomFactory    = 13; # 11 工場建設
our $HcomMountain   = 14; # 12 採掘場整備
our $HcomBase       = 15; # 13 ミサイル基地建設
our $HcomDbase      = 16; # 14 防衛施設建設
our $HcomSbase      = 17; # 15 海底基地建設
our $HcomMonument   = 18; # 16 記念碑建造
our $HcomHaribote   = 19; # 17 ハリボテ設置

our $HcomSeacity    = 20; # 18 海底都市建設
our $HcomMonbuy     = 21; # 19 怪獣購入
our $HcomMonbuyt    = 22; # 20 tetora購入
our $HcomPark       = 23; # 21 遊園地建設
our $HcomMine       = 24; # 22 地雷設置
our $HcomNursery    = 25; # 23 養殖場設置
our $HcomKyujo      = 26; # 24 野球場
our $HcomUmiamu     = 27; # 25 海あみゅ建設
our $HcomFoodim     = 28; # 26 食物研究所建設
our $HcomProcity    = 29; # 27 防災化
our $HcomBoku       = 30; # 28 僕の引越し

# 発射系
our $HcomMissileNM    = 31; # ミサイル発射
our $HcomMissilePP    = 32; # PPミサイル発射
our $HcomMissileST    = 33; # STミサイル発射
our $HcomMissileLD    = 34; # 陸地破壊弾発射
our $HcomSendMonster  = 35; # 怪獣派遣
our $HcomMissileSPP   = 36; # SPPミサイル発射
our $HcomMissileSS    = 37; # 核ミサイル発射
our $HcomMissileLR    = 38; # 地形隆起弾発射

# 人工衛星発射
our $HcomEisei      = 39; # 人工衛星発射
our $HcomEiseimente = 40; # 人工衛星メンテ

# 運営系
our $HcomDoNothing  = 41; # 資金繰り
our $HcomSell       = 42; # 食料輸出
our $HcomMoney      = 43; # 資金援助
our $HcomFood       = 44; # 食料援助
our $HcomPropaganda = 45; # 誘致活動
our $HcomGiveup     = 46; # 島の放棄
our $HcomSave       = 47; # 保存
our $HcomLoad       = 48; # 復元
our $HcomAlly       = 49; # 同盟加盟・脱退

our $HcomSendPirates = 50;  # 海賊

our $HcomNewtown    = 70; # 29 ニュータウン建設
our $HcomBigtown    = 71; # 30 現代都市建設
our $HcomSeatown    = 72; # 31 海底ニュー建設
our $HcomFarmcpc    = 73; # 32 牧場建設
our $HcomCollege    = 74; # 大学建設
our $HcomOnsen      = 75; # 温泉掘削
our $HcomReclaim2   = 76; # 遠距離埋め立て
our $HcomHouse      = 77; # 島主の家
our $HcomRizort     = 78; # リゾート地
our $HcomBettown    = 79; # 輝ける都市

our $HcomEiseiLzr   = 80; # 人工衛星レーザー
our $HcomEiseiAtt   = 81; # 人工衛星破壊

our $HcomGivefood   = 100;  # エサをあげる
our $HcomKai        = 101;  # 改装
our $HcomHTget      = 102;  # ハイテクゲット
our $HcomArmSupply  = 103;  # 軍事物資調達
our $HcomReclaim2dan = 105; # 2段階埋め立て
our $HcomDestroy2   = 106;  # 高速掘削
our $HcomReclaim_spd = 107; # 高速埋め立て
our $HcomYotei      = 108;  # 予定地
our $HcomBoku2      = 109;  # 僕の引越し２
our $HcomYakusho    = 110;  # 役所
our $HcomFire       = 111;  # 消防署建設
our $HcomItemUse    = 112;  # アイテムおく
our $HcomItemThrow  = 113;  # アイテム捨てる
our $HcomZoo        = 114;  # 動物園建設

our $HcomMax = 114; #コマンド表示用の上限




# 自動入力系
our $HcomAutoPrepare    = 200; # 51 フル整地
our $HcomAutoPrepare2    = 201; # 52 フル地ならし
our $HcomAutoDelete        = 202; # 53 全コマンド消去
our $HcomAutoReclaim    = 203; # 54 浅瀬埋め立て
our $HcomAutoDestroy    = 204; # 55 浅瀬掘削
our $HcomAutoSellTree    = 205; # 56 伐採
our $HcomAutoForestry    = 206; # 57 伐採と植林

our @HkindBFM = ($HcomMissileNM,
                 $HcomMissilePP,
                 $HcomMissileSPP,
                 $HcomMissileST,
                 $HcomMissileSS);

# 順番
# コマンドリスト 変換前
our @HcomList = ();
    {
        my @comList =
           ($HcomHouse, $HcomBettown, $HcomKai, $HcomPrepare, $HcomSell,
            $HcomPrepare2, $HcomYotei, $HcomReclaim, $HcomReclaim2, $HcomReclaim2dan ,$HcomReclaim_spd ,
            $HcomDestroy,$HcomDestroy2, $HcomOnsen,
            $HcomSellTree, $HcomPlant, $HcomFarm, $HcomFoodim, $HcomFarmcpc, $HcomFactory, $HcomHTget, $HcomMountain, $HcomNursery, $HcomCollege,$HcomFire,
            $HcomPark, $HcomKyujo, $HcomUmiamu, $HcomZoo,
            $HcomRizort, $HcomBase, $HcomDbase, $HcomSbase, $HcomSeacity,
            $HcomMonument, $HcomMonbuy, $HcomMonbuyt, $HcomHaribote, $HcomMine,
            $HcomMinato, $HcomFune, $HcomProcity, $HcomNewtown, $HcomBigtown, $HcomSeatown, $HcomBoku, $HcomBoku2, $HcomYakusho, $HcomSeki,
            $HcomEisei, $HcomEiseimente,
            $HcomMissileNM, $HcomMissilePP, $HcomMissileSPP,
            $HcomMissileST, $HcomMissileLD, $HcomMissileLR, $HcomMissileSS, $HcomEiseiLzr, $HcomEiseiAtt, $HcomSendMonster, $HcomSendPirates,
            $HcomDoNothing,
            $HcomMoney, $HcomFood, $HcomPropaganda, $HcomGiveup, $HcomGivefood,
            $HcomItemThrow, $HcomItemUse,
            $HcomSave, $HcomLoad, $HcomAlly,
            $HcomAutoReclaim, $HcomAutoDestroy, $HcomAutoSellTree, $HcomAutoForestry,
            $HcomAutoPrepare, $HcomAutoPrepare2, $HcomAutoDelete);

# ここはいじらないでください
        my $addr    = $ENV{'REMOTE_ADDR'};
        foreach (@comList) {
            next if (($_ == $HcomAlly) && (!(ALLY_USE) || !$HallyJoinComUse || $HarmisticeTurn));
            next if (($_ == $HcomMissileST) && !$HuseMissileST);
            next if (($_ == $HcomSendMonster) && !INIT_USE_SEND_MONSTER);
            push(@HcomList, $_);
        }
    }
our $HcommandTotal = $#HcomList + 1; # コマンドの種類

# コマンド分割
# このコマンド分割だけは、自動入力系のコマンドは設定しないで下さい。
# our @HcommandDivido = 
#    (
#    '運営,41,50',   # 計画番号41〜50
#    '整地,0,5',     # 計画番号00〜05
#    '建設,11,19',   # 計画番号11〜19
#    '開発,6,10',    # 計画番号06〜10
#    '都市,70,79',   # 計画番号70〜75
#    '施設,20,30',   # 計画番号20〜30
#    '衛星,39,40',   # 計画番号39〜40
#    '運営,100,113', # 計画番号100〜105
#    '攻撃,31,38',   # 計画番号31〜38
#    '攻撃,80,85',   # 計画番号80〜85
#    );

# コマンド分割
# 自信ないけど、ひとまずコマンドを管理できる。
# 表示は、mapのプログラムで管理。。。
our @HcommandDivido2 = 
    (
    "運営,$HcomDoNothing,$HcomSell,$HcomMoney,$HcomFood"
       .",$HcomPropaganda,$HcomGiveup,$HcomSave,$HcomLoad"
       .",$HcomAlly",

    "整地,$HcomPrepare,$HcomPrepare2,$HcomReclaim,$HcomReclaim2dan,$HcomReclaim2"
       .",$HcomDestroy,$HcomDestroy2,$HcomReclaim_spd"
       .",$HcomSellTree",

    "建設,$HcomPlant,$HcomFarm"
       .",$HcomFactory,$HcomMountain"
       .",$HcomBase,$HcomDbase"
       .",$HcomSbase,$HcomMonument"
       .",$HcomHaribote",

    "開発,$HcomMinato,$HcomFune"
       .",$HcomSeki",

    "都市,$HcomNewtown,$HcomBigtown"
       .",$HcomSeatown,$HcomFarmcpc"
       .",$HcomCollege,$HcomOnsen"
       .",$HcomHouse"
       .",$HcomRizort,$HcomBettown",

    "施設,$HcomSeacity,$HcomPark"
       .",$HcomMine,$HcomNursery"
       .",$HcomKyujo,$HcomUmiamu"
       .",$HcomFoodim,$HcomProcity"
       .",$HcomFire,$HcomZoo"
       .",$HcomMonbuy,$HcomMonbuyt",

    "衛星,$HcomEisei,$HcomEiseimente",

    "運営,$HcomGivefood,$HcomKai"
       .",$HcomHTget,$HcomArmSupply"
       .",$HcomYotei,$HcomBoku"
       .",$HcomBoku2,$HcomYakusho"
       .",$HcomItemUse"
       .",$HcomItemThrow",

    "攻撃,$HcomMissileNM,$HcomMissilePP"
       .",$HcomMissileST,$HcomMissileSPP"
       .",$HcomMissileLR,$HcomMissileSS"
       .",$HcomMissileLD,$HcomSendMonster,$HcomSendPirates",

    "攻撃,$HcomEiseiLzr,$HcomEiseiAtt",
    );

# 自動入力を固めたもの
# java scriptで右に出てるやつ
our @Hcommand_Auto =
    (
        $HcomAutoPrepare,
        $HcomAutoPrepare2,
        $HcomAutoDelete,
        $HcomAutoReclaim,
        $HcomAutoDestroy,
        $HcomAutoSellTree,
        $HcomAutoForestry,
    );

# 計画の名前と値段
# Pointx### にすると、ポイントになる。
our @HcomName;
our @HcomCost;

SetCommandData($HcomHouse       , '自宅建設/税率変更' , 'Pointx3');
SetCommandData($HcomBettown     , '輝ける都市計画'    , 'Pointx1');
SetCommandData($HcomKai         , '改装・強化'        , 'Pointx1');
SetCommandData($HcomPrepare     , '整地'              , 5);
SetCommandData($HcomYotei       , '予定地確保/解除'   , 0);

SetCommandData($HcomPrepare2    , '地ならし'          , 100);
SetCommandData($HcomReclaim     , '埋め立て'          , 150);
SetCommandData($HcomReclaim2    , '遠距離埋め立て'    , 3000);
SetCommandData($HcomReclaim2dan , '2段埋め立て'       , 2000);
SetCommandData($HcomReclaim_spd , '高速埋め立て'      , 2450);
SetCommandData($HcomDestroy     , '掘削'              , 200);
SetCommandData($HcomDestroy2    , '高速掘削'          , 2000);

SetCommandData($HcomMinato      , '港町開発'          , 550);
SetCommandData($HcomOnsen       , '温泉掘削'          , 50);
SetCommandData($HcomFune        , '造船・出航'        , 300);

SetCommandData($HcomSeki        , '関所建設'          , 200);
SetCommandData($HcomSellTree    , '伐採'              , 0);
SetCommandData($HcomPlant       , '植林'              , 50);
SetCommandData($HcomFarm        , '農場整備'          , 20);
SetCommandData($HcomFoodim      , '食物研究所建設'    , 2500);

SetCommandData($HcomFarmcpc     , '牧場建設/家畜販売' , 1500);
SetCommandData($HcomCollege     , '大学建設'          , 500);
SetCommandData($HcomFactory     , '工場建設'          , 100);
SetCommandData($HcomHTget       , 'ハイテク技術誘致'  , 10000);

SetCommandData($HcomMountain    , '採掘場整備'        , 300);
SetCommandData($HcomBase        , 'ミサイル基地建設'  , 300);
SetCommandData($HcomDbase       , '防衛施設建設'      , 800);
SetCommandData($HcomSbase       , '海底基地建設'      , 8000);
SetCommandData($HcomSeacity     , '海底都市建設'      , 77777);
SetCommandData($HcomMonument    , '記念碑建造'        , 9999);
SetCommandData($HcomMonbuy      , '怪獣の購入/配置'   , 3980);
SetCommandData($HcomMonbuyt     , 'テトラの購入/配置' , 10000);
SetCommandData($HcomHaribote    , 'ハリボテ設置'      , 1);

SetCommandData($HcomMine        , '地雷設置'          , 100);
SetCommandData($HcomPark        , '遊園地建設'        , 1000);
SetCommandData($HcomNursery     , '養殖場設置'        , 50);
SetCommandData($HcomKyujo       , '野球場建設'        , 1000);
SetCommandData($HcomUmiamu      , '海あみゅ建設'      , 15000);
SetCommandData($HcomRizort      , 'リゾート地開発'    , 40000);

SetCommandData($HcomProcity     , '防災都市化'        , 25000);
SetCommandData($HcomNewtown     , 'ニュータウン建設'  , 950);
SetCommandData($HcomBigtown     , '現代都市建設'      , 45000);
SetCommandData($HcomSeatown     , '海底新都市建設'    , 69800);
SetCommandData($HcomBoku        , '僕の引越し'        , 1000);
SetCommandData($HcomBoku2       , '僕の引越し2'       , 'Pointx4');

SetCommandData($HcomEisei       , '人工衛星打ち上げ'  , 9999);
SetCommandData($HcomEiseimente  , '人工衛星修復'      , 5000);
SetCommandData($HcomEiseiAtt    , '衛星破壊砲発射'    , 49999);
SetCommandData($HcomEiseiLzr    , '衛星レーザー発射'  , 39999);

SetCommandData($HcomMissileNM   , 'ミサイル発射'      , 20);
SetCommandData($HcomMissilePP   , 'PPミサイル発射'    , 50);
SetCommandData($HcomMissileSPP  , 'SPPミサイル発射'   , 1000);
SetCommandData($HcomMissileST   , 'STミサイル発射'    , 50);
SetCommandData($HcomMissileLD   , '陸地破壊弾発射'    , 100000);
SetCommandData($HcomMissileLR   , '地形隆起弾発射'     , 50000);
SetCommandData($HcomMissileSS   , '核ミサイル発射'     , 100000);

SetCommandData($HcomSendMonster , '怪獣派遣'           , 500);
SetCommandData($HcomSendPirates , '海賊派遣'           , 1500);

SetCommandData($HcomDoNothing   , '資金繰り'           , 0);
SetCommandData($HcomSell        , '食料輸出'           , -100);
SetCommandData($HcomMoney       , '資金援助'           , 100);
SetCommandData($HcomFood        , '食料援助'           , -100);

SetCommandData($HcomPropaganda  , '誘致活動'           , 1000);
SetCommandData($HcomGiveup      , "${AfterName}の放棄" , 0);
SetCommandData($HcomGivefood    , 'エサをあげる'       , -50000);
SetCommandData($HcomYakusho     , '島役所建設'         , 30000);
SetCommandData($HcomFire        , '消防署建設'         , 600);

SetCommandData($HcomItemThrow   , 'アイテム捨てる'     , 0);
SetCommandData($HcomItemUse     , 'アイテムおく'       , 0);

SetCommandData($HcomZoo         , '動物園建設'         , 100000);
#- - - - - - - - - - - - - - - - - - - - - - - -
SetCommandData($HcomAutoPrepare  , '整地自動入力'         , 0);
SetCommandData($HcomAutoPrepare2 , '地ならし自動入力'     , 0);
SetCommandData($HcomAutoDelete   , '全計画を白紙撤回'     , 0);
SetCommandData($HcomAutoReclaim  , '浅瀬埋め立て自動入力' , 0);
SetCommandData($HcomAutoDestroy  , '浅瀬掘削自動入力'     , 0);
SetCommandData($HcomAutoSellTree , '伐採自動入力'         , 0);
SetCommandData($HcomAutoForestry , '伐採＆植林自動入力'   , 0);

#- - - - - - - - - - - - - - - - - - - - - - - -
SetCommandData($HcomAlly , '同盟へ加盟・脱退' , 0);
SetCommandData($HcomSave , '時の記憶'         , 100000);
SetCommandData($HcomLoad , '時の忘却'         , 100000);

#----------------------------------------------------------------------
# 変数
#----------------------------------------------------------------------

# COOKIE
our ($defaultID) = 0;       # 島の名前
our ($defaultTarget) = '';   # ターゲットの名前
our ($rqID) = -1;

my ($access) ='';
my ($wiiU_javamode) = 'java';
my ($wiiU_password) = '';
my ($init_ID) = 0;       #初期の表示用ID

# 島の座標数
our $HpointNumber = $HislandSize * $HislandSize;
our $pointNumber = $HpointNumber - 1;

our $HtempBack;         # 「戻る」リンク

# ゲーム用
our $HmainMode;
our ($HjavaMode) = '';
our ($HdefaultPassword) = '';
our $HdefaultY;
our ($HdefaultName) = '';
our $HspeakerID;
our $HallyPactMode;
our $HcurrentCampID;

our @Hrpx , @Hrpy;

our $HallyTitle;
our $HallyMessage;

our ($HcurrentID) = 0;

our $HDayEvent;             # イベント日
our $HDayEvent_Edge;        # イベント日 イベント完了フラグ

our $Hms1;                  # mapサイズ
our $Hms2;                  # mapサイズ

our $HislandTurn;           # ターン数

our ($HlbbsMode) = 0;

our $HsepTurnFlag;

our ($Htitle_sub) = '';

our ($HimgLine) = '';
our ($HjavaModeSet) = 0;
our ($HskinName) = '' ;
our ($HviewIslandNumber) = 0;

our $HcommandX, $HcommandY ,$HcommandArg;
our $HcommandComary;
our $HasetupMode;

our $HSpace_Debris;

our @HrankingID;

our $HplayNow;      # ターンを更新しました
our $HnextTime;     # ターン更新時刻

our ($Body) = '<body>';

#----------------------------------------------------------------------
# メイン
#----------------------------------------------------------------------
    # 「戻る」リンク
    $HtempBack = "<a href=\"$HthisFile\"><span class='big'>トップへ戻る</span></a>";
    $Body = '<body>';

    # 乱数の初期化
    srand(time() ^ ($$ + ($$ << 15)));

    wiiU_ip_check();

    # COOKIE読みこみ
    cookieInput();

    # CGI読みこみ
    cgiInput();

    # ロックをかける
    if (!$HsepTurnFlag && !hakolock()) {
        # ロック失敗

        tempHeader();   # ヘッダ出力
        tempLockFail(); # ロック失敗メッセージ
        tempFooter();   # フッタ出力
        exit(0);        # 終了
    }

    if (-e $HpasswordFile) {
        # パスワードファイルがある
        open(PIN, "<$HpasswordFile") || die $!;
        chomp($HmasterPassword  = <PIN>); # マスタパスワードを読み込む
        chomp($HspecialPassword = <PIN>); # 特殊パスワードを読み込む
        close(PIN);
    }
    else {

        unlock();
        tempHeader();
        tempNoPasswordFile();
        tempFooter();
        exit(0);
    }

    # 島データの読みこみ
    if (readIslandsFile($HcurrentID) == 0) {

        unlock();
        tempHeader();
        tempNoDataFile();
        tempFooter();
        exit(0);
    }

    # テンプレートを初期化
    if (   ($HmainMode eq 'turn')
        || (   ($HmainMode eq 'top')
            && (!checkMasterPassword($HinputPassword)) ) ) {
        tempInitialize(0);
    }
    else {
        tempInitialize(1);
    }

    # COOKIEによるIDチェック
    if ($HmainMode eq 'owner') {
        # アクセス・ログ
        axeslog() if($HtopAxes >= 1);
        
        unless($ENV{'HTTP_COOKIE'}) {
            cookieOutput();                 # COOKIEが削除されたかどうか書き込みチェック
            next if($ENV{'HTTP_COOKIE'});   # 書き込みOK
        # クッキーを有効にしていない
        #    unlock();
        #    tempHeader();
        #    tempWrong("クッキーを有効にしてください。");
        #    tempFooter();
        #    exit(0);
        }

        if ($checkID || $checkImg) {
            # idから島を取得
            my ($pcheck) = checkPassword($Hislands[$HidToNumber{$HcurrentID}],$HinputPassword);
            my ($free) = 0;

            foreach (@freepass) {
                $free += 1 if(($_ == $defaultID) || ($_ == $HcurrentID));
            }
            my ($icheck) = !($checkID && ($HcurrentID != $defaultID) && $defaultID);
            my ($lcheck) = !($checkImg && ($HimgLine eq '' || $HimgLine eq $HimageDir));
            # パスワード
            if(($pcheck != 2) && ($free != 2) && (!$icheck || !$lcheck)) {
                # １つの島を初心者用に解放する時などは ($free != 2) の部分を !$free に変更して下さい。
                unlock();
                tempHeader();
                if(!$icheck) {

                    tempWrong("自分の島以外には入れません！"); # ID違い
                }
                else {
                    tempWrong("「画像のローカル設定」をして下さい。"); # ローカル設定していない
                }
                tempFooter();
                exit(0);
            }
        }
    }

    # COOKIE出力
    cookieOutput();

    # ヘッダ出力
    if (   ($HmainMode eq 'commandJava')                            # コマンド入力モード
        || ($HmainMode eq 'command2')                               # コマンド入力モード（ver1.1より追加・自動系用
        || (   ($HjavaMode eq 'java')
            && (   ($HmainMode eq 'owner')
                || ($HmainMode eq 'comment')                        # コメント入力モード
                || ($HmainMode eq 'totoyoso')                       # TOTO予想１入力モード
                || ($HmainMode eq 'totoyoso2')                      # TOTO予想２入力モード
                || ($HmainMode eq 'lbbs')                           # コメント入力モード
                || ($HmainMode eq 'shuto')                          # 首都名変更モード
                || ($HmainMode eq 'teamname')                       # 首都名変更モード
                || ($HmainMode eq 'yaku_chg')                       # 首都名変更モード
                || ($HmainMode eq 'preab')                          # 陣営共同開発モード
                                                ) )
        || (0)) { 

        $Htitle_sub = ' マップ 開発';
        $Body = "<body onload=\"SelectList('');init()\">";
        require('./hako-map.cgi');

        # ヘッダ出力
        tempHeaderJava();
        if($HmainMode eq 'commandJava') {           # 開発モード
            commandJavaMain();

        } elsif($HmainMode eq 'command2') {         # 開発モード2（ver1.1より追加・自動系コマンド用）
            commandMain();

        } elsif($HmainMode eq 'comment') {          # コメント入力モード
            commentMain();

        } elsif($HmainMode eq 'totoyoso') {         # TOTO予想１入力モード
            totoInputMain(0);

        } elsif($HmainMode eq 'totoyoso2') {        # TOTO予想２入力モード
            totoInputMain(1);

        } elsif($HmainMode eq 'shuto') {            # 首都名変更モード
            require('./hako-map.cgi');
            shutoMain();

        } elsif($HmainMode eq 'teamname') {         # 首都名変更モード
            require('./hako-map.cgi');
            TeamMain();

        } elsif($HmainMode eq 'yaku_chg') {         # 首都名変更モード
            require('./hako-map.cgi');
            WorkChangeMain();

        } elsif($HmainMode eq 'preab') {            # 陣営共同開発モード
            require('./hako-map.cgi');
            preabMain();

        } elsif($HmainMode eq 'lbbs') {             # ローカル掲示板モード
            require('./hako-lbbs.cgi');
            localBbsMain();

        } else {
            ownerMain();

        }
        # フッタ出力
        tempFooter();
        # 終了
        exit(0);
    }
    elsif ($HmainMode eq 'landmap') {

        $Htitle_sub = ' マップ';
        require('./hako-map.cgi');

        $Body = '<body>';
        # ヘッダ出力
        tempHeaderJava();
        # 観光モード
        printIslandJava();
        # フッタ出力
        tempFooter();
        # 終了
        exit(0);

    }
    elsif ($HmainMode eq 'taijilist') {        # 管理人によるあずかりモード
        require('./hako-map.cgi');
        $Body = '<body>';
        # ヘッダ出力
        tempHeaderJava();

        Show_Taiji_List();

        # フッタ出力
        tempFooter();
        # 終了
        exit(0);

    }
    elsif(   ($HmainMode ne 'new')
          && ($HmainMode ne 'lbbs') ) {
        # ヘッダ出力
        tempHeader();
    }

    # =====================================================================

    if ($HmainMode eq 'turn') {             # ターン進行
        require('./hako-turn.cgi');
        turnMain();

    } elsif($HmainMode eq 'new') {          # 島の新規作成
        require('./hako-make.cgi');
        require('./hako-map.cgi');
        newIslandMain();

    } elsif($HmainMode eq 'top') {          # 管理人によるあずかりモード
        # その他の場合はトップページモード
        require('./hako-top.cgi');
        topPageMain();

    } elsif($HmainMode eq 'newally') {      # 同盟の新規作成
        require('./hako-make.cgi');
        require('./hako-top.cgi');
        makeAllyMain();

    } elsif($HmainMode eq 'delally') {      # 同盟の削除
        require('./hako-make.cgi');
        require('./hako-top.cgi');
        deleteAllyMain();

    } elsif($HmainMode eq 'inoutally') {    # 同盟の加盟・脱退
        require('./hako-make.cgi');
        require('./hako-top.cgi');
        joinAllyMain();

    } elsif($HmainMode eq 'allypact') {     # 盟主コメントモード
        require('./hako-make.cgi');
        allyPactMain();

    } elsif($HmainMode eq 'joinally') {     # 同盟設定
        require('./hako-make.cgi');
        newAllyTop();

    } elsif($HmainMode eq 'aoa') {          # 同盟内の友好国設定
        require('./hako-top.cgi');
        amityOfAlly();

    } elsif($HmainMode eq 'preab') {        # 陣営共同開発モード
        require('./hako-map.cgi');
        preabMain();

    } elsif($HmainMode eq 'campCHAT') {     # 陣営モード
        require('./hako-map.cgi');
        require('./hako-camp.cgi');
        campMain(1);

    } elsif($HmainMode eq 'camp') {         # 陣営モード
        require('./hako-map.cgi');
        require('./hako-camp.cgi');
        campMain(0);

    } elsif($HmainMode eq 'asetup') {       # 友好国設定確認モード
        require('./hako-make.cgi');
        amitySetupMain();

    } elsif($HmainMode eq 'print') {        # 観光モード
        require('./hako-map.cgi');
        $Htitle_sub = ' マップ';
        printIslandMain();

    } elsif($HmainMode eq 'productlist') {  # プロダクトリスト
        require ('./hako-map_product.cgi');
        $Htitle_sub = ' 物資';
        ProductListMain();

    } elsif($HmainMode eq 'tradelist') {    # 取引リスト
        require ('./hako-map.cgi');
        require ('./hako-trade.cgi');
        $Htitle_sub = ' 取引';
        TradeListMain();

    } elsif($HmainMode eq 'tradedelete') {  # 取引リスト
        require ('./hako-map.cgi');
        require ('./hako-trade.cgi');
        $Htitle_sub = ' 取引';
        TradeDeleteMain();
        TradeListMain();

    } elsif($HmainMode eq 'trademake') {    # 取引リスト
        require ('./hako-map.cgi');
        require ('./hako-trade.cgi');
        $Htitle_sub = ' 取引';
        TradeMakeMain();
        TradeListMain();

    }
    elsif($HmainMode eq 'tradecng') {       # 取引リスト
        require ('./hako-map.cgi');
        require ('./hako-trade.cgi');
        $Htitle_sub = ' 取引';
        TradeEditMain();
        TradeListMain();

    } elsif($HmainMode eq 'owner') {        # 開発モード
        require ('./hako-map.cgi');
        $Htitle_sub = ' 開発';
        ownerMain();

    } elsif($HmainMode eq 'command') {      # コマンド入力モード
        require('./hako-map.cgi');
        commandMain();

    } elsif($HmainMode eq 'comment') {      # コメント入力モード
        require('./hako-map.cgi');
        commentMain();

    } elsif($HmainMode eq 'lbbs') {         # ローカル掲示板モード
        require('./hako-map.cgi');
        require('./hako-lbbs.cgi');
        localBbsMain();

    } elsif($HmainMode eq 'change') {       # 情報変更モード
        require('./hako-make.cgi');
        changeMain();

    } elsif($HmainMode eq 'totoyoso') {     # コメント入力モード
        require('./hako-map.cgi');
        totoInputMain(0);

    } elsif($HmainMode eq 'totoyoso2') {    # コメント入力モード
        require('./hako-map.cgi');
        totoInputMain(1);

    } elsif($HmainMode eq 'shuto') {        # 首都名変更モード
        require('./hako-map.cgi');
        shutoMain();

    } elsif($HmainMode eq 'rank') {         # ランキング
        require('./hako-ranking.cgi');
        rankIslandMain();

    } elsif($HmainMode eq 'rekidai') {      # 歴代最多人口記録
        require('./hako-ranking.cgi');
        rekidaiPopMain();

    } elsif($HmainMode eq 'hcdata') {       # HakoniwaCup戦績
        require('./hako-make.cgi');
        hcdataMain();

    } elsif($HmainMode eq 'bf_point') {     # bf 戦績
        require('./hako-make.cgi');
        bfpointMain();

    } elsif($HmainMode eq 'teamname') {     # 首都名変更モード
        require('./hako-map.cgi');
        TeamMain();

    } elsif($HmainMode eq 'yaku_chg') {     # 首都名変更モード
        require('./hako-map.cgi');
        WorkChangeMain();

    } elsif($HmainMode eq 'join') {         # 新しい島を探す
        require('./hako-make.cgi');
        newIslandTop();

    } elsif($HmainMode eq 'rename') {       # 島の名前とパスワードの変更
        require('./hako-make.cgi');
        renameIslandMain();

    } elsif($HmainMode eq 'bfield') {       # BattleField作成モード
        require('./hako-make.cgi');
        bfieldMain();

    } elsif($HmainMode eq 'present') {      # 管理人によるプレゼントモード
        require('./hako-make.cgi');
        presentMain();

    } elsif($HmainMode eq 'punish') {       # 管理人による制裁モード
        require('./hako-make.cgi');
        punishMain();

    } elsif($HmainMode eq 'lchange') {      # 管理人による地形変更モード
        require('./hako-make.cgi');
        lchangeMain();

    } elsif($HmainMode eq 'predelete') {    # 管理人によるあずかりモード
        require('./hako-make.cgi');
        preDeleteMain();

    } else {
        # その他の場合はトップページモード
        require('./hako-top.cgi');
        topPageMain();
    }

    # フッタ出力
    tempFooter();

    # 終了
    exit(0);


#----------------------------------------------------------------------
# コマンド設定

sub SetCommandData {
    my ($id, $name, $cost) = @_;

    $HcomCost[$id] = $cost;
    $HcomName[$id] = $name;
}


#----------------------------------------------------------------------
# コマンドを前にずらす
sub slideFront {
    my ($command, $number) = @_;

    # それぞれずらす
    splice(@$command, $number, 1);

    # 最後に資金繰り
    $command->[$HcommandMax - 1] = {
        'kind' => $HcomDoNothing,
        'target' => 0,
        'x' => 0,
        'y' => 0,
        'arg' => 0
    };
}

#----------------------------------------------------------------------
# コマンドを後にずらす
sub slideBack {
    my ($command, $number) = @_;

    # それぞれずらす
    return if ($number == $#$command);
    pop(@$command);
    splice(@$command, $number, 0, $command->[$number]);
}


#----------------------------------------------------------------------
# 入出力
#----------------------------------------------------------------------

# CGIの読みこみ
sub cgiInput {
    my ($line, $getLine);

    # 入力を受け取って日本語コードをEUCに
    $line = <>;
    $line =~ tr/+/ /;
    $line =~ s/%([a-fA-F0-9]{2})/pack(H2, $1)/eg;
#   jcode::convert(\$line, 'euc');

    if ($line !~ /Allypact=([^\&]*)\&/) {

        $line =~ s/[\x00-\x1f\,]//g;
    }
    else {
        # 盟主コメントモード
        # 変更ボタンが押された起動
        $HmainMode = 'allypact';
        $HallyPactMode = 1;
        $HdefaultPassword = $1;
        $line =~ /ALLYCOMMENT=([^\&]*)\&/;
        $HallyComment = cutColumn($1, $HlengthAllyComment*2);
        $line =~ /ALLYTITLE=([^\&]*)\&/;
        $HallyTitle = cutColumn($1, $HlengthAllyTitle*2);
        $line =~ /ISLANDID=([0-9]+)\&/;
        $HcurrentID = $1;
        $line =~ s/(.*)ALLYMESSAGE=//g;
        $HallyMessage = cutColumn($line, $HlengthAllyMessage*2);
        return;
    }

    # GETのやつも受け取る
    $getLine = $ENV{'QUERY_STRING'};

    # 対象の島
    if($line =~ /ISLANDID=([0-9]+)\&/){
        $HcurrentID = $1;
    }

    # パスワード
    if($line =~ /OLDPASS=([^\&]*)\&/) {
        $HoldPassword = $1;
        $HdefaultPassword = $1;
    }
    if($line =~ /PASSWORD=([^\&]*)\&/) {
        $HinputPassword = $1;
        $HdefaultPassword = $1;
    }
    if($line =~ /PASSWORD2=([^\&]*)\&/) {
        $HinputPassword2 = $1;
    }

    # Ｊａｖａスクリプトモード
    if ($line =~ /JAVAMODE=(cgi|java)/) {
        $HjavaMode = $1;
    } elsif ($getLine =~ /JAVAMODE=(cgi|java)/) {
        $HjavaMode = $1;
    }
    if ($getLine =~ /UNLOCK=([0-9]*)/) {
        $HsepTurnFlag = $1;
    }
    # main modeの取得
    if ($line =~ /TurnButton/) {
        if (DEBUG_MODE) {
            $HmainMode = 'Hdebugturn';
        }
    }
    elsif ($line =~ /OwnerButton/) {
        $HmainMode = 'owner';
    }
    elsif ($line =~ /CommandJavaButton([0-9]+)=/) {
        # コマンド送信ボタンの場合（Ｊａｖａスクリプト）
        $HcurrentID = $1;
        $HmainMode = 'commandJava';
        $line =~ /COMARY=([^\&]*)\&/;
        $HcommandComary = $1;
        $line =~ /COMMAND=([^\&]*)\&/;
        $HcommandKind = $1;
        $HdefaultKind = $1;
        $line =~ /AMOUNT=([^\&]*)\&/;
        $HcommandArg = $1;
        $line =~ /TARGETID=([^\&]*)\&/;
        $HcommandTarget = $1;
        $defaultTarget = $1;
        $line =~ /POINTX=([^\&]*)\&/;
        $HcommandX = $1;
        $HdefaultX = $1;
        $line =~ /POINTY=([^\&]*)\&/;
        $HcommandY = $1;
        $HdefaultY = $1;
        # コマンドのポップアップメニューを開く？
        if ($line =~ /MENUOPEN=on/) {
            $HmenuOpen = 'CHECKED';
        }
        elsif ($line =~ /MENUOPEN2=on/) {
            $HmenuOpen2 = 'CHECKED';
        }

    }
    elsif ($line =~ /CommandButton([0-9]+)=/) {
        # コマンド送信ボタンの場合
        $HcurrentID = $1;
        if ($HjavaMode eq 'java') {
            $HmainMode = 'command2';
        }
        else {
            $HmainMode = 'command';
        }

        # コマンドモードの場合、コマンドの取得
        $line =~ /NUMBER=([^\&]*)\&/;
        $HcommandPlanNumber = $1;
        $line =~ /COMMAND=([^\&]*)\&/;
        $HcommandKind = $1;
        $HdefaultKind = $1;
        $line =~ /AMOUNT=([^\&]*)\&/;
        $HcommandArg = $1;
        $line =~ /TARGETID=([^\&]*)\&/;
        $HcommandTarget = $1;
        $defaultTarget = $1;
        $line =~ /POINTX=([^\&]*)\&/;
        $HcommandX = $1;
        $HdefaultX = $1;
        $line =~ /POINTY=([^\&]*)\&/;
        $HcommandY = $1;
        $HdefaultY = $1;
        if($line =~ /COMMANDMODE=(write|insert|delete)/) {
            $HcommandMode = $1;
        }
        # コマンドのポップアップメニューを開く？
        if($line =~ /MENUOPEN=on/) {
            $HmenuOpen = 'CHECKED';
        } elsif($line =~ /MENUOPEN2=on/) {
            $HmenuOpen2 = 'CHECKED';
        }
    } elsif($line =~ /Trade=([0-9]*)/) {
        $HmainMode = 'tradelist';
        $HcurrentID = $1;

    }
    elsif($line =~ /TRADE_DEL=([0-9]*)/) {
        $HmainMode = 'tradedelete';
        $TradeTargetID = $1;
        if ($line =~ /myID=([0-9]*)/) {
            $HcurrentID = $1;
        }
    }
    elsif ($line =~ /TRADE_CHG([12])=([0-9]*)/) {
        $HmainMode = 'tradecng';
        ($TradeTargetChgSide,$TradeTargetID) = ($1,$2);
        if ($line =~ /myID=([0-9]*)/) {
            $HcurrentID = $1;
        }
    }
    elsif ($line =~ /TradeMake=([0-9]*)/) {
        $HmainMode = 'trademake';
        $HcurrentID = $1;
        our ($TradeTargetID) = $HcurrentID;     # 自分のIDで初期化
        if ($line =~ /TargetId=([0-9]*)/) {
            $TradeTargetID = $1;
        }
        our ($TradeObject) = $HcurrentID;     # 自分のIDで初期化
        if ($line =~ /TradeObject=([0-9]*)/) {
            $TradeObject = $1;
        }
        our ($TradeObjectNum) = GetNumberSelectNum('TradeObjectNum' , $line);
        our ($TradeMoney) = GetNumberSelectNum('TradeMoney' , $line);
        our ($TradePaySide) = 0;
        if ($line =~ /TradePaySide=([0-9]*)/) {
            $TradePaySide = $1;
        }
        if ($line =~ /TradeObjSide=([0-9]*)/) {
            $TradeObjSide = $1;
        }

    }
    elsif ($getLine =~ /SightC=([0-9]*)/) {
        $HtempBack = "<A href=\"Javascript:void(0);\" onclick=\"window.open('about:blank','_self').close()\"><span class='big'>[閉じる]</span></A>";
        $HmainMode = 'print';
        $HcurrentID = $1;
        # 管理人モード
        if ($getLine =~ /ADMINMODE=([0-9]*)/) {
            $HadminMode = $1;
        }
    }
    elsif ($getLine =~ /Sight=([0-9]*)/) {
        $HmainMode = 'print';
        $HcurrentID = $1;
        # 管理人モード
        if ($getLine =~ /ADMINMODE=([0-9]*)/) {
            $HadminMode = $1;
        }
    } elsif ($getLine =~ /Product=([0-9]*)/) {
        $HmainMode = 'productlist';
        $HcurrentID = $1;

        # 管理人モード
        if ($getLine =~ /ADMINMODE=([0-9]*)/) {
            $HadminMode = $1;
        }
    }
    elsif ($line =~ /SightButton/) {
        $HmainMode = 'print';
        $line =~ /TARGETID=([^\&]*)\&/;
        $HcurrentID = $1;

    } elsif ($line =~ /LbbsButton(..)([0-9]*)/) {
        $HmainMode = 'lbbs';
        if ($1 eq 'AD') {
            # 管理人
            $HlbbsMode = 5;
        } elsif($1 eq 'DA') {
            # 管理人削除
            $HlbbsMode = 7;
        } elsif($1 eq 'OW') {
            # 島主
            $HlbbsMode = 1;
        } elsif($1 eq 'DL') {
            # 島主削除
            $HlbbsMode = 3;
        } elsif($1 eq 'DS') {
            # 観光者削除
            $HlbbsMode = 2;
        } elsif($1 eq 'CK') {
            # 観光者極秘確認
            $HlbbsMode = 4;
        } else {
            # 観光者
            $HlbbsMode = 0;
        }
        $HcurrentID = $2;

        $line =~ /LBBSNAME=([^\&]*)\&/;
        $HlbbsName = cutColumn($1, $HlengthLbbsName*2);
        $HdefaultName = $HlbbsName;
        $line =~ /LBBSMESSAGE=([^\&]*)\&/;
        $HlbbsMessage = cutColumn($1, $HlengthLbbsMessage*2);
        # 掲示板の発言島
        $line =~ /ISLANDID2=([0-9]+)\&/;
        $HspeakerID = $1;
        # 掲示板の通信形式
        $line =~ /LBBSTYPE=([^\&]*)\&/;
        $HlbbsType = $1;
        # 削除かもしれないので、番号を取得
        if($line =~ /NUMBER=([^\&]*)\&/) {
            $HcommandPlanNumber = $1;
        }

    } elsif ($line =~ /ChangeInfoButton/) {
        $HmainMode = 'change';
        # 名前指定の場合
        if ($line =~ /ISLANDNAME=([^\&]*)\&/){
            $HcurrentName = cutColumn($1, $HlengthIslandName*2);
        }
        # オーナー名の取得
        if ($line =~ /OWNERNAME=([^\&]*)\&/){
            $HcurrentOwnerName = cutColumn($1, $HlengthOwnerName*2);
        }

    } elsif ($line =~ /MessageButton([0-9]*)/) {
        $HmainMode = 'comment';
        $HcurrentID = $1;
        # メッセージ
        if ($line =~ /MESSAGE=([^\&]*)\&/){
            $Hmessage = cutColumn($1, $HlengthMessage*2);
        }

    } elsif ($line =~ /TotoButton([0-9]*)/) {
        $HmainMode = 'totoyoso';
        $HcurrentID = $1;
        # YOSO
        if ($line =~ /YOSOMESSAGE=([^\&]*)\&/) {
            $HyosoMessage[0] = cutColumn($1, $HlengthYoso*2);
        }

    } elsif ($line =~ /TotosButton([0-9]*)/) {
        $HmainMode = 'totoyoso2';
        $HcurrentID = $1;
        # YOSO2
        if($line =~ /YOSOMESSAGE2=([^\&]*)\&/) {
            $HyosoMessage[1] = cutColumn($1, $HlengthYoso*2);
        }

    } elsif($line =~ /ShutoButton([0-9]*)/) {
        $HmainMode = 'shuto';
        $HcurrentID = $1;
        # shuto
        if($line =~ /SHUTOMESSAGE=([^\&]*)\&/) {
            $HshutoMessage = cutColumn($1, $HlengthShuto*2);
        }

    } elsif($line =~ /TeamButton([0-9]*)/) {
        $HmainMode = 'teamname';
        $HcurrentID = $1;
        # team
        if($line =~ /TEAMMESSAGE=([^\&]*)\&/) {
            $HteamMessage = cutColumn($1, $HlengthTeam*2);
        }

    } elsif($line =~ /YakuWorkButton([0-9]*)/) {
        $HmainMode = 'yaku_chg';
        $HcurrentID = $1;

        $HYaku_Chg_Yotei = 0;
        if($line =~ /YAKU_YOTEI=([^\&]*)*/) {
            $HYaku_Chg_Yotei = 1;
        }
        $HYaku_Chg_Narasi = 0;
        if($line =~ /YAKU_NARASI=([^\&]*)*/) {
            $HYaku_Chg_Narasi = 1;
        }

    } elsif($line =~ /PreabButton([0-9]*)/) {
        $HmainMode = 'preab';
        $HcurrentID = $1;

    } elsif($getLine =~ /View=([0-9]*)/) {
        $HmainMode = 'top';
        $HviewIslandNumber = $1;

    } elsif($getLine =~ /IslandMap=([0-9]*)/) {
        $HmainMode = 'landmap';
        $HcurrentID = $1;
        # 自島の取得
        if ($getLine =~ /FROM_ISLAND=([0-9]*)/) {
            our $HmyislandID = $1;
        }

    } elsif($getLine =~ /TaijiList=([0-9]*)/) {
        $HmainMode = 'taijilist';
        $HcurrentID = $1;

    } elsif($getLine =~ /JoinA=([^\&]*)/) {
        $HmainMode = 'joinally';
        $HdefaultPassword = $1;

    } elsif($line =~ /NewAllyButton/) {
        $HmainMode = 'newally';
        # 同盟名の取得
        if($line =~ /ALLYNUMBER=([0-9]*)\&/) {
            $HcurrentAnumber = $1;
        }
        if($line =~ /ALLYID=([0-9]*)\&/) {
            $HallyID = $1;
        }
        $line =~ /ALLYNAME=([^\&]*)\&/;
        $HallyName = cutColumn($1, $HlengthAllyName*2);
        $line =~ /MARK=([^\&]*)\&/;
        $HallyMark = $1;
        $line =~ /COLOR1=([0-9A-F])\&COLOR2=([0-9A-F])\&COLOR3=([0-9A-F])\&COLOR4=([0-9A-F])\&COLOR5=([0-9A-F])\&COLOR6=([0-9A-F])\&/;
        our $HallyColor = $1 . $2 . $3 . $ 4 . $5 . $6;

    } elsif($line =~ /DeleteAllyButton/) {
        $HmainMode = 'delally';
        if($line =~ /ALLYID=([0-9]*)\&/) {
            $HallyID = $1;
        }
        $line =~ /ALLYNUMBER=([0-9]*)\&/;
        $HcurrentAnumber = $1;

    } elsif($line =~ /JoinAllyButton/) {
        $HmainMode = 'inoutally';
        $line =~ /ALLYNUMBER=([0-9]*)\&/;
        $HcurrentAnumber = $1;

    } elsif($getLine =~ /AmiOfAlly=([0-9]*)/) {
        $HmainMode = 'aoa';
        $HallyID = $1;

    } elsif($getLine =~ /Allypact=([^\&]*)/) {
        # 盟主コメントモード
        # 最初の起動
        $HmainMode = 'allypact';
        $HallyPactMode = 0;
        $HcurrentID = $1;

    } elsif ($line =~ /CAMPCHAT=([0-9]*)/) {
        $HtempBack = "<A href=\"Javascript:void(0);\" onclick=\"window.open('about:blank','_self').close()\"><span class='big'>[閉じる]</span></A>";
        $HmainMode = 'campCHAT';
        $HcurrentCampID = $1;
        if($line =~ /PASSWORD=([^\&]*)\&/) {
            $HinputPassword = $1;
            $HdefaultPassword = $1;
        }
        if($line =~ /jpass=([a-zA-Z0-9]*)/) {
            $HcampPassward = $1; # 陣営パスワード
        }
        if($line =~ /id=([0-9]*)/) {
            $HcurrentID = $1;
        }
        $line =~ /LBBSNAME=([^\&]*)\&/;
        $HlbbsName = cutColumn($1, $HlengthLbbsName*2);
        $HdefaultName = $HlbbsName;
        $line =~ /LBBSMESSAGE=([^\&]*)\&/;
        $HlbbsMessage = cutColumn($1, $HlengthLbbsMessage*2);
        $line =~ /wturn=([0-9]*)\&/;
        $Hlbbsturn = $1;
        $line =~ /wislandname=([^\&]*)\&/;
        $Hlbbssendisland = $1;

        $HAnoSend = 0;
        if ($line =~ /SENDALLY=([a-zA-Z0-9]*)/) {
            if ( $HcurrentCampID != int($1) ) {
                $HAnoSendto = int($1);
                $HAnoSend = 1;
            }
        }

        if ( $HlbbsMessage eq '' ) {
            $HmainMode = 'camp';
        }

    } elsif ($line =~ /camp=([0-9]*)/) {
        $HtempBack = "<A href=\"Javascript:void(0);\" onclick=\"window.open('about:blank','_self').close()\"><span class='big'>[閉じる]</span></A>";
        $HmainMode = 'camp';
        $HcurrentCampID = $1;
        if($line =~ /PASSWORD=([^\&]*)\&/) {
            $HinputPassword = $1;
            $HdefaultPassword = $1;
        }
        if($line =~ /jpass=([a-zA-Z0-9]*)/) {
            $HcampPassward = $1; # 陣営パスワード
        }
        if($line =~ /id=([0-9]*)/) {
            $HcurrentID = $1;
        }

    } elsif($getLine =~ /Rank=([0-9]*)/) {
        $HmainMode = 'rank';

    } elsif($getLine =~ /BF_point=([0-9]*)/) {
        $HmainMode = 'bf_point';

    } elsif($getLine =~ /Rename=([0-9]*)/) {
        $HmainMode = 'rename';

    } elsif($getLine =~ /Join=([0-9]*)/) {
        # 誰でも新しい島を探せる
        $HmainMode = ($HadminJoinOnly ? 'top' : 'join');

    } elsif($line =~ /Join=([0-9]*)/) {
        # 管理人だけが新しい島を探せる
        $HmainMode = ($HadminJoinOnly ? 'join' : 'top');

    }
    elsif ($line =~ /NewIslandButton/) {

        $HmainMode = 'new';
        # 名前の取得
        $line =~ /ISLANDNAME=([^\&]*)\&/;
        $HcurrentName = cutColumn($1, $HlengthIslandName*2);
        # オーナー名の取得
        $line =~ /OWNERNAME=([^\&]*)\&/;
        $HcurrentOwnerName = cutColumn($1, $HlengthOwnerName*2);
        if (   ($HarmisticeTurn)
            && ($HcampSelectRule == 2) ) {

            # 陣営を選択可能な場合
            if ($line =~ /CAMPNUMBER=([\-]?[0-9]+)\&/) {
                $HcampNumber = $1;
            }
        }

    } elsif($getLine =~ /ASetup=([^\&]*)/) {        # 同盟設定確認モード
        $HmainMode = 'asetup';
        $HasetupMode = 0;
        $HdefaultPassword = $1;
    } elsif($line =~ /ASetup=([^\&]*)\&/) {
        # 変更ボタンが押された起動
        $HmainMode = 'asetup';
        $HasetupMode = 1;
        $HdefaultPassword = $1;
        while ($line =~/amity=([^\&]*)\&/g) {
            push(@HamityChange, $1);
        }
        while ($line =~/ally=([^\&]*)\&/g) {
            push(@HallyChange, $1);
        }

        # BattleField作成モード
    } elsif($getLine =~ /Bfield=([^\&]*)/) {    
        # 最初の起動
        $HmainMode = 'bfield';
        $HbfieldMode = 0;
        $HdefaultPassword = $1;
    } elsif($line =~ /Bfield=([^\&]*)\&/) {
        # BattleField作成ボタンが押された起動
        $HmainMode = 'bfield';
        $HbfieldMode = 1;
        $HdefaultPassword = $1;

    } elsif($getLine =~ /Present/) {                # 管理人によるプレゼントモード起動
        # 最初の起動
        $HmainMode = 'present';
        $HpresentMode = 0;
    } elsif($line =~ /Present/) {                   # プレゼントボタンが押された起動

        $HmainMode = 'present';
        $HpresentMode = 1;
        ($HpresentMoney) = ($line =~ /PRESENTMONEY=([^\&]*)\&/);
        ($HpresentFood ) = ($line =~ /PRESENTFOOD=([^\&]*)\&/);
        $line =~ /PRESENTLOG=([^\&]*)\&/;
        $HpresentLog   = cutColumn($1, $HlengthPresentLog*2);

    } elsif($getLine =~ /Punish=([^\&]*)/) {        # 管理人による制裁モード
        # 最初の起動
        $HmainMode = 'punish';
        $HpunishMode = 0;
        $HdefaultPassword = $1;
    } elsif($line =~ /Punish=([^\&]*)\&/) {         # 制裁ボタンが押された起動

        $HmainMode = 'punish';
        $HpunishMode = 1;
        $HdefaultPassword = $1;

        $line =~ /POINTX=([^\&]*)\&/;
        $HcommandX = $1;
        $HdefaultX = $1;
        $line =~ /POINTY=([^\&]*)\&/;
        $HcommandY = $1;
        $HdefaultY = $1;
        $line =~ /PUNISHID=([^\&]*)\&/;
        $HpunishID = $1;

    } elsif($getLine =~ /Lchange=([^\&]*)/) {   # 管理人による地形変更モード
        # 最初の起動
        $HmainMode = 'lchange';
        $HlchangeMode = 0;
        $HdefaultPassword = $1;

    } elsif($line =~ /Lchange=([^\&]*)\&/) {    # 管理人による地形変更モード 変更ボタンが押された起動

        $HmainMode = 'lchange';
        $HlchangeMode = 1;
        $HdefaultPassword = $1;
        $line =~ /POINTX=([^\&]*)\&/;
        our ($HcommandX) = $1;
        $HdefaultX = $1;
        $line =~ /POINTY=([^\&]*)\&/;
        our ($HcommandY) = $1;
        $HdefaultY = $1;
        $line =~ /LCHANGEKIND=([^\&]*)\&/;
        our ($HlchangeKIND) = $1;
        $line =~ /LCHANGEVALUE=([^\&]*)\&/;
        our ($HlchangeVALUE) = $1;
        $line =~ /LCHANGEVALUE2=([^\&]*)\&/;
        our ($HlchangeVALUE2) = $1;
        $line =~ /LCHANGEVALUE3=([^\&]*)\&/;
        our ($HlchangeVALUE3) = $1;

    } elsif($getLine =~ /Pdelete=([^\&]*)/) {   # 管理人によるあずかりモード
        # 最初の起動
        $HmainMode = 'predelete';
        $HpreDeleteMode = 0;
        $HdefaultPassword = $1;

    } elsif($line =~ /Pdelete=([^\&]*)\&/) {    # 変更ボタンが押された起動

        $HmainMode = 'predelete';
        $HpreDeleteMode = 1;
        $HdefaultPassword = $1;

    } elsif($getLine =~ /HCdata=([0-9]*)/) {
        $HmainMode = 'hcdata';

    } elsif($getLine =~ /Rekidai=([0-9]*)/) {       # 歴代最多人口記録
        $HmainMode = 'rekidai';

    } else {

        $HmainMode = 'top';
    }
}

#cookie入力
sub cookieInput {
    my ($cookie);

#   $cookie = jcode::euc($ENV{'HTTP_COOKIE'});
    $cookie = $ENV{'HTTP_COOKIE'};

    if($cookie =~ /${HthisFile}OWNISLANDID=\(([^\)]*)\)/) {
        $defaultID = $1;
        $init_ID = $defaultID;
    }
    if($cookie =~ /${HthisFile}OWNISLANDPASSWORD=\(([^\)]*)\)/) {
        $HdefaultPassword = $1;             # cookie
    }
    if($cookie =~ /${HthisFile}TARGETISLANDID=\(([^\)]*)\)/) {
        $defaultTarget = $1;
    }
    if($cookie =~ /${HthisFile}LBBSNAME=\(([^\)]*)\)/) {
        $HdefaultName = $1;
    }
    if($cookie =~ /${HthisFile}POINTX=\(([^\)]*)\)/) {
        $HdefaultX = $1;
    }
    if($cookie =~ /${HthisFile}POINTY=\(([^\)]*)\)/) {
        $HdefaultY = $1;
    }
    if($cookie =~ /${HthisFile}KIND=\(([^\)]*)\)/) {
        $HdefaultKind = $1;
    }
    if($cookie =~ /${HthisFile}JAVAMODESET=\(([^\)]*)\)/) {
        $HjavaModeSet = $1;
    }

    if($cookie =~ /${HthisFile}IMGLINE=\(([^\)]*)\)/) {
        $HimgLine = $1;
    }

    # wiiU 救済措置
    if($access eq 'WiiU'){
        $init_ID = $rqID if($rqID > -1);
        $HjavaModeSet = $wiiU_javamode;
        $HdefaultPassword = $wiiU_password;
        $HjavaModeSet = 'java' if ( $HjavaModeSet eq '');
    }

}


#----------------------------------------------------------------------
#cookie出力
sub cookieOutput {
    my ($cookie, $info);

    # 消える期限の設定
    my ($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) = gmtime(time + 30 * 86400); # 現在 + 30日

    # 2ケタ化
    $year += 1900;
    $date = "0$date" if($date < 10);
    $hour = "0$hour" if($hour < 10);
    $min  = "0$min" if($min < 10);
    $sec  = "0$sec" if($sec < 10);

    # 曜日を文字に
    $day = ("Sunday", "Monday", "Tuesday", "Wednesday",    "Thursday", "Friday", "Saturday")[$day];

    # 月を文字に
    $mon = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")[$mon];

    # パスと期限のセット
    $info = "; expires=$day, $date\-$mon\-$year $hour:$min:$sec GMT\n";
    $cookie = '';

    if (($HcurrentID) && ($HmainMode eq 'owner')){
        $cookie .= "Set-Cookie: ${HthisFile}OWNISLANDID=($HcurrentID) $info";
    }
    if ($HinputPassword) {
        $cookie .= "Set-Cookie: ${HthisFile}OWNISLANDPASSWORD=($HinputPassword) $info";
    }
    if ($HcommandTarget) {
        $cookie .= "Set-Cookie: ${HthisFile}TARGETISLANDID=($HcommandTarget) $info";
    }
    if ($HlbbsName) {
        $cookie .= "Set-Cookie: ${HthisFile}LBBSNAME=($HlbbsName) $info";
    }
    if ($HcommandX) {
        $cookie .= "Set-Cookie: ${HthisFile}POINTX=($HcommandX) $info";
    }
    if ($HcommandY) {
        $cookie .= "Set-Cookie: ${HthisFile}POINTY=($HcommandY) $info";
    }
    if ($HcommandKind) {
        # 自動系以外
        $cookie .= "Set-Cookie: ${HthisFile}KIND=($HcommandKind) $info";
    }
    if ($HjavaMode) {
        $cookie .= "Set-Cookie: ${HthisFile}JAVAMODESET=($HjavaMode) $info";
    }
    if ($HimgLine) {
        $cookie .= "Set-Cookie: ${HthisFile}IMGLINE=($HimgLine) $info";
    }

    out($cookie);
}


#----------------------------------------------------------------------
# wiiU アクセス用
#----------------------------------------------------------------------
sub wiiU_ip_check {

    my ($agent) = $ENV{'HTTP_USER_AGENT'};
    my ($line) = "";

    if (   (0)
        || ( index($agent , '(Nintendo WiiU)') > 5 )
        || ( index($agent , '(Nintendo 3DS;') > 5 )
        || ( index($agent , 'New Nintendo 3DS') > 5 ) ) {

        $access ='WiiU';
        open IDFILE, $WiiUaxesFile;
        while ($line =<IDFILE>) {

            $line =~ /^(.+)to([^,]+),([^,]+),([^,]+)/;
            if ( $ENV{'REMOTE_ADDR'} eq $1 ) {
                $rqID = $2;
                $wiiU_javamode = $3;
                $wiiU_password = $4;
                last;
            }
        }
        close(IDFILE);
    }

    return $rqID;
}


#----------------------------------------------------------------------
sub GetNumberSelectNum {
    my ($name , $line) = @_;

    my ($ret) = '';
    my ($k);
    for ($k = 0; $k < 9; $k++) {
        if ($line =~ /$name$k=([0-9]*)/) {
            $ret .= $1;
        }
    }
    return ($ret);
}


#----------------------------------------------------------------------
#commandJavaMain
#----------------------------------------------------------------------
sub wiiU_ip_check_write {
    my ($number) = @_;
    my ($agent) = $ENV{'HTTP_USER_AGENT'};
    my ($line) = "";
    my ($tempjava) = "";
    my ($temppass) = "";

    if (  (0) 
        || ( index($agent , '(Nintendo WiiU)') > 5 )
        || ( index($agent , '(Nintendo 3DS;') > 5 )
        || ( index($agent , 'New Nintendo 3DS') > 5 ) ) {

        open IDFILE, $WiiUaxesFile;
        while($line = <IDFILE>) {
            $line =~ /^(.+)to([^,]*),([^,]*),([^,]*)/;
            if ( $ENV{'REMOTE_ADDR'} eq $1 ){
                $rqID = $2;
                $tempjava = $3;
                $temppass = $4;
                last;
            }
        }
        close(IDFILE);

        if (   ($rqID == -1)
            || ($number != $rqID)
            || ($HjavaMode ne $tempjava)
            || ($temppass ne $HinputPassword)
                                ){
            open(IDFILE, "$WiiUaxesFile");
            my @lines = <IDFILE>;
            while (100 <= @lines) { pop @lines; }
            close(IDFILE);
            unshift(@lines, "$ENV{'REMOTE_ADDR'}to$number,$HjavaMode,$HinputPassword,$rqID - $tempjava - $temppass\n");

            open(IDFILE, ">$WiiUaxesFile");
            foreach $line (@lines) {
                print IDFILE $line;
            }
            close(IDFILE);
        }

        chmod(0777,$WiiUaxesFile);
    }
}


#----------------------------------------------------------------------
# ユーティリティ
#----------------------------------------------------------------------
sub hakolock {
    if ($server_config::HlockMode == 1) {
        # directory式ロック
        return hakolock1();

    } elsif($server_config::HlockMode == 2) {
        # flock式ロック
        return hakolock2();
    } elsif($server_config::HlockMode == 3) {
        # symlink式ロック
        return hakolock3();
    } else {
        # 通常ファイル式ロック
        return hakolock4();
    }
}


sub hakolock1 {
    # ロックを試す
    if (mkdir('hakojimalock', $HdirMode)) {
        # 成功
        return 1;
    } else {
        # 失敗
        my ($b) = (stat('hakojimalock'))[9];
        if (($b > 0) && ((time() -  $b)> MAIN_UNLOCK_TIME)) {
            # 強制解除
            unlock();

            # ヘッダ出力
            tempHeader();

            # 強制解除メッセージ
            tempUnlock();

            # フッタ出力
            tempFooter();

            # 終了
            exit(0);
        }
        return 0;
    }
}


sub hakolock2 {
    open(LOCKID, '>>hakojimalockflock');
    if (flock(LOCKID, 2)) {
        # 成功
        return 1;
    }
    else {
        # 失敗
        return 0;
    }
}


sub hakolock3 {
    # ロックを試す
    if (symlink('hakojimalockdummy', 'hakojimalock')) {
        # 成功
        return 1;
    }
    else {
        # 失敗
        my ($b) = (lstat('hakojimalock'))[9];
        if (($b > 0) && ((time() -  $b)> MAIN_UNLOCK_TIME)) {

            unlock();       # 強制解除
            tempHeader();   # ヘッダ出力
            tempUnlock();   # 強制解除メッセージ
            tempFooter();   # フッタ出力
            exit(0);
        }
        return 0;
    }
}

sub hakolock4 {
    # ロックを試す
    if (unlink('key-free')) {
        # 成功
        open(OUT, '>key-locked');
        print OUT time;
        close(OUT);
        return 1;
    }
    else {
        # ロック時間チェック
        if (!open(IN, 'key-locked')) {
            return 0;
        }

        my ($t);
        $t = <IN>;
        close(IN);
        if (   ($t != 0)
            && (($t + MAIN_UNLOCK_TIME) < time)) {

            unlock();          # 120秒以上経過してたら、強制的にロックを外す
            tempHeader();      # ヘッダ出力
            tempUnlock();      # 強制解除メッセージ
            tempFooter();      # フッタ出力
            exit(0);
        }
        return 0;
    }
}


#----------------------------------------------------------------------
# ロックを外す
#----------------------------------------------------------------------
sub unlock {
    if ($server_config::HlockMode == 1) {
        # directory式ロック
        rmdir('hakojimalock');

    } elsif ($server_config::HlockMode == 2) {
        # flock式ロック
        close(LOCKID);

    } elsif ($server_config::HlockMode == 3) {
        # symlink式ロック
        unlink('hakojimalock');
    } else {
        # 通常ファイル式ロック
        my ($i);
        $i = rename('key-locked', 'key-free');
    }
}


#----------------------------------------------------------------------
# 小さい方を返す
sub min {
    return ($_[0] < $_[1]) ? $_[0] : $_[1];
}


#----------------------------------------------------------------------
# 大きいほうを返す
sub max {
    return ($_[0] >= $_[1]) ? $_[0] : $_[1];
}

#----------------------------------------------------------------------
# パスワードエンコード
sub encode {
    if ($cryptOn == 1) {
        return crypt($_[0], 'h2');
    } else {
        return $_[0];
    }
}

#----------------------------------------------------------------------
# 1000億単位丸めルーチン
sub aboutMoney {
    my ($m) = @_;

    my ($order) = 10 ** (INIT_HIDE_MONEY_MODE - 2);
    my ($money);

    if ($m < 500 * $order) {
        $money = 500 * $order;
        return "推定${money}${HunitMoney}未満";
    }
    else {
        $m = int(($m + 500 * $order) / (1000 * $order));
        $money = $m * 1000 * $order;
        return "推定${money}${HunitMoney}";
    }
}

#----------------------------------------------------------------------
# 10発単位丸めルーチン
sub aboutMissile {
    my ($m) = @_;

    if ($m < 5) {
        return "推定10${HunitMissile}未満";
    }
    else {
        $m = int(($m + 5) / 10);
        return "推定${m}0${HunitMissile}";
    }
}


# ---------------------------------------------------------------------
sub Get_ZooState {
    my ($island) = @_;

    my ($tmp);
    my (@mons_list);

    $tmp = $island->{'zoo'};
    chomp($tmp);

    @mons_list = split(/\,/,$tmp);

    my ($kazu) = 0;
    my ($zookazu) = 0;
    my ($zookazus) = 0;
    my ($mshurui) = 0;
    my ($mkind) = 0;

    foreach $kazu (@mons_list) {

        $zookazu  += $kazu;
        $zookazus += $kazu * $HmonsterZooMoney[$mkind];  # $parは設定怪獣ごとにする
        if ($kazu > 0) {
            $mshurui++;
        }
        $mkind++;
    }

    return ($zookazu, $zookazus, $mshurui);
}


#----------------------------------------------------------------------
# エスケープ文字の処理
#----------------------------------------------------------------------
sub htmlEscape {
    my ($s, $mode) = @_;
    $s =~ s/&/&amp;/g;
    $s =~ s/</&lt;/g;
    $s =~ s/>/&gt;/g;
    $s =~ s/\"/&quot;/g; #"

    if ($mode) {
        $s =~ s/\r\n/<br>/g;
        $s =~ s/\r/<br>/g;
        $s =~ s/\n/<br>/g;
        $s =~ s/(<br>){5,}//g; # 大量改行対策
    }
    return $s;
}

#----------------------------------------------------------------------
# 80ケタに切り揃え
#----------------------------------------------------------------------
sub cutColumn {
    my ($s, $c) = @_;
    jcode::convert(\$s, 'euc');
    if (length($s) <= $c) {
        return $s;
    }
    else {

        if ($HlengthAlert) {
            unlock();
            tempHeader();
            tempWrong("文字数オーバーです！");
            tempFooter();
            exit(0);
        }
        # 合計80ケタになるまで切り取り
        my ($ss) = '';
        my ($count) = 0;
        while ($count < $c) {
            $s =~ s/(^[\x80-\xFF][\x80-\xFF])|(^[\x00-\x7F])//;
            if ($1) {

                $ss .= $1;
                $count ++;
            }
            else {

                $ss .= $2;
            }
            $count ++;
        }
        return $ss;
    }
}


# ---------------------------------------------------------------------
# 怪獣硬化
# ---------------------------------------------------------------------
sub isMonsterCuring {
    my ($kind) = @_;
    my ($special) = $HmonsterSpecial[$kind];

    if (   (($special == 3) && ($HislandTurn % 2))
        || (($special == 8) && !(seqnum($HislandTurn) % 2))
        || (($special == 4) && !($HislandTurn % 2))
        || (($kind == $Mons_Kisinhei) && !(seqnum2($HislandTurn, 12) % 2))
                                                             ) {
        # 硬化中
        return 1;
    }
    return 0;
}


#----------------------------------------------------------------------
# 防衛基地のHP
#----------------------------------------------------------------------
sub GetDefenceSpec {
    my ($lv) = @_;
    my ($defLevel , $defHP);

    $defLevel = $lv & $HDefenceLevelMask;
    $defHP = $lv >> $HDefenceHP_SHIFT;

    return ($defLevel , $defHP);
}


#----------------------------------------------------------------------
# 怪獣の情報
#----------------------------------------------------------------------
sub monsterSpec {
    my ($lv) = @_;

    my ($kind) = ($lv >> $Mons_Kind_Shift) & $Mons_Kind_MASK;

    my ($name);
    $name = $HmonsterName[$kind];

    my ($hp) = ($lv & $Mons_HP_MASK);

    return ($kind, $name, $hp);
}


#----------------------------------------------------------------------
# 怪獣の情報
#----------------------------------------------------------------------
sub GetmonsterKind {
    my ($lv) = @_;

    # 種類
    my ($kind) = ($lv >> $Mons_Kind_Shift) & $Mons_Kind_MASK;

    return ($kind);
}


#----------------------------------------------------------------------
# 経験地からレベルを算出
#----------------------------------------------------------------------
sub expToLevel {
    my ($kind, $exp) = @_;
    my ($i);
    if ($kind == $HlandBase) {
        # ミサイル基地
        for ($i = $maxBaseLevel; $i > 1; $i--) {
            if ($exp >= $baseLevelUp[$i - 2]) {
                return $i;
            }
        }
        return 1;
    }
    else {
        # 海底基地
        for ($i = $maxSBaseLevel; $i > 1; $i--) {
            if ($exp >= $sBaseLevelUp[$i - 2]) {
                return $i;
            }
        }
        return 1;
    }
}


#----------------------------------------------------------------------
# (0,0)から(size - 1, size - 1)までの数字が一回づつ出てくるように
# (@Hrpx, @Hrpy)を設定
#----------------------------------------------------------------------
sub makeRandomPointArray {
    # 初期値
    my ($y);
    @Hrpx = (0..$islandSize) x $HislandSize;
    foreach $y (0..$islandSize) {
        push(@Hrpy, ($y) x $HislandSize);
    }

    # シャッフル
    my ($i, $j);
    for ($i = $HpointNumber; --$i; ) {
        $j = int(rand($i+1));
        next if($i == $j);
        @Hrpx[$i,$j] = @Hrpx[$j,$i];
        @Hrpy[$i,$j] = @Hrpy[$j,$i];
    }
}


#----------------------------------------------------------------------
sub Calc_HouseLevel {
    my ($pts) = @_;

    my ($hlv) = 0;
    foreach (0..9) {
        $hlv = 9 - $_;
        last if($pts > $HouseLevel[$hlv]);
    }

    return ($hlv);
}


#----------------------------------------------------------------------
# 0から(n - 1)の乱数
#----------------------------------------------------------------------
sub random {
    return int(rand(1) * $_[0]);
}


#----------------------------------------------------------------------
# 与えた数値に対応する疑似乱数(0から9の整数のみ)
#----------------------------------------------------------------------
sub seqnum {
    my ($v) = sin($_[0] + 1234); # 1234 は任意の整数、乱数の系列を変える
    return (substr($v, -2, 1));
}


#----------------------------------------------------------------------
# 与えた数値に対応する疑似乱数(0から9の整数のみ)
#----------------------------------------------------------------------
sub seqnum2 {
    my ($v , $seed) = @_;
    $v = sin($v + $seed); # $seed は任意の整数、乱数の系列を変える
    return (substr($v, -2, 1));
}


#----------------------------------------------------------------------
# ソート
#----------------------------------------------------------------------
sub islandSort {
    my ($kind, $mode) = @_;

    # 人口が同じときは直前のターンの順番のまま
    my @idx = (0..$#Hislands);
    @idx = sort {
        $Hislands[$b]->{'field'} <=> $Hislands[$a]->{'field'} ||
        $Hislands[$a]->{'dead'} <=> $Hislands[$b]->{'dead'} || # 死滅フラグが立っていれば後ろへ
        $Hislands[$a]->{'predelete'} <=> $Hislands[$b]->{'predelete'} || # 預かりフラグが立っていれば後ろへ
        $Hislands[$b]->{$kind} <=> $Hislands[$a]->{$kind} ||
        $a <=> $b
    } @idx;
    @Hislands = @Hislands[@idx] if($kind eq 'pts');
    if ($mode) {
        my @Hidx;
        foreach (0..$#idx) {
            $Hidx[$idx[$_]] = $_;
        }
        while (my($k,$v) = each %HidToNumber){
            $HidToNumber{$k} = $Hidx[$v];
        }
    }

    return $Hislands[$idx[$HbfieldNumber]];
}


#----------------------------------------------------------------------
# 人口順にソート(同盟バージョン)
#----------------------------------------------------------------------
sub allySort {
    # 人口が同じときは直前のターンの順番のまま
    my @idx = (0..$#Hally);
    @idx = sort {
            $Hally[$a]->{'dead'} <=> $Hally[$b]->{'dead'} || # 死滅フラグが立っていれば後ろへ
            $Hally[$b]->{'score'} <=> $Hally[$a]->{'score'} ||
            $a <=> $b
           } @idx;
    @Hally = @Hally[@idx];
    my @Hidx;
    foreach (0..$#idx) {
        $Hidx[$idx[$_]] = $_;
    }
    while (my($k,$v) = each %HidToAllyNumber){
        $HidToAllyNumber{$k} = $Hidx[$v];
    }
}


#----------------------------------------------------------------------
# ログ表示
#----------------------------------------------------------------------
# ファイル番号指定でログ表示
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
            if (   ($mode == 0)
                || ($id1 != $id) ) {
                # 機密表示権利なし
                next;
            }
            $m = '<B>(機密)</B>:';
        }
        else {
            $m = '';
        }

        # 表示的確か
        if ($id != 0) {
            if (   ($id != $id1)
                && ($id != $id2) ) {
                next;
            }
        }

        if (!$set_turn){
            out("<b>=====[<span class='number'><font size='4'> ターン$turn </font></span>]================================================</b><br>\n");
            $set_turn++;
        }
        out("　${m}$message<BR>\n");
    }
    close(LIN);
}


#----------------------------------------------------------------------
# テンプレート
#----------------------------------------------------------------------
# 初期化
sub tempInitialize {
    my ($mode) = @_;
    # 島セレクト(デフォルト自分)
    $HislandList = getIslandList($init_ID, $mode);
    $HtargetList = getIslandList($defaultTarget, $mode);
}


#----------------------------------------------------------------------
# 島データのプルダウンメニュー用
sub getIslandList {
    my ($select, $mode) = @_;
    my ($list, $name, $id, $s, $i,$island);

    #島リストのメニュー
    $list = '';
    my ($predel);
    foreach $i (0..$islandNumber) {
        $island = $Hislands[$i];
        $predel = ($island->{'predelete'}) ? '[預]' : '';
        $name = islandName($island);
        $name =~ s/<[^<]*>//g;
        $id = $island->{'id'};
        $s = ($id eq $select) ? 'SELECTED' : '';
        $list .= '<OPTION VALUE="'.$id.'" ' .$s. '>' . $predel . $name. "</option>\n" if($mode || ($id <=100));
    }
    return $list;
}


#----------------------------------------------------------------------
# ロック失敗
#----------------------------------------------------------------------
sub tempLockFail {
    # タイトル
    out(<<END);
<span class='big'>同時アクセスエラーです。<BR>
ブラウザの「戻る」ボタンを押し、<BR>
しばらく待ってから再度お試し下さい。</span>$HtempBack
END
}


#----------------------------------------------------------------------
# 強制解除
#----------------------------------------------------------------------
sub tempUnlock {
    # タイトル
    out(<<END);
<span class='big'>前回のアクセスが異常終了だったようです。<BR>
ロックを強制解除しました。</span>$HtempBack
END
}


#----------------------------------------------------------------------
# パスワードファイルがない
#----------------------------------------------------------------------
sub tempNoPasswordFile {
    out(<<END);
<span class='big'>パスワードファイルが開けません。</span>$HtempBack
END
}


#----------------------------------------------------------------------
# hakojima.datがない
#----------------------------------------------------------------------
sub tempNoDataFile {
    out(<<END);
<span class='big'>データファイルが開けません。</span>"${HdirName}/$HmainData"$HtempBack
END
}


#----------------------------------------------------------------------
# ID違いorローカル設定していないorクッキー設定していない
#----------------------------------------------------------------------
sub tempWrong {
    my($str) = @_;

    out(<<END);
<SCRIPT type="text/javascript">
<!--
function init(){
}
function SelectList(theForm){
}
//-->
</SCRIPT>
<span class='big'>$str</span>$HtempBack
END
}


#----------------------------------------------------------------------
# 何か問題発生
sub tempProblem {
    out(<<END);
<span class='big'>問題発生、とりあえず戻ってください。</span>$HtempBack
END
}


#----------------------------------------------------------------------
# ヘッダ
sub tempHeader {

    my ($mapsizeNumber) = $HidToNumber{$defaultID};
    $Hms1 = 16;
    $Hms2 = $Hms1 << 1;     # 2倍

    if ($server_config::HpathGzip == 1 && $ENV{'HTTP_ACCEPT_ENCODING'}=~/gzip/ ) {
        print qq{Content-type: text/html; charset=EUC-JP\n};
        print qq{Content-encoding: gzip\n\n};
        open(STDOUT,"| $HpathGzip/gzip -1 -c");
        print " " x 2048 if($ENV{HTTP_USER_AGENT}=~/MSIE/);
        print qq{<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\n\n};
#       print qq{<!DOCTYPE html>\n\n};
    }
    else {
        print qq{Content-type: text/html; charset=EUC-JP\n\n};
        print qq{<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\n\n};
#       print qq{<!DOCTYPE html>\n\n};
    }

    out(<<END);
<html lang="ja">
<head>
  <title>$Htitle</title>
  <meta http-equiv="Content-Type" CONTENT="text/html; charset=EUC-JP">
  <meta http-equiv="Expires" content="259200">
  <meta http-equiv="Content-Script-Type" content="text/javascript">
  <meta name="format-detection" content="telephone=no">
  <meta name="theme-color" content="#99FF99">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="og:type" content="website"/>
  <meta property="og:url" content="http://minimal97.mydns.jp:8123/hako/">
  <meta property="og:title" content="minimal97の箱庭諸島" />
  <meta property="og:description" content="minimal97が運営する無料ブラウザゲームです。" />
  <meta name="twitter:card" content="summary">
  <meta name="twitter:site" content="@minimal97">
  <meta name="twitter:creator" content="@minimal97" />
  <meta name="twitter:title" content="minimal97の箱庭諸島">
  <meta name="twitter:description" content="minimal97が運営する無料ブラウザゲームです。">
  <meta property="og:image" content="http://graphics8.nytimes.com/images/2011/12/08/technology/bits-newtwitter/bits-newtwitter-tmagArticle.jpg" />
  <base href="${baseIMG}/${seasonIMG}">
  <link rel="shortcut icon" href="./img/fav.ico">
  <link rel="stylesheet" type="text/css" href="${baseSKIN}">
  <style type="text/css">
img.maptile_ret {
  width: ${Hms2}px;
  height: ${Hms2}px;
  border: 0px;
  border-style:hidden;
  transform:scale(-1, 1);
}
  </style>
</head>
$Body
  <div id='BodySpecial'>
END
html_template::PrintHeader();
}

# フッタ
sub tempFooter {
    out(<<END);
<hr><div class='LinkFoot'>
$Hfooter
<br>
<small>
  <span class='Nret'><b>Hakoniwa R.A. JS.$versionInfo</b></span>
  <span class='Nret'><b>(based on 020610model)</b></span>
</small><br>
END
##### 追加 親方20020307
    if (USE_PERFORMANCE) {
        my ($uti, $sti, $cuti, $csti) = times();
        $uti += $cuti;
        $sti += $csti;
        my ($cpu) = $uti + $sti;
        my ($timea) = sprintf("%.5f",Time::HiRes::time - $Hakoniwa_start_time);
    #       ログファイル書き出し(テスト計測用　普段はコメントにしておいてください)
    #       open(POUT,">>cpu-h.log");
    #       print POUT "CPU($cpu) : user($uti) system($sti)\n";
    #       close(POUT);
        out(<<END);
<small>CPU($cpu): user($uti) system($sti) /t:$timea
(
END
system("/bin/ps -o rss -e -q $$");
    out(<<END);
kb)</small>
END
    }
#####
    out(<<END);
</body>
</html>
END
}



