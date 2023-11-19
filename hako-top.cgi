#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# トップモジュール(ver1.00)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# Hakoniwa R.A. ver2.11
# メインスクリプト(箱庭諸島 ver2.30)
# 使用条件、使用方法等は、read-renas.txtファイルを参照
#
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------
require './hako-landinfo.cgi';
require './server_config.pm';
#----------------------------------------------------------------------
# トップページモード
#----------------------------------------------------------------------
# メイン
sub topPageMain {
    # アクセス・ログ
    axeslog() if ($HtopAxes == 2);
    # 開放
    unlock();

    # テンプレート出力
    tempTopPage();
}

#----------------------------------------------------------------------
#
#   デバッグ用
sub DebugButtonPrint {

    if (DEBUG_MODE) {
        out(<<END);
    <form action="$HthisFile" method="POST">
      <input type="submit" value="ターンを進める" name="TurnButton">
    </form>
END
    }
}


#----------------------------------------------------------------------
sub PrintTopMenuLink {

    my ($output);

    $output = "<div class='TopMenuLink'>\n";

    if (!(ADMIN_JOIN_ONLY)) {

        $output .= "[<a class='Nret' href='$HthisFile?Join=0'>新しい${AfterName}を探す</a>] \n";
    }
    else {

        $output .= (qq|<b>※</b>新しい${AfterName}を探したい方は「<b>${AfterName}名、あなたの名前、パスワード</b>」を管理人までメールしてください。<br>|);
    }
    $output .= (qq|<span class='Nret'>[<a href="$HthisFile?Rename=0">${AfterName}の名前とパスワードの変更</a>]</span> |);

    #out(qq|[<A href="$HthisFile?JoinA=0">同盟の設定</A>] |) if(($HallyUse == 1) );
    if (   (USE_GZIP)
        || (!(USE_HTML_LOG_MDOE))
        || (!(-e "${HhtmlDir}/hakolog.html")) ) {

        $output .= (qq|[<a class='Nret' href="${HbaseDir}/history.cgi?Event=0" target="_blank">最近の出来事</a>] |);
    }
    else {

        $output .= (qq|[<a class='Nret' href="${htmlDir}/hakolog.html" target="_blank">最近の出来事</a>] |);
    }

    out(<<END);
  $output
  [<a class='Nret' href="$HthisFile?Rekidai=0" target="_blank">歴代最多人口記録</a>] 
  [<a class='Nret' href="$HthisFile?Rank=0" target="_blank">ランキング</a>] 
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
# サイトメニュー
#----------------------------------------------------------------------
sub TopSiteMenu {

    my (@URL_Table) = (
        [ "miniverse" , "../frm/viewforum.php?f=4"],
        [ "マニュアル", "http://minimal97.com/wiki/"],
    );

    my ($tbl_cnt) = (@URL_Table >> 1) + 1;        # table / 2 する
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
            $outtext .= "<a title='$title' href='$adr' target='_blank' class='Nret'>$title</a>　";
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

    my ($news_rand) = random(100);      # キャッシュ用

    out(<<END);
  <div class='topblock'>
    <h2 class='subtitle'>ニュース用</h2>まずは、要望があれば、miniverseに記載してください。<span class='Nret'><a target='_blank' href='http://minimal97.com/wiki/index.php?%BD%A4%C0%B5%B3%D0%BD%F13'>さらに細かいメモ</a></span><br>
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

    # java モードか、 cgiモードか
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
    <h2 class='subtitle'>自分の${AfterName}へ</h2>
    <form name="Island" action="$HthisFile" method="post">
      あなたの${AfterName}の名前は？<br>
      <select name="ISLANDID">
          $HislandList
      </select><br><br>
      パスワードをどうぞ！！<br>
      <input type="hidden" name="OwnerButton">
      <input type="text" name="PASSWORD" value="$HdefaultPassword" size="32" maxlength="32"><br>
      <input type="radio" name="JAVAMODE" value="cgi"  $radio>CGIモード
      <input type="radio" name="JAVAMODE" value="java" $radio2>Javaスクリプトモード<br>
      <input type="submit" value="開発しに行く">　　　
      <input type="button" value="新しい画面" onClick="newdevelope()">
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
    <span class='Nret'>新規のかたは、</span>
    <span class='Nret'>[新しい${AfterName}を探す]から!!</span>
  </small>
</h2>
<div style="display:block;">
  <div class="topblock">
END

    # デバッグモードなら「ターンを進める」ボタン
    DebugButtonPrint();

    # 終了ターン数と終了日時を表示
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
            $HlimitTime = sprintf('%d年 %d月 %d日 %d時', (gmtime($HlimitTime + $Hjst))[5] + 1900, (gmtime($HlimitTime + $Hjst))[4] + 1, (gmtime($HlimitTime + $Hjst))[3,2]);
            $HlastTurnS = "<small>／${HgameLimitTurn}<small>《${HlimitTime}まで》</small></small>";
        }
    }
    else {

        $HlastTurnS = '　（ゲームは終了しました）';
    }

    TopSiteMenu();

    # <a title="箱庭共通マップＮ" href="../hako_k" target="_blank" class='Nret'>箱庭共通マップN</a>

    # 現在のターンを表示
    #my ($mode) = '';
    #$mode = ($HislandTurn < $HarmisticeTurn) ? "(〜$HarmisticeTurn <small>停戦期間</small>)" : ($HislandTurn == $HarmisticeTurn) ? '(<small>次ターンより戦闘期間</small>)' : '(<small>戦闘期間</small>)' if($HarmisticeTurn);
    out('    <div class="Turn">');
    #季節は無し $Hseason
    out(qq|<h2 class="subtitle"><small>ターン</small> ${HislandTurn}<small>${HlastTurnS}</small></h2></div>\n|);

    # 飾り
    {
        my ($i);
        my ($str_sq) = '';
        my ($real) = ($HislandTurn + 8) % 12 ;
        for ($i = 0 ; $i < 12; $i++) {

            $str_sq .= ($i == $real) ? '■' : '□';
        }
        out($str_sq);
    }

    # 次回更新時間表示
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
        $sss = "$mon月 $day日 $hour時 $min分 $sec秒";
        $mon2++;
    }

    my ($bbb) = '';
    if (   ($HgameLimitTurn == 0)
        || ($HislandTurn < $HgameLimitTurn) ) {

        $bbb = "${mon2}月 ${date2}日 ${hour2}時 ${min2}分";
    }
    else {

        $bbb = '更新は停止しています';
    }

    # 次のターンまでの時間表示
    if (   !($HmainMode eq 'turn')
        && (defined $HleftTime) ) {

        $hour2 = int($HleftTime/3600);
        $min2 = int(($HleftTime-$hour2*3600)/60);
        $sec2 = ($HleftTime-$hour2*3600-$min2*60);
        $rtStr = "次の更新時間まであと $hour2時間 $min2分 $sec2秒";
    }
    else {

        if ($HplayNow) {

            $rtStr = "ターンを更新しました\n";
        }
        else {

            $rtStr = '';
        }
    }

# リアルタイマー
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
    document.frm_TIME.TIME.value = '次の更新時間まであと ' + hour + '時間 ' + min + '分 ' + sec + '秒';
  }
  else {
    document.frm_TIME.TIME.value = 'ターン更新時刻になりました！ ($HnextTime)';
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
    # フォーム
    out(<<END);
    <p id="nexttime">
        現在の時間：<b>$sss</b><br>（次回の更新時間：$bbb）
    </p>
    <span class="rednews">ターン更新付近での更新連打は控えてください。<br>島データが壊れます。<br>せめて30秒は待ってください。<br>
島の作成はひとり、１島までです。<br>同じIPアドレスが割り当てられた島を見つけたら、沈めます。</span>
  </div>
END

    tempNewsspace();

    out(<<END);
</div>
END
}


#----------------------------------------------------------------------
# トップページ
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
    <h2 class="subtitle">諸${AfterName}の状況</h2>
    <span class='Nret'>${AfterName}の名前をクリックすると、</span>
    <span class='Nret'><b>観光</b>することができます。</span>
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
                $j = '★' if (!$ii && $HbfieldNumber);

                out(qq|<a href="$HthisFile?View=$ii#View">${HtagNumber_}[$j〜$k]${H_tagNumber}</a>&nbsp;|);
            }
        }
    }

    my ($mStr1) = '';
    if (INIT_HIDE_MONEY_MODE) {
        $mStr1 = "  <th $HbgTitleCell align='center'>${HtagTH_}資金${H_tagTH}</th>";
    }

    my ($msStr1) = '';
    if (INIT_HIDE_MISSILE_MODE) {
        $msStr1 = "  <th $HbgTitleCell align='center'>${HtagTH_}ミサイル数";
        if (INIT_USE_ARM_SUPPLY) {

            $msStr1 .= "(軍事物資)${H_tagTH}</th>";
        }
        else {
            $msStr1 .= "${H_tagTH}</th>";
        }
    }

    out('<table border>');

    my ($head);
    $head = <<"END";
<tr>
  <th $HbgTitleCell align="center">${HtagTH_}順<br>位${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}${AfterName}${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}天候${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}人口${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}面積${H_tagTH}</th>
$mStr1
  <th $HbgTitleCell align="center">${HtagTH_}食料${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}農場${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}職場${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}ハイテク<br>職場${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}採掘場${H_tagTH}</th>
  <th $HbgTitleCell align="center">${HtagTH_}軍事<br>技術${H_tagTH}</th>
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
    my @uniName = ( '[天使ミカエル]',
                    '[首都]',
                    '[壊れた侵略者]',
                    '[王蟲の脱け殻]',
                    '[闇石]',
                    '[地石]',
                    '[氷石]',
                    '[風石]',
                    '[炎石]',
                    '[光石]',
                    '[古代遺跡]',
                    '[幸福の女神像]',
                    '[200億で油田の碑]'
                                            );

    my ($ssss);             # スタジアム情報
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
        $farm       = (!$farm) ? "保有せず" : ${farm}.'0'.$HunitPop;
        $factory    = (!$factory) ? "保有せず" : "${factory}0$HunitPop";
        $factoryHT  = (!$factoryHT) ? "保有せず" : "${factoryHT}0$HunitPop";
        $mountain   = (!$mountain) ? "保有せず" : "${mountain}0$HunitPop";
        $renae      = int($island->{'rena'} / 10 );
        $pts        = $island->{'pts'};
        $eisei2     = $island->{'eisei2'};
        $eisei2nd   = int($eisei2 / 100 );

        $weather    = $island->{'weather_old'};
        $w_tag      = "<img src='./img/weather/weather$weather.gif' alt=''>";

        $eisei2     = ($eisei2nd == 0) ? '通算観光者数１万人未満<br>' : '通算観光者数'.$eisei2nd.'万人<br>';

        $absent = $island->{'absent'};

        $name = islandName($island);

        $BF_Flag    = isBattleField($island);

        if ($BF_Flag) {

            $j = '★';
            $name = ${HtagNumber_}. $name. ${H_tagNumber};
        }
        elsif ($absent == 0) {

            $name = ${HtagName_}.$name.${H_tagName};
        }
        else {

            $name = ${HtagName2_} . $name . '('.$absent.')' . ${H_tagName2} ;
        }
        $name = '<span class="attention">【管理人あずかり】</span><br>' . $name if ($island->{'predelete'});

        $bumons = '';
        $prize = '';
        $BF_Score = '';
        $me_sat = '';
        $ssss = '';
        # バトルフィールドでは表示しない。
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

            $ino = ($island->{'inoraland'}) ? "<img src=\"${HStatImgDir}inoraland.gif\" alt='' title=\"いのらランド\" class='landinfoIcon'>" : '';
            $zooicon = ($island->{'zoo_Mons_cnt'}) ? "<img src=\"${HStatImgDir}land84.gif\" alt='' title=\"動物園 $island->{'zoo_Mons_cnt'}匹\" class='landinfoIcon'>" : '';

            my ($rt) = "\n";
            $unique = '';
            if ($island->{'uni'}) {

                $unique = "<span class='shuto'><img src=\"./img/prize/prize10.svg\" alt='' title=\"入手の難しいユニーク地形：$rt${unilist}／全$uniNum種類\" ";
                $unilist =~ s/$rt//g;
                $unique .= "class='landinfoIcon'> $island->{'tuni'}ヶ所 </span>";
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

                $nn = ($nn eq '') ? '練習中' : $HStadiumResult[$stshoka] ;

                if ($stshoka >= 1) {

                    $ssss = "<img src=\"./img/sc.gif\" title=\"".$nn.' 攻('.$sto.')守('.$std.')KP('.$stk.')'.$rt.'チーム成績 勝点' . $island->{'kachiten'} .'/ '.$stwin.'勝'.$stlose.'敗'.$stdrow.'分'.$rt." / 通算$stwint勝$stloset敗$stdrowt分 / 優勝$styusho回\" alt='' class='landinfoIcon'> "
                }
                elsif ($stshoka == 0) {

                    $ssss = '';
                }
            }

            {
                my ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
                my ($force) = $mshp + $msap + $msdp + $mssp;
                $island->{'force'} = $force;
                $mspet = "<img alt='' src=\"${HMapImgDir}ms.gif\" title=\"マスコットいのら" .
                         "(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswin匹撃破/経験値$msexe)\" ".
                         "onMouseOver='status=\"マスコットいのら(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswin匹撃破/経験値$msexe)\"; return true;' ".
                         " class='landinfoIcon'>Sum($force)" if ($mshp);
                $mspet = "<img alt='' src=\"${HMapImgDir}tet.gif\" title=\"超神獣テトラ" .
                         "(HP$mshp.AP$msap.DP$msdp.SP$mssp/$mswin匹撃破/経験値$msexe)\" ".
                         "class='landinfoIcon'>Sum($force)" if ($tet);
                $mspet = '' if (!$mshp && !$tet);
            }

            $bumons = ScoreBoard_Bumon($island);

            $prize = ScoreBoard_Prize($island);         # ターン賞、その他賞
            $prize .= ScoreBoard_Taiji($island);        # 倒した怪獣リスト  怪獣を増やすので、リストは削除

            $BF_Score = ScoreBoard_BF_Point($island);   # バトルフィールドスコア

            $me_sat = ScoreBoard_Eisei($island);        # 人工衛星
        }

        $HbgStatCell = $HbgCommentCell;
        $HbgStatCell = 'class="MonsterCell"' if ($island->{'monsterlive'});

        # 資金
        my ($mStr1) = '';
        if (INIT_HIDE_MONEY_MODE == 1) {

            $mStr1 = "<td class=TopInfoCell align=right>".$island->{'money'}.$HunitMoney.'</td>';
        }
        elsif (   (INIT_HIDE_MONEY_MODE == 2)
               || (INIT_HIDE_MONEY_MODE == 3)) {

            my ($mTmp) = aboutMoney($island->{'money'});
            $mStr1 = "  <td class='TopInfoCell' align='right'>$mTmp</td>";
        }

        # ミサイル発射可能数
        $msStr1 = '';
        if (INIT_HIDE_MISSILE_MODE) {

            $msStr1 = "<td class='TopInfoCell' align='right'>$island->{'missiles'}${HunitMissile}";
            if (INIT_HIDE_MISSILE_MODE == 2) {

                my ($mTmp) = aboutMissile($island->{'missiles'});
                $msStr1 = "<td class='TopInfoCell' align='right'>${mTmp}</td>";
            }
            elsif (INIT_USE_ARM_SUPPLY) {

                $msStr1 .= "($island->{'army'}個)</td>";
            }
            else {

                $msStr1 .= '</td>';
            }
        }

        {
            my ($comment_tag);
            if ($island->{'onm'} eq '') {

                $comment_tag = "${HtagTH_}コメント : ${H_tagTH}";
            }
            else {

                $comment_tag = "${HtagLbbsSS_}$island->{'onm'} : ${H_tagLbbsSS}";
            }
            $oStr = "<td $HbgTotoCell colspan='$col1' align='left'>${comment_tag}$island->{'comment'}</td>";
        }

        my ($house) = '';

        $Farmcpc = '';
        if (!$BF_Flag) {
                                                                        # 牧場系
            $Farmcpc = ScoreBoard_Farm($island);
                                                                        # 家
            {
                my ($eisei1) = $island->{'eisei1'};

                if ($eisei1) {

                    $hlv = Calc_HouseLevel($pts);

                    my ($onm) = $island->{'onm'};
                    my ($n) = "の$HHouseName[$hlv]";
                    my ($zeikin) = int($pop * ($hlv + 1) * $eisei1 / 100);
                    $house .= "<span class='house'><img src=\"${HMapImgDir}house${hlv}.gif\" alt='' title=\"$onm$n\" class='landinfoIcon'>税率$eisei1％($zeikin$HunitMoney)</span>"
                }
                else {

                    $house = '';
                }
            }
            # 首都名
            my ($top_shutomsg) = $island->{'shutomessage'};
            $shutoname = ($top_shutomsg == 555) ? '' : "<font size='-1'><span class='shuto'>首都：".$top_shutomsg.'</span></font><br>';
        }

        # 出現中の怪獣リスト
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
    <font size="-1">失業率</font>:($unemployed)<br>
    <span class="eisei"><font size="-1">$eisei2</font></span>
  </div>
</td>
END
        }
        else {

            $msStr1 = "<td ${HbgInfoCell} align='right'>−</td>" if (INIT_HIDE_MISSILE_MODE);
            $oStr = "<td $HbgTotoCell colspan='$col1' align='left'>${HtagLbbsSS_}$server_config::HadminName${H_tagLbbsSS} : $island->{'comment'}</td>";
            out(<<END);
<th $HbgNameCell rowspan="4" align="left">
  <div class="t_center">
    <a style=\"text-decoration:none\" href="${HthisFile}?Sight=${id}" title="ID:${id}">$name</a><br><br>
    <a style=\"text-decoration:none\" href="${HthisFile}?BF_point=0">${HtagTH_}<u>Battle Field戦績</u>${H_tagTH}</a>
  </div>
</th>
END
        }
        $areatag = (!$island->{'area'}) ? '0坪' : $island->{'area'}.$HunitArea;
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
  <td $HbgTotoCell colspan="5" align="left">${HtagtTH_}看板1：${H_tagtTH}$island->{'totoyoso'}->[0]</td>
  <td $HbgTotoCell colspan="$col" align="left">${HtagtTH_}看板2：${H_tagtTH}$island->{'totoyoso'}->[1]</td>
</tr>
<tr>
  $oStr
</tr>
<tr>
  <td $HbgStatCell colspan="$col1" align="left">${HtagtTH_}<font size="-1">$prize$ino$zooicon$ssss$unique$house$mspet$Farmcpc$BF_Score$bumons$me_sat$monslive</font>${H_tagtTH}</td>
</tr>
END
    }
    # 島の情報 ループここまで

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
#   同盟操作、管理人のみ
sub JoinAllyforAdmin {

    out(<<END) if (ADMIN_JOIN_ONLY);
<hr>
<div align="right">
  <form action="$HthisFile" method="POST" style="margin : 2px 0px;">
    <input type="hidden" name="Join" value="0">
    <input type="password" name="PASSWORD" size="16" maxlength="16">
    <input type="submit" name="submit" value="管理用">
  </form>
</div>
END
}


#----------------------------------------------------------------------
sub PrintWorldStat {

    out(<<END);
<h2 class="subtitle">状況</h2>
<b>(仮)スペースデブリ：$HSpace_Debris</b>
<hr>
END
}


#----------------------------------------------------------------------
# Hakoniwa Cupログ表示
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
        $output = ${HtagNumber_}.'ターン'.${1} . ${H_tagNumber}. '：' . ${2} . "<br>\n" . $output;
    }
    #   @line = reverse(@line);
    #
    # foreach $l (@line) {
    #    $l =~ /^([0-9]*),(.*)$/;
    #    out("${HtagNumber_}ターン${1}${H_tagNumber}：${2}<BR>\n");
    # }

    out($output);
    close(CIN);
    out("</div>");
}


#----------------------------------------------------------------------
sub historySpace {

    out(<<END);
<div id='HistoryLog' class="topblock M">
  <h2 class="subtitle">発見の記録</h2>
  <div class="topHistoryLog">
END
  historyPrint();
  out(<<END);
  </div>
</div>
END

}


#----------------------------------------------------------------------
# 記録ファイル表示
#----------------------------------------------------------------------
sub historyPrint {

    my ($output) = '';
    open(HIN, "${HdirName}/hakojima.his");
    my (@line, $l);
    while ($l = <HIN>) {
        chomp($l);
    #   push(@line, $l);
        $l =~ /^([0-9]*),(.*)$/;
        $output = "${HtagNumber_}ターン${1}${H_tagNumber}：${2}<br>\n" . $output;
    }
    # @line = reverse(@line);

    out("$output");
    close(HIN);
}


#----------------------------------------------------------------------
# 同盟の情報
#----------------------------------------------------------------------
sub amityOfAlly() {
    # 開放
    unlock();

    my ($ally) = $Hally[$HidToAllyNumber{$HallyID}];
    my ($allyName) = "<font color=\"$ally->{'color'}\"><B>$ally->{'mark'}</B></FONT>$ally->{'name'}";

    out(<<END);
<p align='center'>$HtempBack</p>
<div id='campInfo'>
<h1>$allyNameの情報</h1>
END

    allyInfo($HallyID) if ($ally->{'number'});

    my ($mStr1) = '';
    if (INIT_HIDE_MONEY_MODE) {

        $mStr1 = "<th $HbgTitleCell align='center'>${HtagTH_}資金${H_tagTH}</th>";
        $col++;
    }

    my ($msStr1) = '';
    if (INIT_HIDE_MISSILE_MODE) {

        $msStr1 = "<th $HbgTitleCell align='center'>${HtagTH_}ミサイル数";
        $col++;
        if (INIT_USE_ARM_SUPPLY) {

            $msStr1 .= "(軍事物資)${H_tagTH}</th>";
        }
        else {

            $msStr1 .= "${H_tagTH}</th>";
        }
    }

    if ($ally->{'message'} ne '') {

        my ($allyTitle) = $ally->{'title'};
        my ($allyMessage) = $ally->{'message'};
        $allyTitle = '盟主からのメッセージ' if ($allyTitle eq '');
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
  <th $HbgTitleCell align='center'>${HtagTH_}順位${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}${AfterName}${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}ポイント${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}人口${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}面積${H_tagTH}</th>
  $mStr1
  <th $HbgTitleCell align='center'>${HtagTH_}食料${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}農場規模${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}工場規模${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}採掘場規模${H_tagTH}</th>
  <th $HbgTitleCell align='center'>${HtagTH_}軍事技術${H_tagTH}</th>
  $msStr1
</tr>
END
    out("<tr><th colspan=$col>所属している島がありません！</th></tr>") if (!$ally->{'number'});

    my ($id, $number, $island, $factory, $mountain, $farm, $name, $mStr2, $msStr2);
    foreach (@{$ally->{'memberId'}}) {

        $id = $_;
        $number = $HidToNumber{$id};
        $island = $Hislands[$number];
        $number += (1 - $HbfieldNumber);
        $farm = $island->{'farm'};
        $factory = $island->{'factory'};
        $mountain = $island->{'mountain'};
        $farm = ($farm == 0) ? '保有せず' : "${farm}0$HunitPop";
        $factory = ($factory == 0) ? '保有せず' : "${factory}0$HunitPop";
        $mountain = ($mountain == 0) ? '保有せず' : "${mountain}0$HunitPop";
        $name = islandName($island);

        if ($island->{'field'}) {

            $number = '★';
            $name = "${HtagNumber_}${name}${H_tagNumber}";
        }
        elsif (!($island->{'absent'})) {

            $name = "${HtagName_}${name}${H_tagName}";
        }
        else {

            $name = "${HtagName2_}${name}($island->{'absent'})${H_tagName2}";
        }
        $name = '<span class="attention">【管理人あずかり】</span><BR>' . $name if ($island->{'predelete'});

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

                $msStr2 .= "($island->{'army'}個)</td>";
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
# 同盟の状況
#----------------------------------------------------------------------
sub AllyMakeButton() {

    if ($HallyNumber) {

        allyInfo(-1);
        my ($aStr) = ($HarmisticeTurn) ? '陣営' : '同盟';
        my ($l_comment) = '';
        $l_comment = "、${HallyTopName}島の名前だと「コメント変更」欄へ" if (!$HarmisticeTurn);
        out(<<END);
　<span class='Nret'><b>※</b>${aStr}の名前をクリックすると</span><span class='Nret'>「${aStr}の情報」欄へ
$l_comment
移動します。</span>
END
    }
}


#----------------------------------------------------------------------
# 同盟の状況
#----------------------------------------------------------------------
sub allyInfo() {
    my ($num) = @_;

    my ($aStr) = ($HarmisticeTurn) ? '陣営' : '同盟';

    if ($num == -1) {
        out(<<END);
<div class='campInfo'>
  <h2 class="subtitle">各同盟の状況</h2>
END
    }

    out(<<END);
  <p>占有率は、<b>ポイント</b>により算出されたものです。</p>
  <p>[<a href="$HthisFile?JoinA=0">加盟、同盟の作成</a>]</p>
  <table class="top_ary" border>
    <thead class="sc">
      <tr>
        <th class='TitleCell nm' align='center'>${HtagTH_}順<br>位${H_tagTH}</th>
        <th class='TitleCell dd' align='center'>${HtagTH_}${aStr}${H_tagTH}</th>
        <th class='TitleCell ee' align='center'>${HtagTH_}マーク${H_tagTH}</th>
        <th class='TitleCell ee' align='center'>${HtagTH_}${AfterName}の数${H_tagTH}</th>
        <th class='TitleCell ee' align='center'>${HtagTH_}ポイント${H_tagTH}</th>
        <th class='TitleCell ee' align='center'>${HtagTH_}占有率${H_tagTH}</th>
        <th class='TitleCell ee' align='center'>${HtagTH_}弾発射${H_tagTH}</th>
        <th class='TitleCell ee' align='center'>${HtagTH_}弾飛来${H_tagTH}</th>
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
        my ($missileOut) = ($ally->{'ext'}[0] == 0) ? 'なし' : "$ally->{'ext'}[0]発";
        my ($missileIn) = ($ally->{'ext'}[1] == 0) ? 'なし' : "$ally->{'ext'}[1]発";
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
    <td $HbgCommentCell colspan='7'><a style='text-decoration:none' href='$HthisFile?Allypact=$ally->{'id'}'>${owner}</a>：$comment</td>
  </tr>

END
    }

    out("    </tbody>\n  </table>");
    out('</div>') if ($num == -1);
}

1;
