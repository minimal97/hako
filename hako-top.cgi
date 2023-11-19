#----------------------------------------------------------------------
# Ȣ����� ver2.30
# �ȥåץ⥸�塼��(ver1.00)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# Hakoniwa R.A. ver2.11
# �ᥤ�󥹥���ץ�(Ȣ����� ver2.30)
# ���Ѿ�������ˡ���ϡ�read-renas.txt�ե�����򻲾�
#
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------
require './hako-landinfo.cgi';
require './server_config.pm';
#----------------------------------------------------------------------
# �ȥåץڡ����⡼��
#----------------------------------------------------------------------
# �ᥤ��
sub topPageMain {
    # ������������
    axeslog() if ($HtopAxes == 2);
    # ����
    unlock();

    # �ƥ�ץ졼�Ƚ���
    tempTopPage();
}

#----------------------------------------------------------------------
#
#   �ǥХå���
sub DebugButtonPrint {

    if (DEBUG_MODE) {
        out(<<END);
    <form action="$HthisFile" method="POST">
      <input type="submit" value="�������ʤ��" name="TurnButton">
    </form>
END
    }
}


#----------------------------------------------------------------------
sub PrintTopMenuLink {

    my ($output);

    $output = "<div class='TopMenuLink'>\n";

    if (!(ADMIN_JOIN_ONLY)) {

        $output .= "[<a class='Nret' href='$HthisFile?Join=0'>������${AfterName}��õ��</a>] \n";
    }
    else {

        $output .= (qq|<b>��</b>������${AfterName}��õ���������ϡ�<b>${AfterName}̾�����ʤ���̾�����ѥ����</b>�פ�����ͤޤǥ᡼�뤷�Ƥ���������<br>|);
    }
    $output .= (qq|<span class='Nret'>[<a href="$HthisFile?Rename=0">${AfterName}��̾���ȥѥ���ɤ��ѹ�</a>]</span> |);

    #out(qq|[<A href="$HthisFile?JoinA=0">Ʊ��������</A>] |) if(($HallyUse == 1) );
    if (   (USE_GZIP)
        || (!(USE_HTML_LOG_MDOE))
        || (!(-e "${HhtmlDir}/hakolog.html")) ) {

        $output .= (qq|[<a class='Nret' href="${HbaseDir}/history.cgi?Event=0" target="_blank">�Ƕ�ν����</a>] |);
    }
    else {

        $output .= (qq|[<a class='Nret' href="${htmlDir}/hakolog.html" target="_blank">�Ƕ�ν����</a>] |);
    }

    out(<<END);
  $output
  [<a class='Nret' href="$HthisFile?Rekidai=0" target="_blank">�����¿�͸���Ͽ</a>] 
  [<a class='Nret' href="$HthisFile?Rank=0" target="_blank">��󥭥�</a>] 
</div><!-- $init_server -->
END
}


#----------------------------------------------------------------------
sub PrintScriptTag {

    out(<<END);
<script type="text/javascript"><!--
function newdevelope(){
  document.Island.target = "newWindow";
  document.Island.submit();
}
// -->
</script>
END

}


#----------------------------------------------------------------------
# �����ȥ�˥塼
#----------------------------------------------------------------------
sub TopSiteMenu {

    my (@URL_Table) = (
        [ "miniverse" , "../frm/viewforum.php?f=4"],
        [ "�ޥ˥奢��", "http://minimal97.com/wiki/"],
    );

    my ($tbl_cnt) = (@URL_Table >> 1) + 1;        # table / 2 ����
    my ($i);
    my ($adr , $title);

    if ($tbl_cnt) {

        my ($outtext) = '';

        $outtext =<<END;
    <h2>
      <small>
END
        for ($i = 0 ; $i < $tbl_cnt ; $i++) {

            $title = $URL_Table[$i][0];
            $adr = $URL_Table[$i][1];
            $outtext .= "<a title='$title' href='$adr' target='_blank' class='Nret'>$title</a>��";
        }

        $outtext .=<<END;
      </small>
    </h2>
END
        out($outtext);
    }
}


#----------------------------------------------------------------------
sub tempNewsspace {

    my ($news_rand) = random(100);      # ����å�����

    out(<<END);
  <div class='topblock'>
    <h2 class='subtitle'>�˥塼����</h2>�ޤ��ϡ���˾������С�miniverse�˵��ܤ��Ƥ���������<span class='Nret'><a target='_blank' href='http://minimal97.com/wiki/index.php?%BD%A4%C0%B5%B3%D0%BD%F13'>����˺٤������</a></span><br>
    <div class='ifrm-container'>
      <iframe class='ifrm' scrolling='auto' src='news.html?no-cache=$news_rand'></iframe>
    </div>
  </div>
END

}

#----------------------------------------------------------------------
sub Login_space {

    my ($radio,$radio2);

    $radio = '';
    $radio2 = '';

    # java �⡼�ɤ��� cgi�⡼�ɤ�
    if ($HjavaModeSet eq 'java') {

        $radio2 = 'checked';
    }
    elsif ($HjavaModeSet eq 'cgi') {

        $radio = 'checked';
    }
    else {
        # default
        $radio2 = 'checked';
    }

    out(<<END);
<div class='topblock'>
  <div class='myIsland'>
    <h2 class='subtitle'>��ʬ��${AfterName}��</h2>
    <form name="Island" action="$HthisFile" method="post">
      ���ʤ���${AfterName}��̾���ϡ�<br>
      <select name="ISLANDID">
          $HislandList
      </select><br><br>
      �ѥ���ɤ�ɤ�������<br>
      <input type="hidden" name="OwnerButton">
      <input type="text" name="PASSWORD" value="$HdefaultPassword" size="32" maxlength="32"><br>
      <input type="radio" name="JAVAMODE" value="cgi"  $radio>CGI�⡼��
      <input type="radio" name="JAVAMODE" value="java" $radio2>Java������ץȥ⡼��<br>
      <input type="submit" value="��ȯ���˹Ԥ�">������
      <input type="button" value="����������" onClick="newdevelope()">
    </form>
  </div>
</div>
END


}

#----------------------------------------------------------------------
sub PrintTopBlock {

    out(<<END);
${HtagTitle_}$Htitle${H_tagTitle}
<h2 class="subtitle">
  <small>
    <span class='Nret'>�����Τ����ϡ�</span>
    <span class='Nret'>[������${AfterName}��õ��]����!!</span>
  </small>
</h2>
<div style="display:block;">
  <div class="topblock">
END

    # �ǥХå��⡼�ɤʤ�֥������ʤ��ץܥ���
    DebugButtonPrint();

    # ��λ��������Ƚ�λ������ɽ��
    my ($HlastTurnS);
    if (!(INIT_GAME_LIMIT_TURN)) {

        $HlastTurnS = '';
    }
    elsif ($HislandTurn < $HgameLimitTurn) {

        my ($remainTime) = 0;
        if (INIT_FLEX_TIME_SET) {

            my ($all) = 0;
            my ($tsn, $ten);

            foreach (@HflexTime) {$all += $_;}
            $tsn = $HislandTurn % @HflexTime;
            {
                my ($ts, $te);
                $ts  = int($HislandTurn / @HflexTime);
                $te  = int($HgameLimitTurn / @HflexTime);
                $ten = $HgameLimitTurn % @HflexTime;
                $remainTime += $all * ($te - $ts - 1);
            }

            if ($tsn) {

                foreach($tsn..$#HflexTime) {

                    $remainTime += $HflexTime[$_];
                }
            }
            else {

                $remainTime += $all;
            }

            if ($ten) {
                foreach(0..($ten - 1)) {

                    $remainTime += $HflexTime[$_];
                }
            }
            $remainTime *= 3600;
        }
        else {

            $remainTime = $HunitTime * ($HgameLimitTurn - $HislandTurn);
        }

        {
            my ($HlimitTime);
            $HlimitTime = $HislandLastTime + $remainTime;
            $HlimitTime = sprintf('%dǯ %d�� %d�� %d��', (gmtime($HlimitTime + $Hjst))[5] + 1900, (gmtime($HlimitTime + $Hjst))[4] + 1, (gmtime($HlimitTime + $Hjst))[3,2]);
            $HlastTurnS = "<small>��${HgameLimitTurn}<small>��${HlimitTime}�ޤǡ�</small></small>";
        }
    }
    else {

        $HlastTurnS = '���ʥ�����Ͻ�λ���ޤ�����';
    }

    TopSiteMenu();

    # <a title="Ȣ���̥ޥåף�" href="../hako_k" target="_blank" class='Nret'>Ȣ���̥ޥå�N</a>

    # ���ߤΥ������ɽ��
    #my ($mode) = '';
    #$mode = ($HislandTurn < $HarmisticeTurn) ? "(��$HarmisticeTurn <small>�������</small>)" : ($HislandTurn == $HarmisticeTurn) ? '(<small>������������Ʈ����</small>)' : '(<small>��Ʈ����</small>)' if($HarmisticeTurn);
    out('    <div class="Turn">');
    #�����̵�� $Hseason
    out(qq|<h2 class="subtitle"><small>������</small> ${HislandTurn}<small>${HlastTurnS}</small></h2></div>\n|);

    # ����
    {
        my ($i);
        my ($str_sq) = '';
        my ($real) = ($HislandTurn + 8) % 12 ;
        for ($i = 0 ; $i < 12; $i++) {

            $str_sq .= ($i == $real) ? '��' : '��';
        }
        out($str_sq);
    }

    # ���󹹿�����ɽ��
    my ($aaa);
    if (INIT_FLEX_TIME_SET) {
        $aaa = $HislandLastTime + 3600 * $HflexTime[($HislandTurn % ($#HflexTime + 1))];
    }
    else {
        $aaa = $HislandLastTime + $HunitTime;
    }


    my ($sec2, $min2, $hour2, $date2, $mon2, $dummy2);
    {
        ($sec2, $min2, $hour2, $date2, $mon2, $dummy2, $dummy2, $dummy2, $dummy2) = gmtime($aaa + $Hjst);
    }

    my ($sss) = '';
    {
        my ($sec, $min, $hour, $mon, $day);
        $mon = %main::Hday{'month'};
        $day = %main::Hday{'day'};
        $hour = %main::Hday{'hour'};
        $min = %main::Hday{'min'};
        $sec = %main::Hday{'sec'};
        $sss = "$mon�� $day�� $hour�� $minʬ $sec��";
        $mon2++;
    }

    my ($bbb) = '';
    if (   ($HgameLimitTurn == 0)
        || ($HislandTurn < $HgameLimitTurn) ) {

        $bbb = "${mon2}�� ${date2}�� ${hour2}�� ${min2}ʬ";
    }
    else {

        $bbb = '��������ߤ��Ƥ��ޤ�';
    }

    # ���Υ�����ޤǤλ���ɽ��
    if (   !($HmainMode eq 'turn')
        && (defined $HleftTime) ) {

        $hour2 = int($HleftTime/3600);
        $min2 = int(($HleftTime-$hour2*3600)/60);
        $sec2 = ($HleftTime-$hour2*3600-$min2*60);
        $rtStr = "���ι������֤ޤǤ��� $hour2���� $min2ʬ $sec2��";
    }
    else {

        if ($HplayNow) {

            $rtStr = "������򹹿����ޤ���\n";
        }
        else {

            $rtStr = '';
        }
    }

# �ꥢ�륿���ޡ�
    if (INIT_REAL_TIMER) {

        out(<<END) if (defined $HleftTime);
    <form name="frm_TIME" style="margin  : 2px 0px;">
      <input type="text" name="TIME" size="50" readonly class="timer">
    </form>
    <script type="text/javascript"><!--
var leftTime = $HleftTime;
var hour, min, sec;

function showTimeLeft() {
  if (leftTime > 0) {
    setTimeout('showTimeLeft()', 1000);
    hour = Math.floor(leftTime / 3600);
    min  = Math.floor(leftTime % 3600 / 60);
    sec  = leftTime % 60;
    leftTime--;
    document.frm_TIME.TIME.value = '���ι������֤ޤǤ��� ' + hour + '���� ' + min + 'ʬ ' + sec + '��';
  }
  else {
    document.frm_TIME.TIME.value = '�����󹹿�����ˤʤ�ޤ����� ($HnextTime)';
  }
}

if ($HplayNow) {
  showTimeLeft();
}
else {
  document.frm_TIME.TIME.value = '';
}
//-->
    </script>
END

    }
    else {

        out("<div class='timer'>$rtStr</div>");
    }
    # �ե�����
    out(<<END);
    <p id="nexttime">
        ���ߤλ��֡�<b>$sss</b><br>�ʼ���ι������֡�$bbb��
    </p>
    <span class="rednews">�����󹹿��ն�Ǥι���Ϣ�ǤϹ����Ƥ���������<br>��ǡ���������ޤ���<br>�����30�ä��ԤäƤ���������<br>
��κ����ϤҤȤꡢ����ޤǤǤ���<br>Ʊ��IP���ɥ쥹��������Ƥ�줿��򸫤Ĥ����顢����ޤ���</span>
  </div>
END

    tempNewsspace();

    out(<<END);
</div>
END
}


#----------------------------------------------------------------------
# �ȥåץڡ���
#----------------------------------------------------------------------
sub tempTopPage {

    PrintTopMenuLink();

    PrintScriptTag();

    out("<hr>");

    PrintTopBlock();

    out("<hr>");

    Login_space();

    historySpace();

    out(<<END);
<div style="display:block; float:none">
  <hr>
END

    AllyMakeButton();

    out(<<END);
</div>
<hr>
END
    PrintWorldStat();

    islandSort('pts');
    out(<<END);
<div>
  <div>
    <h2 class="subtitle">��${AfterName}�ξ���</h2>
    <span class='Nret'>${AfterName}��̾���򥯥�å�����ȡ�</span>
    <span class='Nret'><b>�Ѹ�</b>���뤳�Ȥ��Ǥ��ޤ���</span>
    <div id='islandView'>
END

    my ($island, $j, $farm, $factory, $factoryHT, $mountain, $unemployed, $renae, $pts, $eisei2, $eisei2nd,
        $hcturn, $name, $id, $prize, $ii, $num);
    {
        my ($jj , $k);

        $jj = int(($islandNumber + INIT_VIEW_ISLAND_COUNT - $HbfieldNumber) / INIT_VIEW_ISLAND_COUNT);
        if ($jj > 1) {

            for ($ii = 0; $ii < $jj; $ii++) {

                $j = $ii * INIT_VIEW_ISLAND_COUNT;
                $k = min($j + INIT_VIEW_ISLAND_COUNT, $HislandNumber - $HbfieldNumber);
                $j++;
                $j = '��' if (!$ii && $HbfieldNumber);

                out(qq|<a href="$HthisFile?View=$ii#View">${HtagNumber_}[$j��$k]${H_tagNumber}</a>&nbsp;|);
            }
        }
    }

    my ($mStr1) = '';
    if (INIT_HIDE_MONEY_MODE) {
        $mStr1 = "  <th $HbgTitleCell align='center'>${HtagTH_}���${H_tagTH}</th>";
    }

    my ($msStr1) = '';
    if (INIT_HIDE_MISSILE_MODE) {
        $msStr1 = "  <th $HbgTitleCell align='center'>${HtagTH_}�ߥ������";
        if (INIT_USE_ARM_SUPPLY) {

            $msStr1 .= "(����ʪ��)${H_tagTH}</th>";
        }
        else {
            $msStr1 .= "${H_tagTH}</th>";
        }
    }

    out('<table border>');

    my ($head);
    $head = <<"END";
<tr>
  <th $HbgTitleCell align="center">${HtagTH_}��<br>��${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}${AfterName}${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}ŷ��${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}�͸�${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}����${H_tagTH}</th>
$mStr1
  <th $HbgTitleCell align="center">${HtagTH_}����${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}����${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}����${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}�ϥ��ƥ�<br>����${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}�η���${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}����<br>����${H_tagTH}</th>
$msStr1
</tr>
END

    my ($col) = 4 + (INIT_HIDE_MONEY_MODE != 0) + (INIT_HIDE_MISSILE_MODE != 0);
    my ($col1) = 5 + $col;
    my ($col2) = 7 + $col;

    $HviewIslandNumber *= INIT_VIEW_ISLAND_COUNT;
    my ($start, $end) = ($HviewIslandNumber + $HbfieldNumber, min($HviewIslandNumber + INIT_VIEW_ISLAND_COUNT + $HbfieldNumber, $HislandNumber));
    $start = 0 if (!$HviewIslandNumber);

    my ($HbgStatCell);
    my ($HbgNumCell);
    my ($weather , $w_tag);
    my ($unilist) = '';
    my ($ino) = '';
    my ($zooicon) = '';
    my @uniName = ( '[ŷ�ȥߥ�����]',
                    '[����]',
                    '[���줿��ά��]',
                    '[��굤�æ����]',
                    '[����]',
                    '[����]',
                    '[ɹ��]',
                    '[����]',
                    '[����]',
                    '[����]',
                    '[�������]',
                    '[��ʡ�ν�����]',
                    '[200�������Ĥ���]'
                                            );

    my ($ssss);             # �������������
    my ($areatag , $shutoname,$absent);
    my ($unique) = '';
    my ($siaisu,$mspet,$monslive,$BF_Flag);
    my ($BF_Score) = '';
    my ($me_sat) = '';
    $msStr1 = '';

    my ($bumons,$hlv,$pop,$Farmcpc , $oStr);
    my ($uniNum) = $#uniName + 1;

    $hcturn = int($HislandTurn / 100) * 100;

    for ($ii = $start; $ii < $end; $ii++) {

        $j = $ii + 1 - $HbfieldNumber;
        $island = $Hislands[$ii];
        if (($HbfieldNumber && $j == 1) || ($ii == $start)) {

            out("<tr><th></th></tr><tr><th></th></tr>$head");
        }
        $id         = $island->{'id'};
        $farm       = $island->{'farm'};
        $factory    = $island->{'factory'};
        $factoryHT  = $island->{'factoryHT'};
        $mountain   = $island->{'mountain'};
        $pop        = $island->{'pop'};
        if ($pop) {
            $unemployed = ($pop - ($farm + $factory +$factoryHT+ $mountain) * 10) / $pop * 100;
            $unemployed = '<span class="' . ($unemployed < 0 ? 'unemploy1' : 'unemploy2') . '">' . sprintf("%.2f%%", $unemployed) . '</span>';
        }
        $farm       = (!$farm) ? "��ͭ����" : ${farm}.'0'.$HunitPop;
        $factory    = (!$factory) ? "��ͭ����" : "${factory}0$HunitPop";
        $factoryHT  = (!$factoryHT) ? "��ͭ����" : "${factoryHT}0$HunitPop";
        $mountain   = (!$mountain) ? "��ͭ����" : "${mountain}0$HunitPop";
        $renae      = int($island->{'rena'} / 10 );
        $pts        = $island->{'pts'};
        $eisei2     = $island->{'eisei2'};
        $eisei2nd   = int($eisei2 / 100 );

        $weather    = $island->{'weather_old'};
        $w_tag      = "<img src='./img/weather/weather$weather.gif' alt=''>";

        $eisei2     = ($eisei2nd == 0) ? '�̻��Ѹ��Կ�������̤��<br>' : '�̻��Ѹ��Կ�'.$eisei2nd.'����<br>';

        $absent = $island->{'absent'};

        $name = islandName($island);

        $BF_Flag    = isBattleField($island);

        if ($BF_Flag) {

            $j = '��';
            $name = ${HtagNumber_}. $name. ${H_tagNumber};
        }
        elsif ($absent == 0) {

            $name = ${HtagName_}.$name.${H_tagName};
        }
        else {

            $name = ${HtagName2_} . $name . '('.$absent.')' . ${H_tagName2} ;
        }
        $name = '<span class="attention">�ڴ����ͤ��������</span><br>' . $name if ($island->{'predelete'});

        $bumons = '';
        $prize = '';
        $BF_Score = '';
        $me_sat = '';
        $ssss = '';
        # �Хȥ�ե�����ɤǤ�ɽ�����ʤ���
        if (!$BF_Flag) {

            my @uniData = split(/,/, $island->{'eisei6'});
            $unilist = '';
            $island->{'uni'} = 0;
            $island->{'tuni'} = 0;

            foreach (0..$#uniName) {

                $unilist .= " $uniName[$_]\n" if ($uniData[$_] > 0);
                $island->{'tuni'} += $uniData[$_];
                $island->{'uni'}++ if($uniData[$_] > 0);
            }

            $ino = ($island->{'inoraland'}) ? "<img src=\"${HStatImgDir}inoraland.gif\" alt='' title=\"���Τ����\" class='landinfoIcon'>" : '';
            $zooicon = ($island->{'zoo_Mons_cnt'}) ? "<img src=\"${HStatImgDir}land84.gif\" alt='' title=\"ưʪ�� $island->{'zoo_Mons_cnt'}ɤ\" class='landinfoIcon'>" : '';

            my ($rt) = "\n";
            $unique = '';
            if ($island->{'uni'}) {

                $unique = "<span class='shuto'><img src=\"./img/prize/prize10.svg\" alt='' title=\"������񤷤���ˡ����Ϸ���$rt${unilist}����$uniNum����\" ";
                $unilist =~ s/$rt//g;
                $unique .= "class='landinfoIcon'> $island->{'tuni'}���� </span>";
            }

            {
                my ($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $island->{'eisei4'});
                $island->{'kachiten'} = $stwin*3 + $stdrow;
                #$island->{'kachitent'} = $stwint*3 + $stdrowt;
                $siaisu = $stwint + $stdrowt + $stloset;
                $siaisu = ($siaisu == 0) ? 1 : ($siaisu) ;
                #$island->{'shoritu'} = int($stwint / $siaisu * 100);
                #$island->{'teamforce'} = $sto + $std + $stk;
                #$island->{'styusho'} = $styusho;
                my ($nn) = $HStadiumResult[$stshoka];

                $nn = ($nn eq '') ? '������' : $HStadiumResult[$stshoka] ;

                if ($stshoka >= 1) {

                    $ssss = "<img src=\"./img/sc.gif\" title=\"".$nn.' ��('.$sto.')��('.$std.')KP('.$stk.')'.$rt.'���������� ����' . $island->{'kachiten'} .'/ '.$stwin.'��'.$stlose.'��'.$stdrow.'ʬ'.$rt." / �̻�$stwint��$stloset��$stdrowtʬ / ͥ��$styusho��\" alt='' class='landinfoIcon'> "
                }
                elsif ($stshoka == 0) {

                    $ssss = '';
                }
            }

            {
                my ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
                my ($force) = $mshp + $msap + $msdp + $mssp;
                $island->{'force'} = $force;
                $mspet = "<img alt='' src=\"${HMapImgDir}ms.gif\" title=\"�ޥ����åȤ��Τ�" .
                         "(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswinɤ����/�и���$msexe)\" ".
                         "onMouseOver='status=\"�ޥ����åȤ��Τ�(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswinɤ����/�и���$msexe)\"; return true;' ".
                         " class='landinfoIcon'>Sum($force)" if ($mshp);
                $mspet = "<img alt='' src=\"${HMapImgDir}tet.gif\" title=\"Ķ���åƥȥ�" .
                         "(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswinɤ����/�и���$msexe)\" ".
                         "class='landinfoIcon'>Sum($force)" if ($tet);
                $mspet = '' if (!$mshp && !$tet);
            }

            $bumons = ScoreBoard_Bumon($island);

            $prize = ScoreBoard_Prize($island);         # ������ޡ�����¾��
            $prize .= ScoreBoard_Taiji($island);        # �ݤ������åꥹ��  ���ä����䤹�Τǡ��ꥹ�ȤϺ��

            $BF_Score = ScoreBoard_BF_Point($island);   # �Хȥ�ե�����ɥ�����

            $me_sat = ScoreBoard_Eisei($island);        # �͹�����
        }

        $HbgStatCell = $HbgCommentCell;
        $HbgStatCell = 'class="MonsterCell"' if ($island->{'monsterlive'});

        # ���
        my ($mStr1) = '';
        if (INIT_HIDE_MONEY_MODE == 1) {

            $mStr1 = "<td class=TopInfoCell align=right>".$island->{'money'}.$HunitMoney.'</td>';
        }
        elsif (   (INIT_HIDE_MONEY_MODE == 2)
               || (INIT_HIDE_MONEY_MODE == 3)) {

            my ($mTmp) = aboutMoney($island->{'money'});
            $mStr1 = "  <td class='TopInfoCell' align='right'>$mTmp</td>";
        }

        # �ߥ�����ȯ�Ͳ�ǽ��
        $msStr1 = '';
        if (INIT_HIDE_MISSILE_MODE) {

            $msStr1 = "<td class='TopInfoCell' align='right'>$island->{'missiles'}${HunitMissile}";
            if (INIT_HIDE_MISSILE_MODE == 2) {

                my ($mTmp) = aboutMissile($island->{'missiles'});
                $msStr1 = "<td class='TopInfoCell' align='right'>${mTmp}</td>";
            }
            elsif (INIT_USE_ARM_SUPPLY) {

                $msStr1 .= "($island->{'army'}��)</td>";
            }
            else {

                $msStr1 .= '</td>';
            }
        }

        {
            my ($comment_tag);
            if ($island->{'onm'} eq '') {

                $comment_tag = "${HtagTH_}������ : ${H_tagTH}";
            }
            else {

                $comment_tag = "${HtagLbbsSS_}$island->{'onm'} : ${H_tagLbbsSS}";
            }
            $oStr = "<td $HbgTotoCell colspan='$col1' align='left'>${comment_tag}$island->{'comment'}</td>";
        }

        my ($house) = '';

        $Farmcpc = '';
        if (!$BF_Flag) {
                                                                        # �Ҿ��
            $Farmcpc = ScoreBoard_Farm($island);
                                                                        # ��
            {
                my ($eisei1) = $island->{'eisei1'};

                if ($eisei1) {

                    $hlv = Calc_HouseLevel($pts);

                    my ($onm) = $island->{'onm'};
                    my ($n) = "��$HHouseName[$hlv]";
                    my ($zeikin) = int($pop * ($hlv + 1) * $eisei1 / 100);
                    $house .= "<span class='house'><img src=\"${HMapImgDir}house${hlv}.gif\" alt='' title=\"$onm$n\" class='landinfoIcon'>��Ψ$eisei1��($zeikin$HunitMoney)</span>"
                }
                else {

                    $house = '';
                }
            }
            # ����̾
            my ($top_shutomsg) = $island->{'shutomessage'};
            $shutoname = ($top_shutomsg == 555) ? '' : "<font size='-1'><span class='shuto'>���ԡ�".$top_shutomsg.'</span></font><br>';
        }

        # �и���β��åꥹ��
        $monslive = ScoreBoard_LiveMonster($island);
        $monslive = "<br>$monslive" if (($island->{'monsterlive'}) && (!$BF_Flag));

        $HbgNumCell = ($island->{'missileAlert'}) ? 'class="NumberCellAlert topNumber"' : 'class="NumberCell topNumber"' ;

        out(<<END);
<tr>
<th $HbgNumCell rowspan="4" align="center">
  ${HtagNumber_}$j${H_tagNumber}
</th>
END

        if (!$BF_Flag) {

            out(<<END);
<td $HbgNameCell rowspan="4" align="left">
  <div align="center">
    <a style=\"text-decoration:none\" href="${HthisFile}?Sight=${id}" title="ID:${id}">$name</a><br>
    $shutoname
    <span class="point">$pts</span>pts.<br>
    <font size="-1">����Ψ</font>:($unemployed)<br>
    <span class="eisei"><font size="-1">$eisei2</font></span>
  </div>
</td>
END
        }
        else {

            $msStr1 = "<td ${HbgInfoCell} align='right'>��</td>" if (INIT_HIDE_MISSILE_MODE);
            $oStr = "<td $HbgTotoCell colspan='$col1' align='left'>${HtagLbbsSS_}$server_config::HadminName${H_tagLbbsSS} : $island->{'comment'}</td>";
            out(<<END);
<th $HbgNameCell rowspan="4" align="left">
  <div class="t_center">
    <a style=\"text-decoration:none\" href="${HthisFile}?Sight=${id}" title="ID:${id}">$name</a><br><br>
    <a style=\"text-decoration:none\" href="${HthisFile}?BF_point=0">${HtagTH_}<u>Battle Field����</u>${H_tagTH}</a>
  </div>
</th>
END
        }
        $areatag = (!$island->{'area'}) ? '0��' : $island->{'area'}.$HunitArea;
        out(<<END);
<td class="TopInfoCell" align="center">$w_tag</td>
<td class="TopInfoCell" align="right">${pop}${HunitPop}</td>
<td class="TopInfoCell" align="right">$areatag</td>
$mStr1
<td class="TopInfoCell" align="right">$island->{'food'}$HunitFood</td>
<td class="TopInfoCell" align="right">$farm</td>
<td class="TopInfoCell" align="right">$factory</td>
<td class="TopInfoCell" align="right">$factoryHT</td>
<td class="TopInfoCell" align="right">$mountain</td>
<td class="TopInfoCell" align="right">Lv$renae</td>
$msStr1
</tr>
<tr>
  <td $HbgTotoCell colspan="5" align="left">${HtagtTH_}����1��${H_tagtTH}$island->{'totoyoso'}->[0]</td>
  <td $HbgTotoCell colspan="$col" align="left">${HtagtTH_}����2��${H_tagtTH}$island->{'totoyoso'}->[1]</td>
</tr>
<tr>
  $oStr
</tr>
<tr>
  <td $HbgStatCell colspan="$col1" align="left">${HtagtTH_}<font size="-1">$prize$ino$zooicon$ssss$unique$house$mspet$Farmcpc$BF_Score$bumons$me_sat$monslive</font>${H_tagtTH}</td>
</tr>
END
    }
    # ��ξ��� �롼�פ����ޤ�

    out(<<END);
</table>
</div>
END
    out("<hr>");
    hcPrint();
    JoinAllyforAdmin();
}


#----------------------------------------------------------------------
#
#   Ʊ���������ͤΤ�
sub JoinAllyforAdmin {

    out(<<END) if (ADMIN_JOIN_ONLY);
<hr>
<div align="right">
  <form action="$HthisFile" method="POST" style="margin : 2px 0px;">
    <input type="hidden" name="Join" value="0">
    <input type="password" name="PASSWORD" size="16" maxlength="16">
    <input type="submit" name="submit" value="������">
  </form>
</div>
END
}


#----------------------------------------------------------------------
sub PrintWorldStat {

    out(<<END);
<h2 class="subtitle">����</h2>
<b>(��)���ڡ����ǥ֥ꡧ$HSpace_Debris</b>
<hr>
END
}


#----------------------------------------------------------------------
# Hakoniwa Cup��ɽ��
#----------------------------------------------------------------------
sub hcPrint {

    out(<<END);
<h2 class="subtitle">
  <a href="$HthisFile?HCdata=0" target="_blank">Hakoniwa Cup $hcturn</a>
</h2>
<div class='NoWarp' style="overflow:auto; height:${HdivHeight2}px;">
END

    open(CIN, "${HdirName}/hakojima.lhc");
    my (@line, $l);
    my ($output) = '';

    while ($l = <CIN>) {
        chomp($l);
        $l =~ /^([0-9]*),(.*)$/;
        $output = ${HtagNumber_}.'������'.${1} . ${H_tagNumber}. '��' . ${2} . "<br>\n" . $output;
    }
    #   @line = reverse(@line);
    #
    # foreach $l (@line) {
    #    $l =~ /^([0-9]*),(.*)$/;
    #    out("${HtagNumber_}������${1}${H_tagNumber}��${2}<BR>\n");
    # }

    out($output);
    close(CIN);
    out("</div>");
}


#----------------------------------------------------------------------
sub historySpace {

    out(<<END);
<div id='HistoryLog' class="topblock M">
  <h2 class="subtitle">ȯ���ε�Ͽ</h2>
  <div class="topHistoryLog">
END
  historyPrint();
  out(<<END);
  </div>
</div>
END

}


#----------------------------------------------------------------------
# ��Ͽ�ե�����ɽ��
#----------------------------------------------------------------------
sub historyPrint {

    my ($output) = '';
    open(HIN, "${HdirName}/hakojima.his");
    my (@line, $l);
    while ($l = <HIN>) {
        chomp($l);
    #   push(@line, $l);
        $l =~ /^([0-9]*),(.*)$/;
        $output = "${HtagNumber_}������${1}${H_tagNumber}��${2}<br>\n" . $output;
    }
    # @line = reverse(@line);

    out("$output");
    close(HIN);
}


#----------------------------------------------------------------------
# Ʊ���ξ���
#----------------------------------------------------------------------
sub amityOfAlly() {
    # ����
    unlock();

    my ($ally) = $Hally[$HidToAllyNumber{$HallyID}];
    my ($allyName) = "<font color=\"$ally->{'color'}\"><B>$ally->{'mark'}</B></FONT>$ally->{'name'}";

    out(<<END);
<p align='center'>$HtempBack</p>
<div id='campInfo'>
<h1>$allyName�ξ���</h1>
END

    allyInfo($HallyID) if ($ally->{'number'});

    my ($mStr1) = '';
    if (INIT_HIDE_MONEY_MODE) {

        $mStr1 = "<th $HbgTitleCell align='center'>${HtagTH_}���${H_tagTH}</th>";
        $col++;
    }

    my ($msStr1) = '';
    if (INIT_HIDE_MISSILE_MODE) {

        $msStr1 = "<th $HbgTitleCell align='center'>${HtagTH_}�ߥ������";
        $col++;
        if (INIT_USE_ARM_SUPPLY) {

            $msStr1 .= "(����ʪ��)${H_tagTH}</th>";
        }
        else {

            $msStr1 .= "${H_tagTH}</th>";
        }
    }

    if ($ally->{'message'} ne '') {

        my ($allyTitle) = $ally->{'title'};
        my ($allyMessage) = $ally->{'message'};
        $allyTitle = '���礫��Υ�å�����' if ($allyTitle eq '');
        $allyMessage =~ s/([^=^\"]|^)(http\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\%]+)/$1<a href=\"$2\" target='_top'>$2<\/a>/g;
        out(<<END);
<hr>
<table border width="80%">
  <tr><th $HbgTitleCell>${HtagTH_}$allyTitle${H_tagTH}</th></tr>
  <tr><td $HbgInfoCell><blockquote>$allyMessage</blockquote></td></tr>
</table>
END
    }

    out(<<END);
<hr>
<table border><tr>
  <th $HbgTitleCell align='center'>${HtagTH_}���${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}${AfterName}${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}�ݥ����${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}�͸�${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}����${H_tagTH}</th>
  $mStr1
  <th $HbgTitleCell align='center'>${HtagTH_}����${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}���쵬��${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}���쵬��${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}�η��쵬��${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}��������${H_tagTH}</th>
  $msStr1
</tr>
END
    out("<tr><th colspan=$col>��°���Ƥ����礬����ޤ���</th></tr>") if (!$ally->{'number'});

    my ($id, $number, $island, $factory, $mountain, $farm, $name, $mStr2, $msStr2);
    foreach (@{$ally->{'memberId'}}) {

        $id = $_;
        $number = $HidToNumber{$id};
        $island = $Hislands[$number];
        $number += (1 - $HbfieldNumber);
        $farm = $island->{'farm'};
        $factory = $island->{'factory'};
        $mountain = $island->{'mountain'};
        $farm = ($farm == 0) ? '��ͭ����' : "${farm}0$HunitPop";
        $factory = ($factory == 0) ? '��ͭ����' : "${factory}0$HunitPop";
        $mountain = ($mountain == 0) ? '��ͭ����' : "${mountain}0$HunitPop";
        $name = islandName($island);

        if ($island->{'field'}) {

            $number = '��';
            $name = "${HtagNumber_}${name}${H_tagNumber}";
        }
        elsif (!($island->{'absent'})) {

            $name = "${HtagName_}${name}${H_tagName}";
        }
        else {

            $name = "${HtagName2_}${name}($island->{'absent'})${H_tagName2}";
        }
        $name = '<span class="attention">�ڴ����ͤ��������</span><BR>' . $name if ($island->{'predelete'});

        $mStr2 = '';
        if (INIT_HIDE_MONEY_MODE == 1) {

            $mStr2 = "<td $HbgInfoCell align=right>$island->{'money'}$HunitMoney</td>";
        }
        elsif (   (INIT_HIDE_MONEY_MODE == 2)
               || (INIT_HIDE_MONEY_MODE == 3)) {

            my ($mTmp) = aboutMoney($island->{'money'});
            $mStr2 = "<td $HbgInfoCell align=right>$mTmp</td>";
        }

        $renae = int($island->{'rena'} / 10 );
        $msStr2 = '';
        if (INIT_HIDE_MISSILE_MODE) {

            $msStr2 = "<td $HbgInfoCell align=right>$island->{'missiles'}${HunitMissile}";
            if (INIT_HIDE_MISSILE_MODE == 2) {

                my ($mTmp) = aboutMissile($island->{'missiles'});
                $msStr2 = "<td $HbgInfoCell align=right>${mTmp}</td>";
            }
            elsif (INIT_USE_ARM_SUPPLY) {

                $msStr2 .= "($island->{'army'}��)</td>";
            }
            else {
                $msStr2 .= '</td>';
            }
        }

    out(<<END);
<tr>
  <td $HbgNumberCell align="center">${HtagNumber_}$number${H_tagNumber}</td>
  <td $HbgNameCell align="left">
    <a style=\"text-decoration:none\" href="${HthisFile}?Sight=${id}">$name</a>
  </td>
  <td class="TopInfoCell" align="right">$island->{'pts'}</td>
  <td class="TopInfoCell" align="right">$island->{'pop'}$HunitPop</td>
  <td class="TopInfoCell" align="right">$island->{'area'}$HunitArea</td>
  $mStr2
  <td class="TopInfoCell" align="right">$island->{'food'}$HunitFood</td>
  <td class="TopInfoCell" align="right">$farm</td>
  <td class="TopInfoCell" align="right">$factory</td>
  <td class="TopInfoCell" align="right">$mountain</td>
  <td class="TopInfoCell" align="right">Lv$renae</td>
  $msStr2
</tr>
END
    }

    out(<<END);
</table>
END
}


#----------------------------------------------------------------------
# Ʊ���ξ���
#----------------------------------------------------------------------
sub AllyMakeButton() {

    if ($HallyNumber) {

        allyInfo(-1);
        my ($aStr) = ($HarmisticeTurn) ? '�ر�' : 'Ʊ��';
        my ($l_comment) = '';
        $l_comment = "��${HallyTopName}���̾�����ȡ֥������ѹ������" if (!$HarmisticeTurn);
        out(<<END);
��<span class='Nret'><b>��</b>${aStr}��̾���򥯥�å������</span><span class='Nret'>��${aStr}�ξ�������
$l_comment
��ư���ޤ���</span>
END
    }
}


#----------------------------------------------------------------------
# Ʊ���ξ���
#----------------------------------------------------------------------
sub allyInfo() {
    my ($num) = @_;

    my ($aStr) = ($HarmisticeTurn) ? '�ر�' : 'Ʊ��';

    if ($num == -1) {
        out(<<END);
<div class='campInfo'>
  <h2 class="subtitle">��Ʊ���ξ���</h2>
END
    }

    out(<<END);
  <p>��ͭΨ�ϡ�<b>�ݥ����</b>�ˤ�껻�Ф��줿��ΤǤ���</p>
  <p>[<a href="$HthisFile?JoinA=0">������Ʊ���κ���</a>]</p>
  <table class="top_ary" border>
    <thead class="sc">
      <tr>
        <th class='TitleCell nm' align='center'>${HtagTH_}��<br>��${H_tagTH}</th>
        <th class='TitleCell dd' align='center'>${HtagTH_}${aStr}${H_tagTH}</th>
        <th class='TitleCell ee' align='center'>${HtagTH_}�ޡ���${H_tagTH}</th>
        <th class='TitleCell ee' align='center'>${HtagTH_}${AfterName}�ο�${H_tagTH}</th>
        <th class='TitleCell ee' align='center'>${HtagTH_}�ݥ����${H_tagTH}</th>
        <th class='TitleCell ee' align='center'>${HtagTH_}��ͭΨ${H_tagTH}</th>
        <th class='TitleCell ee' align='center'>${HtagTH_}��ȯ��${H_tagTH}</th>
        <th class='TitleCell ee' align='center'>${HtagTH_}������${H_tagTH}</th>
        <th class='TitleCell dd' align='center'>${HtagTH_}GNP${H_tagTH}</th>
      </tr>
    </thead>
    <tbody class="sb">
END

    my ($row);
    my ($name);
    my ($comment);
    my ($ally);
    my ($n);

    foreach (0..($HallyNumber - 1)) {

        if (   ($num != -1)
            && ($_ != $HidToAllyNumber{$num})) {
            next;
        }

        $n = $_ + 1;
        $ally = $Hally[$_];
        my ($missileOut) = ($ally->{'ext'}[0] == 0) ? '�ʤ�' : "$ally->{'ext'}[0]ȯ";
        my ($missileIn) = ($ally->{'ext'}[1] == 0) ? '�ʤ�' : "$ally->{'ext'}[1]ȯ";
        my ($gnp) = "$ally->{'ext'}[2]${HunitMoney}";
        my ($owner) = $HidToNumber{$ally->{'id'}};

        $row = 2;
        if (defined $owner) {

            $owner = islandName($Hislands[$owner]);
        }
        else {

            $row = 1;
        }

        if ($num == -1) {

            $name = "<A style=\"text-decoration:none\" href=\"$HthisFile?AmiOfAlly=$ally->{'id'}\">$ally->{'name'}</A>";
        }
        else {

            $name = $ally->{'name'};
        }
        $comment = $ally->{'comment'};
        out(<<END);
  <tr>
    <td class='NumberCell nm' rowspan='$row' align='center'>${HtagNumber_}$n${H_tagNumber}</td>
    <td class='InfoCell dd' rowspan='$row' align='center'>$name</td>
    <td class='InfoCell ee' align='center'><b><font color="$ally->{'color'}">$ally->{'mark'}</font></b></td>
    <td class='InfoCell ee' align='right'>$ally->{'number'}${AfterName}</td>
    <td class='InfoCell ee' align='right'>$ally->{'score'}</td>
    <td class='InfoCell ee' align='right'>$ally->{'occupation'}\%</td>
    <td class='InfoCell ee' align='right'>$missileOut</td>
    <td class='InfoCell ee' align='right'>$missileIn</td>
    <td class='InfoCell dd' align='right'>$gnp</td>
  </tr>
END
        out(<<END) if ($row == 2);
  <tr>
    <td $HbgCommentCell colspan='7'><a style='text-decoration:none' href='$HthisFile?Allypact=$ally->{'id'}'>${owner}</a>��$comment</td>
  </tr>

END
    }

    out("    </tbody>\n  </table>");
    out('</div>') if ($num == -1);
}

1;
