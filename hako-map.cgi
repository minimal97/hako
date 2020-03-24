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

    if ($HimgLine ne '' ) {
        $baseIMG = $HimgLine;
    } else {
        $baseIMG = $server_config::HimageDir;
    }

    if ($HskinName ne '' ) {
        $baseSKIN = $HskinName;
    } else {
        $baseSKIN = "${efileDir}/$HcssFile";
    }

    if (SEASON_IMAGE_SET && $Hmonth) {
        $seasonIMG = "$HseasonImg[$Hmonth]/";
    } else {
        $seasonIMG = '';
    }

    my ($mapsizeNumber) = $HidToNumber{$defaultID};

    $Hms1 = 16;
    $Hms2 = $Hms1 << 1; # x2

    if (   (USE_GZIP == 1)
        && ($ENV{'HTTP_ACCEPT_ENCODING'}=~/gzip/) ) {

        print qq{Content-type: text/html; charset=EUC-JP\n};
        print qq{Content-encoding: gzip\n\n};
        open(STDOUT,"| $HpathGzip/gzip -1 -c");
        print " " x 2048 if($ENV{HTTP_USER_AGENT}=~/MSIE/);
        print qq{<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\n\n};
    }else{
        print qq{Content-type: text/html; charset=EUC-JP\n\n};
        print qq{<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\n\n};
    }

    out(<<END);
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-JP">
<meta http-equiv="Content-Script-Type" content="text/javascript">
END
    if ($HmainMode eq 'landmap') {
        print "<meta name='viewport' content='width=device-width,initial-scale=1'>" ;
    }else{
        #print '<meta name="viewport" content="width=device-width,initial-scale=1">' ;
    }
    out(<<END);
<meta name="theme-color" content="#99FF99">
<link rel="shortcut icon" href="./img/fav.ico">
<title>$Htitle $Htitle_sub</title>
<base href="${baseIMG}/${seasonIMG}">
<link rel="stylesheet" type="text/css" href="${baseSKIN}">
<style type="text/css">
img.maptile {
  width: ${Hms2}px;
  height: ${Hms2}px;
  border: 0px;
  border-style:hidden;
}

img.maptile_ret {
  width: ${Hms2}px;
  height: ${Hms2}px;
  border: 0px;
  border-style:hidden;
  transform:scale(-1, 1);
}
</style>
</head>
$Body<div id='BodySpecial'>
END

    if (   ($HmainMode eq 'landmap')
        || ($HmainMode eq 'taijilist') ) {

    out(<<END);
<div align='center'>
  <a href=\"#\" onclick=\"window.close()\">${HtagBig_}[閉じる]${H_tagBig}</a>
</div>
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
        }else{
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
    my ($cflag);
    my ($cmd_lp);

    $com_count = @HcommandDivido2;

    for($m = 0; $m < $com_count; $m++) {

        $set_listcom .= "\[ ";

        my (@cmd) = split(/,/,$HcommandDivido2[$m]);
        my ($cmdsetnum) = ($#cmd) + 1;

        for ($cmd_lp = 1 ; $cmd_lp < $cmdsetnum ; $cmd_lp++) {
            $l_kind = $cmd[$cmd_lp];

            # 必要な条件がなければコマンドから除外する
            next if((($l_kind == $HcomSave)||($l_kind == $HcomLoad))&& !($island->{'shr'}));
            next if(($l_kind == $HcomBettown) && ($Hislands[$HcurrentNumber]->{'shutomessage'} == 555));
            next if(($l_kind == $HcomYakusho) && ($Hislands[$HcurrentNumber]->{'shutomessage'} == 555));
            next if(($l_kind == $HcomYakusho) && ($Hislands[$HcurrentNumber]->{'yaku'} > 0));

            # 値段算出
            my($temp_cost);
            $temp_cost = $HcomCost[$l_kind];
            if($temp_cost =~ s/Pointx(.*)$//g) {
                $l_cost = $island->{'pts'} * int($1);
            }else{
                $l_cost = $temp_cost;
            }

            if($l_cost == 0) {
                $l_cost = '無料';
            } elsif($l_cost < 0) {
                $l_cost = - $l_cost;
                $l_cost .= $HunitFood;
            } else {
                $l_cost .= $HunitMoney;
            }

            if (isCommandEnable($l_kind) ) {
                $set_listcom .= "\[$l_kind\,\'$HcomName[$l_kind]\',\'$l_cost\'\]\,\n";
                if(($m > 0) && ($m < 8)) {
                    $click_com[$m] .= "<a title='$l_cost' href='javascript:void(0);' onClick='cominput(myForm,6,$l_kind)' style='text-decoration:none'>$HcomName[$l_kind]<font size='-1'>($l_cost)</font></a><br>\n";
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
    if($HdefaultKind eq ''){
        $default_Kind = 1;
    } else {
        $default_Kind = $HdefaultKind;
    }

    #島リストセット
    my ($set_island, $l_name, $l_id);
    $set_island = "";
    foreach $i (0..$islandNumber) {
        $l_name = islandName($Hislands[$i]);
        $l_name =~ s/<[^<]*>//g;
        $l_name =~ s/'/\\'/g;
        $l_id = $Hislands[$i]->{'id'};
        if($i == $islandNumber){
            $set_island .= "\[$l_id\,\'$l_name\'\]\n";
        }else{
            $set_island .= "\[$l_id\,\'$l_name\'\]\,";
        }
    }

    my ($set_monument_tags);
    my ($set_monument_img_tags);
    for ($i = 0; $i <= 95; $i++) {
        if ($i == 95){
            $set_monument_tags .= "\'$HmonumentName[$i]\'\n";
            $set_monument_img_tags .= "\'${HMapImgDir}$HmonumentImage[$i]\'\n";
        }
        else {
            $set_monument_tags .= "\'$HmonumentName[$i]\'\,";
            $set_monument_img_tags .= "\'${HMapImgDir}$HmonumentImage[$i]\'\,";
        }
    }

    if(EXTRA_JS) {
        unless(-e "${HefileDir}/hakojima.js") {
            require('./hako-js.cgi');
            makeJS(1);
        }
    }

    OwnarMap_Header();

    out(<<END);
<SCRIPT type="text/javascript">
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
  if(map_cmd_chg ){
    event = event || window.event; 
    event.returnValue = '入力中のページから移動しますか？';
  }
}

//-->
</SCRIPT>
END

    MapCommonScript();

    if(EXTRA_JS) {
        out(<<END);
<SCRIPT Language="JavaScript" SRC="${efileDir}/hakojima.js"></SCRIPT>
END
    } else {
        require('./hako-js.cgi');
        makeJS(0);
    }

    out(<<END);
<DIV ID="menu" style="position:absolute; visibility:hidden;">
  <TABLE BORDER=0 class="PopupCell">
  <TR>
    <TD class='T' colspan=2>
      <FORM name='POPUP'>
        <IMG NAME="NAVIIMG" alt='' SRC="" class='maptile' align="left">
        <TEXTAREA style="font-size:0.8em;" NAME="COMSTATUS" cols="48" rows="3" class="popupnavi" style="resize:none;"></TEXTAREA>
      </FORM>
    </TD>
  </TR>
  <TR>
    <TD>
$click_com[1]<hr>
$click_com[2]<hr>
$click_com[7]
    </TD>
    <TD>
$click_com[3]<hr>
$click_com[5]<hr>
$click_com[4]<hr>
$click_com[6]
    </TD>
  </TR>
  <TR>
    <TD colspan=2>
<a href="Javascript:void(0);" onClick="menuclose()" STYlE="text-decoration:none">メニューを閉じる</A>
    </TD>
  </TR>
</TABLE>
</DIV>
END

    islandInfo(1);

    out(<<END);
<!-- # 追加（JS版 ver2.0）ＩＥ６対応------->
<CENTER><TABLE BORDER=0><TR><TD class='M'>
<!---ここまで------------------------------>
<CENTER>
<TABLE BORDER>
<TR valign=top>
<TD $HbgInputCell width=25%>
<CENTER>
<FORM name="myForm" action="$HthisFile" method=POST>
<P>
<B>計画番号</B><SELECT NAME=NUMBER>
END
    # 計画番号
    Plan_number();

    {
    my ($open);
    $open = ($HmenuOpen eq 'CHECKED') ? 'CHECKED' : '';

        out(<<END);
</SELECT><BR>
<HR>
<B>開発計画</B>
<INPUT TYPE="checkbox" NAME="MENUOPEN"onClick="check_menu()" $open>非表示<br>
<SELECT NAME=menu onchange="SelectList(myForm)">
<OPTION VALUE=>全種類
END
    }

    {
        my ($aa);
        my ($t_list);
        for($i = 0; $i < $com_count; $i++) {
            ($aa) = split(/,/,$HcommandDivido2[$i]);
            $t_list .= ("<OPTION VALUE=$i>$aa\n");
        }
        out($t_list);
    }
    out(<<END);
</SELECT><br>
<SELECT NAME=COMMAND>
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
</SELECT>
<HR>
<B>コマンド入力</B><BR><B>
<A HREF=JavaScript:void(0); onClick="cominput(myForm,1)">挿入</A>
　<A HREF=JavaScript:void(0); onClick="cominput(myForm,2)">上書き</A>
　<A HREF=JavaScript:void(0); onClick="cominput(myForm,3)">削除</A>
</B>
<HR>
END
    PointPanel();

    out(<<END);
<B>数量</B><SELECT NAME=AMOUNT>
END

    # 数量
    command_arg();

    my($myislandID) = $defaultTarget;
    $myislandID = $island->{'id'} if($myislandID eq '');

    out(<<END);
</SELECT>
<HR>
<B>目標の${AfterName}</B>：
<B><A HREF=JavaScript:void(0); onClick="jump(myForm, '$HjavaMode')"> 表示 </A></B>
・
<B><A HREF=JavaScript:void(0); onClick="myisland(myForm,'$myislandID')"> 前選択 </A></B><BR>
<SELECT NAME=TARGETID>
$HtargetList<BR>
</SELECT>
<HR>
<B>コマンド移動</B>：
<BIG>
<A HREF=JavaScript:void(0); onClick="cominput(myForm,4)" STYlE="text-decoration:none"> ▲ </A>・・
<A HREF=JavaScript:void(0); onClick="cominput(myForm,5)" STYlE="text-decoration:none"> ▼ </A>
</BIG>
<HR>
<INPUT TYPE="hidden" NAME="COMARY" value="comary">
<INPUT TYPE="hidden" NAME="JAVAMODE" value="$HjavaMode">
<INPUT TYPE="submit" VALUE="計画送信" NAME=CommandJavaButton$Hislands[$HcurrentNumber]->{'id'} onClick="map_cmd_chg=false;">
<br><font size=2>最後に<span class='attention'>計画送信ボタン</span>を<br>押すのを忘れないように。</font>
<HR>
<B>パスワード</B></BR>
<INPUT TYPE="password" NAME="PASSWORD" VALUE="$HdefaultPassword">
</CENTER>
<CENTER><textarea class="popupnavi" style="resize:none;" cols="20" rows="5" id="CMD_HELP">test</textarea></CENTER>
</TD>
<TD $HbgMapCell><center>
<TEXTAREA NAME="COMSTATUS" cols="64" rows="3" style="resize:none;"></TEXTAREA>
</center>
END
    islandMap(1, 1);    # 島の地図、所有者モード
    out(<<END);

</FORM>
</TD>
<TD $HbgCommandCell id="plan">
<FORM name="allForm" action="$HthisFile" method="post">
<INPUT TYPE="hidden" NAME="PASSWORD" VALUE="$HdefaultPassword">
<INPUT TYPE="hidden" NAME="MENUOPEN" VALUE="allmenu">
<INPUT TYPE="hidden" NAME="NUMBER" VALUE="allno">
<INPUT TYPE="hidden" NAME="POINTY" VALUE="0">
<INPUT TYPE="hidden" NAME="POINTX" VALUE="0">
<INPUT TYPE="hidden" NAME="JAVAMODE" value="$HjavaMode">
<DIV ID='AutoCommand'><B>自動系</B><br>
<SELECT NAME=COMMAND>
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
                $s = ($kind == $HdefaultKind) ? 'SELECTED' : '';
                out("<OPTION VALUE=$kind $s>$HcomName[$kind]($cost)\n");
            }
        }
    }

    out(<<END);
</SELECT><br>
<B>伐採数量</B><SELECT NAME=AMOUNT>
END

    command_arg();

    out(<<END);
</SELECT>×200本以上<br>
<INPUT TYPE="hidden" NAME="CommandButton$Hislands[$HcurrentNumber]->{'id'}">
<INPUT TYPE="submit" VALUE="自動系計画送信">
<HR>
</DIV>
<ilayer name="PARENT_LINKMSG" width="100%" height="100%">
  <layer name="LINKMSG1" width="200"></layer>
  <span id="LINKMSG1"></span>
</ilayer><BR>
</FORM>
</TD>
</TR>
</TABLE>
END
    # 持ち物描画
    islandItemData();
    # 各種拡張データ表示
    islandData();

    out(<<END);
</CENTER>
</TD></TR>
</TABLE>
<HR>
END

    # コメント更新 フォーム
    CommentForm($island);

    out(<<END);
<!-- # 追加（JS版 ver2.0）ＩＥ６対応------->
</CENTER>
<!---ここまで------------------------------>
END

}


#----------------------------------------------------------------------
# 計画番号をprint
# <OPTION VALUE=$i> のみ
#----------------------------------------------------------------------
sub Plan_number {

    my($j, $i);
    {
        my ($t_cmdlist) = '';
        $j = 0;
        for($i = 0; $i < $HcommandMax; $i++) {
            $j = $i + 1;
            $t_cmdlist .= ("<OPTION VALUE=$i>$j");
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
    if(!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    # モードで分岐
    my($command) = $island->{'command'};
    for($i = 0; $i < $HcommandMax; $i++) {
        # コマンド登録
        $HcommandComary =~ s/([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*) //;
        my $kind = $1;
        if($kind == 0) {
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
# 観光モード
#----------------------------------------------------------------------
sub printIslandJava {
    # 開放
    unlock();

    my($island);

    # idから島番号を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    $island = $Hislands[$HcurrentNumber];

    # なぜかその島がない場合
    if($HcurrentNumber eq '') {
        tempProblem();
        return;
    }

    # 名前の取得
    $HcurrentName = islandName($Hislands[$HcurrentNumber]);

    #コマンドリストセット
    my($l_kind);
    my($m);
    @click_com[8, 9]  = ('', '');
    if($HjavaMode eq 'java'){
        $com_count = @HcommandDivido2;
        my($temp_cost);
        my($l_cost);

        my($tag_s_s,$tag_s_e);
        my ($flag);
        my ($cmd_lp);

        for($m = 0; $m < $com_count; $m++) {

            if (   ($m == 8)
                || ($m == 9)
                            ) {
            }else{
                next;
            }

            my (@cmd) = split(/,/,$HcommandDivido2[$m]);
            my ($cmdsetnum) = ($#cmd) + 1;

            for ($cmd_lp = 1 ; $cmd_lp < $cmdsetnum ; $cmd_lp++) {
                $tag_s_s = '';
                $tag_s_e = '';
                $l_kind = $cmd[$cmd_lp];

                if (isCommandEnable($l_kind) ) {

                    # 値段算出
                    $temp_cost = $HcomCost[$l_kind];
                    if($temp_cost =~ s/Pointx(.*)$//g) {
                        $l_cost = $island->{'pts'} * int($1);
                    }else{
                        $l_cost = $temp_cost;
                    }

                    if($l_cost == 0) {
                        $l_cost = '無料';
                    } else {
                        $l_cost .= $HunitMoney;
                    }

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

                        if (   ($HcurrentID != $HmyislandID)
                            && ($island->{'pop'} < $HguardPop)) {
                            $tag_s_s = "<s $HcurrentID>";
                            $tag_s_e = '</s>';
                        }
                    }

                    $click_com[$m] .= "<a title='$l_cost' href='javascript:void(0);' onClick='window.opener.cominput(window.opener.document.myForm,6,$l_kind)' STYlE='text-decoration:none'>$tag_s_s$HcomName[$l_kind]<font size='-1'>($l_cost)</font>$tag_s_e</a><br>\n";
#                   $click_com[$m] .= "<a title='$l_cost' href='javascript:void(0);' onClick='window.opener.cominput(window.opener.document.myForm,6,$l_kind)' STYlE='text-decoration:none'>$HcomName[$l_kind]/$l_cost</a><br>\n";
                }
            }
        }
    }

    out(<<END);
<SCRIPT type="text/javascript">
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
//-->
</SCRIPT>
<h2 align='center'>${HtagName_}${HcurrentName}${H_tagName}</h2>
<div id='targetMap'>
END
    islandInfo(0);

    out(<<END);
<div align='center'>
攻撃する地点をクリックして下さい。<br>クリックした地点が開発画面の座標に設定されます。</DIV>
<DIV ID="menu" style="position:absolute; visibility:hidden;">
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
    <a href="Javascript:void(0);" onClick="menuclose()" style="text-decoration:none">メニューを閉じる</A>
  </td>
</tr>
</table>
</div>
END
    if(checkPassword($island, $HdefaultPassword) && ($island->{'id'} eq $defaultID)) {
        islandMap(1, 1);  # 島の地図、観光モード
    } else {
        islandMap(0, 1);  # 島の地図、観光モード
    }

    # 近況
    tempRecent(0, $HuseHistory2);
    out('</DIV>');
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
    if($HcurrentNumber eq '') {
        tempProblem();
        return;
    }

    # 名前の取得
    $HcurrentName = islandName($Hislands[$HcurrentNumber]);

    # 観光画面
    tempPrintIslandHead(); # ようこそ!!
    MapCommonScript();
    islandInfo(0); # 島の情報
    islandMap($HadminMode, 0); # 島の地図、観光モード

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
    my($island) = $Hislands[$HcurrentNumber];
    $HcurrentName = islandName($island);

    # パスワード
    if(!checkPassword($island,$HinputPassword)) {
        # password間違い
        tempWrongPassword();
        return;
    }

    wiiU_ip_check_write($HcurrentID);

    # 開発画面
    if($HjavaMode eq 'java') {
        tempOwnerJava(); # 「Javaスクリプト開発計画」
    }else{               # 「通常モード開発計画」
        tempOwner();
    }

    # ○○島ローカル掲示板
    if($HuseLbbs) {
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
    if(!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    # モードで分岐
    my($command) = $island->{'command'};

    if($HcommandMode eq 'delete') {
        slideFront($command, $HcommandPlanNumber);
        tempCommandDelete();
    } elsif(($HcommandKind == $HcomAutoPrepare) ||
            ($HcommandKind == $HcomAutoPrepare2)) {
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
        while(($j < $HpointNumber) && ($i < $HcommandMax)) {
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
    } elsif(($HcommandKind == $HcomAutoReclaim) ||
            ($HcommandKind == $HcomAutoDestroy)) {
        # 浅瀬埋め立て、浅瀬掘削
        makeRandomPointArray();
        my($land) = $island->{'land'};
        my($landValue) = $island->{'landValue'};

        # コマンドの種類決定
        my($kind) = $HcomReclaim;
        if($HcommandKind == $HcomAutoDestroy) {
            $kind = $HcomDestroy;
        }
        my($i) = 0;
        my($j) = 0;
        while(($j < $HpointNumber) && ($i < $HcommandMax)) {
            my($x) = $Hrpx[$j];
            my($y) = $Hrpy[$j];
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
    } elsif(($HcommandKind == $HcomAutoSellTree) ||
            ($HcommandKind == $HcomAutoForestry)) {
        # 伐採、伐採と植林
        # （数量×２００本より多い森だけが対象）
        makeRandomPointArray();
        my($land) = $island->{'land'};
        my($landValue) = $island->{'landValue'};

        # コマンドの種類決定
        my($kind) = ($HcommandKind == $HcomAutoForestry) ? 1 : 0;
        my($i) = 0;
        my($j) = 0;
        while(($j < $HpointNumber) && ($i < $HcommandMax)) {
            my($x) = $Hrpx[$j];
            my($y) = $Hrpy[$j];
            if (($land->[$x][$y] == $HlandForest) && ($landValue->[$x][$y] > $HcommandArg * 2)) {
                if($kind) {
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
    } elsif($HcommandKind == $HcomAutoDelete) {
        # 全消し
        my($i);
        for($i = 0; $i < $HcommandMax; $i++) {
            slideFront($command, $HcommandPlanNumber);
        }
        tempCommandDelete();
    } else {
        if($HcommandMode eq 'insert') {
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
    my($island) = $Hislands[$HcurrentNumber];
    $HcurrentName = islandName($island);

    # パスワード
    if(!checkPassword($island,$HinputPassword)) {
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
    my($num) = @_;

    # idから島を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my($island) = $Hislands[$HcurrentNumber];

    # パスワード
    if(!checkPassword($island,$HinputPassword)) {
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
    if(!checkPassword($island,$HinputPassword)) {
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
    my($island) = $Hislands[$HcurrentNumber];


    # パスワード
    if(!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    if ( $HYaku_Chg_Yotei == 1 ){
        $island->{'yaku_work'} |= $HYakushoWorkYotei;
    }else{
        $island->{'yaku_work'} &= (0xFF ^ $HYakushoWorkYotei);
    }

    if ( $HYaku_Chg_Narasi == 1 ){
        $island->{'yaku_work'} |= $HYakushoWorkSeiti;
    }else{
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
    my($island) = $Hislands[$HcurrentNumber];

    # パスワード
    if(!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    if($HteamMessage == 555) {
        tempTeamWrong();
    } else {
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
    my($mode) = @_;
    my($i);
    for($i = 0; $i < $HlogMax; $i++) {
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
<SCRIPT Language="JavaScript">
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
    if(document.getElementById){
        for (i = 0; i < $HcommandMax; i++) {
            document.getElementById("CMD_"+i).innerHTML = "○";
        }
        document.getElementById("CMD_"+x).innerHTML = "●";
    }
    return true;
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
</SCRIPT>
END

    islandInfo(1);

    out(<<END);
<DIV align='center'>
<TABLE BORDER='1'>
<TR valign=top>
<TD $HbgInputCell >
</div>
<form name="myForm" action="$HthisFile" method=POST>
<INPUT TYPE=submit VALUE="計画送信" NAME=CommandButton$Hislands[$HcurrentNumber]->{'id'}>
<hr>
<b>パスワード</b></br>
<INPUT TYPE=password NAME=PASSWORD VALUE="$HdefaultPassword">
<hr>
<b>計画番号</b><select name=NUMBER onChange="cmdsl()">
END
    # 計画番号
    my($j, $i);
    Plan_number();

out(<<END);
</select><br>
<hr>
<b>開発計画</b><br>
<font size=-1><select name="COMMAND"></font>
END

    #コマンド
    my($kind, $cost, $s);
    my($temp_cost);
    for($i = 0; $i < $HcommandTotal; $i++) {
        $kind = $HcomList[$i];
        next if((($kind == $HcomSave)||($kind == $HcomLoad))&& !($Hislands[$HcurrentNumber]->{'shr'}));
        next if(($kind == $HcomBettown) && ($Hislands[$HcurrentNumber]->{'shutomessage'} == 555));

        # 値段算出
        $temp_cost = $HcomCost[$kind];
        if($temp_cost =~ s/Pointx(.*)$//g) {
            $cost = $island->{'pts'} * int($1);
        }else{
            $cost = $temp_cost;
        }

        if($cost == 0) {
            $cost = '無料';
        } elsif($cost < 0) {
            $cost = - $cost;
            $cost .= $HunitFood;
        } else {
            $cost .= $HunitMoney;
        }

        $s = ($kind == $HdefaultKind) ? 'selected' : '';
        out("<option value=$kind $s>$HcomName[$kind]($cost)");
    }

    out(<<END);
</select>
<hr>
END

    PointPanel();
    out(<<END);
<B>数量</B><SELECT NAME=AMOUNT>
END

    # 数量 2ですすめてなんとか小さくする。
    command_arg();

    out(<<END);
</select>
<hr>
<b>目標の${AfterName}</b>：
<b><a href="JavaScript:void(0);" onClick="jump(myForm, '$HjavaMode')"> 表\示 </A></B><BR>
<select name=TARGETID>
$HtargetList<br>
</select></font>
<hr>
<b>動作</b><br>
<input type="radio" name="COMMANDMODE" value="insert" checked>挿入
<input type="radio" name="COMMANDMODE" value="write">上書き<br>
<input type="radio" name="COMMANDMODE" value="delete">削除
<hr>
<input type="submit" value="計画送信" name=CommandButton$Hislands[$HcurrentNumber]->{'id'}>
<br>
</center>
</form>
<center><textarea class="popupnavi" style="resize:none;" cols="20" rows="5" id="CMD_HELP">test</textarea></center>
</td>
<td $HbgMapCell>
END

    my $totoyoso = $Hislands[$HcurrentNumber]->{'totoyoso'}->[0];
    my ($mapsize) = $totoyoso;
    if($mapsize =~ /\(mapsize\@(\d+)\)/) {
        if($1 < 1){ $Hms1 = 1;} elsif($1 > 32){ $Hms1 = 32;} else { $Hms1 = $1;}
    }else{
        $Hms1 = 16;
    }
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
        for($i = 0; $i < $HcommandMax; $i++) {
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
</center>
<hr>
END
    CommentForm($island);
}


#----------------------------------------------------------------------
sub PointPanel {
    out(<<END);
<B>座標(</B>
<SELECT NAME=POINTX>
END
    my ($i);
    foreach $i (0..$islandSize) {
        if($i == $HdefaultX) {
            out("<OPTION VALUE=$i SELECTED>$i");
            for ( ; $i > $islandSize ; $i++) { out("<OPTION VALUE=$i>$i"); }
        } else {
            out("<OPTION VALUE=$i>$i");
        }
    }

    out(<<END);
</SELECT>, <SELECT NAME=POINTY>
END

    foreach $i (0..$islandSize) {
        if($i == $HdefaultY) {
            out("<OPTION VALUE=$i SELECTED>$i");
            for ( ; $i > $islandSize ; $i++) { out("<OPTION VALUE=$i>$i"); }
        } else {
            out("<OPTION VALUE=$i>$i");
        }
    }
    out(<<END);
</SELECT><B>)</B>
END

}


#----------------------------------------------------------------------
# コメント更新
#----------------------------------------------------------------------
sub CommentForm {
    my ($island) = @_;
    my ($id) = $island->{'id'};
    out(<<END);
<div id='CommentBox'>
<h2>コメント更新</h2>
<FORM action="$HthisFile" method="POST">
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
<TH>看板1<br><small>(全角${HlengthYoso}字まで)</small></th>
<TD><INPUT TYPE="text" name="YOSOMESSAGE" size="44" value="$totoyoso">
<INPUT TYPE="submit" VALUE="更新" NAME=TotoButton$id>
</td></tr>
<tr>
<TH>看板2<BR><small>(全角${HlengthYoso}字まで)</small></th>
<TD><INPUT TYPE="text" NAME="YOSOMESSAGE2" SIZE="44" VALUE="$totoyoso2">
<INPUT TYPE="submit" VALUE="更新" NAME=TotosButton$id>
</TD></TR>
END

}


#----------------------------------------------------------------------
# チーム名変更フォーム
#----------------------------------------------------------------------
sub TeamNameChangeForm {
    my($island) = @_;

    my $teammessage = $island->{'hakoteam'};
    my $sta_cnt = $island->{'stadiumnum'};

    if ($sta_cnt > 0 ) {
        out(<<END);
<TR>
<TH>チーム名変更<BR><small>(全角${HlengthTeam}字まで)</small></TH>
<TD><INPUT TYPE=text NAME=TEAMMESSAGE SIZE=32 VALUE="$teammessage">
<INPUT TYPE=submit VALUE="チーム名変更" NAME=TeamButton$Hislands[$HcurrentNumber]->{'id'}>
</TD></TR>
<TR>
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

        if ( $Hislands[$HcurrentNumber]->{'yaku_work'} & $HYakushoWorkYotei ){
            $temp_yotei = 'checked="checked"';
        }
        if ( $Hislands[$HcurrentNumber]->{'yaku_work'} & $HYakushoWorkSeiti ){
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
    } else {
        out(<<END);
<tr>
<th>首都名変更<br><small>(全角${HlengthShuto}字まで)</small></th>
<td><input type="text" NAME=SHUTOMESSAGE SIZE=32 VALUE="$shutomessage">
<input type="submit" value="首都名変更" NAME=ShutoButton$Hislands[$HcurrentNumber]->{'id'}>
</td></tr>
<tr>
END
    }
}

#----------------------------------------------------------------------
# 入力済みコマンド表示
sub tempCommand {
    my($number, $command, $shr, $mode) = @_;

    my($kind, $target, $x, $y, $arg) =
        (
            $command->{'kind'},
            $command->{'target'},
            $command->{'x'},
            $command->{'y'},
            $command->{'arg'}
        );
    $HcomName[$kind] = '' if((($kind == $HcomSave)||($kind == $HcomLoad))&& !$shr);

    if ($HcomName[$kind] eq '') { $HcomName[$kind] = "このコマンドは使えなくなりました($kind)"; }
    my ($name) = "$HtagComName_${HcomName[$kind]}$H_tagComName";
    my ($point) = "$HtagName_($x,$y)$H_tagName";
    $target = islandName($Hislands[$HidToNumber{$target}]);
    if ($target eq '') {
        $target = '無人';
    }
    $target = "$HtagName_${target}$H_tagName";

    my ($value) = $arg * $HcomCost[$kind];
    $value = $HcomCost[$kind] if(!$value);
    if($value < 0) {
        $value = -$value;
        $value = "$value$HunitFood";
    } else {
        $value = "$value$HunitMoney";
    }
    $value = "$HtagName_$value$H_tagName";

    my($j) = sprintf("%02d：", $number + 1);

    out("<a style=\"text-decoration:none\" href=\"JavaScript:void(0);\" onClick=\"ns($number);cmdsl();return true;\">") if($mode);
    out("$HtagNumber_<span id=\"CMD_$number\">○</span>$j$H_tagNumber$HnormalColor_");

    my ($command_msg) = '';

    if(($kind == $HcomDoNothing) ||
       ($kind == $HcomSave) ||
       ($kind == $HcomLoad) ||
       ($kind == $HcomGiveup)) {
        $command_msg = "$name";
    } elsif(($kind == $HcomFarm) ||
        ($kind == $HcomFoodim) ||
        ($kind == $HcomFactory) ||
        ($kind == $HcomNursery) ||
        ($kind == $HcomBoku) ||
        ($kind == $HcomPark) ||
        ($kind == $HcomUmiamu) ||
        ($kind == $HcomMountain) ||
        ($kind == $HcomKai) ||
        ($kind == $HcomHTget) ||
        ($kind == $HcomGivefood) ||
        ($kind == $HcomPropaganda)) {
        # 回数付き
        if(($arg == 0) ||
           ($arg == 1)) {
            $command_msg = "$pointで$name" ;
        } else {
            $command_msg = "$pointで$name($arg回)";
        }

    } elsif($kind == $HcomFarmcpc) {
        my ($msg);
        if($arg == 2) {
            $msg = '養豚場';
        }elsif($arg == 3) {
            $msg = '牧場';
        }else{
            $msg = '養鶏場';
        }
        $command_msg = "$pointで$name($arg)$HtagComName_$msg$H_tagComName" ;

    } elsif($kind == $HcomHaribote) {
        # 数付き
        if($arg == 0) {
            $command_msg = ("$pointで$name");
        } else {
            $command_msg = ("$pointで$name($arg)");
        }
    } elsif($kind == $HcomHouse) {
        # 数付き
        $command_msg = ("$pointで$name($arg)");

    } elsif($kind == $HcomItemThrow) {
        # 数付き
        $command_msg = ("$name($arg)");

    } elsif($kind == $HcomMonument) {
        # 数付き
        $arg = 0 if( ($arg >= $HmonumentNumber) && ($arg != 94) );
        $command_msg = ("$pointで$name($HmonumentName[$arg]<IMG SRC=\"${HMapImgDir}$HmonumentImage[$arg]\" width=16 height=16 alt=''>)");
    } elsif($kind == $HcomDestroy) {
        # 掘削
        if ($arg != 0) {
            $command_msg = ("$pointで$name(予算${value})");
        } else {
            $command_msg = ("$pointで$name");
        }
    } elsif ($kind == $HcomOnsen) {
        # 温泉掘削
        $arg = 1 if(!$arg);
        $command_msg = ("$pointで$name(予算${value})");
    } elsif ($kind == $HcomMine) {
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

    } elsif (   ($kind == $HcomSendMonster)
             || ($kind == $HcomSendPirates)) {
        # 怪獣派遣
        $command_msg = ("$targetへ$name");

    } elsif($kind == $HcomSell) {
        # 食料輸出
        $command_msg = ("$name$value");

    } elsif($kind == $HcomFune) {
        # 造船
        if( ($arg != 77 ) && ($arg >= $HfuneNumber) ||
            ($arg == 0) ) {
            $arg = 1;
        }
        my ($t);
        if ( $arg == 77 ) {
            $t = "$HtagName_海上都市$H_tagName<img src=\"${HMapImgDir}land39.gif\" width=16 height=16 alt=''>";
        }
        else {
            $t = "$HtagName_$HfuneName[$arg]$H_tagName<img src=\"${HMapImgDir}$HfuneImage[$arg]\" width=16 height=16 alt=''>";
        }
        $command_msg = ("$pointで$name$t");

    } elsif (   ($kind == $HcomEisei)
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
        } elsif ($kind == $HcomEiseimente) {
            $command_msg = ("$HtagComName_$t修復$H_tagComName");
        } elsif ($kind == $HcomEiseiAtt) {
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
$command_msg$H_normalColor$close_anc
<br>
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
    if($HcurrentNumber eq '') {
        tempProblem();
        return;
    }

    # 名前の取得
    $HcurrentName = islandName($Hislands[$HcurrentNumber]);

    out(<<END);
<DIV align='center'>${HtagBig_}<span class='Nret'>${HtagName_}「${HcurrentName}」${H_tagName}の</span><span class='Nret'>怪獣図鑑</span>${H_tagBig}<BR>
</DIV>

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
    <TH $HbgTitleCell>${HtagTH_}番号${H_tagTH}</TH>
    <TH $HbgTitleCell>${HtagTH_}怪獣${H_tagTH}</TH>
    <TH $HbgTitleCell>${HtagTH_}名前${H_tagTH}</TH>
    <TH $HbgTitleCell>${HtagTH_}体力${H_tagTH}</TH>
    <TH $HbgTitleCell>${HtagTH_}残骸の値段${H_tagTH}</TH>
    <TH $HbgTitleCell>${HtagTH_}経験値${H_tagTH}</TH>$zoo_list</TR>
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

            for ($bit = 0 ; $bit < 32; $bit++ ) {

                $mkind = $mbase + $bit;

                if ( GetTaijiFlag($island,$mkind) ) {

                    if ( $zookazu ) {

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

        }else{

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

        if ($flag & (1 << $mMask) ){

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
    my($mode, $mode2) = @_;

    if ($mode2) {
        my($enPass) = $HdefaultPassword;
        my($pass) = $mode ? "<INPUT type=hidden name=PASSWORD value=$enPass size=16 maxlength=16>" : '';
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
    my($wmode) = @_;
    $HtargetList = getIslandList($HcurrentID, 1);

    my $jumptag;
    if ( $wmode ) {
        $jumptag = "if (url != \"\" ) window.open(\"$HthisFile?SightC=\"+url);";
    }else{
        $jumptag = "if (url != \"\" ) location.href = \"$HthisFile?Sight=\"+url;";
    }
    out(<<END);
<CENTER>
<SCRIPT LANGUAGE="JavaScript">
function jump(theForm) {
    var sIndex = theForm.urlsel.selectedIndex;
    var url = theForm.urlsel.options[sIndex].value;
    $jumptag
}
</SCRIPT>
<FORM name="urlForm">
<TABLE align=center border=0>
<TR><TD>
<SELECT NAME="urlsel">
$HtargetList
</SELECT><BR>
</TD>
<TD><input type="button" value=" GO " onClick="jump(this.form)"></TD>
</TR></TABLE>
</form>
</CENTER>
END
}

#----------------------------------------------------------------------
sub exLbbs {
    my($bbsID, $mode) = @_;

    my ($admin, $id) = ('', '');
    if ($mode == 1) {

        $mode = 'yes';
        $id = $bbsID;
        my ($island) = $Hislands[$HidToNumber{$bbsID}];
        my ($onm) = $island->{'onm'};
        $onm = "$island->{'name'}$AfterName" if($onm eq '');
        $admin =<<"END";
<INPUT type=hidden name=name value='$onm'>
<INPUT type=hidden name=title value='$island->{'name'}$AfterName観光掲示板'>
<INPUT type=hidden name=message value='ようこそ！$island->{'name'}$AfterName観光案内所へ'>
END
    } elsif($defaultID ne '') {

        $mode = 'no';
        $id = $defaultID;
    }
    else {
        $mode = '';
    }

    out(<<END);
<SCRIPT Language="JavaScript">
<!--
function Exlbbs(){
    newExlbbs = window.open("", "newExlbbs", "menubar=yes,toolbar=no,location=no,directories=no,status=yes,scrollbars=yes,resizable=yes,width=600,height=300");
    document.exLbbs.target = "newExlbbs";
//    document.exLbbs.submit();
}
//-->
</SCRIPT>
<DIV ID='localBBS'>
<HR>
<h2><span class='Nret'>${HtagName_}${HcurrentName}${AfterName}${H_tagName}</span><span class='Nret'>観光者通信</span></h2>
<FORM name="exLbbs" action="${HlbbsDir}/lbbs.cgi" method=POST encType=multipart/form-data>
  <INPUT type="hidden" name="mode" value='view'>
  $admin
  <INPUT type="hidden" name=owner value="$mode">
  <INPUT type="hidden" name=logfile value="${bbsID}.cgi">
  <INPUT type="hidden" name=id value="$id">
  <INPUT type="hidden" name=pass value="$HdefaultPassword">
  <INPUT type="submit" value='観光掲示板の閲覧・投稿' onClick="Exlbbs()">
</FORM>
</DIV>
END
}

1;
