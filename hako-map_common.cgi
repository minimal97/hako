#----------------------------------------------------------------------
# Ȣ����� ver2.30
# �Ͽޥ⡼�ɥ⥸�塼��(ver1.00)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# Hakoniwa R.A. ver2.11
# �ᥤ�󥹥���ץ�(Ȣ����� ver2.30)
# ���Ѿ�������ˡ���ϡ�read-renas.txt�ե�����򻲾�
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------
# �ʣ��֣�������ץ��� -ver1.11-
# ���Ѿ�������ˡ���ϡ����۸��Ǥ���ǧ��������
# ��°��js-readme.txt�⤪�ɤ߲�������
# ���äݡ���http://appoh.execweb.cx/hakoniwa/
#----------------------------------------------------------------------
# �ޥå׽����ζ�����ʬ��ȴ���Ф���

#----------------------------------------------------------------------
# static
# �ޥå״ؿ��ν����
#----------------------------------------------------------------------
    my ($pic_sub);

    $pic_sub->{"$HlandSea"} = \&Sea_LandString;
    $pic_sub->{"$HlandTown"} = \&Town_LandString;
    $pic_sub->{"$HlandWaste"} = \&Waste_LandString;
    $pic_sub->{"$HlandMountain"} = \&Mountain_LandString;
    $pic_sub->{"$HlandUmicity"} = \&Umicity_LandString;
    $pic_sub->{"$HlandCollege"} = \&College_LandString;
    $pic_sub->{"$HlandPlains"} = \&Plains_LandString;
    $pic_sub->{"$HlandPlains"} = \&Plains_LandString;

#----------------------------------------------------------------------
# �����糫ȯ�ײ�
#----------------------------------------------------------------------
sub OwnarMap_Header {
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];

    out(<<END);
<div align="center">
<h2>${HtagName_}${HcurrentName}${H_tagName}��ȯ�ײ�</h2>
$HtempBack<br>
</div>
END

}

#----------------------------------------------------------------------
# ���̤�print
sub command_arg {

    my ($out) = '';
    # ���� 2�Ǥ�����Ƥʤ�Ȥ����������롣
    for ($i = 0; $i < 100; $i++) {
        $out .= ("<option value=$i>$i");
        $i++;
        $out .= ("<option value=$i>$i");
    }
    out($out);
}


#----------------------------------------------------------------------
sub isCommandEnable {
    my ($l_kind) = @_;

    for ($i = 0; $i < $HcommandTotal; $i++) {

        if ($l_kind == $HcomList[$i]) {
            return 1;
        }
    }
    return 0;
}

#----------------------------------------------------------------------
# ����Ͽ�
#----------------------------------------------------------------------

# �����ɽ��
sub islandInfo {
    my ($mode) = @_;

    my ($island) = $Hislands[$HcurrentNumber];
    # ����ɽ��
    my ($rank) = $HcurrentNumber + 1 - $HbfieldNumber;
    my ($farm) = $island->{'farm'};
    my ($factory) = $island->{'factory'};
    my ($HTfactor) = $island->{'factoryHT'};
    my ($mountain) = $island->{'mountain'};
    my ($pts) = $island->{'pts'};
    my ($rena, $renae);
    my ($unemployed);
    my ($civreq);

    $rena = $island->{'rena'};
    $civreq = ($island->{'civreq'}) ? $island->{'civreq'} : "�ʤ�";
    $renae = (int($rena / 10 ));
    $unemployed = ($island->{'pop'} - ($farm + $factory + $HTfactor + $mountain) * 10) / $island->{'pop'} * 100 if($island->{'pop'});
    $unemployed = '<span class="' . ($unemployed < 0 ? 'unemploy1' : 'unemploy2') . '">' . sprintf("%.2f%%", $unemployed) . '</span>' if($island->{'pop'});
    $farm = ($farm == 0) ? "��ͭ����" : "${farm}0$HunitPop";
    $factory = ($factory == 0) ? "��ͭ����" : "${factory}0$HunitPop";
    $HTfactor = ($HTfactor == 0) ? "��ͭ����" : "${HTfactor}0$HunitPop";
    $mountain = ($mountain == 0) ? "��ͭ����" : "${mountain}0$HunitPop";
    #$pts = ($pts == 0) ? "0pts." : "${pts}pts.";

    my ($col_num) = 12;

    my ($mStr1) = '';
    my ($mStr2) = '';
    if (   (INIT_HIDE_MONEY_MODE == 1)
        || ($HmainMode eq 'owner')
        || ($island->{'id'} > 100)) {

        # ̵���ޤ���owner�⡼�ɤޤ���BattleField
        $mStr1 = "<th $HbgTitleCell>${HtagTH_}���${H_tagTH}</th>";
        $mStr2 = "<td $HbgInfoCell align=right>$island->{'money'}$HunitMoney</td>";
        $col_num++;         # �ơ��֥��Ĺ����
    }
    elsif (   (INIT_HIDE_MONEY_MODE == 2)
           || (INIT_HIDE_MONEY_MODE == 3)) {

        my ($mTmp) = aboutMoney($island->{'money'});

        # 1000��ñ�̥⡼��
        $mStr1 = "<th $HbgTitleCell>${HtagTH_}���${H_tagTH}</th>";
        $mStr2 = "<td $HbgInfoCell align='right'>$mTmp</td>";
        $col_num++;         # �ơ��֥��Ĺ����
    }

    my ($bStr, $rStr1, $rStr2, $uStr1, $uStr2, $msStr1, $msStr2) = ('', '', '', '', '', '', '');

    if (($island->{'id'} <= 100) && !($island->{'BF_Flag'})) {
        # ���ݥ���ȤȽ��
        $rStr1 = "<th $HbgTitleCell>${HtagTH_}���${H_tagTH}</th><th $HbgTitleCell>${HtagTH_}<small>���Point</small>${H_tagTH}</th>";
        $rStr2 = "<td $HbgNumberCell rowspan='2' align='center'>${HtagNumber_}$rank${H_tagNumber}</td><td $HbgPoinCell align=right>${pts}</td>";
        # ����Ψ
        $uStr1 = "<th $HbgTitleCell>${HtagTH_}����Ψ${H_tagTH}</th>";
        $uStr2 = "<td $HbgInfoCell align='right'>${unemployed}</td>";
        $col_num = $col_num + 2;             # �ơ��֥��Ĺ����
        # ȯ�Ͳ�ǽ�ߥ������(��ͭ��)
        if (INIT_HIDE_MISSILE_MODE || ($HmainMode eq 'owner')) {

            # ̵���ޤ���owner�⡼��
            $msStr1 = "<th $HbgTitleCell>${HtagTH_}�ߥ������";
            $msStr2 = "<td $HbgInfoCell align=right>$island->{'missiles'}${HunitMissile}";
            $col_num++;         # �ơ��֥��Ĺ����

            if (INIT_HIDE_MISSILE_MODE == 2) {

                my ($mTmp) = aboutMissile($island->{'missiles'});
                # 10ȯñ�̥⡼��
                $msStr1 = "<th $HbgTitleCell>${HtagTH_}�ߥ������${H_tagTH}</th>";
                $msStr2 = "<td $HbgInfoCell align='right'>${mTmp}</td>";
            }
            elsif (INIT_USE_ARM_SUPPLY) {

                $msStr1 .= "(����ʪ��)${H_tagTH}</th>";
                $msStr2 .= "($island->{'army'}��)</td>";
            }
            else {
                $msStr1 .= "${H_tagTH}</th>";
                $msStr2 .= "</td>";
            }
        }
    } else {
        $bStr = "<tr><th colspan='13'><font size='5'>${HtagTH_}Battle Field${H_tagTH}</font></th></tr>";
        $col_num ++;         # �ơ��֥��Ĺ����
    }

    my ($prize);
    $prize = '';

    # �������ա�����¾��
    $prize = ScoreBoard_Prize($island);

    # �ݤ������åꥹ��  ���ä����䤹�Τǡ��ꥹ�ȤϺ��
    $prize .= ScoreBoard_Taiji($island);

    # �����
    my $bumons = ScoreBoard_Bumon($island);

    my ($monslive);
    $monslive = ScoreBoard_LiveMonster($island);

    # �͹�����
    $me_sat = ScoreBoard_Eisei($island);

    # �Ҿ��
    my($Farmcpc) = ScoreBoard_Farm($island);

    # ��
    my ($house) = '';
    my ($hlv);
    my ($tax) = $island->{'eisei1'};
    $hlv = Calc_HouseLevel($island->{'pts'});
    my $onm = $island->{'onm'};
    my $n = ('�ξ���', '�δʰ׽���', '�ν���', '�ι�齻��', '�ι�š', '�����š', '�ι���š', '�ξ�', '�ε��', '�β����')[$hlv];
    my $zeikin = int($island->{'pop'} * ($hlv + 1) * $tax / 100);

    if ($tax) {
        $house  = "<span class='house'>";
        $house .= "<img src=\"./img/land/house${hlv}.gif\" alt=\"$onm$n\" class='landinfoIcon'>��Ψ$tax��($zeikin$HunitMoney)" ;
        $house .= '</span>';
    }

    my ($weather);
    my ($w_tag);
    my ($wn_tag);
    $weather    = $island->{'weather_old'};
    $w_tag      = "<img src='./img/weather/weather$weather.gif' TITLE='Ϣ³��$island->{'weather_chain'}��'>";
    $weather    = $island->{'weather'};
    $wn_tag      = "<img src='./img/weather/weather$weather.gif'>";

    my ($areatag);

    $areatag = (!$island->{'area'}) ? '0��' : "$island->{'area'}$HunitArea";


    out(<<END);
<div id='islandInfo' align="center">
<table border>
$bStr
<tr>
$rStr1
<th $HbgTitleCell>${HtagTH_}ŷ��${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}<small>��������<br>ŷ��ͽ��</small>${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}����${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}�͸�${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}����${H_tagTH}</th>
$mStr1
<th $HbgTitleCell>${HtagTH_}����${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}����${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}����${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}HT����${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}�η���${H_tagTH}</th>
$uStr1
<th $HbgTitleCell>${HtagTH_}����<br>����${H_tagTH}</th>
$msStr1
<th $HbgTitleCell>${HtagTH_}��˾/����${H_tagTH}</th>
</TR>
<TR>
$rStr2
<TD $HbgInfoCell align=center>$w_tag</td>
<TD $HbgInfoCell align=center>$wn_tag</td>
<TD $HbgInfoCell align=center>$island->{'temperature'}</td>
<TD $HbgInfoCell align=right>$island->{'pop'}$HunitPop</td>
<TD $HbgInfoCell align=right>$areatag</td>
$mStr2
<TD $HbgInfoCell align=right>$island->{'food'}$HunitFood</td>
<TD $HbgInfoCell align=right>${farm}</td>
<TD $HbgInfoCell align=right>${factory}</td>
<TD $HbgInfoCell align=right>${HTfactor}</td>
<TD $HbgInfoCell align=right>${mountain}</td>
$uStr2
<TD $HbgInfoCell align=right>Lv${renae}</td>
$msStr2
<TD $HbgInfoCell align=right>$CivReqDisp[$civreq]</td>
</TR>
<TR>
<TD $HbgCommentCell COLSPAN=${col_num} align=left>${HtagtTH_}info��<font size="-1">$prize$house$monslive$Farmcpc$bumons$me_sat</font>${H_tagtTH}
END
    my $AllyBBS = '';
    if($HallyNumber){
        my $aNo = random(100);
        $aNo *= 10;
        for ($i = 0; $i < $HallyNumber; $i++) {
            my $ally  = $Hally[$i];
            my $member = $Hally[$i]->{'memberId'};
            my $flag = 1;
            foreach (@$member) {
                if($island->{'id'} == $_) {
                    $flag = 0;
                    last;
                }
            }
            next if($flag);
            my $allyId  = $Hally[$i]->{'id'};
            my $cpass = $ally->{'password'};
            my $jpass = $ally->{'Takayan'};
            my $set_name = $HcurrentName;
            $set_name =~ s/<FONT COLOR=\"[\w\#]+\"><B>(.*)<\/B><\/FONT>//g;
            $set_name =~ s/<[^<]*>//g;
            $set_name =~ s/\r//g;
            my $allyName = $ally->{'name'};
            $allyName =~ s/�ھ��ԡ���//g;
            $aNo += $i;
            my $campInfo = '';
            $campInfo = "<FORM name='allyForm$aNo' action='${HthisFile}' method='POST' target='_blank' style='margin-bottom: 0px;'>" if ($mode);
            $campInfo .=<<_CAMP_ if($mode && $HarmisticeTurn);
��[<A STYlE="text-decoration:none" HREF="JavaScript:void(0)" onClick="document.allyForm${aNo}.submit();return false;">��������</A>]
_CAMP_
            $campInfo .=<<_CAMP_ if($mode);
<INPUT type=hidden name="camp" value="$allyId">
<INPUT type=hidden name="ally" value="$allyId">
<INPUT type=hidden name="cpass" value="$cpass">
<INPUT type=hidden name="jpass" value="$jpass">
<INPUT type=hidden name="PASSWORD" value="$HdefaultPassword">
<INPUT type=hidden name="id" value="$island->{'id'}">
</FORM>
</td>
_CAMP_

            if ($mode && $HallyBbs) {
                if ($HarmisticeTurn) {
                    $AllyBBS .=<<_BBS_;
<font color="$ally->{'color'}"><b>$ally->{'mark'}</b></font>$ally->{'name'}
[<a style="text-decoration:none" href="JavaScript:void(0)" onClick="document.allyForm${aNo}.action='${HbaseDir}/${HallyBbsScript}';document.allyForm${aNo}.submit();return false;">�����ļ�</a>]
${campInfo}
_BBS_
                }
                else {
                    $AllyBBS .=<<_BBS_;
<a style="text-decoration:none" HREF="JavaScript:void(0)" onClick="document.allyForm${aNo}.action='${HbaseDir}/${HallyBbsScript}';document.allyForm${aNo}.submit();return false;">
<FONT COLOR="$ally->{'color'}"><B>$ally->{'mark'}</B></FONT>$ally->{'name'}</A>${campInfo}
_BBS_
                }
            }
            else {
                $AllyBBS .=<<_BBS_;
<font color="$ally->{'color'}"><b>$ally->{'mark'}</b></font>$ally->{'name'}${campInfo}
_BBS_
            }
        }
        $AllyBBS .= '';
        #$AllyBBS = "" if (!$allyId);
    }

    my ($allytitle) = $HarmisticeTurn ? '�ر�' : 'Ʊ��';
    out(<<END) if($HallyNumber);
  </td>
  </tr>
  <tr>
    <th $HbgTitleCell>${HtagTH_}${allytitle}${H_tagTH}</th>
    <td $HbgInfoCell colspan=${col_num} class='T'>${AllyBBS}
  </tr>
  </table>
</div>
END
}


# �����ƥ��ɽ��
sub islandItemData {
    print("<div id=itembox>");

    out(<<END);
  <table border>
    <tr>
      <th $HbgTitleCell align="center" rowspan="2">${HtagTH_}����ʪ${H_tagTH}</th>
END
    for ( $ibox = 0 ; $ibox < $HItem_MAX ; $ibox++){

        print( "<th $HbgTitleCell align=center>${HtagTH_}${ibox}${H_tagTH}</th>\n");
    }

    out(<<END);
    </tr>
    <tr>
END

    my ($island) = $Hislands[$HcurrentNumber];
    my ($land) = $island->{'item_land'};
    my ($lv) = $island->{'item_landValue'};
    my ($lv2) = $island->{'item_landValue2'};
    my ($id) = $island->{'id'};
    my ($shrturn) = $island->{'shrturn'};

    for ( $ibox = 0 ; $ibox < $HItem_MAX ; $ibox++){

        print( "<td id='itembox${ibox}' ${HbgInfoCell} align='center'>");
        # ���Ϸ������
        #landString($island, $land->[$ibox], $lv->[$ibox], $lv2->[$ibox], $ibox, 0, 1, "", $jsmode, 1);
        landString2($island, $ibox, 0,  1, "", $jsmode, 1);

        print( "</td>\n");
    }

    out(<<END);
    </TR>
  </table>
END

    print('</div>');
}


sub landString2 {
    my ($island, $x, $y, $mode, $comStr, $jsmode, $boxmode) = @_;

    my ($kind);
    my ($lv);
    my ($lv2);
    my ($lv3);

    if ($boxmode) {

        my ($ikind) = $island->{'item_land'};
        my ($ilv) = $island->{'item_landValue'};
        my ($ilv2) = $island->{'item_landValue2'};
        my ($ilv3) = $island->{'item_landValue3'};
        #my ($id) = $island->{'id'};
        #my ($shrturn) = $island->{'shrturn'};

        $kind = $ikind->[$x];
        $lv = $ilv->[$x];
        $lv2 = $ilv2->[$x];
        $lv3 = $ilv3->[$x];
        $y = 0;
        $comStr = '';
        #landString($island, $kind, $lv, $lv2, $x, 0, 1, "", $jsmode, $boxmode);
    }
    else {

        my ($land) = $island->{'land'};
        my ($landValue) = $island->{'landValue'};
        my ($landValue2) = $island->{'landValue2'};
        my ($landValue3) = $island->{'landValue3'};

        $kind = $land->[$x][$y];
        $lv = $landValue->[$x][$y];
        $lv2 = $landValue2->[$x][$y];
        $lv3 = $landValue3->[$x][$y];
    }

    my ($land_data) = conv_island_struct($kind, $lv, $lv2, $lv3);
    landString($island, $land_data, $x, $y, $mode, $comStr, $jsmode, $boxmode);
}


#----------------------------------------------------------------------
sub Forest_Img_Gen {

    my ($Forest_Img) = 'land6.png';
    $mon += 1;

    if (   (%main::Hday{'month'} == 10)
        || (%main::Hday{'month'} == 11)
        || (%main::Hday{'month'} == 12) ) {
        $Forest_Img = 'land6_aut.png';
    }

    return $Forest_Img;
}


#----------------------------------------------------------------------
sub conv_island_struct {
    my ($l , $lv , $lv2, $lv3) = @_;

    return {
        'kind' => $l,
        'landValue' => $lv,
        'landValue2' => $lv2,
        'landValue3' => $lv3,
    };
}


#----------------------------------------------------------------------
sub College_LandString {
    my ($island , $x, $y, $land_data ,$mode, $shrturn, $boxmode) = @_;
    my ($image, $alt, $naviTitle, $naviText);

    my ($kind , $lv , $lv2 , $lv3);
    $kind = $land_data->{'kind'};
    $lv = $land_data->{'landValue'};
    $lv2 = $land_data->{'landValue2'};
    $lv3 = $land_data->{'landValue3'};

        # ���
        my($p, $n);
        if($lv == 0) {
            $p = '34';
            $n = '�������';
        } elsif($lv == 1) {
            $p = '35';
            $n = '�������';
        } elsif($lv == 2) {
            $p = '36';
            $n = '������';
        } elsif($lv == 3) {
            $p = '37';
            $n = '�������';
        } elsif($lv == 4) {
            $p = '44';
            $n = "��ʪ��� (�Ե�)$rt HP:$mshp AP:$msap DP:$msdp SP:${mssp}$rt $mswinɤ���� / �и���$msexe";
        } elsif($lv == 96) {
            $p = '44';
            $p = '44x' if($mode == 1);
            $n = "��ʪ��� (�ж�)$rt HP:$mshp AP:$msap DP:$msdp SP:${mssp}$rt $mswinɤ���� / �и���$msexe";
        } elsif($lv == 98) {
            $p = '48';
            $n = "��ʪ��� (�Ե�)$rt HP:$mshp AP:$msap DP:$msdp SP:${mssp}$rt $mswinɤ���� / �и���$msexe";
        } elsif($lv == 97) {
            $p = '48';
            $p = '48x' if($mode == 1);
            $n = "��ʪ��� (�ж�)$rt HP:$mshp AP:$msap DP:$msdp SP:${mssp}$rt $mswinɤ���� / �и���$msexe";
        } elsif($lv == 99) {
            $p = '47';
            $n = '��ʪ��� (��ư��)';
        } else {
            $p = '46';
            $n = '�������';
        }

        $image = "land${p}.gif";
        $alt = "$n";

        $naviTitle = (split(' ',$n))[0];

        if ($lv2 > 0) {
            $naviText = "������($lv2)";
        }

    return ($image, $alt, $naviTitle, $naviText);
}
#----------------------------------------------------------------------
sub Sea_LandString {
    my ($island , $x , $y , $land_data , $mode, $shrturn, $boxmode) = @_;

    my ($image, $alt, $naviTitle, $naviText) = ('','','','');

    my ($kind , $lv , $lv2 , $lv3);
    $kind = $land_data->{'kind'};
    $lv = $land_data->{'landValue'};
    $lv2 = $land_data->{'landValue2'};
    $lv3 = $land_data->{'landValue3'};

    if ( $boxmode ) {
        $image = 'noitem.gif';
        $alt = '�ʤ�';
        $naviTitle  = '�ʤ�';

    }else{
        if($lv) {
            # ����
            $image = 'land14.gif';
            $alt = '��(����)';
            $naviTitle  = '����';
        } else {
            # ��
            $image = Sea_Img_Gen(1, $x, $y);
            $alt = '��';
            $naviTitle  = '��';
        }
    }
    return ($image, $alt, $naviTitle, $naviText);
}


#----------------------------------------------------------------------
sub Town_LandString {
    my ($island,$x,$y,$land_data , $mode, $shrturn, $boxmode) = @_;
    my ($image, $alt, $naviTitle, $naviText) = ('','','','');

    my ($kind , $lv , $lv2 , $lv3);
    $kind = $land_data->{'kind'};
    $lv = $land_data->{'landValue'};
    $lv2 = $land_data->{'landValue2'};
    $lv3 = $land_data->{'landValue3'};

        # Į
        my($p, $n);
        if($lv < 30) {
            $p = 'land3.png';
            $n = '¼';
        } elsif($lv < 65) {
            $p = 'land4.png';
            $n = 'Į';
        } elsif($lv < 100) {
            $p = 'land402.png';
            $n = 'Į';
        } elsif($lv < 150) {
            $p = 'land5.png';
            $n = '�Ի�';
        } elsif($lv < 200) {
            $p = 'land501.png';
            $n = '�Ի�';
        } else {
            $p = 'land502.png';
            $n = '���Ի�';
        }

        $image = $p;
        $alt = "$n(${lv}$HunitPop)";
        $naviTitle  = $n;
        $naviText  = "${lv}${HunitPop}";

    return ($image, $alt, $naviTitle, $naviText);
}


#----------------------------------------------------------------------
sub Waste_LandString {
    my ($island,$x,$y,$land_data ,$mode, $shrturn, $boxmode) = @_;
    my ($image, $alt, $naviTitle, $naviText) = ('','','','');

    my ($kind , $lv , $lv2 , $lv3);
    $kind = $land_data->{'kind'};
    $lv = $land_data->{'landValue'};
    $lv2 = $land_data->{'landValue2'};
    $lv3 = $land_data->{'landValue3'};

    # ����
    $alt = '����';
    $naviTitle  = '����';
    $naviText  = '';

    if($lv == 1) {
        $image = 'land13.gif';  # ������
    } elsif($lv  == 2) {
        $image = 'land13m.gif'; # ���
    } elsif($lv  == 3) {
        $image = 'iwaba.gif';   # ���
        $alt = '���';
        $naviTitle  = '���';
    } elsif($lv  == 4) {
        $image = 'wastetown.png'; # ���
    } else {
        $image = 'land1.png';
    }

    return ($image, $alt, $naviTitle, $naviText);
}


#----------------------------------------------------------------------
sub Mountain_LandString {
    my ($island,$x,$y,$land_data , $mode, $shrturn, $boxmode) = @_;

    my ($image, $alt, $naviTitle, $naviText) = ('','','','');
    my ($kind , $lv , $lv2 , $lv3);

    $kind = $land_data->{'kind'};
    $lv = $land_data->{'landValue'};
    $lv2 = $land_data->{'landValue2'};
    $lv3 = $land_data->{'landValue3'};

    # ��
    my($str);
    $str = '';
    if($lv > 0) {
        if ( $lv < 20){
            $image = 'mt1.png';
        }elsif ( $lv < 30){
            $image = 'mt2.png';
        }elsif ( $lv < 40){
            $image = 'mt3.png';
        }else{
            $image = 'mt4.png';
        }
        $alt = "��(�η���${lv}0${HunitPop}����)";
        $naviText  = "�η���${lv}0${HunitPop}����";
    } else {
        $image = 'land11.gif';
        $alt = '��';
    }
    $naviTitle  = '��';

    return ($image, $alt, $naviTitle, $naviText);
}

#----------------------------------------------------------------------
sub Umicity_LandString {
    my($island , $x,$y,$land_data , $mode, $shrturn, $boxmode) = @_;
    my ($image, $alt, $naviTitle, $naviText);

    my ($kind , $lv , $lv2 , $lv3);
    $kind = $land_data->{'kind'};
    $lv = $land_data->{'landValue'};
    $lv2 = $land_data->{'landValue2'};
    $lv3 = $land_data->{'landValue3'};

    my $mwork =  int($lv/30);
    my $hwork =  int($lv/30);
    #my $lwork =  int($lv/60);
    $image = 'land82.gif';
    $alt = "���Ի�(${lv}$HunitPop/����${mwork}0$HunitPop/HT����${hwork}0$HunitPop)";
    $naviText  = "${lv}$HunitPop&lt;br&gt;����${mwork}0$HunitPop&lt;br&gt;HT����${hwork}0$HunitPop";
    $naviTitle  = '���Ի�';

    return ($image, $alt, $naviTitle, $naviText);
}


#----------------------------------------------------------------------
sub Plains_LandString {
    my($island , $x,$y,$land_data , $mode, $shrturn, $boxmode) = @_;
    my ($image, $alt, $naviTitle, $naviText);

    my ($kind , $lv , $lv2 , $lv3);
    $kind = $land_data->{'kind'};
    $lv = $land_data->{'landValue'};
    $lv2 = $land_data->{'landValue2'};
    $lv3 = $land_data->{'landValue3'};

    # ʿ��
    if (!$lv) {
        $image = 'land2.gif';
        $alt = 'ʿ��';
        $naviTitle  = 'ʿ��';
    } else {
        $image = 'yotei.png';
        $alt = 'ͽ����';
        $naviTitle  = 'ͽ����';
    }

    return ($image, $alt, $naviTitle, $naviText);
}

#----------------------------------------------------------------------
sub landString {
    my($island, $land_data, $x, $y, $mode, $comStr, $jsmode, $boxmode) = @_;
    $mode = ($mode) ? $mode : 0;

    my ($image, $alt);
    my ($rt) = "\n";
    my ($naviTitle);
    my ($naviText) = '';
    my ($naviExp) = "''";
    my ($monster_style) ='';
    my ($map_style) = 'maptile';
    my ($shrturn) = $island->{'shrturn'};
    my ($id) = $island->{'id'};
    my ($shutomessage) = $island->{'shutomessage'};

    #my ($land_data) = conv_island_struct($l, $lv, $lv2, $lv3);

    my ($kind , $lv , $lv2 , $lv3);
    $l = $land_data->{'kind'};
    $lv = $land_data->{'landValue'};
    $lv2 = $land_data->{'landValue2'};
    $lv3 = $land_data->{'landValue3'};

    if(defined $pic_sub->{"$l"}) {

        my ($subroutine) = $pic_sub->{"$l"};
        ($image, $alt, $naviTitle, $naviText) = $subroutine->($island , $x,$y,$land_data, $mode, $shrturn, $boxmode);

    } elsif($l == $HlandFarm) {
        # ����
        if ($lv2 == 1){
            $image = 'kaju.gif';
            $alt = "�̼���(${lv}0${HunitPop}����)";
            $naviTitle  = '�̼���';

        } elsif($lv2 == 2) {
            $image = 'sio.gif';
            $alt = "����(${lv}0${HunitPop}����)";
            $naviTitle  = '����';

        }else{
            if($lv < 25) {
                $image = 'farm1.png';
            } elsif($lv < 50) {
                $image = 'farm2.png';
            } else{
                $image = 'farm3.png';
            }
            $alt = "����(${lv}0${HunitPop}����)";
            $naviTitle  = '����';
        }
        $naviText  = "${lv}0${HunitPop}����";

    } elsif($l == $HlandNewtown) {
        # �˥塼������
        my $nwork =  int($lv/15);
        if ($lv < 100){
            $image = 'new1.png';
        }else{
            $image = 'new2.png';
        }
        if ($nwork > 0) {
            $alt = "�˥塼������(${lv}$HunitPop/����${nwork}0$HunitPop)";
            $naviText  = "${lv}$HunitPop&lt;br&gt;����${nwork}0$HunitPop";
        }else{
            $alt = "�˥塼������(${lv}$HunitPop)";
            $naviText  = "${lv}$HunitPop";
        }
        $naviTitle  = '�˥塼������';

    } elsif($l == $HlandProcity) {
        # Į
        my ($c) = '�ɺ��Իԥ��';
        if ($lv < 110) {
            $c .= '��';
        } elsif($lv < 130) {
            $c .= '��';
        } elsif($lv < 160) {
            $c .= '��';
        } elsif($lv < 200) {
            $c .= '��';
        } else {
            $c .= '��';
        }

        $image = "land26.gif";
        $alt = "$c(${lv}$HunitPop)";
        $naviTitle  = $c;
        $naviText  = "${lv}${HunitPop}";

    } elsif($l == $HlandForest) {
        # ��
        $image = Forest_Img_Gen();
        $alt = '��';
        # �Ѹ��Ԥξ����ڤ��ܿ�����
        $alt .= "(${lv}$HunitTree)" if ($mode == 1);
        $naviTitle  = '��';
        $naviText = "(${lv}$HunitTree)" if ($mode == 1);

    } elsif($l == $HlandFactory) {
        # ����
        if ($lv2 == 1) {
            $image = 'moku.png';
            $alt = "�ڹ���(${lv}0${HunitPop}����)";
            $naviTitle  = '�ڹ���';
            $naviText  = "${lv}0${HunitPop}����";

        }else{
            $image = 'land8.gif';
            $alt = "����(${lv}0${HunitPop}����)";
            $naviTitle  = '����';
            $naviText  = "${lv}0${HunitPop}����";
        }

    } elsif ($l == $HlandNursery) {
        # �ܿ���
        $image = 'nursery.gif';
        $alt = "�ܿ���(${lv}0${HunitPop}����)";
        $naviTitle  = '�ܿ���';
        $naviText  = "${lv}0${HunitPop}����";

    } elsif ($l == $HlandKyujokai) {
        # ����
        $image = 'land23kai.gif';
        $alt = "¿��Ū����������$rt ����$nn$rt ��($sto)��($std)KP($stk)$rt ���������� ����$kachiten / $stwin��$stlose��$stdrowʬ$rt / �̻�$stwint��$stloset��$stdrowtʬ / ͥ��$styusho��)";
        $naviTitle  = '¿��Ū����������';
        $naviText  = "����$nn&lt;br&gt; ��($sto)��($std)KP($stk)&lt;br&gt; ���������� ����$kachiten / $stwin��$stlose��$stdrowʬ<br> / �̻�$stwint��$stloset��$stdrowtʬ / ͥ��$styusho��)";

    } elsif ($l == $HlandFoodim) {
        # �����
        my ($f);
        if ($lv < 480) {
            $f = '��ʪ�����';
            $image = "land25.gif";
        } else {
            $f = '�ɺҷ���ʪ�����';
            $image = "land25_bousai.png";
        }
        $alt = "$f(���촹��${lv}0${HunitPop}����)";
        $naviTitle  = $f;
        $naviText  = "���촹��${lv}0${HunitPop}����";

    } elsif ($l == $HlandFarmchi) {
        $works = $lv;
        $image = 'land31.gif';
        $alt = "�ܷܾ�(${lv}����/������${works}$HunitFood)";
        $naviTitle  = '�ܷܾ�';
        $naviText  = "${lv}����&lt;br&gt;������${works}$HunitFood";

    } elsif ($l == $HlandFarmpic) {
        $works = $lv*2;
        $image = 'land32.gif';
        $alt = "���ھ�(${lv}��Ƭ/������${works}$HunitFood)";
        $naviTitle  = '���ھ�';
        $naviText  = "${lv}��Ƭ&lt;br&gt;������${works}$HunitFood";

    } elsif ($l == $HlandFarmcow) {
        $works = $lv*3;
        $image = 'land33.gif';
        $alt = "�Ҿ�(${lv}��Ƭ/������${works}$HunitFood)";
        $naviTitle  = '�Ҿ�';
        $naviText  = "${lv}��Ƭ&lt;br&gt;������${works}$HunitFood";

    } elsif ($l == $HlandBase) {
        if ($mode == 1) {
            # �ߥ��������
            my($level) = expToLevel($l, $lv);
            $image = "missile${level}.png";
            $alt = "�ߥ�������� (��٥� ${level}/�и��� $lv)";
            $naviText = "(Lv ${level}/�и��� $lv)";
            $naviTitle  = '�ߥ��������';
        } else {
            # �Ѹ��Ԥξ��Ͽ��Τդ�
            $image = Forest_Img_Gen();
            $alt = '��';
            $naviTitle  = '��';
        }

    } elsif ($l == $HlandSbase) {
        # �������
        if($mode == 1) {
            my($level) = expToLevel($l, $lv);
            if ($level == 1) {
                $image = 'land12_1.gif';

            } elsif ($level == 2) {
                $image = 'land12_2.gif';

            }else{
                $image = 'land12.gif';
            }

            $alt = "������� (��٥� ${level}/�и��� $lv)";
            $naviText = "(Lv ${level}/�и��� $lv)";
            $naviTitle  = '�������';
        } else {
            # �Ѹ��Ԥξ��ϳ��Τդ�
            $image = Sea_Img_Gen($id, $x, $y);
            $alt = '��';
            $naviTitle  = '��';
        }

    } elsif ($l == $HlandSeacity) {
        # �����Ի�
        if($mode == 1) {
            $image = 'land17.gif';
            $alt = "�����Ի�(${lv}$HunitPop)";
            $naviText = "�����Ի�(${lv}$HunitPop)";
            $naviTitle  = '�����Ի�';
        } else {
            # �Ѹ��Ԥξ��ϳ��Τդ�
            $image = Sea_Img_Gen($id, $x, $y);
            $alt = '��';
            $naviTitle  = '��';
        }

    } elsif ($l == $HlandHTFactory) {
        # �ϥ��ƥ�����
        $image = 'land50.gif';
        $alt = "�ϥ��ƥ�¿���Ҵ��(${lv}0${HunitPop}����)";
        $naviTitle  = '�ϥ��ƥ�¿���Ҵ��';
        $naviText  = "${lv}0${HunitPop}����";

    } elsif ($l == $HlandSHTF) {
        $image = 'land85.gif';
        $alt = "HT����${lv}0${HunitPop}����";
        $naviTitle = "�ϥ��ƥ�¿���Ҵ�ȡ���";
        $naviText = "${lv}0${HunitPop}����";

    } elsif ($l == $HlandFiredept) {
        $image = 'firedept.gif';
        $alt = "���ɽ�";
        $naviTitle = "���ɽ�";

    } elsif ($l == $HlandFrocity) {
        # �����Ի�
        if ($lv < 100) {
            $image = 'land39_mini.png';
        } elsif ($lv < 170) {
            $image = 'land39.gif';
        } else {
            $image = 'land39_up.gif';
        }
        $alt = "�����Իԥᥬ�ե���(${lv}$HunitPop)";
        $naviTitle  = '�����Իԥᥬ�ե���';
        $naviText  = "${lv}${HunitPop}";

    } elsif ($l == $HlandMinato) {
        # ��
        $image = 'land21.gif';
        $alt = "��Į(${lv}$HunitPop)";
        $naviTitle  = '��Į';
        $naviText  = "${lv}${HunitPop}";

    } elsif ($l == $HlandOnsen) {
        # ����
        $image = 'land40.gif';
        $alt = "������(${lv}$HunitPop)";
        $naviTitle  = '������';
        $naviText  = "${lv}${HunitPop}";

    } elsif ($l == $HlandSunahama) {
        # ����
        $image = 'land38.gif';
        if ($lv > 0) {

            $alt = '����';
            $naviTitle  = '����';
        }else{

            $alt = '����';
            $naviTitle  = '����';
        }

    } elsif ($l == $HlandDefence) {
        # �ɱһ���
        my ($deflv , $defHP) = GetDefenceSpec($lv);

        if ($deflv == 1) {
            $image = 'land10kai.gif';
            $alt = '�ɱһ��ߡ���';
            $naviTitle  = '�ɱһ��ߡ���';

        } elsif ($deflv == 2) {
            $image = 'land88.gif';
            $naviTitle  = "�ɱһ��ߡ���+Lzr";
            if($mode == 1) {
                $alt = "�ɱһ��ߡ���+Lzr(�ѵס�$defHP)";
                $naviText  = "�ѵס�$defHP";
            }else{
                $alt = "�ɱһ��ߡ���+Lzr";
            }

        } elsif ($deflv == 0) {
            $image = 'land10.gif';
            $alt = '�ɱһ���';
            $naviTitle  = '�ɱһ���';

        } else {
            $image = 'land10.gif';
            $alt = "�ɱһ���";
            $naviTitle  = "�ɱһ���$lv";
        }

    } elsif($l == $HlandHaribote) {
        # �ϥ�ܥ�
        $image = 'land10.gif';
        if ($mode == 1) {
            $alt = '�ϥ�ܥ�';
            $naviTitle  = '�ϥ�ܥ�';
        } else {
            # �Ѹ��Ԥξ����ɱһ��ߤΤդ�
            $alt = '�ɱһ���';
            $naviTitle  = '�ɱһ���';
        }

    } elsif ($l == $HlandTrain) {
        $image = "./train/Rail${lv}.gif";
        if ($lv & $Train_Exist) {
            $alt = '�ż�';
            $naviTitle  = '�ż�';
            $naviText  = "�����󤴤Ȥ�";
        }else{
            $alt = '��ϩ';
            $naviTitle  = '��ϩ';
        }

    } elsif($l == $HlandBeachPark) {
        $image = 'beach.png';
        $alt = "�������(���Ȱ�${lv}0${HunitPop})";
        $naviTitle  = '�������';
        $naviText  = "���Ȱ�${lv}0${HunitPop}";

    } elsif($l == $HlandIce) {
        if($lv > 0) {
            $image = 'land42.gif';
            $alt = "ŷ���������Ⱦ�(���Ȱ�${lv}0${HunitPop})";
            $naviTitle  = 'ŷ���������Ⱦ�';
            $naviText  = "���Ȱ�${lv}0${HunitPop}";
        } else {
            $image = 'land41.gif';
            $alt = 'ɹ��';
            $naviTitle  = 'ɹ��';
        }

    } elsif($l == $HlandInaka) {
        # ���ʤ�
        $image = 'inaka.gif';
        $alt = '���ʤ�';
        $naviTitle  = '���ʤ�';
        my ($fm) = int($lv/10) + 1;
        $naviText  = "${lv}$HunitPop&lt;br&gt;���ϡ�${fm}0${HunitPop}����";

    } elsif($l == $HlandOil) {
        # ��������
        $image = 'land16.gif';
        $alt = '��������';
        $naviTitle  = '��������';

    } elsif($l == $HlandMonument) {
        # ��ǰ��
        $image = $HmonumentImage[$lv];
        $alt = $HmonumentName[$lv];
        $naviTitle  = $alt;

    } elsif($l == $HlandFune) {
        # fune
        $image = $HfuneImage[$lv];
        $alt = $HfuneName[$lv];
        $naviTitle  = $alt;
        $naviExp = "\'SHIP$lv\'";

    } elsif($l == $HlandMonster) {
        # ����
        my($kind, $name, $hp) = monsterSpec($lv);
        $image = $HmonsterImage[$kind];

        # �Ų���?
        if(isMonsterCuring($kind)) {
            # �Ų���
            $image = $HmonsterImage2[$kind];
        }
        $alt = "$name(����${hp})";
        $naviTitle  = $name;
        $naviText  = "����${hp}";
        $alt  = "$name(����:����)" if ( $kind == $Mons_Totten);
        $naviText  = "����:����" if ( $kind == $Mons_Totten);
        $naviExp = "\'MONSTER$kind\'";

        $map_style = 'maptile_ret' if(seqnum2(($HislandTurn+$y),($id+$x)) % 2);

    } elsif($l == $HlandPark) {
        # ͷ����
        $image = 'park.gif';
        $alt = "ͷ����(���Ȱ�${lv}0${HunitPop}/���׸���${mikomi}$HunitMoney�ʾ�)";
        $naviTitle  = 'ͷ����';
        $naviText  = "���Ȱ�${lv}0${HunitPop}<br>���׸���${mikomi}$HunitMoney�ʾ�";


    } elsif($l == $HlandUmiamu) {
        # �����ߤ�
        $image = 'land24.gif';
        $alt = "�����ߤ�(���Ȱ�${lv}0${HunitPop})";
        $naviTitle  = '�����ߤ�';
        $naviText  = "���Ȱ�${lv}0${HunitPop}";

    } elsif($l == $HlandKatorikun) {
        # ��路
        $image = 'katori.gif';
        $alt = '�ڤι�褯��';
        $naviTitle  = '�ڤι�褯��';

    } elsif($l == $HlandBigtown) {
        # �����Ի�
        my $mwork =  int($lv/20);
        my $lwork =  int($lv/30);
        $image = 'land29.gif';
        $alt = "�����Ի�(${lv}$HunitPop/����${mwork}0$HunitPop/����${lwork}0$HunitPop)";
        $naviTitle  = '�����Ի�';
        $naviText  = "${lv}$HunitPop&lt;br&gt;����${mwork}0$HunitPop&lt;br&gt;����${lwork}0$HunitPop";

    } elsif($l == $HlandBettown) {
        # �������Ի�
        if ( $lv >= 2000 ) {
            $image = 'bedtown2.gif';

        }else{
            $image = 'land45.png';

        }
        $alt = "�������Ի�(${lv}$HunitPop)";
        $naviTitle  = '�������Ի�';
        $naviText  = "${lv}$HunitPop";

    } elsif($l == $HlandRizort) {
        # �꥾������
        my ($rena) = $island->{'rena'};
        my ($eis1) = $island->{'eis1'};
        my ($eis2) = $island->{'eis2'};
        my ($eis3) = $island->{'eis3'};
        my ($eis5) = $island->{'eis5'};
        my ($fore) = $island->{'fore'};
        my ($monsterlive) = $island->{'monsterlive'};

        my ($rwork) = $lv + $eis1 + $eis2 + $eis3 + $eis5 + int($fore/10) + int($rena/10) - $monsterlive * 100;
        $image = 'land43.png';
        $alt = "�꥾������(�ںߴѸ���${lv}$HunitPop/���׸���${rwork}$HunitMoney)";
        $naviTitle  = '�꥾������';
        $naviText  = "�ںߴѸ���${lv}$HunitPop&lt;br&gt;���׸���${rwork}$HunitMoney";

    } elsif($l == $HlandBigRizort) {
        # �꥾������
        $image = 'land49.gif';
        $alt = "�׳��꥾���ȥۥƥ�(�ںߴѸ���${lv}$HunitPop)";
        $naviTitle  = '�׳��꥾���ȥۥƥ�';
        $naviText  = "�ںߴѸ���${lv}$HunitPop";

    } elsif($l == $HlandRottenSea) {
        # �峤
        $image = 'land20.gif';
        $alt = '�峤';
        $naviTitle  = '�峤';

    } elsif($l == $HlandOilCity) {
        # �����Ի�
        my $mwork =  int($lv/40);
        $image = 'oilcity.gif';
        $alt = "�����Ի�(${lv}$HunitPop/����${mwork}0$HunitPop)";
        $naviText  = "${lv}$HunitPop&lt;br&gt;����${mwork}0$HunitPop";
        $naviTitle  = '�����Ի�';

    } elsif($l == $HlandRocket) {
        # ���å�
        $image = 'monument27.gif';
        $naviTitle  = '���å�';
        $alt = "���å�";

    } elsif($l == $HlandUmishuto) {
        # ������
        if($mode == 0) {
            # �Ѹ��Ԥξ��ϳ��Τդ�
            $image = Sea_Img_Gen($id, $x, $y);
            $alt = '��';
            $naviTitle  = '��';
        } else {
            $image = 'umishuto.png';
            $alt = "�������(${lv}$HunitPop)";
            $naviTitle  = '�������';
            $naviText  = "(${lv}$HunitPop)";
        }

    } elsif($l == $HlandGold) {
        # �⻳
        $image = 'land15.gif';
        $alt = "�⻳(�η���${lv}0${HunitPop}����)";
        $naviTitle  = '�⻳';
        $naviText  = "�⻳${lv}0${HunitPop}����";

    } elsif($l == $HlandSeatown) {
        # ���쿷�Ի�
        if($mode == 1) {
            my $owork =  int($lv/40);
            $image = 'land30.gif';
            $alt = "���쿷�Ի�(${lv}$HunitPop/����${owork}0$HunitPop/����${owork}0$HunitPop)";
            $naviTitle  = '���쿷�Ի�';
            $naviText  = "(${lv}$HunitPop/����${owork}0$HunitPop/����${owork}0$HunitPop)";
        } else {
            # �Ѹ��Ԥξ��ϳ��Τդ�
            $image = Sea_Img_Gen($id, $x, $y);
            $alt = '��';
            $naviTitle  = '��';
        }

    } elsif($l == $HlandYougan) {
        # �ϴ�����
        $image = 'land60.gif';
        $alt = '�ϴ�����';
        $naviTitle  = '�ϴ�����';

    } elsif($l == $HlandStation) {
        # ��
        $image = 'station.gif';
        $alt = '��';
        $naviTitle  = '��';

    } elsif($l == $HlandHouse) {
        # ���β�
        my($n) = $onm;
        $n .= ('�ξ���', '�δʰ׽���', '�ν���', '�ι�齻��', '�ι�š', '�����š', '�ι���š', '�ξ�', '�ε��', '�β����')[$hlv];
        $image = "house${hlv}.gif";
        $alt = "$n";
        $naviTitle = $n;

    } elsif($l == $HlandKyujo) {
        # ����
        $image = 'land23.gif';
        $alt = '����';
        $naviTitle  = '����';

    } elsif($l == $HlandInoraLand) {
        # ͷ����
        $image = 'inoraland.gif';
        $alt = "���Τ����(���Ȱ�${lv}0${HunitPop}/���׸���${mikomi}$HunitMoney�ʾ�)";
        $naviTitle  = '���Τ����';
        $naviText  = "���Ȱ�${lv}0${HunitPop}<br>���׸���${mikomi}$HunitMoney�ʾ�";

    } elsif($l == $HlandBigFood) {
        my ($foodkind);
        my ($foodHP);
        $foodkind = $lv >> $Food_Kind_Shift;

        $image =  $BigFoodImage[$foodkind];
        $alt = $BigFoodName[$foodkind];
        $naviTitle  = $BigFoodName[$foodkind];
        $foodHP = $lv & $Food_HP_MASK;
        $naviText  = "���ϡ�${foodHP}";

    } elsif($l == $HlandYakusho) {
        # �����
        $image =  'land52.gif';
        $alt = "�����:��٥�:${lv}";
        $naviTitle  = "�����:��٥�:${lv}";
        $naviText = "��٥�:${lv}";

    } elsif($l == $HlandOmamori) {
        # ����
        $image = 'mamori.gif';
        $naviTitle  = '���ޤ��';
        $alt = "���ޤ�ꡧ���̡��Ĥ�${lv}";
        $naviText  = "���ޤ�ꡧ���̡��Ĥ�${lv}";

    } elsif($l == $HlandShuto) {
        # ����
        $image = 'shuto.png';
        $shutomessage =~ s/'/��/g;
        $alt = "����$shutomessage(${lv}$HunitPop)";
        $naviTitle  = "����$shutomessage";
        $naviText  = "${lv}$HunitPop";

    } elsif($l == $HlandEgg) {
        # ��
        $image =  $HEggImage[$lv];
        $alt = '��';
        $naviTitle  = '��';

    } elsif($l == $HlandSeki) {
        # �ؽ�
        $image = 'land27.gif';
        $alt = '�ؽ�';
        $naviTitle  = '�ؽ�';

    } elsif($l == $HlandGomi) {
        # �ؽ�
        $image = 'gomi_yotei.png';
        $alt = '��Ω��';
        $naviTitle  = '��Ω��';
        $naviText  = "${lv}�Υ���";

    } elsif($l == $HlandShrine) {
        # ���ο���
        $image = 'shrine.gif';
        $alt = "���ο���";
        $alt .= "(������${lv})" if($lv > 0);
        $naviTitle  = '���ο���';
        $naviText = "������${lv}" if($lv > 0);

    } elsif($l == $HlandZoo) {
        # ưʪ��
        my ($zookazu, $zookazus, $m_syurui) = Get_ZooState($island);
        my ($bariaA) = $island->{'rena'} - $zookazus * 25;
        my ($bariaB) = $island->{'rena'} - $zookazus * 50;


        $image = 'land84.gif'; # ��ǰ��β�����ή��
        $alt = "ưʪ��Lv${lv}";
        $naviTitle  = "ưʪ��Lv${lv}";
        $naviText = "$m_syurui����$zookazuɤ/$mNameList<br>�Хꥢ��[$bariaA]�Хꥢ��[$bariaB]";

    } elsif($l == $HlandHospital) {
        $image =  'GShospital.gif';
        $alt = '�±�';
        $naviTitle  = '�±�';

    } elsif($l == $HlandBoueki) {
        $image =  'land70.gif';
        $alt = '�ǰ׹�';
        $naviTitle  = '�ǰ׹�';

    } elsif($l == $HlandMine) {
        if($mode == 1) {
            my ($da) = $lv & $Hmine_DAMAGE_MASK;
            # ����
            $image = 'land22.gif';
            $image = 'sea_mine.gif' if ($lv & $Hmine_SEA_FLAG);
            $alt = "����(���᡼��$da)";
            $naviText = "����(���᡼��$da)";
        } else {
            # �Ѹ��Ԥξ��Ͽ��Τդ�
            $image = Forest_Img_Gen();
            $image = Sea_Img_Gen($id, $x, $y) if ($lv & $Hmine_SEA_FLAG);
            $alt = '��';
            $alt = '��' if ($lv & $Hmine_SEA_FLAG);
        }
        $naviTitle  = '��';
        $naviTitle  = '��' if ($lv & $Hmine_SEA_FLAG);

    } else{
        $alt = "kind:($l)/val:($lv)";
    }

    my $alt1 = $alt;
    $alt1 =~ s/$rt//g;

    $image = $HMapImgDir . $image;

    if ( $boxmode ) {
        $point = "($x)";
        if($jsmode) {
            out(qq|<A HREF="JavaScript:void(0);" onclick="boxslct($x);return true;" |);
            # out(qq|<A onclick="boxslct($x);return 1;" |);
            if($mode == 1 && $HmainMode ne 'landmap') {
                out(qq|onMouseOver="set_com($x,$y,'$point $alt1');status='$point $alt1';return true;" onMouseOut="status='';">|);
            }elsif($HmainMode eq 'landmap') {
                out(qq|onMouseOver="status= '$point $alt1';return 1;">|);
            }
            out("<img src=\"$image\"TITLE=\"$point $alt\" class='maptile'></A>");
        } else {
            if($mode == 1) {
                # ��ȯ���̤ξ��ϡ���ɸ����
                # out("<A HREF='JavaScript:void(0);' onclick='boxslct($x);return true;' ");
                out("<IMG  ");
                out("onclick=\"boxslct($x);return 1;\" onMouseOver=\"status = '$point $alt1 ';return true;\" onMouseOut=\"status = '';\" ");
                out("alt='' SRC=\"$image\" TITLE=\"$point $alt \" class='maptile cur_p'>");
                # ��ɸ�����Ĥ�
                #out('</A>');
            } else {
                out("<IMG alt='' SRC=\"$image\" class='maptile'>");
                # ��ɸ�����Ĥ�

            }
        }

    }else{
        my ($point) = "($x,$y)";

        #$point .= "debug($lv3)";

        if ($jsmode) {

            out(qq|<A HREF="JavaScript:void(0);" onclick="ps($x,$y);set_land($x,$y,'$point\\n $alt1','$image');" |);

            if (   ($mode == 1)
                && ($HmainMode ne 'landmap') ) {

                out(qq|onMouseOver="set_com($x,$y,'$point $alt1');status='$point $alt1 $comStr'; Navi($x,$y,'$image','$naviTitle','$naviText',$naviExp); return true;" onMouseOut="status='';">|);

            }elsif ($HmainMode eq 'landmap') {

                out(qq|onMouseOver="status= '$point $alt1 $comStr';return true;" onMouseOut="status = '';">|);
            }

            out("<img src=\"$image\"TITLE=\"$point $alt $comStr\" class='maptile'></A>");

        } else {

            if ($mode == 1) {

                # ��ȯ���̤ξ��ϡ���ɸ����
                out(qq|<A HREF=\"JavaScript:void(0);\" onclick=\"ps($x,$y);tohint('$point $alt1\\n$comStr');return true;\" onMouseOver="status = '$point $alt1 $comStr';return true;" onMouseOut="status = '';"><img src=\"$image\"TITLE=\"$point $alt $comStr\" class='${map_style}' alt=''></A>|);

            } else {
    #           out("<A HREF=\"JavaScript:void(0);\" onMouseOver=\"Navi($x, $y,'$image', '$naviTitle', '$naviText', $naviExp);\" onMouseOut=\"NaviClose(); return false\">");
    #           out("<A HREF=\"JavaScript:void(0);\" onMouseOver=\"Navi($x, $y,'$image', '$naviTitle', '$naviText', $naviExp); status = '$point $alt1 $comStr'; return true;\" onMouseOut=\"NaviClose(); status=''; return false\">");
    #           out("<img src=\"$image\" width=$Hms2 height=$Hms2 BORDER=0 onMouseOver=\"Navi($x,$y,'$image','$naviTitle','$naviText',$naviExp);\" onClick=\"Navi($x,$y,'$image','$naviTitle','$naviText',$naviExp);\" onMouseOut=\"NaviClose(); return false\">");
                out("<img src=\"$image\" class='${map_style}' alt='' onMouseOver=\"Navi($x,$y,'$image','$naviTitle','$naviText',$naviExp);\" ONKEYPRESS='return false;' onClick=\"Navi($x,$y,'$image','$naviTitle','$naviText',$naviExp);\">");
                # ��ɸ�����Ĥ�
    #           out("</A>");
            }
        }

    }
}


# �Ƽ��ĥ�ǡ���ɽ��(���ζ�˴) kokoha nokosu
sub islandData {
    my(@data) = @{$Hislands[$HcurrentNumber]->{'ext'}};

    # ������
    $data[1] = int($data[1] / 10);
    $data[2] = $data[2] ? "$data[2]��" : '�ʤ�';
    $data[3] = $data[3] ? "$data[3]��" : '�ʤ�';
    $data[4] = $data[4] ? "$data[4]00��" : '�ʤ�';
    $data[5] = $data[5] ? "$data[5]ȯ" : '�ʤ�';
    $data[6] = $data[6] ? "$data[6]ȯ" : '�ʤ�';
    $data[7] = $data[7] ? "$data[7]ȯ" : '�ʤ�';
    my ($monsterkill) = $Hislands[$HcurrentNumber]->{'taiji'} ? "$Hislands[$HcurrentNumber]->{'taiji'}$HunitMonster" : '�ʤ�';
    my ($aStr1, $aStr2) = ('', '');
    my ($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $Hislands[$HcurrentNumber]->{'eisei4'});
    my ($kachiten) = $stwin*3 + $stdrow;
    my $nn = $HStadiumResult[$stshoka];
    $nn = '������' if($nn eq '');

    if ($HallyNumber) {
        $aStr1 = "<th $HbgTitleCell align=center>${HtagTH_}�׸���${H_tagTH}</th>";
        $aStr2 = "<TD $HbgInfoCell align=center>$data[1]</td>";
    }

    my ($island) = $Hislands[$HcurrentNumber];
    my ($work_farm , $work_biz , $work_bizHT ,  $unemployed , $unemployed_str);
    my ($pop, $farm, $factory, $factoryHT, $mountain) =
    (
        $island->{'pop'},
        $island->{'farm'} *10,
        $island->{'factory'}*10,
        $island->{'factoryHT'}*10,
        $island->{'mountain'} * 10
    );
    my ($tpop);

    # �Ż�����ǧ
    $unemployed = 0;
    $work_farm = 0;
    $work_biz = 0;
    $work_bizHT = 0;

    if ($pop > $farm) {
        # ���Ȥ�������꤬;����
        if ( $farm > 0 ){
            $work_farm = int( ($pop /$farm) * 100 );
            $work_farm = 100 if($work_farm > 100);
        }
        $tpop = ($pop - $farm);

        if ( $factory + $mountain > 0 ) {
            $work_biz = int( ($tpop / ($factory + $mountain) )* 100 );
            $work_biz = 100 if($work_biz > 100);
        }
        $tpop = ($tpop - ($factory + $mountain));

        if (($factoryHT > 0) && ($tpop > 0) ) {
            $work_bizHT = int( ($tpop / ($factoryHT) )* 100 );
            $work_bizHT = 100 if($work_bizHT > 100);
        }

        $unemployed = $tpop - ($factoryHT) ;
        $unemployed = 0  if($unemployed < 0);

    } else {
        # ���Ȥ����Ǽ���դξ��
        if ($farm) {
            $work_farm = int( ($pop /$farm)*100);
        }else{
            $work_farm = 0;
        }
    }
    $unemployed_str = "$unemployed$HunitPop";
    if (!$unemployed ){
        $unemployed_str = '0��';
    }

    out(<<END);
<div id='extInfo'>
  <table border="0">
    <tr>
      <td>
        <table border>
          <tr>
            $aStr1
            <th $HbgTitleCell align=center>${HtagTH_}�ɷ���${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}�߷���${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}̱�߽�${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}������${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}��ȯ��${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}���ɸ�${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}�༣��${H_tagTH}</th>
          </tr>
          <tr>
            $aStr2
            <TD $HbgInfoCell align=center>$data[2]</td>
            <TD $HbgInfoCell align=center>$data[3]</td>
            <TD $HbgInfoCell align=center>$data[4]</td>
            <TD $HbgInfoCell align=center>$data[5]</td>
            <TD $HbgInfoCell align=center>$data[6]</td>
            <TD $HbgInfoCell align=center>$data[7]</td>
            <TD $HbgInfoCell align=center>$monsterkill</td>
          </tr>
        </table>
      </td>
END
    if ($island->{'stadiumnum'} > 0) {
        my ($shoritu);
        $shoritu = '-';
        if ( ($stwint + $stloset) ) {
            $shoritu = int(($stwint / ($stwint + $stloset)) * 100 );
        }
    out(<<END);
      <td>
        <table border>
          <tr>
            <th $HbgTitleCell align=center>${HtagTH_}����${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}��${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}��${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}KP${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}����${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}���${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}�̻�(��Ψ)${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}ͥ��${H_tagTH}</th>
          </TR>
          <TR>
            <TD $HbgInfoCell align=center>$nn</td>
            <TD $HbgInfoCell align=center>$sto</td>
            <TD $HbgInfoCell align=center>$std</td>
            <TD $HbgInfoCell align=center>$stk</td>
            <TD $HbgInfoCell align=center>$kachiten</td>
            <TD $HbgInfoCell align=center>$stwin��$stlose��$stdrowʬ</td>
            <TD $HbgInfoCell align=center>$stwint��$stloset��$stdrowtʬ($shoritu%)</td>
            <TD $HbgInfoCell align=center>$styusho��</td>
          </TR>
        </table>
        </td>
      </tr>
END
    }

    if ($HmainMode eq 'owner') {
    out(<<END);
<tr>
<td>
<table border>
  <tr>
    <th $HbgTitleCell align=center>${HtagTH_}����<br>��ƯΨ${H_tagTH}</th>
    <th $HbgTitleCell align=center>${HtagTH_}�ӥ��ͥ�<br>��ƯΨ${H_tagTH}</th>
    <th $HbgTitleCell align=center>${HtagTH_}HT����<br>��ƯΨ${H_tagTH}</th>
    <th $HbgTitleCell align=center>${HtagTH_}���ȼ�${H_tagTH}</th>
  </tr>
  <tr>
    <td $HbgInfoCell align=center>$work_farm%</td>
    <td $HbgInfoCell align=center>$work_biz%</td>
    <td $HbgInfoCell align=center>$work_bizHT%</td>
    <td $HbgInfoCell align=center>$unemployed_str</td>
  </tr>
</table>
</td>
END
    }

    my ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
    my ($mspet , $petname);
    $mspet = "<img src=\"${HMapImgDir}monster30.gif\" TITLE=\"�ޥ����åȤ��Τ�(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswinɤ����/�и���$msexe)\" onMouseOver='status=\"�ޥ����åȤ��Τ�(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswinɤ����/�и���$msexe)\"; return true;' onMouseOut=\"status = '';\" WIDTH=32 HEIGHT=\"32\">" if($mshp);
    $mspet = "<img src=\"${HMapImgDir}tet.gif\" TITLE=\"Ķ���åƥȥ�(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswinɤ����/�и���$msexe)\" onMouseOver='status=\"Ķ���åƥȥ�(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswinɤ����/�и���$msexe)\"; return true;' onMouseOut=\"status = '';\" WIDTH=32 HEIGHT=\"32\">" if($tet);

    $petname = '�ޥ����åȤ��Τ�' if ($mshp);
    $petname = 'Ķ���åƥȥ�' if ($tet);
    $mspet = '' if (!$mshp && !$tet);

    if ($mshp || $tet) {

    out(<<END);
<td>
<table border="1">
<tr>
<th $HbgTitleCell align="center" rowspan="7">${HtagTH_}$petname ${H_tagTH}</th>
</tr>
<tr>
<th $HbgTitleCell align=center rowspan="2">${HtagTH_}$mspet${H_tagTH}</th>
<th $HbgTitleCell align=center>${HtagTH_}HP${H_tagTH}</th>
<th $HbgTitleCell align=center>${HtagTH_}AP${H_tagTH}</th>
<th $HbgTitleCell align=center>${HtagTH_}DP${H_tagTH}</th>
<th $HbgTitleCell align=center>${HtagTH_}SP${H_tagTH}</th>
<th $HbgTitleCell align=center>${HtagTH_}����${H_tagTH}</th>
<th $HbgTitleCell align=center>${HtagTH_}�и���${H_tagTH}</th>
</tr>
<tr>
<th $HbgInfoCell align=center>$mshp</th>
<th $HbgInfoCell align=center>$msap</th>
<th $HbgInfoCell align=center>$msdp</th>
<th $HbgInfoCell align=center>$mssp</th>
<th $HbgInfoCell align=center>$mswin</th>
<th $HbgInfoCell align=center>$msexe</th>
</tr>
</table>
</td>
END

    }
    my ($ownmode) = 0;
    $ownmode = 1 if ($HmainMode eq 'owner');
    out(<<END);
</tr>
</table>
</div>

END
    if ($HmainMode eq 'owner') {

        out("<hr>");
        out("<b><a href=JavaScript:void(0); onClick='show_taijilist($island->{'id'},$ownmode)'>���ä�����</a></b> / ");
        out("<b><a href=JavaScript:void(0); onClick='show_Productlist($island->{'id'},$ownmode)'>ʪ��(��)</a></b> / ");

        TradeButton($island);
    }

}


#----------------------------------------------------------------------
#
#
sub TradeButton {
    my ($island) = @_;

    unless ($island->{'predelete'}) {
        out(<<END);
        <form action="${HthisFile}" method="post">
          <input type="hidden" name="PASSWORD" value="$HdefaultPassword">
          <input type="submit" value="�������(��)" name="Trade=$HcurrentID">
        </form>
END
    }
}


#----------------------------------------------------------------------
# �Ͽޤ�ɽ��
#----------------------------------------------------------------------
# $mode��1�ʤ顢�ߥ�����������򤽤Τޤ�ɽ��
# $jsmode��1�ʤ顢JS�⡼��
sub islandMap {
    my ($mode, $jsmode) = @_;

    my ($island) = $Hislands[$HcurrentNumber];

    out(<<END);
<div id='islandMap'>
  <table border>
    <tr>
      <td>
END
    # �Ϸ����Ϸ��ͤ����
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($l, $lv);

    my ($pts) = ($island->{'pts'}) ? $island->{'pts'} : 0;

    local ($hlv);

    $hlv = Calc_HouseLevel($pts);

    local ($onm) = $island->{'onm'};
    my ($shutomessage) = $island->{'shutomessage'};
    my ($eis1) = $island->{'eis1'};
    my ($area) = $island->{'area'};
    my ($pop) = $island->{'pop'};
    my ($mikomi) = int($pop * 3 * 11 / 500);
    local ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
    local ($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $island->{'eisei4'});
    local $kachiten = $stwin*3 + $stdrow;
    local $nn = ('������', 'ͽ���裱���Ԥ�', 'ͽ���裲���Ԥ�', 'ͽ���裳���Ԥ�', 'ͽ���裴���Ԥ�', 'ͽ����λ�Ԥ�',    '�ࡹ�辡���Ԥ�', '��辡���Ԥ�', '�辡���Ԥ�',
            'ͥ����', '������', 'ͽ�����', '�ࡹ�辡�餱', '��辡�餱', '�裲��')[$stshoka];
    $nn = '������' if($nn eq '');


    if ( ($mode == 0) && ($island->{'effect'} & 1) ) {
        out('<div align=center>���Ⱦ㳲��ȯ�����Ƥ��ޤ���</div>');
    }

    # ���ޥ�ɼ���
    my ($com, @comStr, $i);
    if ($HmainMode eq 'owner') {
        my ($j , $cKind);
        my ($command) = $island->{'command'};
        for ($i = 0; $i < $HcommandMax; $i++) {
            $j = $i + 1;
            $com = $command->[$i];
            $cKind = $com->{'kind'};
            if (   ($cKind < 31)
                || ((70 <= $cKind) && ($cKind <= 79))
                || ((100 <= $cKind) && ($cKind <= $HcomMax))) {
                $comStr[$com->{'x'}][$com->{'y'}] .= " [${j}]$HcomName[$com->{'kind'}]";
            }
        }
    }

    #�ҥ�ȥѥͥ�
    out("<div id='NaviView'></div>");
    out("<div class='map_cur' id='map_cur'></div>") if(($jsmode) && ($mode));
    out('<center><textarea style="resize:none;" cols="70" rows="3" id="HINT_PANEL">hint</textarea></center>') if((!$jsmode) && ($mode));
    # ��ɸ(��)�����
    # out("<nobr>");

    foreach $y (0..$islandSize) {
        out("<img src=\"img/space.png\" width=$Hms1 alt='' height=${Hms2}><img src=\"img/space${y}.gif\" alt='' width=$Hms1 height=${Hms2}>");
    }
    out("<img src=\"img/space.png\" width=$Hms1 alt='' height=${Hms2}><BR>\n");

    # ���Ϸ�����Ӳ��Ԥ����
    my ($x, $y);
    my ($xx, $yy);
    my ($ir);

    my ($shuffle) = 0;

    if ( ($island->{'effect'} & 1) && ($mode == 0) ) {
        makeRandomPointArray();
        $shuffle = 1;
    }

    my ($id) = $island->{'id'};
    my ($shrturn) = $island->{'shrturn'};

    foreach $y (0..$islandSize) {
        # �������ܤʤ��ֹ�����
        out("<img src=\"img/space${y}.gif\" width='$Hms1' height='${Hms2}' alt=''>") if(!($y % 2));

        # ���Ϸ������
        foreach $x (0..$islandSize) {

            if ($shuffle) {

                $ir = $y * ISLAND_SIZE + $x;
                $xx = $Hrpx[$ir];
                $yy = $Hrpy[$ir];
            }
            else {

                $xx = $x;
                $yy = $y;
            }

            landString2($island, $xx, $yy, $mode, $comStr[$xx][$yy], $jsmode ,0);
            #landString($island, $land->[$xx][$yy], $landValue->[$xx][$yy],$landValue2->[$xx][$yy], $x, $y, $mode, $comStr[$xx][$yy], $jsmode ,0);
        }

        # ������ܤʤ��ֹ�����
        out("<img src=\"img/space${y}.gif\" width='$Hms1' height='${Hms2}' alt=''>") if ($y % 2);

        # ���Ԥ����
        out("<br>\n");
    }
    out("</td></tr></table></div>\n");
}



#----------------------------------------------------------------------
sub MapCommonScript {

    my($island) = $Hislands[$HcurrentNumber];

    out(<<END);
<SCRIPT type="text/javascript">
<!--
function boxslct(x) {
  window.document.myForm.AMOUNT.options[x].selected = true;
  return true;
}

END

    out(<<END) if ($island->{'monsterlive'});       #���ä��ʤ��ʤ顢ɽ�����ʤ�
MONSTER0 = "��¤����";
MONSTER1 = "";
MONSTER2 = "�����������ϹŲ�";
MONSTER3 = "���ߥ�����̵����(10%)";
MONSTER4 = "������2���ư����";
MONSTER5 = "�����粿���ư���뤫����";
MONSTER6 = "������������ϹŲ�";
MONSTER7 = "";
MONSTER8 = "���峤�����߽Ф�<br>������2���ư����";
MONSTER9 = "��������Ų�";
MONSTER10 = "���ߥ�����̵����(10%)";
MONSTER11 = "����ư��������90%��ʬ��";
MONSTER12 = "�����粿���ư���뤫����";
MONSTER13 = "������,�ߥ�����̵����(90%)<br>���׷��ȤǼ���2hex����<br>����ʡ(???)";
MONSTER14 = "���ߥ�����ۼ�(10%)<br>��������Ų�<br>������1hex�˥��饤��ʬ��";
MONSTER15 = "���ߥ�����̵����(10%)<br>��������Ų�<br>��������Ƥ�";
MONSTER16 = "���ߥ�����̵����(50%)<br>���׷��ȤǼ���1hex����<br>������";
MONSTER17 = "���޷�ߥ�����ȯ��(40��90%)<br>���ߥ�����ȯ��(60%)<br>��¿��Ƭ�ߥ�����ȯ��(40%)<br>�����ȥߥå����ܥ�ȯ��(20%)<br>�����粿���ư���뤫����";
MONSTER18 = "���ߥ�����̵����(10%��)<br>�����(60%)<br>����Ƥ���(60%)<br>���׷��ȤǼ���2hex����";
MONSTER19 = "����ƥ�,��������<br>���ɥ쥤��,����<br>��¾����ˤ�ƶ����ޤ�";
MONSTER20 = "���ߥ�����̵����(30%)<br>������(20%)<br>����ߥåȲ��(HP>13)<br>����������(������+2)<br>���׷��ȤǼ���1hex����";
MONSTER21 = "���ߥ�����̵����(20%)<br>���網��(15%),����(20%)<br>������(50%)<br>����������(������+3)";
MONSTER22 = "���ߥ�����̵����(25%)<br>�����������ȡ���(����1hex)<br>�����������륢��(����,�ߥ��������,�ɱһ���,����,����)";
MONSTER23 = "����500��100000���ߤ����Ǥ�����";
MONSTER24 = "����5000��1000000���ߤ����Ǥ�����<br>��500000��50000000�ȥ��������Ǥ�����";
MONSTER25 = "������2���פ���";
MONSTER26 = "���ۤ�����ˤ��פ���";
MONSTER27 = "�����Τ����֤�";
MONSTER28 = "������Ф�ڥåȲ���";
MONSTER29 = "��¾�β��ä򹶷�<br>���ڥå�����";
MONSTER30 = "�����٤˵�����Ϥ��ˤ����٤˳��ä��Ƥ���ƥȥ�";
MONSTER31 = "���Ѹ��Ҥ����Ͽޤ�������ɽ������ʤ��ʤ롣";
MONSTER32 = "���ۤ�ή�������Ӥ���ζ�����������ͦ�ޤ�������<br>��ˤ���ä��ꡢ�������ळ�Ȥ����롣";
MONSTER33 = "���ߥ�����̵����(50%)";
MONSTER34 = "���ߥ�����̵����(10%)��<br>���ä�����ȡ����Ȥ���μ������ʤ��ʤ롿<br>���ȿ���ӡ��������";
MONSTER35 = "�����Ф�Ƥ������";
MONSTER36 = "";
MONSTER37 = "�ۤ�����ˤ��פ��롣�Ԥ�������Ϥ�򴹤��롣";
END

    out(<<END);
SHIP0  = "[�ݻ���] 5${HunitMoney}<br>[����] �西����290${HunitFood}��320${HunitFood}";
SHIP1  = "[�ݻ���] 5${HunitMoney}<br>[����] �西����290${HunitFood}��320${HunitFood}";
SHIP2  = "[�ݻ���] 20${HunitMoney}<br>[����] �西����490${HunitFood}��530${HunitFood}";
SHIP3  = "[�ݻ���] 300${HunitMoney}<br>[ȯ����Ψ] ����(2%)<br>������(0.5%:Max50000${HunitMoney})";
SHIP4  = "[�ݻ�����] 1000${HunitFood}<br>[����] �西����150${HunitMoney}��400${HunitMoney}";
SHIP5  = "[�ݻ���] 60${HunitMoney}<br>[����] �西����690${HunitFood}��730${HunitFood}";
SHIP6  = "[�ݻ���] 30${HunitMoney}/1hex��ư<br>[����] �西����490${HunitFood}��530${HunitFood}/1hex��ư";
SHIP7  = "[�ݻ���] 500${HunitMoney}<br>[ȯ����Ψ] ����(4%)<br>������(1%:Max100500${HunitMoney})";
SHIP8  = "[�ݻ�����] 3000${HunitFood}<br>[����] �西����(1500 + �͸�/1000)${HunitMoney}<br>[ɹ�����ͳ�Ψ] 10%";
SHIP9  = "[�ݻ���] 100${HunitMoney}<br>[���ä��ư����] SPP�ߥ�����100${HunitMoney}/1ȯ";
SHIP10 = "[�ݻ���] 400${HunitMoney}<br>[���ä�ֻ�] ¿��Ƭ�ߥ�����3000${HunitMoney}/1ȯ";
SHIP11 = "[�ݻ���] 60${HunitMoney}/1hex��ư<br>[����] �西�����西����690${HunitFood}��730${HunitFood}/1hex��ư";
SHIP19 = "[�ݻ���] 1000${HunitMoney}<br>[���ä�ֻ�] ���ͥ륮��ˤ50000${HunitMoney}/1ȯ";

var miniTaiji;
function show_taijilist(url,mode) {
  if (url != "" ) {
    window.self.name = "trap";
    if (   (miniTaiji == null)
        || (miniTaiji.closed) ) {
      miniTaiji = window.open("$HthisFile?TaijiList=" +url , "taiji", "menubar=1,toolbar=0,location=0,directories=0,status=0,scrollbars=1,resizable=1,width=700,height=630");
    }else{
      miniTaiji.location.href = "$HthisFile?TaijiList=" +url;
      miniTaiji.focus();
    }
  }
}

var miniProduct;
function show_Productlist(url,mode) {
  if (url != "" ) {
    window.self.name = "trap";
    if (   (miniProduct == null)
        || (miniProduct.closed) ) {
      miniProduct = window.open("$HthisFile?Product=" +url , "taiji", "menubar=1,toolbar=0,location=0,directories=0,status=0,scrollbars=1,resizable=1,width=700,height=630");
    }else{
      miniProduct.location.href = "$HthisFile?Product=" +url;
      miniProduct.focus();
    }
  }
}

function Navi(x, y, img, title, text, exp) {
  StyElm = document.getElementById("NaviView");

  StyElm.style.width = 250;
  if(x + 1 > $HislandSize / 2) {
    // ��¦
    StyElm.style.marginLeft = (x - 5) * 32 - 10;
  } else {
    // ��¦
    StyElm.style.marginLeft = (x + 1) * 32;
  }
  StyElm.style.marginTop = (y) * 32 - 32 + 120; // y �ϸ���

  StyElm.innerHTML = "<img src='./img/noitem.gif' alt='' width=16 height=16 onClick='NaviClose();'><div class='NaviTitle'  style='font-size: 80%;'>" + title + " (" + x + "," + y + ")<\\/div><table><tr><td class='M'><img alt='' class='NaviImg' src=" + img + "><\\/td><td class='M'><div class='NaviText' style='font-size: 80%;'>" + text + "<\\/div>";
  if(exp) {
    StyElm.innerHTML += "<div class='NaviText' style='font-size: 80%;'>" + eval(exp) + "<\\/div>";
  }
  StyElm.innerHTML += "<\\/td><\\/tr><\\/table>";
  StyElm.style.visibility = "visible";
}

function NaviClose() {
  StyElm = document.getElementById("NaviView");
  StyElm.style.visibility = "hidden";
}

function ps(x, y) {
  if(opener) {
    window.opener.document.lcForm.POINTX.options[x].selected = true;
    window.opener.document.lcForm.POINTY.options[y].selected = true;
    return 1;
  }
}
//-->
</SCRIPT>
END
}


1;
