#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# ターン進行モジュール(ver1.02)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# Hakoniwa R.A. ver1.11
# メインスクリプト(箱庭諸島 ver2.30)
# 使用条件、使用方法等は、read-renas.txtファイルを参照
#
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# 定数
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# include
#----------------------------------------------------------------------
require('./hako-turn_log.cgi');     # ログ出力ファイル
require('./hako-turn_monster.cgi'); # スパゲッティ 怪獣処理を引っ越してゆく
require('./hako-turn_food.cgi');


#----------------------------------------------------------------------
# static
#----------------------------------------------------------------------


#----------------------------------------------------------------------
#----------------------------------------------------------------------


# ---------------------------------------------------------------------
# 通常の山
# ---------------------------------------------------------------------
sub SetMountain_Normal {
    my ($island , $x , $y) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    $land->[$x][$y] = $HlandMountain;
    $landValue->[$x][$y] = 0;
    $landValue2->[$x][$y] = 0;
    $landValue3->[$x][$y] = 0;
}

# ---------------------------------------------------------------------
# 記念碑の設置 val指定
# ---------------------------------------------------------------------
sub SetMonument_Normal {
    my ($island , $x , $y , $val) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    $land->[$x][$y] = $HlandMonument;
    $landValue->[$x][$y] = $val;
    $landValue2->[$x][$y] = 0;
    $landValue3->[$x][$y] = 0;
}


# ---------------------------------------------------------------------
# 溶岩
# ---------------------------------------------------------------------
sub SetYoganLand {
    my ($island , $x , $y) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    $land->[$x][$y] = $HlandYougan;
    $landValue->[$x][$y] = random(3) + 2;
    $landValue2->[$x][$y] = 0;
    $landValue3->[$x][$y] = 0;
}


# ---------------------------------------------------------------------
# 通常の荒れ地
# ---------------------------------------------------------------------
sub SetWasteLand_Normal {
    my ($island , $x , $y) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    $land->[$x][$y] = $HlandWaste;
    $landValue->[$x][$y] = 0;
    $landValue2->[$x][$y] = 0;
    $landValue3->[$x][$y] = 0;
}


# ---------------------------------------------------------------------
# 通常の荒れ地
# ---------------------------------------------------------------------
sub SetWasteLand_Normal_val {
    my ($island , $x , $y , $val) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    $land->[$x][$y] = $HlandWaste;
    $landValue->[$x][$y] = $val;
    $landValue2->[$x][$y] = 0;
    $landValue3->[$x][$y] = 0;
}


# ---------------------------------------------------------------------
# 海上油田
# ---------------------------------------------------------------------
sub SetOilLand {
    my ($island , $x , $y) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    $land->[$x][$y] = $HlandOil;
    $landValue->[$x][$y] = 0;
    $landValue2->[$x][$y] = 0;
    $landValue3->[$x][$y] = 0;
    $island->{'oil'}++;
}


# ---------------------------------------------------------------------
# モンスター配置
# ---------------------------------------------------------------------
sub SetMonsterLand_Normal {
    my ($island , $x , $y , $mkind) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    my ($lv) = Calc_MonsterLandValue($mkind);

    $land->[$x][$y] = $HlandMonster;
    $landValue->[$x][$y] = $lv;
    $landValue2->[$x][$y] = 0;
    $landValue3->[$x][$y] = 0;


    $island->{'monspnt'}->[$island->{'monsterlive'}] = { x => $x, y => $y };
    $island->{'monsterlive'}++;
}


# ---------------------------------------------------------------------
# 通常の海
# ---------------------------------------------------------------------
sub SetSeaLand_Normal {
    my ($island , $x , $y) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    $land->[$x][$y] = $HlandSea;
    $landValue->[$x][$y] = 0;
    $landValue2->[$x][$y] = 0;
    $landValue3->[$x][$y] = 0;
}


# ---------------------------------------------------------------------
# 通常の海
# ---------------------------------------------------------------------
sub SetSeaShallowLand {
    my ($island , $x , $y) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    $land->[$x][$y] = $HlandSea;
    $landValue->[$x][$y] = 1;
    $landValue2->[$x][$y] = 0;
    $landValue3->[$x][$y] = 0;
}


# ---------------------------------------------------------------------
# 腐海
# ---------------------------------------------------------------------
sub SetRottenSea {
    my ($island , $x , $y) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    $land->[$x][$y] = $HlandRottenSea;
    $landValue->[$x][$y] = 0;
    $landValue2->[$x][$y] = 0;
    $landValue3->[$x][$y] = 0;
}


# ---------------------------------------------------------------------
# 流氷
# ---------------------------------------------------------------------
sub SetIce_Normal {
    my ($island , $x , $y) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    $land->[$x][$y] = $HlandIce;
    $landValue->[$x][$y] = 0;
    $landValue2->[$x][$y] = 0;
    $landValue3->[$x][$y] = 0;
}



# ---------------------------------------------------------------------
# 通常の平地
# ---------------------------------------------------------------------
sub SetPlains_Normal {
    my ($island , $x , $y) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    $land->[$x][$y] = $HlandPlains;
    $landValue->[$x][$y] = 0;
    $landValue2->[$x][$y] = 0;
    $landValue3->[$x][$y] = 0;
}


# ---------------------------------------------------------------------
# ペットが攻撃しないモンスター
# ---------------------------------------------------------------------
sub isNoAttackMonster {
    my ($mKind) = @_;

    if (   ($mKind == $Mons_SuperTetra)
        || ($mKind == $Mons_hime_inora)
        || ($mKind == $Mons_Mascot_inora) ) {

        return 1;
    }
    return 0;
}


# ---------------------------------------------------------------------
# 怪獣の攻撃
# ---------------------------------------------------------------------
sub CityAttack {
    my ($island , $x , $y) = @_;

    if (   (!($island->{'monsterlive'}))
        || ($island->{'BF_Flag'}) ) {
        return 0;
    }

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    my ($landKind) = $land->[$x][$y];
    my ($lv) = $landValue->[$x][$y];
    my ($lv2) = $landValue2->[$x][$y];
    my ($lv3) = $landValue3->[$x][$y];

    my ($mKind, $mName, $mHp);

    my ($i, $count, $sx, $sy);

    my ($damage);

    $count = 0;

    for ($i = 1; $i < 7; $i++) {
        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # 行による位置調整
        $sx-- if (!($sy % 2) && ($y % 2));

        if (($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)) {
            # 範囲外の場合
        }
        else {

            # 範囲内の場合
            if ($land->[$sx][$sy] == $HlandMonster) {

                ($mKind, $mName, $mHp) = monsterSpec($landValue->[$sx][$sy]);
                unless (isNoAttackMonster($mKind)) {

                    if ($lv > 0) {
                        $damage = random(10)+5;
                        MonsterAttackHook($island , $sx , $sy , $mKind , $damage, $tx , $ty);
                        $lv -= $damage;
                        $count++;
                    }
                }
            }
        }
    }

    $landValue->[$x][$y] = max($lv , 0);

    if ($count) {
        my ($lName) = landName($landKind, $lv,$lv2,$lv3);
        my ($id) = $island->{'id'};
        my ($this_pos) = "($x, $y)";
        my ($name) = islandName($island);

        if (   ($landKind == $HlandSeacity)
            || ($landKind == $HlandUmishuto) ) {

            logMonsAttacksSecret($id, $name, $lName, $this_pos);
        }
        else {

            logMonsAttacks($id, $name, $lName, $this_pos);
        }
    }
    return $count;
}


# ---------------------------------------------------------------------
# 怪獣の攻撃イベント
# 特殊な攻撃を含める場合
# ---------------------------------------------------------------------
sub MonsterAttackHook {
    my ($island , $x , $y , $mKind , $damage , $bx , $by) = @_;

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    if ($mKind == $Mons_Kisinhei) {

        $landValue3->[$x][$y] += $damage;
    }
    else{
        # なにもしない
    }
}


# ---------------------------------------------------------------------
# 
# ---------------------------------------------------------------------
sub Town_Deserted {
    my ($island , $x , $y) = @_;

    my ($land) = $island->{'land'};

    my ($landKind) = $land->[$x][$y];

    if ($land->[$x][$y] == $HlandTown) {

        my ($landValue) = $island->{'landValue'};
        my ($lv) = $landValue->[$x][$y];

        if ($landValue->[$x][$y] <= 0) {
            SetPlains_Normal($island,$x,$y);
            return (1);
        }
    }
    return (0);
}


1;
