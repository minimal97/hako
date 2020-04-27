#----------------------------------------------------------------------
# minimal97 の 箱庭諸島
# プロダクト・リストモードモジュール
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
require './init-game.cgi';

#----------------------------------------------------------------------
#----------------------------------------------------------------------
sub food_product_plus {
    my ($island , $product , $val) = @_;

    $island->{$product} += $val;
    $island->{$product} = min((INIT_MAXIMUM_FOOD * 2),$island->{$product});

    $island->{'food'} += $val;
}

#----------------------------------------------------------------------
#
#   サタン用
#
sub food_product_All_Clear {
    my ($island) = @_;
    my ($product);

    foreach $product (@HProduct_Food_hash_table) {

        $island->{$product} = 0;
    }

    $island->{'food'} = 0;
}


#----------------------------------------------------------------------
#
#
sub food_product_Random_consumption {
    my ($island , $consumption) = @_;

    if ($consumption == 0) {
        return (0);
    }

    $island->{'food'} -= $consumption;
    $island->{'food'} = ($island->{'food'} < 0) ? 0 : ($island->{'food'});

    my (@product_list) = ();
    my ($product_num) = 0;
    my ($product_sum) = 0;

    my ($product);
    foreach $product (@HProduct_Food_hash_table) {

        if (   ($island->{$product})
            && ($island->{$product} > 0)) {

            $product_list[$product_num] = $product;
            $product_num += ($island->{$product}) ? 1 : 0;
            $product_sum += ($island->{$product});
        }
    }

    if (   ($product_sum < $consumption)
        && ($island->{'food'} <= 0)) {
        food_product_All_Clear($island);
        return (0);
    }

    # 緊急
    if (   ($product_sum < $consumption)) {
        return (0);
    }

    my ($cons);
    my ($tar);
    my ($tarhash);
    for ( ; ; ) {

        $cons = 5 + random(20);
        $cons = min($cons , $consumption);
        $cons = min($cons , $product_sum);
        $tar = random($product_num);
        $tarhash = $product_list[$tar];

        if ($island->{$tarhash} >= $cons) {

            $island->{$tarhash} -= $cons;

        }else{

            $cons = min($island->{$tarhash} , $cons);
            $island->{$tarhash} = 0;

            splice(@product_list, $tar, 1);
            $product_num--;
        }

        $product_sum -= $cons;
        $consumption -= $cons;
        if ($consumption <= 0) {
            last;
        }
    }

    return (0);
}


#----------------------------------------------------------------------
#
#   オーバーヘッドをカット
#
sub food_product_overheadcut {
    my ($island) = @_;

    my (@product_list) = ();
    my ($product_num) = 0;
    my ($product_sum) = 0;
    my ($product);
    foreach $product (@HProduct_Food_hash_table) {

        if (   ($island->{$product})
            && ($island->{$product} > 0)) {

            $product_list[$product_num] = $product;
            $product_num += 1;
            $product_sum += ($island->{$product});
        }
    }


    if ($product_sum <= INIT_MAXIMUM_FOOD) {
        return (0);
    }

    my ($cut) = $product_sum - INIT_MAXIMUM_FOOD;

    my ($cons);
    my ($tar);
    my ($tarhash);
    for ( ; ; ) {

        $cons = 2 + random(20);
        $cons = min($cons , $cut);
        $cons = min($cons , $product_sum);
        $tar = random($product_num);
        $tarhash = $product_list[$tar];

        if ($island->{$tarhash} >= $cons) {

            $island->{$tarhash} -= $cons;

        }else{

            $cons = min($island->{$tarhash} , $cons);
            $island->{$tarhash} = 0;

            splice(@product_list, $tar, 1);
            $product_num--;
        }

        $product_sum -= $cons;
        $cut -= $cons;
        if ($cut <= 0) {
            last;
        }
    }
}


#----------------------------------------------------------------------
#
#
sub food_product_Random_consumption_zantei {
    my ($island , $consumption) = @_;

    if ($consumption == 0) {
        return (0);
    }

    my (@product_list) = ();
    my ($product_num) = 0;
    my ($product_sum) = 0;

    my ($product);
    foreach $product (@HProduct_Food_hash_table) {

        if (   ($island->{$product})
            && ($island->{$product} > 0)) {

            $product_list[$product_num] = $product;
            $product_num += ($island->{$product}) ? 1 : 0;
            $product_sum += ($island->{$product});
        }
    }

    if (   ($product_sum < $consumption)
        && ($island->{'food'} <= 0)) {
        food_product_All_Clear($island);
        return (0);
    }

    # 緊急
    if (   ($product_sum < $consumption)) {
        return (0);
    }

    my ($cons);
    my ($tar);
    my ($tarhash);
    for ( ; ; ) {

        $cons = 5 + random(20);
        $cons = min($cons , $consumption);
        $cons = min($cons , $product_sum);
        $tar = random($product_num);
        $tarhash = $product_list[$tar];

        if ($island->{$tarhash} >= $cons) {

            $island->{$tarhash} -= $cons;

        }else{

            $cons = min($island->{$tarhash} , $cons);
            $island->{$tarhash} = 0;

            splice(@product_list, $tar, 1);
            $product_num--;
        }

        $product_sum -= $cons;
        $consumption -= $cons;
        if ($consumption <= 0) {
            last;
        }
    }

    {
        $product_sum = 0;
        foreach $product (@product_list) {

            $product_sum += $island->{$product};
            $island->{$product} = min($island->{$product} , INIT_MAXIMUM_FOOD);     # いらなくなるはず
        }
    }
    return (0);
}

#----------------------------------------------------------------------
#
#
sub food_export {
    my ($island , $tIsland ,$value ) = @_;

    $island->{'food'} -= $value;
    $tIsland->{'food'} += $value;
    $island->{'ext'}[1] += int($value/10); # 貢献度
    $tIsland->{'ext'}[1] -= int($value/10); # 貢献度

    my (@product_list) = ();
    my ($product_num) = 0;
    my ($product_sum) = 0;

    {
        my ($product);
        foreach $product (@HProduct_Food_hash_table) {

            if (   ($island->{$product})
                && ($island->{$product} > 0)) {

                $product_list[$product_num] = $product;
                $product_num += ($island->{$product}) ? 1 : 0;
                $product_sum += ($island->{$product});
            }
        }
    }

    $value = min($product_sum , $value);

    {
        my ($temp);
        my ($dice);
        my ($product);

        while ($value > 0) {

            $temp = (1 + random(($value/100))) * 100;
            $dice = random($product_num);

            $product = $product_list[$dice];

            $temp = min($temp , $island->{$product});
            if ($island->{$product}) {

                $island->{$product} -= $temp;
                $tIsland->{$product} += $temp;
            }

            $value -= $temp;
            $product_sum -= $temp;

            if ($product_sum <= 0) {
                last;
            }
        }
    }

}


#----------------------------------------------------------------------
#
#
sub food_product_consumption {
    my ($island , $consumption) = @_;

    if ($consumption <= 0) {
        return (0);
    }

    my ($foodkind) = 0;                     # 食べ物の種類

    $island->{'food'} -= $consumption;

    my (%product_wk) = ();
    my ($over) = 0;
    my ($consumption_for_sio) = int($consumption * 0.04);

    if ($island->{'sio'} <= 0) {
        $foodkind++;                        # 食べ物の種類
        if (($island->{'sio'} >= $consumption_for_sio)) {

            $island->{'sio'} -= $consumption_for_sio;
            $over = 0;
        }
        else {

            $over = $consumption_for_sio = $island->{'sio'};
            $island->{'sio'} = 0;
        }
    }

    $consumption += $over - $consumption_for_sio;

    my ($product);
    my ($product_num);
    foreach $product (@HProduct_Food_hash_table) {

        if ($product eq 'sio' ) {
            # 除外
        }
        else {
            $product_wk{$product} = $island->{$product};
            $product_num += ($island->{$product}) ? 1 : 0;
        }
    }

    my ($ave);
    if ($product_num) {
        $ave = int($consumption / $product_num);
    }
    else {
        $ave = 0;
    }

    my ($food_val) = 0;
    for my $key (sort {$product_wk{$a} <=> $product_wk{$b}} keys %product_wk) {

        $food_val = ($island->{$key}) ? ($island->{$key}) : 0 ;
        next if ($food_val <= 0);

        if ($island->{$key} >= $ave) {

            $over = 0;
            $island->{$key} -= $ave;

        }else{

            $over = $ave - $island->{$key};
            $island->{$key} = 0;
        }

        $consumption -= $ave;
        $consumption += $over;
        $foodkind++;                        # 食べ物の種類
        last if ($consumption <= 0);

        $product_num--;
        next if ($product_num <= 0);

        $ave = int($consumption / $product_num);
    }

    $island->{'food'} = ($island->{'food'} < 0) ? 0 : ($island->{'food'});

    my ($product_sum) = 0;
    foreach $product (@HProduct_Food_hash_table) {

        if (   ($island->{$product})
            && ($island->{$product} > 0)) {

            $product_sum += ($island->{$product});
        }
    }

    return ($foodkind);
}


#----------------------------------------------------------------------
#
#

sub food_product_check {
    my ($island) = @_;

    my ($product_sum) = 0;

    my ($product);
    foreach $product (@HProduct_Food_hash_table) {

        if (   ($island->{$product})
            && ($island->{$product} > 0)) {

            $product_sum += ($island->{$product});
        }
    }

    if ($island->{'food'} != $product_sum) {

        my ($val) = ($island->{'food'} - $product_sum);

        food_product_hosei($island, $val);
        logOut("debug：食べ物の数が不一致：$island->{'food'} / $product_sum", $island->{'id'});
    }
}


#----------------------------------------------------------------------
#
#   雑な補正
#
sub food_product_hosei {
    my ($island , $val) = @_;

    my ($hosei) = 50 + random(400);

    if ($val < 0) {
        $hosei = -$hosei;
        $hosei = max($hosei , $val);
    }
    else {
        $hosei = min($hosei , $val);
    }

    my ($product_sum) = 0;
    my ($product);
    foreach $product (@HProduct_Food_hash_table) {

        if (   ($island->{$product})
            && ($island->{$product} > 0)) {

            if (1) {
                $island->{$product} += $hosei;
                last;
            }
        }
    }
}


1;