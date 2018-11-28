# うらにわ -uRAniwa-: http://snow.prohosting.com/awinokah/
#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# ローカル掲示板モジュール(ver1.00)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
#――――――――――――――――――――――――――――――――――――
#							  箱庭諸島 2nd
#								  v1.5
#							 箱庭諸島 海戦
#								  v1.3
#					  by 親方 webgame@oyoyo.ne.jp
#					http://www.oyoyo.ne.jp/webgame/
#――――――――――――――――――――――――――――――――――――
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
    if ($HlbbsMode < 2 || $HlbbsMode == 5) {
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
            tempHeader() if($HlbbsMode == 5 || $HlbbsMode == 7);
            unlock();
            tempWrongPassword();
            return;
        }

        # オーナー名を設定
        # $HlbbsName = $island->{'owner'};
    } elsif ($HlbbsMode == 0) {
        # 観光者モード
        my($sIsland);

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
			my($cost) = ($HlbbsType eq 'PUBLIC') ? $HlbbsMoneyPublic : $HlbbsMoneySecret;
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
			my $name = islandName($sIsland);
			$speaker = $name . ',' . $HspeakerID;
		} else {
			# 匿名
			$speaker = $ENV{'REMOTE_HOST'};
			$speaker = $ENV{'REMOTE_ADDR'} if ($speaker eq '');
		}

	} elsif ($HlbbsMode == 2) {
		# 観光者削除モード
		my($sIsland);

		# idから島番号を取得
		my($number) = $HidToNumber{$HspeakerID};
		$sIsland = $Hislands[$number];

		# なぜかその島がない場合
		if($number eq '') {
			unlock();
			tempProblem();
			return;
		}

		# IDチェック
		$lbbs->[$HcommandPlanNumber] =~ /[0-9]*\<.*,([0-9]*)\<[0-9]*\>.*\>.*$/;
		my $wId = $1;
		if($wId != $HspeakerID) {
			# ID間違い
			unlock();
			tempWrong("あなたの発言ではありません！");
			return;
		}

		# パスワードチェック
		if(!checkPassword($sIsland,$HinputPassword)) {
			# password間違い
			unlock();
			tempWrongPassword();
			return;
		}
	} elsif ($HlbbsMode == 4) {
		# 観光者極秘通信確認モード
		my($sIsland);

		# idから島番号を取得
		my($number) = $HidToNumber{$HspeakerID};
		$sIsland = $Hislands[$number];

		# なぜかその島がない場合
		if($number eq '') {
			unlock();
			tempProblem();
			return;
		}

		# パスワードチェック
		if(!checkPassword($sIsland,$HinputPassword)) {
			# password間違い
			unlock();
			tempWrongPassword();
			return;
		}
	}

	# モードで分岐
	if($HlbbsMode == 4) {
		printIslandMain();
		return;
	} elsif($HlbbsMode == 2 || $HlbbsMode == 3 || $HlbbsMode == 7) {
		# 削除モード
		if(($HlbbsMode == 3 || $HlbbsMode == 7) && ($HcommandPlanNumber == $HlbbsMax)) {
			foreach (0..($HlbbsMax - 1)) {
				$lbbs->[$_] = '0<<0>>';
			}
		} else {
			# メッセージを前にずらす
			slideBackLbbsMessage($lbbs, $HcommandPlanNumber);
		}
		tempLbbsDelete() if($HlbbsMode != 7);
	} else {
		# 記帳モード
		$speaker = "管理人,0" if($HlbbsMode == 5);
		if ($HlbbsType ne 'SECRET') {
			# 公開と匿名
			$speaker = "0<$speaker";
		} else {
			# 極秘
			$speaker = "1<$speaker";
		}
		# メッセージを後ろにずらす
		slideLbbsMessage($lbbs);

		# メッセージ書き込み
		my($message);
		if($HlbbsMode == 1) {
			$message = '1';
		} else {
			$message = '0';
		}
		$HlbbsName = "$HislandTurn：" . htmlEscape($HlbbsName);
		$HlbbsMessage = htmlEscape($HlbbsMessage);
		$lbbs->[0] = "$speaker<$message>$HlbbsName>$HlbbsMessage";

		tempLbbsAdd() if($HlbbsMode != 5);
	}

	# データ書き出し
	writeIslandsFile($HcurrentID);

	# もとのモードへ
	if($HlbbsMode % 2 == 0) {
		printIslandMain();
	} elsif($HlbbsMode == 5 || $HlbbsMode == 7) {
		tempHeader() if($jumpTug !~ /location/);
		print $jumpTug;
		unlock();
		exit;
	} else {
		ownerMain();
	}
}

#----------------------------------------------------------------------
# ローカル掲示板のメッセージを一つ後ろにずらす
sub slideLbbsMessage {
    my ($lbbs) = @_;

    my ($i);
    pop(@$lbbs);
    unshift(@$lbbs, $lbbs->[0]);
}


#----------------------------------------------------------------------
# ローカル掲示板のメッセージを一つ前にずらす
sub slideBackLbbsMessage {
    my ($lbbs, $number) = @_;

    my ($i);
    splice(@$lbbs, $number, 1);
    $lbbs->[$HlbbsMax - 1] = '0<<0>>';
}


#----------------------------------------------------------------------
# テンプレートその他
#----------------------------------------------------------------------
sub tempLbbsMain {
    my($mode) = @_;

    out('<DIV ID="localBBS">');
    tempLbbsHead();     # ローカル掲示板
    # 書き込みフォーム
    if ($mode) {
        tempLbbsInputOW();
    } else {
        tempLbbsInput();
    }
    tempLbbsContents(); # 掲示板内容
    out('</DIV>');
}


#----------------------------------------------------------------------
# ローカル掲示板
sub tempLbbsHead {
    out(<<END);
<HR>
${HtagBig_}<span class='Nret'>${HtagName_}${HcurrentName}${H_tagName}</span><span class='Nret'>観光者通信</span>${H_tagBig}<BR>
END
}


#----------------------------------------------------------------------
# ローカル掲示板入力フォーム
sub tempLbbsInput {
    out(<<END);
<FORM action="$HthisFile" method="POST">
END
    if ($HlbbsMoneyPublic + $HlbbsMoneySecret > 0) {
        # 発言は有料
        out('<DIV align="center"><B>※</B>');
        out("公開通信は<B>$HlbbsMoneyPublic$HunitMoney</B>です。") if ($HlbbsMoneyPublic > 0);
        out("極秘通信は<B>$HlbbsMoneySecret$HunitMoney</B>です。") if ($HlbbsMoneySecret > 0);
        out('</DIV>');
    }
    my $col = ' colspan=2' if(!$HlbbsAnon);

    # out("<B>※</B>${AfterName}を持っている方は名前を変更しても所有者名が使われます。");

    out(<<END);
<TABLE BORDER>
<TR>
<TH>名前<small>(全角${HlengthLbbsName}字まで)</small></TH>
<TH$col>内容<small>(全角${HlengthLbbsMessage}字まで)</small></TH>
<TH>通信方法</TH>
</TR>
<TR>
<TD><INPUT type="text" size="30" MAXLENGTH="30" name="LBBSNAME" value="$HdefaultName"></TD>
<TD$col><INPUT type="text" SIZE="70" name="LBBSMESSAGE"></TD>
<TD>
<INPUT type="radio" name="LBBSTYPE" value="PUBLIC" CHECKED>公開<br>
<INPUT type="radio" name="LBBSTYPE" value="SECRET">極秘
</TD>
</TR>
<TR>
<TH>パスワード</TH>
<TH>${AfterName}名</TH>
<TH$col>動作</TH>
</TR>
<TR>
<TD><INPUT type="password" size="16" MAXLENGTH=16 name="PASSWORD" value="$HdefaultPassword"></TD>
<TD>
<SELECT name="ISLANDID2">$HislandList</SELECT>
END
    out(<<END) if ($HlbbsAnon);
<INPUT type="radio" name="LBBSTYPE" value="ANON">観光客
END

    out(<<END);
</TD>
<TD><DIV align='center'>
<INPUT type="submit" value="記帳する" name="LbbsButtonSS$HcurrentID">
<INPUT type="submit" value="極秘確認" name="LbbsButtonCK$HcurrentID">
</DIV></TD>
END
    if (!$HlbbsAnon) {
        out(<<END);
<TD align="right">
番号
<SELECT name="NUMBER">
END
        {
            # 発言番号
            my($j, $i);
            for($i = 0; $i < $HlbbsMax; $i++) {
                $j = $i + 1;
                out("<OPTION value=$i>$j\n");
            }
        }
        out(<<END);
</SELECT><br>
<INPUT type="submit" value="削除" name="LbbsButtonDS$HcurrentID">
</TD>
END
    }
    out(<<END);
</TR>
</TABLE>
</FORM>
END
}

#----------------------------------------------------------------------
# ローカル掲示板入力フォーム owner mode用
sub tempLbbsInputOW {

	out(<<END);
<FORM action="$HthisFile" method="POST">
<INPUT type="hidden" NAME=JAVAMODE value="$HjavaMode">
END
	# out("<B>※</B>名前を変更しても所有者名が使われます。");

	out(<<END);
<TABLE BORDER>
<TR>
<TH>名前<small>(全角${HlengthLbbsName}字まで)</small></TH>
<TH COLSPAN=2>内容<small>(全角${HlengthLbbsMessage}字まで)</small></TH>
</TR>
<TR>
<TD><INPUT type="text" SIZE="32" MAXLENGTH="32" NAME="LBBSNAME" value="$HdefaultName"></TD>
<TD COLSPAN=2><INPUT type="text" SIZE="80" NAME="LBBSMESSAGE"></TD>
</TR>
<TR>
<TH>パスワード</TH>
<TH COLSPAN=2>動作</TH>
</TR>
<TR>
<TD><INPUT type="password" SIZE="16" MAXLENGTH="16" NAME="PASSWORD" value="$HdefaultPassword"></TD>
<TD align=right>
<INPUT type="submit" VALUE="記帳する" NAME="LbbsButtonOW$HcurrentID">
</TD>
<TD align=right>
番号
<SELECT NAME=NUMBER>
END
    {
    	# 発言番号
    	my($j, $i);
    	for($i = 0; $i < $HlbbsMax; $i++) {
    		$j = $i + 1;
    		out("<OPTION VALUE=$i>$j\n");
    	}
    	out("<OPTION VALUE=$HlbbsMax>全\n");
    }
	out(<<END);
</SELECT>
<INPUT type="submit" VALUE="削除する" NAME="LbbsButtonDL$HcurrentID">
</TD>
</TR>
</TABLE>
</FORM>
END
}

#----------------------------------------------------------------------
# ローカル掲示板内容
sub tempLbbsContents {
    my ($lbbs, $line);
    $lbbs = $Hislands[$HcurrentNumber]->{'lbbs'};
    out(<<END);
<TABLE BORDER>
<TR>
<TH>番号</TH>
<TH>記帳内容</TH>
</TR>
END

    my ($i , $j);
    my ($speaker);
    my ($sNo);
    my ($sName, $sID);

    for ($i = 0; $i < $HlbbsMax; $i++) {
        $line = $lbbs->[$i];
        if ($line =~ /([0-9]*)\<(.*)\<([0-9]*)\>(.*)\>(.*)$/) {
            $j = $i + 1;
            out("<TR><TD align='center'>$HtagNumber_$j$H_tagNumber</TD>");

#           $speaker = "<span class='lbbsST'><B><SMALL>($2)</SMALL></B></span>" if ($HlbbsSpeaker && ($2 ne ''));
            ($sName, $sID) = split(/,/, $2);
            $sNo = $HidToNumber{$sID} if (defined $sID);
            $speaker = '';
            if ($HlbbsSpeaker && ($sName)) {
                if(defined $sNo){
                    $speaker = "<span class='lbbsST'><B><SMALL>(<A STYlE=\"text-decoration:none\" HREF=\"$HthisFile?Sight=$sID\">$sName</A>)</SMALL></B></span>";
                } else {
                    $speaker = "<span class='lbbsST'><B><SMALL>($sName)</SMALL></B></span>";
                }
            }
            if ($3 == 0) {
                # 観光者
                if ($1 == 0) {
                    # 公開
                    out("<TD>$HtagLbbsSS_$4 > $5$H_tagLbbsSS $speaker</TD></TR>");
				} else {
					# 極秘
					if (($HmainMode ne 'owner') &&(($HspeakerID eq '') || ($sID != $HspeakerID))) {
						# 観光客
						out("<TD><DIV align='center'><span class='lbbsST'>- 極秘 -</span></DIV></TD></TR>");
					} else {
						# オーナー
						out("<TD>$HtagLbbsSS_$4 >(秘) $5$H_tagLbbsSS $speaker</TD></TR>");
                    }
                }
            } else {
                # 島主
                out("<TD>$HtagLbbsOW_$4 > $5$H_tagLbbsOW $speaker</TD></TR>");
            }
        }
    }

    out(<<END);
</TD></TR></TABLE>
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
${HtagBig_}記帳内容を削除しました。${H_tagBig}<HR>
END
}

#----------------------------------------------------------------------
# コマンド登録
sub tempLbbsAdd {
    out(<<END);
${HtagBig_}記帳を行いました。${H_tagBig}<HR>
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
