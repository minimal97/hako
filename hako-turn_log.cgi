#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# ターン進行モジュール(ver1.02)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Hakoniwa R.A. ver1.11
# メインスクリプト(箱庭諸島 ver2.30)
# 使用条件、使用方法等は、read-renas.txtファイルを参照
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------
# ファイルが大きいので、ログテンプレートだけ分割
# turnでインクルードすること。

#----------------------------------------------------------------------
# ログテンプレート
#----------------------------------------------------------------------
# 軍事物資調達 未使用
sub logArmSupply {
	my ($id, $name, $comName, $num) = @_;
	logOut("${HtagName_}${name}${H_tagName}が、${HtagNumber_}$num個${H_tagNumber}の${HtagComName_}$comName${H_tagComName}を行いました。",$id);
}

# 首都できた
sub logShuto {
    my ($id, $name, $lName, $sName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>は、<b>首都$sName</b>として${AfterName}の中心的都市へとなりました。",$id);
    logHistory("${HtagName_}${name}${H_tagName}に<b>首都$sName</b>が出来ました。");
}

# 温泉発見
sub logHotFound {
    my ($id, $name, $point, $comName, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}で<b>$str</b>の予算をつぎ込んだ${HtagComName_}${comName}${H_tagComName}が行われ、<b>温泉が掘り当てられました</b>。",$id);
}

# 温泉発見ならず
sub logHotFail {
    my ($id, $name, $point, $comName, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}で<b>$str</b>の予算をつぎ込んだ${HtagComName_}${comName}${H_tagComName}が行われましたが、温泉は見つかりませんでした。",$id);
}

# 神殿からの収入
sub logSinMoney {
    my ($id, $name, $str) = @_;
    logSecret("${HtagName_}${name}$point${H_tagName}の<b>神殿</b>で祝いの祭りが行われ、<b>$str</b>の収益が上がりました。",$id);
}

# 神社からの収入
sub logJinMoney {
    my ($id, $name, $str) = @_;
    logSecret("${HtagName_}${name}$point${H_tagName}の<b>神社</b>で祝いの祭りが行われ、<b>$str</b>の収益が上がりました。",$id);
}

# 援助金からの収入
sub logEnjo {
    my ($id, $name, $lName, $point, $str) = @_;
    logOut("開発進行委員会から${HtagName_}${name}${H_tagName}に<b>$str</b>の援助金が支給されたようです！",$id);
}

# ミサイルまとめログ
sub logMsTotal {
    my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $count, $mukou, $bouei, $kaijumukou, $kaijuhit, $fuhatu) = @_;
    logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}$count発の${comName}${H_tagComName}を行いました。<br>　　　${HtagName_}結果${H_tagName}⇒(無効$mukou発/防衛$bouei発/怪獣相殺$kaijumukou発/怪獣命中$kaijuhit発/不発弾$fuhatu発)",$id, $tId);
}

# ステルスミサイルまとめログ
sub logMsTotalS {
    my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $count, $mukou, $bouei, $kaijumukou, $kaijuhit, $fuhatu) = @_;
    logSecret("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}$count発の${comName}${H_tagComName}を行いました。<br>　　　${HtagName_}結果${H_tagName}⇒(無効$mukou発/防衛$bouei発/怪獣相殺$kaijumukou発/怪獣命中$kaijuhit発/不発弾$fuhatu発)",$id);
    logLate("<b>何者か</b>が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}$count発の${comName}${H_tagComName}を行いました。<br>　　　${HtagName_}結果${H_tagName}⇒(無効$mukou発/防衛$bouei発/怪獣相殺$kaijumukou発/怪獣命中$kaijuhit発)", $tId);
}

# 首都を攻撃する
sub logMonsAttacks {
    my ($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>は怪獣に${HtagDisaster_}攻撃${H_tagDisaster}され被害を受けました。",$id);
}

# 首都を攻撃する
sub logMonsAttacksSecret {
    my ($id, $name, $lName, $point) = @_;
    logSecret("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>は怪獣に${HtagDisaster_}攻撃${H_tagDisaster}され被害を受けました。",$id);
}

# 資金・食料・衛星足りない、許可されない
sub logNoAny { #20
	my ($id, $name, $comName, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}で予定されていた${HtagComName_}$comName${H_tagComName}は、$strため中止されました。",$id);
}

# マスコットが攻撃する
sub logMsAttackt {
    my ($id, $name, $mName, $point, $cPoint, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}${H_tagName}の<b>$mName</b>が$tPoint<b>$tName</b>を攻撃し${HtagDisaster_}$point${H_tagDisaster}のダメージを与え${HtagDisaster_}$cPoint${H_tagDisaster}のダメージを受けました。",$id, $tId);
}

# ミカエル像完成
sub logMsAttackmika {
    my ($id, $name, $mName, $point, $cPoint, $tName) = @_;
    logOut("${HtagName_}${name}${H_tagName}の<b>$mName</b>と<b>$tName</b>の戦いは伝説となり、${AfterName}民は<b>幸福の女神像</b>を建造しました。",$id, $tId);
}

# 攻撃で首はね
sub logItiAttackms {
    my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>が$tPoint<b>$tName</b>を斬りつけました。",$id, $tId);
}


# 氷で串刺し
sub logIceAttack {
    my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>の発する氷の矢は${HtagName_}$tPoint${H_tagName}の<b>$tName</b>の中心を貫きました。",$id, $tId);
}

# 焼き
sub logFireAttack {
    my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>の呼び起こした${HtagDisaster_}炎${H_tagDisaster}は${HtagName_}$tPoint${H_tagName}の<b>$tName</b>を焼きました。",$id, $tId);
}

# ヘルファイア
sub logHellAttack {
    my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>の呼び起こした${HtagDisaster_}地獄の炎${H_tagDisaster}は${HtagName_}$tPoint${H_tagName}の<b>$tName</b>を焼き尽くしました。",$id, $tId);
}

# 新型軍艦が攻撃する
sub logFuneAttackSSS {
    my ($id, $name, $lName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>が<b>エネルギー砲</b>を発射し、<b>$tName</b>に命中しました。",$id, $tId);
}

# 新型軍艦が攻撃する
sub logFuneAttackSSSR {
    my ($id, $name, $lName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}${H_tagName}の<b>$tName</b>は<b>木っ端微塵</b>になりました。",$id, $tId);
}

# 新型軍艦が攻撃する
sub logFuneAttackSSST {
    my ($id, $name, $lName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}${H_tagName}の<b>$tName</b>は<b>木っ端微塵</b>になり、<b>$lName</b>は${HtagDisaster_}オーバーヒート${H_tagDisaster}により${HtagDisaster_}大爆発${H_tagDisaster}しました。",$id, $tId);
}

# 卵孵化
sub logEggBomb {
	my ($id, $name, $lName, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>から<b>$mName</b>が出現しました。",$id);
}

# 卵解除被害
sub logEggDamage {
	my ($id, $name, $landName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$landName</b>は${HtagDisaster_}卵の破裂によるエネルギー${H_tagDisaster}により水没しました。",$id);
}

# いのら出撃
sub logMstakeon {
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>は<b>怪獣退治</b>に向かいました。",$id);
}

# いのら帰宅
sub logMstakeokaeri {
	my ($id, $name, $lName, $point, $tName) = @_;
	logOut("${HtagName_}${name}${H_tagName}の<b>$lName</b>が${HtagName_}$point${H_tagName}の<b>$tName</b>に帰ってきました。おつかれさま。",$id);
}

# いのら家出
sub logMstakeiede {
	my ($id, $name, $lName, $point, $tName) = @_;
	logOut("${HtagName_}${name}${H_tagName}の<b>$lName</b>は帰るべき家がないために旅に出ました。",$id);
}

# いのら行方不明
sub logMstakeoff {
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>は<b>マスコット怪獣</b>損失のため運営困難になりました。",$id);
}

# いのら家出
sub logHimeKaeru {
	my ($id, $name, $lName) = @_;
	logOut("${HtagName_}${name}${H_tagName}の<b>$lName</b>は、あばれ疲れたので帰りました。",$id);
}

# 重税逆ギレ
sub logKire {
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}の<b>重税</b>に${AfterName}民は${HtagDisaster_}キレ${H_tagDisaster}ました！！",$id);
}

# 重税被害
sub logKireDamage {
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>は${HtagDisaster_}暴れる${AfterName}民${H_tagDisaster}によって${HtagDisaster_}破壊${H_tagDisaster}されました。",$id);
}

# 重税被害
sub logZeikin_fuman {
    my ($id, $name) = @_;
    logOut("${HtagName_}${name}${H_tagName}の住民は、<b>税金に対して、切り捨てられる資金が多いことに、不満</b>を感じています。",$id);
}

# 怪獣現る(魔方陣)
sub logMonsComemagic {
	my ($id, $name, $mName, $point, $lName) = @_;
	logOut("${HtagName_}${name}${H_tagName}の破壊された<b>魔方陣</b>から<b>$mName</b>出現！！",$id);
}

# 怪獣、周囲を凍て尽くす
sub logMonsCold {
	my ($id, $name, $lName, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>は<b>$mName</b>を取り巻く冷気により凍てつきました。",$id);
}

# 卵
sub logEggFound {
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}での${HtagComName_}$comName${H_tagComName}中に、<b>何かの卵</b>が発見され${HtagComName_}$comName業者${H_tagComName}には破壊が無理なので放置することにしました。",$id);
}

# 遺跡
sub logIsekiFound {
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}での${HtagComName_}$comName${H_tagComName}中に、<b>古代遺跡</b>が発見され<b>${AfterName}の重要埋蔵文化財</b>に指定されました。",$id);
}

# 受賞
sub logPrizet {
	my ($id, $name, $pName, $value) = @_;
	my ($str) = "(賞金${HtagMoney_}$value${H_tagMoney})" if($value > 0);
	logOut("${HtagName_}${name}${H_tagName}が<b>$pName</b>を受賞しました。$str",$id);
	logHistory("${HtagName_}${name}${H_tagName}、<b>$pName</b>を受賞$str");
}

# 箱庭カップ
sub logHC {
	my ($id, $name, $stsanka) = @_;
	if ($stsanka) {
#	logHistory("${HtagName_}Hakoniwa Cup $HislandTurn${H_tagName}開催！<b>参加数</b>${HtagNumber_}$stsanka${AfterName}！${H_tagNumber}");
		logHcup("${HtagName_}Hakoniwa Cup $HislandTurn${H_tagName}開催！<b>参加数</b>${HtagNumber_}$stsanka${AfterName}！${H_tagNumber}");
	}
    else {
		logHcup("${HtagName_}Hakoniwa Cup $HislandTurn${H_tagName}は、参加する${AfterName}がなかったため${HtagNumber_}中止になりました。${H_tagNumber}");
	}
}

# 箱庭カップ開会式
sub logHCstart {
	my ($id, $name, $str) = @_;
#   logHistory("${HtagName_}${name}${H_tagName}で<b>Hakoniwa Cup 開会式</b>が行なわれ、${HtagMoney_}$str${H_tagMoney}の経済効果を巻き起こしました。",$id);
	logLate("${HtagName_}${name}${H_tagName}で<b>Hakoniwa Cup 開会式</b>が行なわれ、${HtagMoney_}$str${H_tagMoney}の経済効果を巻き起こしました。",$id);
	logHcup("${HtagName_}${name}${H_tagName}で<b>Hakoniwa Cup 開会式</b>が行なわれ、${HtagMoney_}$str${H_tagMoney}の経済効果を巻き起こしました。");
}

# 箱庭カップ試合
sub logHCgame {
	my ($id, $tId, $name, $tName, $lName, $gName, $goal, $tgoal, $Teamname, $tTeamname) = @_;
	my ($tena, $ttena);
	my ($home, $away);

    $tena = "";
    $tena = "(${Teamname})" if ( length($Teamname) > 0);
    $ttena = "";
    $ttena = "(${tTeamname})" if ( length($tTeamname) > 0);

	if ($goal < $tgoal) {
		$str = "${HtagLose_}${name}代表${tena}${H_tagLose}<b>VS</b>${HtagWin_}${tName}代表${ttena}${H_tagWin} ⇒ ${HtagLose_}$goal${H_tagLose}<b>−</b>${HtagWin_}$tgoal${H_tagWin}";
	}
    else {
		$str = "${HtagWin_}${name}代表${tena}${H_tagWin}<b>VS</b>${HtagLose_}${tName}代表${ttena}${H_tagLose} ⇒ ${HtagWin_}$goal${H_tagWin}<b>−</b>${HtagLose_}$tgoal${H_tagLose}";
	}
	logLate("${HtagName_}${name}${H_tagName}で<b>Hakoniwa Cup $gName</b>が行われました。$str",$id, $tId);
	logHcup("${HtagName_}Hakoniwa Cup ${gName}${H_tagName}、$str");
}

# 箱庭カップ勝利
sub logHCwin {
	my ($id, $name, $cName, $str) = @_;
	logLate("${HtagName_}${name}代表${H_tagName}の<b>$cName</b>は${HtagName_}${name}${H_tagName}に${HtagMoney_}$str${H_tagMoney}の経済効果を巻き起こしました。",$id);
}

# 箱庭カップ優勝
sub logHCwintop {
	my ($id, $name, $cName) = @_;
#   logHistory("${HtagName_}${name}代表${H_tagName}、${HtagWin_}Hakoniwa Cup $cName優勝！${H_tagWin}",$id);
	logLate("${HtagWin_}${name}代表${H_tagWin}、${HtagName_}Hakoniwa Cup $cName${H_tagName}${HtagWin_}優勝！${H_tagWin}",$id);
	logHcup("${HtagWin_}${name}代表${H_tagWin}、${HtagName_}Hakoniwa Cup $cName${H_tagName}${HtagWin_}優勝！${H_tagWin}");
}

# 箱庭カップ不戦勝
sub logHCantiwin {
	my ($id, $name, $gName) = @_;
	logLate("${HtagName_}Hakoniwa Cup ${gName}${H_tagName}、${HtagWin_}${name}代表${H_tagWin}は、対戦チームがいないため${HtagWin_}不戦勝${H_tagWin}となりました。",$id);
	logHcup("${HtagName_}Hakoniwa Cup ${gName}${H_tagName}、${HtagWin_}${name}代表${H_tagWin}は、対戦チームがいないため${HtagWin_}不戦勝${H_tagWin}。");
}

# 箱庭カップ
sub logHCsin {
	my ($id, $name, $stsin) = @_;
#   logHistory("${HtagName_}Hakoniwa Cup 決勝トーナメント進出${AfterName}!!${H_tagName}<br><font size=\"-1\"><b>$stsin</b></font>");
	logHcup("${HtagName_}Hakoniwa Cup 決勝トーナメント進出${AfterName}!!${H_tagName}<br><font size=\"-1\"><b>$stsin</b></font>");
}

# 観光ありがとうございます
sub logKankouMigrate {
	my ($id, $tId, $name, $lName, $tName, $point, $pop) = @_;
	logOut("${HtagName_}${tName}${H_tagName}から${HtagName_}${name}$point${H_tagName}の<b>$lName</b>へ<b>$pop${HunitPop}</b>の観光者が来てくれました。ありがとうございます。",$id, $tId);
}

# ミサイル撃とうとしたが基地がない
sub logMsNoBase { #1
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}で予定されていた${HtagComName_}${comName}${H_tagComName}は、<b>ミサイル設備を保有していない</b>ために実行できませんでした。",$id);
}

# 対象地形の種類による失敗
sub logLandFail { #14
    my ($id, $name, $comName, $kind, $point) = @_;
    logOut("${HtagName_}${name}${H_tagName}で予定されていた${HtagComName_}$comName${H_tagComName}は、予定地の${HtagName_}$point${H_tagName}が<b>$kind</b>だったため中止されました。",$id);
}

# 対象地形の種類による失敗２
sub logLandFail2 { #5
	my ($id, $name, $comName, $point, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}で予定されていた${HtagComName_}$comName${H_tagComName}は、予定地の${HtagName_}$point${H_tagName}が$strため中止されました。",$id);
}

# 町を整地
sub logTownDel { #25
    my ($id, $name, $tName , $comName, $point, $lv) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}で<b>${tName}</b>に${HtagComName_}${comName}${H_tagComName}を行ったため、<b>${lv}${HunitPop}</b>が立ち去りました。",$id);
}

# 町を整地
sub logSouon { #25
    my ($id, $name, $point, $tName, $lv) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>${tName}</b>の騒音に耐え切れず、周囲の住民<b>${lv}${HunitPop}</b>が立ち去りました。",$id);
}

# 整地系成功
sub logLandSuc { #25
	my ($id, $name, $comName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}で${HtagComName_}${comName}${H_tagComName}が行われました。",$id);
}

# 整地系ログまとめ
sub logLandSucMatome {
	my ($id, $name, $comName, $point) = @_;
	logOut("${HtagName_}${name}${H_tagName}で${HtagComName_}${comName}${H_tagComName}が行われました。<br>　　<b>⇒</b> $point",$id);
}

# 衛星撃沈
sub logEiseifail { #1
	my ($id, $name, $comName, $point) = @_;
	logOut("${HtagName_}${name}${H_tagName}で${HtagComName_}${comName}${H_tagComName}が行われましたが打ち上げは${HtagDisaster_}失敗${H_tagDisaster}したようです。",$id);
}

# 油田発見
sub logOilFound { #1
	my ($id, $name, $point, $comName, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}で${HtagMoney_}$str${H_tagMoney}の予算をつぎ込んだ${HtagComName_}${comName}${H_tagComName}が行われ、<b>油田が掘り当てられました</b>。",$id);
}

# 油田発見200
sub logOil200Found { #1
	my ($id, $name, $point, $comName, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}で${HtagMoney_}$str${H_tagMoney}の予算をつぎ込んだ${HtagComName_}${comName}${H_tagComName}が行われ、<b>油田が掘り当てられました</b>。<br>200億で油田の碑が贈られました。",$id);
}

# 油田発見ならず
sub logOilFail { #1
	my ($id, $name, $point, $comName, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}で${HtagMoney_}$str${H_tagMoney}の予算をつぎ込んだ${HtagComName_}${comName}${H_tagComName}が行われましたが、油田は見つかりませんでした。",$id);
}

# 油田・関所・遊園地・帆船からの収入
sub logOilMoney { #9
	my ($id, $name, $lName, $point, $value, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>から、${HtagMoney_}$value${H_tagMoney}の$strが上がりました。",$id);
}

# 油田枯渇、広域被害その他
sub logDamageAny { #29
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>は$str",$id);
}

# 遊園地のイベント
sub logParkEvent { #4
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>でイベントが開催され、${HtagFood_}$str${H_tagFood}の食料が消費されました。",$id);
}

# 保険からの収入
sub logHoken { #1
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>の事故により、${HtagMoney_}$str${H_tagMoney}の保険がおりました。",$id);
}

# 土産からの収入
sub logMiyage { #1
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName記念碑公園</b>のお土産屋さんから${HtagMoney_}$str${H_tagMoney}の収入がありました。",$id);
}

# 優勝からの収入
sub logYusho { #1
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}の野球チームは${HtagName_}$point${H_tagName}の<b>$lName</b>で行われた箱庭リーグ決勝戦でみごと優勝し、${HtagMoney_}$str${H_tagMoney}の経済効果があがりました。",$id);
}

# TITANIC映画化
sub logTitanicEnd { #1
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>の沈没は映画化され、多くの人が涙を流しました。(${HtagMoney_}$str${H_tagMoney}の利益収入)",$id);
}

# 海底探索からの収入
sub logTansaku { #1
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>が財宝を発見！${HtagMoney_}$str${H_tagMoney}の価値があることがわかりました。",$id);
	logHistory("${HtagName_}${name}${H_tagName}の<b>$lName</b>が財宝を発見！");
}

# 海底探索の油田
sub logTansakuoil { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}で<b>$lName</b>が油田を発見！",$id);
}

# 幸運
sub logOilMoneyt { #1
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>が落とした羽根に${HtagMoney_}$str${H_tagMoney}の値が付きました。",$id);
}

# 幸運２
sub logParkEventt { #2
    my ($id, $name, $lName, $point, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>がもたらした豊作により、さらに${HtagFood_}$str${H_tagFood}の食料が出来ました。",$id);
}

# ハイテク企業の消費
sub logFactoryHT { #2
    my ($id, $name, $lName, $str) = @_;
    logSecret("${HtagName_}${name}${H_tagName}の<b>$lName</b>は、${HtagMoney_}$str${H_tagMoney}を消費しました。",$id);
}

# 船の収穫
sub logParkEventf { #2
    my ($id, $name, $lName, $point, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>は、${HtagFood_}$str${H_tagFood}の食料を得ました。",$id);
}

# 防衛施設、自爆セット
#sub logBombSet { #1
#   my($id, $name, $lName, $point) = @_;
#   logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>の<b>自爆装置がセット</b>されました。",$id);
#}

# 防衛施設、自爆作動
#sub logBombFire { #1
#   my($id, $name, $lName, $point) = @_;
#   logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>、${HtagDisaster_}自爆装置作動！！${H_tagDisaster}",$id);
#}

# 記念碑、発射
sub logMonFly { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>が<b>轟音とともに飛び立ちました</b>。",$id);
}

# 記念碑、落下
sub logMonDamage { #1
	my ($id, $name, $point) = @_;
	logOut("<b>何かとてつもないもの</b>が${HtagName_}${name}$point${H_tagName}地点に落下しました！！",$id);
}

# 植林orミサイル基地
sub logPBSuc { #3
	my ($id, $name, $comName, $point) = @_;
	logSecret("${HtagName_}${name}$point${H_tagName}で${HtagComName_}${comName}${H_tagComName}が行われました。",$id);
	logOut("こころなしか、${HtagName_}${name}${H_tagName}の<b>森</b>が増えたようです。",$id);
}

# ハリボテ
sub logHariSuc { #1
	my ($id, $name, $comName, $comName2, $point) = @_;
	logSecret("${HtagName_}${name}$point${H_tagName}で${HtagComName_}${comName}${H_tagComName}が行われました。",$id);
	logLandSuc($id, $name, $comName2, $point);
}

# 射程内に怪獣がいない
sub logNoTarget {
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}で予定されていた${HtagComName_}$comName${H_tagComName}は、射程内に怪獣がいないため中止されました。",$id);
}

# ミサイル撃ったが範囲外
sub logMsOut { #1
	my ($id, $tId, $name, $tName, $comName, $point) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、<b>領域外の海</b>に落ちた模様です。",$id, $tId);
}

# ステルスミサイル撃ったが範囲外
sub logMsOutS { #1
	my ($id, $tId, $name, $tName, $comName, $point) = @_;
	logSecret("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、<b>領域外の海</b>に落ちた模様です。",$id);
	logLate("<b>何者か</b>が${HtagName_}${tName}$point${H_tagName}へ向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、<b>領域外の海</b>に落ちた模様です。",$tId);
}

# 衛星破壊成功
sub logEiseiAtts { #1
	my ($id, $tId, $name, $tName, $comName, $tEiseiname) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}${H_tagName}に向けて${HtagComName_}${comName}${H_tagComName}を行い、<b>$tEiseiname</b>に命中。<b>$tEiseiname</b>は跡形もなく消し飛びました。",$id, $tId);
}

# 衛星破壊失敗
sub logEiseiAttf { #1
	my ($id, $tId, $name, $tName, $comName, $tEiseiname) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}${H_tagName}の<b>$tEiseiname</b>に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、何にも命中せず宇宙の彼方へと飛び去ってしまいました。。",$id, $tId);
}

# ミサイル撃ったが防衛施設でキャッチ
sub logMsCaught { #2
	my ($id, $tId, $name, $tName, $comName, $point, $tPoint) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、${HtagName_}$tPoint${H_tagName}地点上空にて力場に捉えられ、<b>空中爆発</b>しました。",$id, $tId);
}

# ステルスミサイル撃ったが防衛施設でキャッチ
sub logMsCaughtS { #2
	my ($id, $tId, $name, $tName, $comName, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、${HtagName_}$tPoint${H_tagName}地点上空にて力場に捉えられ、<b>空中爆発</b>しました。",$id);
	logLate("<b>何者か</b>が${HtagName_}${tName}$point${H_tagName}へ向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、${HtagName_}$tPoint${H_tagName}地点上空にて力場に捉えられ、<b>空中爆発</b>しました。",$tId);
}

# ミサイル撃ったが防衛衛星でキャッチ(STバレます)
sub logMsCaughtE { #1
	my ($id, $tId, $name, $tName, $comName, $point, $tPoint) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、<b>防衛衛星</b>に撃ち落とされました。",$id, $tId);
}

# ミサイル撃ったが効果なし
sub logMsNoDamage { #3
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $flag) = @_;
	my ($noga) = 'の';
	$noga = 'が' if ($flag);
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、${HtagName_}$tPoint${H_tagName}${noga}<b>$tLname</b>に落ちたので被害がありませんでした。",$id, $tId);
}

# ステルスミサイル撃ったが効果なし
sub logMsNoDamageS { #2
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $flag) = @_;
	my ($noga) = 'の';
	$noga = 'が' if ($flag);
	logSecret("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、${HtagName_}$tPoint${H_tagName}${noga}<b>$tLname</b>に落ちたので被害がありませんでした。",$id);
	logLate("<b>何者か</b>が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、${HtagName_}$tPoint${H_tagName}${noga}<b>$tLname</b>に落ちたので被害がありませんでした。",$tId);
}

# 通常ミサイル、怪獣に命中、ダメージ・殺傷 or 陸地破壊弾(LD)、山に命中
sub logMsMonster { #3
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行い、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>に命中。<b>$tLname</b>は$str",$id, $tId);
}

# ステルスミサイル、怪獣に命中、ダメージ・殺傷
sub logMsMonsterS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logSecret("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行い、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>に命中。<b>$tLname</b>は$str",$id);
	logLate("<b>何者か</b>が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行い、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>に命中。<b>$tLname</b>は$str",$tId);
}

# 陸地破壊弾(LD)、地形隆起弾(LR)、海底基地に命中
sub logMsLSbase { #3
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行い、${HtagName_}$tPoint${H_tagName}に着水後爆発、同地点にあった<b>$tLname</b>は$str",$id, $tId);
}

# 陸地破壊弾(LD)、地形隆起弾(LR)、怪獣に命中
sub logMsLMonster { #2
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行い、${HtagName_}$tPoint${H_tagName}に着弾し爆発。陸地は<b>$tLname</b>もろとも$str",$id, $tId);
}

# 陸地破壊弾(LD)地形隆起弾(LR)浅瀬・腐海・その他の地形に命中
sub logMsLOther { #7
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行い、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>に着弾。$str",$id, $tId);
}

# 核ミサイル、着弾
sub logMsSS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行い、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>に着弾し大爆発しました。",$id, $tId);
}

# 通常ミサイル通常地形・腐海・怪獣(硬化中)に命中
sub logMsNormal { #3
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行い、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>に命中、$str",$id, $tId);
}

# ステルスミサイル通常地形・腐海・怪獣(硬化中)に命中
sub logMsNormalS { #3
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logSecret("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行い、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>に命中、$str",$id);
	logLate("<b>何者か</b>が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行い、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>に命中、$str",$tId);
}

# 怪獣の死体
sub logMsMonMoney { #6
	my ($tId, $mName, $value) = @_;
	logOut("<b>$mName</b>の残骸には、<b>$value$HunitMoney</b>の値が付きました。",$tId);
}

# ミサイル難民到着
sub logMsBoatPeople { #1
	my ($id, $name, $achive) = @_;
	logOut("${HtagName_}${name}${H_tagName}にどこからともなく<b>$achive${HunitPop}もの難民</b>が漂着しました。${HtagName_}${name}${H_tagName}は快く受け入れたようです。",$id);
}

# ステルスミサイル、荒地に着弾
sub logMsWasteS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>に落ちました。",$id);
	logLate("<b>何者か</b>が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>に落ちました。",$tId);
}

# ステルスミサイル、怪獣にたたき落とされる
sub logMsMonsCautS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>にたたき落とされました。",$id);
}

# ステルスミサイル、天使にたたき落とされる
sub logMsMonsCauttS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>に打ち消されました。",$id);
}

# ステルスミサイル、スライムにたたき落とされる
sub logMsMonsCautlS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>に飲み込まれました。",$id);
}

# ステルスミサイル、メカにたたき落とされる
sub logMsMonsCautmS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>による迎撃ミサイルに撃ち落されました。",$id);
}

# 通常ミサイル、怪獣にたたき落とされる・荒地に着弾
sub logMsMonsCaut { #5
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$point${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、${HtagName_}$tPoint${H_tagName}の<b>$tLname</b>に$str",$id, $tId);
}

# 怪獣が攻撃する
sub logMonsAttack { #2
	my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>が$tPoint<b>$tName</b>に向かって炎を吐きつけました。",$id, $tId);
}

# 天使が攻撃する
sub logMonsAttackt { #1
	my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>が$tPoint<b>$tName</b>を攻撃しました。",$id, $tId);
}

# イレが攻撃する
sub logIreAttackt { #2
	my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}${H_tagName}の<b>$mName</b>が$tPoint<b>$tName</b>を攻撃し${HtagDisaster_}$point${H_tagDisaster}のダメージを与えました。",$id, $tId);
}

# 攻撃で首はね
sub logItiAttack { #1
	my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>が$tPoint<b>$tName</b>の首を刎ねました。",$id, $tId);
}

# 力場で怪獣あうち
sub logBariaAttack { #1
	my ($id, $name, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$tPoint${H_tagName}の<b>$tName</b>が強力な力場に押し潰されました。",$id, $tId);
}

# 魔法メテオ、クエイク
sub logMgSpel { #3
	my ($id, $name, $mName, $point, $spel) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>は${HtagDisaster_}$spel${H_tagDisaster}を唱えました。",$id);
}

# 魔法ドレイン
sub logMgDrain { #1
	my ($id, $name, $mName, $tName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>は<b>$tName</b>に対して${HtagDisaster_}ドレイン${H_tagDisaster}を唱えました。",$id);
}

# かみなりいのらのかみなり
sub logKaminariCall { #1
    my ($id, $name, $mName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>は<b>かみなり</b>を呼び起こしました。",$id);
}

# 召喚
sub logShoukan { #1
	my ($id, $name, $nName, $mName, $point) = @_;
	logOut("<b>$nName</b>は${HtagName_}${name}$point${H_tagName}に<b>$mName</b>を${HtagDisaster_}召喚${H_tagDisaster}しました。",$id);
}

# 大恐慌
sub logKyoukou { #1
	my ($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>は${HtagName_}${name}${H_tagName}に${HtagDisaster_}大恐慌${H_tagDisaster}をもたらしました。",$id);
}

# 腐食
sub logFushoku { #2
	my ($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>は${HtagName_}${name}${H_tagName}の蓄えていた<b>食料</b>を${HtagDisaster_}腐敗${H_tagDisaster}させてしまったようです。",$id);
}

# big迎撃？！
sub logEiseiBigcome { #0
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}の<b>迎撃衛星</b>は${HtagName_}${name}${H_tagName}に向かってくる${HtagDisaster_}巨大隕石${H_tagDisaster}を撃ち落としたようです！！",$id);
}

# 迎撃？！
sub logEiseicome { #0
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}の<b>迎撃衛星</b>は${HtagName_}${name}${H_tagName}に向かってくる${HtagDisaster_}隕石${H_tagDisaster}を撃ち落としたようです！！",$id);
}

# 衛星消滅？！
sub logEiseiEnd { #4
	my ($id, $name, $tEiseiname) = @_;
	logOut("${HtagName_}${name}${H_tagName}の<b>$tEiseiname</b>は${HtagDisaster_}崩壊${H_tagDisaster}したようです！！",$id);
}

# 封印解除
sub logUmlimit { #1
	my ($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>の<b>封印</b>が${HtagDisaster_}解除${H_tagDisaster}されてしまったようです。",$id);
}

# 封印解除被害
sub logUmlimitDamage { #1
	my ($id, $name, $mName, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>は<b>$mName</b>の${HtagDisaster_}解放されたエネルギー${H_tagDisaster}により壊滅しました。",$id);
}

# ウリエルのコメット〜
sub logUrieruMeteo { #1
	my ($id, $name, $lName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>が引き寄せた${HtagDisaster_}小隕石${H_tagDisaster}が${HtagName_}$tPoint${H_tagName}の<b>$tName</b>に落下し一帯が壊滅しました。",$id, $tId);
}

# 新型軍艦が攻撃する
sub logFuneAttack { #1
	my ($id, $name, $lName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>が多弾頭ミサイルを発射し、${HtagName_}$tPoint${H_tagName}の<b>$tName</b>に命中しました。",$id, $tId);
}

# メカの攻撃
sub logMekaAttack { #4
	my ($id, $name, $lName, $point, $tName, $tPoint, $kind, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>が発射した$kindが${HtagName_}$tPoint${H_tagName}の<b>$tName</b>に着弾し$strました。",$id, $tId);
}

# 腐海が生まれた
sub logRottenSeaBorn { #2
	my ($id, $name, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}に<b>王蟲</b>から<b>腐海</b>が生まれました。",$id);
}

# 脱皮してみた
sub logNuginugi { #1
	my ($id, $name, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}に<b>王蟲</b>が脱皮しました。",$id);
}

# きしんへい食べ物ログ
sub logKishinhei_down { #1
    my ($island , $point , $val) = @_;
    my ($name) = $island->{'name'} . $AfterName;
    my ($id) = $island->{'id'};

    logOut("${HtagName_}${name}$point${H_tagName}で倒れた<b>きしんへい</b>から${val}${HunitFood}のなぞ肉が出てきました。",$id);
}

# きしんへい食べ物ログ
sub logKishinhei_kyusyu { #1
    my ($island , $point , $val) = @_;
    my ($name) = $island->{'name'} . $AfterName;
    my ($id) = $island->{'id'};

    logOut("${HtagName_}${name}$point${H_tagName}の<b>きしんへい</b>が周辺の住民、<b>${val}${HunitPop}</b>を吸収しました。",$id);
}

# きしんへい食べ物ログ
sub logKishinhei_Kaihuku { #1
    my ($island , $point) = @_;
    my ($name) = $island->{'name'} . $AfterName;
    my ($id) = $island->{'id'};

    logOut("${HtagName_}${name}$point${H_tagName}の<b>きしんへい</b>が自動修復を行いました。",$id);
}

# レーザー命中、、
sub logLzr { #3
    my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
    logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$tPoint${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行い、<b>$tLname</b>に命中、<b>$tLname</b>は$str",$id, $tId);
}

# レーザー失敗
sub logLzrFail { #3
    my ($id, $tId, $name, $tName, $comName, $tPoint) = @_;
    logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}$tPoint${H_tagName}地点に向けて${HtagComName_}${comName}${H_tagComName}を行いましたが、防衛施設により守られました。",$id, $tId);
}

# 怪獣派遣
sub logMonsSend { #1
	my ($id, $tId, $name, $tName , $mName) = @_;
	logOut("${HtagName_}${name}${H_tagName}が<b>${mName}</b>を建造。${HtagName_}${tName}${H_tagName}へ送りこみました。",$id, $tId);
}

# 怪獣派遣 極秘
sub logSecretMonsSend { #1
	my ($id, $tId, $name, $tName , $mName) = @_;
	logSecret("${HtagName_}${name}${H_tagName}が<b>${mName}</b>を${HtagName_}${tName}${H_tagName}へ送りこみました。",$id, $tId);
}


# 別の同盟を結成している
sub logLeaderAlready {
	my ($id, $name, $tName, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}で予定されていた${HtagName_}${tName}${H_tagName}の${HtagComName_}${comName}${H_tagComName}は、すでに自分の同盟を結成しているため中止されました。",$id);
}

# 別の同盟に加盟している
sub logOtherAlready {
	my ($id, $name, $tName, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}で予定されていた${HtagName_}${tName}${H_tagName}の${HtagComName_}${comName}${H_tagComName}は、すでに別の同盟に加盟しているため中止されました。",$id);
}

# 加盟
sub logAlly {
	my ($id, $tId, $name, $allyName) = @_;
	logOut("${HtagName_}${name}${H_tagName}が『${HtagName_}${allyName}${H_tagName}』に${HtagNumber_}加盟${H_tagNumber}しました。", $id, $tId);
}

# 脱退
sub logAllyEnd {
	my ($id, $tId, $name, $allyName) = @_;
	logOut("${HtagName_}${name}${H_tagName}が『${HtagName_}${allyName}${H_tagName}』から${HtagDisaster_}脱退${H_tagDisaster}しました。", $id, $tId);
}

# 輸出
sub logSell { #1
	my ($id, $name, $comName, $value) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagFood_}$value$HunitFood${H_tagFood}の${HtagComName_}${comName}${H_tagComName}を行いました。",$id);
}

# 援助
sub logAid { #1
	my ($id, $tId, $name, $tName, $comName, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}が${HtagName_}${tName}${H_tagName}へ$strの${HtagComName_}${comName}${H_tagComName}を行いました。",$id, $tId);
}

# 陣営外への援助（不許可）
sub logAidFail {
	my ($id, $tId, $name, $tName, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}で予定されていた${HtagName_}${tName}${H_tagName}への${HtagComName_}${comName}${H_tagComName}は許可されていないため中止しました。",$id, $tId);
}

# 攻撃禁止
sub logNotAvail {
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}で予定されていた${HtagComName_}${comName}${H_tagComName}は許可されていないため中止しました。",$id);
}

# 誘致活動、資金繰り(コメントアウトしてます)
sub logPropaganda { #4
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}で${HtagComName_}${comName}${H_tagComName}が行われました。",$id);
}

# 放棄
sub logGiveup { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}は放棄され、<b>無人${AfterName}</b>になりました。",$id);
	logHistory("${HtagName_}${name}${H_tagName}、放棄され<b>無人${AfterName}</b>となる。");
}

# 時の記憶、時の忘却
sub logSaveLoad { #5
	my ($id, $name, $comName, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}が、${HtagComName_}${comName}${H_tagComName}$str",$id);
}

# 時の記憶、時の忘却、失敗
sub logSaveLoadFail { #3
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}が、${HtagComName_}${comName}${H_tagComName}",$id);
}

# 時の記憶データ消失
sub logSaveLoadVanish { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}で、時の侍者がごたごたを起こし${HtagDisaster_}時の記憶を消し去りました。${H_tagDisaster}",$id);
}

# バトルフィールドスコア換金
sub logBF_SCORE { #1
	my ($id, $name ,$score) = @_;
    my ($va);
    $va = $score * $HBF_Point_Value;
	logOut("<b>バトルフィールド</b>から${HtagName_}${name}${H_tagName}へ、<b>${va}${HunitMoney}</b>の賞金が贈られました。",$id);
}

# 死滅
sub logDead { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}から人がいなくなり、<b>無人${AfterName}</b>になりました。",$id);
	logHistory("${HtagName_}${name}${H_tagName}、人がいなくなり<b>無人${AfterName}</b>となる。");
}

# 死滅(サバイバルモード)
sub logTDead { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}は、<b>沈没</b>し跡形もなくなりました。",$id);
	logHistory("${HtagName_}${name}${H_tagName}、<b>沈没</b>する。");
}

# 飢餓
sub logStarve { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}の${HtagDisaster_}食料が不足${H_tagDisaster}しています！！",$id);
}

# 副作用？！
sub logStarvefood { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}の<b>遺伝子組換え食物</b>に${HtagDisaster_}副作用${H_tagDisaster}があったようです！！",$id);
}

# 胞子？！
sub logRotsick { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}の<b>腐海</b>が生み出した<b>胞子</b>は${HtagName_}${name}${H_tagName}に${HtagDisaster_}疫病${H_tagDisaster}をもたらしたようです！！",$id);
}

# 疫病？！
sub logSatansick { #1
	my ($id, $name) = @_;
	logOut("<b>魔王サタン</b>は${HtagName_}${name}${H_tagName}の<b>食料</b>を${HtagDisaster_}腐敗${H_tagDisaster}させ、${HtagName_}${name}${H_tagName}では${HtagDisaster_}疫病${H_tagDisaster}が流行っているようです！！",$id);
}

# 怪獣現る
sub logMonsCome { #3
	my ($id, $name, $mName, $point, $lName) = @_;
	logOut("${HtagName_}${name}${H_tagName}に<b>$mName</b>出現！！${HtagName_}$point${H_tagName}の<b>$lName</b>が踏み荒らされました。",$id);
}

# 怪獣放つ
sub logMonsFree { #1
	my ($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}で<b>$mName</b>を購入・放置しました。",$id);
}

# 怪獣動く
sub logMonsMove { #1
	my ($id, $name, $lName, $point, $mName , $msg) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>が<b>$mName</b>$msg",$id);
}

# 怪獣、防衛施設を踏む
sub logMonsMoveDefence { #1
	my ($id, $name, $lName, $point, $mName) = @_;
	logOut("<b>$mName</b>が${HtagName_}${name}$point${H_tagName}の<b>$lName</b>へ到達、<b>${lName}の自爆装置が作動！！</b>",$id);
}

# 怪獣ワープ
sub logMonsWarp { #1
	my ($id, $name, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>怪獣$mName</b>が消え去りました！",$id);
}

# 怪獣の周囲地形ワープ
sub logMonsWarpLand { #2
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}に<b>$lName</b>が出現しました！",$id);
}

# スライムが分裂した
sub lognewMonsterBorn { #1
	my ($id, $name, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}に<b>スライム</b>が分裂しました。",$id);
}

# 助け呼んだ
sub lognewKaiju { #1
	my ($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}に<b>$mName</b>が助けに来ました。",$id);
}

# 怪獣、自爆です
sub logMonsBomb { #1
	my ($id, $name, $lName, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>が${HtagDisaster_}メルトダウン${H_tagDisaster}を起こし自爆しました。",$id);
}

# 怪獣、仲間を呼ぶ
sub logMonsHelpMe { #1
	my ($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}${point}${H_tagName}の<b>怪獣$mName</b>が天に向かって咆哮しました！",$id);
}

# 怪獣が爆発する
sub logMonsExplosion { #1
	my ($id, $name, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>怪獣$mName</b>が<b>大爆発</b>を起こしました！",$id);
}

# 怪獣、周囲を焼き尽くす
sub logMonsFire { #1
	my ($id, $name, $lName, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>が<b>$mName</b>による衝撃波で壊滅しました。",$id);
}

# 怪獣、周囲を焼き尽くす
sub logMonsFireS { #1
	my ($id, $name, $lName, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>が<b>怪獣$mName</b>の吐き出した炎で焼き尽くされました。",$id);
}

# 怪獣、地雷を踏む
sub logMonsMine { #3
	my ($id, $name, $lName, $point, $mName, $str) = @_;
	logOut("<b>怪獣$mName</b>が${HtagName_}${name}$point${H_tagName}の<b>$lName</b>を踏んで爆発、<b>怪獣$mName</b>は$str",$id);
}

# 怪獣　お金を盗む
sub logMonsMoneyStole {
	my ($id, $name, $smoney, $mName) = @_;
	logOut("<b>怪獣$mName</b>が${HtagName_}${name}${H_tagName}から${HtagDisaster_}${smoney}${HunitMoney}${H_tagDisaster}を盗みました。",$id);
}

# 怪獣　お金を盗む
sub logMonsMoneyStoleMiss {
	my ($id, $name, $mName) = @_;
	logOut("<b>怪獣$mName</b>が${HtagName_}${name}${H_tagName}からお金を盗もうと試みましたが失敗したようです。",$id);
}

# 怪獣　食料を盗む
sub logMonsFoodStole {
	my ($id, $name, $sfood, $mName) = @_;
	logOut("<b>怪獣$mName</b>が${HtagName_}${name}${H_tagName}から食料${HtagDisaster_}${sfood}${HunitFood}${H_tagDisaster}を盗みました。",$id);
}

# 怪獣　食料を盗む
sub logMonsFoodStoleMiss {
	my ($id, $name, $mName) = @_;
	logOut("<b>怪獣$mName</b>が${HtagName_}${name}${H_tagName}から食料を盗もうと試みましたが失敗したようです。",$id);
}

# 火災
sub logFire { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>が${HtagDisaster_}火災${H_tagDisaster}により壊滅しました。",$id);
}

# 火災未遂
sub logFirenot { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>が${HtagDisaster_}火災${H_tagDisaster}により被害を受けました。",$id);
}

# 埋蔵金
sub logMaizo { #1
	my ($id, $name, $comName, $value) = @_;
	logOut("${HtagName_}${name}${H_tagName}での${HtagComName_}$comName${H_tagComName}中に、${HtagMoney_}$value$HunitMoney${H_tagMoney}もの<b>埋蔵金</b>が発見されました。",$id);
}

# 金塊
sub logGold { #1
	my ($id, $name, $comName, $value) = @_;
	logOut("${HtagName_}${name}${H_tagName}での${HtagComName_}$comName${H_tagComName}中に、<b>金塊</b>が発見され${HtagMoney_}$value$HunitMoney${H_tagMoney}の利益があがりました。",$id);
}

# 金枯渇
sub logGoldEnd { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>から金が採れなくなったようです。",$id);
}

# 地震発生
sub logEarthquake { #2
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}で大規模な${HtagDisaster_}地震${H_tagDisaster}が発生！！",$id);
}

# 食料不足被害
sub logSvDamage { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>に<b>食料を求めて住民が殺到</b>。<b>$lName</b>は壊滅しました。",$id);
}

# 津波発生
sub logTsunami { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}付近で${HtagDisaster_}津波${H_tagDisaster}発生！！",$id);
}

# 台風発生
sub logTyphoon { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}に${HtagDisaster_}台風${H_tagDisaster}上陸！！",$id);
}

# 隕石、落下
sub logMeteo { #10
    my ($id, $name, $lName, $point, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>に${HtagDisaster_}隕石${H_tagDisaster}が落下$strました。",$id);
}

# 隕石、落下 2
sub logMeteo2 {
    my ($id, $name, $lName, $point, $str , $metro) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>に${HtagDisaster_}${metro}${H_tagDisaster}が落下$strました。",$id);
}

# 隕石、落下
sub logMeteo_Safe {
    my ($island) = @_;

    my ($name) = islandName($island);
    my ($id) = $island->{'id'};

    logOut("${HtagName_}${name}${H_tagName}へ${HtagDisaster_}隕石${H_tagDisaster}が飛来してきましたが、迎撃衛星によって守られました。",$id);
}

# 隕石、落下 def
sub logMeteoDef {
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}に${HtagDisaster_}隕石${H_tagDisaster}が落下$strました。",$id);
}

# 隕石、怪獣
sub logMeteoMonster { #2
	my ($id, $name, $lName, $point) = @_;
	logOut("<b>$lName</b>がいた${HtagName_}${name}$point${H_tagName}地点に${HtagDisaster_}隕石${H_tagDisaster}が落下、陸地は<b>$lName</b>もろとも水没しました。",$id);
}

# 巨大隕石
sub logHugeMeteo { #2
	my ($id, $name, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}地点に${HtagDisaster_}巨大隕石${H_tagDisaster}が落下！！",$id);
}

# 噴火
sub logEruption { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}地点で${HtagDisaster_}火山が噴火${H_tagDisaster}、<b>山</b>が出来ました。",$id);
}

# 噴火２
sub logEruption2 { #3
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}地点の<b>$lName</b>は、${HtagDisaster_}噴火${H_tagDisaster}の影響で$str",$id);
}

# 地盤沈下発生
sub logFalldown { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}で${HtagDisaster_}地盤沈下${H_tagDisaster}が発生しました！！",$id);
}

# 広域被害、怪獣水没
sub logWideDamageMonsterSea { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}の陸地は<b>$lName</b>もろとも水没しました。",$id);
}

# 受賞
sub logPrize { #10
	my ($id, $name, $pName) = @_;
	logOut("${HtagName_}${name}${H_tagName}が<b>$pName</b>を受賞しました。",$id);
	logHistory("${HtagName_}${name}${H_tagName}、<b>$pName</b>を受賞");
}

# 失業者がデモ
sub logUnemployedDemo { #1
	my ($id, $name, $pop, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}で${str}<b>$pop${HunitPop}</b>がデモ行進を行いました。",$id);
}

# 失業者が暴動
sub logUnemployedRiot { #1
	my ($id, $name, $lName, $pop, $point, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}で${str}<b>$pop${HunitPop}</b>が${HtagDisaster_}暴動${H_tagDisaster}を起こして${HtagName_}$point${H_tagName}地点の<b>$lName</b>に<b>殺到</b>。<b>$lName</b>は壊滅しました。",$id);
}

# 失業者が移民
sub logUnemployedMigrate { #1
	my ($id, $tId, $name, $tName, $pop, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}から${HtagName_}${tName}${H_tagName}へ${str}<b>$pop${HunitPop}</b>の移民が到着しました。${HtagName_}${tName}${H_tagName}は快く受け入れたようです。",$id, $tId);
}

# 移民いやーん
sub logUnemployedReturn { #1
	my ($id, $tId, $name, $lName, $tName, $pop, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}から${HtagName_}${tName}${H_tagName}へ${str}<b>$pop${HunitPop}</b>の移民が到着しましたが、${HtagName_}${tName}${H_tagName}の<b>$lName</b>は受け入れを拒否したようです。",$id, $tId);
}

# 人口減少
sub logPopDecrease { #5
    my ($id, $name, $lName, $tName, $str, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>が${HtagDisaster_}${str}${H_tagDisaster}による人口減少で<b>$tName</b>になりました。",$id);
}

# 新しい町ができた
sub logPlains2Town {
    my ($island, $lName, $point) = @_;

    my ($id) = $island->{'id'};
    #require './hako-io.cgi';
    my ($name) = islandName($island);

    logOut("${HtagName_}${name}$point${H_tagName}の<b>平地</b>に新しい<b>${lName}</b>ができました。",$id);
}

# 島役所が予定地
sub logYakusho_Plains2 {
    my ($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>を島役所が<b>予定地</b>にしました。",$id);
}

# 島役所がちならし
sub logYakusho_Prepare {
    my ($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>を島役所が<b>平地</b>にしました。",$id);
}

# スパイダーマン
sub logSpiderMan {
    my ($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>${lName}</b>に<b>スパイダーマン男</b>が現れ、ビルの屋上で身柄を確保される事件がありました。",$id);
}

# 怪獣の拒否による失敗
sub logBokuFail2 {
    my ($id, $name, $comName, $kind, $point) = @_;
    logOut("${HtagName_}${name}${H_tagName}で予定されていた${HtagComName_}$comName${H_tagComName}は、予定地${HtagName_}$point${H_tagName}の<b>$kind</b>が嫌々をしたため中止されました。",$id);
}

# 釣り
sub logFishing {
    my ($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>${lName}</b>では、釣り名人が大物を釣り上げたニュースで持ちきりです。",$id);
}

# 引っ越し失敗
sub logHikkosi_miss {
    my ($id, $name) = @_;
    my ($comName);
    $comName = $HcomName[$HcomBoku2];
    logOut("${HtagName_}${name}${H_tagName}で予定されていた<b>${comName}</b>は、目的地が適さないため、失敗しました。",$id);
}

# カンストフード
sub logFoodsute {
    my ($id, $name, $fd , $money) = @_;
    #○○島の持ちきれなくなった食料Xトンは、Y億円に換金されました。
    logSecret("${HtagName_}${name}${H_tagName}の持ちきれなくなった食料${HtagFood_}${fd}${HunitFood}${H_tagFood}は${HtagMoney_}${money}${HunitMoney}${H_tagMoney}に換金されました。",$id);
}

# フード
sub logGiveFoodUpdate {
    my ($id, $sta, $update ) = @_;
    #○○島の持ちきれなくなった食料Xトンは、Y億円に換金されました。
    logOut("<b>$sta</b>が、$updateにアップした！",$id);
}

# アイテムを捨てる
sub logItemThrow {
    my ($id, $name, $iName) = @_;
    logSecret("${HtagName_}${name}${H_tagName}は<b>${iName}</b>を捨てました。",$id);
}

# アイテムおく。
sub logItemPuton {
    my ($id, $name,$point, $iName ) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}に<b>${iName}</b>を置きました。",$id);
}

# アイテムがない
sub logItemisNoting {
    my ($id, $name) = @_;
    logOut("${HtagName_}${name}${H_tagName}は持ってないアイテムを使おうとしました。",$id);
}

# アイテムがおけない
sub logItemDeny {
    my ($id, $name, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}がアイテムを置くのに適さないため、失敗しました。",$id);
}

# スケート場しずむ
sub logSkateDown {
    my ($island, $landname, $x, $y) = @_;
    my ($point) = "($x,$y)";
    my ($id) = $island->{'id'};
    my ($name) = islandName($island);
    logOut("${HtagName_}${name}$point${H_tagName}の<b>${landname}</b>は、氷がとけてなくなりました。",$id);
}

# 焼き溶岩
sub logLavaAttack {
    my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$mName</b>の呼び起こした${HtagDisaster_}溶岩${H_tagDisaster}は${HtagName_}$tPoint${H_tagName}の<b>$tName</b>を焼きました。",$id, $tId);
}

# 召喚
sub logNige {
    my ($id, $name, $lName, $mName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>動物園</b>から<b>$mName</b>が${HtagDisaster_}脱走${H_tagDisaster}しました。",$id);
}

# 怪獣仕入れ
sub logSiire {
    my ($id, $name, $lName, $mName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>は<b>$mName</b>を入荷し話題をよんでいます。",$id);
END
}

# 油田からの収入
sub logOilMoney2 {
    my ($id, $name, $lName, $point, $str, $str2) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>$lName</b>から、${HtagMoney_}$str${H_tagMoney}の収益が上がりました。(食料${HtagFood_}$str2${H_tagFood}消費)",$id);
END
}

# 召喚
sub logNige2 {
    my ($id, $name, $lName, $mName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}の<b>動物園</b>から<b>$mName</b>を${HtagDisaster_}脱走${H_tagDisaster}させました。",$id);
}

1;
