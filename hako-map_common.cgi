#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# 地図モードモジュール(ver1.00)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# Hakoniwa R.A. ver2.11
# メインスクリプト(箱庭諸島 ver2.30)
# 使用条件、使用方法等は、read-renas.txtファイルを参照
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------
# ＪＡＶＡスクリプト版 -ver1.11-
# 使用条件、使用方法等は、配布元でご確認下さい。
# 付属のjs-readme.txtもお読み下さい。
# あっぽー：http://appoh.execweb.cx/hakoniwa/
#----------------------------------------------------------------------
# マップ処理の共通部分を抜き出す。

#----------------------------------------------------------------------
# static
# マップ関数の初期化
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
# ○○島開発計画
#----------------------------------------------------------------------
sub OwnarMap_Header {
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];

    out(<<END);
<div align="center">
<h2>${HtagName_}${HcurrentName}${H_tagName}開発計画</h2>
$HtempBack<br>
</div>
END

}

#----------------------------------------------------------------------
# 数量をprint
sub command_arg {

    my ($out) = '';
    # 数量 2ですすめてなんとか小さくする。
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
# 島の地図
#----------------------------------------------------------------------

# 情報の表示
sub islandInfo {
    my ($mode) = @_;

    my ($island) = $Hislands[$HcurrentNumber];
    # 情報表示
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
    $civreq = ($island->{'civreq'}) ? $island->{'civreq'} : "なし";
    $renae = (int($rena / 10 ));
    $unemployed = ($island->{'pop'} - ($farm + $factory + $HTfactor + $mountain) * 10) / $island->{'pop'} * 100 if($island->{'pop'});
    $unemployed = '<span class="' . ($unemployed < 0 ? 'unemploy1' : 'unemploy2') . '">' . sprintf("%.2f%%", $unemployed) . '</span>' if($island->{'pop'});
    $farm = ($farm == 0) ? "保有せず" : "${farm}0$HunitPop";
    $factory = ($factory == 0) ? "保有せず" : "${factory}0$HunitPop";
    $HTfactor = ($HTfactor == 0) ? "保有せず" : "${HTfactor}0$HunitPop";
    $mountain = ($mountain == 0) ? "保有せず" : "${mountain}0$HunitPop";
    #$pts = ($pts == 0) ? "0pts." : "${pts}pts.";

    my ($col_num) = 12;

    my ($mStr1) = '';
    my ($mStr2) = '';
    if (   (INIT_HIDE_MONEY_MODE == 1)
        || ($HmainMode eq 'owner')
        || ($island->{'id'} > 100)) {

        # 無条件またはownerモードまたはBattleField
        $mStr1 = "<th $HbgTitleCell>${HtagTH_}資金${H_tagTH}</th>";
        $mStr2 = "<td $HbgInfoCell align=right>$island->{'money'}$HunitMoney</td>";
        $col_num++;         # テーブルの長さ＋
    }
    elsif (   (INIT_HIDE_MONEY_MODE == 2)
           || (INIT_HIDE_MONEY_MODE == 3)) {

        my ($mTmp) = aboutMoney($island->{'money'});

        # 1000億単位モード
        $mStr1 = "<th $HbgTitleCell>${HtagTH_}資金${H_tagTH}</th>";
        $mStr2 = "<td $HbgInfoCell align='right'>$mTmp</td>";
        $col_num++;         # テーブルの長さ＋
    }

    my ($bStr, $rStr1, $rStr2, $uStr1, $uStr2, $msStr1, $msStr2) = ('', '', '', '', '', '', '');

    if (($island->{'id'} <= 100) && !($island->{'BF_Flag'})) {
        # 総合ポイントと順位
        $rStr1 = "<th $HbgTitleCell>${HtagTH_}順位${H_tagTH}</th><th $HbgTitleCell>${HtagTH_}<small>総合Point</small>${H_tagTH}</th>";
        $rStr2 = "<td $HbgNumberCell rowspan='2' align='center'>${HtagNumber_}$rank${H_tagNumber}</td><td $HbgPoinCell align=right>${pts}</td>";
        # 失業率
        $uStr1 = "<th $HbgTitleCell>${HtagTH_}失業率${H_tagTH}</th>";
        $uStr2 = "<td $HbgInfoCell align='right'>${unemployed}</td>";
        $col_num = $col_num + 2;             # テーブルの長さ＋
        # 発射可能ミサイル数(保有数)
        if (INIT_HIDE_MISSILE_MODE || ($HmainMode eq 'owner')) {

            # 無条件またはownerモード
            $msStr1 = "<th $HbgTitleCell>${HtagTH_}ミサイル数";
            $msStr2 = "<td $HbgInfoCell align=right>$island->{'missiles'}${HunitMissile}";
            $col_num++;         # テーブルの長さ＋

            if (INIT_HIDE_MISSILE_MODE == 2) {

                my ($mTmp) = aboutMissile($island->{'missiles'});
                # 10発単位モード
                $msStr1 = "<th $HbgTitleCell>${HtagTH_}ミサイル数${H_tagTH}</th>";
                $msStr2 = "<td $HbgInfoCell align='right'>${mTmp}</td>";
            }
            elsif (INIT_USE_ARM_SUPPLY) {

                $msStr1 .= "(軍事物資)${H_tagTH}</th>";
                $msStr2 .= "($island->{'army'}個)</td>";
            }
            else {
                $msStr1 .= "${H_tagTH}</th>";
                $msStr2 .= "</td>";
            }
        }
    } else {
        $bStr = "<tr><th colspan='13'><font size='5'>${HtagTH_}Battle Field${H_tagTH}</font></th></tr>";
        $col_num ++;         # テーブルの長さ＋
    }

    my ($prize);
    $prize = '';

    # ターン杯、その他賞
    $prize = ScoreBoard_Prize($island);

    # 倒した怪獣リスト  怪獣を増やすので、リストは削除
    $prize .= ScoreBoard_Taiji($island);

    # 部門賞
    my $bumons = ScoreBoard_Bumon($island);

    my ($monslive);
    $monslive = ScoreBoard_LiveMonster($island);

    # 人工衛星
    $me_sat = ScoreBoard_Eisei($island);

    # 牧場系
    my($Farmcpc) = ScoreBoard_Farm($island);

    # 家
    my ($house) = '';
    my ($hlv);
    my ($tax) = $island->{'eisei1'};
    $hlv = Calc_HouseLevel($island->{'pts'});
    my $onm = $island->{'onm'};
    my $n = ('の小屋', 'の簡易住宅', 'の住宅', 'の高級住宅', 'の豪邸', 'の大豪邸', 'の高級豪邸', 'の城', 'の巨城', 'の黄金城')[$hlv];
    my $zeikin = int($island->{'pop'} * ($hlv + 1) * $tax / 100);

    if ($tax) {
        $house  = "<span class='house'>";
        $house .= "<img src=\"./img/land/house${hlv}.gif\" alt=\"$onm$n\" class='landinfoIcon'>税率$tax％($zeikin$HunitMoney)" ;
        $house .= '</span>';
    }

    my ($weather);
    my ($w_tag);
    my ($wn_tag);
    $weather    = $island->{'weather_old'};
    $w_tag      = "<img src='./img/weather/weather$weather.gif' TITLE='連続：$island->{'weather_chain'}日'>";
    $weather    = $island->{'weather'};
    $wn_tag      = "<img src='./img/weather/weather$weather.gif'>";

    my ($areatag);

    $areatag = (!$island->{'area'}) ? '0坪' : "$island->{'area'}$HunitArea";


    out(<<END);
<div id='islandInfo' align="center">
<table border>
$bStr
<tr>
$rStr1
<th $HbgTitleCell>${HtagTH_}天候${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}<small>次ターン<br>天候予想</small>${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}気温${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}人口${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}面積${H_tagTH}</th>
$mStr1
<th $HbgTitleCell>${HtagTH_}食料${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}農場${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}職場${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}HT職場${H_tagTH}</th>
<th $HbgTitleCell>${HtagTH_}採掘場${H_tagTH}</th>
$uStr1
<th $HbgTitleCell>${HtagTH_}軍事<br>技術${H_tagTH}</th>
$msStr1
<th $HbgTitleCell>${HtagTH_}要望/数値${H_tagTH}</th>
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
<TD $HbgCommentCell COLSPAN=${col_num} align=left>${HtagtTH_}info：<font size="-1">$prize$house$monslive$Farmcpc$bumons$me_sat</font>${H_tagtTH}
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
            $allyName =~ s/【勝者！】//g;
            $aNo += $i;
            my $campInfo = '';
            $campInfo = "<FORM name='allyForm$aNo' action='${HthisFile}' method='POST' target='_blank' style='margin-bottom: 0px;'>" if ($mode);
            $campInfo .=<<_CAMP_ if($mode && $HarmisticeTurn);
　[<A STYlE="text-decoration:none" HREF="JavaScript:void(0)" onClick="document.allyForm${aNo}.submit();return false;">作戦本部</A>]
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
[<a style="text-decoration:none" href="JavaScript:void(0)" onClick="document.allyForm${aNo}.action='${HbaseDir}/${HallyBbsScript}';document.allyForm${aNo}.submit();return false;">作戦会議室</a>]
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

    my ($allytitle) = $HarmisticeTurn ? '陣営' : '同盟';
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


# アイテムの表示
sub islandItemData {
    print("<div id=itembox>");

    out(<<END);
  <table border>
    <tr>
      <th $HbgTitleCell align="center" rowspan="2">${HtagTH_}持ち物${H_tagTH}</th>
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
        # 各地形を出力
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

        # 大学
        my($p, $n);
        if($lv == 0) {
            $p = '34';
            $n = '農業大学';
        } elsif($lv == 1) {
            $p = '35';
            $n = '工業大学';
        } elsif($lv == 2) {
            $p = '36';
            $n = '総合大学';
        } elsif($lv == 3) {
            $p = '37';
            $n = '軍事大学';
        } elsif($lv == 4) {
            $p = '44';
            $n = "生物大学 (待機)$rt HP:$mshp AP:$msap DP:$msdp SP:${mssp}$rt $mswin匹撃破 / 経験値$msexe";
        } elsif($lv == 96) {
            $p = '44';
            $p = '44x' if($mode == 1);
            $n = "生物大学 (出禁)$rt HP:$mshp AP:$msap DP:$msdp SP:${mssp}$rt $mswin匹撃破 / 経験値$msexe";
        } elsif($lv == 98) {
            $p = '48';
            $n = "生物大学 (待機)$rt HP:$mshp AP:$msap DP:$msdp SP:${mssp}$rt $mswin匹撃破 / 経験値$msexe";
        } elsif($lv == 97) {
            $p = '48';
            $p = '48x' if($mode == 1);
            $n = "生物大学 (出禁)$rt HP:$mshp AP:$msap DP:$msdp SP:${mssp}$rt $mswin匹撃破 / 経験値$msexe";
        } elsif($lv == 99) {
            $p = '47';
            $n = '生物大学 (出動中)';
        } else {
            $p = '46';
            $n = '気象大学';
        }

        $image = "land${p}.gif";
        $alt = "$n";

        $naviTitle = (split(' ',$n))[0];

        if ($lv2 > 0) {
            $naviText = "復興中($lv2)";
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
        $alt = 'なし';
        $naviTitle  = 'なし';

    }else{
        if($lv) {
            # 浅瀬
            $image = 'land14.gif';
            $alt = '海(浅瀬)';
            $naviTitle  = '浅瀬';
        } else {
            # 海
            $image = Sea_Img_Gen(1, $x, $y);
            $alt = '海';
            $naviTitle  = '海';
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

        # 町
        my($p, $n);
        if($lv < 30) {
            $p = 'land3.png';
            $n = '村';
        } elsif($lv < 65) {
            $p = 'land4.png';
            $n = '町';
        } elsif($lv < 100) {
            $p = 'land402.png';
            $n = '町';
        } elsif($lv < 150) {
            $p = 'land5.png';
            $n = '都市';
        } elsif($lv < 200) {
            $p = 'land501.png';
            $n = '都市';
        } else {
            $p = 'land502.png';
            $n = '大都市';
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

    # 荒地
    $alt = '荒地';
    $naviTitle  = '荒地';
    $naviText  = '';

    if($lv == 1) {
        $image = 'land13.gif';  # 着弾点
    } elsif($lv  == 2) {
        $image = 'land13m.gif'; # 隕石
    } elsif($lv  == 3) {
        $image = 'iwaba.gif';   # 岩場
        $alt = '岩場';
        $naviTitle  = '岩場';
    } elsif($lv  == 4) {
        $image = 'wastetown.png'; # 隕石
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

    # 山
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
        $alt = "山(採掘場${lv}0${HunitPop}規模)";
        $naviText  = "採掘場${lv}0${HunitPop}規模";
    } else {
        $image = 'land11.gif';
        $alt = '山';
    }
    $naviTitle  = '山';

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
    $alt = "海都市(${lv}$HunitPop/職場${mwork}0$HunitPop/HT職場${hwork}0$HunitPop)";
    $naviText  = "${lv}$HunitPop&lt;br&gt;職場${mwork}0$HunitPop&lt;br&gt;HT職場${hwork}0$HunitPop";
    $naviTitle  = '海都市';

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

    # 平地
    if (!$lv) {
        $image = 'land2.gif';
        $alt = '平地';
        $naviTitle  = '平地';
    } else {
        $image = 'yotei.png';
        $alt = '予定地';
        $naviTitle  = '予定地';
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
        # 農場
        if ($lv2 == 1){
            $image = 'kaju.gif';
            $alt = "果樹園(${lv}0${HunitPop}規模)";
            $naviTitle  = '果樹園';

        } elsif($lv2 == 2) {
            $image = 'sio.gif';
            $alt = "塩田(${lv}0${HunitPop}規模)";
            $naviTitle  = '塩田';

        }else{
            if($lv < 25) {
                $image = 'farm1.png';
            } elsif($lv < 50) {
                $image = 'farm2.png';
            } else{
                $image = 'farm3.png';
            }
            $alt = "農場(${lv}0${HunitPop}規模)";
            $naviTitle  = '農場';
        }
        $naviText  = "${lv}0${HunitPop}規模";

    } elsif($l == $HlandNewtown) {
        # ニュータウン
        my $nwork =  int($lv/15);
        if ($lv < 100){
            $image = 'new1.png';
        }else{
            $image = 'new2.png';
        }
        if ($nwork > 0) {
            $alt = "ニュータウン(${lv}$HunitPop/職場${nwork}0$HunitPop)";
            $naviText  = "${lv}$HunitPop&lt;br&gt;職場${nwork}0$HunitPop";
        }else{
            $alt = "ニュータウン(${lv}$HunitPop)";
            $naviText  = "${lv}$HunitPop";
        }
        $naviTitle  = 'ニュータウン';

    } elsif($l == $HlandProcity) {
        # 町
        my ($c) = '防災都市ランク';
        if ($lv < 110) {
            $c .= 'Ｅ';
        } elsif($lv < 130) {
            $c .= 'Ｄ';
        } elsif($lv < 160) {
            $c .= 'Ｃ';
        } elsif($lv < 200) {
            $c .= 'Ｂ';
        } else {
            $c .= 'Ａ';
        }

        $image = "land26.gif";
        $alt = "$c(${lv}$HunitPop)";
        $naviTitle  = $c;
        $naviText  = "${lv}${HunitPop}";

    } elsif($l == $HlandForest) {
        # 森
        $image = Forest_Img_Gen();
        $alt = '森';
        # 観光者の場合は木の本数隠す
        $alt .= "(${lv}$HunitTree)" if ($mode == 1);
        $naviTitle  = '森';
        $naviText = "(${lv}$HunitTree)" if ($mode == 1);

    } elsif($l == $HlandFactory) {
        # 工場
        if ($lv2 == 1) {
            $image = 'moku.png';
            $alt = "木工所(${lv}0${HunitPop}規模)";
            $naviTitle  = '木工所';
            $naviText  = "${lv}0${HunitPop}規模";

        }else{
            $image = 'land8.gif';
            $alt = "工場(${lv}0${HunitPop}規模)";
            $naviTitle  = '工場';
            $naviText  = "${lv}0${HunitPop}規模";
        }

    } elsif ($l == $HlandNursery) {
        # 養殖場
        $image = 'nursery.gif';
        $alt = "養殖場(${lv}0${HunitPop}規模)";
        $naviTitle  = '養殖場';
        $naviText  = "${lv}0${HunitPop}規模";

    } elsif ($l == $HlandKyujokai) {
        # 野球場
        $image = 'land23kai.gif';
        $alt = "多目的スタジアム$rt 選手$nn$rt 攻($sto)守($std)KP($stk)$rt チーム成績 勝点$kachiten / $stwin勝$stlose敗$stdrow分$rt / 通算$stwint勝$stloset敗$stdrowt分 / 優勝$styusho回)";
        $naviTitle  = '多目的スタジアム';
        $naviText  = "選手$nn&lt;br&gt; 攻($sto)守($std)KP($stk)&lt;br&gt; チーム成績 勝点$kachiten / $stwin勝$stlose敗$stdrow分<br> / 通算$stwint勝$stloset敗$stdrowt分 / 優勝$styusho回)";

    } elsif ($l == $HlandFoodim) {
        # 研究所
        my ($f);
        if ($lv < 480) {
            $f = '食物研究所';
            $image = "land25.gif";
        } else {
            $f = '防災型食物研究所';
            $image = "land25_bousai.png";
        }
        $alt = "$f(農場換算${lv}0${HunitPop}規模)";
        $naviTitle  = $f;
        $naviText  = "農場換算${lv}0${HunitPop}規模";

    } elsif ($l == $HlandFarmchi) {
        $works = $lv;
        $image = 'land31.gif';
        $alt = "養鶏場(${lv}万羽/生産力${works}$HunitFood)";
        $naviTitle  = '養鶏場';
        $naviText  = "${lv}万羽&lt;br&gt;生産力${works}$HunitFood";

    } elsif ($l == $HlandFarmpic) {
        $works = $lv*2;
        $image = 'land32.gif';
        $alt = "養豚場(${lv}万頭/生産力${works}$HunitFood)";
        $naviTitle  = '養豚場';
        $naviText  = "${lv}万頭&lt;br&gt;生産力${works}$HunitFood";

    } elsif ($l == $HlandFarmcow) {
        $works = $lv*3;
        $image = 'land33.gif';
        $alt = "牧場(${lv}万頭/生産力${works}$HunitFood)";
        $naviTitle  = '牧場';
        $naviText  = "${lv}万頭&lt;br&gt;生産力${works}$HunitFood";

    } elsif ($l == $HlandBase) {
        if ($mode == 1) {
            # ミサイル基地
            my($level) = expToLevel($l, $lv);
            $image = "missile${level}.png";
            $alt = "ミサイル基地 (レベル ${level}/経験値 $lv)";
            $naviText = "(Lv ${level}/経験値 $lv)";
            $naviTitle  = 'ミサイル基地';
        } else {
            # 観光者の場合は森のふり
            $image = Forest_Img_Gen();
            $alt = '森';
            $naviTitle  = '森';
        }

    } elsif ($l == $HlandSbase) {
        # 海底基地
        if($mode == 1) {
            my($level) = expToLevel($l, $lv);
            if ($level == 1) {
                $image = 'land12_1.gif';

            } elsif ($level == 2) {
                $image = 'land12_2.gif';

            }else{
                $image = 'land12.gif';
            }

            $alt = "海底基地 (レベル ${level}/経験値 $lv)";
            $naviText = "(Lv ${level}/経験値 $lv)";
            $naviTitle  = '海底基地';
        } else {
            # 観光者の場合は海のふり
            $image = Sea_Img_Gen($id, $x, $y);
            $alt = '海';
            $naviTitle  = '海';
        }

    } elsif ($l == $HlandSeacity) {
        # 海底都市
        if($mode == 1) {
            $image = 'land17.gif';
            $alt = "海底都市(${lv}$HunitPop)";
            $naviText = "海底都市(${lv}$HunitPop)";
            $naviTitle  = '海底都市';
        } else {
            # 観光者の場合は海のふり
            $image = Sea_Img_Gen($id, $x, $y);
            $alt = '海';
            $naviTitle  = '海';
        }

    } elsif ($l == $HlandHTFactory) {
        # ハイテク工場
        $image = 'land50.gif';
        $alt = "ハイテク多国籍企業(${lv}0${HunitPop}規模)";
        $naviTitle  = 'ハイテク多国籍企業';
        $naviText  = "${lv}0${HunitPop}規模";

    } elsif ($l == $HlandSHTF) {
        $image = 'land85.gif';
        $alt = "HT職場${lv}0${HunitPop}規模";
        $naviTitle = "ハイテク多国籍企業・改";
        $naviText = "${lv}0${HunitPop}規模";

    } elsif ($l == $HlandFiredept) {
        $image = 'firedept.gif';
        $alt = "消防署";
        $naviTitle = "消防署";

    } elsif ($l == $HlandFrocity) {
        # 海上都市
        if ($lv < 100) {
            $image = 'land39_mini.png';
        } elsif ($lv < 170) {
            $image = 'land39.gif';
        } else {
            $image = 'land39_up.gif';
        }
        $alt = "海上都市メガフロート(${lv}$HunitPop)";
        $naviTitle  = '海上都市メガフロート';
        $naviText  = "${lv}${HunitPop}";

    } elsif ($l == $HlandMinato) {
        # 港
        $image = 'land21.gif';
        $alt = "港町(${lv}$HunitPop)";
        $naviTitle  = '港町';
        $naviText  = "${lv}${HunitPop}";

    } elsif ($l == $HlandOnsen) {
        # 温泉
        $image = 'land40.gif';
        $alt = "温泉街(${lv}$HunitPop)";
        $naviTitle  = '温泉街';
        $naviText  = "${lv}${HunitPop}";

    } elsif ($l == $HlandSunahama) {
        # 砂浜
        $image = 'land38.gif';
        if ($lv > 0) {

            $alt = '砂丘';
            $naviTitle  = '砂丘';
        }else{

            $alt = '砂浜';
            $naviTitle  = '砂浜';
        }

    } elsif ($l == $HlandDefence) {
        # 防衛施設
        my ($deflv , $defHP) = GetDefenceSpec($lv);

        if ($deflv == 1) {
            $image = 'land10kai.gif';
            $alt = '防衛施設・改';
            $naviTitle  = '防衛施設・改';

        } elsif ($deflv == 2) {
            $image = 'land88.gif';
            $naviTitle  = "防衛施設・改+Lzr";
            if($mode == 1) {
                $alt = "防衛施設・改+Lzr(耐久：$defHP)";
                $naviText  = "耐久：$defHP";
            }else{
                $alt = "防衛施設・改+Lzr";
            }

        } elsif ($deflv == 0) {
            $image = 'land10.gif';
            $alt = '防衛施設';
            $naviTitle  = '防衛施設';

        } else {
            $image = 'land10.gif';
            $alt = "防衛施設";
            $naviTitle  = "防衛施設$lv";
        }

    } elsif($l == $HlandHaribote) {
        # ハリボテ
        $image = 'land10.gif';
        if ($mode == 1) {
            $alt = 'ハリボテ';
            $naviTitle  = 'ハリボテ';
        } else {
            # 観光者の場合は防衛施設のふり
            $alt = '防衛施設';
            $naviTitle  = '防衛施設';
        }

    } elsif ($l == $HlandTrain) {
        $image = "./train/Rail${lv}.gif";
        if ($lv & $Train_Exist) {
            $alt = '電車';
            $naviTitle  = '電車';
            $naviText  = "がたんごとん";
        }else{
            $alt = '線路';
            $naviTitle  = '線路';
        }

    } elsif($l == $HlandBeachPark) {
        $image = 'beach.png';
        $alt = "海水浴場(従業員${lv}0${HunitPop})";
        $naviTitle  = '海水浴場';
        $naviText  = "従業員${lv}0${HunitPop}";

    } elsif($l == $HlandIce) {
        if($lv > 0) {
            $image = 'land42.gif';
            $alt = "天然スケート場(従業員${lv}0${HunitPop})";
            $naviTitle  = '天然スケート場';
            $naviText  = "従業員${lv}0${HunitPop}";
        } else {
            $image = 'land41.gif';
            $alt = '氷河';
            $naviTitle  = '氷河';
        }

    } elsif($l == $HlandInaka) {
        # いなか
        $image = 'inaka.gif';
        $alt = 'いなか';
        $naviTitle  = 'いなか';
        my ($fm) = int($lv/10) + 1;
        $naviText  = "${lv}$HunitPop&lt;br&gt;農地：${fm}0${HunitPop}規模";

    } elsif($l == $HlandOil) {
        # 海底油田
        $image = 'land16.gif';
        $alt = '海底油田';
        $naviTitle  = '海底油田';

    } elsif($l == $HlandMonument) {
        # 記念碑
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
        # 怪獣
        my($kind, $name, $hp) = monsterSpec($lv);
        $image = $HmonsterImage[$kind];

        # 硬化中?
        if(isMonsterCuring($kind)) {
            # 硬化中
            $image = $HmonsterImage2[$kind];
        }
        $alt = "$name(体力${hp})";
        $naviTitle  = $name;
        $naviText  = "体力${hp}";
        $alt  = "$name(体力:？？)" if ( $kind == $Mons_Totten);
        $naviText  = "体力:？？" if ( $kind == $Mons_Totten);
        $naviExp = "\'MONSTER$kind\'";

        $map_style = 'maptile_ret' if(seqnum2(($HislandTurn+$y),($id+$x)) % 2);

    } elsif($l == $HlandPark) {
        # 遊園地
        $image = 'park.gif';
        $alt = "遊園地(従業員${lv}0${HunitPop}/収益見込${mikomi}$HunitMoney以上)";
        $naviTitle  = '遊園地';
        $naviText  = "従業員${lv}0${HunitPop}<br>収益見込${mikomi}$HunitMoney以上";


    } elsif($l == $HlandUmiamu) {
        # 海あみゅ
        $image = 'land24.gif';
        $alt = "海あみゅ(従業員${lv}0${HunitPop})";
        $naviTitle  = '海あみゅ';
        $naviText  = "従業員${lv}0${HunitPop}";

    } elsif($l == $HlandKatorikun) {
        # 香取君
        $image = 'katori.gif';
        $alt = '豚の香取くん';
        $naviTitle  = '豚の香取くん';

    } elsif($l == $HlandBigtown) {
        # 現代都市
        my $mwork =  int($lv/20);
        my $lwork =  int($lv/30);
        $image = 'land29.gif';
        $alt = "現代都市(${lv}$HunitPop/職場${mwork}0$HunitPop/農場${lwork}0$HunitPop)";
        $naviTitle  = '現代都市';
        $naviText  = "${lv}$HunitPop&lt;br&gt;職場${mwork}0$HunitPop&lt;br&gt;農場${lwork}0$HunitPop";

    } elsif($l == $HlandBettown) {
        # 輝ける都市
        if ( $lv >= 2000 ) {
            $image = 'bedtown2.gif';

        }else{
            $image = 'land45.png';

        }
        $alt = "輝ける都市(${lv}$HunitPop)";
        $naviTitle  = '輝ける都市';
        $naviText  = "${lv}$HunitPop";

    } elsif($l == $HlandRizort) {
        # リゾート地
        my ($rena) = $island->{'rena'};
        my ($eis1) = $island->{'eis1'};
        my ($eis2) = $island->{'eis2'};
        my ($eis3) = $island->{'eis3'};
        my ($eis5) = $island->{'eis5'};
        my ($fore) = $island->{'fore'};
        my ($monsterlive) = $island->{'monsterlive'};

        my ($rwork) = $lv + $eis1 + $eis2 + $eis3 + $eis5 + int($fore/10) + int($rena/10) - $monsterlive * 100;
        $image = 'land43.png';
        $alt = "リゾート地(滞在観光客${lv}$HunitPop/収益見込${rwork}$HunitMoney)";
        $naviTitle  = 'リゾート地';
        $naviText  = "滞在観光客${lv}$HunitPop&lt;br&gt;収益見込${rwork}$HunitMoney";

    } elsif($l == $HlandBigRizort) {
        # リゾート地
        $image = 'land49.gif';
        $alt = "臨海リゾートホテル(滞在観光客${lv}$HunitPop)";
        $naviTitle  = '臨海リゾートホテル';
        $naviText  = "滞在観光客${lv}$HunitPop";

    } elsif($l == $HlandRottenSea) {
        # 腐海
        $image = 'land20.gif';
        $alt = '腐海';
        $naviTitle  = '腐海';

    } elsif($l == $HlandOilCity) {
        # 油田都市
        my $mwork =  int($lv/40);
        $image = 'oilcity.gif';
        $alt = "油田都市(${lv}$HunitPop/職場${mwork}0$HunitPop)";
        $naviText  = "${lv}$HunitPop&lt;br&gt;職場${mwork}0$HunitPop";
        $naviTitle  = '油田都市';

    } elsif($l == $HlandRocket) {
        # ロケット
        $image = 'monument27.gif';
        $naviTitle  = 'ロケット';
        $alt = "ロケット";

    } elsif($l == $HlandUmishuto) {
        # 海首都
        if($mode == 0) {
            # 観光者の場合は海のふり
            $image = Sea_Img_Gen($id, $x, $y);
            $alt = '海';
            $naviTitle  = '海';
        } else {
            $image = 'umishuto.png';
            $alt = "海底首都(${lv}$HunitPop)";
            $naviTitle  = '海底首都';
            $naviText  = "(${lv}$HunitPop)";
        }

    } elsif($l == $HlandGold) {
        # 金山
        $image = 'land15.gif';
        $alt = "金山(採掘場${lv}0${HunitPop}規模)";
        $naviTitle  = '金山';
        $naviText  = "金山${lv}0${HunitPop}規模";

    } elsif($l == $HlandSeatown) {
        # 海底新都市
        if($mode == 1) {
            my $owork =  int($lv/40);
            $image = 'land30.gif';
            $alt = "海底新都市(${lv}$HunitPop/職場${owork}0$HunitPop/農場${owork}0$HunitPop)";
            $naviTitle  = '海底新都市';
            $naviText  = "(${lv}$HunitPop/職場${owork}0$HunitPop/農場${owork}0$HunitPop)";
        } else {
            # 観光者の場合は海のふり
            $image = Sea_Img_Gen($id, $x, $y);
            $alt = '海';
            $naviTitle  = '海';
        }

    } elsif($l == $HlandYougan) {
        # 溶岩地帯
        $image = 'land60.gif';
        $alt = '溶岩地帯';
        $naviTitle  = '溶岩地帯';

    } elsif($l == $HlandStation) {
        # 駅
        $image = 'station.gif';
        $alt = '駅';
        $naviTitle  = '駅';

    } elsif($l == $HlandHouse) {
        # 島主の家
        my($n) = $onm;
        $n .= ('の小屋', 'の簡易住宅', 'の住宅', 'の高級住宅', 'の豪邸', 'の大豪邸', 'の高級豪邸', 'の城', 'の巨城', 'の黄金城')[$hlv];
        $image = "house${hlv}.gif";
        $alt = "$n";
        $naviTitle = $n;

    } elsif($l == $HlandKyujo) {
        # 野球場
        $image = 'land23.gif';
        $alt = '野球場';
        $naviTitle  = '野球場';

    } elsif($l == $HlandInoraLand) {
        # 遊園地
        $image = 'inoraland.gif';
        $alt = "いのらランド(従業員${lv}0${HunitPop}/収益見込${mikomi}$HunitMoney以上)";
        $naviTitle  = 'いのらランド';
        $naviText  = "従業員${lv}0${HunitPop}<br>収益見込${mikomi}$HunitMoney以上";

    } elsif($l == $HlandBigFood) {
        my ($foodkind);
        my ($foodHP);
        $foodkind = $lv >> $Food_Kind_Shift;

        $image =  $BigFoodImage[$foodkind];
        $alt = $BigFoodName[$foodkind];
        $naviTitle  = $BigFoodName[$foodkind];
        $foodHP = $lv & $Food_HP_MASK;
        $naviText  = "体力：${foodHP}";

    } elsif($l == $HlandYakusho) {
        # 島役所
        $image =  'land52.gif';
        $alt = "島役所:レベル:${lv}";
        $naviTitle  = "島役所:レベル:${lv}";
        $naviText = "レベル:${lv}";

    } elsif($l == $HlandOmamori) {
        # お守
        $image = 'mamori.gif';
        $naviTitle  = 'おまもり';
        $alt = "おまもり：効果　残り${lv}";
        $naviText  = "おまもり：効果　残り${lv}";

    } elsif($l == $HlandShuto) {
        # 首都
        $image = 'shuto.png';
        $shutomessage =~ s/'/’/g;
        $alt = "首都$shutomessage(${lv}$HunitPop)";
        $naviTitle  = "首都$shutomessage";
        $naviText  = "${lv}$HunitPop";

    } elsif($l == $HlandEgg) {
        # 卵
        $image =  $HEggImage[$lv];
        $alt = '卵';
        $naviTitle  = '卵';

    } elsif($l == $HlandSeki) {
        # 関所
        $image = 'land27.gif';
        $alt = '関所';
        $naviTitle  = '関所';

    } elsif($l == $HlandGomi) {
        # 関所
        $image = 'gomi_yotei.png';
        $alt = '埋立地';
        $naviTitle  = '埋立地';
        $naviText  = "${lv}のゴミ";

    } elsif($l == $HlandShrine) {
        # 時の神殿
        $image = 'shrine.gif';
        $alt = "時の神殿";
        $alt .= "(ターン${lv})" if($lv > 0);
        $naviTitle  = '時の神殿';
        $naviText = "ターン${lv}" if($lv > 0);

    } elsif($l == $HlandZoo) {
        # 動物園
        my ($zookazu, $zookazus, $m_syurui) = Get_ZooState($island);
        my ($bariaA) = $island->{'rena'} - $zookazus * 25;
        my ($bariaB) = $island->{'rena'} - $zookazus * 50;


        $image = 'land84.gif'; # 記念碑の画像を流用
        $alt = "動物園Lv${lv}";
        $naviTitle  = "動物園Lv${lv}";
        $naviText = "$m_syurui種類$zookazu匹/$mNameList<br>バリアＡ[$bariaA]バリアＢ[$bariaB]";

    } elsif($l == $HlandHospital) {
        $image =  'GShospital.gif';
        $alt = '病院';
        $naviTitle  = '病院';

    } elsif($l == $HlandBoueki) {
        $image =  'land70.gif';
        $alt = '貿易港';
        $naviTitle  = '貿易港';

    } elsif($l == $HlandMine) {
        if($mode == 1) {
            my ($da) = $lv & $Hmine_DAMAGE_MASK;
            # 地雷
            $image = 'land22.gif';
            $image = 'sea_mine.gif' if ($lv & $Hmine_SEA_FLAG);
            $alt = "地雷(ダメージ$da)";
            $naviText = "地雷(ダメージ$da)";
        } else {
            # 観光者の場合は森のふり
            $image = Forest_Img_Gen();
            $image = Sea_Img_Gen($id, $x, $y) if ($lv & $Hmine_SEA_FLAG);
            $alt = '森';
            $alt = '海' if ($lv & $Hmine_SEA_FLAG);
        }
        $naviTitle  = '森';
        $naviTitle  = '海' if ($lv & $Hmine_SEA_FLAG);

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
                # 開発画面の場合は、座標設定
                # out("<A HREF='JavaScript:void(0);' onclick='boxslct($x);return true;' ");
                out("<IMG  ");
                out("onclick=\"boxslct($x);return 1;\" onMouseOver=\"status = '$point $alt1 ';return true;\" onMouseOut=\"status = '';\" ");
                out("alt='' SRC=\"$image\" TITLE=\"$point $alt \" class='maptile cur_p'>");
                # 座標設定閉じ
                #out('</A>');
            } else {
                out("<IMG alt='' SRC=\"$image\" class='maptile'>");
                # 座標設定閉じ

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

                # 開発画面の場合は、座標設定
                out(qq|<A HREF=\"JavaScript:void(0);\" onclick=\"ps($x,$y);tohint('$point $alt1\\n$comStr');return true;\" onMouseOver="status = '$point $alt1 $comStr';return true;" onMouseOut="status = '';"><img src=\"$image\"TITLE=\"$point $alt $comStr\" class='${map_style}' alt=''></A>|);

            } else {
    #           out("<A HREF=\"JavaScript:void(0);\" onMouseOver=\"Navi($x, $y,'$image', '$naviTitle', '$naviText', $naviExp);\" onMouseOut=\"NaviClose(); return false\">");
    #           out("<A HREF=\"JavaScript:void(0);\" onMouseOver=\"Navi($x, $y,'$image', '$naviTitle', '$naviText', $naviExp); status = '$point $alt1 $comStr'; return true;\" onMouseOut=\"NaviClose(); status=''; return false\">");
    #           out("<img src=\"$image\" width=$Hms2 height=$Hms2 BORDER=0 onMouseOver=\"Navi($x,$y,'$image','$naviTitle','$naviText',$naviExp);\" onClick=\"Navi($x,$y,'$image','$naviTitle','$naviText',$naviExp);\" onMouseOut=\"NaviClose(); return false\">");
                out("<img src=\"$image\" class='${map_style}' alt='' onMouseOver=\"Navi($x,$y,'$image','$naviTitle','$naviText',$naviExp);\" ONKEYPRESS='return false;' onClick=\"Navi($x,$y,'$image','$naviTitle','$naviText',$naviExp);\">");
                # 座標設定閉じ
    #           out("</A>");
            }
        }

    }
}


# 各種拡張データ表示(帝国の興亡) kokoha nokosu
sub islandData {
    my(@data) = @{$Hislands[$HcurrentNumber]->{'ext'}};

    # 前処理
    $data[1] = int($data[1] / 10);
    $data[2] = $data[2] ? "$data[2]基" : 'なし';
    $data[3] = $data[3] ? "$data[3]基" : 'なし';
    $data[4] = $data[4] ? "$data[4]00人" : 'なし';
    $data[5] = $data[5] ? "$data[5]発" : 'なし';
    $data[6] = $data[6] ? "$data[6]発" : 'なし';
    $data[7] = $data[7] ? "$data[7]発" : 'なし';
    my ($monsterkill) = $Hislands[$HcurrentNumber]->{'taiji'} ? "$Hislands[$HcurrentNumber]->{'taiji'}$HunitMonster" : 'なし';
    my ($aStr1, $aStr2) = ('', '');
    my ($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $Hislands[$HcurrentNumber]->{'eisei4'});
    my ($kachiten) = $stwin*3 + $stdrow;
    my $nn = $HStadiumResult[$stshoka];
    $nn = '練習中' if($nn eq '');

    if ($HallyNumber) {
        $aStr1 = "<th $HbgTitleCell align=center>${HtagTH_}貢献度${H_tagTH}</th>";
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

    # 仕事場を確認
    $unemployed = 0;
    $work_farm = 0;
    $work_biz = 0;
    $work_bizHT = 0;

    if ($pop > $farm) {
        # 農業だけじゃ手が余る場合
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
        # 農業だけで手一杯の場合
        if ($farm) {
            $work_farm = int( ($pop /$farm)*100);
        }else{
            $work_farm = 0;
        }
    }
    $unemployed_str = "$unemployed$HunitPop";
    if (!$unemployed ){
        $unemployed_str = '0人';
    }

    out(<<END);
<div id='extInfo'>
  <table border="0">
    <tr>
      <td>
        <table border>
          <tr>
            $aStr1
            <th $HbgTitleCell align=center>${HtagTH_}防撃破${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}ミ撃破${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}民救出${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}弾飛来${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}弾発射${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}弾防御${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}退治数${H_tagTH}</th>
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
            <th $HbgTitleCell align=center>${HtagTH_}選手${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}攻${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}守${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}KP${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}勝点${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}試合${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}通算(勝率)${H_tagTH}</th>
            <th $HbgTitleCell align=center>${HtagTH_}優勝${H_tagTH}</th>
          </TR>
          <TR>
            <TD $HbgInfoCell align=center>$nn</td>
            <TD $HbgInfoCell align=center>$sto</td>
            <TD $HbgInfoCell align=center>$std</td>
            <TD $HbgInfoCell align=center>$stk</td>
            <TD $HbgInfoCell align=center>$kachiten</td>
            <TD $HbgInfoCell align=center>$stwin勝$stlose敗$stdrow分</td>
            <TD $HbgInfoCell align=center>$stwint勝$stloset敗$stdrowt分($shoritu%)</td>
            <TD $HbgInfoCell align=center>$styusho回</td>
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
    <th $HbgTitleCell align=center>${HtagTH_}農業<br>稼働率${H_tagTH}</th>
    <th $HbgTitleCell align=center>${HtagTH_}ビジネス<br>稼働率${H_tagTH}</th>
    <th $HbgTitleCell align=center>${HtagTH_}HT産業<br>稼働率${H_tagTH}</th>
    <th $HbgTitleCell align=center>${HtagTH_}失業者${H_tagTH}</th>
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
    $mspet = "<img src=\"${HMapImgDir}monster30.gif\" TITLE=\"マスコットいのら(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswin匹撃破/経験値$msexe)\" onMouseOver='status=\"マスコットいのら(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswin匹撃破/経験値$msexe)\"; return true;' onMouseOut=\"status = '';\" WIDTH=32 HEIGHT=\"32\">" if($mshp);
    $mspet = "<img src=\"${HMapImgDir}tet.gif\" TITLE=\"超神獣テトラ(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswin匹撃破/経験値$msexe)\" onMouseOver='status=\"超神獣テトラ(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswin匹撃破/経験値$msexe)\"; return true;' onMouseOut=\"status = '';\" WIDTH=32 HEIGHT=\"32\">" if($tet);

    $petname = 'マスコットいのら' if ($mshp);
    $petname = '超神獣テトラ' if ($tet);
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
<th $HbgTitleCell align=center>${HtagTH_}撃破${H_tagTH}</th>
<th $HbgTitleCell align=center>${HtagTH_}経験値${H_tagTH}</th>
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
        out("<b><a href=JavaScript:void(0); onClick='show_taijilist($island->{'id'},$ownmode)'>怪獣ずかん</a></b> / ");
        out("<b><a href=JavaScript:void(0); onClick='show_Productlist($island->{'id'},$ownmode)'>物資(仮)</a></b> / ");

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
          <input type="submit" value="取引画面(仮)" name="Trade=$HcurrentID">
        </form>
END
    }
}


#----------------------------------------------------------------------
# 地図の表示
#----------------------------------------------------------------------
# $modeが1なら、ミサイル基地等をそのまま表示
# $jsmodeが1なら、JSモード
sub islandMap {
    my ($mode, $jsmode) = @_;

    my ($island) = $Hislands[$HcurrentNumber];

    out(<<END);
<div id='islandMap'>
  <table border>
    <tr>
      <td>
END
    # 地形、地形値を取得
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
    local $nn = ('練習中', '予選第１戦待ち', '予選第２戦待ち', '予選第３戦待ち', '予選第４戦待ち', '予選終了待ち',    '準々決勝戦待ち', '準決勝戦待ち', '決勝戦待ち',
            '優勝！', '練習中', '予選落ち', '準々決勝負け', '準決勝負け', '第２位')[$stshoka];
    $nn = '練習中' if($nn eq '');


    if ( ($mode == 0) && ($island->{'effect'} & 1) ) {
        out('<div align=center>電波障害が発生しています！</div>');
    }

    # コマンド取得
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

    #ヒントパネル
    out("<div id='NaviView'></div>");
    out("<div class='map_cur' id='map_cur'></div>") if(($jsmode) && ($mode));
    out('<center><textarea style="resize:none;" cols="70" rows="3" id="HINT_PANEL">hint</textarea></center>') if((!$jsmode) && ($mode));
    # 座標(上)を出力
    # out("<nobr>");

    foreach $y (0..$islandSize) {
        out("<img src=\"img/space.png\" width=$Hms1 alt='' height=${Hms2}><img src=\"img/space${y}.gif\" alt='' width=$Hms1 height=${Hms2}>");
    }
    out("<img src=\"img/space.png\" width=$Hms1 alt='' height=${Hms2}><BR>\n");

    # 各地形および改行を出力
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
        # 偶数行目なら番号を出力
        out("<img src=\"img/space${y}.gif\" width='$Hms1' height='${Hms2}' alt=''>") if(!($y % 2));

        # 各地形を出力
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

        # 奇数行目なら番号を出力
        out("<img src=\"img/space${y}.gif\" width='$Hms1' height='${Hms2}' alt=''>") if ($y % 2);

        # 改行を出力
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

    out(<<END) if ($island->{'monsterlive'});       #怪獣いないなら、表示しない
MONSTER0 = "人造怪獣";
MONSTER1 = "";
MONSTER2 = "　奇数ターンは硬化";
MONSTER3 = "　ミサイル無効化(10%)";
MONSTER4 = "　最大2歩移動する";
MONSTER5 = "　最大何歩移動するか不明";
MONSTER6 = "　偶数ターンは硬化";
MONSTER7 = "";
MONSTER8 = "　腐海を生み出す<br>　最大2歩移動する";
MONSTER9 = "　ランダム硬化";
MONSTER10 = "　ミサイル無効化(10%)";
MONSTER11 = "　移動した時に90%で分裂";
MONSTER12 = "　最大何歩移動するか不明";
MONSTER13 = "　攻撃,ミサイル無効化(90%)<br>　衝撃波で周囲2hex壊滅<br>　幸福(???)";
MONSTER14 = "　ミサイル吸収(10%)<br>　ランダム硬化<br>　周囲1hexにスライム分裂";
MONSTER15 = "　ミサイル無効化(10%)<br>　ランダム硬化<br>　助けを呼ぶ";
MONSTER16 = "　ミサイル無効化(50%)<br>　衝撃波で周囲1hex壊滅<br>　自爆";
MONSTER17 = "　迎撃ミサイル発射(40〜90%)<br>　ミサイル発射(60%)<br>　多弾頭ミサイル発射(40%)<br>　アトミック☆ボム発射(20%)<br>　最大何歩移動するか不明";
MONSTER18 = "　ミサイル無効化(10%〜)<br>　刎頚(60%)<br>　めてお〜(60%)<br>　衝撃波で周囲2hex壊滅";
MONSTER19 = "　メテオ,クエイク<br>　ドレイン,召喚<br>　他の島にも影響します";
MONSTER20 = "　ミサイル無効化(30%)<br>　腐敗(20%)<br>　リミット解除(HP>13)<br>　自然治癒(ターン+2)<br>　衝撃波で周囲1hex壊滅";
MONSTER21 = "　ミサイル無効化(20%)<br>　大恐慌(15%),腐敗(20%)<br>　疫病(50%)<br>　自然治癒(ターン+3)";
MONSTER22 = "　ミサイル無効化(25%)<br>　アイスストーム(周囲1hex)<br>　アイシクルアロー(怪獣,ミサイル基地,防衛施設,船舶,油田)";
MONSTER23 = "　約500〜100000億円を盗んでいく。";
MONSTER24 = "　約5000〜1000000億円を盗んでいく。<br>約500000〜50000000トン食料を盗んでいく。";
MONSTER25 = "　最大2回ワープする";
MONSTER26 = "　ほかの島にもワープする";
MONSTER27 = "　海のかいぶつ";
MONSTER28 = "　がんばるペット怪獣";
MONSTER29 = "　他の怪獣を攻撃<br>　ペット専用";
MONSTER30 = "　一度に巨大な力を手にした為に覚醒しているテトラ";
MONSTER31 = "　観光客から地図が正しく表示されなくなる。";
MONSTER32 = "　額に流れる汗！腕っ節の強さ！そして勇ましい心！<br>大砲を撃ったり、お金を盗むことがある。";
MONSTER33 = "　ミサイル無効化(50%)";
MONSTER34 = "　ミサイル無効化(10%)／<br>怪獣がいると、産業からの収入がなくなる／<br>産業衰退ビームを放つ";
MONSTER35 = "　あばれてやるわー！！";
MONSTER36 = "";
MONSTER37 = "ほかの島にもワープする。行き先の土地を交換する。";
END

    out(<<END);
SHIP0  = "[維持費] 5${HunitMoney}<br>[収穫] 毎ターン290${HunitFood}〜320${HunitFood}";
SHIP1  = "[維持費] 5${HunitMoney}<br>[収穫] 毎ターン290${HunitFood}〜320${HunitFood}";
SHIP2  = "[維持費] 20${HunitMoney}<br>[収穫] 毎ターン490${HunitFood}〜530${HunitFood}";
SHIP3  = "[維持費] 300${HunitMoney}<br>[発見確率] 油田(2%)<br>　財宝(0.5%:Max50000${HunitMoney})";
SHIP4  = "[維持食料] 1000${HunitFood}<br>[収入] 毎ターン150${HunitMoney}〜400${HunitMoney}";
SHIP5  = "[維持費] 60${HunitMoney}<br>[収穫] 毎ターン690${HunitFood}〜730${HunitFood}";
SHIP6  = "[維持費] 30${HunitMoney}/1hex移動<br>[収入] 毎ターン490${HunitFood}〜530${HunitFood}/1hex移動";
SHIP7  = "[維持費] 500${HunitMoney}<br>[発見確率] 油田(4%)<br>　財宝(1%:Max100500${HunitMoney})";
SHIP8  = "[維持食料] 3000${HunitFood}<br>[収入] 毎ターン(1500 + 人口/1000)${HunitMoney}<br>[氷山激突確率] 10%";
SHIP9  = "[維持費] 100${HunitMoney}<br>[怪獣を始動攻撃] SPPミサイル100${HunitMoney}/1発";
SHIP10 = "[維持費] 400${HunitMoney}<br>[怪獣を瞬殺] 多段頭ミサイル3000${HunitMoney}/1発";
SHIP11 = "[維持費] 60${HunitMoney}/1hex移動<br>[収入] 毎ターン毎ターン690${HunitFood}〜730${HunitFood}/1hex移動";
SHIP19 = "[維持費] 1000${HunitMoney}<br>[怪獣を瞬殺] エネルギー砲50000${HunitMoney}/1発";

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
    // 左側
    StyElm.style.marginLeft = (x - 5) * 32 - 10;
  } else {
    // 右側
    StyElm.style.marginLeft = (x + 1) * 32;
  }
  StyElm.style.marginTop = (y) * 32 - 32 + 120; // y は固定

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
