#!/usr/bin/perl
# ���ϥ����С��˹�碌���ѹ����Ʋ�������
# perl5�ѤǤ���
# Hakoniwa R.A. JS.(based on 020610model)
my ($versionInfo) = "version4.49";        #�����⤦���Ƥ��Ƥʤ�������
#----------------------------------------------------------------------
# Ȣ����� ver2.30
# �ᥤ�󥹥���ץ�(ver1.02)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# Hakoniwa R.A. ver2.11
# �ᥤ�󥹥���ץ�(Ȣ����� ver2.30)
# ���Ѿ�������ˡ���ϡ�read-renas.txt�ե�����򻲾�
#
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------
#use strict 'vars';
require "./html_template.pl";
BEGIN {
########################################
# ���顼ɽ��
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
# ��������ѥե�������ɤ߹���
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
# �ʲ������ߤˤ�ä����ꤹ����ʬ
#----------------------------------------------------------------------
# �۾ｪλ������
# (��å��岿�äǡ�����������뤫)
my ($unlockTime) = 120;
use constant MAIN_UNLOCK_TIME    => 120;

#----------------------------------------------------------------------
# ���ߤˤ�ä����ꤹ����ʬ�ϰʾ�
#----------------------------------------------------------------------


#----------------------------------------------------------------------
# ����ʹߤΥ�����ץȤϡ��ѹ�����뤳�Ȥ����ꤷ�Ƥ��ޤ��󤬡�
# �����äƤ⤫�ޤ��ޤ���
# ���ޥ�ɤ�̾�������ʤʤɤϲ��䤹���Ȼפ��ޤ���
#----------------------------------------------------------------------
my ($WiiUaxesFile) = 'ipfile.dat';
our ($debug_msg) = '';
our ($HAnoSend) = 0;
our ($HadminMode) = 0;

#----------------------------------------------------------------------
# �Ƽ����
#----------------------------------------------------------------------
# �Ϸ��ֹ�
require './hako-land_const.cgi';


# =============================================================================
# �ײ��ֹ������
# ���Ϸ�
our $HcomPrepare    = 01; #  1 ����
our $HcomPrepare2   = 02; #  2 �Ϥʤ餷
our $HcomReclaim    = 03; #  3 ���Ω��
our $HcomDestroy    = 04; #  4 ����
our $HcomSellTree   = 05; #  5 Ȳ��

our $HcomMinato     = 06; #  6 ����ȯ
our $HcomFune       = 07; #  7 ¤��
our $HcomSeki       = 10; #  8 �ؽ����

# ����
our $HcomPlant      = 11; #  9 ����
our $HcomFarm       = 12; # 10 ��������
our $HcomFactory    = 13; # 11 �������
our $HcomMountain   = 14; # 12 �η�������
our $HcomBase       = 15; # 13 �ߥ�������Ϸ���
our $HcomDbase      = 16; # 14 �ɱһ��߷���
our $HcomSbase      = 17; # 15 ������Ϸ���
our $HcomMonument   = 18; # 16 ��ǰ���¤
our $HcomHaribote   = 19; # 17 �ϥ�ܥ�����

our $HcomSeacity    = 20; # 18 �����ԻԷ���
our $HcomMonbuy     = 21; # 19 ���ù���
our $HcomMonbuyt    = 22; # 20 tetora����
our $HcomPark       = 23; # 21 ͷ���Ϸ���
our $HcomMine       = 24; # 22 ��������
our $HcomNursery    = 25; # 23 �ܿ�������
our $HcomKyujo      = 26; # 24 ����
our $HcomUmiamu     = 27; # 25 �����ߤ����
our $HcomFoodim     = 28; # 26 ��ʪ��������
our $HcomProcity    = 29; # 27 �ɺҲ�
our $HcomBoku       = 30; # 28 �ͤΰ��ۤ�

# ȯ�ͷ�
our $HcomMissileNM    = 31; # �ߥ�����ȯ��
our $HcomMissilePP    = 32; # PP�ߥ�����ȯ��
our $HcomMissileST    = 33; # ST�ߥ�����ȯ��
our $HcomMissileLD    = 34; # Φ���˲���ȯ��
our $HcomSendMonster  = 35; # �����ɸ�
our $HcomMissileSPP   = 36; # SPP�ߥ�����ȯ��
our $HcomMissileSS    = 37; # �˥ߥ�����ȯ��
our $HcomMissileLR    = 38; # �Ϸ�δ����ȯ��

# �͹�����ȯ��
our $HcomEisei      = 39; # �͹�����ȯ��
our $HcomEiseimente = 40; # �͹���������

# ���ķ�
our $HcomDoNothing  = 41; # ��ⷫ��
our $HcomSell       = 42; # ����͢��
our $HcomMoney      = 43; # �����
our $HcomFood       = 44; # �������
our $HcomPropaganda = 45; # Ͷ�׳�ư
our $HcomGiveup     = 46; # �������
our $HcomSave       = 47; # ��¸
our $HcomLoad       = 48; # ����
our $HcomAlly       = 49; # Ʊ��������æ��

our $HcomSendPirates = 50;  # ��±

our $HcomNewtown    = 70; # 29 �˥塼���������
our $HcomBigtown    = 71; # 30 �����ԻԷ���
our $HcomSeatown    = 72; # 31 ����˥塼����
our $HcomFarmcpc    = 73; # 32 �Ҿ����
our $HcomCollege    = 74; # ��ط���
our $HcomOnsen      = 75; # ��������
our $HcomReclaim2   = 76; # ���Υ���Ω��
our $HcomHouse      = 77; # ���β�
our $HcomRizort     = 78; # �꥾������
our $HcomBettown    = 79; # �������Ի�

our $HcomEiseiLzr   = 80; # �͹������졼����
our $HcomEiseiAtt   = 81; # �͹������˲�

our $HcomGivefood   = 100;  # �����򤢤���
our $HcomKai        = 101;  # ����
our $HcomHTget      = 102;  # �ϥ��ƥ����å�
our $HcomArmSupply  = 103;  # ����ʪ��Ĵã
our $HcomReclaim2dan = 105; # 2�ʳ����Ω��
our $HcomDestroy2   = 106;  # ��®����
our $HcomReclaim_spd = 107; # ��®���Ω��
our $HcomYotei      = 108;  # ͽ����
our $HcomBoku2      = 109;  # �ͤΰ��ۤ���
our $HcomYakusho    = 110;  # ���
our $HcomFire       = 111;  # ���ɽ����
our $HcomItemUse    = 112;  # �����ƥप��
our $HcomItemThrow  = 113;  # �����ƥ�ΤƤ�
our $HcomZoo        = 114;  # ưʪ�����

our $HcomMax = 114; #���ޥ��ɽ���Ѥξ��




# ��ư���Ϸ�
our $HcomAutoPrepare    = 200; # 51 �ե�����
our $HcomAutoPrepare2    = 201; # 52 �ե��Ϥʤ餷
our $HcomAutoDelete        = 202; # 53 �����ޥ�ɾõ�
our $HcomAutoReclaim    = 203; # 54 �������Ω��
our $HcomAutoDestroy    = 204; # 55 ��������
our $HcomAutoSellTree    = 205; # 56 Ȳ��
our $HcomAutoForestry    = 206; # 57 Ȳ�Τȿ���

our @HkindBFM = ($HcomMissileNM,
                 $HcomMissilePP,
                 $HcomMissileSPP,
                 $HcomMissileST,
                 $HcomMissileSS);

# ����
# ���ޥ�ɥꥹ�� �Ѵ���
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

# �����Ϥ�����ʤ��Ǥ�������
        my $addr    = $ENV{'REMOTE_ADDR'};
        foreach (@comList) {
            next if (($_ == $HcomAlly) && (!(ALLY_USE) || !$HallyJoinComUse || $HarmisticeTurn));
            next if (($_ == $HcomMissileST) && !$HuseMissileST);
            next if (($_ == $HcomSendMonster) && !INIT_USE_SEND_MONSTER);
            push(@HcomList, $_);
        }
    }
our $HcommandTotal = $#HcomList + 1; # ���ޥ�ɤμ���

# ���ޥ��ʬ��
# ���Υ��ޥ��ʬ������ϡ���ư���ϷϤΥ��ޥ�ɤ����ꤷ�ʤ��ǲ�������
# our @HcommandDivido = 
#    (
#    '����,41,50',   # �ײ��ֹ�41��50
#    '����,0,5',     # �ײ��ֹ�00��05
#    '����,11,19',   # �ײ��ֹ�11��19
#    '��ȯ,6,10',    # �ײ��ֹ�06��10
#    '�Ի�,70,79',   # �ײ��ֹ�70��75
#    '����,20,30',   # �ײ��ֹ�20��30
#    '����,39,40',   # �ײ��ֹ�39��40
#    '����,100,113', # �ײ��ֹ�100��105
#    '����,31,38',   # �ײ��ֹ�31��38
#    '����,80,85',   # �ײ��ֹ�80��85
#    );

# ���ޥ��ʬ��
# �����ʤ����ɡ��ҤȤޤ����ޥ�ɤ�����Ǥ��롣
# ɽ���ϡ�map�Υץ����Ǵ���������
our @HcommandDivido2 = 
    (
    "����,$HcomDoNothing,$HcomSell,$HcomMoney,$HcomFood"
       .",$HcomPropaganda,$HcomGiveup,$HcomSave,$HcomLoad"
       .",$HcomAlly",

    "����,$HcomPrepare,$HcomPrepare2,$HcomReclaim,$HcomReclaim2dan,$HcomReclaim2"
       .",$HcomDestroy,$HcomDestroy2,$HcomReclaim_spd"
       .",$HcomSellTree",

    "����,$HcomPlant,$HcomFarm"
       .",$HcomFactory,$HcomMountain"
       .",$HcomBase,$HcomDbase"
       .",$HcomSbase,$HcomMonument"
       .",$HcomHaribote",

    "��ȯ,$HcomMinato,$HcomFune"
       .",$HcomSeki",

    "�Ի�,$HcomNewtown,$HcomBigtown"
       .",$HcomSeatown,$HcomFarmcpc"
       .",$HcomCollege,$HcomOnsen"
       .",$HcomHouse"
       .",$HcomRizort,$HcomBettown",

    "����,$HcomSeacity,$HcomPark"
       .",$HcomMine,$HcomNursery"
       .",$HcomKyujo,$HcomUmiamu"
       .",$HcomFoodim,$HcomProcity"
       .",$HcomFire,$HcomZoo"
       .",$HcomMonbuy,$HcomMonbuyt",

    "����,$HcomEisei,$HcomEiseimente",

    "����,$HcomGivefood,$HcomKai"
       .",$HcomHTget,$HcomArmSupply"
       .",$HcomYotei,$HcomBoku"
       .",$HcomBoku2,$HcomYakusho"
       .",$HcomItemUse"
       .",$HcomItemThrow",

    "����,$HcomMissileNM,$HcomMissilePP"
       .",$HcomMissileST,$HcomMissileSPP"
       .",$HcomMissileLR,$HcomMissileSS"
       .",$HcomMissileLD,$HcomSendMonster,$HcomSendPirates",

    "����,$HcomEiseiLzr,$HcomEiseiAtt",
    );

# ��ư���Ϥ�Ǥ᤿���
# java script�Ǳ��˽ФƤ���
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

# �ײ��̾��������
# Pointx### �ˤ���ȡ��ݥ���Ȥˤʤ롣
our @HcomName;
our @HcomCost;

SetCommandData($HcomHouse       , '�������/��Ψ�ѹ�' , 'Pointx3');
SetCommandData($HcomBettown     , '�������ԻԷײ�'    , 'Pointx1');
SetCommandData($HcomKai         , '����������'        , 'Pointx1');
SetCommandData($HcomPrepare     , '����'              , 5);
SetCommandData($HcomYotei       , 'ͽ���ϳ���/���'   , 0);

SetCommandData($HcomPrepare2    , '�Ϥʤ餷'          , 100);
SetCommandData($HcomReclaim     , '���Ω��'          , 150);
SetCommandData($HcomReclaim2    , '���Υ���Ω��'    , 3000);
SetCommandData($HcomReclaim2dan , '2�����Ω��'       , 2000);
SetCommandData($HcomReclaim_spd , '��®���Ω��'      , 2450);
SetCommandData($HcomDestroy     , '����'              , 200);
SetCommandData($HcomDestroy2    , '��®����'          , 2000);

SetCommandData($HcomMinato      , '��Į��ȯ'          , 550);
SetCommandData($HcomOnsen       , '��������'          , 50);
SetCommandData($HcomFune        , '¤�����й�'        , 300);

SetCommandData($HcomSeki        , '�ؽ����'          , 200);
SetCommandData($HcomSellTree    , 'Ȳ��'              , 0);
SetCommandData($HcomPlant       , '����'              , 50);
SetCommandData($HcomFarm        , '��������'          , 20);
SetCommandData($HcomFoodim      , '��ʪ��������'    , 2500);

SetCommandData($HcomFarmcpc     , '�Ҿ����/��������' , 1500);
SetCommandData($HcomCollege     , '��ط���'          , 500);
SetCommandData($HcomFactory     , '�������'          , 100);
SetCommandData($HcomHTget       , '�ϥ��ƥ�����Ͷ��'  , 10000);

SetCommandData($HcomMountain    , '�η�������'        , 300);
SetCommandData($HcomBase        , '�ߥ�������Ϸ���'  , 300);
SetCommandData($HcomDbase       , '�ɱһ��߷���'      , 800);
SetCommandData($HcomSbase       , '������Ϸ���'      , 8000);
SetCommandData($HcomSeacity     , '�����ԻԷ���'      , 77777);
SetCommandData($HcomMonument    , '��ǰ���¤'        , 9999);
SetCommandData($HcomMonbuy      , '���äι���/����'   , 3980);
SetCommandData($HcomMonbuyt     , '�ƥȥ�ι���/����' , 10000);
SetCommandData($HcomHaribote    , '�ϥ�ܥ�����'      , 1);

SetCommandData($HcomMine        , '��������'          , 100);
SetCommandData($HcomPark        , 'ͷ���Ϸ���'        , 1000);
SetCommandData($HcomNursery     , '�ܿ�������'        , 50);
SetCommandData($HcomKyujo       , '�������'        , 1000);
SetCommandData($HcomUmiamu      , '�����ߤ����'      , 15000);
SetCommandData($HcomRizort      , '�꥾�����ϳ�ȯ'    , 40000);

SetCommandData($HcomProcity     , '�ɺ��ԻԲ�'        , 25000);
SetCommandData($HcomNewtown     , '�˥塼���������'  , 950);
SetCommandData($HcomBigtown     , '�����ԻԷ���'      , 45000);
SetCommandData($HcomSeatown     , '���쿷�ԻԷ���'    , 69800);
SetCommandData($HcomBoku        , '�ͤΰ��ۤ�'        , 1000);
SetCommandData($HcomBoku2       , '�ͤΰ��ۤ�2'       , 'Pointx4');

SetCommandData($HcomEisei       , '�͹������Ǥ��夲'  , 9999);
SetCommandData($HcomEiseimente  , '�͹���������'      , 5000);
SetCommandData($HcomEiseiAtt    , '�����˲�ˤȯ��'    , 49999);
SetCommandData($HcomEiseiLzr    , '�����졼����ȯ��'  , 39999);

SetCommandData($HcomMissileNM   , '�ߥ�����ȯ��'      , 20);
SetCommandData($HcomMissilePP   , 'PP�ߥ�����ȯ��'    , 50);
SetCommandData($HcomMissileSPP  , 'SPP�ߥ�����ȯ��'   , 1000);
SetCommandData($HcomMissileST   , 'ST�ߥ�����ȯ��'    , 50);
SetCommandData($HcomMissileLD   , 'Φ���˲���ȯ��'    , 100000);
SetCommandData($HcomMissileLR   , '�Ϸ�δ����ȯ��'     , 50000);
SetCommandData($HcomMissileSS   , '�˥ߥ�����ȯ��'     , 100000);

SetCommandData($HcomSendMonster , '�����ɸ�'           , 500);
SetCommandData($HcomSendPirates , '��±�ɸ�'           , 1500);

SetCommandData($HcomDoNothing   , '��ⷫ��'           , 0);
SetCommandData($HcomSell        , '����͢��'           , -100);
SetCommandData($HcomMoney       , '�����'           , 100);
SetCommandData($HcomFood        , '�������'           , -100);

SetCommandData($HcomPropaganda  , 'Ͷ�׳�ư'           , 1000);
SetCommandData($HcomGiveup      , "${AfterName}������" , 0);
SetCommandData($HcomGivefood    , '�����򤢤���'       , -50000);
SetCommandData($HcomYakusho     , '��������'         , 30000);
SetCommandData($HcomFire        , '���ɽ����'         , 600);

SetCommandData($HcomItemThrow   , '�����ƥ�ΤƤ�'     , 0);
SetCommandData($HcomItemUse     , '�����ƥप��'       , 0);

SetCommandData($HcomZoo         , 'ưʪ�����'         , 100000);
#- - - - - - - - - - - - - - - - - - - - - - - -
SetCommandData($HcomAutoPrepare  , '���ϼ�ư����'         , 0);
SetCommandData($HcomAutoPrepare2 , '�Ϥʤ餷��ư����'     , 0);
SetCommandData($HcomAutoDelete   , '���ײ�����ű��'     , 0);
SetCommandData($HcomAutoReclaim  , '�������Ω�Ƽ�ư����' , 0);
SetCommandData($HcomAutoDestroy  , '�������Ｋư����'     , 0);
SetCommandData($HcomAutoSellTree , 'Ȳ�μ�ư����'         , 0);
SetCommandData($HcomAutoForestry , 'Ȳ�Ρ����Ӽ�ư����'   , 0);

#- - - - - - - - - - - - - - - - - - - - - - - -
SetCommandData($HcomAlly , 'Ʊ���ز�����æ��' , 0);
SetCommandData($HcomSave , '���ε���'         , 100000);
SetCommandData($HcomLoad , '����˺��'         , 100000);

#----------------------------------------------------------------------
# �ѿ�
#----------------------------------------------------------------------

# COOKIE
our ($defaultID) = 0;       # ���̾��
our ($defaultTarget) = '';   # �������åȤ�̾��
our ($rqID) = -1;

my ($access) ='';
my ($wiiU_javamode) = 'java';
my ($wiiU_password) = '';
my ($init_ID) = 0;       #�����ɽ����ID

# ��κ�ɸ��
our $HpointNumber = $HislandSize * $HislandSize;
our $pointNumber = $HpointNumber - 1;

our $HtempBack;         # �����ץ��

# ��������
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

our $HDayEvent;             # ���٥����
our $HDayEvent_Edge;        # ���٥���� ���٥�ȴ�λ�ե饰

our $Hms1;                  # map������
our $Hms2;                  # map������

our $HislandTurn;           # �������

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

our $HplayNow;      # ������򹹿����ޤ���
our $HnextTime;     # �����󹹿�����

our ($Body) = '<body>';

#----------------------------------------------------------------------
# �ᥤ��
#----------------------------------------------------------------------
    # �����ץ��
    $HtempBack = "<a href=\"$HthisFile\"><span class='big'>�ȥåפ����</span></a>";
    $Body = '<body>';

    # ����ν����
    srand(time() ^ ($$ + ($$ << 15)));

    wiiU_ip_check();

    # COOKIE�ɤߤ���
    cookieInput();

    # CGI�ɤߤ���
    cgiInput();

    # ��å��򤫤���
    if (!$HsepTurnFlag && !hakolock()) {
        # ��å�����

        tempHeader();   # �إå�����
        tempLockFail(); # ��å����ԥ�å�����
        tempFooter();   # �եå�����
        exit(0);        # ��λ
    }

    if (-e $HpasswordFile) {
        # �ѥ���ɥե����뤬����
        open(PIN, "<$HpasswordFile") || die $!;
        chomp($HmasterPassword  = <PIN>); # �ޥ����ѥ���ɤ��ɤ߹���
        chomp($HspecialPassword = <PIN>); # �ü�ѥ���ɤ��ɤ߹���
        close(PIN);
    }
    else {

        unlock();
        tempHeader();
        tempNoPasswordFile();
        tempFooter();
        exit(0);
    }

    # ��ǡ������ɤߤ���
    if (readIslandsFile($HcurrentID) == 0) {

        unlock();
        tempHeader();
        tempNoDataFile();
        tempFooter();
        exit(0);
    }

    # �ƥ�ץ졼�Ȥ�����
    if (   ($HmainMode eq 'turn')
        || (   ($HmainMode eq 'top')
            && (!checkMasterPassword($HinputPassword)) ) ) {
        tempInitialize(0);
    }
    else {
        tempInitialize(1);
    }

    # COOKIE�ˤ��ID�����å�
    if ($HmainMode eq 'owner') {
        # ������������
        axeslog() if($HtopAxes >= 1);
        
        unless($ENV{'HTTP_COOKIE'}) {
            cookieOutput();                 # COOKIE��������줿���ɤ����񤭹��ߥ����å�
            next if($ENV{'HTTP_COOKIE'});   # �񤭹���OK
        # ���å�����ͭ���ˤ��Ƥ��ʤ�
        #    unlock();
        #    tempHeader();
        #    tempWrong("���å�����ͭ���ˤ��Ƥ���������");
        #    tempFooter();
        #    exit(0);
        }

        if ($checkID || $checkImg) {
            # id����������
            my ($pcheck) = checkPassword($Hislands[$HidToNumber{$HcurrentID}],$HinputPassword);
            my ($free) = 0;

            foreach (@freepass) {
                $free += 1 if(($_ == $defaultID) || ($_ == $HcurrentID));
            }
            my ($icheck) = !($checkID && ($HcurrentID != $defaultID) && $defaultID);
            my ($lcheck) = !($checkImg && ($HimgLine eq '' || $HimgLine eq $HimageDir));
            # �ѥ����
            if(($pcheck != 2) && ($free != 2) && (!$icheck || !$lcheck)) {
                # ���Ĥ����鿴���Ѥ˲���������ʤɤ� ($free != 2) ����ʬ�� !$free ���ѹ����Ʋ�������
                unlock();
                tempHeader();
                if(!$icheck) {

                    tempWrong("��ʬ����ʳ��ˤ�����ޤ���"); # ID�㤤
                }
                else {
                    tempWrong("�ֲ����Υ���������פ򤷤Ʋ�������"); # ���������ꤷ�Ƥ��ʤ�
                }
                tempFooter();
                exit(0);
            }
        }
    }

    # COOKIE����
    cookieOutput();

    # �إå�����
    if (   ($HmainMode eq 'commandJava')                            # ���ޥ�����ϥ⡼��
        || ($HmainMode eq 'command2')                               # ���ޥ�����ϥ⡼�ɡ�ver1.1����ɲá���ư����
        || (   ($HjavaMode eq 'java')
            && (   ($HmainMode eq 'owner')
                || ($HmainMode eq 'comment')                        # ���������ϥ⡼��
                || ($HmainMode eq 'totoyoso')                       # TOTOͽ�ۣ����ϥ⡼��
                || ($HmainMode eq 'totoyoso2')                      # TOTOͽ�ۣ����ϥ⡼��
                || ($HmainMode eq 'lbbs')                           # ���������ϥ⡼��
                || ($HmainMode eq 'shuto')                          # ����̾�ѹ��⡼��
                || ($HmainMode eq 'teamname')                       # ����̾�ѹ��⡼��
                || ($HmainMode eq 'yaku_chg')                       # ����̾�ѹ��⡼��
                || ($HmainMode eq 'preab')                          # �رĶ�Ʊ��ȯ�⡼��
                                                ) )
        || (0)) { 

        $Htitle_sub = ' �ޥå� ��ȯ';
        $Body = "<body onload=\"SelectList('');init()\">";
        require('./hako-map.cgi');

        # �إå�����
        tempHeaderJava();
        if($HmainMode eq 'commandJava') {           # ��ȯ�⡼��
            commandJavaMain();

        } elsif($HmainMode eq 'command2') {         # ��ȯ�⡼��2��ver1.1����ɲá���ư�ϥ��ޥ���ѡ�
            commandMain();

        } elsif($HmainMode eq 'comment') {          # ���������ϥ⡼��
            commentMain();

        } elsif($HmainMode eq 'totoyoso') {         # TOTOͽ�ۣ����ϥ⡼��
            totoInputMain(0);

        } elsif($HmainMode eq 'totoyoso2') {        # TOTOͽ�ۣ����ϥ⡼��
            totoInputMain(1);

        } elsif($HmainMode eq 'shuto') {            # ����̾�ѹ��⡼��
            require('./hako-map.cgi');
            shutoMain();

        } elsif($HmainMode eq 'teamname') {         # ����̾�ѹ��⡼��
            require('./hako-map.cgi');
            TeamMain();

        } elsif($HmainMode eq 'yaku_chg') {         # ����̾�ѹ��⡼��
            require('./hako-map.cgi');
            WorkChangeMain();

        } elsif($HmainMode eq 'preab') {            # �رĶ�Ʊ��ȯ�⡼��
            require('./hako-map.cgi');
            preabMain();

        } elsif($HmainMode eq 'lbbs') {             # ������Ǽ��ĥ⡼��
            require('./hako-lbbs.cgi');
            localBbsMain();

        } else {
            ownerMain();

        }
        # �եå�����
        tempFooter();
        # ��λ
        exit(0);
    }
    elsif ($HmainMode eq 'landmap') {

        $Htitle_sub = ' �ޥå�';
        require('./hako-map.cgi');

        $Body = '<body>';
        # �إå�����
        tempHeaderJava();
        # �Ѹ��⡼��
        printIslandJava();
        # �եå�����
        tempFooter();
        # ��λ
        exit(0);

    }
    elsif ($HmainMode eq 'taijilist') {        # �����ͤˤ�뤢������⡼��
        require('./hako-map.cgi');
        $Body = '<body>';
        # �إå�����
        tempHeaderJava();

        Show_Taiji_List();

        # �եå�����
        tempFooter();
        # ��λ
        exit(0);

    }
    elsif(   ($HmainMode ne 'new')
          && ($HmainMode ne 'lbbs') ) {
        # �إå�����
        tempHeader();
    }

    # =====================================================================

    if ($HmainMode eq 'turn') {             # ������ʹ�
        require('./hako-turn.cgi');
        turnMain();

    } elsif($HmainMode eq 'new') {          # ��ο�������
        require('./hako-make.cgi');
        require('./hako-map.cgi');
        newIslandMain();

    } elsif($HmainMode eq 'top') {          # �����ͤˤ�뤢������⡼��
        # ����¾�ξ��ϥȥåץڡ����⡼��
        require('./hako-top.cgi');
        topPageMain();

    } elsif($HmainMode eq 'newally') {      # Ʊ���ο�������
        require('./hako-make.cgi');
        require('./hako-top.cgi');
        makeAllyMain();

    } elsif($HmainMode eq 'delally') {      # Ʊ���κ��
        require('./hako-make.cgi');
        require('./hako-top.cgi');
        deleteAllyMain();

    } elsif($HmainMode eq 'inoutally') {    # Ʊ���β�����æ��
        require('./hako-make.cgi');
        require('./hako-top.cgi');
        joinAllyMain();

    } elsif($HmainMode eq 'allypact') {     # ���祳���ȥ⡼��
        require('./hako-make.cgi');
        allyPactMain();

    } elsif($HmainMode eq 'joinally') {     # Ʊ������
        require('./hako-make.cgi');
        newAllyTop();

    } elsif($HmainMode eq 'aoa') {          # Ʊ�����ͧ��������
        require('./hako-top.cgi');
        amityOfAlly();

    } elsif($HmainMode eq 'preab') {        # �رĶ�Ʊ��ȯ�⡼��
        require('./hako-map.cgi');
        preabMain();

    } elsif($HmainMode eq 'campCHAT') {     # �رĥ⡼��
        require('./hako-map.cgi');
        require('./hako-camp.cgi');
        campMain(1);

    } elsif($HmainMode eq 'camp') {         # �رĥ⡼��
        require('./hako-map.cgi');
        require('./hako-camp.cgi');
        campMain(0);

    } elsif($HmainMode eq 'asetup') {       # ͧ���������ǧ�⡼��
        require('./hako-make.cgi');
        amitySetupMain();

    } elsif($HmainMode eq 'print') {        # �Ѹ��⡼��
        require('./hako-map.cgi');
        $Htitle_sub = ' �ޥå�';
        printIslandMain();

    } elsif($HmainMode eq 'productlist') {  # �ץ�����ȥꥹ��
        require ('./hako-map_product.cgi');
        $Htitle_sub = ' ʪ��';
        ProductListMain();

    } elsif($HmainMode eq 'tradelist') {    # ����ꥹ��
        require ('./hako-map.cgi');
        require ('./hako-trade.cgi');
        $Htitle_sub = ' ���';
        TradeListMain();

    } elsif($HmainMode eq 'tradedelete') {  # ����ꥹ��
        require ('./hako-map.cgi');
        require ('./hako-trade.cgi');
        $Htitle_sub = ' ���';
        TradeDeleteMain();
        TradeListMain();

    } elsif($HmainMode eq 'trademake') {    # ����ꥹ��
        require ('./hako-map.cgi');
        require ('./hako-trade.cgi');
        $Htitle_sub = ' ���';
        TradeMakeMain();
        TradeListMain();

    }
    elsif($HmainMode eq 'tradecng') {       # ����ꥹ��
        require ('./hako-map.cgi');
        require ('./hako-trade.cgi');
        $Htitle_sub = ' ���';
        TradeEditMain();
        TradeListMain();

    } elsif($HmainMode eq 'owner') {        # ��ȯ�⡼��
        require ('./hako-map.cgi');
        $Htitle_sub = ' ��ȯ';
        ownerMain();

    } elsif($HmainMode eq 'command') {      # ���ޥ�����ϥ⡼��
        require('./hako-map.cgi');
        commandMain();

    } elsif($HmainMode eq 'comment') {      # ���������ϥ⡼��
        require('./hako-map.cgi');
        commentMain();

    } elsif($HmainMode eq 'lbbs') {         # ������Ǽ��ĥ⡼��
        require('./hako-map.cgi');
        require('./hako-lbbs.cgi');
        localBbsMain();

    } elsif($HmainMode eq 'change') {       # �����ѹ��⡼��
        require('./hako-make.cgi');
        changeMain();

    } elsif($HmainMode eq 'totoyoso') {     # ���������ϥ⡼��
        require('./hako-map.cgi');
        totoInputMain(0);

    } elsif($HmainMode eq 'totoyoso2') {    # ���������ϥ⡼��
        require('./hako-map.cgi');
        totoInputMain(1);

    } elsif($HmainMode eq 'shuto') {        # ����̾�ѹ��⡼��
        require('./hako-map.cgi');
        shutoMain();

    } elsif($HmainMode eq 'rank') {         # ��󥭥�
        require('./hako-ranking.cgi');
        rankIslandMain();

    } elsif($HmainMode eq 'rekidai') {      # �����¿�͸���Ͽ
        require('./hako-ranking.cgi');
        rekidaiPopMain();

    } elsif($HmainMode eq 'hcdata') {       # HakoniwaCup����
        require('./hako-make.cgi');
        hcdataMain();

    } elsif($HmainMode eq 'bf_point') {     # bf ����
        require('./hako-make.cgi');
        bfpointMain();

    } elsif($HmainMode eq 'teamname') {     # ����̾�ѹ��⡼��
        require('./hako-map.cgi');
        TeamMain();

    } elsif($HmainMode eq 'yaku_chg') {     # ����̾�ѹ��⡼��
        require('./hako-map.cgi');
        WorkChangeMain();

    } elsif($HmainMode eq 'join') {         # ���������õ��
        require('./hako-make.cgi');
        newIslandTop();

    } elsif($HmainMode eq 'rename') {       # ���̾���ȥѥ���ɤ��ѹ�
        require('./hako-make.cgi');
        renameIslandMain();

    } elsif($HmainMode eq 'bfield') {       # BattleField�����⡼��
        require('./hako-make.cgi');
        bfieldMain();

    } elsif($HmainMode eq 'present') {      # �����ͤˤ��ץ쥼��ȥ⡼��
        require('./hako-make.cgi');
        presentMain();

    } elsif($HmainMode eq 'punish') {       # �����ͤˤ�����ۥ⡼��
        require('./hako-make.cgi');
        punishMain();

    } elsif($HmainMode eq 'lchange') {      # �����ͤˤ���Ϸ��ѹ��⡼��
        require('./hako-make.cgi');
        lchangeMain();

    } elsif($HmainMode eq 'predelete') {    # �����ͤˤ�뤢������⡼��
        require('./hako-make.cgi');
        preDeleteMain();

    } else {
        # ����¾�ξ��ϥȥåץڡ����⡼��
        require('./hako-top.cgi');
        topPageMain();
    }

    # �եå�����
    tempFooter();

    # ��λ
    exit(0);


#----------------------------------------------------------------------
# ���ޥ������

sub SetCommandData {
    my ($id, $name, $cost) = @_;

    $HcomCost[$id] = $cost;
    $HcomName[$id] = $name;
}


#----------------------------------------------------------------------
# ���ޥ�ɤ����ˤ��餹
sub slideFront {
    my ($command, $number) = @_;

    # ���줾�줺�餹
    splice(@$command, $number, 1);

    # �Ǹ�˻�ⷫ��
    $command->[$HcommandMax - 1] = {
        'kind' => $HcomDoNothing,
        'target' => 0,
        'x' => 0,
        'y' => 0,
        'arg' => 0
    };
}

#----------------------------------------------------------------------
# ���ޥ�ɤ��ˤ��餹
sub slideBack {
    my ($command, $number) = @_;

    # ���줾�줺�餹
    return if ($number == $#$command);
    pop(@$command);
    splice(@$command, $number, 0, $command->[$number]);
}


#----------------------------------------------------------------------
# ������
#----------------------------------------------------------------------

# CGI���ɤߤ���
sub cgiInput {
    my ($line, $getLine);

    # ���Ϥ������ä����ܸ쥳���ɤ�EUC��
    $line = <>;
    $line =~ tr/+/ /;
    $line =~ s/%([a-fA-F0-9]{2})/pack(H2, $1)/eg;
#   jcode::convert(\$line, 'euc');

    if ($line !~ /Allypact=([^\&]*)\&/) {

        $line =~ s/[\x00-\x1f\,]//g;
    }
    else {
        # ���祳���ȥ⡼��
        # �ѹ��ܥ��󤬲����줿��ư
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

    # GET�Τ�Ĥ�������
    $getLine = $ENV{'QUERY_STRING'};

    # �оݤ���
    if($line =~ /ISLANDID=([0-9]+)\&/){
        $HcurrentID = $1;
    }

    # �ѥ����
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

    # �ʣ���᥹����ץȥ⡼��
    if ($line =~ /JAVAMODE=(cgi|java)/) {
        $HjavaMode = $1;
    } elsif ($getLine =~ /JAVAMODE=(cgi|java)/) {
        $HjavaMode = $1;
    }
    if ($getLine =~ /UNLOCK=([0-9]*)/) {
        $HsepTurnFlag = $1;
    }
    # main mode�μ���
    if ($line =~ /TurnButton/) {
        if (DEBUG_MODE) {
            $HmainMode = 'Hdebugturn';
        }
    }
    elsif ($line =~ /OwnerButton/) {
        $HmainMode = 'owner';
    }
    elsif ($line =~ /CommandJavaButton([0-9]+)=/) {
        # ���ޥ�������ܥ���ξ��ʣʣ���᥹����ץȡ�
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
        # ���ޥ�ɤΥݥåץ��åץ�˥塼�򳫤���
        if ($line =~ /MENUOPEN=on/) {
            $HmenuOpen = 'CHECKED';
        }
        elsif ($line =~ /MENUOPEN2=on/) {
            $HmenuOpen2 = 'CHECKED';
        }

    }
    elsif ($line =~ /CommandButton([0-9]+)=/) {
        # ���ޥ�������ܥ���ξ��
        $HcurrentID = $1;
        if ($HjavaMode eq 'java') {
            $HmainMode = 'command2';
        }
        else {
            $HmainMode = 'command';
        }

        # ���ޥ�ɥ⡼�ɤξ�硢���ޥ�ɤμ���
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
        # ���ޥ�ɤΥݥåץ��åץ�˥塼�򳫤���
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
        our ($TradeTargetID) = $HcurrentID;     # ��ʬ��ID�ǽ����
        if ($line =~ /TargetId=([0-9]*)/) {
            $TradeTargetID = $1;
        }
        our ($TradeObject) = $HcurrentID;     # ��ʬ��ID�ǽ����
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
        $HtempBack = "<A href=\"Javascript:void(0);\" onclick=\"window.open('about:blank','_self').close()\"><span class='big'>[�Ĥ���]</span></A>";
        $HmainMode = 'print';
        $HcurrentID = $1;
        # �����ͥ⡼��
        if ($getLine =~ /ADMINMODE=([0-9]*)/) {
            $HadminMode = $1;
        }
    }
    elsif ($getLine =~ /Sight=([0-9]*)/) {
        $HmainMode = 'print';
        $HcurrentID = $1;
        # �����ͥ⡼��
        if ($getLine =~ /ADMINMODE=([0-9]*)/) {
            $HadminMode = $1;
        }
    } elsif ($getLine =~ /Product=([0-9]*)/) {
        $HmainMode = 'productlist';
        $HcurrentID = $1;

        # �����ͥ⡼��
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
            # ������
            $HlbbsMode = 5;
        } elsif($1 eq 'DA') {
            # �����ͺ��
            $HlbbsMode = 7;
        } elsif($1 eq 'OW') {
            # ���
            $HlbbsMode = 1;
        } elsif($1 eq 'DL') {
            # �����
            $HlbbsMode = 3;
        } elsif($1 eq 'DS') {
            # �Ѹ��Ժ��
            $HlbbsMode = 2;
        } elsif($1 eq 'CK') {
            # �Ѹ��Զ����ǧ
            $HlbbsMode = 4;
        } else {
            # �Ѹ���
            $HlbbsMode = 0;
        }
        $HcurrentID = $2;

        $line =~ /LBBSNAME=([^\&]*)\&/;
        $HlbbsName = cutColumn($1, $HlengthLbbsName*2);
        $HdefaultName = $HlbbsName;
        $line =~ /LBBSMESSAGE=([^\&]*)\&/;
        $HlbbsMessage = cutColumn($1, $HlengthLbbsMessage*2);
        # �Ǽ��Ĥ�ȯ����
        $line =~ /ISLANDID2=([0-9]+)\&/;
        $HspeakerID = $1;
        # �Ǽ��Ĥ��̿�����
        $line =~ /LBBSTYPE=([^\&]*)\&/;
        $HlbbsType = $1;
        # ������⤷��ʤ��Τǡ��ֹ�����
        if($line =~ /NUMBER=([^\&]*)\&/) {
            $HcommandPlanNumber = $1;
        }

    } elsif ($line =~ /ChangeInfoButton/) {
        $HmainMode = 'change';
        # ̾������ξ��
        if ($line =~ /ISLANDNAME=([^\&]*)\&/){
            $HcurrentName = cutColumn($1, $HlengthIslandName*2);
        }
        # �����ʡ�̾�μ���
        if ($line =~ /OWNERNAME=([^\&]*)\&/){
            $HcurrentOwnerName = cutColumn($1, $HlengthOwnerName*2);
        }

    } elsif ($line =~ /MessageButton([0-9]*)/) {
        $HmainMode = 'comment';
        $HcurrentID = $1;
        # ��å�����
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
        # ����μ���
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
        # Ʊ��̾�μ���
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
        # ���祳���ȥ⡼��
        # �ǽ�ε�ư
        $HmainMode = 'allypact';
        $HallyPactMode = 0;
        $HcurrentID = $1;

    } elsif ($line =~ /CAMPCHAT=([0-9]*)/) {
        $HtempBack = "<A href=\"Javascript:void(0);\" onclick=\"window.open('about:blank','_self').close()\"><span class='big'>[�Ĥ���]</span></A>";
        $HmainMode = 'campCHAT';
        $HcurrentCampID = $1;
        if($line =~ /PASSWORD=([^\&]*)\&/) {
            $HinputPassword = $1;
            $HdefaultPassword = $1;
        }
        if($line =~ /jpass=([a-zA-Z0-9]*)/) {
            $HcampPassward = $1; # �رĥѥ����
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
        $HtempBack = "<A href=\"Javascript:void(0);\" onclick=\"window.open('about:blank','_self').close()\"><span class='big'>[�Ĥ���]</span></A>";
        $HmainMode = 'camp';
        $HcurrentCampID = $1;
        if($line =~ /PASSWORD=([^\&]*)\&/) {
            $HinputPassword = $1;
            $HdefaultPassword = $1;
        }
        if($line =~ /jpass=([a-zA-Z0-9]*)/) {
            $HcampPassward = $1; # �رĥѥ����
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
        # ï�Ǥ⿷�������õ����
        $HmainMode = ($HadminJoinOnly ? 'top' : 'join');

    } elsif($line =~ /Join=([0-9]*)/) {
        # �����ͤ��������������õ����
        $HmainMode = ($HadminJoinOnly ? 'join' : 'top');

    }
    elsif ($line =~ /NewIslandButton/) {

        $HmainMode = 'new';
        # ̾���μ���
        $line =~ /ISLANDNAME=([^\&]*)\&/;
        $HcurrentName = cutColumn($1, $HlengthIslandName*2);
        # �����ʡ�̾�μ���
        $line =~ /OWNERNAME=([^\&]*)\&/;
        $HcurrentOwnerName = cutColumn($1, $HlengthOwnerName*2);
        if (   ($HarmisticeTurn)
            && ($HcampSelectRule == 2) ) {

            # �رĤ������ǽ�ʾ��
            if ($line =~ /CAMPNUMBER=([\-]?[0-9]+)\&/) {
                $HcampNumber = $1;
            }
        }

    } elsif($getLine =~ /ASetup=([^\&]*)/) {        # Ʊ�������ǧ�⡼��
        $HmainMode = 'asetup';
        $HasetupMode = 0;
        $HdefaultPassword = $1;
    } elsif($line =~ /ASetup=([^\&]*)\&/) {
        # �ѹ��ܥ��󤬲����줿��ư
        $HmainMode = 'asetup';
        $HasetupMode = 1;
        $HdefaultPassword = $1;
        while ($line =~/amity=([^\&]*)\&/g) {
            push(@HamityChange, $1);
        }
        while ($line =~/ally=([^\&]*)\&/g) {
            push(@HallyChange, $1);
        }

        # BattleField�����⡼��
    } elsif($getLine =~ /Bfield=([^\&]*)/) {    
        # �ǽ�ε�ư
        $HmainMode = 'bfield';
        $HbfieldMode = 0;
        $HdefaultPassword = $1;
    } elsif($line =~ /Bfield=([^\&]*)\&/) {
        # BattleField�����ܥ��󤬲����줿��ư
        $HmainMode = 'bfield';
        $HbfieldMode = 1;
        $HdefaultPassword = $1;

    } elsif($getLine =~ /Present/) {                # �����ͤˤ��ץ쥼��ȥ⡼�ɵ�ư
        # �ǽ�ε�ư
        $HmainMode = 'present';
        $HpresentMode = 0;
    } elsif($line =~ /Present/) {                   # �ץ쥼��ȥܥ��󤬲����줿��ư

        $HmainMode = 'present';
        $HpresentMode = 1;
        ($HpresentMoney) = ($line =~ /PRESENTMONEY=([^\&]*)\&/);
        ($HpresentFood ) = ($line =~ /PRESENTFOOD=([^\&]*)\&/);
        $line =~ /PRESENTLOG=([^\&]*)\&/;
        $HpresentLog   = cutColumn($1, $HlengthPresentLog*2);

    } elsif($getLine =~ /Punish=([^\&]*)/) {        # �����ͤˤ�����ۥ⡼��
        # �ǽ�ε�ư
        $HmainMode = 'punish';
        $HpunishMode = 0;
        $HdefaultPassword = $1;
    } elsif($line =~ /Punish=([^\&]*)\&/) {         # ���ۥܥ��󤬲����줿��ư

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

    } elsif($getLine =~ /Lchange=([^\&]*)/) {   # �����ͤˤ���Ϸ��ѹ��⡼��
        # �ǽ�ε�ư
        $HmainMode = 'lchange';
        $HlchangeMode = 0;
        $HdefaultPassword = $1;

    } elsif($line =~ /Lchange=([^\&]*)\&/) {    # �����ͤˤ���Ϸ��ѹ��⡼�� �ѹ��ܥ��󤬲����줿��ư

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

    } elsif($getLine =~ /Pdelete=([^\&]*)/) {   # �����ͤˤ�뤢������⡼��
        # �ǽ�ε�ư
        $HmainMode = 'predelete';
        $HpreDeleteMode = 0;
        $HdefaultPassword = $1;

    } elsif($line =~ /Pdelete=([^\&]*)\&/) {    # �ѹ��ܥ��󤬲����줿��ư

        $HmainMode = 'predelete';
        $HpreDeleteMode = 1;
        $HdefaultPassword = $1;

    } elsif($getLine =~ /HCdata=([0-9]*)/) {
        $HmainMode = 'hcdata';

    } elsif($getLine =~ /Rekidai=([0-9]*)/) {       # �����¿�͸���Ͽ
        $HmainMode = 'rekidai';

    } else {

        $HmainMode = 'top';
    }
}

#cookie����
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

    # wiiU �ߺ�����
    if($access eq 'WiiU'){
        $init_ID = $rqID if($rqID > -1);
        $HjavaModeSet = $wiiU_javamode;
        $HdefaultPassword = $wiiU_password;
        $HjavaModeSet = 'java' if ( $HjavaModeSet eq '');
    }

}


#----------------------------------------------------------------------
#cookie����
sub cookieOutput {
    my ($cookie, $info);

    # �ä�����¤�����
    my ($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) = gmtime(time + 30 * 86400); # ���� + 30��

    # 2������
    $year += 1900;
    $date = "0$date" if($date < 10);
    $hour = "0$hour" if($hour < 10);
    $min  = "0$min" if($min < 10);
    $sec  = "0$sec" if($sec < 10);

    # ������ʸ����
    $day = ("Sunday", "Monday", "Tuesday", "Wednesday",    "Thursday", "Friday", "Saturday")[$day];

    # ���ʸ����
    $mon = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")[$mon];

    # �ѥ��ȴ��¤Υ��å�
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
        # ��ư�ϰʳ�
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
# wiiU ����������
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
# �桼�ƥ���ƥ�
#----------------------------------------------------------------------
sub hakolock {
    if ($server_config::HlockMode == 1) {
        # directory����å�
        return hakolock1();

    } elsif($server_config::HlockMode == 2) {
        # flock����å�
        return hakolock2();
    } elsif($server_config::HlockMode == 3) {
        # symlink����å�
        return hakolock3();
    } else {
        # �̾�ե����뼰��å�
        return hakolock4();
    }
}


sub hakolock1 {
    # ��å���
    if (mkdir('hakojimalock', $HdirMode)) {
        # ����
        return 1;
    } else {
        # ����
        my ($b) = (stat('hakojimalock'))[9];
        if (($b > 0) && ((time() -  $b)> MAIN_UNLOCK_TIME)) {
            # �������
            unlock();

            # �إå�����
            tempHeader();

            # ���������å�����
            tempUnlock();

            # �եå�����
            tempFooter();

            # ��λ
            exit(0);
        }
        return 0;
    }
}


sub hakolock2 {
    open(LOCKID, '>>hakojimalockflock');
    if (flock(LOCKID, 2)) {
        # ����
        return 1;
    }
    else {
        # ����
        return 0;
    }
}


sub hakolock3 {
    # ��å���
    if (symlink('hakojimalockdummy', 'hakojimalock')) {
        # ����
        return 1;
    }
    else {
        # ����
        my ($b) = (lstat('hakojimalock'))[9];
        if (($b > 0) && ((time() -  $b)> MAIN_UNLOCK_TIME)) {

            unlock();       # �������
            tempHeader();   # �إå�����
            tempUnlock();   # ���������å�����
            tempFooter();   # �եå�����
            exit(0);
        }
        return 0;
    }
}

sub hakolock4 {
    # ��å���
    if (unlink('key-free')) {
        # ����
        open(OUT, '>key-locked');
        print OUT time;
        close(OUT);
        return 1;
    }
    else {
        # ��å����֥����å�
        if (!open(IN, 'key-locked')) {
            return 0;
        }

        my ($t);
        $t = <IN>;
        close(IN);
        if (   ($t != 0)
            && (($t + MAIN_UNLOCK_TIME) < time)) {

            unlock();          # 120�ðʾ�вᤷ�Ƥ��顢����Ū�˥�å��򳰤�
            tempHeader();      # �إå�����
            tempUnlock();      # ���������å�����
            tempFooter();      # �եå�����
            exit(0);
        }
        return 0;
    }
}


#----------------------------------------------------------------------
# ��å��򳰤�
#----------------------------------------------------------------------
sub unlock {
    if ($server_config::HlockMode == 1) {
        # directory����å�
        rmdir('hakojimalock');

    } elsif ($server_config::HlockMode == 2) {
        # flock����å�
        close(LOCKID);

    } elsif ($server_config::HlockMode == 3) {
        # symlink����å�
        unlink('hakojimalock');
    } else {
        # �̾�ե����뼰��å�
        my ($i);
        $i = rename('key-locked', 'key-free');
    }
}


#----------------------------------------------------------------------
# �����������֤�
sub min {
    return ($_[0] < $_[1]) ? $_[0] : $_[1];
}


#----------------------------------------------------------------------
# �礭���ۤ����֤�
sub max {
    return ($_[0] >= $_[1]) ? $_[0] : $_[1];
}

#----------------------------------------------------------------------
# �ѥ���ɥ��󥳡���
sub encode {
    if ($cryptOn == 1) {
        return crypt($_[0], 'h2');
    } else {
        return $_[0];
    }
}

#----------------------------------------------------------------------
# 1000��ñ�̴ݤ�롼����
sub aboutMoney {
    my ($m) = @_;

    my ($order) = 10 ** (INIT_HIDE_MONEY_MODE - 2);
    my ($money);

    if ($m < 500 * $order) {
        $money = 500 * $order;
        return "����${money}${HunitMoney}̤��";
    }
    else {
        $m = int(($m + 500 * $order) / (1000 * $order));
        $money = $m * 1000 * $order;
        return "����${money}${HunitMoney}";
    }
}

#----------------------------------------------------------------------
# 10ȯñ�̴ݤ�롼����
sub aboutMissile {
    my ($m) = @_;

    if ($m < 5) {
        return "����10${HunitMissile}̤��";
    }
    else {
        $m = int(($m + 5) / 10);
        return "����${m}0${HunitMissile}";
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
        $zookazus += $kazu * $HmonsterZooMoney[$mkind];  # $par��������ä��Ȥˤ���
        if ($kazu > 0) {
            $mshurui++;
        }
        $mkind++;
    }

    return ($zookazu, $zookazus, $mshurui);
}


#----------------------------------------------------------------------
# ����������ʸ���ν���
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
        $s =~ s/(<br>){5,}//g; # ���̲����к�
    }
    return $s;
}

#----------------------------------------------------------------------
# 80�������ڤ�·��
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
            tempWrong("ʸ���������С��Ǥ���");
            tempFooter();
            exit(0);
        }
        # ���80�����ˤʤ�ޤ��ڤ���
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
# ���ùŲ�
# ---------------------------------------------------------------------
sub isMonsterCuring {
    my ($kind) = @_;
    my ($special) = $HmonsterSpecial[$kind];

    if (   (($special == 3) && ($HislandTurn % 2))
        || (($special == 8) && !(seqnum($HislandTurn) % 2))
        || (($special == 4) && !($HislandTurn % 2))
        || (($kind == $Mons_Kisinhei) && !(seqnum2($HislandTurn, 12) % 2))
                                                             ) {
        # �Ų���
        return 1;
    }
    return 0;
}


#----------------------------------------------------------------------
# �ɱҴ��Ϥ�HP
#----------------------------------------------------------------------
sub GetDefenceSpec {
    my ($lv) = @_;
    my ($defLevel , $defHP);

    $defLevel = $lv & $HDefenceLevelMask;
    $defHP = $lv >> $HDefenceHP_SHIFT;

    return ($defLevel , $defHP);
}


#----------------------------------------------------------------------
# ���äξ���
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
# ���äξ���
#----------------------------------------------------------------------
sub GetmonsterKind {
    my ($lv) = @_;

    # ����
    my ($kind) = ($lv >> $Mons_Kind_Shift) & $Mons_Kind_MASK;

    return ($kind);
}


#----------------------------------------------------------------------
# �и��Ϥ����٥�򻻽�
#----------------------------------------------------------------------
sub expToLevel {
    my ($kind, $exp) = @_;
    my ($i);
    if ($kind == $HlandBase) {
        # �ߥ��������
        for ($i = $maxBaseLevel; $i > 1; $i--) {
            if ($exp >= $baseLevelUp[$i - 2]) {
                return $i;
            }
        }
        return 1;
    }
    else {
        # �������
        for ($i = $maxSBaseLevel; $i > 1; $i--) {
            if ($exp >= $sBaseLevelUp[$i - 2]) {
                return $i;
            }
        }
        return 1;
    }
}


#----------------------------------------------------------------------
# (0,0)����(size - 1, size - 1)�ޤǤο��������ŤĽФƤ���褦��
# (@Hrpx, @Hrpy)������
#----------------------------------------------------------------------
sub makeRandomPointArray {
    # �����
    my ($y);
    @Hrpx = (0..$islandSize) x $HislandSize;
    foreach $y (0..$islandSize) {
        push(@Hrpy, ($y) x $HislandSize);
    }

    # ����åե�
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
# 0����(n - 1)�����
#----------------------------------------------------------------------
sub random {
    return int(rand(1) * $_[0]);
}


#----------------------------------------------------------------------
# Ϳ�������ͤ��б����뵿�����(0����9�������Τ�)
#----------------------------------------------------------------------
sub seqnum {
    my ($v) = sin($_[0] + 1234); # 1234 ��Ǥ�դ�����������η�����Ѥ���
    return (substr($v, -2, 1));
}


#----------------------------------------------------------------------
# Ϳ�������ͤ��б����뵿�����(0����9�������Τ�)
#----------------------------------------------------------------------
sub seqnum2 {
    my ($v , $seed) = @_;
    $v = sin($v + $seed); # $seed ��Ǥ�դ�����������η�����Ѥ���
    return (substr($v, -2, 1));
}


#----------------------------------------------------------------------
# ������
#----------------------------------------------------------------------
sub islandSort {
    my ($kind, $mode) = @_;

    # �͸���Ʊ���Ȥ���ľ���Υ�����ν��֤Τޤ�
    my @idx = (0..$#Hislands);
    @idx = sort {
        $Hislands[$b]->{'field'} <=> $Hislands[$a]->{'field'} ||
        $Hislands[$a]->{'dead'} <=> $Hislands[$b]->{'dead'} || # ���ǥե饰��Ω�äƤ���и���
        $Hislands[$a]->{'predelete'} <=> $Hislands[$b]->{'predelete'} || # �¤���ե饰��Ω�äƤ���и���
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
# �͸���˥�����(Ʊ���С������)
#----------------------------------------------------------------------
sub allySort {
    # �͸���Ʊ���Ȥ���ľ���Υ�����ν��֤Τޤ�
    my @idx = (0..$#Hally);
    @idx = sort {
            $Hally[$a]->{'dead'} <=> $Hally[$b]->{'dead'} || # ���ǥե饰��Ω�äƤ���и���
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
# ��ɽ��
#----------------------------------------------------------------------
# �ե������ֹ����ǥ�ɽ��
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
            if (   ($mode == 0)
                || ($id1 != $id) ) {
                # ��̩ɽ�������ʤ�
                next;
            }
            $m = '<B>(��̩)</B>:';
        }
        else {
            $m = '';
        }

        # ɽ��Ū�Τ�
        if ($id != 0) {
            if (   ($id != $id1)
                && ($id != $id2) ) {
                next;
            }
        }

        if (!$set_turn){
            out("<b>=====[<span class='number'><font size='4'> ������$turn </font></span>]================================================</b><br>\n");
            $set_turn++;
        }
        out("��${m}$message<BR>\n");
    }
    close(LIN);
}


#----------------------------------------------------------------------
# �ƥ�ץ졼��
#----------------------------------------------------------------------
# �����
sub tempInitialize {
    my ($mode) = @_;
    # �祻�쥯��(�ǥե���ȼ�ʬ)
    $HislandList = getIslandList($init_ID, $mode);
    $HtargetList = getIslandList($defaultTarget, $mode);
}


#----------------------------------------------------------------------
# ��ǡ����Υץ�������˥塼��
sub getIslandList {
    my ($select, $mode) = @_;
    my ($list, $name, $id, $s, $i,$island);

    #��ꥹ�ȤΥ�˥塼
    $list = '';
    my ($predel);
    foreach $i (0..$islandNumber) {
        $island = $Hislands[$i];
        $predel = ($island->{'predelete'}) ? '[��]' : '';
        $name = islandName($island);
        $name =~ s/<[^<]*>//g;
        $id = $island->{'id'};
        $s = ($id eq $select) ? 'SELECTED' : '';
        $list .= '<OPTION VALUE="'.$id.'" ' .$s. '>' . $predel . $name. "</option>\n" if($mode || ($id <=100));
    }
    return $list;
}


#----------------------------------------------------------------------
# ��å�����
#----------------------------------------------------------------------
sub tempLockFail {
    # �����ȥ�
    out(<<END);
<span class='big'>Ʊ�������������顼�Ǥ���<BR>
�֥饦���Ρ����ץܥ���򲡤���<BR>
���Ф餯�ԤäƤ�����٤����������</span>$HtempBack
END
}


#----------------------------------------------------------------------
# �������
#----------------------------------------------------------------------
sub tempUnlock {
    # �����ȥ�
    out(<<END);
<span class='big'>����Υ����������۾ｪλ���ä��褦�Ǥ���<BR>
��å�����������ޤ�����</span>$HtempBack
END
}


#----------------------------------------------------------------------
# �ѥ���ɥե����뤬�ʤ�
#----------------------------------------------------------------------
sub tempNoPasswordFile {
    out(<<END);
<span class='big'>�ѥ���ɥե����뤬�����ޤ���</span>$HtempBack
END
}


#----------------------------------------------------------------------
# hakojima.dat���ʤ�
#----------------------------------------------------------------------
sub tempNoDataFile {
    out(<<END);
<span class='big'>�ǡ����ե����뤬�����ޤ���</span>"${HdirName}/$HmainData"$HtempBack
END
}


#----------------------------------------------------------------------
# ID�㤤or���������ꤷ�Ƥ��ʤ�or���å������ꤷ�Ƥ��ʤ�
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
# ��������ȯ��
sub tempProblem {
    out(<<END);
<span class='big'>����ȯ�����Ȥꤢ������äƤ���������</span>$HtempBack
END
}


#----------------------------------------------------------------------
# �إå�
sub tempHeader {

    my ($mapsizeNumber) = $HidToNumber{$defaultID};
    $Hms1 = 16;
    $Hms2 = $Hms1 << 1;     # 2��

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
  <meta property="og:title" content="minimal97��Ȣ�����" />
  <meta property="og:description" content="minimal97�����Ĥ���̵���֥饦��������Ǥ���" />
  <meta name="twitter:card" content="summary">
  <meta name="twitter:site" content="@minimal97">
  <meta name="twitter:creator" content="@minimal97" />
  <meta name="twitter:title" content="minimal97��Ȣ�����">
  <meta name="twitter:description" content="minimal97�����Ĥ���̵���֥饦��������Ǥ���">
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

# �եå�
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
##### �ɲ� ����20020307
    if (USE_PERFORMANCE) {
        my ($uti, $sti, $cuti, $csti) = times();
        $uti += $cuti;
        $sti += $csti;
        my ($cpu) = $uti + $sti;
        my ($timea) = sprintf("%.5f",Time::HiRes::time - $Hakoniwa_start_time);
    #       ���ե�����񤭽Ф�(�ƥ��ȷ�¬�ѡ����ʤϥ����Ȥˤ��Ƥ����Ƥ�������)
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



