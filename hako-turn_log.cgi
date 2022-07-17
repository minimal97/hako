#----------------------------------------------------------------------
# Ȣ����� ver2.30
# ������ʹԥ⥸�塼��(ver1.02)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Hakoniwa R.A. ver1.11
# �ᥤ�󥹥���ץ�(Ȣ����� ver2.30)
# ���Ѿ�������ˡ���ϡ�read-renas.txt�ե�����򻲾�
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------
# �ե����뤬�礭���Τǡ����ƥ�ץ졼�Ȥ���ʬ��
# turn�ǥ��󥯥롼�ɤ��뤳�ȡ�

#----------------------------------------------------------------------
# ���ƥ�ץ졼��
#----------------------------------------------------------------------
# ����ʪ��Ĵã ̤����
sub logArmSupply {
	my ($id, $name, $comName, $num) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagNumber_}$num��${H_tagNumber}��${HtagComName_}$comName${H_tagComName}��Ԥ��ޤ�����",$id);
}

# ���ԤǤ���
sub logShuto {
    my ($id, $name, $lName, $sName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>�ϡ�<b>����$sName</b>�Ȥ���${AfterName}���濴Ū�ԻԤؤȤʤ�ޤ�����",$id);
    logHistory("${HtagName_}${name}${H_tagName}��<b>����$sName</b>������ޤ�����");
}

# ����ȯ��
sub logHotFound {
    my ($id, $name, $point, $comName, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$str</b>��ͽ����Ĥ������${HtagComName_}${comName}${H_tagComName}���Ԥ�졢<b>�������������Ƥ��ޤ���</b>��",$id);
}

# ����ȯ���ʤ餺
sub logHotFail {
    my ($id, $name, $point, $comName, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$str</b>��ͽ����Ĥ������${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ������������ϸ��Ĥ���ޤ���Ǥ�����",$id);
}

# ���¤���μ���
sub logSinMoney {
    my ($id, $name, $str) = @_;
    logSecret("${HtagName_}${name}$point${H_tagName}��<b>����</b>�ǽˤ��κפ꤬�Ԥ�졢<b>$str</b>�μ��פ��夬��ޤ�����",$id);
}

# ���Ҥ���μ���
sub logJinMoney {
    my ($id, $name, $str) = @_;
    logSecret("${HtagName_}${name}$point${H_tagName}��<b>����</b>�ǽˤ��κפ꤬�Ԥ�졢<b>$str</b>�μ��פ��夬��ޤ�����",$id);
}

# ����⤫��μ���
sub logEnjo {
    my ($id, $name, $lName, $point, $str) = @_;
    logOut("��ȯ�ʹ԰Ѱ��񤫤�${HtagName_}${name}${H_tagName}��<b>$str</b>�α���⤬�ٵ뤵�줿�褦�Ǥ���",$id);
}

# �ߥ�����ޤȤ��
sub logMsTotal {
    my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $count, $mukou, $bouei, $kaijumukou, $kaijuhit, $fuhatu) = @_;
    logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}$countȯ��${comName}${H_tagComName}��Ԥ��ޤ�����<br>������${HtagName_}���${H_tagName}��(̵��$mukouȯ/�ɱ�$boueiȯ/�����껦$kaijumukouȯ/����̿��$kaijuhitȯ/��ȯ��$fuhatuȯ)",$id, $tId);
}

# ���ƥ륹�ߥ�����ޤȤ��
sub logMsTotalS {
    my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $count, $mukou, $bouei, $kaijumukou, $kaijuhit, $fuhatu) = @_;
    logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}$countȯ��${comName}${H_tagComName}��Ԥ��ޤ�����<br>������${HtagName_}���${H_tagName}��(̵��$mukouȯ/�ɱ�$boueiȯ/�����껦$kaijumukouȯ/����̿��$kaijuhitȯ/��ȯ��$fuhatuȯ)",$id);
    logLate("<b>���Ԥ�</b>��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}$countȯ��${comName}${H_tagComName}��Ԥ��ޤ�����<br>������${HtagName_}���${H_tagName}��(̵��$mukouȯ/�ɱ�$boueiȯ/�����껦$kaijumukouȯ/����̿��$kaijuhitȯ)", $tId);
}

# ���Ԥ򹶷⤹��
sub logMonsAttacks {
    my ($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>�ϲ��ä�${HtagDisaster_}����${H_tagDisaster}�����ﳲ������ޤ�����",$id);
}

# ���Ԥ򹶷⤹��
sub logMonsAttacksSecret {
    my ($id, $name, $lName, $point) = @_;
    logSecret("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>�ϲ��ä�${HtagDisaster_}����${H_tagDisaster}�����ﳲ������ޤ�����",$id);
}

# ��⡦����������­��ʤ������Ĥ���ʤ�
sub logNoAny { #20
	my ($id, $name, $comName, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}$comName${H_tagComName}�ϡ�$str������ߤ���ޤ�����",$id);
}

# �ޥ����åȤ����⤹��
sub logMsAttackt {
    my ($id, $name, $mName, $point, $cPoint, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}${H_tagName}��<b>$mName</b>��$tPoint<b>$tName</b>�򹶷⤷${HtagDisaster_}$point${H_tagDisaster}�Υ��᡼����Ϳ��${HtagDisaster_}$cPoint${H_tagDisaster}�Υ��᡼��������ޤ�����",$id, $tId);
}

# �ߥ�����������
sub logMsAttackmika {
    my ($id, $name, $mName, $point, $cPoint, $tName) = @_;
    logOut("${HtagName_}${name}${H_tagName}��<b>$mName</b>��<b>$tName</b>���襤������Ȥʤꡢ${AfterName}̱��<b>��ʡ�ν�����</b>���¤���ޤ�����",$id, $tId);
}

# ����Ǽ�Ϥ�
sub logItiAttackms {
    my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>��$tPoint<b>$tName</b>��¤�Ĥ��ޤ�����",$id, $tId);
}


# ɹ�Ƕ��ɤ�
sub logIceAttack {
    my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>��ȯ����ɹ�����${HtagName_}$tPoint${H_tagName}��<b>$tName</b>���濴��Ӥ��ޤ�����",$id, $tId);
}

# �Ƥ�
sub logFireAttack {
    my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>�θƤӵ�������${HtagDisaster_}��${H_tagDisaster}��${HtagName_}$tPoint${H_tagName}��<b>$tName</b>��Ƥ��ޤ�����",$id, $tId);
}

# �إ�ե�����
sub logHellAttack {
    my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>�θƤӵ�������${HtagDisaster_}�Ϲ��α�${H_tagDisaster}��${HtagName_}$tPoint${H_tagName}��<b>$tName</b>��Ƥ��Ԥ����ޤ�����",$id, $tId);
}

# �������Ϥ����⤹��
sub logFuneAttackSSS {
    my ($id, $name, $lName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��<b>���ͥ륮��ˤ</b>��ȯ�ͤ���<b>$tName</b>��̿�椷�ޤ�����",$id, $tId);
}

# �������Ϥ����⤹��
sub logFuneAttackSSSR {
    my ($id, $name, $lName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}${H_tagName}��<b>$tName</b>��<b>�ڤ�ü����</b>�ˤʤ�ޤ�����",$id, $tId);
}

# �������Ϥ����⤹��
sub logFuneAttackSSST {
    my ($id, $name, $lName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}${H_tagName}��<b>$tName</b>��<b>�ڤ�ü����</b>�ˤʤꡢ<b>$lName</b>��${HtagDisaster_}�����С��ҡ���${H_tagDisaster}�ˤ��${HtagDisaster_}����ȯ${H_tagDisaster}���ޤ�����",$id, $tId);
}

# ���۲�
sub logEggBomb {
	my ($id, $name, $lName, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>����<b>$mName</b>���и����ޤ�����",$id);
}

# �����ﳲ
sub logEggDamage {
	my ($id, $name, $landName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$landName</b>��${HtagDisaster_}��������ˤ�륨�ͥ륮��${H_tagDisaster}�ˤ����פ��ޤ�����",$id);
}

# ���Τ�з�
sub logMstakeon {
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��<b>�����༣</b>�˸������ޤ�����",$id);
}

# ���Τ鵢��
sub logMstakeokaeri {
	my ($id, $name, $lName, $point, $tName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<b>$lName</b>��${HtagName_}$point${H_tagName}��<b>$tName</b>�˵��äƤ��ޤ��������Ĥ��줵�ޡ�",$id);
}

# ���Τ�Ƚ�
sub logMstakeiede {
	my ($id, $name, $lName, $point, $tName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<b>$lName</b>�ϵ���٤��Ȥ��ʤ������ι�˽Фޤ�����",$id);
}

# ���Τ��������
sub logMstakeoff {
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��<b>�ޥ����åȲ���</b>»���Τ��᱿�ĺ���ˤʤ�ޤ�����",$id);
}

# ���Τ�Ƚ�
sub logHimeKaeru {
	my ($id, $name, $lName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<b>$lName</b>�ϡ����Ф���줿�Τǵ���ޤ�����",$id);
}

# ���ǵե���
sub logKire {
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<b>����</b>��${AfterName}̱��${HtagDisaster_}����${H_tagDisaster}�ޤ�������",$id);
}

# �����ﳲ
sub logKireDamage {
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��${HtagDisaster_}˽���${AfterName}̱${H_tagDisaster}�ˤ�ä�${HtagDisaster_}�˲�${H_tagDisaster}����ޤ�����",$id);
}

# �����ﳲ
sub logZeikin_fuman {
    my ($id, $name) = @_;
    logOut("${HtagName_}${name}${H_tagName}�ν�̱�ϡ�<b>�Ƕ���Ф��ơ��ڤ�ΤƤ����⤬¿�����Ȥˡ�����</b>�򴶤��Ƥ��ޤ���",$id);
}

# ���ø���(������)
sub logMonsComemagic {
	my ($id, $name, $mName, $point, $lName) = @_;
	logOut("${HtagName_}${name}${H_tagName}���˲����줿<b>������</b>����<b>$mName</b>�и�����",$id);
}

# ���á����Ϥ���ƿԤ���
sub logMonsCold {
	my ($id, $name, $lName, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��<b>$mName</b>���괬���䵤�ˤ����ƤĤ��ޤ�����",$id);
}

# ��
sub logEggFound {
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}�Ǥ�${HtagComName_}$comName${H_tagComName}��ˡ�<b>��������</b>��ȯ������${HtagComName_}$comName�ȼ�${H_tagComName}�ˤ��˲���̵���ʤΤ����֤��뤳�Ȥˤ��ޤ�����",$id);
}

# ����
sub logIsekiFound {
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}�Ǥ�${HtagComName_}$comName${H_tagComName}��ˡ�<b>�������</b>��ȯ������<b>${AfterName}�ν�����¢ʸ����</b>�˻��ꤵ��ޤ�����",$id);
}

# ����
sub logPrizet {
	my ($id, $name, $pName, $value) = @_;
	my ($str) = "(�޶�${HtagMoney_}$value${H_tagMoney})" if($value > 0);
	logOut("${HtagName_}${name}${H_tagName}��<b>$pName</b>����ޤ��ޤ�����$str",$id);
	logHistory("${HtagName_}${name}${H_tagName}��<b>$pName</b>�����$str");
}

# Ȣ���å�
sub logHC {
	my ($id, $name, $stsanka) = @_;
	if ($stsanka) {
#	logHistory("${HtagName_}Hakoniwa Cup $HislandTurn${H_tagName}���š�<b>���ÿ�</b>${HtagNumber_}$stsanka${AfterName}��${H_tagNumber}");
		logHcup("${HtagName_}Hakoniwa Cup $HislandTurn${H_tagName}���š�<b>���ÿ�</b>${HtagNumber_}$stsanka${AfterName}��${H_tagNumber}");
	}
    else {
		logHcup("${HtagName_}Hakoniwa Cup $HislandTurn${H_tagName}�ϡ����ä���${AfterName}���ʤ��ä�����${HtagNumber_}��ߤˤʤ�ޤ�����${H_tagNumber}");
	}
}

# Ȣ���å׳���
sub logHCstart {
	my ($id, $name, $str) = @_;
#   logHistory("${HtagName_}${name}${H_tagName}��<b>Hakoniwa Cup ����</b>���Ԥʤ�졢${HtagMoney_}$str${H_tagMoney}�ηкѸ��̤򴬤��������ޤ�����",$id);
	logLate("${HtagName_}${name}${H_tagName}��<b>Hakoniwa Cup ����</b>���Ԥʤ�졢${HtagMoney_}$str${H_tagMoney}�ηкѸ��̤򴬤��������ޤ�����",$id);
	logHcup("${HtagName_}${name}${H_tagName}��<b>Hakoniwa Cup ����</b>���Ԥʤ�졢${HtagMoney_}$str${H_tagMoney}�ηкѸ��̤򴬤��������ޤ�����");
}

# Ȣ���å׻��
sub logHCgame {
	my ($id, $tId, $name, $tName, $lName, $gName, $goal, $tgoal, $Teamname, $tTeamname) = @_;
	my ($tena, $ttena);
	my ($home, $away);

    $tena = "";
    $tena = "(${Teamname})" if ( length($Teamname) > 0);
    $ttena = "";
    $ttena = "(${tTeamname})" if ( length($tTeamname) > 0);

	if ($goal < $tgoal) {
		$str = "${HtagLose_}${name}��ɽ${tena}${H_tagLose}<b>VS</b>${HtagWin_}${tName}��ɽ${ttena}${H_tagWin} �� ${HtagLose_}$goal${H_tagLose}<b>��</b>${HtagWin_}$tgoal${H_tagWin}";
	}
    else {
		$str = "${HtagWin_}${name}��ɽ${tena}${H_tagWin}<b>VS</b>${HtagLose_}${tName}��ɽ${ttena}${H_tagLose} �� ${HtagWin_}$goal${H_tagWin}<b>��</b>${HtagLose_}$tgoal${H_tagLose}";
	}
	logLate("${HtagName_}${name}${H_tagName}��<b>Hakoniwa Cup $gName</b>���Ԥ��ޤ�����$str",$id, $tId);
	logHcup("${HtagName_}Hakoniwa Cup ${gName}${H_tagName}��$str");
}

# Ȣ���å׾���
sub logHCwin {
	my ($id, $name, $cName, $str) = @_;
	logLate("${HtagName_}${name}��ɽ${H_tagName}��<b>$cName</b>��${HtagName_}${name}${H_tagName}��${HtagMoney_}$str${H_tagMoney}�ηкѸ��̤򴬤��������ޤ�����",$id);
}

# Ȣ���å�ͥ��
sub logHCwintop {
	my ($id, $name, $cName) = @_;
#   logHistory("${HtagName_}${name}��ɽ${H_tagName}��${HtagWin_}Hakoniwa Cup $cNameͥ����${H_tagWin}",$id);
	logLate("${HtagWin_}${name}��ɽ${H_tagWin}��${HtagName_}Hakoniwa Cup $cName${H_tagName}${HtagWin_}ͥ����${H_tagWin}",$id);
	logHcup("${HtagWin_}${name}��ɽ${H_tagWin}��${HtagName_}Hakoniwa Cup $cName${H_tagName}${HtagWin_}ͥ����${H_tagWin}");
}

# Ȣ���å����ﾡ
sub logHCantiwin {
	my ($id, $name, $gName) = @_;
	logLate("${HtagName_}Hakoniwa Cup ${gName}${H_tagName}��${HtagWin_}${name}��ɽ${H_tagWin}�ϡ���������ब���ʤ�����${HtagWin_}���ﾡ${H_tagWin}�Ȥʤ�ޤ�����",$id);
	logHcup("${HtagName_}Hakoniwa Cup ${gName}${H_tagName}��${HtagWin_}${name}��ɽ${H_tagWin}�ϡ���������ब���ʤ�����${HtagWin_}���ﾡ${H_tagWin}��");
}

# Ȣ���å�
sub logHCsin {
	my ($id, $name, $stsin) = @_;
#   logHistory("${HtagName_}Hakoniwa Cup �辡�ȡ��ʥ��ȿʽ�${AfterName}!!${H_tagName}<br><font size=\"-1\"><b>$stsin</b></font>");
	logHcup("${HtagName_}Hakoniwa Cup �辡�ȡ��ʥ��ȿʽ�${AfterName}!!${H_tagName}<br><font size=\"-1\"><b>$stsin</b></font>");
}

# �Ѹ����꤬�Ȥ��������ޤ�
sub logKankouMigrate {
	my ($id, $tId, $name, $lName, $tName, $point, $pop) = @_;
	logOut("${HtagName_}${tName}${H_tagName}����${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��<b>$pop${HunitPop}</b>�δѸ��Ԥ���Ƥ���ޤ��������꤬�Ȥ��������ޤ���",$id, $tId);
}

# �ߥ������Ȥ��Ȥ��������Ϥ��ʤ�
sub logMsNoBase { #1
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}${comName}${H_tagComName}�ϡ�<b>�ߥ�������������ͭ���Ƥ��ʤ�</b>����˼¹ԤǤ��ޤ���Ǥ�����",$id);
}

# �о��Ϸ��μ���ˤ�뼺��
sub logLandFail { #14
    my ($id, $name, $comName, $kind, $point) = @_;
    logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}$comName${H_tagComName}�ϡ�ͽ���Ϥ�${HtagName_}$point${H_tagName}��<b>$kind</b>���ä�������ߤ���ޤ�����",$id);
}

# �о��Ϸ��μ���ˤ�뼺�ԣ�
sub logLandFail2 { #5
	my ($id, $name, $comName, $point, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}$comName${H_tagComName}�ϡ�ͽ���Ϥ�${HtagName_}$point${H_tagName}��$str������ߤ���ޤ�����",$id);
}

# Į������
sub logTownDel { #25
    my ($id, $name, $tName , $comName, $point, $lv) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>${tName}</b>��${HtagComName_}${comName}${H_tagComName}��Ԥä����ᡢ<b>${lv}${HunitPop}</b>��Ω�����ޤ�����",$id);
}

# Į������
sub logSouon { #25
    my ($id, $name, $point, $tName, $lv) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>${tName}</b>���������Ѥ��ڤ줺�����Ϥν�̱<b>${lv}${HunitPop}</b>��Ω�����ޤ�����",$id);
}

# ���Ϸ�����
sub logLandSuc { #25
	my ($id, $name, $comName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ�����",$id);
}

# ���Ϸϥ��ޤȤ�
sub logLandSucMatome {
	my ($id, $name, $comName, $point) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ�����<br>����<b>��</b> $point",$id);
}

# ��������
sub logEiseifail { #1
	my ($id, $name, $comName, $point) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ������Ǥ��夲��${HtagDisaster_}����${H_tagDisaster}�����褦�Ǥ���",$id);
}

# ����ȯ��
sub logOilFound { #1
	my ($id, $name, $point, $comName, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��${HtagMoney_}$str${H_tagMoney}��ͽ����Ĥ������${HtagComName_}${comName}${H_tagComName}���Ԥ�졢<b>���Ĥ��������Ƥ��ޤ���</b>��",$id);
}

# ����ȯ��200
sub logOil200Found { #1
	my ($id, $name, $point, $comName, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��${HtagMoney_}$str${H_tagMoney}��ͽ����Ĥ������${HtagComName_}${comName}${H_tagComName}���Ԥ�졢<b>���Ĥ��������Ƥ��ޤ���</b>��<br>200�������Ĥ��꤬£���ޤ�����",$id);
}

# ����ȯ���ʤ餺
sub logOilFail { #1
	my ($id, $name, $point, $comName, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��${HtagMoney_}$str${H_tagMoney}��ͽ����Ĥ������${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ����������Ĥϸ��Ĥ���ޤ���Ǥ�����",$id);
}

# ���ġ��ؽꡦͷ���ϡ���������μ���
sub logOilMoney { #9
	my ($id, $name, $lName, $point, $value, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>���顢${HtagMoney_}$value${H_tagMoney}��$str���夬��ޤ�����",$id);
}

# ���ĸϳ顢�����ﳲ����¾
sub logDamageAny { #29
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��$str",$id);
}

# ͷ���ϤΥ��٥��
sub logParkEvent { #4
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>�ǥ��٥�Ȥ����Ť��졢${HtagFood_}$str${H_tagFood}�ο��������񤵤�ޤ�����",$id);
}

# �ݸ�����μ���
sub logHoken { #1
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>�λ��Τˤ�ꡢ${HtagMoney_}$str${H_tagMoney}���ݸ�������ޤ�����",$id);
}

# �ڻ�����μ���
sub logMiyage { #1
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName��ǰ�����</b>�Τ��ڻ������󤫤�${HtagMoney_}$str${H_tagMoney}�μ���������ޤ�����",$id);
}

# ͥ������μ���
sub logYusho { #1
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}�����������${HtagName_}$point${H_tagName}��<b>$lName</b>�ǹԤ�줿Ȣ��꡼���辡��Ǥߤ���ͥ������${HtagMoney_}$str${H_tagMoney}�ηкѸ��̤�������ޤ�����",$id);
}

# TITANIC�ǲ貽
sub logTitanicEnd { #1
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>�����פϱǲ貽���졢¿���οͤ��ޤ�ή���ޤ�����(${HtagMoney_}$str${H_tagMoney}�����׼���)",$id);
}

# ����õ������μ���
sub logTansaku { #1
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��������ȯ����${HtagMoney_}$str${H_tagMoney}�β��ͤ����뤳�Ȥ��狼��ޤ�����",$id);
	logHistory("${HtagName_}${name}${H_tagName}��<b>$lName</b>��������ȯ����");
}

# ����õ��������
sub logTansakuoil { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>�����Ĥ�ȯ����",$id);
}

# ����
sub logOilMoneyt { #1
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>����Ȥ���������${HtagMoney_}$str${H_tagMoney}���ͤ��դ��ޤ�����",$id);
}

# ������
sub logParkEventt { #2
    my ($id, $name, $lName, $point, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>���⤿�餷��˭��ˤ�ꡢ�����${HtagFood_}$str${H_tagFood}�ο���������ޤ�����",$id);
}

# �ϥ��ƥ���Ȥξ���
sub logFactoryHT { #2
    my ($id, $name, $lName, $str) = @_;
    logSecret("${HtagName_}${name}${H_tagName}��<b>$lName</b>�ϡ�${HtagMoney_}$str${H_tagMoney}����񤷤ޤ�����",$id);
}

# ���μ���
sub logParkEventf { #2
    my ($id, $name, $lName, $point, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>�ϡ�${HtagFood_}$str${H_tagFood}�ο��������ޤ�����",$id);
}

# �ɱһ��ߡ��������å�
#sub logBombSet { #1
#   my($id, $name, $lName, $point) = @_;
#   logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��<b>�������֤����å�</b>����ޤ�����",$id);
#}

# �ɱһ��ߡ�������ư
#sub logBombFire { #1
#   my($id, $name, $lName, $point) = @_;
#   logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��${HtagDisaster_}�������ֺ�ư����${H_tagDisaster}",$id);
#}

# ��ǰ�ꡢȯ��
sub logMonFly { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��<b>�첻�ȤȤ������Ω���ޤ���</b>��",$id);
}

# ��ǰ�ꡢ�
sub logMonDamage { #1
	my ($id, $name, $point) = @_;
	logOut("<b>�����ȤƤĤ�ʤ����</b>��${HtagName_}${name}$point${H_tagName}����������ޤ�������",$id);
}

# ����or�ߥ��������
sub logPBSuc { #3
	my ($id, $name, $comName, $point) = @_;
	logSecret("${HtagName_}${name}$point${H_tagName}��${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ�����",$id);
	logOut("������ʤ�����${HtagName_}${name}${H_tagName}��<b>��</b>���������褦�Ǥ���",$id);
}

# �ϥ�ܥ�
sub logHariSuc { #1
	my ($id, $name, $comName, $comName2, $point) = @_;
	logSecret("${HtagName_}${name}$point${H_tagName}��${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ�����",$id);
	logLandSuc($id, $name, $comName2, $point);
}

# ������˲��ä����ʤ�
sub logNoTarget {
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}$comName${H_tagComName}�ϡ�������˲��ä����ʤ�������ߤ���ޤ�����",$id);
}

# �ߥ������ä����ϰϳ�
sub logMsOut { #1
	my ($id, $tId, $name, $tName, $comName, $point) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������<b>�ΰ賰�γ�</b>����������ͤǤ���",$id, $tId);
}

# ���ƥ륹�ߥ������ä����ϰϳ�
sub logMsOutS { #1
	my ($id, $tId, $name, $tName, $comName, $point) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������<b>�ΰ賰�γ�</b>����������ͤǤ���",$id);
	logLate("<b>���Ԥ�</b>��${HtagName_}${tName}$point${H_tagName}�ظ�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������<b>�ΰ賰�γ�</b>����������ͤǤ���",$tId);
}

# �����˲�����
sub logEiseiAtts { #1
	my ($id, $tId, $name, $tName, $comName, $tEiseiname) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}${H_tagName}�˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���<b>$tEiseiname</b>��̿�档<b>$tEiseiname</b>���׷���ʤ��ä����Ӥޤ�����",$id, $tId);
}

# �����˲�����
sub logEiseiAttf { #1
	my ($id, $tId, $name, $tName, $comName, $tEiseiname) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}${H_tagName}��<b>$tEiseiname</b>�˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ����������ˤ�̿�椻������������ؤ����ӵ�äƤ��ޤ��ޤ�������",$id, $tId);
}

# �ߥ������ä����ɱһ��ߤǥ���å�
sub logMsCaught { #2
	my ($id, $tId, $name, $tName, $comName, $point, $tPoint) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��������ˤ��Ͼ��ª����졢<b>������ȯ</b>���ޤ�����",$id, $tId);
}

# ���ƥ륹�ߥ������ä����ɱһ��ߤǥ���å�
sub logMsCaughtS { #2
	my ($id, $tId, $name, $tName, $comName, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��������ˤ��Ͼ��ª����졢<b>������ȯ</b>���ޤ�����",$id);
	logLate("<b>���Ԥ�</b>��${HtagName_}${tName}$point${H_tagName}�ظ�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��������ˤ��Ͼ��ª����졢<b>������ȯ</b>���ޤ�����",$tId);
}

# �ߥ������ä����ɱұ����ǥ���å�(ST�Х�ޤ�)
sub logMsCaughtE { #1
	my ($id, $tId, $name, $tName, $comName, $point, $tPoint) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������<b>�ɱұ���</b>�˷����Ȥ���ޤ�����",$id, $tId);
}

# �ߥ������ä������̤ʤ�
sub logMsNoDamage { #3
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $flag) = @_;
	my ($noga) = '��';
	$noga = '��' if ($flag);
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}${noga}<b>$tLname</b>��������Τ��ﳲ������ޤ���Ǥ�����",$id, $tId);
}

# ���ƥ륹�ߥ������ä������̤ʤ�
sub logMsNoDamageS { #2
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $flag) = @_;
	my ($noga) = '��';
	$noga = '��' if ($flag);
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}${noga}<b>$tLname</b>��������Τ��ﳲ������ޤ���Ǥ�����",$id);
	logLate("<b>���Ԥ�</b>��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}${noga}<b>$tLname</b>��������Τ��ﳲ������ޤ���Ǥ�����",$tId);
}

# �̾�ߥ����롢���ä�̿�桢���᡼�������� or Φ���˲���(LD)������̿��
sub logMsMonster { #3
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>��̿�档<b>$tLname</b>��$str",$id, $tId);
}

# ���ƥ륹�ߥ����롢���ä�̿�桢���᡼��������
sub logMsMonsterS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>��̿�档<b>$tLname</b>��$str",$id);
	logLate("<b>���Ԥ�</b>��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>��̿�档<b>$tLname</b>��$str",$tId);
}

# Φ���˲���(LD)���Ϸ�δ����(LR)��������Ϥ�̿��
sub logMsLSbase { #3
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��������ȯ��Ʊ�����ˤ��ä�<b>$tLname</b>��$str",$id, $tId);
}

# Φ���˲���(LD)���Ϸ�δ����(LR)�����ä�̿��
sub logMsLMonster { #2
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}�����Ƥ���ȯ��Φ�Ϥ�<b>$tLname</b>���Ȥ�$str",$id, $tId);
}

# Φ���˲���(LD)�Ϸ�δ����(LR)�������峤������¾���Ϸ���̿��
sub logMsLOther { #7
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>�����ơ�$str",$id, $tId);
}

# �˥ߥ����롢����
sub logMsSS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>�����Ƥ�����ȯ���ޤ�����",$id, $tId);
}

# �̾�ߥ������̾��Ϸ����峤������(�Ų���)��̿��
sub logMsNormal { #3
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>��̿�桢$str",$id, $tId);
}

# ���ƥ륹�ߥ������̾��Ϸ����峤������(�Ų���)��̿��
sub logMsNormalS { #3
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>��̿�桢$str",$id);
	logLate("<b>���Ԥ�</b>��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>��̿�桢$str",$tId);
}

# ���äλ���
sub logMsMonMoney { #6
	my ($tId, $mName, $value) = @_;
	logOut("<b>$mName</b>�λĳ��ˤϡ�<b>$value$HunitMoney</b>���ͤ��դ��ޤ�����",$tId);
}

# �ߥ�������̱����
sub logMsBoatPeople { #1
	my ($id, $name, $achive) = @_;
	logOut("${HtagName_}${name}${H_tagName}�ˤɤ�����Ȥ�ʤ�<b>$achive${HunitPop}�����̱</b>��ɺ�夷�ޤ�����${HtagName_}${name}${H_tagName}�ϲ����������줿�褦�Ǥ���",$id);
}

# ���ƥ륹�ߥ����롢���Ϥ�����
sub logMsWasteS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>������ޤ�����",$id);
	logLate("<b>���Ԥ�</b>��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>������ޤ�����",$tId);
}

# ���ƥ륹�ߥ����롢���äˤ�������Ȥ����
sub logMsMonsCautS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>�ˤ�������Ȥ���ޤ�����",$id);
}

# ���ƥ륹�ߥ����롢ŷ�Ȥˤ�������Ȥ����
sub logMsMonsCauttS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>���Ǥ��ä���ޤ�����",$id);
}

# ���ƥ륹�ߥ����롢���饤��ˤ�������Ȥ����
sub logMsMonsCautlS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>�˰��߹��ޤ�ޤ�����",$id);
}

# ���ƥ륹�ߥ����롢�ᥫ�ˤ�������Ȥ����
sub logMsMonsCautmS { #1
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>�ˤ��޷�ߥ�����˷�����ޤ�����",$id);
}

# �̾�ߥ����롢���äˤ�������Ȥ���롦���Ϥ�����
sub logMsMonsCaut { #5
	my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<b>$tLname</b>��$str",$id, $tId);
}

# ���ä����⤹��
sub logMonsAttack { #2
	my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>��$tPoint<b>$tName</b>�˸����äƱ���Ǥ��Ĥ��ޤ�����",$id, $tId);
}

# ŷ�Ȥ����⤹��
sub logMonsAttackt { #1
	my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>��$tPoint<b>$tName</b>�򹶷⤷�ޤ�����",$id, $tId);
}

# ���줬���⤹��
sub logIreAttackt { #2
	my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<b>$mName</b>��$tPoint<b>$tName</b>�򹶷⤷${HtagDisaster_}$point${H_tagDisaster}�Υ��᡼����Ϳ���ޤ�����",$id, $tId);
}

# ����Ǽ�Ϥ�
sub logItiAttack { #1
	my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>��$tPoint<b>$tName</b>�μ����ͤޤ�����",$id, $tId);
}

# �Ͼ�ǲ��ä�����
sub logBariaAttack { #1
	my ($id, $name, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$tPoint${H_tagName}��<b>$tName</b>�����Ϥ��Ͼ�˲����٤���ޤ�����",$id, $tId);
}

# ��ˡ��ƥ�����������
sub logMgSpel { #3
	my ($id, $name, $mName, $point, $spel) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>��${HtagDisaster_}$spel${H_tagDisaster}�򾧤��ޤ�����",$id);
}

# ��ˡ�ɥ쥤��
sub logMgDrain { #1
	my ($id, $name, $mName, $tName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>��<b>$tName</b>���Ф���${HtagDisaster_}�ɥ쥤��${H_tagDisaster}�򾧤��ޤ�����",$id);
}

# ���ߤʤꤤ�Τ�Τ��ߤʤ�
sub logKaminariCall { #1
    my ($id, $name, $mName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>��<b>���ߤʤ�</b>��Ƥӵ������ޤ�����",$id);
}

# ����
sub logShoukan { #1
	my ($id, $name, $nName, $mName, $point) = @_;
	logOut("<b>$nName</b>��${HtagName_}${name}$point${H_tagName}��<b>$mName</b>��${HtagDisaster_}����${H_tagDisaster}���ޤ�����",$id);
}

# �網��
sub logKyoukou { #1
	my ($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>��${HtagName_}${name}${H_tagName}��${HtagDisaster_}�網��${H_tagDisaster}��⤿�餷�ޤ�����",$id);
}

# �忩
sub logFushoku { #2
	my ($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>��${HtagName_}${name}${H_tagName}���ߤ��Ƥ���<b>����</b>��${HtagDisaster_}����${H_tagDisaster}�����Ƥ��ޤä��褦�Ǥ���",$id);
}

# big�޷⡩��
sub logEiseiBigcome { #0
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<b>�޷����</b>��${HtagName_}${name}${H_tagName}�˸����äƤ���${HtagDisaster_}�������${H_tagDisaster}������Ȥ����褦�Ǥ�����",$id);
}

# �޷⡩��
sub logEiseicome { #0
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<b>�޷����</b>��${HtagName_}${name}${H_tagName}�˸����äƤ���${HtagDisaster_}���${H_tagDisaster}������Ȥ����褦�Ǥ�����",$id);
}

# �������ǡ���
sub logEiseiEnd { #4
	my ($id, $name, $tEiseiname) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<b>$tEiseiname</b>��${HtagDisaster_}����${H_tagDisaster}�����褦�Ǥ�����",$id);
}

# �������
sub logUmlimit { #1
	my ($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>��<b>����</b>��${HtagDisaster_}���${H_tagDisaster}����Ƥ��ޤä��褦�Ǥ���",$id);
}

# ��������ﳲ
sub logUmlimitDamage { #1
	my ($id, $name, $mName, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��<b>$mName</b>��${HtagDisaster_}�������줿���ͥ륮��${H_tagDisaster}�ˤ����Ǥ��ޤ�����",$id);
}

# ���ꥨ��Υ���åȡ�
sub logUrieruMeteo { #1
	my ($id, $name, $lName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>�������󤻤�${HtagDisaster_}�����${H_tagDisaster}��${HtagName_}$tPoint${H_tagName}��<b>$tName</b>��������Ӥ����Ǥ��ޤ�����",$id, $tId);
}

# �������Ϥ����⤹��
sub logFuneAttack { #1
	my ($id, $name, $lName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��¿��Ƭ�ߥ������ȯ�ͤ���${HtagName_}$tPoint${H_tagName}��<b>$tName</b>��̿�椷�ޤ�����",$id, $tId);
}

# �ᥫ�ι���
sub logMekaAttack { #4
	my ($id, $name, $lName, $point, $tName, $tPoint, $kind, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��ȯ�ͤ���$kind��${HtagName_}$tPoint${H_tagName}��<b>$tName</b>�����Ƥ�$str�ޤ�����",$id, $tId);
}

# �峤�����ޤ줿
sub logRottenSeaBorn { #2
	my ($id, $name, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>���</b>����<b>�峤</b>�����ޤ�ޤ�����",$id);
}

# æ�餷�Ƥߤ�
sub logNuginugi { #1
	my ($id, $name, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>���</b>��æ�餷�ޤ�����",$id);
}

# ������ؤ�����ʪ��
sub logKishinhei_down { #1
    my ($island , $point , $val) = @_;
    my ($name) = $island->{'name'} . $AfterName;
    my ($id) = $island->{'id'};

    logOut("${HtagName_}${name}$point${H_tagName}���ݤ줿<b>������ؤ�</b>����${val}${HunitFood}�Τʤ������ФƤ��ޤ�����",$id);
}

# ������ؤ�����ʪ��
sub logKishinhei_kyusyu { #1
    my ($island , $point , $val) = @_;
    my ($name) = $island->{'name'} . $AfterName;
    my ($id) = $island->{'id'};

    logOut("${HtagName_}${name}$point${H_tagName}��<b>������ؤ�</b>�����դν�̱��<b>${val}${HunitPop}</b>��ۼ����ޤ�����",$id);
}

# ������ؤ�����ʪ��
sub logKishinhei_Kaihuku { #1
    my ($island , $point) = @_;
    my ($name) = $island->{'name'} . $AfterName;
    my ($id) = $island->{'id'};

    logOut("${HtagName_}${name}$point${H_tagName}��<b>������ؤ�</b>����ư������Ԥ��ޤ�����",$id);
}

# �졼����̿�桢��
sub logLzr { #3
    my ($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
    logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$tPoint${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���<b>$tLname</b>��̿�桢<b>$tLname</b>��$str",$id, $tId);
}

# �졼��������
sub logLzrFail { #3
    my ($id, $tId, $name, $tName, $comName, $tPoint) = @_;
    logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$tPoint${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ��������ɱһ��ߤˤ�����ޤ�����",$id, $tId);
}

# �����ɸ�
sub logMonsSend { #1
	my ($id, $tId, $name, $tName , $mName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<b>${mName}</b>���¤��${HtagName_}${tName}${H_tagName}�����ꤳ�ߤޤ�����",$id, $tId);
}

# �����ɸ� ����
sub logSecretMonsSend { #1
	my ($id, $tId, $name, $tName , $mName) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��<b>${mName}</b>��${HtagName_}${tName}${H_tagName}�����ꤳ�ߤޤ�����",$id, $tId);
}


# �̤�Ʊ����������Ƥ���
sub logLeaderAlready {
	my ($id, $name, $tName, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagName_}${tName}${H_tagName}��${HtagComName_}${comName}${H_tagComName}�ϡ����Ǥ˼�ʬ��Ʊ����������Ƥ��뤿����ߤ���ޤ�����",$id);
}

# �̤�Ʊ���˲������Ƥ���
sub logOtherAlready {
	my ($id, $name, $tName, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagName_}${tName}${H_tagName}��${HtagComName_}${comName}${H_tagComName}�ϡ����Ǥ��̤�Ʊ���˲������Ƥ��뤿����ߤ���ޤ�����",$id);
}

# ����
sub logAlly {
	my ($id, $tId, $name, $allyName) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagName_}${allyName}${H_tagName}�٤�${HtagNumber_}����${H_tagNumber}���ޤ�����", $id, $tId);
}

# æ��
sub logAllyEnd {
	my ($id, $tId, $name, $allyName) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagName_}${allyName}${H_tagName}�٤���${HtagDisaster_}æ��${H_tagDisaster}���ޤ�����", $id, $tId);
}

# ͢��
sub logSell { #1
	my ($id, $name, $comName, $value) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagFood_}$value$HunitFood${H_tagFood}��${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�����",$id);
}

# ���
sub logAid { #1
	my ($id, $tId, $name, $tName, $comName, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}${H_tagName}��$str��${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�����",$id, $tId);
}

# �رĳ��ؤα�����Ե��ġ�
sub logAidFail {
	my ($id, $tId, $name, $tName, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagName_}${tName}${H_tagName}�ؤ�${HtagComName_}${comName}${H_tagComName}�ϵ��Ĥ���Ƥ��ʤ�������ߤ��ޤ�����",$id, $tId);
}

# ����ػ�
sub logNotAvail {
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}${comName}${H_tagComName}�ϵ��Ĥ���Ƥ��ʤ�������ߤ��ޤ�����",$id);
}

# Ͷ�׳�ư����ⷫ��(�����ȥ����Ȥ��Ƥޤ�)
sub logPropaganda { #4
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ�����",$id);
}

# ����
sub logGiveup { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}���������졢<b>̵��${AfterName}</b>�ˤʤ�ޤ�����",$id);
	logHistory("${HtagName_}${name}${H_tagName}����������<b>̵��${AfterName}</b>�Ȥʤ롣");
}

# ���ε���������˺��
sub logSaveLoad { #5
	my ($id, $name, $comName, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagComName_}${comName}${H_tagComName}$str",$id);
}

# ���ε���������˺�ѡ�����
sub logSaveLoadFail { #3
	my ($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagComName_}${comName}${H_tagComName}",$id);
}

# ���ε����ǡ����ü�
sub logSaveLoadVanish { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}�ǡ����λ��Ԥ����������򵯤���${HtagDisaster_}���ε�����ä����ޤ�����${H_tagDisaster}",$id);
}

# �Хȥ�ե�����ɥ���������
sub logBF_SCORE { #1
	my ($id, $name ,$score) = @_;
    my ($va);
    $va = $score * $HBF_Point_Value;
	logOut("<b>�Хȥ�ե������</b>����${HtagName_}${name}${H_tagName}�ء�<b>${va}${HunitMoney}</b>�ξ޶⤬£���ޤ�����",$id);
}

# ����
sub logDead { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}����ͤ����ʤ��ʤꡢ<b>̵��${AfterName}</b>�ˤʤ�ޤ�����",$id);
	logHistory("${HtagName_}${name}${H_tagName}���ͤ����ʤ��ʤ�<b>̵��${AfterName}</b>�Ȥʤ롣");
}

# ����(���Х��Х�⡼��)
sub logTDead { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}�ϡ�<b>����</b>���׷���ʤ��ʤ�ޤ�����",$id);
	logHistory("${HtagName_}${name}${H_tagName}��<b>����</b>���롣");
}

# ����
sub logStarve { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagDisaster_}��������­${H_tagDisaster}���Ƥ��ޤ�����",$id);
}

# �����ѡ���
sub logStarvefood { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<b>�������ȴ�����ʪ</b>��${HtagDisaster_}������${H_tagDisaster}�����ä��褦�Ǥ�����",$id);
}

# ˦�ҡ���
sub logRotsick { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<b>�峤</b>�����߽Ф���<b>˦��</b>��${HtagName_}${name}${H_tagName}��${HtagDisaster_}����${H_tagDisaster}��⤿�餷���褦�Ǥ�����",$id);
}

# ���¡���
sub logSatansick { #1
	my ($id, $name) = @_;
	logOut("<b>�Ⲧ������</b>��${HtagName_}${name}${H_tagName}��<b>����</b>��${HtagDisaster_}����${H_tagDisaster}������${HtagName_}${name}${H_tagName}�Ǥ�${HtagDisaster_}����${H_tagDisaster}��ή�ԤäƤ���褦�Ǥ�����",$id);
}

# ���ø���
sub logMonsCome { #3
	my ($id, $name, $mName, $point, $lName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<b>$mName</b>�и�����${HtagName_}$point${H_tagName}��<b>$lName</b>��Ƨ�߹Ӥ餵��ޤ�����",$id);
}

# ��������
sub logMonsFree { #1
	my ($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>����������֤��ޤ�����",$id);
}

# ����ư��
sub logMonsMove { #1
	my ($id, $name, $lName, $point, $mName , $msg) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��<b>$mName</b>$msg",$id);
}

# ���á��ɱһ��ߤ�Ƨ��
sub logMonsMoveDefence { #1
	my ($id, $name, $lName, $point, $mName) = @_;
	logOut("<b>$mName</b>��${HtagName_}${name}$point${H_tagName}��<b>$lName</b>����ã��<b>${lName}�μ������֤���ư����</b>",$id);
}

# ���å��
sub logMonsWarp { #1
	my ($id, $name, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>����$mName</b>���ä����ޤ�����",$id);
}

# ���äμ����Ϸ����
sub logMonsWarpLand { #2
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>���и����ޤ�����",$id);
}

# ���饤�बʬ������
sub lognewMonsterBorn { #1
	my ($id, $name, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>���饤��</b>��ʬ�����ޤ�����",$id);
}

# �����Ƥ��
sub lognewKaiju { #1
	my ($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>����������ޤ�����",$id);
}

# ���á������Ǥ�
sub logMonsBomb { #1
	my ($id, $name, $lName, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>��${HtagDisaster_}���ȥ�����${H_tagDisaster}�򵯤����������ޤ�����",$id);
}

# ���á���֤�Ƥ�
sub logMonsHelpMe { #1
	my ($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}${point}${H_tagName}��<b>����$mName</b>��ŷ�˸����ä���Ӭ���ޤ�����",$id);
}

# ���ä���ȯ����
sub logMonsExplosion { #1
	my ($id, $name, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>����$mName</b>��<b>����ȯ</b>�򵯤����ޤ�����",$id);
}

# ���á����Ϥ�Ƥ��Ԥ���
sub logMonsFire { #1
	my ($id, $name, $lName, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��<b>$mName</b>�ˤ��׷��Ȥǲ��Ǥ��ޤ�����",$id);
}

# ���á����Ϥ�Ƥ��Ԥ���
sub logMonsFireS { #1
	my ($id, $name, $lName, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��<b>����$mName</b>���Ǥ��Ф�����ǾƤ��Ԥ�����ޤ�����",$id);
}

# ���á������Ƨ��
sub logMonsMine { #3
	my ($id, $name, $lName, $point, $mName, $str) = @_;
	logOut("<b>����$mName</b>��${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��Ƨ�����ȯ��<b>����$mName</b>��$str",$id);
}

# ���á���������
sub logMonsMoneyStole {
	my ($id, $name, $smoney, $mName) = @_;
	logOut("<b>����$mName</b>��${HtagName_}${name}${H_tagName}����${HtagDisaster_}${smoney}${HunitMoney}${H_tagDisaster}����ߤޤ�����",$id);
}

# ���á���������
sub logMonsMoneyStoleMiss {
	my ($id, $name, $mName) = @_;
	logOut("<b>����$mName</b>��${HtagName_}${name}${H_tagName}���餪�����⤦�Ȼ�ߤޤ��������Ԥ����褦�Ǥ���",$id);
}

# ���á����������
sub logMonsFoodStole {
	my ($id, $name, $sfood, $mName) = @_;
	logOut("<b>����$mName</b>��${HtagName_}${name}${H_tagName}���鿩��${HtagDisaster_}${sfood}${HunitFood}${H_tagDisaster}����ߤޤ�����",$id);
}

# ���á����������
sub logMonsFoodStoleMiss {
	my ($id, $name, $mName) = @_;
	logOut("<b>����$mName</b>��${HtagName_}${name}${H_tagName}���鿩������⤦�Ȼ�ߤޤ��������Ԥ����褦�Ǥ���",$id);
}

# �к�
sub logFire { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��${HtagDisaster_}�к�${H_tagDisaster}�ˤ����Ǥ��ޤ�����",$id);
}

# �к�̤��
sub logFirenot { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��${HtagDisaster_}�к�${H_tagDisaster}�ˤ���ﳲ������ޤ�����",$id);
}

# ��¢��
sub logMaizo { #1
	my ($id, $name, $comName, $value) = @_;
	logOut("${HtagName_}${name}${H_tagName}�Ǥ�${HtagComName_}$comName${H_tagComName}��ˡ�${HtagMoney_}$value$HunitMoney${H_tagMoney}���<b>��¢��</b>��ȯ������ޤ�����",$id);
}

# ���
sub logGold { #1
	my ($id, $name, $comName, $value) = @_;
	logOut("${HtagName_}${name}${H_tagName}�Ǥ�${HtagComName_}$comName${H_tagComName}��ˡ�<b>���</b>��ȯ������${HtagMoney_}$value$HunitMoney${H_tagMoney}�����פ�������ޤ�����",$id);
}

# ��ϳ�
sub logGoldEnd { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>����⤬�Τ�ʤ��ʤä��褦�Ǥ���",$id);
}

# �Ͽ�ȯ��
sub logEarthquake { #2
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}���絬�Ϥ�${HtagDisaster_}�Ͽ�${H_tagDisaster}��ȯ������",$id);
}

# ������­�ﳲ
sub logSvDamage { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��<b>��������ƽ�̱������</b>��<b>$lName</b>�ϲ��Ǥ��ޤ�����",$id);
}

# ����ȯ��
sub logTsunami { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}�ն��${HtagDisaster_}����${H_tagDisaster}ȯ������",$id);
}

# ����ȯ��
sub logTyphoon { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagDisaster_}����${H_tagDisaster}��Φ����",$id);
}

# ��С��
sub logMeteo { #10
    my ($id, $name, $lName, $point, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��${HtagDisaster_}���${H_tagDisaster}���$str�ޤ�����",$id);
}

# ��С�� 2
sub logMeteo2 {
    my ($id, $name, $lName, $point, $str , $metro) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��${HtagDisaster_}${metro}${H_tagDisaster}���$str�ޤ�����",$id);
}

# ��С��
sub logMeteo_Safe {
    my ($island) = @_;

    my ($name) = islandName($island);
    my ($id) = $island->{'id'};

    logOut("${HtagName_}${name}${H_tagName}��${HtagDisaster_}���${H_tagDisaster}�����褷�Ƥ��ޤ��������޷�����ˤ�äƼ���ޤ�����",$id);
}

# ��С�� def
sub logMeteoDef {
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��${HtagDisaster_}���${H_tagDisaster}���$str�ޤ�����",$id);
}

# ��С�����
sub logMeteoMonster { #2
	my ($id, $name, $lName, $point) = @_;
	logOut("<b>$lName</b>������${HtagName_}${name}$point${H_tagName}������${HtagDisaster_}���${H_tagDisaster}�����Φ�Ϥ�<b>$lName</b>���Ȥ���פ��ޤ�����",$id);
}

# �������
sub logHugeMeteo { #2
	my ($id, $name, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}������${HtagDisaster_}�������${H_tagDisaster}�������",$id);
}

# ʮ��
sub logEruption { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}������${HtagDisaster_}�л���ʮ��${H_tagDisaster}��<b>��</b>������ޤ�����",$id);
}

# ʮ�У�
sub logEruption2 { #3
	my ($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}������<b>$lName</b>�ϡ�${HtagDisaster_}ʮ��${H_tagDisaster}�αƶ���$str",$id);
}

# ��������ȯ��
sub logFalldown { #1
	my ($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagDisaster_}��������${H_tagDisaster}��ȯ�����ޤ�������",$id);
}

# �����ﳲ�����ÿ���
sub logWideDamageMonsterSea { #1
	my ($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��Φ�Ϥ�<b>$lName</b>���Ȥ���פ��ޤ�����",$id);
}

# ����
sub logPrize { #10
	my ($id, $name, $pName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<b>$pName</b>����ޤ��ޤ�����",$id);
	logHistory("${HtagName_}${name}${H_tagName}��<b>$pName</b>�����");
}

# ���ȼԤ��ǥ�
sub logUnemployedDemo { #1
	my ($id, $name, $pop, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${str}<b>$pop${HunitPop}</b>���ǥ�Կʤ�Ԥ��ޤ�����",$id);
}

# ���ȼԤ�˽ư
sub logUnemployedRiot { #1
	my ($id, $name, $lName, $pop, $point, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${str}<b>$pop${HunitPop}</b>��${HtagDisaster_}˽ư${H_tagDisaster}�򵯤�����${HtagName_}$point${H_tagName}������<b>$lName</b>��<b>����</b>��<b>$lName</b>�ϲ��Ǥ��ޤ�����",$id);
}

# ���ȼԤ���̱
sub logUnemployedMigrate { #1
	my ($id, $tId, $name, $tName, $pop, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagName_}${tName}${H_tagName}��${str}<b>$pop${HunitPop}</b>�ΰ�̱�����夷�ޤ�����${HtagName_}${tName}${H_tagName}�ϲ����������줿�褦�Ǥ���",$id, $tId);
}

# ��̱���䡼��
sub logUnemployedReturn { #1
	my ($id, $tId, $name, $lName, $tName, $pop, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagName_}${tName}${H_tagName}��${str}<b>$pop${HunitPop}</b>�ΰ�̱�����夷�ޤ�������${HtagName_}${tName}${H_tagName}��<b>$lName</b>�ϼ����������ݤ����褦�Ǥ���",$id, $tId);
}

# �͸�����
sub logPopDecrease { #5
    my ($id, $name, $lName, $tName, $str, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��${HtagDisaster_}${str}${H_tagDisaster}�ˤ��͸�������<b>$tName</b>�ˤʤ�ޤ�����",$id);
}

# ������Į���Ǥ���
sub logPlains2Town {
    my ($island, $lName, $point) = @_;

    my ($id) = $island->{'id'};
    #require './hako-io.cgi';
    my ($name) = islandName($island);

    logOut("${HtagName_}${name}$point${H_tagName}��<b>ʿ��</b>�˿�����<b>${lName}</b>���Ǥ��ޤ�����",$id);
}

# ����꤬ͽ����
sub logYakusho_Plains2 {
    my ($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>������꤬<b>ͽ����</b>�ˤ��ޤ�����",$id);
}

# ����꤬���ʤ餷
sub logYakusho_Prepare {
    my ($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>������꤬<b>ʿ��</b>�ˤ��ޤ�����",$id);
}

# ���ѥ������ޥ�
sub logSpiderMan {
    my ($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>${lName}</b>��<b>���ѥ������ޥ���</b>�����졢�ӥ�β���ǿ�������ݤ������郎����ޤ�����",$id);
}

# ���äε��ݤˤ�뼺��
sub logBokuFail2 {
    my ($id, $name, $comName, $kind, $point) = @_;
    logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}$comName${H_tagComName}�ϡ�ͽ����${HtagName_}$point${H_tagName}��<b>$kind</b>�������򤷤�������ߤ���ޤ�����",$id);
}

# ���
sub logFishing {
    my ($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>${lName}</b>�Ǥϡ����̾�ͤ���ʪ�����夲���˥塼���ǻ�������Ǥ���",$id);
}

# ���ñۤ�����
sub logHikkosi_miss {
    my ($id, $name) = @_;
    my ($comName);
    $comName = $HcomName[$HcomBoku2];
    logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���<b>${comName}</b>�ϡ���Ū�Ϥ�Ŭ���ʤ����ᡢ���Ԥ��ޤ�����",$id);
}

# ���󥹥ȥա���
sub logFoodsute {
    my ($id, $name, $fd , $money) = @_;
    #������λ�������ʤ��ʤä�����X�ȥ�ϡ�Y���ߤ˴��⤵��ޤ�����
    logSecret("${HtagName_}${name}${H_tagName}�λ�������ʤ��ʤä�����${HtagFood_}${fd}${HunitFood}${H_tagFood}��${HtagMoney_}${money}${HunitMoney}${H_tagMoney}�˴��⤵��ޤ�����",$id);
}

# �ա���
sub logGiveFoodUpdate {
    my ($id, $sta, $update ) = @_;
    #������λ�������ʤ��ʤä�����X�ȥ�ϡ�Y���ߤ˴��⤵��ޤ�����
    logOut("<b>$sta</b>����$update�˥��åפ�����",$id);
}

# �����ƥ��ΤƤ�
sub logItemThrow {
    my ($id, $name, $iName) = @_;
    logSecret("${HtagName_}${name}${H_tagName}��<b>${iName}</b>��ΤƤޤ�����",$id);
}

# �����ƥप����
sub logItemPuton {
    my ($id, $name,$point, $iName ) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>${iName}</b>���֤��ޤ�����",$id);
}

# �����ƥब�ʤ�
sub logItemisNoting {
    my ($id, $name) = @_;
    logOut("${HtagName_}${name}${H_tagName}�ϻ��äƤʤ������ƥ��Ȥ����Ȥ��ޤ�����",$id);
}

# �����ƥब�����ʤ�
sub logItemDeny {
    my ($id, $name, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}�������ƥ���֤��Τ�Ŭ���ʤ����ᡢ���Ԥ��ޤ�����",$id);
}

# �������Ⱦ줷����
sub logSkateDown {
    my ($island, $landname, $x, $y) = @_;
    my ($point) = "($x,$y)";
    my ($id) = $island->{'id'};
    my ($name) = islandName($island);
    logOut("${HtagName_}${name}$point${H_tagName}��<b>${landname}</b>�ϡ�ɹ���Ȥ��Ƥʤ��ʤ�ޤ�����",$id);
}

# �Ƥ��ϴ�
sub logLavaAttack {
    my ($id, $name, $mName, $point, $tName, $tPoint) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$mName</b>�θƤӵ�������${HtagDisaster_}�ϴ�${H_tagDisaster}��${HtagName_}$tPoint${H_tagName}��<b>$tName</b>��Ƥ��ޤ�����",$id, $tId);
}

# ����
sub logNige {
    my ($id, $name, $lName, $mName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>ưʪ��</b>����<b>$mName</b>��${HtagDisaster_}æ��${H_tagDisaster}���ޤ�����",$id);
}

# ���û�����
sub logSiire {
    my ($id, $name, $lName, $mName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>��<b>$mName</b>�����٤��������Ǥ��ޤ���",$id);
END
}

# ���Ĥ���μ���
sub logOilMoney2 {
    my ($id, $name, $lName, $point, $str, $str2) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>$lName</b>���顢${HtagMoney_}$str${H_tagMoney}�μ��פ��夬��ޤ�����(����${HtagFood_}$str2${H_tagFood}����)",$id);
END
}

# ����
sub logNige2 {
    my ($id, $name, $lName, $mName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<b>ưʪ��</b>����<b>$mName</b>��${HtagDisaster_}æ��${H_tagDisaster}�����ޤ�����",$id);
}

1;
