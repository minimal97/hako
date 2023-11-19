# うらにわ -uRAniwa-: http://snow.prohosting.com/awinokah/
#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# ローカル掲示板モジュール(ver1.00)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
#―――――――――――――――――――――――――――――――――――
#                             箱庭諸島 2nd
#                                 v1.5
#                            箱庭諸島 海戦
#                                 v1.3
#                    by 親方 webgame@oyoyo.ne.jp
#                   http://www.oyoyo.ne.jp/webgame/
#―――――――――――――――――――――――――――――――――――
#----------------------------------------------------------------------
# ローカル掲示板モード
#----------------------------------------------------------------------
# メイン
sub localBbsMain {
    # idから島番号を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my ($island) = $Hislands[$HcurrentNumber];

    # ヘッダ出力
    tempHeader() if ($HjavaMode ne 'java' && $HlbbsMode < 5);

    # なぜかその島がない場合
    if ($HcurrentNumber eq '') {
        unlock();
        tempProblem();
        return;
    }

    # 削除モードじゃなくて名前かメッセージがない場合
    if (   ($HlbbsMode < 2)
        || ($HlbbsMode == 5) ) {

        if (   ($HlbbsName eq '')
            || ($HlbbsMessage eq '')) {

            tempHeader() if ($HlbbsMode == 5);
            unlock();
            tempLbbsNoMessage();
            return;
        }
    }

    my ($speaker);
    my ($lbbs);
    $lbbs = $island->{'lbbs'};

    # 観光者モードじゃない時はパスワードチェック
    if ($HlbbsMode % 2 == 1) {
        if (!checkPassword($island,$HinputPassword)) {
            # password間違い
            tempHeader() if ($HlbbsMode == 5 || $HlbbsMode == 7);
            unlock();
            tempWrongPassword();
            return;
        }

        # オーナー名を設定
        # $HlbbsName = $island->{'owner'};
    }
    elsif ($HlbbsMode == 0) {
        # 観光者モード
        my ($sIsland);

        if ($HlbbsType ne 'ANON') {
            # 公開と極秘

            # idから島番号を取得
            my ($number) = $HidToNumber{$HspeakerID};
            $sIsland = $Hislands[$number];

            # なぜかその島がない場合
            if ($number eq '') {
                unlock();
                tempProblem();
                return;
            }

            # パスワードチェック
            if (!checkPassword($sIsland,$HinputPassword)) {
                # password間違い
                unlock();
                tempWrongPassword();
                return;
            }

            # オーナー名を設定
            # $HlbbsName = $sIsland->{'owner'};

            # 通信費用を払う
            my ($cost) = ($HlbbsType eq 'PUBLIC') ? $HlbbsMoneyPublic : $HlbbsMoneySecret;
            if ($sIsland->{'money'} < $cost) {
                # 費用不足
                unlock();
                tempLbbsNoMoney();
                return;
            }
            $sIsland->{'money'} -= $cost;
        }

        # 発言者を記憶する
        if ($HlbbsType ne 'ANON') {
            # 公開と極秘
            my ($name) = islandName($sIsland);
            $speaker = $name . ',' . $HspeakerID;
        }
        else {
            # 匿名
            $speaker = $ENV{'REMOTE_HOST'};
            $speaker = $ENV{'REMOTE_ADDR'} if ($speaker eq '');
        }
    }
    elsif ($HlbbsMode == 2) {
        # 観光者削除モード
        my ($sIsland);

        # idから島番号を取得
        my ($number) = $HidToNumber{$HspeakerID};
        $sIsland = $Hislands[$number];

        # なぜかその島がない場合
        if ($number eq '') {
            unlock();
            tempProblem();
            return;
        }

        # IDチェック
        $lbbs->[$HcommandPlanNumber] =~ /[0-9]*\<.*,([0-9]*)\<[0-9]*\>.*\>.*$/;
        my ($wId) = $1;
        if ($wId != $HspeakerID) {
            # ID間違い
            unlock();
            tempWrong("あなたの発言ではありません！");
            return;
        }

        # パスワードチェック
        if (!checkPassword($sIsland,$HinputPassword)) {
            # password間違い
            unlock();
            tempWrongPassword();
            return;
        }
    }
    elsif ($HlbbsMode == 4) {
        # 観光者極秘通信確認モード
        my ($sIsland);

        # idから島番号を取得
        my ($number) = $HidToNumber{$HspeakerID};
        $sIsland = $Hislands[$number];

        # なぜかその島がない場合
        if ($number eq '') {
            unlock();
            tempProblem();
            return;
        }

        # パスワードチェック
        if (!checkPassword($sIsland,$HinputPassword)) {
            # password間違い
            unlock();
            tempWrongPassword();
            return;
        }
    }

    # モードで分岐
    if ($HlbbsMode == 4) {
        printIslandMain();
        return;
    }
    elsif (   ($HlbbsMode == 2)
           || ($HlbbsMode == 3)
           || ($HlbbsMode == 7) ) {
        # 削除モード
        if (   ($HlbbsMode == 3 || $HlbbsMode == 7)
            && ($HcommandPlanNumber == LBBS_MAX)) {
			foreach (0..($HlbbsMax - 1)) {
				$lbbs->[$_] = '0<<0>>';
			}
		}
        else {
            # メッセージを前にずらす
            slideBackLbbsMessage($lbbs, $HcommandPlanNumber);
        }
        tempLbbsDelete() if ($HlbbsMode != 7);
    }
    else {
        # 記帳モード
        $speaker = "管理人,0" if ($HlbbsMode == 5);
        if ($HlbbsType ne 'SECRET') {
            # 公開と匿名
            $speaker = "0<$speaker";
        }
        else {
            # 極秘
            $speaker = "1<$speaker";
        }
        # メッセージを後ろにずらす
        slideLbbsMessage($lbbs);

        # メッセージ書き込み
        my ($message);
        if ($HlbbsMode == 1) {
            $message = '1';
        }
        else {
            $message = '0';
        }
        $HlbbsName = "$HislandTurn：" . htmlEscape($HlbbsName);
        $HlbbsMessage = htmlEscape($HlbbsMessage);
        $lbbs->[0] = "$speaker<$message>$HlbbsName>$HlbbsMessage";

        tempLbbsAdd() if ($HlbbsMode != 5);
    }

    # データ書き出し
    writeIslandsFile($HcurrentID);

    # もとのモードへ
    if ($HlbbsMode % 2 == 0) {

        printIslandMain();
    }
    elsif (   ($HlbbsMode == 5)
           || ($HlbbsMode == 7) ) {

        tempHeader() if ($jumpTug !~ /location/);
        print $jumpTug;
        unlock();
        exit;
    }
    else {

        ownerMain();
    }
}

#----------------------------------------------------------------------
# ローカル掲示板のメッセージを一つ後ろにずらす
sub slideLbbsMessage {
    my ($lbbs) = @_;

    pop(@$lbbs);
    unshift(@$lbbs, $lbbs->[0]);
}


#----------------------------------------------------------------------
# ローカル掲示板のメッセージを一つ前にずらす
sub slideBackLbbsMessage {
    my ($lbbs, $number) = @_;

    splice(@$lbbs, $number, 1);
    $lbbs->[$HlbbsMax - 1] = '0<<0>>';
}


#----------------------------------------------------------------------
# テンプレートその他
#----------------------------------------------------------------------
sub tempLbbsMain {
    my ($mode) = @_;

    out('<div id="localBBS" align="center">');
    tempLbbsHead();     # ローカル掲示板
    out('</div>');
    out('  <div id="localBBS" align="left">');
    # 書き込みフォーム
    if ($mode) {
        tempLbbsInputOW();
    }
    else {
        tempLbbsInput();
    }
    tempLbbsContents(); # 掲示板内容
    out('</div>');
}


#----------------------------------------------------------------------
# ローカル掲示板
sub tempLbbsHead {
    out(<<END);
<hr>
${HtagBig_}<span class='Nret'>${HtagName_}${HcurrentName}${H_tagName}</span><span class='Nret'>観光者通信</span>${H_tagBig}<br>
END
}


#----------------------------------------------------------------------
# ローカル掲示板入力フォーム
sub tempLbbsInput {
    out(<<END);
<form action="$HthisFile" method="POST">
END
    if ($HlbbsMoneyPublic + $HlbbsMoneySecret > 0) {
        # 発言は有料
        out('<div align="center"><b>※</b>');
        out("公開通信は<b>$HlbbsMoneyPublic$HunitMoney</b>です。") if ($HlbbsMoneyPublic > 0);
        out("極秘通信は<b>$HlbbsMoneySecret$HunitMoney</b>です。") if ($HlbbsMoneySecret > 0);
        out('</div>');
    }
    my $col = ' colspan=2' if(!$HlbbsAnon);

    # out("<b>※</b>${AfterName}を持っている方は名前を変更しても所有者名が使われます。");

    out(<<END);
  <table border>
    <tr>
      <th>名前<small>(全角${HlengthLbbsName}字まで)</small></th>
      <th $col>内容<small>(全角${HlengthLbbsMessage}字まで)</small></th>
      <th>通信方法</th>
    </tr>
    <tr>
      <td>
        <input type="text" size="30" MAXLENGTH="30" name="LBBSNAME" value="$HdefaultName">
      </td>
      <td $col>
        <input type="text" size="70" name="LBBSMESSAGE">
      </td>
      <td>
        <input type="radio" name="LBBSTYPE" value="PUBLIC" checked>公開<br>
        <input type="radio" name="LBBSTYPE" value="SECRET">極秘
      </td>
    </tr>
    <tr>
      <th>パスワード</th>
      <th>${AfterName}名</th>
      <th $col>動作</th>
    </tr>
    <tr>
      <td>
        <input type="password" size="16" maxlength='16' name="PASSWORD" value="$HdefaultPassword">
      </td>
      <td>
        <select name="ISLANDID2">$HislandList</select>
END
    out(<<END) if ($HlbbsAnon);
        <input type="radio" name="LBBSTYPE" value="ANON">観光客
END

    out(<<END);
      </td>
      <td>
        <div align='center'>
          <input type="submit" value="記帳する" name="LbbsButtonSS$HcurrentID">
          <input type="submit" value="極秘確認" name="LbbsButtonCK$HcurrentID">
        </div>
      </td>
END
    if (!$HlbbsAnon) {
        out(<<END);
      <td align="right">
番号
        <select name="NUMBER">
END
        {
            # 発言番号
            my ($j, $i);
            for($i = 0; $i < $HlbbsMax; $i++) {
                $j = $i + 1;
                out("<option value=$i>$j\n");
            }
        }
        out(<<END);
        </select><br>
        <input type="submit" value="削除" name="LbbsButtonDS$HcurrentID">
      </td>
END
    }
    out(<<END);
    </tr>
  </table>
</form>
END
}

#----------------------------------------------------------------------
# ローカル掲示板入力フォーム owner mode用
sub tempLbbsInputOW {

    out(<<END);
<form action="$HthisFile" method="POST">
<input type="hidden" name="JAVAMODE" value="$HjavaMode">
<table border>
  <tr>
    <th>名前<small>(全角${HlengthLbbsName}字まで)</small></th>
    <th colspan="2">内容<small>(全角${HlengthLbbsMessage}字まで)</small></th>
  </tr>
  <tr>
    <td><input type="text" size="32" maxlength="32" name="LBBSNAME" value="$HdefaultName"></td>
    <td colspan="2"><input type="text" SIZE="80" name="LBBSMESSAGE"></td>
  </tr>
  <tr>
    <th>パスワード</th>
    <th colspan="2">動作</th>
  </tr>
  <tr>
    <td><input type="password" size="16" maxlength="16" name="PASSWORD" value="$HdefaultPassword"></td>
    <td align="right">
      <input type="submit" value="記帳する" name="LbbsButtonOW$HcurrentID">
    </td>
    <td align="right">
番号
      <select name="NUMBER">
END
    {
        # 発言番号
        my ($j, $i);
    	for($i = 0; $i < $HlbbsMax; $i++) {
            $j = $i + 1;
            out("<OPTION VALUE=$i>$j\n");
        }
    	out("<OPTION VALUE=$HlbbsMax>全\n");
    }
    out(<<END);
      </select>
      <input type="submit" value="削除する" name="LbbsButtonDL$HcurrentID">
    </td>
  </tr>
</table>
</form>
END
}

#----------------------------------------------------------------------
# ローカル掲示板内容
sub tempLbbsContents {
    my ($lbbs, $line);
    $lbbs = $Hislands[$HcurrentNumber]->{'lbbs'};
    out(<<END);
<table border>
  <tr>
    <th>番号</th>
    <th>記帳内容</th>
  </tr>
END

    my ($i , $j);
    my ($speaker);
    my ($sNo);
    my ($sName, $sID);

    for ($i = 0; $i < $HlbbsMax; $i++) {
        $line = $lbbs->[$i];
        if ($line =~ /([0-9]*)\<(.*)\<([0-9]*)\>(.*)\>(.*)$/) {
            $j = $i + 1;
            out("<tr><td align='center'>$HtagNumber_$j$H_tagNumber</td>");

#           $speaker = "<span class='lbbsST'><B><SMALL>($2)</SMALL></B></span>" if ($HlbbsSpeaker && ($2 ne ''));
            ($sName, $sID) = split(/,/, $2);
            $sNo = $HidToNumber{$sID} if (defined $sID);
            $speaker = '';
            if (   ($HlbbsSpeaker)
                && ($sName)) {

                if (defined $sNo) {
                    $speaker = "\n      <span class='lbbsST'><b><small>(<a style=\"text-decoration:none\" href=\"$HthisFile?Sight=$sID\">$sName</a>)</small></b></span>\n";
                }
                else {
                    $speaker = "\n      <span class='lbbsST'><b><small>($sName)</small></b></span>\n";
                }
            }
            out("    <td>\n");
            if ($3 == 0) {
                # 観光者
                if ($1 == 0) {
                    # 公開
                    out("      $HtagLbbsSS_$4 &gt; $5$H_tagLbbsSS $speaker\n");
                }
                else {
                    # 極秘
                    if (   ($HmainMode ne 'owner')
                        && (($HspeakerID eq '') || ($sID != $HspeakerID))) {
                        # 観光客
                        out("<div class='t_center'><span class='lbbsST'>- 極秘 -</span></div>");
                    }
                    else {
                        # オーナー
                        out("      $HtagLbbsSS_$4 &gt;(秘) $5$H_tagLbbsSS $speaker\n");
                    }
                }
            }
            else {
                # 島主
                out("      $HtagLbbsOW_$4 &gt; $5$H_tagLbbsOW $speaker\n");
            }
            out(<<END);
    </td>
  </tr>
END
        }
    }

    out(<<END);
</table>
END
}

#----------------------------------------------------------------------
# ローカル掲示板で名前かメッセージがない場合
sub tempLbbsNoMessage {
    out(<<END);
${HtagBig_}名前または内容の欄が空欄です。${H_tagBig}$HtempBack
END
}

#----------------------------------------------------------------------
# 書きこみ削除
sub tempLbbsDelete {
    out(<<END);
${HtagBig_}記帳内容を削除しました。${H_tagBig}<hr>
END
}

#----------------------------------------------------------------------
# コマンド登録
sub tempLbbsAdd {
    out(<<END);
${HtagBig_}記帳を行いました。${H_tagBig}<hr>
END
}

#----------------------------------------------------------------------
# 通信資金足りず
sub tempLbbsNoMoney {
    out(<<END);
${HtagBig_}資金不足のため記帳できません。${H_tagBig}$HtempBack
END
}

1;
