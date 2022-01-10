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
require ('./hako-landinfo.cgi');
require ('./hako-map_common.cgi');
require ("./html_template.pl");
require ('./hako-trade.cgi');
require ('./server_config.pm');

#----------------------------------------------------------------------
# Ｊａｖａスクリプト開発画面
#----------------------------------------------------------------------
# ヘッダ
sub tempHeaderJava {

    $baseIMG = $server_config::HimageDir;
    $baseSKIN = "${efileDir}/$HcssFile";
    $seasonIMG = '';

    my ($mapsizeNumber) = $HidToNumber{$defaultID};

    Print_MIMEtype();

    out(<<END);
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=EUC-JP">
  <meta http-equiv="Content-Script-Type" content="text/javascript">
END
    if ($HmainMode eq 'landmap') {
       # print "<meta name='viewport' content='width=device-width,initial-scale=1'>" ;
    }
    else {
        #print '<meta name="viewport" content="width=device-width,initial-scale=1">' ;
    }
    out(<<END);
  <meta name="theme-color" content="#99FF99">
  <link rel="shortcut icon" href="./img/fav.ico">
  <title>$Htitle $Htitle_sub</title>
  <base href="${baseIMG}/${seasonIMG}">
  <link rel="stylesheet" type="text/css" href="${baseSKIN}">
<!-- 
  <style type="text/css">
img.maptile {
  width: 32px;
  height: 32px;
  border: 0px;
  border-style:hidden;
}
  </style>
-->
</head>
$Body<div id='BodySpecial'>
END

    if (   ($HmainMode eq 'landmap')
        || ($HmainMode eq 'taijilist')
        || ($HmainMode eq 'monument_num')
                                         ) {

    out(<<END);
<p align='center'>
  <a href=\"#\" onclick=\"window.close()\">${HtagBig_}[閉じる]${H_tagBig}</a>
</p>
END
    }
    else {
        html_template::PrintHeader();
    }
}


#----------------------------------------------------------------------
# ○○島開発計画
#----------------------------------------------------------------------
sub tempOwnerJava {
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];

    # コマンドセット
    my ($set_com) = '';
    my ($com_max) = '';
    my ($i);

    for ($i = 0; $i < $HcommandMax; $i++) {
        # 各要素の取り出し
        my ($command) = $island->{'command'}->[$i];
        my ($s_kind, $s_target, $s_x, $s_y, $s_arg) =
            (
                $command->{'kind'},
                $command->{'target'},
                $command->{'x'},
                $command->{'y'},
                $command->{'arg'}
            );

        # コマンド登録
        if ($i == $HcommandMax-1) {
            $set_com .= "\[$s_kind\,$s_x\,$s_y\,$s_arg\,$s_target\]";
            $com_max .= '0';
        }
        else {
            $set_com .= "\[$s_kind\,$s_x\,$s_y\,$s_arg\,$s_target\]\,";
            $com_max .= '0,';
        }
    }

    #コマンドリストセット
    my ($l_kind);
    my ($m);
    my ($set_listcom) = '';
    @click_com[1..7]  = ('', '', '', '', '', '', '');
    my ($All_listCom) = 0;
    my ($bai);
    my ($cmd_lp);

    $com_count = @HcommandDivido2;

    my (@cmd);
    my ($cmdsetnum);

    for ($m = 0; $m < $com_count; $m++) {

        $set_listcom .= "\[ ";

        @cmd = split(/,/,$HcommandDivido2[$m]);
        $cmdsetnum = ($#cmd) + 1;

        for ($cmd_lp = 1 ; $cmd_lp < $cmdsetnum ; $cmd_lp++) {
            $l_kind = $cmd[$cmd_lp];

            # 必要な条件がなければコマンドから除外する
            next if((($l_kind == $HcomSave)||($l_kind == $HcomLoad))&& !($island->{'shr'}));
            next if(($l_kind == $HcomBettown) && ($Hislands[$HcurrentNumber]->{'shutomessage'} == 555));
            next if(($l_kind == $HcomYakusho) && ($Hislands[$HcurrentNumber]->{'shutomessage'} == 555));
            next if(($l_kind == $HcomYakusho) && ($Hislands[$HcurrentNumber]->{'yaku'} > 0));

            # 値段算出
            $l_cost = toCostDisplay($HcomCost[$l_kind] , $island);

            if (isCommandEnable($l_kind)) {
                $set_listcom .= "\[$l_kind\,\'$HcomName[$l_kind]\',\'$l_cost\'\]\,\n";
                if (($m > 0) && ($m < 8)) {
                    $click_com[$m] .= "      <a title='$l_cost' href='javascript:void(0);' onClick='cominput(myForm,6,$l_kind)' style='text-decoration:none'>$HcomName[$l_kind]<font size='-1'>($l_cost)</font></a><br>\n";
#                   $click_com[$m] .= "<a title='$l_cost' href='javascript:void(0);' onClick='cominput(myForm,6,$l_kind)' style='text-decoration:none'>$HcomName[$l_kind]($l_cost)</a><br>\n";
                }
                $All_listCom++;
            }
#           next if($l_kind < $ff+1);
        }
        $bai = length($set_listcom);
        $set_listcom = substr($set_listcom, 0,$bai-2);
        $set_listcom .= " \],\n";
    }

    $bai = length($set_listcom);
    $set_listcom = substr($set_listcom, 0,$bai-2);

    if ($HdefaultKind eq '') {

        $default_Kind = 1;
    }
    else {

        $default_Kind = $HdefaultKind;
    }

    #島リストセット
    my ($set_island, $l_name, $l_id);
    $set_island = "";
    foreach my $i (0..$islandNumber) {

        $l_name = islandName($Hislands[$i]);
        $l_name =~ s/<[^<]*>//g;
        $l_name =~ s/'/\\'/g;
        $l_id = $Hislands[$i]->{'id'};
        if ($i == $islandNumber) {
            $set_island .= "\[$l_id\,\'$l_name\'\]\n";
        }
        else {
            $set_island .= "\[$l_id\,\'$l_name\'\]\,";
        }
    }

    my ($set_monument_tags);
    my ($set_monument_img_tags);
    for ($i = 0; $i <= 95; $i++) {

        if ($i == 95) {

            $set_monument_tags .= "\'$HmonumentName[$i]\'\n";
            $set_monument_img_tags .= "\'${HMapImgDir}$HmonumentImage[$i]\'\n";
        }
        else {

            $set_monument_tags .= "\'$HmonumentName[$i]\'\,";
            $set_monument_img_tags .= "\'${HMapImgDir}$HmonumentImage[$i]\'\,";
        }
    }

    if (EXTRA_JS) {

        unless(-e "${HefileDir}/hakojima.js") {

            require('./hako-js.cgi');
            makeJS(1);
        }
    }

    OwnarMap_Header();

    out(<<END);
<script type="text/javascript">
<!--
// ＪＡＶＡスクリプト開発画面配布元
// あっぽー庵箱庭諸島（ http://appoh.execweb.cx/hakoniwa/ ）
// Programmed by Jynichi Sakai(あっぽー)
// ↑ 削除しないで下さい。
var str;
d_Kind = $default_Kind;
d_ID = $HcurrentID;
All_list = $All_listCom;
g = [$com_max];
k1 = [$com_max];
k2 = [$com_max];
tmpcom1 = [ [0,0,0,0,0] ];
tmpcom2 = [ [0,0,0,0,0] ];
command = [
$set_com];
comlist = [
$set_listcom
];
islname = [
$set_island];
//HmonumentName
monument_tag = [
$set_monument_tags];
monument_img_tag = [
$set_monument_img_tags];
// minimal97 ----------
var map_cmd_chg = false; // 操作は、このmap と jsでしているので注意！
window.onbeforeunload = function(event){
  if(map_cmd_chg){
    event = event || window.event; 
    event.returnValue = '入力中のページから移動しますか？';
  }
}
//-->
</script>
END

    MapCommonScript();

    if (EXTRA_JS) {
        out(<<END);
<script type="text/javascript" src="${efileDir}/hakojima.js"></script>
END
    }
    else {

        require('./hako-js.cgi');
        makeJS(0);
    }

    out(<<END);
<div id="menu" style="position:absolute; visibility:hidden;">
  <table BORDER=0 class="PopupCell">
  <tr>
    <td class='T' colspan=2>
      <form name='POPUP'>
        <img name="NAVIIMG" alt='' src="" class='maptile' align="left">
        <textarea style="font-size:0.8em;" NAME="COMSTATUS" cols="48" rows="3" class="popupnavi" style="resize:none;"></textarea>
      </form>
    </td>
  </tr>
  <tr>
    <td>
$click_com[1]<hr>
$click_com[2]<hr>
$click_com[7]
    </td>
    <td>
$click_com[3]<hr>
$click_com[5]<hr>
$click_com[4]<hr>
$click_com[6]
    </td>
  </tr>
  <tr>
    <td colspan=2>
<a href="Javascript:void(0);" onClick="menuclose()" STYlE="text-decoration:none">メニューを閉じる</a>
    </td>
  </tr>
</table>
</div>
END

    islandInfo(1);

    out(<<END);
<!-- # 追加（JS版 ver2.0）ＩＥ６対応----- -->
<center>
<!-- -ここまで---------------------------- -->
        <center>
          <table border>
            <tr valign=top>
              <td $HbgInputCell>
                <center>
                  <form name="myForm" action="$HthisFile" method="POST">
<b>計画番号</b>
                    <select name='NUMBER'>
END
    # 計画番号
    Plan_number();

    {
        my ($open);
        $open = ($HmenuOpen eq 'checked') ? 'checked' : '';

        out(<<END);
                    </select><br>
<hr>
<b>開発計画</b>
                    <input type="checkbox" name="MENUOPEN"onClick="check_menu()" $open>非表示<br>
                    <select name=menu onchange="SelectList(myForm)">
                      <option value=>全種類
END
    }

    {
        my ($aa);
        my ($t_list);
        for ($i = 0; $i < $com_count; $i++) {

            ($aa) = split(/,/,$HcommandDivido2[$i]);
            $t_list .= ("                      <option value=$i>$aa\n");
        }
        out($t_list);
    }
    out(<<END);
                    </select><br>
                    <select name=COMMAND>
                      <option>　　　　　　　　　　</option>
                      <option>　　　　　　　　　　</option>
                      <option>　　　　　　　　　　</option>
                      <option>　　　　　　　　　　</option>
                      <option>　　　　　　　　　　</option>
                      <option>　　　　　　　　　　</option>
                      <option>　　　　　　　　　　</option>
                      <option>　　　　　　　　　　</option>
                      <option>　　　　　　　　　　</option>
                      <option>　　　　　　　　　　</option>
                    </select>
<hr>
<b>コマンド入力</b><br><b>
<a href='javascript:void(0);' onClick="cominput(myForm,1)">挿入</a>
　<a href='javascript:void(0);' onClick="cominput(myForm,2)">上書き</a>
　<a href='javascript:void(0);' onClick="cominput(myForm,3)">削除</a>
</b>
<hr>
END
    PointPanel();

    Command_argPanel();

    my ($myislandID) = $defaultTarget;
    $myislandID = $island->{'id'} if ($myislandID eq '');

    out(<<END);
<hr>
<b>目標の${AfterName}</b>：
<b><a href='javascript:void(0);' onclick="jump(myForm, '$HjavaMode')"> 表示 </a></b>
・
<b><a href='javascript:void(0);' onclick="myisland(myForm,'$myislandID')"> 前選択 </a></b><br>
                    <select name='TARGETID'>
$HtargetList
                    </select>
<hr>
<b>コマンド移動</b>：
<big>
  <a href='javascript:void(0);' onClick="cominput(myForm,4)" style="text-decoration:none"> ▲ </a>・・
  <a href='javascript:void(0);' onClick="cominput(myForm,5)" style="text-decoration:none"> ▼ </a>
</big>
<hr>
                    <input type="hidden" name="COMARY" value="comary">
                    <input type="hidden" name="JAVAMODE" value="$HjavaMode">
<b>パスワード</b><br>
                    <input type="password" name="PASSWORD" value="$HdefaultPassword">
<hr>
                    <input type="submit" value="計画送信" NAME=CommandJavaButton$Hislands[$HcurrentNumber]->{'id'} onClick="map_cmd_chg=false;">
<br>
<font size=2>最後に<span class='attention'>計画送信ボタン</span>を<br>押すのを忘れないように。</font>
<hr>
                  </form>
                    <p><b><a href="javascript:void(0);" onclick="monument_page(myForm, '$HjavaMode')">記念碑数量リスト</a></b></p>
                    <textarea class="popupnavi" style="resize:none;" cols="20" rows="5" id="CMD_HELP">test</textarea>
                </center>
              </td>
              <td $HbgMapCell>
                <form name="map_hint">
                  <center>
                    <textarea name="COMSTATUS" cols="64" rows="3" style="resize:none;"></textarea>
                  </center>
                </form>
END
    islandMap(1, 1);    # 島の地図、所有者モード
    out(<<END);
              </td>
              <td $HbgCommandCell id="plan">
                <form name="allForm" action="$HthisFile" method="post">
                  <input type="hidden" name="PASSWORD" value="$HdefaultPassword">
                  <input type="hidden" name="MENUOPEN" value="allmenu">
                  <input type="hidden" name="NUMBER" value="allno">
                  <input type="hidden" name="POINTY" value="0">
                  <input type="hidden" name="POINTX" value="0">
                  <input type="hidden" name="JAVAMODE" value="$HjavaMode">
                  <div id='AutoCommand'><b>自動系</b><br>
                    <select name='COMMAND'>
END
    #コマンド

    my ($ff) = 0;
    {
        my ($kind, $cost, $s);
        foreach (@Hcommand_Auto) {

            $kind = $_;
            if (isCommandEnable($kind)) {

                $cost = $HcomCost[$kind];
                if ($cost == 0) {

                    $cost = '無料';
                }
                $s = ($kind == $HdefaultKind) ? 'selected' : '';
                out("                      <option value=$kind $s>$HcomName[$kind]($cost)\n");
            }
        }
    }

    out(<<END);
                    </select><br>
<b>伐採数量</b>
                    <select name='AMOUNT'>
END

    command_arg();

    out(<<END);
                    </select>×200本以上<br>
                    <input type="hidden" name="CommandButton$Hislands[$HcurrentNumber]->{'id'}">
                    <input type="submit" value="自動系計画送信">
<hr>
                  </div>
                  <ilayer name="PARENT_LINKMSG" width="100%" height="100%">
                    <layer name="LINKMSG1" width="200"></layer>
                    <span id="LINKMSG1"></span>
                  </ilayer><br>
                </form>
              </td>
            </tr>
          </table>
        </center>
END
    # 持ち物描画
    islandItemData();
    # 各種拡張データ表示
    islandData();

    out(<<END);
</center>
<hr>
END

    # コメント更新 フォーム
    CommentForm($island);

    out(<<END);
<!-- # 追加（JS版 ver2.0）ＩＥ６対応----- -->
<!-- </center> -- -->
<!-- -ここまで---------------------------- -->
END
}


#----------------------------------------------------------------------
# 計画番号をprint
# <OPTION VALUE=$i> のみ
#----------------------------------------------------------------------
sub Plan_number {

    my ($j, $i);
    {
        my ($t_cmdlist) = '';
        $j = 0;
        for ($i = 0; $i < $HcommandMax; $i++) {

            $j = $i + 1;
            $t_cmdlist .= ("<option value=$i>$j");
        }
        out($t_cmdlist);
    }
}


#----------------------------------------------------------------------
# コマンドモード
#----------------------------------------------------------------------
sub commandJavaMain {
    # idから島を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];
    $HcurrentName = islandName($island);

    # パスワード
    if (!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    # モードで分岐
    my ($command) = $island->{'command'};
    for ($i = 0; $i < $HcommandMax; $i++) {
        # コマンド登録
        $HcommandComary =~ s/([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*) //;
        my $kind = $1;
        if ($kind == 0) {

            $kind = $HcomDoNothing;
        }
        $command->[$i] = {
            'kind' => $kind,
            'x' => $2,
            'y' => $3,
            'arg' => $4,
            'target' => $5
        };
    }
    tempCommandAdd();
    # データの書き出し
    writeIslandsFile($HcurrentID);

    # owner modeへ
    ownerMain();
}


#----------------------------------------------------------------------
#
#----------------------------------------------------------------------
sub toCostDisplay {
    my ($cost , $island) = @_;

    my ($l_cost);

    $l_cost = CalcCostbyPoint($cost , $island);

    if ($l_cost == 0) {
        $l_cost = '無料';
    }
    elsif ($l_cost < 0) {
        $l_cost = - $l_cost;
        $l_cost .= $HunitFood;
    }
    else {
        $l_cost .= $HunitMoney;
    }
    return ($l_cost);
}


#----------------------------------------------------------------------
# 観光モード
#----------------------------------------------------------------------
sub printIslandJava {

    my ($island);
    # 開放
    unlock();

    # idから島番号を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    $island = $Hislands[$HcurrentNumber];

    # なぜかその島がない場合
    if ($HcurrentNumber eq '') {

        tempProblem();
        return;
    }

    # 名前の取得
    $HcurrentName = islandName($Hislands[$HcurrentNumber]);

    #コマンドリストセット
    my ($l_kind);
    my ($m);
    @click_com[8, 9]  = ('', '');
    if ($HjavaMode eq 'java') {

        $com_count = @HcommandDivido2;
        my ($l_cost);

        my ($tag_s_s,$tag_s_e);
        my ($flag);
        my ($cmd_lp);
        my (@cmd);
        my ($cmdsetnum);

        for ($m = 0; $m < $com_count; $m++) {

            if (   ($m == 8)
                || ($m == 9) ) {
            }
            else {
                next;
            }

            @cmd = split(/,/,$HcommandDivido2[$m]);
            $cmdsetnum = ($#cmd) + 1;

            for ($cmd_lp = 1 ; $cmd_lp < $cmdsetnum ; $cmd_lp++) {

                $tag_s_s = '';
                $tag_s_e = '';
                $l_kind = $cmd[$cmd_lp];

                if (isCommandEnable($l_kind) ) {

                    # 値段算出
                    $l_cost = toCostDisplay($HcomCost[$l_kind] , $island);

                    if (   ($l_kind == $HcomEiseiLzr)
                        || ($l_kind == $HcomSendPirates)
                        || ($l_kind == $HcomSendMonster)
                        || ($l_kind == $HcomMissileNM)
                        || ($l_kind == $HcomMissilePP)
                        || ($l_kind == $HcomMissileSPP)
                        || ($l_kind == $HcomMissileST)
                        || ($l_kind == $HcomMissileSS)
                        || ($l_kind == $HcomMissileLR)
                        || ($l_kind == $HcomMissileLD)
                                                        ) {

                        if (   (   ($HcurrentID != $HmyislandID)
                                && ($HcurrentID != 67))
                            && ($island->{'pop'} < $HguardPop)) {

                            $tag_s_s = "<s $HcurrentID>";
                            $tag_s_e = '</s>';
                        }
                    }
                    $click_com[$m] .= "<a title='$l_cost' href='javascript:void(0);' onClick='window.opener.cominput(window.opener.document.myForm,6,$l_kind)' style='text-decoration:none'>$tag_s_s$HcomName[$l_kind]<font size='-1'>($l_cost)</font>$tag_s_e</a><br>\n";
#                   $click_com[$m] .= "<a title='$l_cost' href='javascript:void(0);' onClick='window.opener.cominput(window.opener.document.myForm,6,$l_kind)' STYlE='text-decoration:none'>$HcomName[$l_kind]/$l_cost</a><br>\n";
                }
            }
        }
    }

    out(<<END);
<script type="text/javascript">
<!--
if(document.getElementById) {
    document.onmousemove = Mmove;
} else if(document.layers) {
    window.captureEvents(Event.MOUSEMOVE);
    window.onMouseMove = Mmove;
} else if(document.all) {
    document.onmousemove = Mmove;
}

if((document.layers) || (document.all)){  // IE4、IE5、NN4
    window.document.onmouseup = menuclose;
}

function ps(x, y) {
  var ja = '$HjavaMode';
  window.opener.document.myForm.POINTX.options[x].selected = true;
  window.opener.document.myForm.POINTY.options[y].selected = true;
  if(ja == 'java')moveLAYER("menu",mx,my);
  return true;
}

function moveLAYER(layName,x,y) {
    if(document.getElementById){        //NN6,IE5
        if(document.all){                //IE5
            el = document.getElementById(layName);
            el.style.left= event.clientX + document.body.scrollLeft + 10;
            el.style.top= event.clientY + document.body.scrollTop - 30;
            el.style.display = "block";
            el.style.visibility ='visible';
        }else{
            el = document.getElementById(layName);
            el.style.left=x+10;
            el.style.top=y-30;
            el.style.display = "block";
            el.style.visibility ='visible';
        }
    } else if(document.layers){                //NN4
        msgLay = document.layers[layName];
        msgLay.moveTo(x+10,y-30);
        msgLay.visibility = "show";
    } else if(document.all){                //IE4
        msgLay = document.all(layName);
        msgLay.style.pixelLeft = x+10;
        msgLay.style.pixelTop = y-30;
        msgLay.style.display = "block";
        msgLay.style.visibility = "visible";
    }

}

function menuclose() {

    ResetImgFrame();

    if (document.getElementById){
        document.getElementById("menu").style.display = "none";
    } else if (document.layers){
        document.menu.visibility = "hide";
    } else if (document.all){
        window["menu"].style.display = "none";
    }
}

function Mmove(e) {
  if(document.all){
    mx = event.x;
    my = event.y;
  }else if(document.layers){
    mx = e.pageX;
    my = e.pageY;
  }else if(document.getElementById){
    mx = e.pageX;
    my = e.pageY;
  }
}

function set_land(x, y, land, img) {
  com_str = land + "\\n";
  document.POPUP.COMSTATUS.value= com_str;
  document.POPUP.NAVIIMG.src= img;
}

function ResetImgFrame() {
  for (f=0;f<$HislandSize;f++) {
    for (i=0;i<$HislandSize;i++) {
      FrameDel(i, f);
    }
  }
}

function FrameDel(x, y) {
  var add = "";
  var name = document.getElementById("map_" + x + "-" + y);
  if (name.classList.contains('tile_ret') == true) {
    add = "tile_ret";
  }
  name.className = "maptile " + add;
}

function MapTileSelect(x, y) {
  ResetImgFrame();
  SetImgFrame(x, y);
}

function SetImgFrame(x ,y) {
  var add = "";
  var name = document.getElementById("map_" + x + "-" + y);

  if (name.classList.contains('tile_ret') == true) {
    add = "tile_ret";
  }
  name.className = "tileselect " + add;
  name.style.borderColor = "#ffffff";
}

//-->
</script>
<h2 align='center'>${HtagName_}${HcurrentName}${H_tagName}</h2>
<div id='targetMap'>
END
    islandInfo(0);

    out(<<END);
<div align='center'>
攻撃する地点をクリックして下さい。<br>クリックした地点が開発画面の座標に設定されます。
</div>
<div id="menu" style="position:absolute; visibility:hidden;">
<table border="0" class="PopupCell">
  <tr>
    <td class='T'>
      <form name='POPUP'>
        <img alt='' name="NAVIIMG" src="" width="32" height="32" align="left">
        <textarea name="COMSTATUS" rows="2" class="popupnavi"></textarea>
      </form>
    </td>
  </tr>
  <tr>
    <td>
    $click_com[8]<hr>
    $click_com[9]<hr>
    <a href="Javascript:void(0);" onClick="menuclose()" style="text-decoration:none">メニューを閉じる</a>
  </td>
</tr>
</table>
</div>
END
    if (   (checkPassword($island, $HdefaultPassword))
        && ($island->{'id'} eq $defaultID)) {

        islandMap(1, 1);  # 島の地図、観光モード
    }
    else {

        islandMap(0, 1);  # 島の地図、観光モード
    }

    out('</div>');
}


#----------------------------------------------------------------------
# 観光モード
#----------------------------------------------------------------------
# メイン
sub printIslandMain {
    # 開放
    unlock();

    # idから島番号を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};

    # なぜかその島がない場合
    if ($HcurrentNumber eq '') {
        tempProblem();
        return;
    }

    # 名前の取得
    $HcurrentName = islandName($Hislands[$HcurrentNumber]);

    # 観光画面
    tempPrintIslandHead();          # ようこそ!!
    MapCommonScript();
    islandInfo(0);                  # 島の情報
    islandMap($HadminMode, 0);      # 島の地図、観光モード

    islandJamp();   # 島の移動
    islandData();   # 各種データ

    # ○○島ローカル掲示板
    if ($HuseLbbs) {

        require('./hako-lbbs.cgi');
        tempLbbsMain(0);
    }

    if (USE_EX_LBBS) {     # 外部掲示板

        exLbbs($HcurrentID, 0) ;
    }

    # 近況
    tempRecent(0, $HuseHistory2);
}

#----------------------------------------------------------------------
# 開発モード
#----------------------------------------------------------------------
# メイン
sub ownerMain {
    # 開放
    unlock();

    # モードを明示
    $HmainMode = 'owner';

    # idから島を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];
    $HcurrentName = islandName($island);

    # パスワード
    if (!checkPassword($island,$HinputPassword)) {
        # password間違い
        tempWrongPassword();
        return;
    }

    wiiU_ip_check_write($HcurrentID);

    # 開発画面
    if ($HjavaMode eq 'java') {
        tempOwnerJava(); # 「Javaスクリプト開発計画」
    }
    else {               # 「通常モード開発計画」
        tempOwner();
    }

    # ○○島ローカル掲示板
    if ($HuseLbbs) {

        require('./hako-lbbs.cgi');
        tempLbbsMain(1);     # ローカル掲示板
    }
    if (USE_EX_LBBS) {     # 外部掲示板
        exLbbs($HcurrentID, 1) ;
    }

    # 近況
    tempRecent(1, $HuseHistory1);
}


#----------------------------------------------------------------------
# コマンドモード
#----------------------------------------------------------------------
# メイン
sub commandMain {
    # idから島を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];
    $HcurrentName = islandName($island);

    # パスワード
    if (!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    # モードで分岐
    my ($command) = $island->{'command'};

    if ($HcommandMode eq 'delete') {

        slideFront($command, $HcommandPlanNumber);
        tempCommandDelete();
    }
    elsif (   ($HcommandKind == $HcomAutoPrepare)
           || ($HcommandKind == $HcomAutoPrepare2)) {
        # フル整地、フル地ならし
        # 座標配列を作る
        makeRandomPointArray();
        my ($land) = $island->{'land'};

        # コマンドの種類決定
        my ($kind) = $HcomPrepare;
        if ($HcommandKind == $HcomAutoPrepare2) {

            $kind = $HcomPrepare2;
        }

        my ($i) = 0;
        my ($j) = 0;
        while (($j < $HpointNumber) && ($i < $HcommandMax)) {
            my ($x) = $Hrpx[$j];
            my ($y) = $Hrpy[$j];
            if ($land->[$x][$y] == LAND_WASTE) {
                slideBack($command, $HcommandPlanNumber);
                $command->[$HcommandPlanNumber] = {
                    'kind' => $kind,
                    'target' => 0,
                    'x' => $x,
                    'y' => $y,
                    'arg' => 0
                    };
                $i++;
            }
            $j++;
        }
        tempCommandAdd();
    }
    elsif (   ($HcommandKind == $HcomAutoReclaim)
           || ($HcommandKind == $HcomAutoDestroy)) {
        # 浅瀬埋め立て、浅瀬掘削
        makeRandomPointArray();
        my ($land) = $island->{'land'};
        my ($landValue) = $island->{'landValue'};

        # コマンドの種類決定
        my ($kind) = $HcomReclaim;
        if ($HcommandKind == $HcomAutoDestroy) {
            $kind = $HcomDestroy;
        }
        my ($i) = 0;
        my ($j) = 0;
        while (($j < $HpointNumber) && ($i < $HcommandMax)) {
            my ($x) = $Hrpx[$j];
            my ($y) = $Hrpy[$j];
            if (($land->[$x][$y] == $HlandSea) && ($landValue->[$x][$y] == 1)) {
                slideBack($command, $HcommandPlanNumber);
                $command->[$HcommandPlanNumber] = {
                    'kind' => $kind,
                    'target' => 0,
                    'x' => $x,
                    'y' => $y,
                    'arg' => 0
                };
                $i++;
            }
            $j++;
        }
        tempCommandAdd();
    }
    elsif (   ($HcommandKind == $HcomAutoSellTree)
           || ($HcommandKind == $HcomAutoForestry)) {

        # 伐採、伐採と植林
        # （数量×２００本より多い森だけが対象）
        makeRandomPointArray();
        my ($land) = $island->{'land'};
        my ($landValue) = $island->{'landValue'};

        # コマンドの種類決定
        my ($kind) = ($HcommandKind == $HcomAutoForestry) ? 1 : 0;
        my ($i) = 0;
        my ($j) = 0;
        while (($j < $HpointNumber) && ($i < $HcommandMax)) {
            my ($x) = $Hrpx[$j];
            my ($y) = $Hrpy[$j];
            if (($land->[$x][$y] == $HlandForest) && ($landValue->[$x][$y] > $HcommandArg * 2)) {
                if ($kind) {
                    slideBack($command, $HcommandPlanNumber);
                    $command->[$HcommandPlanNumber] = {
                        'kind' => $HcomPlant,
                        'target' => 0,
                        'x' => $x,
                        'y' => $y,
                        'arg' => 0
                    };
                    $i++;
                }
                slideBack($command, $HcommandPlanNumber);
                $command->[$HcommandPlanNumber] = {
                    'kind' => $HcomSellTree,
                    'target' => 0,
                    'x' => $x,
                    'y' => $y,
                    'arg' => 0
                };
                $i++;
            }
            $j++;
        }
        tempCommandAdd();
    }
    elsif ($HcommandKind == $HcomAutoDelete) {
        # 全消し
        my ($i);
        for ($i = 0; $i < $HcommandMax; $i++) {
            slideFront($command, $HcommandPlanNumber);
        }
        tempCommandDelete();
    }
    else {
        if ($HcommandMode eq 'insert') {
            slideBack($command, $HcommandPlanNumber);
        }
        tempCommandAdd();
        # コマンドを登録
        $command->[$HcommandPlanNumber] = {
            'kind' => $HcommandKind,
            'target' => $HcommandTarget,
            'x' => $HcommandX,
            'y' => $HcommandY,
            'arg' => $HcommandArg
        };
    }

    $HcommandPlanNumber++ if ($HcommandPlanNumber + 1 < $HcommandMax);

    # データの書き出し
    writeIslandsFile($HcurrentID);

    # owner modeへ
    ownerMain();
}


#----------------------------------------------------------------------
# コメント入力モード
#----------------------------------------------------------------------
# メイン
sub commentMain {
    # idから島を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];
    $HcurrentName = islandName($island);

    # パスワード
    if (!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    # メッセージを更新
    $island->{'comment'} = htmlEscape($Hmessage);

    # データの書き出し
    writeIslandsFile($HcurrentID);

    # コメント更新メッセージ
    tempComment();

    # owner modeへ
    ownerMain();
}

#----------------------------------------------------------------------
# toto入力モード
#----------------------------------------------------------------------
# メイン
sub totoInputMain {
    my ($num) = @_;

    # idから島を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];

    # パスワード
    if (!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    # メッセージを更新
    $island->{'totoyoso'}->[$num] = htmlEscape($HyosoMessage[$num]);
    # データの書き出し
    writeIslandsFile($HcurrentID);

    # コメント更新メッセージ
    tempToto();

    # owner modeへ
    ownerMain();
}


#----------------------------------------------------------------------
# 首都名前変更
#----------------------------------------------------------------------
sub shutoMain {

    # idから島を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];

    # パスワード
    if (!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    if ($HshutoMessage == 555) {
        tempShutoWrong();
    }
    else {
        # メッセージを更新
        $island->{'shutomessage'} = htmlEscape($HshutoMessage);

        # データの書き出し
        writeIslandsFile($HcurrentID);

        # コメント更新メッセージ
        tempShuto();
    }
    # owner modeへ
    ownerMain();
}

#----------------------------------------------------------------------
# 役所の仕事を変える
#----------------------------------------------------------------------
sub WorkChangeMain {

    # idから島を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];


    # パスワード
    if (!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    if ($HYaku_Chg_Yotei == 1) {

        $island->{'yaku_work'} |= $HYakushoWorkYotei;
    }
    else {

        $island->{'yaku_work'} &= (0xFF ^ $HYakushoWorkYotei);
    }

    if ($HYaku_Chg_Narasi == 1) {

        $island->{'yaku_work'} |= $HYakushoWorkSeiti;
    }
    else {

        $island->{'yaku_work'} &= (0xFF ^ $HYakushoWorkSeiti);
    }

    # データの書き出し
    writeIslandsFile($HcurrentID);
    # owner modeへ
    ownerMain();
}


#----------------------------------------------------------------------
# チーム
#----------------------------------------------------------------------
sub TeamMain {

    # idから島を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];

    # パスワード
    if (!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    if ($HteamMessage == 555) {
        tempTeamWrong();
    }
    else {
        # メッセージを更新
        $island->{'hakoteam'} = htmlEscape($HteamMessage);

        # データの書き出し
        writeIslandsFile($HcurrentID);

        # コメント更新メッセージ
        tempTeam();
    }
    # owner modeへ
    ownerMain();
}


#----------------------------------------------------------------------
# 与えた数値に対応する疑似乱数
#----------------------------------------------------------------------
sub seqnum2 {
    my ($seed,$seed2) = @_;
    my ($v) = sin($seed + 33 + $seed2); # 33 は任意の整数、乱数の系列を変える

    return (int(substr($v, -4, 3)));
}

#----------------------------------------------------------------------
sub Sea_Img_Gen {
    my ($id,$x,$y) = @_;

    my ($Sea_Img) = 'land0.png';

    if (   (!(seqnum2($HislandTurn,$id+8) % 3) )
        && ($x == (seqnum2($HislandTurn,$id+3) % ISLAND_SIZE) )
        && ($y == (seqnum2($HislandTurn,$id+1) % ISLAND_SIZE) ) ) {
        $Sea_Img = 'kamome.gif';
    }

    return $Sea_Img;
}


#----------------------------------------------------------------------
# テンプレートその他
#----------------------------------------------------------------------
# 個別ログ表示
sub logPrintLocal {
    my ($mode) = @_;
    my ($i);
    for ($i = 0; $i < $HlogMax; $i++) {
        logFilePrint($i, $HcurrentID, $mode);
    }
}

#----------------------------------------------------------------------
# ○○島へようこそ！！
sub tempPrintIslandHead {

    out(<<END);
<div align='center'>
  <h1 class="big">
    <span class='Nret'>${HtagName_}「${HcurrentName}」${H_tagName}へ</span><span class='Nret'>ようこそ！！</span>
  </h1>
$HtempBack<br>
</div>
END
}


#----------------------------------------------------------------------
# ○○島開発計画
sub tempOwner {
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my($island) = $Hislands[$HcurrentNumber];

    OwnarMap_Header();
    MapCommonScript();
    out(<<END);
<script type="text/javascript">
<!--
var miniTargetmap;

function ps(x, y) {
    with (document.myForm) {
        elements[4].options[x].selected = true;
        elements[5].options[y].selected = true;
        with (elements[7]) {
            var i;
            for (i = 0; i < length; i++) {
                if (options[i].value == $HcurrentID) {
                    options[i].selected = true;
                    break;
                }
            }
        }
    }
    return 1;
}

function ns(x) {
    document.myForm.elements[2].options[x].selected = true;
    return 1;
}

function cmdsl() {
    var i;
    var x;
    x = document.myForm.elements[2].selectedIndex;
    if (document.getElementById){
        for (i = 0; i < $HcommandMax; i++) {
            document.getElementById("CMD_"+i).innerHTML = "○";
        }
        document.getElementById("CMD_"+x).innerHTML = "●";
    }
    return true;
}

var monumentlist;
function monument_page(theForm, j_mode) {
    if ( (monumentlist == null)||(monumentlist.closed) ) {
        monumentlist = window.open("$HthisFile?MONUMENT_NUM=1", "minitar", "menubar=1,toolbar=0,location=0,directories=no,status=1,scrollbars=1,resizable=1,width=700,height=630");
    }
    else{
        monumentlist.location.href = "$HthisFile?MONUMENT_NUM=1";
        monumentlist.focus();
    }
}


function jump(theForm, j_mode) {
    var sIndex = theForm.TARGETID.selectedIndex;
    var url = theForm.TARGETID.options[sIndex].value;
    if (url != "" ) {
        window.self.name = "trap";
        if ( (miniTargetmap == null)||(miniTargetmap.closed) ) {
            miniTargetmap = window.open("$HthisFile?IslandMap="+url+"&JAVAMODE="+j_mode+"&FROM_ISLAND=$island->{'id'}", "minitar", "menubar=1,toolbar=0,location=0,directories=no,status=1,scrollbars=1,resizable=1,width=700,height=630");
        }else{
            miniTargetmap.location.href = "$HthisFile?IslandMap="+url+"&JAVAMODE="+j_mode+"&FROM_ISLAND=$island->{'id'}";
            miniTargetmap.focus();
        }
    }
}

function tohint(pos,str) {
    if(document.getElementById){
        document.getElementById("HINT_PANEL").innerHTML = pos;
    }
}
//-->
</script>
END

    islandInfo(1);

    out(<<END);
<div align='center'>
  <table border='1'>
    <tr valign=top>
      <td $HbgInputCell >
        <form name="myForm" action="$HthisFile" method="POST">
          <input type="submit" value="計画送信" name="CommandButton$Hislands[$HcurrentNumber]->{'id'}">
          <hr>
          <b>パスワード</b></br>
          <input type="password" name="PASSWORD" value="$HdefaultPassword">
          <hr>
          <b>計画番号</b>
          <select name="NUMBER" onChange="cmdsl()">
END
    # 計画番号
    Plan_number();

out(<<END);
          </select><br>
          <hr>
          <b>開発計画</b><br>
          <select name="COMMAND">
END

    #コマンド
    my ($j, $i);
    my ($kind, $cost, $s);
    for ($i = 0; $i < $HcommandTotal; $i++) {
        $kind = $HcomList[$i];
        next if ((($kind == $HcomSave)||($kind == $HcomLoad))&& !($Hislands[$HcurrentNumber]->{'shr'}));
        next if (($kind == $HcomBettown) && ($Hislands[$HcurrentNumber]->{'shutomessage'} == 555));

        # 値段算出
        $cost = toCostDisplay($HcomCost[$kind], $island);

        $s = ($kind == $HdefaultKind) ? 'selected' : '';
        out("<option value='$kind' $s>$HcomName[$kind]($cost)\n");
    }

    out(<<END);
          </select>
          <hr>
END

    PointPanel();

    Command_argPanel();

    out(<<END);
          <hr>
          <b>目標の${AfterName}</b>：
          <b><a href="javascript:void(0);" onclick="jump(myForm, '$HjavaMode')"> 表\示 </a></b><br>
          <select name='TARGETID'>
$HtargetList
          </select>
          <hr>
          <b>動作</b><br>
          <input type="radio" name="COMMANDMODE" value="insert" checked>挿入
          <input type="radio" name="COMMANDMODE" value="write">上書き<br>
          <input type="radio" name="COMMANDMODE" value="delete">削除
          <hr>
          <input type="submit" value="計画送信" name=CommandButton$Hislands[$HcurrentNumber]->{'id'}>
          <br>
        </form>
        <center>
          <p><b><a href="javascript:void(0);" onclick="monument_page(myForm, '$HjavaMode')">記念碑数量リスト</a></b></p>
          <textarea class="popupnavi" style="resize:none;" cols="20" rows="5" id="CMD_HELP">test</textarea>
        </center>
      </td>
      <td $HbgMapCell>
END

    my ($totoyoso) = $Hislands[$HcurrentNumber]->{'totoyoso'}->[0];
    my ($mapsize) = $totoyoso;

    $Hms1 = 16;
    $Hms2 = $Hms1*2;
    islandMap(1, 0); # 島の地図、所有者モード

    out(<<END);
        <div align='center'>
          <form action="$HthisFile" method="POST" target="_blank">
            <b>観光する${AfterName}</b><select name=TARGETID>$HtargetList<br></select>
            <input type="submit" value="画面を開く" name="SightButton">
          </form>
        </div>
      </td>
      <td $HbgCommandCell>
END
    {
        my ($cmd) = $Hislands[$HcurrentNumber]->{'command'};
        for ($i = 0; $i < $HcommandMax; $i++) {
            tempCommand($i, $cmd->[$i], $Hislands[$HcurrentNumber]->{'shr'}, 1);
        }
    }
    out(<<END);
      </td>
    </tr>
  </table>
END
    # 持ち物描画
    islandItemData();
    # 各種拡張データ表示
    islandData();

    out(<<END);
</div>
<hr>
END
    CommentForm($island);
}

#----------------------------------------------------------------------
sub Command_argPanel {

    out(<<END);
          <b>数量</b>
          <select name='AMOUNT'>
END

    # 数量 2ですすめてなんとか小さくする。
    command_arg();

    out(<<END);
          </select>
END
}


#----------------------------------------------------------------------
sub PointPanel {
    out(<<END);
<b>座標(</b>
<select name='POINTX'>
END
    foreach my $i (0..$islandSize) {
        if ($i == $HdefaultX) {

            out("<option value=$i selected>$i");
            for ( ; $i > $islandSize ; $i++) { out("<option value=$i>$i"); }
        }
        else {

            out("<option value=$i>$i");
        }
    }

    out(<<END);
</select>, <select name=POINTY>
END

    foreach my $i (0..$islandSize) {
        if ($i == $HdefaultY) {

            out("<option value=$i selected>$i");
            for ( ; $i > $islandSize ; $i++) { out("<option value=$i>$i"); }
        }
        else {

            out("<option value=$i>$i");
        }
    }
    out(<<END);
</select><b>)</b>
END
}


#----------------------------------------------------------------------
# コメント更新
#----------------------------------------------------------------------
sub CommentForm {
    my ($island) = @_;
    my ($id) = $island->{'id'};
    out(<<END);
<div id='CommentBox' align='center'>
  <h2>コメント更新</h2>
  <form action="$HthisFile" method="POST">
    <input type="hidden" name="JAVAMODE" value="$HjavaMode">
    <table border="0">
END
    CommentChangeForm($island);
    ShutoChangeForm($island);
    TeamNameChangeForm($island);
    YakusyoChangeForm($island);
    totoMessageChangeForm($island);
    out(<<END);
    </table>
  </form>
</div>
END
}


#----------------------------------------------------------------------
# コメントフォーム
#----------------------------------------------------------------------
sub CommentChangeForm {
    my ($island) = @_;
    my ($id) = $island->{'id'};
    my ($comment) = $island->{'comment'};

    out(<<END);
    <tr>
      <th>コメント<br><small>(全角${HlengthMessage}字まで)</small></th>
      <td><input type="text" name="MESSAGE" size="80" value="$comment"></td>
    </tr>
    <tr>
      <th>パスワード</th>
      <td><input type="password" name="PASSWORD" value="$HdefaultPassword">
        <input type="submit" value="コメント更新" name="MessageButton$id">
      </td>
    </tr>
END
}

#----------------------------------------------------------------------
# チーム名変更フォーム
#----------------------------------------------------------------------
sub totoMessageChangeForm {
    my ($island) = @_;
    my ($id) = $island->{'id'};

    my ($totoyoso) =  $island->{'totoyoso'}->[0];
    my ($totoyoso2) = $island->{'totoyoso'}->[1];

    out(<<END);
<tr>
<th>看板1<br><small>(全角${HlengthYoso}字まで)</small></th>
<td><input type="text" name="YOSOMESSAGE" size="44" value="$totoyoso">
<INPUT TYPE="submit" VALUE="更新" NAME=TotoButton$id>
</td></tr>
<tr>
<th>看板2<BR><small>(全角${HlengthYoso}字まで)</small></th>
<td><input type="text" name="YOSOMESSAGE2" size="44" value="$totoyoso2">
<input type="submit" value="更新" name=TotosButton$id>
</td></tr>
END
}


#----------------------------------------------------------------------
# チーム名変更フォーム
#----------------------------------------------------------------------
sub TeamNameChangeForm {
    my ($island) = @_;

    my ($teammessage) = $island->{'hakoteam'};
    my ($sta_cnt) = $island->{'stadiumnum'};

    if ($sta_cnt > 0) {
        out(<<END);
<tr>
  <th>チーム名変更<br><small>(全角${HlengthTeam}字まで)</small></th>
  <td><INPUT TYPE=text NAME=TEAMMESSAGE SIZE=32 VALUE="$teammessage">
    <input type="submit" value="チーム名変更" name=TeamButton$Hislands[$HcurrentNumber]->{'id'}>
  </td>
</tr>
<tr>
END
    }
}


#----------------------------------------------------------------------
# 役所変更フォーム
#----------------------------------------------------------------------
sub YakusyoChangeForm {
    my ($island) = @_;

    my ($id) = $island->{'id'};

    if ($island->{'yaku_work'} > 0 ) {
        my ($temp_yotei , $temp_narasi);

        if ($Hislands[$HcurrentNumber]->{'yaku_work'} & $HYakushoWorkYotei) {
            $temp_yotei = 'checked="checked"';
        }
        if ($Hislands[$HcurrentNumber]->{'yaku_work'} & $HYakushoWorkSeiti) {
            $temp_narasi ='checked="checked"';
        }
        out(<<END);
<tr>
<th>役所の仕事</th>
  <td>
    <span style="background-color:#ffcc99"><input type="checkbox" name="YAKU_YOTEI" value="$HYakushoWorkYotei" ${temp_yotei}>自動予定地</span>　
    <span style="background-color:#ffcc99"><input type="checkbox" name="YAKU_NARASI" value="$HYakushoWorkSeiti" ${temp_narasi}>自動地ならし</span>　
    <input type="submit" value="決定" name="YakuWorkButton$id">
  </td>
</tr>
<tr>
END
    }
}


#----------------------------------------------------------------------
# 首都名変更フォーム
#----------------------------------------------------------------------
sub ShutoChangeForm {
    my($island) = @_;

    my $shutomessage = $island->{'shutomessage'};

    if ($shutomessage == 555) {
        # $shutohen = "";
    }
    else {
        out(<<END);
    <tr>
      <th>首都名変更<br><small>(全角${HlengthShuto}字まで)</small></th>
      <td>
        <input type="text" name=SHUTOMESSAGE size=32 value="$shutomessage">
        <input type="submit" value="首都名変更" name=ShutoButton$Hislands[$HcurrentNumber]->{'id'}>
      </td>
    </tr>
END
    }
}

#----------------------------------------------------------------------
# 入力済みコマンド表示
sub tempCommand {
    my ($number, $command, $shr, $mode) = @_;

    my ($kind, $target, $x, $y, $arg) =
        (
            $command->{'kind'},
            $command->{'target'},
            $command->{'x'},
            $command->{'y'},
            $command->{'arg'}
        );
    $HcomName[$kind] = '' if ((($kind == $HcomSave)||($kind == $HcomLoad))&& !$shr);

    if ($HcomName[$kind] eq '') { $HcomName[$kind] = "このコマンドは使えなくなりました($kind)"; }
    my ($name) = "$HtagComName_${HcomName[$kind]}$H_tagComName";
    my ($point) = "$HtagName_($x,$y)$H_tagName";
    $target = islandName($Hislands[$HidToNumber{$target}]);
    if ($target eq '') {
        $target = '無人';
    }
    $target = "$HtagName_${target}$H_tagName";

    my ($value) = $arg * $HcomCost[$kind];
    $value = $HcomCost[$kind] if (!$value);
    if ($value < 0) {

        $value = -$value;
        $value = "$value$HunitFood";
    }
    else {

        $value = "$value$HunitMoney";
    }
    $value = "$HtagName_$value$H_tagName";

    my ($j) = sprintf("%02d：", $number + 1);

    out("<a style=\"text-decoration:none\" href=\"javascript:void(0);\" onClick=\"ns($number);cmdsl();return true;\">") if($mode);
    out("$HtagNumber_<span id=\"CMD_$number\">○</span>$j$H_tagNumber$HnormalColor_");

    my ($command_msg) = '';

    if (   ($kind == $HcomDoNothing)
        || ($kind == $HcomSave)
        || ($kind == $HcomLoad)
        || ($kind == $HcomGiveup)) {

        $command_msg = "$name";
    }
    elsif (   ($kind == $HcomFarm)
           || ($kind == $HcomFoodim)
           || ($kind == $HcomFactory)
           || ($kind == $HcomNursery)
           || ($kind == $HcomBoku)
           || ($kind == $HcomPark)
           || ($kind == $HcomUmiamu)
           || ($kind == $HcomMountain)
           || ($kind == $HcomKai)
           || ($kind == $HcomHTget)
           || ($kind == $HcomGivefood)
           || ($kind == $HcomPropaganda)) {
        # 回数付き
        if (   ($arg == 0)
            || ($arg == 1)) {
            $command_msg = "$pointで$name" ;
        }
        else {
            $command_msg = "$pointで$name($arg回)";
        }
    }
    elsif ($kind == $HcomFarmcpc) {

        my ($msg);
        if ($arg == 2) {
            $msg = '養豚場';
        }
        elsif ($arg == 3) {
            $msg = '牧場';
        }
        else {
            $msg = '養鶏場';
        }
        $command_msg = "$pointで$name($arg)$HtagComName_$msg$H_tagComName" ;
    }
    elsif ($kind == $HcomHaribote) {

        # 数付き
        if ($arg == 0) {
            $command_msg = ("$pointで$name");
        }
        else {
            $command_msg = ("$pointで$name($arg)");
        }
    }
    elsif ($kind == $HcomHouse) {
        # 数付き
        $command_msg = ("$pointで$name($arg)");

    }
    elsif ($kind == $HcomItemThrow) {
        # 数付き
        $command_msg = ("$name($arg)");

    }
    elsif ($kind == $HcomMonument) {
        # 数付き
        $arg = 0 if( ($arg >= $HmonumentNumber) && ($arg != 94) );
        $command_msg = ("$pointで$name($HmonumentName[$arg]<IMG SRC=\"${HMapImgDir}$HmonumentImage[$arg]\" width=16 height=16 alt=''>)");
    }
    elsif ($kind == $HcomDestroy) {
        # 掘削
        if ($arg != 0) {
            $command_msg = ("$pointで$name(予算${value})");
        }
        else {
            $command_msg = ("$pointで$name");
        }
    }
    elsif ($kind == $HcomOnsen) {
        # 温泉掘削
        $arg = 1 if(!$arg);
        $command_msg = ("$pointで$name(予算${value})");
    }
    elsif ($kind == $HcomMine) {
        # 地雷
        if ($arg == 0) {
            $arg = 1;
        } elsif ($arg > 9) {
            $arg = 9;
        }
        $command_msg = ("$pointで$name(ダメージ$arg)");
    }
    elsif ($kind == $HcomZoo) {

        if (!$HmonsterZoo[$arg]) {
            $arg = 0;
        }
        $command_msg = ("$pointで$name(もしくは$HmonsterName[$arg]脱出)");
    }
    elsif (   ($kind == $HcomMissileNM)
           || ($kind == $HcomMissilePP)
           || ($kind == $HcomMissileSPP)
           || ($kind == $HcomMissileST)
           || ($kind == $HcomMissileSS)
           || ($kind == $HcomMissileLR)
           || ($kind == $HcomMissileLD)) {
        # ミサイル系
        my ($n) = ($arg == 0 ? '無制限' : "${arg}発");
        $command_msg = ("$target$pointへ$name($HtagName_$n$H_tagName)");
    }
    elsif (   ($kind == $HcomSendMonster)
             || ($kind == $HcomSendPirates)) {
        # 怪獣派遣
        $command_msg = ("$targetへ$name");
    }
    elsif ($kind == $HcomSell) {
        # 食料輸出
        $command_msg = ("$name$value");
    }
    elsif ($kind == $HcomFune) {
        # 造船
        if ( ($arg != 77) && ($arg >= $HfuneNumber) ||
             ($arg == 0) ) {
            $arg = 1;
        }
        my ($t);
        if ($arg == 77) {
            $t = "$HtagName_海上都市$H_tagName<img src=\"${HMapImgDir}land39.gif\" width=16 height=16 alt=''>";
        }
        else {
            $t = "$HtagName_$HfuneName[$arg]$H_tagName<img src=\"${HMapImgDir}$HfuneImage[$arg]\" width=16 height=16 alt=''>";
        }
        $command_msg = ("$pointで$name$t");
    }
    elsif (   ($kind == $HcomEisei)
           || ($kind == $HcomEiseimente)
           || ($kind == $HcomEiseiAtt)) {

        if (   ($arg > $HeiseiNumber)
            || ($arg == 0)) {
            $arg = 1;
        }
        my ($t);
        $t = $HeiseiName[$arg];
        if ($kind == $HcomEisei) {
            $command_msg = ("$HtagComName_$t打ち上げ$H_tagComName");
        }
        elsif ($kind == $HcomEiseimente) {
            $command_msg = ("$HtagComName_$t修復$H_tagComName");
        }
        elsif ($kind == $HcomEiseiAtt) {
            $command_msg = ("$targetの<B>$t</B>へ$name");
        }
    }
    elsif ($kind == $HcomEiseiLzr) {
        $command_msg = ("$target$pointへ$name");
    }
    elsif (   ($kind == $HcomMoney)
           || ($kind == $HcomFood)) {
        # 援助
        $command_msg = ("$targetへ$name$value");
    }
    elsif ($kind == $HcomAlly) {
        # 同盟 加盟・脱退
        $command_msg = ("$targetの$name");
    }
    else {
        # 座標付き
        $command_msg = ("$pointで$name");
    }

    my ($close_anc) = '';
    ($close_anc) = '</a>' if ($mode);

    out(<<END);
$command_msg$H_normalColor$close_anc<br>
END
}


#----------------------------------------------------------------------
# ○○島開発計画
#----------------------------------------------------------------------
sub Show_Taiji_List {

    # 開放
    unlock();

    # idから島番号を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    $island = $Hislands[$HcurrentNumber];

    # なぜかその島がない場合
    if ($HcurrentNumber eq '') {
        tempProblem();
        return;
    }

    # 名前の取得
    $HcurrentName = islandName($Hislands[$HcurrentNumber]);

    out(<<END);
<div align='center'>${HtagBig_}<span class='Nret'>${HtagName_}「${HcurrentName}」${H_tagName}の</span><span class='Nret'>怪獣図鑑</span>${H_tagBig}<BR>
</div>

END

    my ($zoo_list) = '';

    my ($zookazu);
    my ($zookazus);
    my ($m_syurui);

    ($zookazu, $zookazus, $m_syurui) = Get_ZooState($island);

    if ($zookazu) {

        $tmp = $island->{'zoo'};
        chomp($tmp);
        @mons_list = split(/\,/,$tmp);

        $zoo_list = "<th $HbgTitleCell>${HtagTH_}動物園${H_tagTH}</th>";
    }

    out(<<END);
<div>ここには、退治した怪獣が載ります。$zookazus<br>
<div align='center'>
<table border><tr>
    <th $HbgTitleCell>${HtagTH_}番号${H_tagTH}</th>
    <th $HbgTitleCell>${HtagTH_}怪獣${H_tagTH}</th>
    <th $HbgTitleCell>${HtagTH_}名前${H_tagTH}</th>
    <th $HbgTitleCell>${HtagTH_}体力${H_tagTH}</th>
    <th $HbgTitleCell>${HtagTH_}残骸の値段${H_tagTH}</th>
    <th $HbgTitleCell>${HtagTH_}経験値${H_tagTH}</TH>$zoo_list</tr>
END

    my ($block);
    my ($flags);
    my ($bit);
    my ($mbase) = 0;
    my ($mkind) = 0;
    my ($zonum) = 0;

    for ($block = 0 ; $block < 5; $block++ ) {

        $zoo_list = '';
        $mbase = $block * 32;   #32bit
        if (defined $island->{'taiji_list'}[$block]) {
            $flags = $island->{'taiji_list'}[$block];

            my ($maxHP);

            for ($bit = 0 ; $bit < 32; $bit++) {

                $mkind = $mbase + $bit;

                if (GetTaijiFlag($island,$mkind)) {

                    if ($zookazu) {

                        $zonum = 0 ;
                        if ($mons_list[$mkind]) {
                            $zonum = $mons_list[$mkind] ;
                        }
                        $zoo_list = "<td>$zonum</td>";
                    }

                    $maxHP = $HmonsterBHP[$mkind] + $HmonsterDHP[$mkind];
        out(<<END);
<tr><td $HbgTitleCell>$mkind</td><td><img src='./${HMapImgDir}$HmonsterImage[$mkind]'></td><td>$HmonsterName[$mkind]</TD><TD>$HmonsterBHP[$mkind]〜$maxHP</TD><TD>$HmonsterValue[$mkind]</TD><TD>$HmonsterExp[$mkind]</TD>$zoo_list</TR>
END
                }
            }
        }
        else {

            last;
        }
    }
    out(<<END);
</TABLE>
</div>
END

}

#----------------------------------------------------------------------
# たいじ
sub GetTaijiFlag {
    my ($island, $mKind) = @_;

    my ($block) = int($mKind/32);
    my ($mMask);

    $mMask = ($mKind % 32);

    if (defined $island->{'taiji_list'}[$block]) {
        my ($flag) = $island->{'taiji_list'}[$block];

        if ($flag & (1 << $mMask)) {

            return 1;
        }
    }
    return 0;
}


#----------------------------------------------------------------------
# コマンド削除
sub tempCommandDelete {
    out(<<END);
<span class='big'>コマンドを削除しました</span><hr>
END
}
#----------------------------------------------------------------------
# コマンド登録
sub tempCommandAdd {
    out(<<END);
<span class='big'>コマンドを登録しました</span><hr>
END
}
#----------------------------------------------------------------------
# コメント変更成功
sub tempComment {
    out(<<END);
<span class='big'>コメントを更新しました</span><hr>
END
}
#----------------------------------------------------------------------
# toto変更成功
sub tempToto {
    out(<<END);
<span class="big">変更しました</span><hr>
END
}
#----------------------------------------------------------------------
# shuto変更成功
sub tempShuto {
    out(<<END);
<span class="big">首都名を変更しました</span><hr>
END
}
#----------------------------------------------------------------------
# shuto変更失敗
sub tempShutoWrong {
    out(<<END);
<span class='big'>その首都名には変更できません</span><hr>
END
}

#----------------------------------------------------------------------
# shuto変更成功
sub tempTeam {
    out(<<END);
<span class='big'>チーム名を変更しました</span><hr>
END
}
#----------------------------------------------------------------------
# shuto変更失敗
sub tempTeamWrong {
    out(<<END);
<span class='big'>そのチーム名には変更できません</span><hr>
END
}


#----------------------------------------------------------------------
# 近況
sub tempRecent {
    my ($mode, $mode2) = @_;

    if ($mode2) {
        my ($enPass) = $HdefaultPassword;
        my ($pass) = $mode ? "<INPUT type=hidden name=PASSWORD value=$enPass size=16 maxlength=16>" : '';
        out(<<END);
<script type="text/javascript">
<!--
function Recent(){
    newRecent = window.open("${HbaseDir}/history.cgi?ID=$HcurrentID", "newRecent", "menubar=yes,toolbar=no,location=no,directories=no,status=no,scrollbars=yes,resizable=yes,width=800,height=300");
    document.recentForm.target = "newRecent";
    document.recentForm.method = "post";
    document.recentForm.submit();
}
//-->
</script>
<hr>
<div id='RecentlyLog'>
  <div align='center'>
    <h2>${HtagName_}${HcurrentName}${H_tagName}の近況</h2>
    <form name="recentForm" action="${HbaseDir}/history.cgi" method="post">
      <input type="hidden" name="ID" value="$HcurrentID">
$pass
      <input type="submit" value="近況を見る" onClick="Recent()">
    </form>
  </div>
</div>
END
    }
    else {
        out(<<END);
<div id='RecentlyLog'>
<hr>
<h2>${HtagName_}${HcurrentName}${H_tagName}の近況</h2>
END
        logPrintLocal($mode);
        out("</DIV>");
    }
}


#----------------------------------------------------------------------
# 島の移動
sub islandJamp {
    my ($wmode) = @_;
    $HtargetList = getIslandList($HcurrentID, 1);

    my $jumptag;
    if ($wmode) {
        $jumptag = "if (url != \"\" ) window.open(\"$HthisFile?SightC=\"+url);";
    }
    else {
        $jumptag = "if (url != \"\" ) location.href = \"$HthisFile?Sight=\"+url;";
    }
    out(<<END);
<script type="text/javascript">
function jump(theForm) {
    var sIndex = theForm.urlsel.selectedIndex;
    var url = theForm.urlsel.options[sIndex].value;
    $jumptag
}
</script>
<center>
<form name="urlForm">
  <table align='center' border='0'>
    <tr>
      <td>
        <select name="urlsel">
$HtargetList
        </select><BR>
      </td>
      <td>
        <input type="button" value=" GO " onClick="jump(this.form)">
      </td>
    </tr>
  </table>
</form>
</center>
END
}


#----------------------------------------------------------------------
sub exLbbs {
    my ($bbsID, $mode) = @_;

    my ($admin, $id) = ('', '');
    if ($mode == 1) {

        $mode = 'yes';
        $id = $bbsID;
        my ($island) = $Hislands[$HidToNumber{$bbsID}];
        my ($onm) = $island->{'onm'};
        $onm = "$island->{'name'}$AfterName" if($onm eq '');
        $admin =<<"END";
<input type='hidden' name='name' value='$onm'>
<input type='hidden' name='title' value='$island->{'name'}$AfterName観光掲示板'>
<input type='hidden' name='message' value='ようこそ！$island->{'name'}$AfterName観光案内所へ'>
END
    }
    elsif ($defaultID ne '') {

        $mode = 'no';
        $id = $defaultID;
    }
    else {
        $mode = '';
    }

    out(<<END);
<script type="text/javascript">
<!--
function Exlbbs(){
    newExlbbs = window.open("", "newExlbbs", "menubar=yes,toolbar=no,location=no,directories=no,status=yes,scrollbars=yes,resizable=yes,width=600,height=300");
    document.exLbbs.target = "newExlbbs";
//    document.exLbbs.submit();
}
//-->
</script>
<DIV ID='localBBS'>
<HR>
<h2><span class='Nret'>${HtagName_}${HcurrentName}${AfterName}${H_tagName}</span><span class='Nret'>観光者通信</span></h2>
<form name="exLbbs" action="${HlbbsDir}/lbbs.cgi" method=POST encType=multipart/form-data>
  <input type="hidden" name="mode" value='view'>
  $admin
  <input type="hidden" name='owner' value="$mode">
  <input type="hidden" name='logfile' value="${bbsID}.cgi">
  <input type="hidden" name='id' value="$id">
  <input type="hidden" name='pass' value="$HdefaultPassword">
  <input type="submit" value='観光掲示板の閲覧・投稿' onClick="Exlbbs()">
</form>
</div>
END
}

1;
