#----------------------------------------------------------------------
# top �� map�Ѥ�land info
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# �ݤ������ò��� �� �༣�� ʸ������֤�
# �ݤ������åꥹ��  ���ä����䤹�Τǡ��ꥹ�ȤϺ��
#----------------------------------------------------------------------
sub ScoreBoard_Taiji {
    my ($island) = @_;

    my ($prize) = '';

    if ($island->{'taiji'}) {
        my ($prize1, $prize2) = split(/\t/, $island->{'prize'});
        $prize1 =~ /([0-9]*),([0-9]*),(.*)/;
        my ($flags, $monsters, $turns) = ($1, $2, $3);

        my ($image) = $HMapImgDir . $HmonsterImage[$monsters];
        $prize .= "<span class='monsm'><img alt='' src=\"${image}\" title=\"[$HmonsterName[$monsters]]\" ";
        $prize .= " class='landinfoIcon'>$island->{'taiji'}$HunitMonster�༣</span> ";
    }
    return $prize;
}


#----------------------------------------------------------------------
# ����
#
sub ScoreBoard_Eisei {
    my ($island) = @_;

    my ($me_sat) = "<br><span class='eisei'>";
    my ($kind, $i);
    my ($emp) = 0;

    for ($i = 1; $i < 7; $i++) {

        $kind = 'eis' . $i;
        $me_sat .= "<img src=\"${HStatImgDir}$HeiseiImage[$i]\" title=\"$HeiseiName[$i]\" alt='' class='landinfoIcon'>$island->{$kind}%" if ($island->{$kind} >= 1);
        $emp += $island->{$kind};
    }

    $me_sat .= '</span>';
    $me_sat = ' ' if (!$emp);

    return $me_sat;
}


#----------------------------------------------------------------------
# �Хȥ�ե�����ɥ�����
#----------------------------------------------------------------------
sub ScoreBoard_BF_Point {
    my ($island) = @_;

    my ($BF_Score) = '';
    if ($island->{'landscore'}) {
        $BF_Score = $island->{'landscore'};

        $BF_Score = " <img src=\"${HMapImgDir}land9.gif\" alt='' class='landinfoIcon'>BF:".$BF_Score.'��';
    }

    return $BF_Score;
}


#----------------------------------------------------------------------
# �Ҿ��
#----------------------------------------------------------------------
sub ScoreBoard_Farm {
    my ($island) = @_;

    my ($Farmcpc) = '';
    my ($tori) = $island->{'tare'};
    my ($buta) = $island->{'zipro'};
    my ($ushi) = $island->{'leje'};

    if (   ($tori)
        || ($buta)
        || ($ushi)) {

        $Farmcpc  = "<span class='unemploy1'>";
        $Farmcpc .= "<img src=\"img/niwatori.gif\"  alt='' title=\"�ˤ�Ȥ�\" class='landinfoIcon'>$tori����" if ($tori);
        $Farmcpc .= "<img src=\"img/buta.gif\"  alt='' title=\"�֤�\" class='landinfoIcon'>".$buta."��Ƭ" if ($buta);
        $Farmcpc .= "<img src=\"img/ushi.gif\"  alt='' title=\"����\" class='landinfoIcon'>$ushi��Ƭ" if ($ushi);
        $Farmcpc .= '</span>';
    }

    return $Farmcpc;
}


#----------------------------------------------------------------------
# prize
#----------------------------------------------------------------------
sub ScoreBoard_Prize {
    my ($island) = @_;

    my ($flags, $monsters, $turns);
    {
        my ($prize1, $prize2) = split(/\t/, $island->{'prize'});
        $prize1 =~ /([0-9]*),([0-9]*),(.*)/;
        ($flags, $monsters, $turns) = ($1, $2, $3);
        $prize = '';
    }

    my ($alt) = '';
    my @turnPrize = reverse(split(/,/, $turns));
    my ($i) = 0;
    foreach (@turnPrize) {
        last if($i > 3);
        $alt .= "\n" if ($i++);
        $alt .= $_ . ${Hprize[0]};
    }
    {
        my ($tNum) = @turnPrize;
        $alt .= ($i < $tNum ? "\n¾��${tNum}�����" : "\n�ʾ�${tNum}�����") if($tNum);
    }
    my ($alt1) = $alt;
    # $alt1 =~ s/$rt/ /g;
    $prize .= "<img src=\"./img/prize/prize0.svg\"  alt='' title=\"$alt\" onMouseOver='status=\"$alt1\"; return 1;' class='landinfoIcon'> " if ($alt ne '');

    # ̾���˾ޤ�ʸ�����ɲ�
    my ($f) = 1;
    for ($i = 1; $i < 10; $i++) {
        if ($flags & $f) {
            $prize .= "<IMG SRC=\"./img/prize/prize${i}.gif\" alt=''  TITLE=\"${Hprize[$i]}\" ";
            $prize .= "class='landinfoIcon'> ";
        }
        $f = $f << 1;
    }

    return ($prize);
}


#----------------------------------------------------------------------
# �и���β��åꥹ��
#----------------------------------------------------------------------
sub ScoreBoard_LiveMonster {
    my ($island) = @_;

    my ($monsterlive) = $island->{'monsterlive'};
    my ($ret) = '';

    if ($monsterlive > 0) {
        my ($monsliveimg) = '';
        my ($monsm) = '';
        my ($mName) = '';

        $mName = "[$HmonsterName[$island->{'monsterlivetype'}]]";
        my ($image) = $HmonsterImage[$island->{'monsterlivetype'}];
        $monsliveimg = "<img src=\"${HMapImgDir}${image}\"  alt=''  title=\"$mName\" ";
        $monsliveimg .= "class='landinfoIcon'>";
        $monsm = "${monsterlive}$HunitMonster�и���!!";
        $ret = '<span class="unemploy2">' . $monsliveimg . $monsm . '</span> ';
    }

    return ($ret);
}


#----------------------------------------------------------------------
# �ܡ��ʥ� �����
#----------------------------------------------------------------------
sub ScoreBoard_Bumon {
    my ($island) = @_;
    my ($bumonCount) = 0;

    my ($top_matome) = '';
    my $bName = '';
    my ($rID);
    my ($element);
    my ($uni) = 0;

    foreach (0..$#HrankingID) {
        $rID = $HrankingID[$_];
        $element = $island->{$BUMON_ELEMENTS[$_]};
        if (   ($island->{'id'} == $rID)
            && ($element ne '')
            && ($element != 0)) {

            $bumonCount++;
            $top_matome .= " <img src=\"$BUMON_ICON[$_]\" alt='' title=\"����ޡ�$BUMON_NAME[$_]\" class='landinfoIcon'> ";
        }
    }

    my ($bumons) = '';
    if ($bumonCount) {
        $bumons .= $top_matome ;
        $bumons = '<br>�����('.$bumonCount.'��)��' . $bumons;
    }

    return $bumons;
}


#----------------------------------------------------------------------
# �������󤫤��
#----------------------------------------------------------------------
sub UpdateStat {
    my ($island, $turn ) = @_;

    my ($seicho, $zouka, $food_zouka, $area_zouka, $rieki);

    my ($out_html);

    $seicho     = ($island->{'monta'} < 0) ? "$island->{'monta'}pts." : "��$island->{'monta'}pts.";

    $zouka      = ($island->{'hamu'} < 0) ? $island->{'hamu'}.$HunitPop : '��'.$island->{'hamu'}.$HunitPop;
    $zouka      = '' if ($island->{'hamu'} == 0) ;

    $food_zouka = ($island->{'old_food'} < 0) ? "$island->{'old_food'}$HunitFood" : "��$island->{'old_food'}$HunitFood";
    $food_zouka = '' if ($island->{'old_food'} == 0) ;

    $area_zouka = ($island->{'old_area'} < 0) ? "$island->{'old_area'}$HunitArea" : "��$island->{'old_area'}$HunitArea";
    $area_zouka = '' if ($island->{'old_area'} == 0) ;

    $rieki      = ($island->{'pika'} < 0) ? $island->{'pika'}.$HunitMoney : '��'.$island->{'pika'}.$HunitMoney;
    $rieki      = '' if ($island->{'pika'} == 0) ;

    my ($tha_t) = int($turn / 100) * 100;


#    <span class="monsm"><font size="-2">��������<br>$seicho$zouka$rieki$food_zouka$area_zouka</font></span><br>
#    <span class="monsm"><font size="-2">$tha_t�����󤫤�$island->{'tha_diff'}pts.</font></span>
    $out_html = "<span class='monsm'><font size='-1'>��������$seicho$zouka$rieki$food_zouka$area_zouka��";
    $out_html .= "$tha_t�����󤫤�$island->{'tha_diff'}pts.</font></span>";

    return $out_html;
}


1;
