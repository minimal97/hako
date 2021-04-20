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

#----------------------------------------------------------------------
# static
#----------------------------------------------------------------------




# ---------------------------------------------------------------------
# �ϴ���ä�5hex
# ---------------------------------------------------------------------
sub FiveHexFlame {
    my($island, $x ,$y) = @_;

    my (@wayX);
    my (@wayY);

    $ra=random(6);

    if ($ra==1) {
        @wayX = (-1,-2,-3,-4,-5);
        @wayY = ( 0, 0, 0, 0, 0);
    }
    elsif ($ra==2) {

        @wayX = ( 1, 2, 3, 4, 5);
        @wayY = ( 0, 0, 0, 0, 0);
    }
    elsif ($ra==3) {
        @wayX = ( 3, 2, 2, 1, 1);
        @wayY = (-5,-4,-3,-2,-1);
    }
    elsif ($ra==4) {
        @wayX = ( 3, 2, 2, 1, 1);
        @wayY = ( 5, 4, 3, 2, 1);
    }
    elsif ($ra==5) {
        @wayX = (0,-1, -1,-2,-2);
        @wayY = (1, 2,  3, 4, 5);
    }
    else {
        @wayX = (-2,-2,-1,-1, 0);
        @wayY = (-5,-4,-3,-2,-1);
    }

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($mKind, $mName, $mHp) = monsterSpec($landValue->[$x][$y]);
    my ($id) = $island->{'id'};
    my ($name) = islandName($island);

    my ($i , $sx , $sy);

    for ($i = 0; $i < 5; $i++) {
        $sx = $x + $wayX[$i];
        $sy = $y + $wayY[$i];

        # �Ԥˤ�����Ĵ��
        $sx-- if (!($sy % 2) && ($y % 2));
        # �ϰϳ�
        next if (($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

        if (NoDamage_by_Flame($land->[$sx][$sy]) ) {

        }
        elsif ($land->[$sx][$sy] == $HlandMonster) {

            # �оݤȤʤ���äγ����Ǽ��Ф�
            my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
            my ($tlv) = $landValue->[$sx][$sy];

            if (isMonsterCuring($tKind)) {
                # �оݤ��Ų���ʤ���̤ʤ�
                next;
            }
            if (random(1000) < 600) {
                if (   ($tKind == 28)
                    || ($tKind == 30)) {
                    logLavaAttack($id, $name, $mName, "($x, $y)", $tName, "($sx, $sy)");
                    $dmge = random(4);
                    $tHp -= $dmge;
                    $tlv -= $dmge;
                    $landValue->[$sx][$sy] = $tlv;

                    if ($tHp < 1) {
                        # �оݤβ���
                        SetYoganLand($island , $sx , $sy);
                        $island->{'monsterlive'} -= 1;
                        # �󾩶�
                        my ($value) = $HmonsterValue[$tKind];
                        $island->{'money'} += $value;
                        logMsMonMoney($id, $tName, $value);
                    }
                }
                elsif ($tKind != 33) {
                    logLavaAttack($id, $name, $mName, "($x, $y)", $tName, "($sx, $sy)");

                    # �оݤβ���
                    SetYoganLand($island , $sx , $sy);
                    $island->{'monsterlive'} -= 1;

                    if (random(1000) < 100) {
                        SetMonument_Normal($island , $sx , $sy , 78);
                    }
                    # �󾩶�
                    my ($value) = $HmonsterValue[$tKind];
                    $island->{'money'} += $value;
                    logMsMonMoney($id, $tName, $value);
                }
            }
        }
        else {

            if ($land->[$sx][$sy] != $HlandYougan) {
                logLavaAttack($id, $name, $mName, "($x, $y)", landName($land->[$sx][$sy], $landValue->[$sx][$sy],$landValue2->[$sx][$sy]), "($sx, $sy)");
            }
            SetYoganLand($island , $sx , $sy);
        }
    }
}


# ---------------------------------------------------------------------
# �ڥåȲ��ä�����
# ---------------------------------------------------------------------



# ---------------------------------------------------------------------
# �ϴ���ä�3way
# ---------------------------------------------------------------------
sub ThreeWayFlame {
    my ($island, $x ,$y) = @_;

    my (@wayX);
    my (@wayY);
    if (random(2)){
        @wayX = ( 1, 1, 1, 1,-1,-2);
        @wayY = (-2,-1, 1, 2, 0, 0);
    }
    else {
        @wayX = (-1, 0, 0,-1, 1, 2);
        @wayY = (-2,-1, 1, 2, 0, 0);
    }

    my ($id) = $island->{'id'};
    my ($name) = islandName($island);
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};
    my ($mKind, $mName, $mHp) = monsterSpec($landValue->[$x][$y]);

    my ($i , $sx , $sy);

    for ($i = 0; $i < 6; $i++) {
        $sx = $x + $wayX[$i];
        $sy = $y + $wayY[$i];

        # �Ԥˤ�����Ĵ��
        $sx-- if (!($sy % 2) && ($y % 2));
        # �ϰϳ�
        next if (($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

        if (NoDamage_by_Flame($land->[$sx][$sy]) ){

        }
        elsif ($land->[$sx][$sy] == $HlandMonster) {

            # �оݤȤʤ���äγ����Ǽ��Ф�
            my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
            my ($tlv) = $landValue->[$sx][$sy];

            if (isMonsterCuring($tKind)) {
                # �оݤ��Ų���ʤ���̤ʤ�
                next;
            }
            if (random(1000) < 600) {

                if (   ($tKind == 28)
                    || ($tKind == 30) ) {

                    logLavaAttack($id, $name, $mName, "($x, $y)", $tName, "($sx, $sy)");
                    $dmge = random(4);
                    $tHp -= $dmge;
                    $tlv -= $dmge;
                    $landValue->[$sx][$sy] = $tlv;

                    if ($tHp < 1) {
                        # �оݤβ���
                        $land->[$sx][$sy] = $HlandYougan;
                        $landValue->[$sx][$sy] = random(3) + 1;
                        $landValue2->[$sx][$sy] = 0;
                        $landValue3->[$sx][$sy] = 0;

                        $island->{'monsterlive'} -= 1;
                        # �󾩶�
                        my($value) = $HmonsterValue[$tKind];
                        $island->{'money'} += $value;
                        logMsMonMoney($id, $tName, $value);
                    }
                }
                elsif($tKind != 33) {

                    logLavaAttack($id, $name, $mName, "($x, $y)", $tName, "($sx, $sy)");

                    # �оݤβ���
                    $land->[$sx][$sy] = $HlandYougan;
                    $landValue->[$sx][$sy] = random(3) + 1;
                    $landValue2->[$sx][$sy] = 0;
                    $landValue3->[$sx][$sy] = 0;

                    $island->{'monsterlive'} -= 1;

                    if (random(1000) < 100) {
                        $land->[$sx][$sy] = $HlandMonument;
                        $landValue->[$sx][$sy] = 78;
                    }
                    # �󾩶�
                    my($value) = $HmonsterValue[$tKind];
                    $island->{'money'} += $value;
                    logMsMonMoney($id, $tName, $value);
                }
            }
        }
        else {

            if ($land->[$sx][$sy] != $HlandYougan) {
                logLavaAttack($island->{'id'}, $name, $mName, "($x, $y)", landName($land->[$sx][$sy], $landValue->[$sx][$sy], $landValue2->[$sx][$sy]), "($sx, $sy)");
            }
            $land->[$sx][$sy] = $HlandYougan;
            $landValue->[$sx][$sy] = random(3) + 1;
            $landValue2->[$sx][$sy] = 0;
            $landValue3->[$sx][$sy] = 0;
        }
    }
}


#------------------------------------------------------------------------------------
# ��Ȥ��Τ�
#------------------------------------------------------------------------------------
sub RetroBeam {
    my ($island , $mName) = @_;

    my ($par) = 100;

    if (!(random(100) < $par)) {
        return 0;
    }

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    my ($tx,$ty,$i);
    my ($id) = $island->{'id'};
    my ($beamname) = '���ȿ���ӡ���';

    foreach $i (0..$pointNumber) {
        $tx = $Hrpx[$i];
        $ty = $Hrpy[$i];

        if (   ($land->[$tx][$ty] == $HlandFactory)
            || ($land->[$tx][$ty] == $HlandFoodim)
            || ($land->[$tx][$ty] == $HlandHTFactory)
            || ($land->[$tx][$ty] == $HlandSHTF)) {

            if ($landValue->[$tx][$ty] > 3) {
                my ($name) = islandName($island);
                my ($tPoint) = "($tx,$ty)";

                $landValue->[$tx][$ty] = int($landValue->[$tx][$ty] / 2);
                my ($lName) = landName($land->[$tx][$ty] , $landValue->[$tx][$ty],$landValue2->[$tx][$ty]);

                logOut("${HtagName_}${name}${H_tagName}��<B>$mName</B>��$tPoint<B>$lName</B>�˸�����<B>$beamname</B>���������ﳲ������ޤ�����",$id);

                if ( random(3) ) {
                    last;
                }
            }
        }
    }

    return 0;
}


1;
