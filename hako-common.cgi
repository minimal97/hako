# すべての定数をここにまとめる！
require './init-server.cgi';
require './init-game.cgi';


#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub CalcCostbyPoint {
    my ($cost , $island) = @_;

    my ($temp_cost);
    $temp_cost = $cost;
    if ($temp_cost =~ s/Pointx(.*)$//g) {
        $cost = $island->{'pts'} * int($1);
    }
    else {
        $cost = $temp_cost;
    }

    return $cost;
}


#----------------------------------------------------------------------
# 
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
# 
#----------------------------------------------------------------------
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


1;

