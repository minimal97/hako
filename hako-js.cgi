#----------------------------------------------------------------------
# ＪＡＶＡスクリプト版 -ver1.11-
# 使用条件、使用方法等は、配布元でご確認下さい。
# 付属のjs-readme.txtもお読み下さい。
# あっぽー：http://appoh.execweb.cx/hakoniwa/
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# 外部jsファイル作成
#----------------------------------------------------------------------
sub makeJS {
    my($mode) = @_;

    my($src);
    my($mons_name);

    $mons_name = 'monsnm = [';

    {
        my($l);
        my($temp);
        my($cn);
        my($cnt) = 0;
        $cn = '';

        foreach $l (@HmonsterName) {
            $temp = '""';
            if ($HmonsterZoo[$cnt]) {
                $temp = "\"$l\"";
            }
            $mons_name = $mons_name . $cn . $temp;
            $cn = ',';
            $cnt++;
        }
        $mons_name = $mons_name . "];\n";
    }

    $src = <<"END";

function init() {
    var i;
    var s;
    var str;

    for(i = 0; i < command.length ;i++) {
        for(s = 0; s < $com_count ;s++) {
            var comlist2 = comlist[s];
            for(j = 0; j < comlist2.length ; j++) {
                if(command[i][0] == comlist2[j][0]) {
                    g[i] = comlist2[j][1];
                }
            }
        }
    }
    outp();
    str = plchg(0);
    str = "<TABLE border=0><TR><TD class='commandjs1'><B>−−−− 送信済み −−−−</B><br><br>"+str+"<br><B>−−−− 送信済み −−−−</B></TD></TR></TABLE>";
    disp(str, "#ccffcc");

    check_menu();
    if((document.layers) || (document.all)){  // IE4、IE5、NN4
        window.document.onmouseup = menuclose;
    }
}

function cominput(theForm, x, k) {
    map_cmd_chg = true;
    a = theForm.NUMBER.options[theForm.NUMBER.selectedIndex].value;
    b = theForm.COMMAND.options[theForm.COMMAND.selectedIndex].value;
    c = theForm.POINTX.options[theForm.POINTX.selectedIndex].value;
    d = theForm.POINTY.options[theForm.POINTY.selectedIndex].value;
    e = theForm.AMOUNT.options[theForm.AMOUNT.selectedIndex].value;
    f = theForm.TARGETID.options[theForm.TARGETID.selectedIndex].value;
    if(x == 6){ b = k; menuclose();    }
    if (x == 1 || x == 6){
        for(i = $HcommandMax - 1; i > a; i--) {
            command[i] = command[i-1];
            g[i] = g[i-1];
        }
    }else if(x == 3){
        for(i = Math.floor(a); i < ($HcommandMax - 1); i++) {
            command[i] = command[i + 1];
            g[i] = g[i+1];
        }
        command[$HcommandMax-1] = [$HcomDoNothing,0,0,0,0];
        g[$HcommandMax-1] = '資金繰り';
        str = plchg(a);
        str = "<TABLE border=0><TR><TD class='commandjs2'><B>＝＝＝＝ 未送信 ＝＝＝＝</B><br><br>"+str+"<br><B>＝＝＝＝ 未送信 ＝＝＝＝</B></TD></TR></TABLE>";
        disp(str,"white");
        outp();
        return true;
    }else if(x == 4){
        i = Math.floor(a)
            if (i == 0){ return true; }
        i = Math.floor(a)
            tmpcom1[i] = command[i];tmpcom2[i] = command[i - 1];
        command[i] = tmpcom2[i];command[i-1] = tmpcom1[i];
        k1[i] = g[i];k2[i] = g[i - 1];
        g[i] = k2[i];g[i-1] = k1[i];
        ns(--i);
        str = plchg(i);
        str = "<TABLE border=0><TR><TD class='commandjs2'><B>＝＝＝＝ 未送信 ＝＝＝＝</B><br><br>"+str+"<br><B>＝＝＝＝＝未送信 ＝＝＝＝</B></TD></TR></TABLE>";
        disp(str,"white");
        outp();
        return true;
    }else if(x == 5){
        i = Math.floor(a)
            if (i == $HcommandMax-1){ return true; }
        tmpcom1[i] = command[i];tmpcom2[i] = command[i + 1];
        command[i] = tmpcom2[i];command[i+1] = tmpcom1[i];
        k1[i] = g[i];k2[i] = g[i + 1];
        g[i] = k2[i];g[i+1] = k1[i];
        ns(++i);
        str = plchg(i);
        str = "<TABLE border=0><TR><TD class='commandjs2'><B>＝＝＝＝ 未送信 ＝＝＝＝</B><br><br>"+str+"<br><B>＝＝＝＝ 未送信 ＝＝＝＝</B></TD></TR></TABLE>";
        disp(str,"white");
        outp();
        return true;
    }

    for(s = 0; s < $com_count ;s++) {
        var comlist2 = comlist[s];
        for(i = 0; i < comlist2.length; i++){
            if(comlist2[i][0] == b){
                g[a] = comlist2[i][1];
                break;
            }
        }
    }
    command[a] = [b,c,d,e,f];
    ns(++a);
    str = plchg(a);
    str = "<TABLE border=0><TR><TD class='commandjs2'><B>＝＝＝＝ 未送信 ＝＝＝＝</B><br><br>"+str+"<br><B>＝＝＝＝ 未送信 ＝＝＝＝</B></TD></TR></TABLE>";
    disp(str, "white");
    outp();
    return true;
}

// 新しい クリックイベント
function cmd_click(i) {

    ns(i);
    if(document.getElementById){
        if (document.getElementById("LINKMSG1").innerHTML.indexOf("未送信") > 0){
          nosend=true;
        }else{
          nosend=false;
        }
    } else if(document.all){
        el = document.all("LINKMSG1");
        if (el.innerHTML.indexOf("未送信") > 0 ){
          nosend=true;
        }else{
          nosend=false;
        }
    }
    str = plchg(i);
    if(nosend){
        str = "<TABLE border=0><TR><TD class='commandjs2'><B>＝＝＝＝ 未送信 ＝＝＝＝</B><br><br>"+str+"<br><B>＝＝＝＝ 未送信 ＝＝＝＝</B></TD></TR></TABLE>";
        disp(str, "white");
    }else{
        str = "<TABLE border=0><TR><TD class='commandjs1'><B>−−−− 送信済み −−−−</B><br><br>"+str+"<br><B>−−−− 送信済み −−−−</B></TD></TR></TABLE>";
        disp(str, "#ccffcc");
    }
    outp();

    return true;
}

$mons_name

function plchg( selnm ) {
    var farmpic = '';
    strn1 = '';
    var cmd;
    var suu;
    var d;
    var kind;
    var tgt;
    var strn2;

    var i;

    for(i = 0; i < $HcommandMax; i++)    {
        d = 0;
        c = command[i];
        if(g[i] == 0) { g[i] = 'このコマンドは使えなくなりました'; }
        kind = '$HtagComName_' + g[i] + '$H_tagComName';
        x = c[1];
        y = c[2];
        d = 0;
        tgt = '';
        point = '${HtagName_}(' + x + ',' + y + ')${H_tagName}';
        for(j = 0; j < islname.length ; j++) {
            if(c[4] == islname[j][0]){
                tgt = '$HtagName_' + islname[j][1] + '${H_tagName}';
                break;
            } 
        }
        if(tgt == ''){
            tgt = '無人島';
        }
        cmd = c[0];
        suu = c[3];
        if(cmd == $HcomDoNothing ||
           cmd == $HcomSave ||
           cmd == $HcomLoad ||
           cmd == $HcomGiveup){ // 資金繰り、島の放棄
               strn2 = kind;
        }else if(cmd == $HcomAlly) { // 同盟 加盟・脱退
            strn2 = tgt + 'の' + kind;
        }else if(cmd == $HcomArmSupply){ // 軍事物資調達
            if(suu == 0){ suu = 1; }
            arg = '($HtagName_' + suu + '個${H_tagName})';
            strn2 = kind + arg;
        }else if(cmd == $HcomMissileNM || // ミサイル関連
                 cmd == $HcomMissilePP ||
                 cmd == $HcomMissileSPP ||
                 cmd == $HcomMissileST ||
                 cmd == $HcomMissileSS ||
                 cmd == $HcomMissileLR ||
                 cmd == $HcomMissileLD){
            if(suu == 0){
                arg = '($HtagName_無制限${H_tagName})';
            } else {
                arg = '($HtagName_' + suu + '発${H_tagName})';
            }
            strn2 = tgt + point + 'へ' + kind + arg;
        }else if(cmd == $HcomEiseiLzr){ // 人工衛星レーザー
            d = 1;
            strn2 = tgt + point + 'へ' + kind;
        }else if(  (cmd == $HcomSendMonster)
                 ||(cmd == $HcomSendPirates)){ // 怪獣派遣
            strn2 = tgt + 'へ' + kind;
        }else if(cmd == $HcomSell){ // 食料輸出
            if(suu == 0){ suu = 1; }
            arg = suu * (- ($HcomCost[$HcomSell]));
            arg = '($HtagName_' + arg + '$HunitFood${H_tagName})';
            strn2 = kind + arg;
        }else if(cmd == $HcomPropaganda){ // 誘致活動
            if(suu == 0){ suu = 1; }
            if(suu == 1){
                strn2 = kind;
            } else {
                arg = '($HtagName_' + suu + '回${H_tagName})';
                strn2 = kind + arg;
            }
        }else if(cmd == $HcomMoney){ // 資金援助
            if(suu == 0){ suu = 1; }
            arg = suu * $HcomCost[$HcomMoney];
            arg = '($HtagName_' + arg + '$HunitMoney${H_tagName})';
            strn2 = tgt + 'へ' + kind + arg;
        }else if(cmd == $HcomFood){ // 食料援助
            if(suu == 0){ suu = 1; }
            arg = suu * (- ($HcomCost[$HcomFood]));
            arg = '($HtagName_' + arg + '$HunitFood${H_tagName})';
            strn2 = tgt + 'へ' + kind + arg;
        }else if(cmd == $HcomDestroy){ // 掘削
            d = 1;
            if(suu == 0){
                strn2 = point + 'で' + kind;
            } else {
                arg = suu * $HcomCost[$HcomDestroy];
                arg = '(予\算$HtagName_' + arg + '$HunitMoney${H_tagName})';
                strn2 = point + 'で' + kind + arg;
            }
        }else if(cmd == $HcomOnsen){ // 温泉掘削
            d = 1;
            if(suu == 0){ suu = 1; }
            arg = suu * $HcomCost[$HcomOnsen];
            arg = '(予\算$HtagName_' + arg + '$HunitMoney${H_tagName})';
            strn2 = point + 'で' + kind + arg;
        }else if(cmd == $HcomFarm || // 農場、工場、採掘場整備
                 cmd == $HcomFoodim ||
                 cmd == $HcomFactory ||
                 cmd == $HcomNursery ||
                 cmd == $HcomBoku ||
                 cmd == $HcomPark ||
                 cmd == $HcomUmiamu ||
                 cmd == $HcomMountain ||
                 cmd == $HcomKai ||
                 cmd == $HcomHTget ||
                 cmd == $HcomGivefood ||
                 cmd == $HcomPropaganda) {
            d = 1;
            if(suu == 0){ suu = 1; }
            if(suu != 1){
                arg = '($HtagName_' + suu + '回${H_tagName})';
                strn2 = point + 'で' + kind + arg;
            }else{
                strn2 = point + 'で' + kind;
            }
        }else if(cmd == $HcomMine) { // 地雷設置
            d = 1;
            if(suu == 0){ suu = 1; }
            if(suu > 9){ suu = 9; }
            arg = '(ダメージ$HtagName_' + suu + '${H_tagName})';
            strn2 = point + 'で' + kind + arg;

        }else if(cmd == $HcomZoo) { // 動物園
            d = 1;
            if (suu > $#HmonsterName) {
                suu = $#HmonsterName;
            }
            if (monsnm[suu]) {
            }else{
                suu = 0;
            }
            arg = '($HtagName_' + monsnm[suu] + '${H_tagName})';
            strn2 = point + 'で' + kind +'もしくは'+ arg + '脱出';

        }else if(cmd == $HcomItemUse) { // アイテムおく
            d = 1;
            arg = '($HtagName_' + suu + '${H_tagName})';
            strn2 = point + 'で' + kind + arg;
        }else if(cmd == $HcomItemThrow) { // アイテム捨てる
            d = 1;
            arg = '($HtagName_' + suu + '${H_tagName})';
            strn2 = kind + arg;
        }else if(cmd == $HcomHouse) { // 自宅 税率
            d = 1;
            arg = '($HtagName_' + suu + '${H_tagName})';
            strn2 = point + 'で' + kind + arg;
        }else if (   (cmd == $HcomFarmcpc)  ) {        // 牧場
            d = 1;
            arg = '($HtagName_' + suu + '${H_tagName})';
            if(suu == 2) {
                strn2 = point + 'で' + kind + arg + '(${HtagName_}養豚場${H_tagName})';
            } else if(suu == 3) {
                strn2 = point + 'で' + kind + arg + '(${HtagName_}牧場${H_tagName})';
            } else {
                strn2 = point + 'で' + kind + arg + '(${HtagName_}養鶏場${H_tagName})';
            }

        }else if ((cmd == $HcomHaribote) ) {
            d = 1;
            if(suu == 0){
                strn2 = point + 'で' + kind;
            } else {
                arg = '($HtagName_' + suu + '${H_tagName})';
                strn2 = point + 'で' + kind + arg;
            }
        }else if(cmd == $HcomMonument){ // 記念碑建設
            d = 1;
            if((suu>=$HmonumentNumber)&&(suu!=94)){suu=0;}
            arg = '($HtagName_' + suu + ':' + monument_tag[suu] +'<img SRC="'+monument_img_tag[suu] +'" width=16 height=16' + '>' + '${H_tagName})';
            strn2 = point + 'で' + kind + arg;
        }else if(cmd == $HcomFune){ // 造船
            d = 1;
            if(( (suu != 77) && (suu >= $HfuneNumber)) || (suu == 0)) { suu = 1; }
            if(suu == 1){ arg = '<B>$HfuneName[1]</B><img src="${HMapImgDir}$HfuneImage[1]" width=16 height=16 alt="">'; }
            else if(suu == 2){ arg = '<B>$HfuneName[2]</B><img src="${HMapImgDir}$HfuneImage[2]" width=16 height=16 alt="">'; }
            else if(suu == 3){ arg = '<B>$HfuneName[3]</B><img src="${HMapImgDir}$HfuneImage[3]" width=16 height=16 alt="">'; }
            else if(suu == 4){ arg = '<B>$HfuneName[4]</B><img src="${HMapImgDir}$HfuneImage[4]" width=16 height=16 alt="">'; }
            else if(suu == 5){ arg = '<B>$HfuneName[5]</B><img src="${HMapImgDir}$HfuneImage[5]" width=16 height=16 alt="">'; }
            else if(suu == 6){ arg = '<B>$HfuneName[6]</B><img src="${HMapImgDir}$HfuneImage[6]" width=16 height=16 alt="">'; }
            else if(suu == 7){ arg = '<B>$HfuneName[7]</B><img src="${HMapImgDir}$HfuneImage[7]" width=16 height=16 alt="">'; }
            else if(suu == 8){ arg = '<B>$HfuneName[8]</B><img src="${HMapImgDir}$HfuneImage[8]" width=16 height=16 alt="">'; }
            else if(suu == 9){ arg = '<B>$HfuneName[9]</B><img src="${HMapImgDir}$HfuneImage[9]" width=16 height=16 alt="">'; }
            else if(suu == 10){ arg = '<B>$HfuneName[10]</B><img src="${HMapImgDir}$HfuneImage[10]" width=16 height=16 alt="">'; }
            else if(suu == 11){ arg = '<B>$HfuneName[11]</B><img src="${HMapImgDir}$HfuneImage[11]" width=16 height=16 alt="">'; }
            else if(suu == 12){ arg = '<B>$HfuneName[12]</B><img src="${HMapImgDir}$HfuneImage[12]" width=16 height=16 alt="">'; }
            else if(suu == 77){ arg = '<B>海上都市</B><img src="${HMapImgDir}land39.gif" width="16" height="16" alt="">'; }
            strn2 = point + 'で' + kind +'('+arg+')';
        }else if(cmd == $HcomEisei || // 人工衛星発射、メンテ、破壊
                 cmd == $HcomEiseimente ||
                 cmd == $HcomEiseiAtt) {
            if((suu >= 7) || (suu == 0)) { suu = 1; }
            if((cmd == $HcomEiseimente)&&((suu >5) || (suu == 0))) { suu = 1; } // イレギュラーを修復しない
            if(suu == 1){ arg = '<B>$HeiseiName[1]</B>'; }
            else if(suu == 2){ arg = '<B>$HeiseiName[2]</B>'; }
            else if(suu == 3){ arg = '<B>$HeiseiName[3]</B>'; }
            else if(suu == 4){ arg = '<B>$HeiseiName[4]</B>'; }
            else if(suu == 5){ arg = '<B>$HeiseiName[5]</B>'; }
            else if(suu == 6){ arg = '<B>$HeiseiName[6]</B>'; }
            if(cmd == $HcomEisei){
                strn2 = '$HtagComName_' + arg + '打ち上げ$H_tagComName';
            } else if(cmd == $HcomEiseimente){
                strn2 = '$HtagComName_' + arg + '修復$H_tagComName';
            } else if(cmd == $HcomEiseiAtt){
                strn2 = tgt + 'の' + arg + 'へ' + kind;
            }
        }else{
            d=1;
            strn2 = point + 'で' + kind;
        }
        tmpnum = (i + 1);
        if(i < 9){ tmpnum = '0' + tmpnum; }
        if(i ==selnm){
            strn2 = '<u>'+strn2+'</u>';
            tmpnum = '●' + tmpnum;
            map_cur(x,y,d);
        }else{
            tmpnum = '○' + tmpnum;
        }
        strn1 +=
            '<A STYLE="text-decoration:none;" HREF="JavaScript:void(0);" onClick="cmd_click(' + i + ')">$HtagNumber_' +
                tmpnum + ':$H_tagNumber<FONT SIZE=-1>$HnormalColor_' +
                    strn2 + '$H_normalColor</FONT></A><BR>\\n';
    }
    return strn1;
}

function map_cur(x,y,d) {
  var p_x;
  StyElm = document.getElementById("map_cur");
  if(d) {
    StyElm.style.visibility = "visible";
    p_x = 0;
    if(!(y%2)){p_x=16;}
    StyElm.style.Height = 2; // y は固定
    StyElm.style.marginLeft = ((x) * 32)-2 + (p_x);
    StyElm.style.marginTop = (y+2) * 32-2; // y は固定
  }else{
    StyElm.style.visibility = "hidden";
  }
}

function disp(str,bgclr) {
    if(str == null)  str = "";

    if(document.getElementById){
        document.getElementById("LINKMSG1").innerHTML = str;
//      document.getElementById("plan").bgColor = bgclr;
    } else if(document.all){
        el = document.all("LINKMSG1");
        el.innerHTML = str;
//      document.all.plan.bgColor = bgclr;
    } else if(document.layers) {
        lay = document.layers["PARENT_LINKMSG"].document.layers["LINKMSG1"];
        lay.document.open();
        lay.document.write("<font style='font-size:11pt'>"+str+"</font>");
        lay.document.close();
//      document.layers["PARENT_LINKMSG"].bgColor = bgclr;
    }
}

function outp() {
    var comary = "";

    for(k = 0; k < command.length; k++){
        comary = comary + command[k][0]
            +" "+command[k][1]
                +" "+command[k][2]
                    +" "+command[k][3]
                        +" "+command[k][4]
                            +" ";
    }
    document.myForm.COMARY.value = comary;
}

function ps(x, y) {
    with (document.myForm) {
        elements[4].options[x].selected = true;
        elements[5].options[y].selected = true;
        with (elements[7]) {
            var i;
            for (i = 0; i < length; i++) {
                if (options[i].value == d_ID) {
                    options[i].selected = true;
                    break;
                }
            }
        }
    }
    document.allForm.POINTX.value = x;
    document.allForm.POINTY.value = y;
    if(!(document.myForm.MENUOPEN.checked))
        moveLAYER("menu",mx,my);
    return true;
}

function ns(x) {
    if (x == $HcommandMax){ return true; }
    document.myForm.elements[0].options[x].selected = true;
    document.allForm.NUMBER.value = x;
    return true;
}

function set_land(x, y, lnd, img) {
    var cmd;
    //com_str = lnd + "";
    com_str = lnd + "\\n";
    for(i = 0; i < $HcommandMax; i++)    {
        c = command[i];
        x2 = c[1];
        y2 = c[2];
        cmd = c[0];
        if(x == x2 && y == y2 && (cmd < 30 ||(cmd > 69 && cmd <= $HcomMax))){
            com_str += "[" + (i + 1) +"]" ;
            kind = g[i];
            if(cmd == $HcomDestroy){
                if(c[3] == 0){
                    com_str += kind;
                } else {
                    arg = c[3] * 200;
                    arg = "(予\算" + arg + "$HunitMoney)";
                    com_str += kind + arg;
                }
            }else if(cmd == $HcomFarm ||
                     cmd == $HcomNursery ||
                     cmd == $HcomFactory ||
                     cmd == $HcomMountain ||
                     cmd == $HcomFoodim ||
                     cmd == $HcomBoku ||
                     cmd == $HcomPark ||
                     cmd == $HcomUmiamu) {
                if(c[3] == 0){ c[3] = 1; }
                if(c[3] != 1){
                    arg = "(" + c[3] + "回)";
                    com_str += kind + arg;
                }else{
                    com_str += kind;
                }
            }else if(cmd == $HcomFune || // 造船、牧場、記念碑建設
                     cmd == $HcomFarmcpc ||
                     cmd == $HcomMonument) {
                if(c[3] == 0){
                    com_str += kind;
                } else {
                    arg = "(" + c[3] + ")";
                    com_str += kind + arg;
                }
            }else{
                com_str += kind;
            }
            com_str += " ";
        }
    }
    document.POPUP.COMSTATUS.value= com_str;
    document.POPUP.NAVIIMG.src= img;
}
//top
function set_com(x, y, land) {
    com_str = land + "\\n";
    for(i = 0; i < $HcommandMax; i++)    {
        c = command[i];
        x2 = c[1];
        y2 = c[2];
        if(x == x2 && y == y2 && (c[0] < 30 ||(c[0] > 69 && c[0] <= $HcomMax))){
            com_str += "[" + (i + 1) +"]" ;
            kind = g[i];
            if(c[0] == $HcomDestroy){
                if(c[3] == 0){
                    com_str += kind;
                } else {
                    arg = c[3] * 200;
                    arg = "(予\算" + arg + "$HunitMoney)";
                    com_str += kind + arg;
                }
            }else if(c[0] == $HcomFarm ||
                     c[0] == $HcomNursery ||
                     c[0] == $HcomFactory ||
                     c[0] == $HcomMountain ||
                     c[0] == $HcomFoodim ||
                     c[0] == $HcomBoku ||
                     c[0] == $HcomPark ||
                     c[0] == $HcomUmiamu) {
                if(c[3] == 0){ c[3] = 1; }
                if(c[3] != 1){
                    arg = "(" + c[3] + "回)";
                    com_str += kind + arg;
                }else{
                    com_str += kind;
                }
            }else if(c[0] == $HcomFune || // 造船、牧場、記念碑建設
                     c[0] == $HcomFarmcpc ||
                     c[0] == $HcomMonument) {
                if(c[3] == 0){
                    com_str += kind;
                } else {
                    arg = "(" + c[3] + ")";
                    com_str += kind + arg;
                }
            }else{
                com_str += kind;
            }
            com_str += " ";
        }
    }
    document.myForm.COMSTATUS.value= com_str;
}

//function not_com() {
//document.myForm.COMSTATUS.value="";
//}

function myisland(theForm,myid) {
    for(i = 0; i < islname.length ;i++) {
        if(islname[i][0] == myid) {
            break;
        }
    }
    theForm.TARGETID.selectedIndex = i;
}
var miniTargetmap;
function jump(theForm, j_mode) {
    var sIndex = theForm.TARGETID.selectedIndex;
    var url = theForm.TARGETID.options[sIndex].value;
    if (url != "") {
        window.self.name = "trap";
        if ( (miniTargetmap == null)||(miniTargetmap.closed) ) {
            miniTargetmap = window.open("$HthisFile?IslandMap=" +url+"&JAVAMODE="+j_mode+ "&FROM_ISLAND=$HcurrentID", "minitar", "menubar=1,toolbar=0,location=0,directories=no,status=1,scrollbars=1,resizable=1,width=700,height=630");
        }else{
            miniTargetmap.location.href = "$HthisFile?IslandMap=" + url + "&JAVAMODE=" + j_mode + "&FROM_ISLAND=$HcurrentID";
            miniTargetmap.focus();
        }
    }
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


function SelectList(theForm) {
    var u, selected_ok;
    if(!theForm){s = ''}
    else { s = theForm.menu.options[theForm.menu.selectedIndex].value; }
    if(s == ''){
        u = 0; selected_ok = 0;
        document.myForm.COMMAND.options.length = All_list;
        for (i=0; i<comlist.length; i++) {
            var command = comlist[i];
            for (a=0; a<command.length; a++) {
                comName = command[a][1] + "(" + command[a][2] + ")";
                document.myForm.COMMAND.options[u].value = command[a][0];
                document.myForm.COMMAND.options[u].text = comName;
                if(command[a][0] == d_Kind){
                    document.myForm.COMMAND.options[u].selected = true;
                    selected_ok = 1;
                }
                u++;
            }
        }
        if(selected_ok == 0)
            document.myForm.COMMAND.selectedIndex = 0;
    } else {
        var command = comlist[s];
        document.myForm.COMMAND.options.length = command.length;
        for (i=0; i<command.length; i++) {
            comName = command[i][1] + "(" + command[i][2] + ")";
            document.myForm.COMMAND.options[i].value = command[i][0];
            document.myForm.COMMAND.options[i].text = comName;
            if(command[i][0] == d_Kind){
                document.myForm.COMMAND.options[i].selected = true;
                selected_ok = 1;
            }
        }
        if(selected_ok == 0) document.myForm.COMMAND.selectedIndex = 0;
    }
}

function chkwindowsize(){ // この関数で、ウィンドウの大きさを調べる。 320x365,372x464
// body.clientWidthは、ページ構築後にしか取得できないので、関数にしてonload後に呼び出してます。
    if (document.all){
        wX = document.body.clientWidth; // 横軸
        wY = document.body.clientHeight; // 縦軸
    } else {
        wX = window.innerWidth;
        wY = window.innerHeight;
    }
// NN用、4.7も6も使える。
}

function moveLAYER(layName,x,y) {
    winX = 240; winY = 350; //ポップアップメニューの横縦のサイズ
    chkwindowsize();
    if(x + winX*3/4 > wX) { cX = -20 - winX; } else { cX = 10; }
    if(y + winY/2 > wY) { cY = 30 - winY; } else if(y + winY > wY){ cY = 30 - winY/2; } else { cY = -30; }
    if(document.getElementById){        //NN6,IE5
        if(document.all){               //IE5
            if(event.clientX + winX*3/4 > wX) { cX = -20 - winX; } else { cX = 10; }
            if(event.clientY + winY/2 > wY) { cY = 30 - winY; } else if(event.clientY + winY > wY){ cY = 30 - winY/2; } else { cY = -30; }
            el = document.getElementById(layName);
            el.style.left= event.clientX + document.body.scrollLeft + cX;
            el.style.top= event.clientY + document.body.scrollTop + cY;
            el.style.display = "block";
            el.style.visibility ='visible';
        }else{
            el = document.getElementById(layName);
            el.style.left=x + cX;
            el.style.top=y + cY;
            el.style.display = "block";
            el.style.visibility ='visible';
        }
    } else if(document.layers){         //NN4
        msgLay = document.layers[layName];
        msgLay.moveTo(x + cX,y + cY);
        msgLay.visibility = "show";
    } else if(document.all){            //IE4
        msgLay = document.all(layName);
        msgLay.style.pixelLeft = x + cX;
        msgLay.style.pixelTop = y + cY;
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

function check_menu() {
    if(!(document.myForm.MENUOPEN.checked)){
        if(document.getElementById){ //NN6,IE5
            document.onmousemove = Mmove;
        } else if(document.layers){ // NN4 KEYDOWNイベントはWin98系で文字化けするのでコメント化
            window.captureEvents(Event.MOUSEMOVE);
//          window.captureEvents(Event.MOUSEMOVE | Event.KEYDOWN);
            window.onMouseMove = Mmove;
        } else if(document.all){ // IE4
            document.onmousemove = Mmove;
        }
        document.allForm.MENUOPEN.value="";
    }else{
        document.allForm.MENUOPEN.value="on";
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
END

    if($mode) {
        open(OUT,">${HefileDir}/hakojima.js");
#        print OUT jcode::sjis($src);
        print OUT $src;
        close(OUT);
        chmod(0666, "${HefileDir}/hakojima.js");
    } else {
        out(<<END);
<SCRIPT Language="JavaScript">
<!--
$src
//-->
</SCRIPT>
END
    }
}

1;
