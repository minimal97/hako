
#----------------------------------------------------------------------
# 各種定数
#----------------------------------------------------------------------
# 地形番号
our $HlandSea       = 0;    # 海
use constant SEA_SHALLOWS_VAL => 1; # 浅瀬

our $HlandWaste     = 1;    # 荒地
use constant LAND_WASTE => 1; # 荒地
our $HlandPlains    = 2;    # 平地
our $HlandTown      = 3;    # 町系
our $HlandForest    = 4;    # 森
our $HlandFarm      = 5;    # 農場
our $HlandFactory   = 6;    # 工場
our $HlandBase      = 7;    # ミサイル基地
our $HlandDefence   = 8;    # 防衛施設
our $HlandMountain  = 9;    # 山
our $HlandMonster   = 10;   # 怪獣

our $HlandSbase     = 11;   # 海底基地
our $HlandOil       = 12;   # 海底油田
our $HlandMonument  = 13;   # 記念碑
our $HlandHaribote  = 14;   # ハリボテ
our $HlandSeacity   = 15;   # 海底都市
our $HlandPark      = 16;   # 遊園地
our $HlandMinato    = 17;   # 港
our $HlandFune      = 18;   # 船舶
our $HlandMine      = 19;   # 地雷
our $HlandNursery   = 20;   # 養殖場

our $HlandKyujo     = 21;   # 野球場
our $HlandUmiamu    = 22;   # 海あみゅ
our $HlandFoodim    = 23;   # 食物研究所
our $HlandProcity   = 24;   # 防災都市
our $HlandGold      = 25;   # 金山
our $HlandSeki      = 26;   # 関所
our $HlandRottenSea = 27;   # 腐海
our $HlandNewtown   = 28;   # ニュータウン
our $HlandBigtown   = 29;   # 現代都市
our $HlandSeatown   = 30;   # 海底ニュー

our $HlandFarmchi   = 31;   # 養鶏場
our $HlandFarmpic   = 32;   # 養豚場
our $HlandFarmcow   = 33;   # 牧場
our $HlandCollege   = 34;   # 大学
our $HlandFrocity   = 35;   # 海上都市
our $HlandSunahama  = 36;   # 砂浜
our $HlandOnsen     = 37;   # 温泉
our $HlandHouse     = 38;   # 島主の家
our $HlandShuto     = 39;   # 首都
our $HlandUmishuto  = 40;   # 海底首都

our $HlandIce       = 41;   # 氷河
our $HlandRizort    = 42;   # リゾート地
our $HlandBettown   = 43;   # 輝ける都市
our $HlandKyujokai  = 44;   # 多目的スタジアム
our $HlandBigRizort = 45;   # 臨海リゾートホテル
our $HlandHTFactory = 46;   # ハイテク企業
our $HlandSHTF      = 47;   # ハイテク企業・改
our $HlandUmicity   = 48;   # 海都市系
our $HlandYakusho   = 49;   # 島役所
our $HlandKatorikun = 50;   # 香取君

our $HlandEgg       = 51;   # 卵
our $HlandAirport   = 52;   # 空港
our $HlandFire      = 53;   # 消防署
our $HlandHospital  = 54;   # 病院
our $HlandOmamori   = 55;   # お守
our $HlandOilCity   = 56;   # 油田都市
our $HlandFiredept  = 57;   # 消防署
our $HlandRocket    = 58;   # ロケット
our $HlandInoraLand = 59;   # いのらランド
our $HlandYougan    = 60;   # 溶岩

our $HlandInaka     = 61;   # いなか
our $HlandCeleb     = 62;   # セレブの町
our $HlandAtmoth    = 63;   # アトモス
our $HlandTrain     = 64;   # 線路
our $HlandZoo       = 65;   # 動物園
our $HlandStation   = 66;   # 駅
our $HlandBeachPark = 67;   # 海水浴場

our $HlandGomi      = 68;   # ごみ置き場
our $HlandGomiFactory = 69; # ごみ処理場
our $HlandBoueki    = 70;   # 
our $HlandCamp      = 71;   # キャンプ場

our $HlandBayResort = 72;   # ベイリゾート

our $HlandShrine    = 98;   # 時の神殿 34
our $HlandHugeMonster = 99; # 巨大怪獣 35
our $HlandBigFood   = 100;  # 大きな食べ物

1;
