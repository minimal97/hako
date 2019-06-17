#----------------------------------------------------------------------
# minimal97の箱庭諸島
# ランキング作成
# make から分岐
#
#----------------------------------------------------------------------

require './hako-const.cgi';

#----------------------------------------------------------------------
# ランキング
#----------------------------------------------------------------------
sub rankIslandMain {
    my $i;

    foreach $i (0..$islandNumber) {
        my $rena = $Hislands[$i]->{'rena'}; # 軍事力
        $Hislands[$i]->{'renae'} = int($rena / 10 ) + 1;

        my ($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $Hislands[$i]->{'eisei4'});
        $Hislands[$i]->{'kachiten'} = $stwin*3 + $stdrow;
        $Hislands[$i]->{'kachitent'} = $stwint*3 + $stdrowt;
        my $siaisu = $stwint + $stdrowt + $stloset;
        $siaisu = 1 if($siaisu == 0);
        $Hislands[$i]->{'shoritu'} = int($stwint / $siaisu * 100);
        $Hislands[$i]->{'teamforce'} = $sto + $std + $stk;
        $Hislands[$i]->{'styusho'} = $styusho;

		my($mshp, $msap, $msdp, $mssp) = (split(/,/, $Hislands[$i]->{'eisei5'}))[0..3];
		$Hislands[$i]->{'force'} = $mshp + $msap + $msdp + $mssp;

		foreach (split(/,/, $Hislands[$i]->{'eisei6'})) {
			$Hislands[$i]->{'tuni'} += $_;
			$Hislands[$i]->{'uni'}++ if($_ > 0);
		}
	}

    my $hcturn = int($HislandTurn/100) * 100;

    my @bAfterName = (
                   "$HunitPop", "0$HunitPop規模", "0$HunitPop規模", "0$HunitPop規模","$HunitTree",
                        '万羽', '万頭'      , '万頭'          , "$HunitMonster"   , "$HunitMonster",
                        'pts.', "$HunitPop" , "$HunitMoney"   , 'ヶ所'            , "",
                        'pts.', "$HunitPop" , "種類/$tuniヶ所", 'pts.'            , '回'           ,
            "％($rstwint勝$rstloset敗$rstdrowt分)", "($ktstwint勝$ktstloset敗$ktstdrowt分)", "($kstwin勝$kstlose敗$kstdrow分)",'pts' , "匹");

    my @bBeforeName = ('', '', '', '', '', '', '', '', '','', '前ターン＋', '前ターン＋', '前ターン＋', '', 'Lv', '合計', '', '', '合計', '', '', '勝点', '勝点' , '');

    my @islands;
    my @ids;
    $i = 0;
    foreach (@BUMON_ELEMENTS) {
        $islands{$_} = $Hislands[$HidToNumber{$HrankingID[$i]}];
        $ids{$_} = $islands{$_}->{'id'};
        $i++;
    }
    my ($tuni) = $islands{'uni'}->{'tuni'};
    my ($kstwin, $kstdrow, $kstlose) = (split(/,/, $islands{'kachiten'}->{'eisei4'}))[3..5]; # 
    my ($ktstwint, $ktstdrowt, $ktstloset) = (split(/,/, $islands{'kachitent'}->{'eisei4'}))[6..8]; # 
    my ($rstwint, $rstdrowt, $rstloset) = (split(/,/, $islands{'shoritu'}->{'eisei4'}))[6..8]; # 

    # 開放
    unlock();

    out(<<END);
<DIV ID='Ranking'  style='display=inline-block;'>
<H1>各部門別NO.1</H1>
<DIV width="100%"  style='display=inline-block;'>
<span class='Nret'>
目指せ<B>ALL NO.1</B></span>
<span class='Nret'>！！クリックすると、<B>観光</B>することができます。</span>
</DIV >
END
    my ($tag);
    foreach (0..$#BUMON_ELEMENTS) {
        my $id = $islands{$BUMON_ELEMENTS[$_]}->{'id'};
        my $name = islandName($islands{$BUMON_ELEMENTS[$_]});
        my $element = $islands{$BUMON_ELEMENTS[$_]}->{$BUMON_ELEMENTS[$_]};

        $tag = 'float:Left;';

        if ($_ == $#BUMON_ELEMENTS) {
            $tag = '';
        }

        out(<<END);
<TABLE ALIGN="center" class='RankingSeparate' style='display=inline-block; $tag'>
  <TR>
  <td>
    <TABLE BORDER=1 width="100%">
      <TR><TD class="RankingCell" ALIGN="center" COLSPAN="2">
      <span class="bumon">${BUMON_NAME[$_]}NO.1</span></TD></TR>
END

        if (   ($element ne '')
            && ($element != 0)) {
            out(<<END);
      <TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="${HthisFile}?Sight=${id}" alt="ID=${id}" title="ID=${id}">${HtagName_}${name}${H_tagName}</TD></TR>
      <TR><TD ALIGN="center">${bBeforeName[$_]}${element}${bAfterName[$_]}</TD></TR>
    </TABLE>
  </TD>
  </TR>
</TABLE>
END
        } else {
            out(<<END);
      <TR><TD ALIGN="center">${HtagName_} - ${H_tagName}</TD></TR>
      <TR><TD ALIGN="center"> - </TD></TR>
    </TABLE>
  </TD>
  </TR>
</TABLE>
END
        }
#        out("</TR></TABLE>\n") if(!(($_ + 1) % 5));
    }
#   out("</TR></TABLE>\n") if((($#BUMON_ELEMENTS + 1) % 5));
    out("</DIV>\n");
}


#----------------------------------------------------------------------
# 歴代人口記録
#----------------------------------------------------------------------
# メイン
sub rekidaiPopMain {

    my ($flag, $id, $pop, $turn, $name, @rekidai, $oldpop);

    $flag = 0;

    if (!open(RIN, "<${HdirName}/rekidai.dat")) {
        rename("${HdirName}/rekidai.tmp", "${HdirName}/rekidai.dat");
        if (!open(RIN, "<${HdirName}/rekidai.dat")) {
            $flag = 1;
        }
    }

    if (!$flag) {
        my ($n);
        my ($line);

		$n = 0;
		while($line = <RIN>) {
			$line =~ /^([0-9]*),([0-9]*),([0-9]*),(.*)$/;
			($id, $pop, $turn, $name) = ($1, $2, $3, $4);
			$rekidai[$n]->{'id'} = $id;
			$rekidai[$n]->{'pop'} = $pop;
			$rekidai[$n]->{'turn'} = $turn;
			$rekidai[$n]->{'name'} = $name;
			$n++;
		}
		close(RIN);
	}
	# 開放
	unlock();

	out(<<END);
<DIV align='center'>$HtempBack</DIV><BR>
<DIV ID='Successive'>
<H1>歴代最多人口記録</H1>
<table border=0 width=50%><tr>
<TH $HbgTitleCell align=center>${HtagTH_}順位${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}${AfterName}名${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}人口${H_tagTH}</TH>
<TH $HbgTitleCell align=center>${HtagTH_}ターン${H_tagTH}</TH>
END
    if (!$flag) {
        my ($j);
        my ($n);
        my ($reki);

		$j = 0;
		$n = 1;
		$oldpop = 0;
		$pop = 0;
		while(($j < 10) || $flag) {
			$reki = $rekidai[$j];
			last unless(defined $reki->{'pop'});
			$oldpop = $pop;
			($id, $pop, $turn, $name) = ($reki->{'id'}, $reki->{'pop'}, $reki->{'turn'}, $reki->{'name'});
			if(defined $HidToNumber{$id}) {
				$name = "<A STYlE=\"text-decoration:none\" HREF=\"${HthisFile}?Sight=${id}\" alt=\"ID=${id}\" title=\"ID=${id}\">${HtagName_}$name${AfterName}${H_tagName}</A>";
			} else {
				$name = "${HtagName2_}$name${AfterName}${H_tagName2}";
			}
			$j++;
			$n = $j if($oldpop > $pop);
			$reki = $rekidai[$j];
			$flag =0 unless(defined $reki->{'pop'});
			if($reki->{'pop'} < $pop) {
				$flag =0;
			} else {
				$flag =1;
			}
			out(<<END);
</tr><tr>
<TD $HbgNumberCell align=right>${HtagNumber_}$n${H_tagNumber}</TD>
<TD $HbgNameCell align=right>$name</TD>
<TD $HbgInfoCell align=right>$pop${HunitPop}</TD>
<TD $HbgInfoCell align=right>$turn</TD>
END
		}

	} else {
		out(<<END);
</tr><tr><TH colspan=4>データがありません！</TH>
END
	}
		out(<<END);
</tr></table></DIV>
END

}

1;

