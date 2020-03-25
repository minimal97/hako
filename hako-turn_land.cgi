#----------------------------------------------------------------------
# Ȣ����� ver2.30
# ������ʹԥ⥸�塼��(ver1.02)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# Hakoniwa R.A. ver1.11
# �ᥤ�󥹥���ץ�(Ȣ����� ver2.30)
# ���Ѿ�������ˡ���ϡ�read-renas.txt�ե�����򻲾�
#
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# ���
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# include
#----------------------------------------------------------------------
require('./hako-turn_log.cgi');     # �����ϥե�����
require('./hako-turn_monster.cgi'); # ���ѥ��åƥ� ���ý�������ñۤ��Ƥ椯
require('./hako-turn_food.cgi');


#----------------------------------------------------------------------
# static
#----------------------------------------------------------------------


#----------------------------------------------------------------------
#----------------------------------------------------------------------


# ---------------------------------------------------------------------
# �̾�λ�
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
# ��ǰ������� val����
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
# �ϴ�
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
# �̾�ιӤ���
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
# �̾�ιӤ���
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
# ��������
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
# ��󥹥�������
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
# �̾�γ�
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
# �̾�γ�
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
# �峤
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
# ήɹ
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
# �̾��ʿ��
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
# �ڥåȤ����⤷�ʤ���󥹥���
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
# ���äι���
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

        # �Ԥˤ�����Ĵ��
        $sx-- if (!($sy % 2) && ($y % 2));

        if (($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)) {
            # �ϰϳ��ξ��
        }
        else {

            # �ϰ���ξ��
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
# ���äι��⥤�٥��
# �ü�ʹ����ޤ����
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
        # �ʤˤ⤷�ʤ�
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
