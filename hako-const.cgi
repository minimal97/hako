# ���٤Ƥ�����򤳤��ˤޤȤ�롪
require './init-server.cgi';
#----------------------------------------
# ����
#----------------------------------------
our $Mons_Kind_Shift = 16;
our $Mons_Kind_MASK = 0x3F;
our $Mons_HP_MASK = 0xFFFF;

$HdisMonsBorder1 =  5000; # �͸����1(���å�٥�1)
$HdisMonsBorder2 =  7500; # �͸����2(���å�٥�2)
$HdisMonsBorder3 =  9000; # �͸����3(���å�٥�3)
$HdisMonsBorder4 = 10000; # �͸����4(���å�٥�4)
$HdisMonsBorder5 = 20000; # �͸����4(���å�٥�4)

#  �»���˹�碌�ƽи�Ψ���ѹ�
#                  0  2  4  6  8  10 12 14 16 18 20 22
@HdisMonster    =( 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 2 ); # ñ�����Ѥ�����νи�Ψ(0.01%ñ��)

# ����
# $HmonsterNumber  = 31;

$Mons_MechaInora = 0;       #
$Mons_Inora = 1;            #
$Mons_Kamemusi = 2;         #
$Mons_Kuribo = 3;           #
$Mons_KatuGin = 4;          #
$Mons_Teresa = 5;           #
$Mons_Met = 6;              #
$Mons_KingInora = 7;        #
$Mons_Omu = 8;              #
$Mons_MetaHamu = 9;         #
$Mons_Barimoa = 10;         #
$Mons_Slime = 11;           #
$Mons_HaneHamu = 12;        #
$Mons_Mikael = 13;          # �ߥ�����
$Mons_SlimeLegend = 14;     # ���饤��쥸�����
$Mons_Raygira = 15;         # �쥤����
$Mons_Queen_inora = 16;     # �������󤤤Τ�
$Mons_f20 = 17;             # f20
$Mons_Uriel = 18;           # ���ꥨ��
$Mons_Alfr = 19 ;           # �������
$Mons_Ethereal = 20;        # �����ꥢ
$Mons_Satan = 21;           # ������
$Mons_Ice_scorpion = 22;    # �������������ԥ���
$Mons_Totten = 23;          # �ȥåƥ�
$Mons_Wario = 24;           # ��ꥪ
$Mons_Unbaba = 27;          # ����Х�
$Mons_Mascot_inora = 28;    # �ޥ����åȤ��Τ�
$Mons_Tetra = 29;           # �ƥȥ�
$Mons_SuperTetra = 30;      # Ķ���åƥȥ�
$Mons_Pirates = 32;         # ��±��
$Mons_Volgenom = 33;        # �����륲���
$Mons_Retro_inora = 34;     # ��ȥ��Τ�
$Mons_hime_inora = 35;      # �Ҥᤤ�Τ�
$Mons_Kisinhei   = 36;      # ������ؤ�
$Mons_EnderInora = 37;      # ����������Τ�

$HmonsterDefence = 100; # ���ä��ߥ������á�����Ψ random(1000) < ̵��

# ̾��
our @HmonsterName;

# 1111 1111 1111
#        HH HHHH 
our @HmonsterBHP;       # ��������
our @HmonsterDHP;       # ���Ϥ���
our @HmonsterSpecial;   # �ü�ǽ��
our @HmonsterExp;       # �и���
our @HmonsterValue;     # ���Τ�����
our @HmonsterImage;     # �����ե�����
our @HmonsterImage2;    # �����ե����뤽��2(�Ų���)
our @HmonsterZoo;       # ưʪ��ǻ���� ��Ψ
our @HmonsterZooMoney;  # ưʪ��β���
                                                                                                                                                                                                                                        
# �ü�ǽ�Ϥ����Ƥϡ�
#  0 �äˤʤ�
#  1 ­��®��(����2�⤢�뤯)
#  2 ­���ȤƤ�®��(���粿�⤢�뤯������)
#  3 ���������ϹŲ�
#  4 ����������ϹŲ�
#  5 �ߥ�����޷�
#  6 ���ä򹶷�
#  7 �׷��ȣ�
#  8 ������ʥ�����˹Ų�
#  9 ���������ȡ���
# 11 ���ä����Ϥ�Ƥ��Ԥ���(���ϣ��ޥ�����)
# 12 �λ�ˤʤ������ȯ(���ϣ��ޥ�����)
# 13 ��֤�Ƥ�
# 14 ��פ��� �ۤ����礢��
# 15 ��פ���ʼ��Ϥ��Ϸ��⴬�������
# 16 ��פ��� �ۤ�����ʤ� ���磲��
# 17 �֤�����
# 18 �ϴ�
# 19 ���ܥ�
# 20 ���סܤ��

    #               �ֹ�,               ̾��,                ����,           ����2,         ����,  ���Ϥ�, str  �ü�, �и���, ���Τ�  ưʪ��  ưʪ��
    #                                                                                       ����   ��         , ǽ��          ����    ��      ���� *150��
    SetMonsterTable($Mons_MechaInora,   '��¤�ᥫ���Τ�',   'monster7.gif', '',             2,       0,    1,     0,    5,      0,       100, 1);
    SetMonsterTable($Mons_Inora,        '���ä��Τ�',       'monster0.gif', '',             1,       2,    2,     0,    5,      400,     100, 1);
    SetMonsterTable($Mons_Kamemusi,     '���å���ॷ',     'monster5.gif', 'monster4.gif', 1,       2,    3,     3,    7,      500,     100, 1);
    SetMonsterTable($Mons_Kuribo,       '����ܡ�',         'monster1.gif', '',             1,       2,    4,     0,    5,      1000,    100, 1);
    SetMonsterTable($Mons_KatuGin,     '���ġ᥮�󥵥�ʥ�','katugin.png',  '',             2,       2,    5,     1,    15,     800,     100, 1);
    SetMonsterTable($Mons_Pirates,      '��±��',           'mship01.gif',  '',             3,       1,    1,     0,    20,     1500,    0,   0);

    SetMonsterTable($Mons_Teresa,       '�ƥ쥵',           'monster8.gif', '',             1,       0,    6,     2,    12,     300,     100, 1);
    SetMonsterTable($Mons_Met,          '��å�',           'met.png',      'met_kouka.png',4,       2,    7,     4,    20,     1500,    100, 1);
    SetMonsterTable($Mons_KingInora,    '���å��󥰤��Τ�', 'monster3.gif', '',             7,       2,    8,     0,    30,     5555,    100, 1);
    SetMonsterTable($Mons_Omu,          '�Žò��',         'monster18.gif','',             6,       0,    9,     1,    45,     2500,    0,   0);
    SetMonsterTable(26,                '��פ��Τ饭��','ghostking.gif','',             8,       4,   10,     14,   30,     10000,   25,  1);
    SetMonsterTable(27,                 '�ӥå�����Х�',   'monster27.png','',             7,       2,    8,     2,    30,     0,       0,   0);

    SetMonsterTable($Mons_MetaHamu,     '�Žä᤿�Ϥ�',     'monster25.gif','monster25.gif',5,       2,   10,     8,    40,     3500,    100, 1);
    SetMonsterTable($Mons_Barimoa,      '���åХ�⥢',     'monster13.gif','',             7,       2,   11,     5,    35,     3000,    100, 1);
    SetMonsterTable($Mons_Slime,        '��å��饤��',     'monster14.gif','',             2,       0,   12,     0,    5,      100,     90,  1);
    SetMonsterTable($Mons_HaneHamu,     '���äϤͤϤ�',     'monster16.gif','',             5,       2,   13,     2,    40,     3500,    100, 1);

    SetMonsterTable($Mons_EnderInora,   '����������Τ�',   'ghostking.gif','',             8,       4,   10,     14,   30,     15000,   10,  1);

    SetMonsterTable($Mons_Mikael,       'ŷ�ȥߥ�����',     'monster17.gif','',             10,      0,   14,     0,    99,     99999,   100, 1);
    SetMonsterTable($Mons_SlimeLegend, '���饤��쥸�����','monster19.gif','monster20.gif',5,       0,   15,     8,    70,     27000,   60,  1);
    SetMonsterTable($Mons_Raygira,      '��å쥤����',     'monster22.gif','monster4.gif', 9,       0,   16,     8,    55,     10000,   100, 1);
    SetMonsterTable($Mons_Queen_inora, '��å������󤤤Τ�','monster21.gif','',             9,       0,   17,     5,    60,     12000,   100, 1);
    SetMonsterTable($Mons_f20,          '��¤����f02',      'f02.gif',      '',             8,       0,   18,     2,    85,     48000,   10,  1);
    SetMonsterTable($Mons_Uriel,        'ŷ�ȥ��ꥨ��',     'monster23.gif','',             9,       0,   19,     0,    90,     80000,   5,   1);
    SetMonsterTable($Mons_Alfr,         '��ѻե������',   'monster24.gif','',             2,       0,   20,     1,    95,     95000,   10,  2);
    SetMonsterTable($Mons_Ethereal,     '��ŷ�ȥ����ꥢ',   'monster26.gif','',             7,       0,   21,     7,    0,      85000,   20,  1);
    SetMonsterTable($Mons_Satan,        '�Ⲧ������',       'monster27.gif','',             10,      0,   22,     0,    80,     0,       2,   2);
    SetMonsterTable($Mons_Ice_scorpion,'�������������ԥ���','monster29.gif','',             9,       0,   23,     2,    40,     4000,    10,  2);
    SetMonsterTable(25,                 '��פ��Τ�',     'monsterghost.gif','',          6,       2,    8,     16,   20,     1500,    50,  1);
    SetMonsterTable($Mons_Volgenom,     '�����륲���',     'kaeru.gif',    '',             7,       0,   23,     18,   40,     4000,    20,  2);
    SetMonsterTable($Mons_Retro_inora,  '��ȥ��Τ�',     'retro.gif',   '',              6,       4,   22,     19,   55,     37564,   30,  1);

    SetMonsterTable(31,                 '�����⎭��',         'monster82.gif','',             30,      10,  31,     17,   100,    9000,    80,  1);
    SetMonsterTable($Mons_Totten,       '�ȥåƥ�',         'totten.png',   '',             7,       2,   24,     2,    30,     95000,   10,  1);
    SetMonsterTable($Mons_Wario,        '��ꥪ',           'wario.png',    '',             32,      32,  25,     1,    120,    200000,  0,   0);

    SetMonsterTable($Mons_Kisinhei,     '������ؤ�',       'kisinhei.png','kisinhei_curing.png', 8, 2,   36,     2,    90,     100000,  0,   0);
    SetMonsterTable(35,                 '�Ҥᤤ�Τ�',       'queen.gif',    '',             65530,   0,   35,     20,   0,      0,       0,   0);

    SetMonsterTable(28,                 '�ޥ����åȤ��Τ�', 'monster30.gif','',             0,       0,   28,     0,    0,      1,       0,   0);
    SetMonsterTable(29,                 '���åƥȥ�',       'monster10.gif','',             5,       0,   29,     6,    7,      2000,    0,   0);
    SetMonsterTable($Mons_SuperTetra,   'Ķ���åƥȥ�',     'monster28.gif','',             11,      0,   30,     0,    99,     200000,  0,   0);

    SetMonsterTable(37,                 '��ʼ',             'monster28.gif','',             32,      0,   99,     0,    0,      2,       0,   0);

our @HmonsterTABLE = (0);
our $HmonsterLevel1TABLE_NUM;
our $HmonsterLevel2TABLE_NUM;
our $HmonsterLevel3TABLE_NUM;
our $HmonsterLevel4TABLE_NUM;
our $HmonsterLevel5TABLE_NUM;

#�ǥХå���
our @DebugMonster = (37);

    {
        # ��٥�ˤ�äƽи�������ä򤳤�����Ͽ���롣
        my @HmonsterLevel1Table = ( $Mons_Inora,  2,  3,  4, $Mons_Pirates,$Mons_Pirates,$Mons_Pirates);
        my @HmonsterLevel2Table = (  5,  6,  7,  8, 27, 25);
        my @HmonsterLevel3Table = (  9, 10, 11, 12);
        my @HmonsterLevel4Table = ( 13, 14, 15, 16, 17, 18, 19, 20, 22, 26 ,$Mons_Volgenom,$Mons_Retro_inora);
        my @HmonsterLevel5Table = ( 23, 24, 31 ,$Mons_Kisinhei );

        # ���Υơ��֥뤫��Ҥ��Ƥ���褦�ˤ��롣
        push (@HmonsterTABLE , @HmonsterLevel1Table);
        $HmonsterLevel1TABLE_NUM = $#HmonsterTABLE;

        push (@HmonsterTABLE , @HmonsterLevel2Table);
        $HmonsterLevel2TABLE_NUM = $#HmonsterTABLE;

        push (@HmonsterTABLE , @HmonsterLevel3Table);
        $HmonsterLevel3TABLE_NUM = $#HmonsterTABLE;

        push (@HmonsterTABLE , @HmonsterLevel4Table);
        $HmonsterLevel4TABLE_NUM = $#HmonsterTABLE;

        push (@HmonsterTABLE , @HmonsterLevel5Table);
        $HmonsterLevel5TABLE_NUM = $#HmonsterTABLE;
    }


#----------------------------------------
# ����
#----------------------------------------
# ���Ĥμ���
$HoilMoney = 2500;

# ���Ĥθϳ��Ψ
$HoilRatio = 80;

# �����θϳ��Ψ
$HonsenRatio = 10;

#----------------------------------------
# �礭�ʿ���ʪ
#----------------------------------------
$Food_Kind_Shift = $Mons_Kind_Shift;
$Food_Kind_MASK = $Mons_Kind_MASK;
$Food_HP_MASK = $Mons_HP_MASK;
# �����ढ�뤫
$HBigFoodNum = 1;
# ̾��
@BigFoodName = 
   (   
    '����',             #  0
    '���祳�ꥹ',       #  1
    '���祳�졼�Ի�',   #  2
    '�Ҥ����',         #  3
    '�ݥå���',         #  4
    '�ץ�å�',         #  5
    '�ݥå���',         #  6
    '�ץ�å�',         #  7
    '����'              #  banpei
    );
# ̾��
@BigFoodImage = 
   (   
    'moti.gif',         #  0 ����
    'chocolith.gif',    #  1 ���祳�ꥹ
    'chocolatown.gif',  #  2 ���祳�졼�Ի�
    'hisimoti.gif',     #  3 �Ҥ����
    'pocky.png',        #  4
    'pretz.png',        #  5
    'pochy.png',        #  6
    'prech.png',        #  7
    'moti.gif'          #  banpei
    );
# ̾��
@BigFoodMoney = 
   (   
      200000,    #  0 ����
      200000,    #  1 ���祳�ꥹ
      200000,    #  2 ���祳�졼�Ի�
      50000,     #  3 �Ҥ����
      50000,     #  4 �ݥå���
      50000,     #  5 �ץ�å�
      50000,     #  6 �ݥå���
      50000,     #  7 �ץ�å�
      2          #  banpei
    );

#----------------------------------------
# ��ǰ��
#----------------------------------------
# �����ढ�뤫
$HmonumentNumber = 44;
# $MonumentDust = 28;     #����Υ���Ȣ
# ̾��

# SetMonumentTable
SetMonumentTable(  0 , '��Υꥹ',  'monument0.gif');
SetMonumentTable(  1 , '����',      'monument5.gif');
SetMonumentTable(  2 , '�襤����',  'monument3.gif');
SetMonumentTable(  3 , '�饹����',  'monument12.gif');
SetMonumentTable(  4 , '����',      'monument11.gif');
SetMonumentTable(  5 , '�衼����',  'monument13.gif');
SetMonumentTable(  6 , '����',      'monument16.gif');
SetMonumentTable(  7 , '����',      'monument15.gif');
SetMonumentTable(  8 , '����',      'monument14.gif');
SetMonumentTable(  9 , '������',  'monument17.gif');
SetMonumentTable( 10 , '�⥢��',    'monument18.gif');
SetMonumentTable( 11 , '�ϵ嵷',    'monument19.gif');
SetMonumentTable( 12 , '�Хå�',    'monument20.gif');
SetMonumentTable( 13 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 14 , '���������Τ���', 'monument4.gif');
SetMonumentTable( 15 , '�ƥȥ���',  'monument22.gif');
SetMonumentTable( 16 , '�ϤͤϤ���','monument23.gif');
SetMonumentTable( 17 , '���å�',  'monument27.gif');
SetMonumentTable( 18 , '�ԥ�ߥå�','monument29.gif');
SetMonumentTable( 19 , '��������',  'monument30.gif');
SetMonumentTable( 20 , '�Х�(��)',  'monument31.gif');
SetMonumentTable( 21 , '�Х�(��)',  'monument32.gif');
SetMonumentTable( 22 , '�ѥ󥸡�',  'monument33.gif');
SetMonumentTable( 23 , '��;�(�ݷ�)','monument34.gif');
SetMonumentTable( 24 , '��;�(����)','monument35.gif');
SetMonumentTable( 25 , '������',    'monument40.gif');
SetMonumentTable( 26 , '����',      'monument46.gif');
SetMonumentTable( 27 , '����',      'monument47.gif');
SetMonumentTable( 28 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 29 , '����ڤ��Ȥ�','kon.png');
SetMonumentTable( 30 , '������','wanwan.png');
SetMonumentTable( 31 , '���ꥹ�ޥ��ĥ꡼','monument37.gif');
SetMonumentTable( 32 , '���ꥹ�ޥ��ĥ꡼','monument9.gif');
SetMonumentTable( 33 , '��������',  'nature.png');
SetMonumentTable( 34 , '��',        'monument26.gif');
SetMonumentTable( 35 , '������',    'monument28.gif');
SetMonumentTable( 36 , '���',      'monument36.gif');
SetMonumentTable( 37 , '�㤦����',  'monument38.gif');
SetMonumentTable( 38 , '��ξ',      'train103.png');
SetMonumentTable( 39 , '�����ӥ�',  'kirby.png');
SetMonumentTable( 40 , '���ߥ���',  'miv.png');
SetMonumentTable( 41 , '�̤������','mog.png');
SetMonumentTable( 42 , '��',        'station.gif');
SetMonumentTable( 43 , '��ʥ�',    'xe.png');
SetMonumentTable( 44 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 45 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 46 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 47 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 48 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 49 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 50 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 51 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 52 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 53 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 54 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 55 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 56 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 57 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 58 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 59 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 60 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 61 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 62 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 63 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 64 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 65 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 66 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 67 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 68 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 69 , '����Ȣ',    'monument21.gif');
SetMonumentTable( 70 , '������',    'gate70.gif');
SetMonumentTable( 71 , 'ư���ǧ��', 'monument0.gif');
SetMonumentTable( 72 , '�ȡ��ޡ��Х󥬥�ƥ�', 'Thomas.png');
SetMonumentTable( 73 , '����ޥ˥奨��', 'Gi.png');
SetMonumentTable( 74 , '����',      'monument53.gif');
SetMonumentTable( 75 , '����',      'monument52.gif');
SetMonumentTable( 76 , 'ɹ��',      'monument48.gif');
SetMonumentTable( 77 , '����',      'monument49.gif');
SetMonumentTable( 78 , '����',      'monument50.gif');
SetMonumentTable( 79 , '����',      'monument51.gif');
SetMonumentTable( 80 , '��',        'monument41.gif');
SetMonumentTable( 81 , '��',        'monument42.gif');
SetMonumentTable( 82 , '��',        'monument43.gif');
SetMonumentTable( 83 , '��',        'monument44.gif');
SetMonumentTable( 84 , '�������',  'monument45.gif');
SetMonumentTable( 85 , 'Millennium���ꥹ�ޥ��ĥ꡼', 'monument9.gif');
SetMonumentTable( 86 , '���줿��ά��',  'monument24.gif');
SetMonumentTable( 87 , '��굤�æ����',  'monument25.gif');
SetMonumentTable( 88 , '��',        'monument26.gif');
SetMonumentTable( 89 , '������',    'monument28.gif');
SetMonumentTable( 90 , '���',      'monument36.gif');
SetMonumentTable( 91 , '���ꥹ�ޥ��ĥ꡼2001', 'monument37.gif');
SetMonumentTable( 92 , '�㤦����',  'monument38.gif');
SetMonumentTable( 93 , '��ʡ�ν�����','monument54.gif');
SetMonumentTable( 94 , '�ڤι�褯��','katori.gif');
SetMonumentTable( 95 , '200�������Ĥ���','monument_200oil.gif');
SetMonumentTable( 96 , '������',    'your_name.gif' );


#----------------------------------------
# ��
#----------------------------------------
$HEggKindMax = 4;
# �����ե�����
@HEggImage = 
    (
    'monument41.gif',
    'monument42.gif',
    'monument43.gif',
    'monument44.gif'
    );

#----------------------------------------
# ��
#----------------------------------------
# �����ढ�뤫
$HfuneNumber = 12;

$HcomFrocity_num = 77;      # �ᥬ�ե�����

# ̾��
@HfuneName =
	(
	 '��������',            #  0
	 '��������',            #  1
	 '�淿����',            #  2
	 '����õ����',          #  3
	 '����',                #  4
	 '�緿����',            #  5
	 '��®����',            #  6
	 '����õ��������',      #  7
	 '��ڵ���TITANIC',     #  8
	 '���RENAS',           #  9
	 '���ERADICATE',       # 10
	 '����MASTER',          # 11
	 '��Υꥹ',            # 12
	 '��Υꥹ',            # 13
	 '��Υꥹ',            # 14
	 '��Υꥹ',            # 15
	 '��Υꥹ',            # 16
	 '��Υꥹ',            # 17
	 '��Υꥹ',            # 18
	 '���ERADICATE����'    # 19
	);

@HfuneFood = 
	(
	 1,	 1,	 1,	 0,	 0,	 1,	 1,	 0,	 0,	 0,	 0,	 1,	 0,	 0,	 0,	 0,	 0,	 0,	 0,	 0	);


#                 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
@HfuneSpecial = ( 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 5, 0);
# �ü�ǽ�Ϥ����Ƥϡ�
# 0 �äˤʤ�
# 1 ­��®��(����2�⤢�뤯)
# 2 ­���ȤƤ�®��(���粿�⤢�뤯������)

# �����ե�����
@HfuneImage = 
	(
	 'fune1.gif',
	 'fune1.gif',
	 'fune2.gif',
	 'fune5.gif',
	 'fune4.gif',
	 'fune3.gif',
	 'fune6.gif',
	 'noti.png',
	 'fune7.gif',
	 'fune8.gif',
	 'fune9.gif',
	 'fune10.gif',
	 'monument0.gif',
	 'monument0.gif',
	 'monument0.gif',
	 'monument0.gif',
	 'monument0.gif',
	 'monument0.gif',
	 'monument0.gif',
	 'fune11.gif'
	 );

#----------------------------------------
# �͹�����
#----------------------------------------
# ̾��
our @HeiseiName =
   ( '���ݱ���',  '���ݱ���',  '��¬����',    '�޷����',    '��������',  '�ɱұ���',  '���쥮��顼' );

# �����ե�����
our @HeiseiImage =
   ( 'kisho.gif', 'kisho.gif', 'kansoku.svg', 'geigeki.gif', 'gunji.gif', 'bouei.gif', 'ire.gif' );

our $HeiseiNumber = @HeiseiName;

#----------------------------------------
# ���β�
#----------------------------------------
our @HHouseName;
$HHouseName[0] = '����';
$HHouseName[1] = '�ʰ׽���';
$HHouseName[2] = '����';
$HHouseName[3] = '��齻��';
$HHouseName[4] = '��š';
$HHouseName[5] = '���š';
$HHouseName[6] = '����š';
$HHouseName[7] = '��';
$HHouseName[8] = '���';
$HHouseName[9] = '�����';


#----------------------------------------
# ��ϩ
#----------------------------------------
our $HTrainBase = 10;

our $HTrainMAX = 22;


#----------------------------------------
our @BUMON_NAME;
our @BUMON_ELEMENTS;
our @BUMON_ICON;

    SetBumonTable(0  , '�͸�'             , 'pop'           , "./${HMapImgDir}land502.png");
    SetBumonTable(1  , '����'             , 'farm'          , './img/prize/p_fa.gif');
    SetBumonTable(2  , '����'             , 'factory'       , "./${HMapImgDir}land8.gif");
    SetBumonTable(3  , '�η���'           , 'mountain'      , "./${HMapImgDir}land15.gif");
    SetBumonTable(4  , '����'             , 'fore'          , "./${HMapImgDir}land6.gif");
    SetBumonTable(5  , '�ˤ�Ȥ��'       , 'tare'          , "./img/prize/niwatori_up.gif");
    SetBumonTable(6  , '�֤���'           , 'zipro'         , "./img/prize/buta_up.png");
    SetBumonTable(7  , '������'           , 'leje'          , "./img/prize/ushi_up.gif");
    SetBumonTable(8  , '���ýи���'       , 'monsterlive'   , "./${HMapImgDir}monster0.gif");
    SetBumonTable(9  , '�����༣��'       , 'taiji'         , "./${HMapImgDir}monster0.gif");
    SetBumonTable(10 , '��Ĺ��'           , 'monta'         , "./img/prize/prize11.svg");
    SetBumonTable(11 , '�͸�����'         , 'hamu'          , "./${HMapImgDir}land502.png");
    SetBumonTable(12 , '����'             , 'pika'          , "./img/prize/money.gif");
    SetBumonTable(13 , '��ǰ���'         , 'kei'           , "./${HMapImgDir}monument0.gif");
    SetBumonTable(14 , '��������'         , 'renae'         , "./${HMapImgDir}land37.gif");
    SetBumonTable(15 , '��ʪ���ǽ��'     , 'force'         , "./img/mascot.png");
    SetBumonTable(16 , '�̻��Ѹ���'       , 'eisei2'        , "./${HMapImgDir}land43.gif");
    SetBumonTable(17 , '��ˡ����Ϸ���'   , 'uni'           , "./${HMapImgDir}monument0.gif");
    SetBumonTable(18 , '���å�����������' , 'teamforce'     , "./img/sc.gif");
    SetBumonTable(19 , 'HC ͥ�����'      , 'styusho'       , "./img/sc.gif");
    SetBumonTable(20 , 'HC �̻���Ψ'      , 'shoritu'       , "./img/sc.gif");
    SetBumonTable(21 , 'HC �̻�����'      , 'kachitent'     , "./img/sc.gif");
    SetBumonTable(22 , "HC${hcturn} ����" , 'kachiten'      , "./img/sc.gif");
    SetBumonTable(23 , '100��������Ĺ'    , 'tha_diff'      , "./img/prize/pr100.svg");
    SetBumonTable(24 , 'ưʪ����ÿ�'     , 'zoo_Mons_cnt'  , "./${HMapImgDir}land84.gif");
    SetBumonTable(25 , '�ϥ��ƥ�'         , 'factoryHT'     , "./${HMapImgDir}land85.gif");
    SetBumonTable(26 , '������'           , 'area'          , "./img/prize/island.gif");


#
sub SetBumonTable {
    my ($no, $name, $ele, $icon) = @_;

    $BUMON_NAME[$no] = $name;
    $BUMON_ELEMENTS[$no] = $ele;
    $BUMON_ICON[$no] = $icon;
}


#----------------------------------------
# �޴ط�
#----------------------------------------
# �������դ򲿥�������˽Ф���
our $HturnPrizeUnit = 100;

# �ޤ�̾��
our @Hprize;
$Hprize[0] = '��������';
$Hprize[1] = '�˱ɾ�';
$Hprize[2] = 'Ķ�˱ɾ�';
$Hprize[3] = '����˱ɾ�';
$Hprize[4] = 'ʿ�¾�';
$Hprize[5] = 'Ķʿ�¾�';
$Hprize[6] = '���ʿ�¾�';
$Hprize[7] = '�����';
$Hprize[8] = 'Ķ�����';
$Hprize[9] = '��˺����';


#----------------------------------------------------------------------
# ����
#----------------------------------------------------------------------
our $Hmine_DAMAGE_MASK = 0x00FF;
our $Hmine_SEA_FLAG = 0x800000;

#----------------------------------------------------------------------
# ��������
#----------------------------------------------------------------------
our $HYakusho_Narasi = 700 ;
our $HYakusho_Narasi2 = 1400 ;

#----------------------------------------------------------------------
# �Ϸ��Ѳ�
#----------------------------------------------------------------------
# random(100)
our $To_Sunahama_par = 5;
our $To_Ice_par = 1;

our $Sunahama_To_Sea_par = 30;
our $Ice_To_Sea_par = 10;

our $HForest_Limit = 800 ;

#----------------------------------------------------------------------
# �Ϳ�����
#----------------------------------------------------------------------
our $HTown_growstop = 100 ;     # Į�οͿ�����
our $HTown_limit    = 250 ;     # Į�οͿ�����
our $HOnsen_limit   = 100 ;     # �����οͿ�����

our $HProcity_growstop = 100 ;  # �ɺ��ԻԤοͿ�����
our $HProcity_limit = 200 ;     # �ɺ��ԻԤοͿ�����

our $HFrocity_limit = 200 ;     # �ᥬ�ե��ȤοͿ�����
our $HSeatown_limit = 400 ;     # �����ԻԤοͿ�����
our $HBigtown_limit = 500 ;     # �����ԻԷ�
our $HShrine_limit  = 200;
our $HBettown_limit = 2000;     # �������Ի�

our $HUmicity_growstop = 2000;  # ���Ի�
our $HUmicity_limit = 3000;     # ���Ի�

our $HNewtown_growstop = 100 ;  # �˥塼������οͿ�����
our $HNewtown_limit = 300 ;     # �˥塼������οͿ�����

our $HShuto_growstop = 750 ;    # ���ԤοͿ�����
our $HShuto_limit   = 4000 ;    # ���ԤοͿ�����

our $HMountain_add   = 5;
our $HMountain_limit = 200;


our $HGold_add      = 20;
our $HGold_limit    = 200;

our $HLivestock_limit = 4000;       # ���ܾ��


our $HFactory_add   = 10;           # ���� �ɲ�
our $HFactory_base  = 30;           # ���� �ɲ�
our $HFactory_limit = 100;          # ���� ����

# ���Τ����
our $HInoraland_add = 30;
our $HInoraland_limit = 1500;

# �ϥ��ƥ����
our $HlandSHTF_add = 2;
our $HlandSHTF_limit = 500 + 350;

# �ϥ��ƥ����
our $HlandHTFactory_add = 2;
our $HlandHTFactory_limit =500 + 250;

our $HFoodim_add    = 10;           # ��ʪ����� �ɲ�
our $HFoodim_base   = 30;           # ��ʪ����� �ɲ�
our $HFoodim_limit  = 500;          # ��ʪ����� ����

our $HPark_add      = 30;           # ͷ����
our $HIce_add       = 25;           # ͷ����
our $HPark_base     = 10;           # ͷ����
our $HPark_limit    = 100;          # ͷ����

our $HNursery_add = 5;
our $HNursery_base = 20;
our $HNursery_limit = 100;

our $HHTFactory_add = 10;        #�ϥ��ƥ���� �ɲ�
our $HHTFactory_limit = 500;        #�ϥ��ƥ���� �ɲ�

our $HUmiamu_limit = 1000;
our $HUmiamu_add = 30;
our $HUmiamu_base = 50;

our $HInoraLand_limit = 1500;
our $HInoraLand_add = 30;
# base�ϡ�$HPark_limit


our $HFarm_base = 10;
our $HFarm_add = 2;
our $HFarm_limit = 50;

our $HMine_limit = 9;

our $Reason_Normal = 0;
our $Reason_FoodShort = 1;
our $Reason_Rotten = 2;
our $Reason_Plague = 3;
our $Reason_SideEffect = 4;

our $HInaka_growstop = 30;
our $HInaka_limit = 30;

#----------------------------------------------------------------------
# ����
#----------------------------------------------------------------------
#                          0,   1,   2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12��
our @HTemperatureMax = (  25,  25,  24, 25, 27, 30, 33, 35, 35, 34, 33, 28, 26); # 
our @HTemperatureAve = (   8,   8,   9, 10, 15, 21, 23, 29, 29, 24, 19, 13,  8); # ʿ��
our @HTemperatureMin = ( -13, -13, -11, -6, -2,  4,  7, 16, 13,  8,  1, -7, -9); # 

our $HWeather_Sunny = 0;
our $HWeather_Cloud = 1;
our $HWeather_Rain = 2;
our $HWeather_Snow = 3;

our @HWeather_table = (
    [ 17,  9,  5],        #0
    [ 17,  9,  5],        #1
    [ 12,  9,  7],        #2
    [ 14, 10,  7],        #3
    [ 11,  8, 11],        #4
    [ 13, 12,  6],        #5
    [ 10, 10, 10],        #6
    [  6, 17,  8],        #7
    [ 11, 15,  5],        #8
    [  8, 12, 10],        #9
    [  9,  3, 19],        #10
    [ 16,  6,  8],        #11
    [ 17, 10,  4]         #12
);

#print "$HWeather_table[0][0]\n";
#----------------------------------------------------------------------
# ʪ�����
#----------------------------------------------------------------------
our @HProduct_Food_hash_table = (
    'kome' , 'yasai' , 'kudamono', 'seafood' , 'sio' , 
    'toriniku', 'butaniku' , 'gyuniku', 'nazoniku' , 'tamago'
);

our @HProduct_Name;
$HProduct_Name{'kome'}      = '����';
$HProduct_Name{'yasai'}     = '���';
$HProduct_Name{'kudamono'}  = '�������';
$HProduct_Name{'seafood'}   = '������';
$HProduct_Name{'sio'}       = '��';
$HProduct_Name{'toriniku'}  = '����';
$HProduct_Name{'butaniku'}  = '����';
$HProduct_Name{'gyuniku'}   = '����';
$HProduct_Name{'nazoniku'}  = '�ʤ���';
$HProduct_Name{'tamago'}  = '���ޤ�';

our @HProduct_unitName;
$HProduct_unitName{'kome'}      = '00�ȥ�';
$HProduct_unitName{'yasai'}     = '00�ȥ�';
$HProduct_unitName{'kudamono'}  = '00�ȥ�';
$HProduct_unitName{'seafood'}   = '00�ȥ�';
$HProduct_unitName{'sio'}       = '00�ȥ�';
$HProduct_unitName{'toriniku'}  = '00�ȥ�';
$HProduct_unitName{'butaniku'}  = '00�ȥ�';
$HProduct_unitName{'gyuniku'}   = '00�ȥ�';
$HProduct_unitName{'nazoniku'}  = '00�ȥ�';
$HProduct_unitName{'tamago'}  = '00�ȥ�';


#----------------------------------------------------------------------

our $HStadiumResult = ('������',       'ͽ���裱���Ԥ�', 'ͽ���裲���Ԥ�', 'ͽ���裳���Ԥ�', 'ͽ���裴���Ԥ�',
             'ͽ����λ�Ԥ�', '�ࡹ�辡���Ԥ�', '��辡���Ԥ�',   '�辡���Ԥ�', 'ͥ����',
             '������',       'ͽ�����',       '�ࡹ�辡�餱',   '��辡�餱', '�裲��');

#----------------------------------------------------------------------
# �ɱҴ���
#----------------------------------------------------------------------
our $HDefenceLevelMask = 0x0F;
our $HDefenceHP_SHIFT  = 4;
our $HDefenceTurnCost  = 2200;

#----------------------------------------------------------------------
# ���
#----------------------------------------------------------------------
our $HYakushoMAXLevel  = 6;
our $HYakushoWorkExist = 0x01;
our $HYakushoWorkYotei = 0x02;
our $HYakushoWorkSeiti = 0x04;

#----------------------------------------------------------------------
# �� effect
#----------------------------------------------------------------------
our $g_Island_Chaff = 0x01;
our $g_Island_Retro = 0x02;

#----------------------------------------------------------------------
# ��ϩ
#----------------------------------------------------------------------
our $Train_Exist = 0x40;
our $Train_Mask = 0x3F;

#----------------------------------------------------------------------
# BF
#----------------------------------------------------------------------
our $HBF_MONSTER_HOUSE = 1;

our $HBF_Point_Value = 170;
our $HBF_Missile_Limit = 30;

#----------------------------------------------------------------------
# �����ƥ�MAX
#----------------------------------------------------------------------
our $HItem_MAX = 5;
our $HItem_Nothing = 0;


our $HFiredept_cost = 3;
our $HFiredept_guard = 1;       #0.1%
our $HFiredept_save = 50;       # 50 %

#----------------------------------------------------------------------
# ���ڡ��������ڡ��������ڡ���������
#----------------------------------------------------------------------
our $HRocket_SpaceDebri = 50;
our $HRocketMiss_SpaceDebri = 70;
our $HRocketBroken_SpaceDebri = 100;
our $HSpaceDebri_meteo = 1000;
our $HSpaceDebri_evapo = 3;



#----------------------------------------------------------------------
# ��̱���׵�
#----------------------------------------------------------------------
our $HCivReq_None = 0;
our $HCivReq_TaxDown = 1;

our $HCivReq_FailTurn = (12*8);

#----------------------------------------------------------------------
# �ֹ�, ̾��, ����
sub SetMonumentTable {
    my ($no, $name, $image) = @_;

    $HmonumentName[$no] = $name;
    $HmonumentImage[$no] = $image;
}

# �ֹ�, ����, ����2, ��������, ���Ϥ���, �ü�ǽ��, �и���, ���Τ�����, ưʪ�����
sub SetMonsterTable {
    my ($no, $name, $image, $cureimage, $bhp, $dhp, $str , $sp, $exp, $money, $zoo, $zoo_mo) = @_;

    $HmonsterName[$no] = $name;
    $HmonsterImage[$no] = $image;
    $HmonsterImage2[$no] = $cureimage;
    $HmonsterBHP[$no] = $bhp;
    $HmonsterDHP[$no] = $dhp;
    $HmonsterSTR[$no] = $str;
    $HmonsterSpecial[$no] = $sp;
    $HmonsterExp[$no] = $exp;
    $HmonsterValue[$no] = $money;
    $HmonsterZoo[$no] = $zoo;
    $HmonsterZooMoney[$no] = $zoo_mo;
}

1;

