#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# 新規作成モジュール(ver1.00)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
#----------------------------------------------------------------------
#
#   ↑から同盟にかかわりそうなものを分割
#       スパゲッティ
#
#----------------------------------------------------------------------
# make で include
# require './hako-const.cgi';

#----------------------------------------------------------------------
# 情報変更モード
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# 同盟の名前からIDを得る
sub aNameToId {
    my ($name) = @_;

    # 全島から探す
    my ($i);
    for ($i = 0; $i < $HallyNumber; $i++) {
        if ($Hally[$i]->{'name'} eq $name) {
            return $Hally[$i]->{'id'};
        }
    }

    # 見つからなかった場合
    return (-1);
}


#----------------------------------------------------------------------
# 同盟のマークからIDを得る
sub aMarkToId {
    my ($mark) = @_;

    # 全島から探す
    my ($i);
    for ($i = 0; $i < $HallyNumber; $i++) {
        if ($Hally[$i]->{'mark'} eq $mark) {
            return $Hally[$i]->{'id'};
        }
    }

    # 見つからなかった場合
    return -1;
}


#----------------------------------------------------------------------
# 同盟の新規作成モード
#----------------------------------------------------------------------
# 結成・変更メイン
sub makeAllyMain {

    my ($adminMode) = 0;
    # パスワードチェック
    if (checkSpecialPassword($HoldPassword)) {
        $adminMode = 1;
        if ($HallyID > 200) {
            my ($max) = $HallyID;
            if ($HallyNumber) {
                foreach (0..$#Hally) {
                    $max = $Hally[$_]->{'id'} + 1 if($max <= $Hally[$_]->{'id'});
                }
            }

            $HcurrentID = $max;
        }
        elsif (defined $HcurrentAnumber) {
            $HcurrentID = $Hally[$HcurrentAnumber]->{'id'};
        }
        else {
            unlock();
            out("${HtagBig_}結成or変更できません。<br>${adminMode}/${HcurrentAnumber}/${HallyID}<br>${H_tagBig}$HtempBack");
            return;
        }
    }

    # 同盟名があるかチェック
    if ($HallyName eq '') {
        unlock();
        $AfterName = '同盟';
        tempNewIslandNoName();
        return;
    }

    # 同盟名が正当かチェック
    if ($HallyName =~ /[,\?\(\)\<\>\$]|^無人|^沈没$/) {
        # 使えない名前
        unlock();
        tempNewIslandBadOwnerName();
        return;
    }

    # 名前の重複チェック
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    if (!($adminMode && ($HallyID ne '') && ($HallyID < 200)) &&
        ((nameToNumber($HallyName) != -1) ||
        ((aNameToId($HallyName) != -1) && (aNameToId($HallyName) != $HcurrentID)))) {
        # すでに結成ずみ
        unlock();
        tempNewAllyAlready();
        return;
    }

    # マークの重複チェック
    if (!($adminMode && ($HallyID ne '') && ($HallyID < 200)) &&
        ((aMarkToId($HallyMark) != -1) && (aMarkToId($HallyMark) != $HcurrentID))) {
        # すでに使用ずみ
        unlock();
        tempMarkAllyAlready();
        return;
    }

    # passwordの判定
    my ($island) = $Hislands[$HcurrentNumber];
    if (!$adminMode && !checkPassword($island,$HinputPassword)) {
        unlock();
        tempWrongPassword();
        return;
    }

    if (!$adminMode && $island->{'money'} < $HcostMakeAlly) {
        unlock();
        tempNoMoney();
        return;
    }

    my ($n) = $HidToAllyNumber{$HcurrentID};

    if (defined $n) {
        if (   ($adminMode)
            && ($HallyID ne '')
            && ($HallyID < 200) ) {

            my $allyMember = $Hally[$n]->{'memberId'};
            my $aIsland = $Hislands[$HidToNumber{$HallyID}];
            my ($flag) = 0;

            foreach (@$allyMember) {
                if ($_ == $HallyID) {
                    $flag = 1;
                    last;
                }
            }

            if (!$flag) {
                $flag = 2 if(@{$aIsland->{'allyId'}}[0] eq '');
            }

            if (!$flag) {
                unlock();
                out("${HtagBig_}変更できません。${H_tagBig}$HtempBack");
                return;
            }

            $Hally[$n]->{'id'}       = $HallyID;
            $Hally[$n]->{'oName'}    = $aIsland->{'name'};
            if ($flag == 2) {
                $Hally[$n]->{'password'} = $aIsland->{'password'};
                $Hally[$n]->{'score'}    = $aIsland->{'pts'};
                $Hally[$n]->{'number'}++;
                push(@{$Hally[$n]->{'memberId'}}, $aIsland->{'id'});
                push(@{$aIsland->{'allyId'}}, $aIsland->{'id'});
            }
        }
        else {
            # すでに結成ずみなら変更
            logChangeAlly($Hally[$n]->{'name'}, $HallyName) if(!$adminMode && ($Hally[$n]->{'name'} ne $HallyName));
        }
    }
    else {
        # 他の島の同盟に入っている場合は、結成できない
        my ($flag) = 0;
        for ($i = 0; $i < $HallyNumber; $i++) {
            my ($allyMember) = $Hally[$i]->{'memberId'};
            foreach (@$allyMember) {
                if ($_ == $HcurrentID) {
                    $flag = 1;
                    last;
                }
            }
            last if ($flag);
        }

        if ($flag) {
            unlock();
            tempOtherAlready();
            return;
        }

        # 新規
        $n = $HallyNumber;
        $Hally[$n]->{'id'} = $HcurrentID;
        my @memberId = ();
        if ($HallyID < 200) {

            $Hally[$n]->{'oName'}    = $island->{'name'};
            $Hally[$n]->{'password'} = $island->{'password'};
            $Hally[$n]->{'number'}   = 1;
            @memberId = ($HcurrentID);
            $Hally[$n]->{'score'}    = $island->{'pts'};
        }
        else {
            $Hally[$n]->{'oName'}    = '';
            $Hally[$n]->{'password'} = encode($HinputPassword);
            $Hally[$n]->{'number'}   = 0;
            $Hally[$n]->{'score'}    = 0;
        }

        $Hally[$n]->{'Takayan'}  = makeRandomString();
        $Hally[$n]->{'occupation'} = 0;
        $Hally[$n]->{'memberId'} = \@memberId;
        $island->{'allyId'} =  \@memberId;
        my @ext = (0, 0, 0);
        $Hally[$n]->{'ext'}      = \@ext;
        $HidToAllyNumber{$HcurrentID} = $n;
        $HallyNumber++;
        logMakeAlly($HallyName, islandName($island)) if(!$adminMode); # ログ
    }

    # 同盟の各種の値を設定
    $Hally[$n]->{'name'}     = $HallyName;
    $Hally[$n]->{'mark'}     = $HallyMark;
    $Hally[$n]->{'color'}    = "#${HallyColor}";

    # 費用をいただく
    $island->{'money'} -= $HcostMakeAlly if(!$adminMode);
    # データ書き出し
    allyOccupy();
    allySort();
    writeIslandsFile();
    $HislandList = getIslandList($HcurrentID, 0);

    # 開放
    unlock();
    # トップへ
    topPageMain();
}


#----------------------------------------------------------------------
# すでにその名前の同盟がある場合
sub tempNewAllyAlready {
    out(<<END);
${HtagBig_}その同盟ならすでに結成されています。${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# すでにそのマークの同盟がある場合
sub tempMarkAllyAlready {
    out(<<END);
${HtagBig_}そのマークはすでに使用されています。${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 別の同盟を結成している
sub tempLeaderAlready {
    out(<<END);
${HtagBig_}盟主は、自分の同盟以外には加盟できません。${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 放置している島は入れない。
sub tempAbsent {
    out(<<END);
${HtagBig_}新規作成された島、もしくは、10ターン前からコマンドが資金繰りだったため、加盟できません。${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 別の同盟に加盟している
sub tempOtherAlready {
    out(<<END);
${HtagBig_}ひとつの同盟にしか加盟できません。${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 資金足りず
sub tempNoMoney {
    out(<<END);
${HtagBig_}資金不足です(/_<。)${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 解散
sub deleteAllyMain {

    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];
    my ($n) = $HidToAllyNumber{$HcurrentID};
    my ($adminMode) = 0;

    # パスワードチェック
    if (checkSpecialPassword($HoldPassword)) {

        $n = $HcurrentAnumber;
        $HcurrentID = $Hally[$n]->{'id'};
        $adminMode = 1;
    }
    else {

        # passwordの判定
        if (!checkPassword($island,$HinputPassword)) {
            unlock();
            tempWrongPassword();
            return;
        }

        if (!checkPassword($Hally[$n],$HinputPassword)) {
            unlock();
            tempWrongPassword();
            return;
        }

        # 念のためIDもチェック
        if ($Hally[$n]->{'id'} != $HcurrentID) {
            unlock();
            tempWrongAlly();
            return;
        }
    }

    # HarmisticeTurn を除外
    my $allyMember = $Hally[$n]->{'memberId'};
    if (   $adminMode
        && (   (@{$allyMember}[0] ne '')
            || !(defined $n))
                                ){
        unlock();
        out("${HtagBig_}削除できません。${H_tagBig}$HtempBack");
        out("n = ${n} / allyMember : @{$allyMember}[0]");
        return;
    }

    foreach (@$allyMember) {
        my($island, $aId, @newId);
        $island = $Hislands[$HidToNumber{$_}];
        @newId = ();

        foreach $aId (@{$island->{'allyId'}}) {
            if ($aId != $HcurrentID) {
                push(@newId, $aId);
            }
        }
        $island->{'allyId'} = \@newId;
    }

    logDeleteAlly($Hally[$n]->{'name'}) if(!$adminMode);
    $Hally[$n]->{'dead'} = 1;
    $HidToAllyNumber{$HcurrentID} = undef;
    $HallyNumber--;
    unlink("${HallychatData}$HcurrentID.cht") if(-e "${HallychatData}$HcurrentID.cht");     # チャットデータを削除

    # データ書き出し
    allyOccupy();
    allySort();
    writeIslandsFile();
    $HislandList = getIslandList($HcurrentID, 0);

    # 開放
    unlock();
    # トップへ
    topPageMain();
}


#----------------------------------------------------------------------
# 実際の削除
sub DeleteAlly{

    # 未作成
}


#----------------------------------------------------------------------
# IDチェックにひっかかる
sub tempWrongAlly {

    out(<<END);
${HtagBig_}あなたは盟主ではないと思う。${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 加盟・脱退
sub joinAllyMain {

    # passwordの判定
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];
    if (!checkPassword($island,$HinputPassword)) {
        unlock();
        tempWrongPassword();
        return;
    }

    # ほかの同盟に参加している。
    if (defined $HidToAllyNumber{$HcurrentID}) {
        unlock();
        tempLeaderAlready();
        return;
    }

    # 新規、または、放置気味の同盟はできない。
    if ($island->{'absent'} > 10) {
        unlock();
        tempAbsent();
        return;
    }

    my $ally = $Hally[$HcurrentAnumber];
    if(   ($HallyJoinOne)
       && ($island->{'allyId'}[0] != 0 )
       && ($island->{'allyId'}[0] != $ally->{'id'}) ) {
        unlock();
        tempOtherAlready();
        return;
    }

    my ($allyMember) = $ally->{'memberId'};
    my @newAllyMember = ();
    my ($flag) = 0;

    foreach (@$allyMember) {

        if (!(defined $HidToNumber{$_})) {
        } elsif($_ == $HcurrentID) {
            $flag = 1;
        } else {
            push(@newAllyMember, $_);
        }
    }

    if ($flag) {
        my @newAlly = ();
        logAllyEnd(islandName($island), $ally->{'name'});

        foreach (@{$island->{'allyId'}}) {
            if ($_ != $ally->{'id'}) {
                push(@newAlly, $_);
            }
        }
        $island->{'allyId'} = \@newAlly;
        $ally->{'score'} -= $island->{'pts'};
        $ally->{'number'}--;

    } else {

        logAlly(islandName($island), $ally->{'name'});
        push(@newAllyMember, $HcurrentID);
        push(@{$island->{'allyId'}}, $ally->{'id'});
        $ally->{'score'} += $island->{'pts'};
        $ally->{'number'}++;
    }
    $island->{'ally_turn'} = 0;
    $island->{'money'} -= $HcomCost[$HcomAlly];
    $ally->{'memberId'} = \@newAllyMember;
    # データ書き出し
    allyOccupy();
    allySort();
    writeIslandsFile();
    $HislandList = getIslandList($HcurrentID, 0);

    # 開放
    unlock();
    # トップへ
    topPageMain();
}


#----------------------------------------------------------------------
# 結成
sub logMakeAlly {
    my ($name, $owner) = @_;
    logHistory("同盟『${HtagName_}${name}${H_tagName}』が${HtagName_}${owner}${H_tagName}によって${HtagNumber_}結成${H_tagNumber}される。");
}


#----------------------------------------------------------------------
# 変更
sub logChangeAlly {
    my ($oldname, $newname) = @_;
    logHistory("同盟「${HtagName_}${oldname}${H_tagName}」が『${HtagName_}${newname}${H_tagName}』に名称変更。");
}


#----------------------------------------------------------------------
# 解散
sub logDeleteAlly {
    my ($name) = @_;
    logHistory("同盟『${HtagName_}${name}${H_tagName}』が${HtagDisaster_}解散！${H_tagDisaster}");
}


#----------------------------------------------------------------------
# 加盟
sub logAlly {
    my ($name, $allyName) = @_;
    logHistory("${HtagName_}${name}${H_tagName}が『${HtagName_}${allyName}${H_tagName}』に${HtagNumber_}加盟${H_tagNumber}。");
}


#----------------------------------------------------------------------
# 脱退
sub logAllyEnd {
    my ($name, $allyName) = @_;
    logHistory("${HtagName_}${name}${H_tagName}が『${HtagName_}${allyName}${H_tagName}』から${HtagDisaster_}脱退！${H_tagDisaster}");
}


#----------------------------------------------------------------------
# 同盟の結成・変更・解散・加盟・脱退
#----------------------------------------------------------------------
# 結成・変更・解散・加盟・脱退
sub newAllyTop {

    my ($adminMode) = 0;
    # パスワードチェック
    if (checkSpecialPassword($HdefaultPassword)) {
        $adminMode = 1;
        $HislandList = getIslandList($Hislands[$HbfieldNumber]->{'id'}, 1);
    }
    # 開放
    unlock();
    my ($jsIslandList, $name, $id, $i);

    foreach $i (0..$islandNumber) {

        $name = htmlEscape($Hislands[$i]->{'name'});
        $id = $Hislands[$i]->{'id'};
        $jsIslandList .= "island[$id] = \"$name\"\;\n";
    }

    my ($allyname, $markList, @colorList, @allycolor, $allyList, 
        $jsAllyList, $jsAllyIdList, $jsAllyMarkList, $jsAllyColorList);
    my ($defaultMark, $defaultAllyId);
    my ($n) = $HidToAllyNumber{$defaultID};
    if ($n eq '') {

        $allyname = '';
        $defaultMark = $Hally[0];
        $defaultAllyId= '';
    }
    else {
        $allyname = $Hally[$n]->{'name'};
        $defaultMark = $Hally[$n]->{'mark'};
        $defaultAllyId = $Hally[$n]->{'id'};
    }

    my ($s);
    foreach (0..$#HallyMark) {

        $s = '';
        $s = ' selected' if ($HallyMark[$_] eq $defaultMark);
        $markList .= "<option value=\"$HallyMark[$_]\"$s>$HallyMark[$_]\n"
    }

    foreach $i (1..6) {

        if ($n eq '') {

            $allycolor[$i] = 0;
        }
        else {

            $allycolor[$i] = substr($Hally[$n]->{'color'}, $i, 1);
        }

        foreach (0..9,A..F) {

            $s = '';
            $s = ' selected' if ($_ eq $allycolor[$i]);
            $colorList[$i] .= "<option value=\"$_\"$s>$_\n"
        }
    }

    my ($max) = 201;

    if ($HallyNumber) {

        $jsAllyList = "ally = [";
        $jsAllyIdList = "allyID = [";
        $jsAllyMarkList = "allyMark = [";
        $jsAllyColorList = "allyColor = [";

        my ($s);
        foreach (0..$#Hally) {

            $s = '';
            $s = ' selected' if ($Hally[$_]->{'id'} == $defaultAllyId);
            $allyList .= "<option value=\"$_\"$s>$Hally[$_]->{'name'}\n";
            $jsAllyList .= "'$Hally[$_]->{'name'}'";
            $jsAllyIdList .= "$Hally[$_]->{'id'}";
            $jsAllyMarkList .= "'$Hally[$_]->{'mark'}'";
            $jsAllyColorList .= "[";

            foreach $i (1..6) {

                $jsAllyColorList .= '\'' . substr($Hally[$_]->{'color'}, $i, 1) . '\'';
                $jsAllyColorList .= ',' if ($i < 6);
            }

            $jsAllyColorList .= "]";
            if ($_ < $#Hally) {

                $jsAllyList .= ",\n";
                $jsAllyIdList .= ",\n";
                $jsAllyMarkList .= ",\n";
                $jsAllyColorList .= ",\n";
            }
            $max = $Hally[$_]->{'id'} + 1 if ($max <= $Hally[$_]->{'id'});
        }
        $jsAllyList .= "];\n";
        $jsAllyIdList .= "];\n";
        $jsAllyMarkList .= "];\n";
        $jsAllyColorList .= "];\n";
    }
    my ($str1) = $adminMode ? '(メンテナンス)' : $HallyJoinComUse ? '' : '・加盟・脱退';
    my ($str2) = $adminMode ? '' : 'onChange=colorPack() onClick=colorPack()';
    my ($makeCost) = $HcostMakeAlly ? "${HcostMakeAlly}${HunitMoney}" : '無料';
    my ($keepCost) = $HcostKeepAlly ? "${HcostKeepAlly}${HunitMoney}" : '無料';
    my ($joinCost) = $HcomCost[$HcomAlly] ? "${$HcomCost[$HcomAlly]}${HunitMoney}" : '無料';
    my ($joinStr) = $HallyJoinComUse ? '' : "加盟・脱退の際の費用は、${HtagMoney_}$joinCost${H_tagMoney}です。<br>";
    my ($str3) = $adminMode ? "特殊パスワードは？（必須）<br>
<input type=\"password\" name=\"OLDPASS\" value=\"$HdefaultPassword\" size='32' maxlength='32' class='f'><br>同盟" : "<span class='attention'>(注意)</span><br>
同盟の結成・変更の費用は、${HtagMoney_}${makeCost}${H_tagMoney}です。<br>
また、毎ターン必要とされる維持費は${HtagMoney_}$keepCost${H_tagMoney}です。<br>
（維持費は同盟に所属する${AfterName}で均等に負担することになります）<br>
$joinStr
</p>
あなたの島は？（必須）a<br>
<select name=\"ISLANDID\" $str2>
$HislandList
</select><br>あなた";

    out(<<END);
<p align='center'>$HtempBack</p>
<div id='changeInfo'>
<h1>同盟の結成・変更・解散${str1}</h1>
<table border='0' width='50%'><tr><td class='M'><p>
<form name='AcForm' action='$HthisFile' method='POST'>
$str3のパスワードは？（必須）<br>
<input type='text' name='PASSWORD' size='32' value='$HdefaultPassword' maxlength='32' class='f'>
END

    if ($HallyNumber) {

        my $str4 = $adminMode ? '・結成・変更' : $HallyJoinComUse ? '' : '・加盟・脱退';
        my $str5 = ($adminMode || $HallyJoinComUse) ? '' : '<INPUT TYPE="submit" VALUE="加盟・脱退" NAME="JoinAllyButton">';
        out(<<END);
<br>
<br><b><font size='4'>［解散${str4}］</font></b>
<br>どの同盟ですか？<br>
<select name='ALLYNUMBER' onChange=allyPack() onClick=allyPack()>
$allyList
</select>
<br>
<input type='submit' value='解散' name='DeleteAllyButton'>
$str5
<br>
END
    }

    my $str7 = $adminMode ? "盟主島の変更(上のメニューで同盟を選択)<br> or 同盟の新規作成(上のメニューは無効)<br><SELECT NAME=\"ALLYID\"><OPTION VALUE=\"$max\">新規作成\n$HislandList</SELECT><br>" : '<br><B><FONT SIZE=4>［結成・変更］</FONT></B><br>';
    out(<<END);
<br>
$str7
同盟の名前（変更）<small>(全角${HlengthAllyName}字まで)</small><br>
<input type='text' name='ALLYNAME' value='$allyname' size='32' maxlength='32'><br>
マーク（変更）<br>
<select name='MARK' onChange=colorPack() onClick=colorPack()>
$markList
</select>
<ilayer name='PARENT_CTBL' width='100%' height='100%'>
   <layer name='CTBL' width='200'></layer>
   <span id='CTBL'></span>
</ilayer>
<br>
マークの色コード（変更）<br><table border="0"><tr>
<td align='center'>RED</td>
<td align='center'>GREEN</td>
<td align='center'>BLUE</td>
</tr><tr>
<td><select name="COLOR1" onChange="colorPack()" onClick="colorPack()">
$colorList[1]</select><select name="COLOR2" onChange="colorPack()" onClick="colorPack()">
$colorList[2]</select></td>
<td><select name="COLOR3" onChange="colorPack()" onClick="colorPack()">
$colorList[3]</select><select name="COLOR4" onChange="colorPack()" onClick="colorPack()">
$colorList[4]</select></td>
<td><select name="COLOR5" onChange="colorPack()" onClick="colorPack()">
$colorList[5]</select><select name="COLOR6" onChange=colorPack() onClick=colorPack()>
$colorList[6]</select></td>
</tr></table>
<input type="submit" value="結成(変更)" name="NewAllyButton">
<script language="JavaScript">
<!--
END
    if (!$adminMode) {
        out(<<END);
function colorPack() {
    var island = new Array(128);
$jsIslandList
    a = document.AcForm.COLOR1.value;
    b = document.AcForm.COLOR2.value;
    c = document.AcForm.COLOR3.value;
    d = document.AcForm.COLOR4.value;
    e = document.AcForm.COLOR5.value;
    f = document.AcForm.COLOR6.value;
    mark = document.AcForm.MARK.value;
    number = document.AcForm.ISLANDID.value;

    str = "#" + a + b + c + d + e + f;
//  document.AcForm.AcColorValue.value = str;
    str = '表示サンプル：『<B><span class="number"><FONT color="' + str +'">' + mark + '</FONT></B>'
        + island[number] + '${AfterName}</span>』';
    
    if(document.getElementById){
        document.getElementById("CTBL").innerHTML = str;
    } else if(document.all){
        el = document.all("CTBL");
        el.innerHTML = str;
    } else if(document.layers) {
        lay = document.layers["PARENT_CTBL"].document.layers["CTBL"];
        lay.document.open();
        lay.document.write(str);
        lay.document.close(); 
    }

    return true;
}
function allyPack() {
$jsAllyList
$jsAllyMarkList
$jsAllyColorList
  document.AcForm.ALLYNAME.value = ally[document.AcForm.ALLYNUMBER.value];
  document.AcForm.MARK.value     = allyMark[document.AcForm.ALLYNUMBER.value];
  document.AcForm.COLOR1.value   = allyColor[document.AcForm.ALLYNUMBER.value][0];
  document.AcForm.COLOR2.value   = allyColor[document.AcForm.ALLYNUMBER.value][1];
  document.AcForm.COLOR3.value   = allyColor[document.AcForm.ALLYNUMBER.value][2];
  document.AcForm.COLOR4.value   = allyColor[document.AcForm.ALLYNUMBER.value][3];
  document.AcForm.COLOR5.value   = allyColor[document.AcForm.ALLYNUMBER.value][4];
  document.AcForm.COLOR6.value   = allyColor[document.AcForm.ALLYNUMBER.value][5];
  colorPack();
  return true;
}
END
    } else {
        out(<<END);
function colorPack() {
    var island = new Array(128);
$jsIslandList
    a = document.AcForm.COLOR1.value;
    b = document.AcForm.COLOR2.value;
    c = document.AcForm.COLOR3.value;
    d = document.AcForm.COLOR4.value;
    e = document.AcForm.COLOR5.value;
    f = document.AcForm.COLOR6.value;
    mark = document.AcForm.MARK.value;

    str = "#" + a + b + c + d + e + f;
// document.AcForm.AcColorValue.value = str;
    str = '表示サンプル：『<b><span class="number"><font color="' + str +'">' + mark + '</font></b>'
        + 'さんぷる${AfterName}</span>』';

    if(document.getElementById){
        document.getElementById("CTBL").innerHTML = str;
    } else if(document.all){
        el = document.all("CTBL");
        el.innerHTML = str;
    } else if(document.layers) {
        lay = document.layers["PARENT_CTBL"].document.layers["CTBL"];
        lay.document.open();
        lay.document.write(str);
        lay.document.close(); 
    }

    return true;
}
function allyPack() {
$jsAllyList
$jsAllyIdList
$jsAllyMarkList
$jsAllyColorList
  document.AcForm.ALLYID.value   = allyID[document.AcForm.ALLYNUMBER.value];
  document.AcForm.ALLYNAME.value = ally[document.AcForm.ALLYNUMBER.value];
  document.AcForm.MARK.value     = allyMark[document.AcForm.ALLYNUMBER.value];
  document.AcForm.COLOR1.value   = allyColor[document.AcForm.ALLYNUMBER.value][0];
  document.AcForm.COLOR2.value   = allyColor[document.AcForm.ALLYNUMBER.value][1];
  document.AcForm.COLOR3.value   = allyColor[document.AcForm.ALLYNUMBER.value][2];
  document.AcForm.COLOR4.value   = allyColor[document.AcForm.ALLYNUMBER.value][3];
  document.AcForm.COLOR5.value   = allyColor[document.AcForm.ALLYNUMBER.value][4];
  document.AcForm.COLOR6.value   = allyColor[document.AcForm.ALLYNUMBER.value][5];
  colorPack();
  return true;
}
END
    }
    out(<<END);
colorPack();
//-->
</script>
</form>
</td></tr></table></div>
END
}


#----------------------------------------------------------------------
# 盟主コメントモード
sub allyPactMain {
    if (!$HallyPactMode) {

        unlock();                                           # 開放
        tempAllyPactPage();                                 # テンプレート出力
    }
    else {
                                                            # パスワードチェック
        my $ally = $Hally[$HidToAllyNumber{$HcurrentID}];
        if (checkPassword($ally, $HdefaultPassword)) {

            $HallyComment =~ s/[\x00-\x1f\,]//g;
            $ally->{'comment'} = htmlEscape($HallyComment);
            $ally->{'title'} = htmlEscape($HallyTitle);
            $ally->{'message'} = htmlEscape($HallyMessage, 1);
            # データ書き出し
            writeAllyFile();
            unlock();
            # 変更成功
            tempAllyPactOK($ally->{'name'});
        }
        else {
            # password間違い
            unlock();
            tempWrongPassword();
            return;
        }
    }
}


#----------------------------------------------------------------------
# 盟主コメントモードのトップページ
sub tempAllyPactPage {

    my $ally = $Hally[$HidToAllyNumber{$HcurrentID}];
    my $allyMessage = $ally->{'message'};
    $allyMessage =~ s/<br>/\n/g;
    $allyMessage =~ s/&amp;/&/g;
    $allyMessage =~ s/&lt;/</g;
    $allyMessage =~ s/&gt;/>/g;
    $allyMessage =~ s/&quot;/\"/g; #"

    out(<<END);
<div align='center'>$HtempBack</div><br>
  <div id='changeInfo'>
    <h1>コメント変更（$ally->{'name'}）</H1>
    <table border='0' width='50%'>
      <tr>
        <td class='M'>
          <form action='$HthisFile' method='POST'>
            <b>盟主パスワードは？</b><br>
            <input type='password' name='Allypact' value='$HdefaultPassword' size='32' maxlength='32' class='f'>
            <input type='hidden'  name='ISLANDID' value='$ally->{'id'}'>
            <input type='submit' value='送信' name='AllypactButton'><br>
            <b>コメント</b><small>(全角${HlengthAllyComment}字まで：トップページの「各同盟の状況」欄に表示されます)</small><br>
            <input type='text' name='ALLYCOMMENT'  value='$ally->{'comment'}' size='100' maxlength='50'><br>
            <br>
            <b>メッセージ・盟約など</b>(「同盟の情報」欄の上に表示されます)<br>
タイトル<small>(全角${HlengthAllyTitle}字まで)</small><br>
            <input type='text' name='ALLYTITLE'  value='$ally->{'title'}' size='100' maxlength='50'><br>
メッセージ<small>(全角${HlengthAllyMessage}字まで)</small><br>
            <textarea cols='50' rows='16' name='ALLYMESSAGE' wrap='soft'>$allyMessage</textarea>
<br>
「タイトル」を空欄にすると『盟主からのメッセージ』というタイトルになります。<br>
「メッセージ」を空欄にすると「同盟の情報」欄には何も表示されなくなります。
          </form>
        </td>
      </tr>
    </table>
  </div>
END
}


#----------------------------------------------------------------------
# 盟主コメント変更完了
sub tempAllyPactOK {
    my ($name) = @_;
    out(<<END);
${HtagBig_}$name${AfterName}のコメントを変更しました。${H_tagBig}$HtempBack
END
}


#----------------------------------------------------------------------
# 同盟(陣営)設定
#----------------------------------------------------------------------
sub amitySetupMain() {

    if (!$HasetupMode) {

        unlock();                       # 開放
        tempAmitySetupPage();           # テンプレート出力
    }
    else {
        # パスワードチェック
        if (checkSpecialPassword($HdefaultPassword)) {
            # 特殊パスワード
            my ($id, $aId);
            foreach (0..$islandNumber) {
                undef $Hislands[$_]->{'allyId'};
            }

            foreach (0..($HallyNumber - 1)) {
                undef $Hally[$_]->{'memberId'};
                undef $Hally[$_]->{'number'};
                undef $Hally[$_]->{'score'};
                my ($aId) = $Hally[$_]->{'id'};
                if (defined $HidToNumber{$aId}) {
                    push(@{$Hally[$_]->{'memberId'}}, $Hally[$_]->{'id'});
                    $Hally[$_]->{'score'} += $Hislands[$HidToNumber{$aId}]->{'pts'};
                    push(@{$Hislands[$HidToNumber{$aId}]->{'allyId'}}, $aId);
                }
            }

            foreach (@HallyChange) {

                ($id, $aId) = split(/-/, $_);
                $Hally[$HidToAllyNumber{$aId}]->{'score'} += $Hislands[$HidToNumber{$id}]->{'pts'};
                next if ($id == $aId);
                push(@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}, $id);
                push(@{$Hislands[$HidToNumber{$id}]->{'allyId'}}, $aId);
            }

            foreach (0..($HallyNumber - 1)) {

                $Hally[$_]->{'number'} = @{$Hally[$_]->{'memberId'}};
            }
            allyOccupy();
            allySort();
            writeIslandsFile();
            unlock();

            tempAmitySetupPage();                       # 変更成功
        }
        else {
                                                        # password間違い
            unlock();
            tempWrongPassword();
            return;
        }
    }
}


#----------------------------------------------------------------------
# 同盟(陣営)設定ページ
sub tempAmitySetupPage() {
    # 開放
    unlock();

    out(<<END);
<div align='center'>$HtempBack</div><br>
<div id='campinfo'>
  <h1>同盟(陣営)所属設定</H1>
  <form action="$HthisFile" method="POST">
    <input type="hidden" value="$HdefaultPassword" name="ASetup">
    <table border>
      <tr>
          <th $HbgTitleCell align="center" rowspan="2">${HtagTH_}設定${H_tagTH}<br><input type="submit" value="変更" name="AmityChangeButton"></td>
END

    foreach (0..$islandNumber) {
        $Hislands[$_]->{'ally'} = $Hislands[$_]->{'allyId'}[0];
    }

    my @idx = (0..$#Hislands);
    @idx = sort {
                $Hislands[$b]->{'field'} <=> $Hislands[$a]->{'field'} || # バトルフィールド優先
                $Hislands[$b]->{'ally'} <=> $Hislands[$a]->{'ally'} || # 同盟でソート
                $a <=> $b # $kindが同じなら以前のまま
           } @idx;

    my $aStr = ($HarmisticeTurn) ? '陣営' : '同盟';
    out("<th $HbgTitleCell align='center' colspan='$HallyNumber'>${HtagTH_}${aStr}${H_tagTH}</th>") if ($HallyNumber);
    out("</tr><tr>\n");
    my ($number, $island, $name, $ally);

    foreach (0..($HallyNumber - 1)) {
        $ally = $Hally[$_];
        $name = "<font color=\"$ally->{'color'}\"><b>$ally->{'mark'}</b></font>$ally->{'name'}";
        out(<<END);
        <td class='T'>$name</td>
END
    }
    out("      </tr>\n");

    foreach (0..$islandNumber) {
        $island = $Hislands[$idx[$_]];
        $name = islandName($island);
        my ($id, $amity, $aId);
        $id = $island->{'id'};
        out("      <tr><th $HbgTitleCell>$name</th>");

        for ($i = 0; $i < $HallyNumber; $i++) {
            $ally  = $Hally[$i];
            $aId = $ally->{'id'};
            my $member = $Hally[$i]->{'memberId'};
            my $flag = 1;
            foreach (@$member) {
                if ($id == $_) {
                    $flag = 0;
                    last;
                }
            }

            if ($flag) {
                out("        <th><input type='checkbox' name='ally' value='$id-$aId'></th>");
            } else {
                out("        <th><input type='checkbox' name='ally' value='$id-$aId' checked></th>");
            }
        }
        out("      </tr>\n");
    }
    out(<<END);
    </table>
    <input type="hidden" value="dummy" name="AmityChange">
  </form>
</div>
END
}


#----------------------------------------------------------------------
# ログテンプレート
#----------------------------------------------------------------------
# 新規で名前がない場合
sub tempNewIslandNoName {
    out(<<END);
${HtagBig_}${AfterName}につける名前が必要です。${H_tagBig}$HtempBack
END
}


# 新規でオーナー名がない場合
sub tempNewIslandNoOwnerName {
    out(<<END);
${HtagBig_}あなたの名前が必要です。${H_tagBig}$HtempBack
END
}


# 新規でオーナー名が不正な場合
sub tempNewIslandBadOwnerName {
    out(<<END);
${HtagBig_}',?()<>\$'が入っている名前はやめましょう。${H_tagBig}$HtempBack
END
}

1;
