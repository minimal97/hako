# すべての定数をここにまとめる！
require './init-server.cgi';
#----------------------------------------
# 怪獣
#----------------------------------------
our $Mons_Kind_Shift = 16;
our $Mons_Kind_MASK = 0x3F;
our $Mons_HP_MASK = 0xFFFF;

$HdisMonsBorder1 =  5000; # 人口基準1(怪獣レベル1)
$HdisMonsBorder2 =  7500; # 人口基準2(怪獣レベル2)
$HdisMonsBorder3 =  9000; # 人口基準3(怪獣レベル3)
$HdisMonsBorder4 = 10000; # 人口基準4(怪獣レベル4)
$HdisMonsBorder5 = 20000; # 人口基準4(怪獣レベル4)

#  実時刻に合わせて出現率を変更
#                  0  2  4  6  8  10 12 14 16 18 20 22
@HdisMonster    =( 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 2 ); # 単位面積あたりの出現率(0.01%単位)

# 種類
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
$Mons_Mikael = 13;          # ミカエル
$Mons_SlimeLegend = 14;     # スライムレジェンド
$Mons_Raygira = 15;         # レイジラ
$Mons_Queen_inora = 16;     # クイーンいのら
$Mons_f20 = 17;             # f20
$Mons_Uriel = 18;           # ウリエル
$Mons_Alfr = 19 ;           # アールヴ
$Mons_Ethereal = 20;        # イセリア
$Mons_Satan = 21;           # サタン
$Mons_Ice_scorpion = 22;    # アイススコーピオン
$Mons_Totten = 23;          # トッテン
$Mons_Wario = 24;           # ワリオ
$Mons_Unbaba = 27;          # ウンババ
$Mons_Mascot_inora = 28;    # マスコットいのら
$Mons_Tetra = 29;           # テトラ
$Mons_SuperTetra = 30;      # 超神獣テトラ
$Mons_Pirates = 32;         # 海賊船
$Mons_Volgenom = 33;        # ヴォルゲロム
$Mons_Retro_inora = 34;     # レトロいのら
$Mons_hime_inora = 35;      # ひめいのら
$Mons_Kisinhei   = 36;      # きしんへい
$Mons_EnderInora = 37;      # エンダーいのら

$HmonsterDefence = 100; # 怪獣がミサイルを叩き落す確率 random(1000) < 無効

# 名前
our @HmonsterName;

# 1111 1111 1111
#        HH HHHH 
our @HmonsterBHP;       # 最低体力
our @HmonsterDHP;       # 体力の幅
our @HmonsterSpecial;   # 特殊能力
our @HmonsterExp;       # 経験値
our @HmonsterValue;     # 死体の値段
our @HmonsterImage;     # 画像ファイル
our @HmonsterImage2;    # 画像ファイルその2(硬化中)
our @HmonsterZoo;       # 動物園で飼育可 確率
our @HmonsterZooMoney;  # 動物園の価値
                                                                                                                                                                                                                                        
# 特殊能力の内容は、
#  0 特になし
#  1 足が速い(最大2歩あるく)
#  2 足がとても速い(最大何歩あるくか不明)
#  3 奇数ターンは硬化
#  4 偶数ターンは硬化
#  5 ミサイル迎撃
#  6 怪獣を攻撃
#  7 衝撃波１
#  8 ランダムなターンに硬化
#  9 アイスストーム
# 11 怪獣が周囲を焼き尽くす(周囲６マス壊滅)
# 12 瀕死になると大爆発(周囲６マス壊滅)
# 13 仲間を呼ぶ
# 14 ワープする ほかの島あり
# 15 ワープする（周囲の地形も巻き込む）
# 16 ワープする ほかの島なし 最大２歩
# 17 「の轤ュん
# 18 溶岩
# 19 サボロー
# 20 島ワープ＋もち

    #               番号,               名前,                画像,           画像2,         最低,  体力の, str  特殊, 経験値, 死体の  動物園  動物園
    #                                                                                       体力   幅         , 能力          値段    可      価値 *150億
    SetMonsterTable($Mons_MechaInora,   '人造メカいのら',   'monster7.gif', '',             2,       0,    1,     0,    5,      0,       100, 1);
    SetMonsterTable($Mons_Inora,        '怪獣いのら',       'monster0.gif', '',             1,       2,    2,     0,    5,      400,     100, 1);
    SetMonsterTable($Mons_Kamemusi,     '怪獣カメムシ',     'monster5.gif', 'monster4.gif', 1,       2,    3,     3,    7,      500,     100, 1);
    SetMonsterTable($Mons_Kuribo,       'クリボー',         'monster1.gif', '',             1,       2,    4,     0,    5,      1000,    100, 1);
    SetMonsterTable($Mons_KatuGin,     'カツ＝ギンサヨナラ','katugin.png',  '',             2,       2,    5,     1,    15,     800,     100, 1);
    SetMonsterTable($Mons_Pirates,      '海賊船',           'mship01.gif',  '',             3,       1,    1,     0,    20,     1500,    0,   0);

    SetMonsterTable($Mons_Teresa,       'テレサ',           'monster8.gif', '',             1,       0,    6,     2,    12,     300,     100, 1);
    SetMonsterTable($Mons_Met,          'メット',           'met.png',      'met_kouka.png',4,       2,    7,     4,    20,     1500,    100, 1);
    SetMonsterTable($Mons_KingInora,    '怪獣キングいのら', 'monster3.gif', '',             7,       2,    8,     0,    30,     5555,    100, 1);
    SetMonsterTable($Mons_Omu,          '古獣王蟲',         'monster18.gif','',             6,       0,    9,     1,    45,     2500,    0,   0);
    SetMonsterTable(26,                'ワープいのらキング','ghostking.gif','',             8,       4,   10,     14,   30,     10000,   25,  1);
    SetMonsterTable(27,                 'ビッグウンババ',   'monster27.png','',             7,       2,    8,     2,    30,     0,       0,   0);

    SetMonsterTable($Mons_MetaHamu,     '硬獣めたはむ',     'monster25.gif','monster25.gif',5,       2,   10,     8,    40,     3500,    100, 1);
    SetMonsterTable($Mons_Barimoa,      '怪獣バリモア',     'monster13.gif','',             7,       2,   11,     5,    35,     3000,    100, 1);
    SetMonsterTable($Mons_Slime,        '奇獣スライム',     'monster14.gif','',             2,       0,   12,     0,    5,      100,     90,  1);
    SetMonsterTable($Mons_HaneHamu,     '珍獣はねはむ',     'monster16.gif','',             5,       2,   13,     2,    40,     3500,    100, 1);

    SetMonsterTable($Mons_EnderInora,   'エンダーいのら',   'ghostking.gif','',             8,       4,   10,     14,   30,     15000,   10,  1);

    SetMonsterTable($Mons_Mikael,       '天使ミカエル',     'monster17.gif','',             10,      0,   14,     0,    99,     99999,   100, 1);
    SetMonsterTable($Mons_SlimeLegend, 'スライムレジェンド','monster19.gif','monster20.gif',5,       0,   15,     8,    70,     27000,   60,  1);
    SetMonsterTable($Mons_Raygira,      '魔獣レイジラ',     'monster22.gif','monster4.gif', 9,       0,   16,     8,    55,     10000,   100, 1);
    SetMonsterTable($Mons_Queen_inora, '魔獣クイーンいのら','monster21.gif','',             9,       0,   17,     5,    60,     12000,   100, 1);
    SetMonsterTable($Mons_f20,          '人造怪獣f02',      'f02.gif',      '',             8,       0,   18,     2,    85,     48000,   10,  1);
    SetMonsterTable($Mons_Uriel,        '天使ウリエル',     'monster23.gif','',             9,       0,   19,     0,    90,     80000,   5,   1);
    SetMonsterTable($Mons_Alfr,         '魔術師アールヴ',   'monster24.gif','',             2,       0,   20,     1,    95,     95000,   10,  2);
    SetMonsterTable($Mons_Ethereal,     '堕天使イセリア',   'monster26.gif','',             7,       0,   21,     7,    0,      85000,   20,  1);
    SetMonsterTable($Mons_Satan,        '魔王サタン',       'monster27.gif','',             10,      0,   22,     0,    80,     0,       2,   2);
    SetMonsterTable($Mons_Ice_scorpion,'アイススコーピオン','monster29.gif','',             9,       0,   23,     2,    40,     4000,    10,  2);
    SetMonsterTable(25,                 'ワープいのら',     'monsterghost.gif','',          6,       2,    8,     16,   20,     1500,    50,  1);
    SetMonsterTable($Mons_Volgenom,     'ヴォルゲロム',     'kaeru.gif',    '',             7,       0,   23,     18,   40,     4000,    20,  2);
    SetMonsterTable($Mons_Retro_inora,  'レトロいのら',     'retro.gif',   '',              6,       4,   22,     19,   55,     37564,   30,  1);

    SetMonsterTable(31,                 '｢の轤ｭん',         'monster82.gif','',             30,      10,  31,     17,   100,    9000,    80,  1);
    SetMonsterTable($Mons_Totten,       'トッテン',         'totten.png',   '',             7,       2,   24,     2,    30,     95000,   10,  1);
    SetMonsterTable($Mons_Wario,        'ワリオ',           'wario.png',    '',             32,      32,  25,     1,    120,    200000,  0,   0);

    SetMonsterTable($Mons_Kisinhei,     'きしんへい',       'kisinhei.png','kisinhei_curing.png', 8, 2,   36,     2,    90,     100000,  0,   0);
    SetMonsterTable(35,                 'ひめいのら',       'queen.gif',    '',             65530,   0,   35,     20,   0,      0,       0,   0);

    SetMonsterTable(28,                 'マスコットいのら', 'monster30.gif','',             0,       0,   28,     0,    0,      1,       0,   0);
    SetMonsterTable(29,                 '神獣テトラ',       'monster10.gif','',             5,       0,   29,     6,    7,      2000,    0,   0);
    SetMonsterTable($Mons_SuperTetra,   '超神獣テトラ',     'monster28.gif','',             11,      0,   30,     0,    99,     200000,  0,   0);

    SetMonsterTable(37,                 '番兵',             'monster28.gif','',             32,      0,   99,     0,    0,      2,       0,   0);

our @HmonsterTABLE = (0);
our $HmonsterLevel1TABLE_NUM;
our $HmonsterLevel2TABLE_NUM;
our $HmonsterLevel3TABLE_NUM;
our $HmonsterLevel4TABLE_NUM;
our $HmonsterLevel5TABLE_NUM;

#デバッグ用
our @DebugMonster = (37);

    {
        # レベルによって出現する怪獣をここに登録する。
        my @HmonsterLevel1Table = ( $Mons_Inora,  2,  3,  4, $Mons_Pirates,$Mons_Pirates,$Mons_Pirates);
        my @HmonsterLevel2Table = (  5,  6,  7,  8, 27, 25);
        my @HmonsterLevel3Table = (  9, 10, 11, 12);
        my @HmonsterLevel4Table = ( 13, 14, 15, 16, 17, 18, 19, 20, 22, 26 ,$Mons_Volgenom,$Mons_Retro_inora);
        my @HmonsterLevel5Table = ( 23, 24, 31 ,$Mons_Kisinhei );

        # このテーブルからひいてくるようにする。
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
# 油田
#----------------------------------------
# 油田の収入
$HoilMoney = 2500;

# 油田の枯渇確率
$HoilRatio = 80;

# 温泉の枯渇確率
$HonsenRatio = 10;

#----------------------------------------
# 大きな食べ物
#----------------------------------------
$Food_Kind_Shift = $Mons_Kind_Shift;
$Food_Kind_MASK = $Mons_Kind_MASK;
$Food_HP_MASK = $Mons_HP_MASK;
# 何種類あるか
$HBigFoodNum = 1;
# 名前
@BigFoodName = 
   (   
    '鏡餅',             #  0
    'チョコリス',       #  1
    'チョコレー都市',   #  2
    'ひしもち',         #  3
    'ポッキー',         #  4
    'プリッツ',         #  5
    'ポッチー',         #  6
    'プリッチ',         #  7
    '鏡餅'              #  banpei
    );
# 名前
@BigFoodImage = 
   (   
    'moti.gif',         #  0 鏡餅
    'chocolith.gif',    #  1 チョコリス
    'chocolatown.gif',  #  2 チョコレー都市
    'hisimoti.gif',     #  3 ひしもち
    'pocky.png',        #  4
    'pretz.png',        #  5
    'pochy.png',        #  6
    'prech.png',        #  7
    'moti.gif'          #  banpei
    );
# 名前
@BigFoodMoney = 
   (   
      200000,    #  0 鏡餅
      200000,    #  1 チョコリス
      200000,    #  2 チョコレー都市
      50000,     #  3 ひしもち
      50000,     #  4 ポッキー
      50000,     #  5 プリッツ
      50000,     #  6 ポッチー
      50000,     #  7 プリッチ
      2          #  banpei
    );

#----------------------------------------
# 記念碑
#----------------------------------------
# 何種類あるか
$HmonumentNumber = 44;
# $MonumentDust = 28;     #固定のゴミ箱
# 名前

# SetMonumentTable
SetMonumentTable(  0 , 'モノリス',  'monument0.gif');
SetMonumentTable(  1 , '聖樹',      'monument5.gif');
SetMonumentTable(  2 , '戦いの碑',  'monument3.gif');
SetMonumentTable(  3 , 'ラスカル',  'monument12.gif');
SetMonumentTable(  4 , '棺桶',      'monument11.gif');
SetMonumentTable(  5 , 'ヨーゼフ',  'monument13.gif');
SetMonumentTable(  6 , 'くま',      'monument16.gif');
SetMonumentTable(  7 , 'くま',      'monument15.gif');
SetMonumentTable(  8 , 'くま',      'monument14.gif');
SetMonumentTable(  9 , '雪だるま',  'monument17.gif');
SetMonumentTable( 10 , 'モアイ',    'monument18.gif');
SetMonumentTable( 11 , '地球儀',    'monument19.gif');
SetMonumentTable( 12 , 'バッグ',    'monument20.gif');
SetMonumentTable( 13 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 14 , 'ダークいのら像', 'monument4.gif');
SetMonumentTable( 15 , 'テトラ像',  'monument22.gif');
SetMonumentTable( 16 , 'はねはむ像','monument23.gif');
SetMonumentTable( 17 , 'ロケット',  'monument27.gif');
SetMonumentTable( 18 , 'ピラミッド','monument29.gif');
SetMonumentTable( 19 , 'アサガオ',  'monument30.gif');
SetMonumentTable( 20 , 'バラ(赤)',  'monument31.gif');
SetMonumentTable( 21 , 'バラ(黄)',  'monument32.gif');
SetMonumentTable( 22 , 'パンジー',  'monument33.gif');
SetMonumentTable( 23 , '仙人掌(丸型)','monument34.gif');
SetMonumentTable( 24 , '仙人掌(小型)','monument35.gif');
SetMonumentTable( 25 , '魔方陣',    'monument40.gif');
SetMonumentTable( 26 , '神殿',      'monument46.gif');
SetMonumentTable( 27 , '神社',      'monument47.gif');
SetMonumentTable( 28 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 29 , 'こんぺいとう','kon.png');
SetMonumentTable( 30 , 'ワンワン岩','wanwan.png');
SetMonumentTable( 31 , 'クリスマスツリー','monument37.gif');
SetMonumentTable( 32 , 'クリスマスツリー','monument9.gif');
SetMonumentTable( 33 , '自然公園',  'nature.png');
SetMonumentTable( 34 , '桜',        'monument26.gif');
SetMonumentTable( 35 , '向日葵',    'monument28.gif');
SetMonumentTable( 36 , '銀杏',      'monument36.gif');
SetMonumentTable( 37 , '雪うさぎ',  'monument38.gif');
SetMonumentTable( 38 , '車両',      'train103.png');
SetMonumentTable( 39 , 'カービィ',  'kirby.png');
SetMonumentTable( 40 , '偽ミバ像',  'miv.png');
SetMonumentTable( 41 , 'ぬいぐるみ','mog.png');
SetMonumentTable( 42 , '駅',        'station.gif');
SetMonumentTable( 43 , 'モナド',    'xe.png');
SetMonumentTable( 44 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 45 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 46 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 47 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 48 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 49 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 50 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 51 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 52 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 53 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 54 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 55 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 56 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 57 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 58 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 59 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 60 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 61 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 62 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 63 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 64 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 65 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 66 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 67 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 68 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 69 , 'ごみ箱',    'monument21.gif');
SetMonumentTable( 70 , 'ゲート',    'gate70.gif');
SetMonumentTable( 71 , '動作確認用', 'monument0.gif');
SetMonumentTable( 72 , 'トーマ・バンガルテル', 'Thomas.png');
SetMonumentTable( 73 , 'ギ＝マニュエル', 'Gi.png');
SetMonumentTable( 74 , '闇石',      'monument53.gif');
SetMonumentTable( 75 , '地石',      'monument52.gif');
SetMonumentTable( 76 , '氷石',      'monument48.gif');
SetMonumentTable( 77 , '風石',      'monument49.gif');
SetMonumentTable( 78 , '炎石',      'monument50.gif');
SetMonumentTable( 79 , '光石',      'monument51.gif');
SetMonumentTable( 80 , '卵',        'monument41.gif');
SetMonumentTable( 81 , '卵',        'monument42.gif');
SetMonumentTable( 82 , '卵',        'monument43.gif');
SetMonumentTable( 83 , '卵',        'monument44.gif');
SetMonumentTable( 84 , '古代遺跡',  'monument45.gif');
SetMonumentTable( 85 , 'Millenniumクリスマスツリー', 'monument9.gif');
SetMonumentTable( 86 , '壊れた侵略者',  'monument24.gif');
SetMonumentTable( 87 , '王蟲の脱け殻',  'monument25.gif');
SetMonumentTable( 88 , '桜',        'monument26.gif');
SetMonumentTable( 89 , '向日葵',    'monument28.gif');
SetMonumentTable( 90 , '銀杏',      'monument36.gif');
SetMonumentTable( 91 , 'クリスマスツリー2001', 'monument37.gif');
SetMonumentTable( 92 , '雪うさぎ',  'monument38.gif');
SetMonumentTable( 93 , '幸福の女神像','monument54.gif');
SetMonumentTable( 94 , '豚の香取くん','katori.gif');
SetMonumentTable( 95 , '200億で油田の碑','monument_200oil.gif');
SetMonumentTable( 96 , 'ご神体',    'your_name.gif' );


#----------------------------------------
# 卵
#----------------------------------------
$HEggKindMax = 4;
# 画像ファイル
@HEggImage = 
    (
    'monument41.gif',
    'monument42.gif',
    'monument43.gif',
    'monument44.gif'
    );

#----------------------------------------
# 船
#----------------------------------------
# 何種類あるか
$HfuneNumber = 12;

$HcomFrocity_num = 77;      # メガフロート用

# 名前
@HfuneName =
	(
	 '小型漁船',            #  0
	 '小型漁船',            #  1
	 '中型漁船',            #  2
	 '海底探査船',          #  3
	 '帆船',                #  4
	 '大型漁船',            #  5
	 '高速漁船',            #  6
	 '海底探査船・改',      #  7
	 '豪華客船TITANIC',     #  8
	 '戦艦RENAS',           #  9
	 '戦艦ERADICATE',       # 10
	 '漁船MASTER',          # 11
	 'モノリス',            # 12
	 'モノリス',            # 13
	 'モノリス',            # 14
	 'モノリス',            # 15
	 'モノリス',            # 16
	 'モノリス',            # 17
	 'モノリス',            # 18
	 '戦艦ERADICATE・改'    # 19
	);

@HfuneFood = 
	(
	 1,	 1,	 1,	 0,	 0,	 1,	 1,	 0,	 0,	 0,	 0,	 1,	 0,	 0,	 0,	 0,	 0,	 0,	 0,	 0	);


#                 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
@HfuneSpecial = ( 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 5, 0);
# 特殊能力の内容は、
# 0 特になし
# 1 足が速い(最大2歩あるく)
# 2 足がとても速い(最大何歩あるくか不明)

# 画像ファイル
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
# 人工衛星
#----------------------------------------
# 名前
our @HeiseiName =
   ( '気象衛星',  '気象衛星',  '観測衛星',    '迎撃衛星',    '軍事衛星',  '防衛衛星',  'イレギュラー' );

# 画像ファイル
our @HeiseiImage =
   ( 'kisho.gif', 'kisho.gif', 'kansoku.svg', 'geigeki.gif', 'gunji.gif', 'bouei.gif', 'ire.gif' );

our $HeiseiNumber = @HeiseiName;

#----------------------------------------
# 島主の家
#----------------------------------------
our @HHouseName;
$HHouseName[0] = '小屋';
$HHouseName[1] = '簡易住宅';
$HHouseName[2] = '住宅';
$HHouseName[3] = '高級住宅';
$HHouseName[4] = '豪邸';
$HHouseName[5] = '大豪邸';
$HHouseName[6] = '高級豪邸';
$HHouseName[7] = '城';
$HHouseName[8] = '巨城';
$HHouseName[9] = '黄金城';


#----------------------------------------
# 線路
#----------------------------------------
our $HTrainBase = 10;

our $HTrainMAX = 22;


#----------------------------------------
our @BUMON_NAME;
our @BUMON_ELEMENTS;
our @BUMON_ICON;

    SetBumonTable(0  , '人口'             , 'pop'           , "./${HMapImgDir}land502.png");
    SetBumonTable(1  , '農場'             , 'farm'          , './img/prize/p_fa.gif');
    SetBumonTable(2  , '職場'             , 'factory'       , "./${HMapImgDir}land8.gif");
    SetBumonTable(3  , '採掘場'           , 'mountain'      , "./${HMapImgDir}land15.gif");
    SetBumonTable(4  , '森林'             , 'fore'          , "./${HMapImgDir}land6.gif");
    SetBumonTable(5  , 'にわとり数'       , 'tare'          , "./img/prize/niwatori_up.gif");
    SetBumonTable(6  , 'ぶた数'           , 'zipro'         , "./img/prize/buta_up.png");
    SetBumonTable(7  , 'うし数'           , 'leje'          , "./img/prize/ushi_up.gif");
    SetBumonTable(8  , '怪獣出現数'       , 'monsterlive'   , "./${HMapImgDir}monster0.gif");
    SetBumonTable(9  , '怪獣退治数'       , 'taiji'         , "./${HMapImgDir}monster0.gif");
    SetBumonTable(10 , '成長度'           , 'monta'         , "./img/prize/prize11.svg");
    SetBumonTable(11 , '人口増加'         , 'hamu'          , "./${HMapImgDir}land502.png");
    SetBumonTable(12 , '収入'             , 'pika'          , "./img/prize/money.gif");
    SetBumonTable(13 , '記念碑数'         , 'kei'           , "./${HMapImgDir}monument0.gif");
    SetBumonTable(14 , '軍事技術'         , 'renae'         , "./${HMapImgDir}land37.gif");
    SetBumonTable(15 , '生物大学能力'     , 'force'         , "./img/mascot.png");
    SetBumonTable(16 , '通算観光客'       , 'eisei2'        , "./${HMapImgDir}land43.gif");
    SetBumonTable(17 , 'ユニーク地形数'   , 'uni'           , "./${HMapImgDir}monument0.gif");
    SetBumonTable(18 , 'サッカーチーム力' , 'teamforce'     , "./img/sc.gif");
    SetBumonTable(19 , 'HC 優勝回数'      , 'styusho'       , "./img/sc.gif");
    SetBumonTable(20 , 'HC 通算勝率'      , 'shoritu'       , "./img/sc.gif");
    SetBumonTable(21 , 'HC 通算勝点'      , 'kachitent'     , "./img/sc.gif");
    SetBumonTable(22 , "HC${hcturn} 勝点" , 'kachiten'      , "./img/sc.gif");
    SetBumonTable(23 , '100ターン成長'    , 'tha_diff'      , "./img/prize/pr100.svg");
    SetBumonTable(24 , '動物園怪獣数'     , 'zoo_Mons_cnt'  , "./${HMapImgDir}land84.gif");
    SetBumonTable(25 , 'ハイテク'         , 'factoryHT'     , "./${HMapImgDir}land85.gif");
    SetBumonTable(26 , '島面積'           , 'area'          , "./img/prize/island.gif");


#
sub SetBumonTable {
    my ($no, $name, $ele, $icon) = @_;

    $BUMON_NAME[$no] = $name;
    $BUMON_ELEMENTS[$no] = $ele;
    $BUMON_ICON[$no] = $icon;
}


#----------------------------------------
# 賞関係
#----------------------------------------
# ターン杯を何ターン毎に出すか
our $HturnPrizeUnit = 100;

# 賞の名前
our @Hprize;
$Hprize[0] = 'ターン杯';
$Hprize[1] = '繁栄賞';
$Hprize[2] = '超繁栄賞';
$Hprize[3] = '究極繁栄賞';
$Hprize[4] = '平和賞';
$Hprize[5] = '超平和賞';
$Hprize[6] = '究極平和賞';
$Hprize[7] = '災難賞';
$Hprize[8] = '超災難賞';
$Hprize[9] = '究極災難賞';


#----------------------------------------------------------------------
# 地雷
#----------------------------------------------------------------------
our $Hmine_DAMAGE_MASK = 0x00FF;
our $Hmine_SEA_FLAG = 0x800000;

#----------------------------------------------------------------------
# 料金設定
#----------------------------------------------------------------------
our $HYakusho_Narasi = 700 ;
our $HYakusho_Narasi2 = 1400 ;

#----------------------------------------------------------------------
# 地形変化
#----------------------------------------------------------------------
# random(100)
our $To_Sunahama_par = 5;
our $To_Ice_par = 1;

our $Sunahama_To_Sea_par = 30;
our $Ice_To_Sea_par = 10;

our $HForest_Limit = 800 ;

#----------------------------------------------------------------------
# 人数制限
#----------------------------------------------------------------------
our $HTown_growstop = 100 ;     # 町の人数制限
our $HTown_limit    = 250 ;     # 町の人数制限
our $HOnsen_limit   = 100 ;     # 温泉の人数制限

our $HProcity_growstop = 100 ;  # 防災都市の人数制限
our $HProcity_limit = 200 ;     # 防災都市の人数制限

our $HFrocity_limit = 200 ;     # メガフロートの人数制限
our $HSeatown_limit = 400 ;     # 海底都市の人数制限
our $HBigtown_limit = 500 ;     # 現代都市系
our $HShrine_limit  = 200;
our $HBettown_limit = 2000;     # 輝ける都市

our $HUmicity_growstop = 2000;  # 海都市
our $HUmicity_limit = 3000;     # 海都市

our $HNewtown_growstop = 100 ;  # ニュータウンの人数制限
our $HNewtown_limit = 300 ;     # ニュータウンの人数制限

our $HShuto_growstop = 750 ;    # 首都の人数制限
our $HShuto_limit   = 4000 ;    # 首都の人数制限

our $HMountain_add   = 5;
our $HMountain_limit = 200;


our $HGold_add      = 20;
our $HGold_limit    = 200;

our $HLivestock_limit = 4000;       # 家畜上限


our $HFactory_add   = 10;           # 工場 追加
our $HFactory_base  = 30;           # 工場 追加
our $HFactory_limit = 100;          # 工場 制限

# いのらランド
our $HInoraland_add = 30;
our $HInoraland_limit = 1500;

# ハイテク企業
our $HlandSHTF_add = 2;
our $HlandSHTF_limit = 500 + 350;

# ハイテク企業
our $HlandHTFactory_add = 2;
our $HlandHTFactory_limit =500 + 250;

our $HFoodim_add    = 10;           # 食物研究所 追加
our $HFoodim_base   = 30;           # 食物研究所 追加
our $HFoodim_limit  = 500;          # 食物研究所 制限

our $HPark_add      = 30;           # 遊園地
our $HIce_add       = 25;           # 遊園地
our $HPark_base     = 10;           # 遊園地
our $HPark_limit    = 100;          # 遊園地

our $HNursery_add = 5;
our $HNursery_base = 20;
our $HNursery_limit = 100;

our $HHTFactory_add = 10;        #ハイテク企業 追加
our $HHTFactory_limit = 500;        #ハイテク企業 追加

our $HUmiamu_limit = 1000;
our $HUmiamu_add = 30;
our $HUmiamu_base = 50;

our $HInoraLand_limit = 1500;
our $HInoraLand_add = 30;
# baseは　$HPark_limit


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
# 気温
#----------------------------------------------------------------------
#                          0,   1,   2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12月
our @HTemperatureMax = (  25,  25,  24, 25, 27, 30, 33, 35, 35, 34, 33, 28, 26); # 
our @HTemperatureAve = (   8,   8,   9, 10, 15, 21, 23, 29, 29, 24, 19, 13,  8); # 平均
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
# 物資管理
#----------------------------------------------------------------------
our @HProduct_Food_hash_table = (
    'kome' , 'yasai' , 'kudamono', 'seafood' , 'sio' , 
    'toriniku', 'butaniku' , 'gyuniku', 'nazoniku' , 'tamago'
);

our @HProduct_Name;
$HProduct_Name{'kome'}      = 'コメ';
$HProduct_Name{'yasai'}     = '野菜';
$HProduct_Name{'kudamono'}  = 'くだもの';
$HProduct_Name{'seafood'}   = '魚介類';
$HProduct_Name{'sio'}       = '塩';
$HProduct_Name{'toriniku'}  = '鶏肉';
$HProduct_Name{'butaniku'}  = '豚肉';
$HProduct_Name{'gyuniku'}   = '牛肉';
$HProduct_Name{'nazoniku'}  = 'なぞ肉';
$HProduct_Name{'tamago'}  = 'たまご';

our @HProduct_unitName;
$HProduct_unitName{'kome'}      = '00トン';
$HProduct_unitName{'yasai'}     = '00トン';
$HProduct_unitName{'kudamono'}  = '00トン';
$HProduct_unitName{'seafood'}   = '00トン';
$HProduct_unitName{'sio'}       = '00トン';
$HProduct_unitName{'toriniku'}  = '00トン';
$HProduct_unitName{'butaniku'}  = '00トン';
$HProduct_unitName{'gyuniku'}   = '00トン';
$HProduct_unitName{'nazoniku'}  = '00トン';
$HProduct_unitName{'tamago'}  = '00トン';


#----------------------------------------------------------------------

our $HStadiumResult = ('練習中',       '予選第１戦待ち', '予選第２戦待ち', '予選第３戦待ち', '予選第４戦待ち',
             '予選終了待ち', '準々決勝戦待ち', '準決勝戦待ち',   '決勝戦待ち', '優勝！',
             '練習中',       '予選落ち',       '準々決勝負け',   '準決勝負け', '第２位');

#----------------------------------------------------------------------
# 防衛基地
#----------------------------------------------------------------------
our $HDefenceLevelMask = 0x0F;
our $HDefenceHP_SHIFT  = 4;
our $HDefenceTurnCost  = 2200;

#----------------------------------------------------------------------
# 役所
#----------------------------------------------------------------------
our $HYakushoMAXLevel  = 6;
our $HYakushoWorkExist = 0x01;
our $HYakushoWorkYotei = 0x02;
our $HYakushoWorkSeiti = 0x04;

#----------------------------------------------------------------------
# 島 effect
#----------------------------------------------------------------------
our $g_Island_Chaff = 0x01;
our $g_Island_Retro = 0x02;

#----------------------------------------------------------------------
# 線路
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
# アイテムMAX
#----------------------------------------------------------------------
our $HItem_MAX = 5;
our $HItem_Nothing = 0;


our $HFiredept_cost = 3;
our $HFiredept_guard = 1;       #0.1%
our $HFiredept_save = 50;       # 50 %

#----------------------------------------------------------------------
# スペース、スペース、スペーーーース
#----------------------------------------------------------------------
our $HRocket_SpaceDebri = 50;
our $HRocketMiss_SpaceDebri = 70;
our $HRocketBroken_SpaceDebri = 100;
our $HSpaceDebri_meteo = 1000;
our $HSpaceDebri_evapo = 3;



#----------------------------------------------------------------------
# 市民の要求
#----------------------------------------------------------------------
our $HCivReq_None = 0;
our $HCivReq_TaxDown = 1;

our $HCivReq_FailTurn = (12*8);

#----------------------------------------------------------------------
# 番号, 名前, 画像
sub SetMonumentTable {
    my ($no, $name, $image) = @_;

    $HmonumentName[$no] = $name;
    $HmonumentImage[$no] = $image;
}

# 番号, 画像, 画像2, 最低体力, 体力の幅, 特殊能力, 経験値, 死体の値段, 動物園許可
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

