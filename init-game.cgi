#----------------------------------------------------------------------
# Ȣ����� RA JS ver4.xx
# ����������⥸�塼��(ver1.00)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
# ����ˤ� -uRAniwa-: http://snow.prohosting.com/awinokah/
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# �Ƽ�������
# (����ʹߤ���ʬ�γ������ͤ�Ŭ�ڤ��ͤ��ѹ����Ƥ�������)
#----------------------------------------------------------------------
#----------------------------------------
# ������οʹԤ�ե�����ʤ�
#----------------------------------------
# �����ཪλ�������
# 0 �ˤ���м�ư��λ���ޤ���
$HgameLimitTurn = 0;
use constant INIT_GAME_LIMIT_TURN   => 0;

# �ꥢ�륿���ޡ��λ���(0:���Ѥ��ʤ���1:���Ѥ���)
#$Hrealtimer = 1;
use constant INIT_REAL_TIMER    => 1;

# �ȥåץڡ�����ɽ��������ο�
# �ʤ������������ʣ���ڡ�����ʬ�����ޤ���
our $HviewIslandCount = 50;
use constant INIT_VIEW_ISLAND_COUNT => 50;

# �Хå����åפ򲿥����󤪤��˼�뤫
$HbackupTurn = 1;

# �Хå����åפ򲿲�ʬ�Ĥ���
$HbackupTimes = 12;

# ȯ�����ݻ��Կ�(10����礭�������ɽ��������ޤ������ο��ͤ�Ĵ�����Ʋ�����)
$HhistoryMax = 6;
use constant INIT_HISTORY_MAX => 6;

# ����ɽ�����κ���ι⤵��
# height�λ����ͤ�Ķ����ȥ�������С���ɽ������ޤ���
$HdivHeight = 150; # <DIV style="overflow:auto; height:${HdivHeight}px;">

# Hakoniwa Cup������ɽ�����κ���ι⤵��
# height�λ����ͤ�Ķ����ȥ�������С���ɽ������ޤ���
$HdivHeight2 = 150; # <DIV style="overflow:auto; height:${HdivHeight2}px;">

# �������ޥ�ɼ�ư���ϥ������
$HgiveupTurn = 72;

# ����ϡ�����ϡ����ýи������礬�������͸�
# �ʤ��ο͸���Ķ����ޤǳ�ȯ�����Ǥ��ʤ���
$HguardPop = 500; # ������

# ������Ǽ��Ĥؤ�ƿ̾ȯ������Ĥ��뤫(0:�ػߡ�1:����)
$HlbbsAnon = 0;
use constant INIT_LBBS_ANONYMOUS => 0;

# ������Ǽ��Ĥ�ȯ����ȯ���Ԥ�̾����ɽ�����뤫(0:ɽ�����ʤ���1:ɽ������)
$HlbbsSpeaker = 1;
use constant INIT_LBBS_SPEAKER    => 1;

# ������Ǽ��ĤΥ���ܹԤ��뤫(0:�ܹԤ��ʤ���1:�ܹԤ���)
# (��Ư��ηǼ��ĥ������ȯ���б��˰ܹԤ��뤳�Ȥ��Ǥ��ޤ�)
$HlbbsOldToNew = 1;
use constant INIT_LBBS_OLD_TO_NEW    => 1;

# ¾��Υ�����Ǽ��Ĥ�ȯ�����뤿�������(0:̵�� 1:ͭ��)
$HlbbsMoneyPublic =   0; # ����
$HlbbsMoneySecret = 100; # ����

# ������˲��á��峤���ʤ���С��ߥ������ȯ����ߤˤ��뤫��(0:���ʤ���1:����)
$HtargetMonster = 0;

# ST�ߥ������Ȥ�����(0:�ػ�)
$HuseMissileST = 1;

# �����ɸ���Ȥ�����(0:�ػ�)
$HuseSendMonster = 1;
use constant INIT_USE_SEND_MONSTER    => 1;

# ��ǰ��ȯ�ͤ�Ȥ�����(0:�ػ�)
$HuseBigMissile = 0;
use constant INIT_BIG_MISSILE    => 0;

# �Хȥ�ե�����ɤ򹶷�Ǥ���ߥ�����μ���
@HkindBFM = (31); # ���Ĥ���ߥ�����ȯ�ͥ��ޥ�ɤο���
# ����OK�ξ�� ��  PP  SPP  ST  ��  δ  ��
@HkindBFM = (31, 32,  36, 33, 37, 38, 34);

# ¾�ͤ�����򸫤��ʤ����뤫(0:�����ʤ� 1:������ 2:100�ΰ̤ǻͼθ��� 3:1000�ΰ̤ǻͼθ���)
$HhideMoneyMode = 1;
use constant INIT_HIDE_MONEY_MODE    => 1;

# ¾�ͤ���ߥ�����ȯ�Ͳ�ǽ���򸫤��ʤ����뤫(0:�����ʤ� 1:������ 2:10�ΰ̤ǻͼθ���)
# $HhideMissileMode = 0;
use constant INIT_HIDE_MISSILE_MODE    => 0;

# ����ʪ�񤬤ʤ���Хߥ�����ȯ�ͤǤ��ʤ������Ȥ���(0:�Ȥ�ʤ� 1:�Ȥ�)
$HuseArmSupply = 0;
use constant INIT_USE_ARM_SUPPLY    => 0;

# ����ʪ��Ĵã�򥿡������ʤ��ˤ��뤫(0:���ʤ� 1:����)
# $HnoturnArmSupply = 0;

# ʣ���Υߥ�����ȯ�ͥ��ޥ�ɤ���¹ԤǤ���褦�ˤ��뤫(0:�Ǥ��ʤ� 1:�Ǥ���)
$HanyMissileMode = 1;

# ���ġ�ͷ���ϡ������Ϥμ���(����)�����ܲ����뤫��(0:���ʤ� 1:����(�ݻ������򺹤�����) 2:����(�ݻ�����������ʤ�))
$HlogOmit1 = 1;

# �����������ܲ����뤫��(0:���ʤ� 1:����)
use constant STATUE_LOG_OMIT    => 1;

# ���ϥ����ܲ����뤫��(0:���ʤ� 1:��ɸ���� 2:��ɸ�ʤ�)
$HlogOmit2 = 1;

# �����������ˡ���ء���Į���˥塼�����󣱤Ĥ��Ĥȿ͹��������Ĥ�ǽ餫���äƤ��뤫 (0: ������  1: �Ϥ�)
$HeasyMode = 0;

# JavaScript�ΰ��������ե����벽���뤫��(0:���ʤ� 1:����)
# $HextraJs = 0;
use constant EXTRA_JS    => 0;

#----------------------------------------
# ��⡢�����ʤɤ������ͤ�ñ��
#----------------------------------------
# ������
$HinitialMoney = 2000;

# �������
$HinitialFood = 200;

# ������
$HmaximumMoney = 9999999;

# ���翩��
$HmaximumFood  = 999999;
use constant INIT_MAXIMUM_FOOD    => 999999;

# �����ñ��
$HunitMoney = '����';

# ������ñ��
$HunitFood = '00�ȥ�';

# �͸���ñ��
$HunitPop = '00��';

# ������ñ��
$HunitArea = '00����';

# �ڤο���ñ��
$HunitTree = '00��';

# �ڤ�ñ�������������
$HtreeValue = 5;

# ̾���ѹ��Υ�����
$HcostChangeName = 500;

# �͸�1ñ�̤�����ο���������
$HeatenFood = 0.2;

# �ߥ�����ο���ñ��
$HunitMissile = 'ȯ';

# ���äο���ñ��
$HunitMonster = 'ɤ';
#----------------------------------------
# ���Ϥηи���
#----------------------------------------
# �и��ͤκ�����
$HmaxExpPoint = 200; # ������������Ǥ�255�ޤ�

# ��٥�κ�����
$maxBaseLevel  = 5; # �ߥ��������
$maxSBaseLevel = 4; # �������

# �и��ͤ������Ĥǥ�٥륢�åפ�
@baseLevelUp  = (20, 60, 120, 200);	# �ߥ��������
@sBaseLevelUp = (50, 100, 200);		# �������

#----------------------------------------
# ���βȤΥ��
#----------------------------------------
our @HouseLevel;
$HouseLevel[1] = 15000; # �ʰ׽���
$HouseLevel[2] = 20000; # ����
$HouseLevel[3] = 25000; # ��齻��
$HouseLevel[4] = 30000; # ��š
$HouseLevel[5] = 35000; # ���š
$HouseLevel[6] = 40000; # ����š
$HouseLevel[7] = 45000; # ��
$HouseLevel[8] = 50000; # ���
$HouseLevel[9] = 55000; # �����

#----------------------------------------
# �ɱһ��ߤμ���
#----------------------------------------
# ���ä�Ƨ�ޤ줿����������ʤ�1�����ʤ��ʤ�0
$HdBaseAuto = 0;

# ���礬��ä��ߥ�������ɱҤ���ʤ��褦�ˤ���ʤ�1�����ʤ��ʤ�0
$HdBaseSelfNoDefence	= 1; # �ɱһ���
$HdProcitySelfNoDefence	= 1; # �ɱ��Ի�

# �ɱһ��ߤ�100%���ɱҤ򤷤ʤ��褦�ˤ���ʤ�1�����ʤ��ʤ�0
$HdBaseNoPerfect	=  1; # �ɱһ���
$HdProcityNoPerfect	=  0; # �ɱ��Ի�
$HdNoPerfectP		= 30; # �ɱҤ˼��Ԥ����Ψ(10%)

# �ɱһ���ľ��Υߥ�������ɱҤ���ʤ�1�����ʤ��ʤ�0
$HdBaseSelfDefence = 0; # �ɱһ��� & �ɱ��Ի�


#----------------------------------------------------------------------
# ����¾��ĥ�Ѥ�����(����Ū�ˤϡ��ѹ��Բ�)
#----------------------------------------------------------------------
# ext[0] �ر�id (̤����)
# ext[1] ����point
# ext[2] �˲������ɱһ��ߤο�
# ext[3] �˲������ߥ�������Ϥο�
# ext[4] �߽Ф�����̱�ι�׿͸�
# ext[5] �������ߥ������
# ext[6] ȯ�ͤ����ߥ������
# ext[7] �ɱһ��ߤ��Ƥ����ߥ������
#----------------------------------------
# ����ʸ����������(����ʸ�����ǻ���)
#----------------------------------------
# ʸ�����¤򥪡��С������������������Ǥ��뤫��(0:���ʤ� 1:����)
$HlengthAlert = 0;

$HlengthIslandName  = 15;   # ���̾��
$HlengthOwnerName   = 15;   # ��ν�ͭ�Ԥ�̾��
$HlengthMessage     = 40;   # �ȥåץڡ�����ɽ����������Υ�����
$HlengthLbbsName    = 15;   # �ִѸ��Ǽ��ġפ���Ƽ�̾
$HlengthLbbsMessage = 40;   # �ִѸ��Ǽ��ġפ����
$HlengthYoso        = 30;   # ͽ����
$HlengthShuto       = 15;   # ����̾
$HlengthTeam        = 15;   # ����̾
$HlengthAllyName    = 15;   # Ʊ����̾��
$HlengthAllyComment = 40;   # �ֳ�Ʊ���ξ��������ɽ�����������Υ�����
$HlengthAllyTitle   = 30;   # ��Ʊ���ξ������ξ��ɽ������������å������Υ����ȥ�
$HlengthAllyMessage = 1500; # ��Ʊ���ξ������ξ��ɽ������������å�����
$HlengthPresentLog  = 100;  # �����ͤˤ��ץ쥼��ȥ⡼�ɤΥ�å�����
#----------------------------------------
# �����ط�
#----------------------------------------
# ����
# �����ȥ�ʸ��
$HtagTitle_ = '<h1 class="title">';
$H_tagTitle = '</h1>';

# �礭��ʸ��
$HtagBig_ = '<span class="big">';
$H_tagBig = '</span>';

# ���̾���ʤ�
$HtagName_ = '<span class="islName">';
$H_tagName = '</span>';

# �����ʤä����̾��
$HtagName2_ = '<span class="islName2">';
$H_tagName2 = '</span>';

# ��̤��ֹ�ʤ�
$HtagNumber_ = '<span class="number">';
$H_tagNumber = '</span>';

# ���ɽ�ˤ����븫����
$HtagTH_ = '<span class="head">';
$H_tagTH = '</span>';

# totoɽ�ˤ����븫����
$HtagtTH_ = '<span class="headToTo">';
$H_tagtTH = '</span>';

# ��ȯ�ײ��̾��
$HtagComName_ = '<span class="command">';
$H_tagComName = '</span>';

# �ҳ�
$HtagDisaster_ = '<span class="disaster">';
$H_tagDisaster = '</span>';

# ������Ǽ��ġ��Ѹ��Ԥν񤤤�ʸ��
$HtagLbbsSS_ = '<span class="lbbsSS">';
$H_tagLbbsSS = '</span>';

# ������Ǽ��ġ����ν񤤤�ʸ��
$HtagLbbsOW_ = '<span class="lbbsOW">';
$H_tagLbbsOW = '</span>';

# ����
$HtagMoney_ = '<span class="money">';
$H_tagMoney = '</span>';

# ����
$HtagFood_ = '<span class="food">';
$H_tagFood = '</span>';

# Ȣ���å׾���
$HtagWin_ = '<span class="HCwin">';
$H_tagWin = '</span>';

# Ȣ���å�����
$HtagLose_ = '<span class="HClose">';
$H_tagLose = '</span>';

# �̾��ʸ����
$HnormalColor_ = '<span class="normal">';
$H_normalColor = '</span>';

# ���ɽ�������°��
$HbgTitleCell   = 'class=TitleCell';   # ���ɽ���Ф�
$HbgNumberCell  = 'class=NumberCell';  # ���ɽ���
$HbgNameCell    = 'class=NameCell';    # ���ɽ���̾��
$HbgInfoCell    = 'class=InfoCell';    # ���ɽ��ξ���
$HbgCommentCell = 'class=CommentCell'; # ���ɽ��������
$HbgInputCell   = 'class=InputCell';   # ��ȯ�ײ�ե�����
$HbgMapCell     = 'class=MapCell';     # ��ȯ�ײ��Ͽ�
$HbgCommandCell = 'class=CommandCell'; # ��ȯ�ײ����ϺѤ߷ײ�
$HbgPoinCell    = 'class=PoinCell';    # Point��
$HbgTotoCell    = 'class=TotoCell';    # toto��

1;
