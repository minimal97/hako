#----------------------------------------------------------------------
# ������ҳ� ���ߤʤ�
#----------------------------------------------------------------------


my @HdisThunder    = ( 1, 1, 1, 1, 2, 3, 3, 5, 4, 3, 1, 1, 1); # ����


#----------------------------------------------------------------------
sub ThunderProc {
    my ($island) = @_;

    my ($per) = random(1000);
    my ($num) = random(3) + 1;

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};

    my ($month) = %main::Hday{'month'};
    if ($per <= $HdisThunder[$month]) {

        ThunderAttack($island , $num);
    }
}


#----------------------------------------------------------------------
sub ThunderAttack {
    my ($island, $num) = @_;

    my ($i, $x, $y);

    $num = ($num) ? $num : 1;

    for ($i = 0; $i < $num; $i++) {

        $x = random($HislandSize);
        $y = random($HislandSize);
        ThunderDamage($island , $x, $y);
    }
}


#----------------------------------------------------------------------
sub ThunderDamage {
    my ($island, $x, $y) = @_;

    my ($name) = islandName($island);
    my ($id) = $island->{'id'};
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};

    my ($sx, $sy, $i, $landKind, $lv, $lv2, $point);

    #���� 1hex������ˤ�õ��
    for ($i = 0; $i < 7; $i++) {

        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # �Ԥˤ�����Ĵ��
        $sx-- if (!($sy % 2) && ($y % 2));

        if (   ($sx >= 0)
            && ($sx < $HislandSize)
            && ($sy >= 0)
            && ($sy < $HislandSize) ) {

            $landKind = $land->[$sx][$sy];

            if (   ($landKind == $HlandMonument)
                || ($landKind == $HlandKatorikun)
                || ($landKind == $HlandDefence)
                || ($landKind == $HlandShrine)
                || ($landKind == $HlandHouse)
                || ($landKind == $HlandStation)
                                                 ) {

                logGuardLightningRod($island, landName($landKind, $landValue->[$sx][$sy], $landValue2->[$sx][$sy]));
                return 0;
            }
        }
    }

    $landKind = $land->[$x][$y];

    if (ThunderNoDamageLand($landKind)) {

        return 0;
    }

    if (random(1000) < 22) {

    ThunderLandDamage($island, $x, $y);
    }
    else {

        # ���Ϥ��˲�����
        for ($i = 1; $i < 7; $i++) {

            $sx = $x + $ax[$i];
            $sy = $y + $ay[$i];

            # �Ԥˤ�����Ĵ��
            $sx-- if (!($sy % 2) && ($y % 2));

            if (   ($sx >= 0)
                && ($sx < $HislandSize)
                && ($sy >= 0)
                && ($sy < $HislandSize) ) {

                ThunderLandDamage($island, $sx, $sy);
            }
        }
        SetMonument_Normal($island, $x , $y , 60);
    }
}


#----------------------------------------------------------------------
#----------------------------------------------------------------------
sub ThunderNoDamageLand {
    my ($landKind) = @_;

    if (   ($landKind == $HlandSea)
        || ($landKind == $HlandWaste)
        || ($landKind == $HlandMountain)
        || ($landKind == $HlandGold)
        || ($landKind == $HlandMonument)
        || ($landKind == $HlandDefence)
        || ($landKind == $HlandShrine)
        || ($landKind == $HlandSbase)
        || ($landKind == $HlandSeacity)
        || ($landKind == $HlandSeatown)
        || ($landKind == $HlandUmishuto)
        || ($landKind == $HlandOmamori)
        || ($landKind == $HlandYougan)
        || ($landKind == $HlandTrain)
        || ($landKind == $HlandSunahama)
        || ($landKind == $HlandUmiamu)
                                        ) {

        # �Ρ����᡼��
        return 1;
    }
    return 0;
}


#----------------------------------------------------------------------
#----------------------------------------------------------------------
sub ThunderLandDamage {
    my ($island, $x, $y) = @_;

    my ($name) = islandName($island);
    my ($id) = $island->{'id'};
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue2) = $island->{'landValue3'};

    $landKind = $land->[$x][$y];
    $lv = $landValue->[$x][$y];
    $lv2 = $landValue2->[$x][$y];

    if (ThunderNoDamageLand($landKind)) {
        return 0;
    }

    my ($point) = "($x, $y)";
    my ($damage) = random(100) + 10;

    if (   ($landKind == $HlandPlains)
        || ($landKind == $HlandBase)
        || ($landKind == $HlandForest)
        || ($landKind == $HlandHaribote)
        || ($landKind == $HlandKyujo)
        || ($landKind == $HlandRottenSea)
        || ($landKind == $HlandKyujokai)
        || ($landKind == $HlandYakusho)
        || ($landKind == $HlandEgg)
        || ($landKind == $HlandSeki)
        || ($landKind == $HlandFiredept)
        || ($landKind == $HlandHospital)
        || (($landKind == $HlandMine) && !($lv & $Hmine_SEA_FLAG))
                                                                    ) {

        # 1ȯ���Ѳ�
        logThunderDestructionDamage($island,landName($landKind, $lv,$lv2), $point);
        SetWasteLand_Normal($island, $x, $y);
    }
    elsif (   ($landKind == $HlandOil)
           || ($landKind == $HlandFune)
           || ($landKind == $HlandIce)
           || (($landKind == $HlandMine) && ($lv & $Hmine_SEA_FLAG))
                                                                        ) {

        # 1ȯ���Ѳ�
        logThunderDestructionDamage($island,landName($landKind, $lv,$lv2), $point);
        SetSeaLand_Normal($island, $x, $y);
    }
    elsif ($landKind == $HlandBeachPark) {

        # 1ȯ���Ѳ�
        logThunderDestructionDamage($island,landName($landKind, $lv,$lv2), $point);
        SetKindLand($island, $x, $y , $HlandSunahama);
    }
    elsif ($landKind == $HlandCollege) {

        if (random(100) > 10) {
            $landValue2->[$x][$y] += 5;
            logThunderDamage($island, landName($landKind, $lv,$lv2), $point, '');
        }
        else {

            # 1ȯ���Ѳ�
            logThunderDestructionDamage($island,landName($landKind, $lv,$lv2), $point);
            SetWasteLand_Normal($island, $x, $y);
        }

    }
    elsif ($landKind == $HlandOnsen) {     # LandValue�ˤ��

        $lv = $lv - $damage;

        if ($lv > 0) {

            logThunderDamage($island, landName($landKind, $lv,$lv2), $point, "$lv$HunitPop");
            $landValue->[$x][$y] = "$lv$HunitPop";
        }
        else {

            logThunderDestructionDamage($island,landName($landKind, $lv,$lv2), $point);
            SetMountain_Normal($island, $x, $y);
        }
    }
    elsif (   (0)
           || ($landKind == $HlandTown)     # LandValue�ˤ��
           || ($landKind == $HlandFarm)
           || ($landKind == $HlandFactory)
           || ($landKind == $HlandPark)
           || ($landKind == $HlandMinato)
           || (($landKind == $HlandFoodim) && ($lv < 480))
           || ($landKind == $HlandProcity)
           || ($landKind == $HlandNewtown)
           || ($landKind == $HlandBigtown)
           || ($landKind == $HlandInaka)
           || ($landKind == $HlandFarmchi)
           || ($landKind == $HlandFarmpic)
           || ($landKind == $HlandFarmcow)
           || ($landKind == $HlandShuto)
           || ($landKind == $HlandRizort)
           || ($landKind == $HlandBigRizort)
           || ($landKind == $HlandBettown)
           || ($landKind == $HlandHTFactory)
           || ($landKind == $HlandSHTF)
           || ($landKind == $HlandInoraLand)
                    ) {

        $lv = $lv - $damage;
        if ($lv > 0) {

            logThunderDamage($island, landName($landKind, $lv,$lv2), $point, "$lv$HunitPop");
            $landValue->[$x][$y] = $lv;
        }
        else {

            logThunderDestructionDamage($island,landName($landKind, $lv,$lv2), $point);
            SetWasteLand_Normal($island, $x, $y);
        }
    }
    elsif (   (0)                               # LandValue�ˤ��
           || ($landKind == $HlandNursery)
                                            ) {
        $lv = $lv - $damage;
        if ($lv > 0) {

            logThunderDamage($island, landName($landKind, $lv,$lv2), $point, "$lv$HunitPop");
            $landValue->[$x][$y] = $lv;
        }
        else {

            logThunderDestructionDamage($island,landName($landKind, $lv,$lv2), $point);
            SetSeaShallowLand($island, $x, $y);
        }
    }
    elsif (   (0)                               # LandValue�ˤ��
           || ($landKind == $HlandFrocity)
           || ($landKind == $HlandUmicity)
                                        ) {
        $lv = $lv - $damage;
        if ($lv > 0) {

            logThunderDamage($island, landName($landKind, $lv,$lv2), $point, "$lv$HunitPop");
            $landValue->[$x][$y] = $lv;
        }
        else {

            logThunderDestructionDamage($island,landName($landKind, $lv,$lv2), $point);
            SetSeaShallowLand($island, $x, $y);
        }
    }
    else {

    }
}


#----------------------------------------------------------------------
sub logGuardLightningRod {
    my ($island, $lName, $point) = @_;

    my ($id) = $island->{'id'};
    my ($name) = islandName($island);

    logOut("${HtagName_}${name}${H_tagName}�����뤬����ޤ�������$lName������ˤ�����̤����ޤ�����", $id);
}


#----------------------------------------------------------------------
sub logThunderDestructionDamage {
    my ($island, $lName, $point) = @_;

    my ($id) = $island->{'id'};
    my ($name) = islandName($island);

    logDamageAny($id, $name, $lName, $point, "${HtagDisaster_}����${H_tagDisaster}�ˤ����Ǥ��ޤ�����");
}


#----------------------------------------------------------------------
sub logThunderDamage {
    my ($island, $lName, $point, $str_value) = @_;

    my ($id) = $island->{'id'};
    my ($name) = islandName($island);

    if ($str_value ne '') {     # ��ؤȤζ��̲��Τ��ᡢ������ "***�� ��" ���Ѥ���
        $str_value .= '��';
    }

    logOut("${HtagName_}$name$point${H_tagName}��<b>$lName</b>�����뤬���ꡢ$str_value�ﳲ������ޤ�����", $id);
}


1;
