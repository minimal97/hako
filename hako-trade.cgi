#----------------------------------------------------------------------
# minimal の 箱庭諸島
# 取引用
# ターン処理、マップ処理
#----------------------------------------------------------------------

# 取引ができるかどうか
# 取引なし 0 取引あり 1
our ($HTrade_Exist) = 1;


# 削除されるターン
our ($HTrade_DeleteTurn) = 12;

# 取引ファイル名
# open(IN, "<" , "${HdirName}/${HtradeFile}");
our ($HtradeFile) = "tradelist.dat";

    SetTradeObjList(  0,  1, "米",      "00トン",   "kome");
    SetTradeObjList(  1,  2, "野菜",    "00トン",   "yasai");
    SetTradeObjList(  2,  3, "くだもの","00トン",   "seafood");
    SetTradeObjList(  3,  4, "魚介類",  "00トン",   "toriniku");
    SetTradeObjList(  4,  5, "塩",      "00トン",   "sio");
    SetTradeObjList(  5,  6, "鶏肉",    "00トン",   "toriniku");
    SetTradeObjList(  6,  7, "豚肉",    "00トン",   "butaniku");
    SetTradeObjList(  7,  8, "牛肉",    "00トン",   "gyuniku");
    SetTradeObjList(  8,  9, "たまご",  "00トン",   "tamago");
    SetTradeObjList(  9, 30, "木材",    "00トン",   "wood");
    SetTradeObjList( 10, 50, "家具",    "00トン",   "furniture");
    SetTradeObjList( 11, 70, "ゴミ",    "トン",     "gomi");
    SetTradeObjList( 12,  0, "","","0");         # 最終


#----------------------------------------------------------------------
sub SetTradeObjList {
    my ($no, $val, $name, $unit, $ele) = @_;

    $objectlistVal[$no] = $val;
    $objectlistName[$no] = $name;
    $objectlistUnit[$no] = $unit;
    $objectlistElement[$no] = $ele;
}


#----------------------------------------------------------------------
sub TradeDataRead {
    my ($island, $id) = @_;

    my ($data);
    my ($i);
    open(IN, "<" , "${HdirName}/${HtradeFile}");
    my @lines = <IN>;
    close(IN);                 # ファイルを閉じる

    my ($ret) = '';
    for ($i = 1 ; $i < (@lines) ; $i++) {

        $data = TradeDataConv($lines[$i]);

        if ($id == $data->{'id'}) {
            $ret = $data;
            last;
        }
    }

    return ($ret);
}


#----------------------------------------------------------------------
sub TradeEditMain {

    # idから島番号を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];

    # パスワード
    if (!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    my ($trade_data);
    $trade_data = TradeDataRead($island , $TradeTargetID);

    # なぜかその島がない場合
    if (   ($HcurrentNumber eq '')
        || ($TradeTargetID <= 0)
        || ($trade_data eq '')
                                    ) {
        tempTradeErr();
        return;
    }

    my ($tar_chkid);
    if ($TradeTargetChgSide == 1) {

        $tar_chkid = $trade_data->{'island1_id'};
    }
    else {

        $tar_chkid = $trade_data->{'island2_id'};
    }

    # なぜかその島がない場合
    if ($HcurrentID != $tar_chkid) {
        tempTradeErr();
        return;
    }

    # ChgSideなら ture false 反転
    print $trade_data->{"check$TradeTargetChgSide"};
    if ($TradeTargetChgSide > 0) {

        $trade_data->{"check$TradeTargetChgSide"} = ($trade_data->{"check$TradeTargetChgSide"}) ? 0 : 1;
    }
    print $trade_data->{"check$TradeTargetChgSide"};

    TradeDataUpdate($trade_data);
}


#----------------------------------------------------------------------
sub TradeFileRead {
    my ($tar_id , $trade_data) = @_;

    my ($num) = 0;
    my ($data);

    unless (-e "${HdirName}/${HtradeFile}") {

        open(OUT, ">${HdirName}/${HtradeFile}");
        print OUT "0\n";

        close(OUT);                 # ファイルを閉じる
    }

    open(IN, "<${HdirName}/${HtradeFile}");
    $data = <IN>;       # 最初はIDヘッダなので捨てる
    while (<IN>) {
        $trade_data[$num] = TradeDataConv($_);
        $num++;
    }
    close(IN);                     # ファイルを閉じる

    return ($num);
}



#----------------------------------------------------------------------------------------
sub MakeNumberSelect {
    my ($name , $keta) = @_;

    my ($i , $k);
    $keta = min($keta , 9);
    for ($k = 0; $k < $keta; $k++) {
        out("<select name='$name$k'>");
        for ($i = 0 ; $i <= 9 ; $i++) {
            out("<option value='$i'>$i</option>");
        }
        out("</select>");
    }
}


#----------------------------------------------------------------------------------------
#
# get
#
sub GetTradeNextID {

    my ($num) = 0;
    if (-e "${HdirName}/${HtradeFile}") {

        open(IN, "<${HdirName}/${HtradeFile}");
        $num = <IN>;
        close(IN);                  # ファイルを閉じる
    }
    else {

        open(OUT, ">${HdirName}/${HtradeFile}");
        print OUT "0\n";
        close(OUT);                 # ファイルを閉じる
    }

    return ($num + 1);
}

#----------------------------------------------------------------------------------------
# メイン
# 作成メインはUnlock不要 次のTradeListMainでやる。
sub TradeMakeMain {

    # idから島番号を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    $island = $Hislands[$HcurrentNumber];

    # パスワード
    if (!checkPassword($island,$HinputPassword)) {
        # password間違い
        tempWrongPassword();
        return;
    }

    # なぜかその島がない場合
    if ($HcurrentNumber eq '') {
        tempTradeErr();
        return;
    }

    my ($TargetNumber) = $HidToNumber{$TradeTargetID};
    # なぜかその島がない場合
    if ($TargetNumber eq '') {
        tempTradeErr();
        return;
    }

    # 自分の島だった
    if ($TradeTargetID == $HcurrentID) {
        tempTradeSelfError('自島');
        return;
    }

    if (($TradeObjectNum+0) <= 0) {
        tempTradeNumZero();
        return;
    }

    my ($target_island) = $Hislands[$TargetNumber];

    # 預かりの島はdelete
    if ($target_island->{'predelete'}) {
        tempTradePreDeleteTarget();
        return;
    }
    if ($target_island->{'BF_Flag'}) {
        tempTradeSelfError('バトルフィールド');
        return;
    }

    my ($trade_next_id);
    $trade_next_id = GetTradeNextID();

    # print "Debug : $trade_next_id / $TradeTargetID / $TradeObject / $TradeObjectNum / $TradeMoney / $TradePaySide";

    # ------------ #
    # ファイル更新 #
    # ------------ #
    open(IN, "${HdirName}/${HtradeFile}");
    my @lines = <IN>;
    close(IN);

    my ($i);
    open(OUT, ">" , "${HdirName}/${HtradeFile}");
    $lines[0] = "$trade_next_id\n";

    for ($i = 0 ; $i < (@lines) ; $i++) {

        print OUT $lines[$i];
    }

    print OUT "$trade_next_id,$HcurrentID,$TradeTargetID,$TradeObject,$TradeObjectNum,$TradeObjSide,$TradeMoney,$TradePaySide,0,0,0\n";
    close(OUT);                 # ファイルを閉じる

}




my ($HtradeFile) = "trade.trd";
#----------------------------------------------------------------------------------------
# 別ファイルに分ける
#----------------------------------------------------------------------------------------
# メイン
sub TradeDeleteMain {

    # idから島番号を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    $island = $Hislands[$HcurrentNumber];

    # パスワード
    if (!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    # なぜかその島がない場合
    if ($HcurrentNumber eq '') {
        tempTradeErr();
        return;
    }

    # ------------ #
    # ファイル更新 #
    # ------------ #
    open(IN, "${HdirName}/${HtradeFile}");
    my @lines = <IN>;
    close(IN);

    my ($i);
    open(OUT, ">" , "${HdirName}/${HtradeFile}");

    my ($trade_data);

    for ($i = 0 ; $i < (@lines) ; $i++) {

        $trade_data = TradeDataConv($lines[$i]);

        if (   ($trade_data->{'id'} == $TradeTargetID)
            && ($trade_data->{'island1_id'} == $HcurrentID) ) {
            # 同じID、かつ取引元は削除
        }
        else {

            print OUT $lines[$i];
        }
    }
    close(OUT);                 # ファイルを閉じる
}


#----------------------------------------------------------------------------------------
# 別ファイルに分ける
#----------------------------------------------------------------------------------------
# メイン
sub TradeListMain {

    my (@trade_data);
    my ($num);

    # idから島番号を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};

    # なぜかその島がない場合
    if($HcurrentNumber eq '') {
        unlock();
        tempTradeErr();
        return;
    }

    my ($island) = $Hislands[$HcurrentNumber];

    # パスワード
    if (!checkPassword($island,$HinputPassword)) {
        # password間違い
        unlock();
        tempWrongPassword();
        return;
    }

    $num = TradeFileRead($HcurrentID,\@trade_data);

    # 名前の取得
    $HcurrentName = islandName($island);

    # 取引画面
    TradeListHead(); # ようこそ!!
    MapCommonScript();
    islandInfo(0); # 島の情報

    # 開放
    unlock();

    TradeListCreate($island, \@trade_data , $num); # 島の地図、観光モード
    PrintNewTrade($island);
    # 近況
    # tempRecent(0, $HuseHistory2);
}


#----------------------------------------------------------------------
sub TradeDataUpdate {
    my ($NewData) = @_;

    my ($id) = $NewData->{'id'};
    # データが壊れている
    if ($id == 0) {
        tempTradeErr();
        return;
    }

    # ------------ #
    # ファイル更新 #
    # ------------ #
    open(IN, "${HdirName}/${HtradeFile}");
    my @lines = <IN>;
    close(IN);

    my ($i);
    open(OUT, ">" , "${HdirName}/${HtradeFile}");

    my ($trade_data);

    for ($i = 0 ; $i < (@lines) ; $i++) {

        $trade_data = TradeDataConv($lines[$i]);
        if ($lines[$i]  =~ /([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+)*/ ) {
            if (   ($NewData->{'id'} == $trade_data->{'id'}) ) {

                $lines[$i] = TradeDataToStr($NewData);
            }
        }

        print OUT $lines[$i];
    }
    close(OUT);                 # ファイルを閉じる
}


#----------------------------------------------------------------------
sub PrintNewTrade {
    my ($island) = @_;

    if ($island->{'trade_active'} >= $island->{'trade_max'}) {
        out(<<END);
<hr>
<div>${HtagBig_}取引数が限界なので、新規の取引を作成できません。<br>許可を外すか、削除が必要です。${H_tagBig}</div>
END
        return ;
    }
        out(<<END);
<hr>
<div>
  <div>${HtagBig_}新規${H_tagBig}</div>
  <form name="TradeCreateForm" action="${HthisFile}" method="post">
    <input type="hidden" name="PASSWORD" value="$HdefaultPassword">
    <table>
      <tr>
        <th $HbgTitleCell rowspan='5'>${HtagTH_}内容${H_tagTH}</th>
        <th $HbgTitleCell colspan='5'>${HtagTH_}取引先${H_tagTH}</th>
        <th $HbgTitleCell rowspan='2'>${HtagTH_}操作${H_tagTH}</th>
      </tr>
      <tr>
        <th $HbgTitleCell rowspan='2'>${HtagTH_}物資${H_tagTH}</th>
        <th $HbgTitleCell>${HtagTH_}取引先${H_tagTH}</th>
        <th $HbgTitleCell>${HtagTH_}取引種類${H_tagTH}</th>
        <th $HbgTitleCell>${HtagTH_}数量${H_tagTH}</th>
        <th $HbgTitleCell>${HtagTH_}出す側${H_tagTH}</th>
      </tr>
      <tr>
        <td $HbgInfoCell>
          <select name="TargetId">$HtargetList</select>
        </td>
        <td $HbgInfoCell>
          <select name="TradeObject" onChange="objectchange();">
END
        TradeObjectList();
        out(<<END);
          </select>
        </td>
        <td $HbgInfoCell>
END
        MakeNumberSelect("TradeObjectNum" , 4);
        out(<<END);
<span class="obj_unit">単位</span>
        </td>
        <td $HbgInfoCell>
END
        PrintTradePaySide('TradeObjSide' , 0);
        out(<<END);
        </td>
        <td $HbgInfoCell rowspan='3'><input type="submit" value="申し込む(仮)" name="TradeMake=$HcurrentID"></td>
      </tr>
      <tr>
        <th $HbgTitleCell rowspan='2'>${HtagTH_}お金${H_tagTH}</th>
        <th $HbgTitleCell colspan='3'>${HtagTH_}金額${H_tagTH}</th>
        <th $HbgTitleCell>${HtagTH_}支払う側${H_tagTH}</th>
      </tr>
      <tr>
        <th $HbgInfoCell colspan='3'>${HtagTH_}
END
        MakeNumberSelect("TradeMoney" , 7);
        out("$HunitMoney");
        out(<<END);
        ${H_tagTH}</th>
        <th $HbgInfoCell >${HtagTH_}
END
        PrintTradePaySide('TradePaySide' , 0);
        out(<<END);
        ${H_tagTH}</th>
      </tr>
    </table>
  </form>
  <script type="text/javascript">
    /* 単位 */
END
        out("var OBJ_UNIT = new Array($#objectlistUnit+1);\n");
        {
            my ($i);
            for ($i = 0 ; $objectlistVal[$i] != 0 ; $i++) {

                out("OBJ_UNIT[$i] = '$objectlistUnit[$i]';\n");
            }

        }
        out(<<END);
  function objectchange () {
    var objno;
    var StyElm;
    objno = document.TradeCreateForm.TradeObject.selectedIndex;
    StyElm = document.getElementsByClassName("obj_unit");
    StyElm[0].innerText = OBJ_UNIT[objno];
  }

  objectchange();
  </script>
  </div>
END

}

#----------------------------------------------------------------------
sub TradeListCreate {
    my ($island , $trade_data, $num) = @_;

    my ($HtargetList);

    my ($lp);
    my ($trade_id);
    my ($trade_obj,$trade_num, $trade_objside);
    my ($island1_id,$island2_id);
    my ($island1_name,$island2_name);
    my ($trade_money);
    my ($trade_payside);
    my ($tra_ok1 , $tra_ok2);
    my ($tra_btn1 , $tra_btn2);
    my ($trade_absent);

    my ($trade_active) = 0;

    $HtargetList = getIslandList($island->{'id'}, 1);
    out(<<END);
<hr>
<div>
END
    my ($delete_btn);

    out('<table>');
    my ($enable_cnt) = 0;

    for ($lp = 0 ; $lp < $num ; $lp++) {

        $trade_id = $trade_data[$lp]->{'id'};

        if ($trade_data[$lp]->{'check1'}) {

            $tra_ok1 = "許可";
            $tra_btn1 = "<input type='submit' value='拒否する' name='TRADE_CHG1=$trade_id'>";
        }
        else {

            $tra_ok1 = "拒否";
            $tra_btn1 = '';
            if ($trade_active < $island->{'trade_max'}) {
                $tra_btn1 = "<input type='submit' value='許可する' name='TRADE_CHG1=$trade_id'>";
            }
        }

        if ($trade_data[$lp]->{'check2'}) {

            $tra_ok2 = "許可";
            $tra_btn2 = "<input type='submit' value='拒否する' name='TRADE_CHG2=$trade_id'>";
        }
        else {

            $tra_ok2 = "拒否";
            $tra_btn2 = '';
            if ($trade_active < $island->{'trade_max'}) {
                $tra_btn2 = "<input type='submit' value='許可する' name='TRADE_CHG2=$trade_id'>";
            }
        }


        $island1_id = $trade_data[$lp]->{'island1_id'};
        $island2_id = $trade_data[$lp]->{'island2_id'};
        $island1_name = islandName($Hislands[$HidToNumber{$island1_id}]);

        $island2_name = islandName($Hislands[$HidToNumber{$island2_id}]);

        if (   ($island1_id != $HcurrentID)
            && ($island2_id != $HcurrentID) ) {

        #    next;
        }

        if (   (   ($island1_id == $HcurrentID)
                && ($trade_data[$lp]->{'check1'}) )
            || (   ($island2_id == $HcurrentID)
                && ($trade_data[$lp]->{'check2'}) ) ) {

            $trade_active++;
        }

        $trade_absent = $trade_data[$lp]->{'absent'} + 0;
        $trade_money = $trade_data[$lp]->{'money'} + 0;
        $trade_payside = $trade_data[$lp]->{'payside'};

        $trade_obj = $trade_data[$lp]->{'obj'};
        $trade_num = $trade_data[$lp]->{'obj_num'} + 0;
        $trade_objside = $trade_data[$lp]->{'objside'} + 0;

        $tra_btn1 = ($island1_id == $HcurrentID) ? $tra_btn1 : '';
        $tra_btn2 = ($island2_id == $HcurrentID) ? $tra_btn2 : '';

        $delete_btn = '';
        if ($island1_id == $HcurrentID) {
            $delete_btn = "<input type='submit' value='削除' name='TRADE_DEL=$trade_id'>";
        }

        out(<<END);
    <tr>
      <form name="$lp" action="$HthisFile" method="POST">
      <input type="hidden" name="PASSWORD" value="$HdefaultPassword">
      <input type="hidden" name="myID" value="$HcurrentID">
      <tr>
        <th $HbgTitleCell rowspan='2'            >${HtagTH_}ID${H_tagTH}</th>
        <th $HbgTitleCell rowspan='3' colspan='2'>${HtagTH_}取引${H_tagTH}</th>
        <th $HbgTitleCell             colspan='2'>${HtagTH_}取引元${H_tagTH}</th>
        <th $HbgTitleCell             colspan='2'>${HtagTH_}取引先${H_tagTH}</th>
        <th $HbgTitleCell rowspan='2' colspan='1'>${HtagTH_}放置<br>ターン${H_tagTH}</th>
        <th $HbgTitleCell rowspan='2'            >${HtagTH_}操作${H_tagTH}</th>
      </tr>
      <tr>
        <th $HbgTitleCell colspan='1'>${HtagTH_}名前${H_tagTH}</th>
        <th $HbgTitleCell colspan='1'>${HtagTH_}許可${H_tagTH}</th>
        <th $HbgTitleCell colspan='1'>${HtagTH_}名前${H_tagTH}</th>
        <th $HbgTitleCell colspan='1'>${HtagTH_}許可${H_tagTH}</th>
      </tr>
      <tr>
        <td $HbgInfoCell  rowspan='4'            >$trade_id</td>
        <td $HbgInfoCell  rowspan='1' colspan='1'>$island1_name</td>
        <td $HbgInfoCell  rowspan='1' colspan='1'>${HtagTH_}$tra_ok1<br>$tra_btn1${H_tagTH}</td>
        <td $HbgInfoCell  rowspan='1' colspan='1'>$island2_name</td>
        <td $HbgInfoCell  rowspan='1' colspan='1'>${HtagTH_}$tra_ok2<br>$tra_btn2${H_tagTH}</td>
        <td $HbgInfoCell  rowspan='4'            >$trade_absent</td>
        <td $HbgInfoCell  rowspan='4'            >${HtagTH_}$delete_btn${H_tagTH}</td>
      </tr>

END
        if ($trade_objside) {

        out(<<END);
      <tr>
        <th $HbgTitleCell rowspan='2'            >${HtagTH_}物資${H_tagTH}</th>
        <th $HbgTitleCell             colspan='1'>${HtagTH_}物資${H_tagTH}</th>
        <td $HbgInfoCell              colspan='2'>$objectlistName[$trade_obj]</td>
        <td $HbgInfoCell  rowspan='2' colspan='2'>-</td>
      </tr>
      <tr>
        <th $HbgTitleCell             colspan='1'>${HtagTH_}数量${H_tagTH}</th>
        <td $HbgInfoCell              colspan='2'>$trade_num$objectlistUnit[$trade_obj]</td>
      </tr>
END
        }
        else {

        out(<<END);
      <tr>
        <th $HbgTitleCell rowspan='2'            >${HtagTH_}物資${H_tagTH}</th>
        <th $HbgTitleCell             colspan='1'>${HtagTH_}物資${H_tagTH}</th>
        <td $HbgInfoCell  rowspan='2' colspan='2'>-</td>
        <td $HbgInfoCell              colspan='2'>$objectlistName[$trade_obj]</td>
      </tr>
      <tr>
        <th $HbgTitleCell             colspan='1'>${HtagTH_}数量${H_tagTH}</th>
        <td $HbgInfoCell              colspan='2'>$trade_num$objectlistUnit[$trade_obj]</td>
      </tr>
END
        }
        out(<<END);
      <tr>
        <td $HbgTitleCell             colspan='2'>${HtagTH_}金${H_tagTH}</td>
END

        if ($trade_payside) {
        out(<<END);
        <td $HbgInfoCell              colspan='2'>${HtagTH_}$trade_money$HunitMoney${H_tagTH}</td>
        <td $HbgInfoCell              colspan='2'>-</td>
END
        }
        else {
    out(<<END);
        <td $HbgInfoCell              colspan='2'>-</td>
        <td $HbgInfoCell              colspan='2'>${HtagTH_}$trade_money$HunitMoney${H_tagTH}</td>
END
        }

        out(<<END);
      </tr>
      </form>
    </tr>
END
    }
        out('</table>');

        out(<<END);
</div>
END

    $island->{'trade_active'} = $trade_active;
}

#----------------------------------------------------------------------
# 取引データを STRに
#----------------------------------------------------------------------
sub TradeDataToStr {
    my ($data) = @_;

    my ($TradeTargetID) = $data->{'id'};
    my ($island1_id) = $data->{'island1_id'};
    my ($island2_id) = $data->{'island2_id'};
    my ($obj) = $data->{'obj'};
    my ($obj_num) = $data->{'obj_num'};
    my ($objside) = $data->{'objside'};
    my ($money) = $data->{'money'};
    my ($payside) = $data->{'payside'};
    my ($check1) = $data->{'check1'};
    my ($check2) = $data->{'check2'};
    my ($absent) = $data->{'absent'};

    return ("$TradeTargetID,$island1_id,$island2_id,$obj,$obj_num,$objside,$money,$payside,$check1,$check2,$absent\n");

    # "$trade_next_id,$HcurrentID,$TradeTargetID,$TradeObject,$TradeObjectNum,$TradeMoney,$TradePaySide,0,0\n";
}

#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub TradeDataConv {
    my ($data) = @_;

    chomp($data);
    my ($tradeID ,$island1 , $island2, $trade_obj , $trade_obj_num , $trade_objside , $trade_money , $trade_payside , $check1 , $check2 , $absent) = split(/,/, $data);

    return {
        'id' => int($tradeID),
        'island1_id' => int($island1),
        'island2_id' => int($island2),
        'obj' => int($trade_obj),
        'obj_num' => int($trade_obj_num),
        'objside' => int($trade_objside),
        'money' => int($trade_money),
        'payside' => int($trade_payside),
        'check1' => int($check1),
        'check2' => int($check2),
        'absent' => int($absent),
    };

}

#----------------------------------------------------------------------
sub PrintTradePaySide {
    my ($tag_name,$trade_id) = @_;

    out("<select name='$tag_name'>");
    out("<option value='0'>相手島</option>");
    out("<option value='1'>自島</option>");
    out("</select>");
}


#----------------------------------------------------------------------
sub TradeObjectList {

    my ($i);
    for ($i = 0 ; $objectlistVal[$i] != 0 ; $i++) {

        out("<option value='$objectlistVal[$i]'>$objectlistName[$i]</option>"); 
    }
}


#----------------------------------------------------------------------
sub TradeListHead {
    out(<<END);
<DIV align='center'>${HtagBig_}<span class='Nret'>${HtagName_}「${HcurrentName}」${H_tagName}の</span><span class='Nret'>取引画面</span>${H_tagBig}<BR>
$HtempBack<BR>
</DIV>
END
}


#----------------------------------------------------------------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# 何か問題発生
#
sub tempTradeErr {

    out(<<END);
${HtagBig_}問題が発生しました。${H_tagBig}
END
}


#----------------------------------------------------------------------
# 何か問題発生
#
sub tempTradeSelfError {
    my ($tar) = @_;
    out(<<END);
${HtagBig_}$tarとの取引はできません。${H_tagBig}
END
}


#----------------------------------------------------------------------
# 何か問題発生
#
sub tempTradeNumZero {
    out(<<END);
${HtagBig_}数量が0では取引ができません。${H_tagBig}
END
}


#----------------------------------------------------------------------
# 預かりの島
#
sub tempTradePreDeleteTarget {
    out(<<END);
${HtagBig_}預かりの島へは申請できません。${H_tagBig}
END
}

1;
