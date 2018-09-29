#----------------------------------------------------------------------
# top �� map�Ѥ�land info
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# �ݤ������ò��� �� �༣�� ʸ������֤�
# �ݤ������åꥹ��  ���ä����䤹�Τǡ��ꥹ�ȤϺ��
#----------------------------------------------------------------------
sub ScoreBoard_Taiji {
    my($island) = @_;
    my($prize) = '';

    if ($island->{'taiji'}) {
        my($prize1, $prize2) = split(/\t/, $island->{'prize'});
        $prize1 =~ /([0-9]*),([0-9]*),(.*)/;
        my($flags, $monsters, $turns) = ($1, $2, $3);

        my $image = $HMapImgDir . $HmonsterImage[$monsters];
        $prize .= "<span class='monsm'><IMG SRC=\"${image}\" TITLE=\"[$HmonsterName[$monsters]]\" ";
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
    for($i = 1; $i < 7; $i++) {
        $kind = 'eis' . $i;
        $me_sat .= "<IMG SRC=\"${HStatImgDir}$HeiseiImage[$i]\" TITLE=\"$HeiseiName[$i]\" alt='' class='landinfoIcon'>$island->{$kind}%" if ($island->{$kind} >= 1);
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
    my($island) = @_;
    my ($BF_Score) = '';
    if ($island->{'landscore'}) {
        $BF_Score = $island->{'landscore'};

        $BF_Score = " <img SRC=\"${HMapImgDir}land9.gif\" alt='' class='landinfoIcon'>BF:".$BF_Score.'��';
    }

    return $BF_Score;
}


#----------------------------------------------------------------------
# �Ҿ��
#----------------------------------------------------------------------
sub ScoreBoard_Farm {
    my($island) = @_;

    my($Farmcpc) = '';
    my($tori) = $island->{'tare'};
    my($buta) = $island->{'zipro'};
    my($ushi) = $island->{'leje'};

    if( $tori || $buta || $ushi) {

        $Farmcpc  = "<span class='unemploy1'>";
        $Farmcpc .= "<IMG SRC=\"img/niwatori.gif\" TITLE=\"�ˤ�Ȥ�\" class='landinfoIcon'>$tori����" if($tori);
        $Farmcpc .= "<IMG SRC=\"img/buta.gif\" TITLE=\"�֤�\" class='landinfoIcon'>".$buta."��Ƭ" if($buta);
        $Farmcpc .= "<IMG SRC=\"img/ushi.gif\" TITLE=\"����\" class='landinfoIcon'>$ushi��Ƭ" if($ushi);
        $Farmcpc .= '</span>';
    }

    return $Farmcpc;
}


#----------------------------------------------------------------------
# prize
#----------------------------------------------------------------------
sub ScoreBoard_Prize {
    my($island) = @_;

    my($prize1, $prize2) = split(/\t/, $island->{'prize'});
    $prize1 =~ /([0-9]*),([0-9]*),(.*)/;
    my($flags, $monsters, $turns) = ($1, $2, $3);
    $prize = '';

    my $alt = '';
    my @turnPrize = reverse(split(/,/, $turns));
    my $i = 0;
    foreach (@turnPrize) {
        last if($i > 3);
        $alt .= "\n" if($i++);
        $alt .= $_ . ${Hprize[0]};
    }
    my $tNum = @turnPrize;
    $alt .= ($i < $tNum ? "\n¾��${tNum}�����" : "\n�ʾ�${tNum}�����") if($tNum);
    my $alt1 = $alt;
    # $alt1 =~ s/$rt/ /g;
    $prize .= "<IMG SRC=\"./img/prize/prize0.gif\" TITLE=\"$alt\" onMouseOver='status=\"$alt1\"; return 1;' class='landinfoIcon'> " if ($alt ne '');

    # ̾���˾ޤ�ʸ�����ɲ�
    my($f) = 1;
    for($i = 1; $i < 10; $i++) {
        if($flags & $f) {
            $prize .= "<IMG SRC=\"./img/prize/prize${i}.gif\" TITLE=\"${Hprize[$i]}\" ";
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
    my($island) = @_;

    my ($monsliveimg) = '';
    my ($monsm) = '';
    my ($monsterlive) = $island->{'monsterlive'};

    if ( $monsterlive > 0) {
        my ($mName) = '';
        $mName = "[$HmonsterName[$island->{'monsterlivetype'}]]";
        my $image = $HmonsterImage[$island->{'monsterlivetype'}];
        $monsliveimg = "<IMG SRC=\"${HMapImgDir}${image}\" TITLE=\"$mName\" ";
        $monsliveimg .= "class='landinfoIcon'>";
        $monsm = ($monsterlive == 0) ? '' : "${monsterlive}$HunitMonster�и���!!";
    }

    return ('<span class="unemploy2">' . $monsliveimg . $monsm . '</span> ');

}


	my @bumonName  = (  '�͸�',      '����' ,     '����'      , '�η���'          ,  '����',
                  '�ˤ�Ȥ��',    '�֤���' ,   '������'      , '���ýи���'      , '�����༣��',
                      '��Ĺ��',  '�͸�����' ,     '����'      , '��ǰ���'        , '��������',
                '��ʪ���ǽ��', '�̻��Ѹ���', '��ˡ����Ϸ���', '���å�����������', 'HC ͥ�����', 
                 'HC �̻���Ψ','HC �̻�����', "HC${hcturn} ����" , '100��������Ĺ', 'ưʪ����ÿ�');

	my @elements   = (   'pop', 'farm'      , 'factory'       , 'mountain'        , 'fore',
                        'tare', 'zipro'     , 'leje'          , 'monsterlive'     , 'taiji',
                       'monta', 'hamu'      , 'pika'          , 'kei'             , 'renae',
                       'force', 'eisei2'    , 'uni'           , 'teamforce'       , 'styusho',
                     'shoritu', 'kachitent' , 'kachiten'      , 'tha_diff'        , 'zoo_Mons_cnt');

    my @bumonIcon  = ("./${HMapImgDir}land502.png", './img/prize/p_fa.gif',    "./${HMapImgDir}land8.gif",   "./${HMapImgDir}land15.gif", "./${HMapImgDir}land6.gif",
        './img/prize/niwatori_up.gif', './img/prize/buta_up.png', './img/prize/ushi_up.gif',  "./${HMapImgDir}monster0.gif", "./${HMapImgDir}monster0.gif",
        './img/prize/prize11.gif', "./${HMapImgDir}land502.png", './img/prize/money.gif', "./${HMapImgDir}monument0.gif", "./${HMapImgDir}land37.gif",
        './img/mascot.png', "./${HMapImgDir}land43.gif", "./${HMapImgDir}monument0.gif", './img/sc.gif', './img/sc.gif',
        './img/sc.gif', './img/sc.gif', './img/sc.gif', './img/prize/pr100.gif'   , "./${HMapImgDir}land84.gif");
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

    foreach (0..$#HrankingID) {
        $rID = $HrankingID[$_];
        $element = $island->{$elements[$_]};
        if (   ($island->{'id'} == $rID)
            && ($element ne '')
            && ($element != 0)) {

            $bumonCount++;
            $top_matome .= " <IMG SRC=\"$bumonIcon[$_]\" alt='' TITLE=\"����ޡ�$bumonName[$_]\" class='landinfoIcon'> ";
        }
    }

    my ($bumons) = '';
    if ($bumonCount) {
        $bumons .= $top_matome ;
        $bumons = '<br>�����('.$bumonCount.'��)��' . $bumons;

    }

    return $bumons;
}

1;
