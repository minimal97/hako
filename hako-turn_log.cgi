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
	my($id, $name, $comName, $num) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagNumber_}$num��${H_tagNumber}��${HtagComName_}$comName${H_tagComName}��Ԥ��ޤ�����",$id);
}

# ���ԤǤ���
sub logShuto {
    my($id, $name, $lName, $sName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>�ϡ�<B>����$sName</B>�Ȥ���${AfterName}���濴Ū�ԻԤؤȤʤ�ޤ�����",$id);
    logHistory("${HtagName_}${name}${H_tagName}��<B>����$sName</B>������ޤ�����");
}

# ����ȯ��
sub logHotFound {
    my($id, $name, $point, $comName, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>$str</B>��ͽ����Ĥ������${HtagComName_}${comName}${H_tagComName}���Ԥ�졢<B>�������������Ƥ��ޤ���</B>��",$id);
}

# ����ȯ���ʤ餺
sub logHotFail {
    my($id, $name, $point, $comName, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>$str</B>��ͽ����Ĥ������${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ������������ϸ��Ĥ���ޤ���Ǥ�����",$id);
}

# ���¤���μ���
sub logSinMoney {
    my($id, $name, $str) = @_;
    logSecret("${HtagName_}${name}$point${H_tagName}��<B>����</B>�ǽˤ��κפ꤬�Ԥ�졢<B>$str</B>�μ��פ��夬��ޤ�����",$id);
}

# ���Ҥ���μ���
sub logJinMoney {
    my($id, $name, $str) = @_;
    logSecret("${HtagName_}${name}$point${H_tagName}��<B>����</B>�ǽˤ��κפ꤬�Ԥ�졢<B>$str</B>�μ��פ��夬��ޤ�����",$id);
}

# ����⤫��μ���
sub logEnjo {
    my($id, $name, $lName, $point, $str) = @_;
    logOut("��ȯ�ʹ԰Ѱ��񤫤�${HtagName_}${name}${H_tagName}��<B>$str</B>�α���⤬�ٵ뤵�줿�褦�Ǥ���",$id);
}

# �ߥ�����ޤȤ��
sub logMsTotal {
    my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $count, $mukou, $bouei, $kaijumukou, $kaijuhit, $fuhatu) = @_;
    logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}$countȯ��${comName}${H_tagComName}��Ԥ��ޤ�����<br>������${HtagName_}���${H_tagName}��(̵��$mukouȯ/�ɱ�$boueiȯ/�����껦$kaijumukouȯ/����̿��$kaijuhitȯ/��ȯ��$fuhatuȯ)",$id, $tId);
}

# ���ƥ륹�ߥ�����ޤȤ��
sub logMsTotalS {
    my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $count, $mukou, $bouei, $kaijumukou, $kaijuhit, $fuhatu) = @_;
    logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}$countȯ��${comName}${H_tagComName}��Ԥ��ޤ�����<br>������${HtagName_}���${H_tagName}��(̵��$mukouȯ/�ɱ�$boueiȯ/�����껦$kaijumukouȯ/����̿��$kaijuhitȯ/��ȯ��$fuhatuȯ)",$id);
    logLate("<B>���Ԥ�</B>��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}$countȯ��${comName}${H_tagComName}��Ԥ��ޤ�����<br>������${HtagName_}���${H_tagName}��(̵��$mukouȯ/�ɱ�$boueiȯ/�����껦$kaijumukouȯ/����̿��$kaijuhitȯ)", $tId);
}

# ���Ԥ򹶷⤹��
sub logMonsAttacks {
  my($id, $name, $lName, $point) = @_;
  logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>�ϲ��ä�${HtagDisaster_}����${H_tagDisaster}�����ﳲ������ޤ�����",$id);
}

# ���Ԥ򹶷⤹��
sub logMonsAttacksSecret {
  my($id, $name, $lName, $point) = @_;
  logSecret("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>�ϲ��ä�${HtagDisaster_}����${H_tagDisaster}�����ﳲ������ޤ�����",$id);
}

# ��⡦����������­��ʤ������Ĥ���ʤ�
sub logNoAny { #20
	my($id, $name, $comName, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}$comName${H_tagComName}�ϡ�$str������ߤ���ޤ�����",$id);
}

# �ޥ����åȤ����⤹��
sub logMsAttackt {
  my($id, $name, $mName, $point, $cPoint, $tName, $tPoint) = @_;
  logOut("${HtagName_}${name}${H_tagName}��<B>$mName</B>��$tPoint<B>$tName</B>�򹶷⤷${HtagDisaster_}$point${H_tagDisaster}�Υ��᡼����Ϳ��${HtagDisaster_}$cPoint${H_tagDisaster}�Υ��᡼��������ޤ�����",$id, $tId);
}

# �ߥ�����������
sub logMsAttackmika {
  my($id, $name, $mName, $point, $cPoint, $tName) = @_;
  logOut("${HtagName_}${name}${H_tagName}��<B>$mName</B>��<B>$tName</B>���襤������Ȥʤꡢ${AfterName}̱��<B>��ʡ�ν�����</B>���¤���ޤ�����",$id, $tId);
}

# ����Ǽ�Ϥ�
sub logItiAttackms {
  my($id, $name, $mName, $point, $tName, $tPoint) = @_;
  logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>��$tPoint<B>$tName</B>��¤�Ĥ��ޤ�����",$id, $tId);
}


# ɹ�Ƕ��ɤ�
sub logIceAttack {
  my($id, $name, $mName, $point, $tName, $tPoint) = @_;
  logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>��ȯ����ɹ�����${HtagName_}$tPoint${H_tagName}��<B>$tName</B>���濴��Ӥ��ޤ�����",$id, $tId);
}

# �Ƥ�
sub logFireAttack {
  my($id, $name, $mName, $point, $tName, $tPoint) = @_;
  logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>�θƤӵ�������${HtagDisaster_}��${H_tagDisaster}��${HtagName_}$tPoint${H_tagName}��<B>$tName</B>��Ƥ��ޤ�����",$id, $tId);
}

# �إ�ե�����
sub logHellAttack {
  my($id, $name, $mName, $point, $tName, $tPoint) = @_;
  logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>�θƤӵ�������${HtagDisaster_}�Ϲ��α�${H_tagDisaster}��${HtagName_}$tPoint${H_tagName}��<B>$tName</B>��Ƥ��Ԥ����ޤ�����",$id, $tId);
}

# �������Ϥ����⤹��
sub logFuneAttackSSS {
  my($id, $name, $lName, $point, $tName, $tPoint) = @_;
  logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��<B>���ͥ륮��ˤ</B>��ȯ�ͤ���<B>$tName</B>��̿�椷�ޤ�����",$id, $tId);
}

# �������Ϥ����⤹��
sub logFuneAttackSSSR {
  my($id, $name, $lName, $point, $tName, $tPoint) = @_;
  logOut("${HtagName_}${name}${H_tagName}��<B>$tName</B>��<B>�ڤ�ü����</B>�ˤʤ�ޤ�����",$id, $tId);
}

# �������Ϥ����⤹��
sub logFuneAttackSSST {
  my($id, $name, $lName, $point, $tName, $tPoint) = @_;
  logOut("${HtagName_}${name}${H_tagName}��<B>$tName</B>��<B>�ڤ�ü����</B>�ˤʤꡢ<B>$lName</B>��${HtagDisaster_}�����С��ҡ���${H_tagDisaster}�ˤ��${HtagDisaster_}����ȯ${H_tagDisaster}���ޤ�����",$id, $tId);
}

# ���۲�
sub logEggBomb {
	my($id, $name, $lName, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>����<B>$mName</B>���и����ޤ�����",$id);
}

# �����ﳲ
sub logEggDamage {
	my($id, $name, $landName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$landName</B>��${HtagDisaster_}��������ˤ�륨�ͥ륮��${H_tagDisaster}�ˤ����פ��ޤ�����",$id);
}

# ���Τ�з�
sub logMstakeon {
	my($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��<B>�����༣</B>�˸������ޤ�����",$id);
}

# ���Τ鵢��
sub logMstakeokaeri {
	my($id, $name, $lName, $point, $tName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<B>$lName</B>��${HtagName_}$point${H_tagName}��<B>$tName</B>�˵��äƤ��ޤ��������Ĥ��줵�ޡ�",$id);
}

# ���Τ�Ƚ�
sub logMstakeiede {
	my($id, $name, $lName, $point, $tName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<B>$lName</B>�ϵ���٤��Ȥ��ʤ������ι�˽Фޤ�����",$id);
}

# ���Τ��������
sub logMstakeoff {
	my($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��<B>�ޥ����åȲ���</B>»���Τ��᱿�ĺ���ˤʤ�ޤ�����",$id);
}

# ���Τ�Ƚ�
sub logHimeKaeru {
	my($id, $name, $lName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<B>$lName</B>�ϡ����Ф���줿�Τǵ���ޤ�����",$id);
}

# ���ǵե���
sub logKire {
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<B>����</B>��${AfterName}̱��${HtagDisaster_}����${H_tagDisaster}�ޤ�������",$id);
}

# �����ﳲ
sub logKireDamage {
	my($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��${HtagDisaster_}˽���${AfterName}̱${H_tagDisaster}�ˤ�ä�${HtagDisaster_}�˲�${H_tagDisaster}����ޤ�����",$id);
}

# �����ﳲ
sub logZeikin_fuman {
    my ($id, $name) = @_;
    logOut("${HtagName_}${name}${H_tagName}�ν�̱�ϡ�<b>�Ƕ���Ф��ơ��ڤ�ΤƤ����⤬¿�����Ȥˡ�����</B>�򴶤��Ƥ��ޤ���",$id);
}

# ���ø���(������)
sub logMonsComemagic {
	my($id, $name, $mName, $point, $lName) = @_;
	logOut("${HtagName_}${name}${H_tagName}���˲����줿<B>������</B>����<B>$mName</B>�и�����",$id);
}

# ���á����Ϥ���ƿԤ���
sub logMonsCold {
	my($id, $name, $lName, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��<B>$mName</B>���괬���䵤�ˤ����ƤĤ��ޤ�����",$id);
}

# ��
sub logEggFound {
	my($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}�Ǥ�${HtagComName_}$comName${H_tagComName}��ˡ�<B>��������</B>��ȯ������${HtagComName_}$comName�ȼ�${H_tagComName}�ˤ��˲���̵���ʤΤ����֤��뤳�Ȥˤ��ޤ�����",$id);
}

# ����
sub logIsekiFound {
	my($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}�Ǥ�${HtagComName_}$comName${H_tagComName}��ˡ�<B>�������</B>��ȯ������<B>${AfterName}�ν�����¢ʸ����</B>�˻��ꤵ��ޤ�����",$id);
}

# ����
sub logPrizet {
	my($id, $name, $pName, $value) = @_;
	my $str = "(�޶�${HtagMoney_}$value${H_tagMoney})" if($value > 0);
	logOut("${HtagName_}${name}${H_tagName}��<B>$pName</B>����ޤ��ޤ�����$str",$id);
	logHistory("${HtagName_}${name}${H_tagName}��<B>$pName</B>�����$str");
}

# Ȣ���å�
sub logHC {
	my($id, $name, $stsanka) = @_;
	if($stsanka) {
#		logHistory("${HtagName_}Hakoniwa Cup $HislandTurn${H_tagName}���š�<B>���ÿ�</B>${HtagNumber_}$stsanka${AfterName}��${H_tagNumber}");
		logHcup("${HtagName_}Hakoniwa Cup $HislandTurn${H_tagName}���š�<B>���ÿ�</B>${HtagNumber_}$stsanka${AfterName}��${H_tagNumber}");
	} else {
		logHcup("${HtagName_}Hakoniwa Cup $HislandTurn${H_tagName}�ϡ����ä���${AfterName}���ʤ��ä�����${HtagNumber_}��ߤˤʤ�ޤ�����${H_tagNumber}");
	}
}

# Ȣ���å׳���
sub logHCstart {
	my($id, $name, $str) = @_;
#	logHistory("${HtagName_}${name}${H_tagName}��<B>Hakoniwa Cup ����</B>���Ԥʤ�졢${HtagMoney_}$str${H_tagMoney}�ηкѸ��̤򴬤��������ޤ�����",$id);
	logLate("${HtagName_}${name}${H_tagName}��<B>Hakoniwa Cup ����</B>���Ԥʤ�졢${HtagMoney_}$str${H_tagMoney}�ηкѸ��̤򴬤��������ޤ�����",$id);
	logHcup("${HtagName_}${name}${H_tagName}��<B>Hakoniwa Cup ����</B>���Ԥʤ�졢${HtagMoney_}$str${H_tagMoney}�ηкѸ��̤򴬤��������ޤ�����");
}

# Ȣ���å׻��
sub logHCgame {
	my($id, $tId, $name, $tName, $lName, $gName, $goal, $tgoal, $Teamname, $tTeamname) = @_;
	my($tena, $ttena);
	my($home, $away);

    $tena = "";
    $tena = "(${Teamname})" if ( length($Teamname) > 0);
    $ttena = "";
    $ttena = "(${tTeamname})" if ( length($tTeamname) > 0);

	if($goal < $tgoal) {
		$str = "${HtagLose_}${name}��ɽ${tena}${H_tagLose}<B>VS</B>${HtagWin_}${tName}��ɽ${ttena}${H_tagWin} �� ${HtagLose_}$goal${H_tagLose}<B>��</B>${HtagWin_}$tgoal${H_tagWin}";
	} else {
		$str = "${HtagWin_}${name}��ɽ${tena}${H_tagWin}<B>VS</B>${HtagLose_}${tName}��ɽ${ttena}${H_tagLose} �� ${HtagWin_}$goal${H_tagWin}<B>��</B>${HtagLose_}$tgoal${H_tagLose}";
	}
	logLate("${HtagName_}${name}${H_tagName}��<B>Hakoniwa Cup $gName</B>���Ԥ��ޤ�����$str",$id, $tId);
	logHcup("${HtagName_}Hakoniwa Cup ${gName}${H_tagName}��$str");
}

# Ȣ���å׾���
sub logHCwin {
	my($id, $name, $cName, $str) = @_;
	logLate("${HtagName_}${name}��ɽ${H_tagName}��<B>$cName</B>��${HtagName_}${name}${H_tagName}��${HtagMoney_}$str${H_tagMoney}�ηкѸ��̤򴬤��������ޤ�����",$id);
}

# Ȣ���å�ͥ��
sub logHCwintop {
	my($id, $name, $cName) = @_;
#	logHistory("${HtagName_}${name}��ɽ${H_tagName}��${HtagWin_}Hakoniwa Cup $cNameͥ����${H_tagWin}",$id);
	logLate("${HtagWin_}${name}��ɽ${H_tagWin}��${HtagName_}Hakoniwa Cup $cName${H_tagName}${HtagWin_}ͥ����${H_tagWin}",$id);
	logHcup("${HtagWin_}${name}��ɽ${H_tagWin}��${HtagName_}Hakoniwa Cup $cName${H_tagName}${HtagWin_}ͥ����${H_tagWin}");
}

# Ȣ���å����ﾡ
sub logHCantiwin {
	my($id, $name, $gName) = @_;
	logLate("${HtagName_}Hakoniwa Cup ${gName}${H_tagName}��${HtagWin_}${name}��ɽ${H_tagWin}�ϡ���������ब���ʤ�����${HtagWin_}���ﾡ${H_tagWin}�Ȥʤ�ޤ�����",$id);
	logHcup("${HtagName_}Hakoniwa Cup ${gName}${H_tagName}��${HtagWin_}${name}��ɽ${H_tagWin}�ϡ���������ब���ʤ�����${HtagWin_}���ﾡ${H_tagWin}��");
}

# Ȣ���å�
sub logHCsin {
	my($id, $name, $stsin) = @_;
#	logHistory("${HtagName_}Hakoniwa Cup �辡�ȡ��ʥ��ȿʽ�${AfterName}!!${H_tagName}<br><font size=\"-1\"><B>$stsin</B></font>");
	logHcup("${HtagName_}Hakoniwa Cup �辡�ȡ��ʥ��ȿʽ�${AfterName}!!${H_tagName}<br><font size=\"-1\"><B>$stsin</B></font>");
}

# �Ѹ����꤬�Ȥ��������ޤ�
sub logKankouMigrate {
	my($id, $tId, $name, $lName, $tName, $point, $pop) = @_;
	logOut("${HtagName_}${tName}${H_tagName}����${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��<B>$pop${HunitPop}</B>�δѸ��Ԥ���Ƥ���ޤ��������꤬�Ȥ��������ޤ���",$id, $tId);
}

# �ߥ������Ȥ��Ȥ��������Ϥ��ʤ�
sub logMsNoBase { #1
	my($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}${comName}${H_tagComName}�ϡ�<B>�ߥ�������������ͭ���Ƥ��ʤ�</B>����˼¹ԤǤ��ޤ���Ǥ�����",$id);
}

# �о��Ϸ��μ���ˤ�뼺��
sub logLandFail { #14
    my($id, $name, $comName, $kind, $point) = @_;
    logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}$comName${H_tagComName}�ϡ�ͽ���Ϥ�${HtagName_}$point${H_tagName}��<B>$kind</B>���ä�������ߤ���ޤ�����",$id);
}

# �о��Ϸ��μ���ˤ�뼺�ԣ�
sub logLandFail2 { #5
	my($id, $name, $comName, $point, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}$comName${H_tagComName}�ϡ�ͽ���Ϥ�${HtagName_}$point${H_tagName}��$str������ߤ���ޤ�����",$id);
}

# Į������
sub logTownDel { #25
    my($id, $name, $tName , $comName, $point, $lv) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>${tName}</B>��${HtagComName_}${comName}${H_tagComName}��Ԥä����ᡢ<B>${lv}${HunitPop}</B>��Ω�����ޤ�����",$id);
}

# Į������
sub logSouon { #25
    my($id, $name, $point, $tName, $lv) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>${tName}</B>���������Ѥ��ڤ줺�����Ϥν�̱<B>${lv}${HunitPop}</B>��Ω�����ޤ�����",$id);
}

# ���Ϸ�����
sub logLandSuc { #25
	my($id, $name, $comName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ�����",$id);
}

# ���Ϸϥ��ޤȤ�
sub logLandSucMatome {
	my($id, $name, $comName, $point) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ�����<br>����<B>��</B> $point",$id);
}

# ��������
sub logEiseifail { #1
	my($id, $name, $comName, $point) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ������Ǥ��夲��${HtagDisaster_}����${H_tagDisaster}�����褦�Ǥ���",$id);
}

# ����ȯ��
sub logOilFound { #1
	my($id, $name, $point, $comName, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��${HtagMoney_}$str${H_tagMoney}��ͽ����Ĥ������${HtagComName_}${comName}${H_tagComName}���Ԥ�졢<B>���Ĥ��������Ƥ��ޤ���</B>��",$id);
}

# ����ȯ��200
sub logOil200Found { #1
	my($id, $name, $point, $comName, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��${HtagMoney_}$str${H_tagMoney}��ͽ����Ĥ������${HtagComName_}${comName}${H_tagComName}���Ԥ�졢<B>���Ĥ��������Ƥ��ޤ���</B>��<br>200�������Ĥ��꤬£���ޤ�����",$id);
}

# ����ȯ���ʤ餺
sub logOilFail { #1
	my($id, $name, $point, $comName, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��${HtagMoney_}$str${H_tagMoney}��ͽ����Ĥ������${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ����������Ĥϸ��Ĥ���ޤ���Ǥ�����",$id);
}

# ���ġ��ؽꡦͷ���ϡ���������μ���
sub logOilMoney { #9
	my($id, $name, $lName, $point, $value, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>���顢${HtagMoney_}$value${H_tagMoney}��$str���夬��ޤ�����",$id);
}

# ���ĸϳ顢�����ﳲ����¾
sub logDamageAny { #29
	my($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��$str",$id);
}

# ͷ���ϤΥ��٥��
sub logParkEvent { #4
	my($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>�ǥ��٥�Ȥ����Ť��졢${HtagFood_}$str${H_tagFood}�ο��������񤵤�ޤ�����",$id);
}

# �ݸ�����μ���
sub logHoken { #1
	my($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>�λ��Τˤ�ꡢ${HtagMoney_}$str${H_tagMoney}���ݸ�������ޤ�����",$id);
}

# �ڻ�����μ���
sub logMiyage { #1
	my($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName��ǰ�����</B>�Τ��ڻ������󤫤�${HtagMoney_}$str${H_tagMoney}�μ���������ޤ�����",$id);
}

# ͥ������μ���
sub logYusho { #1
	my($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}�����������${HtagName_}$point${H_tagName}��<B>$lName</B>�ǹԤ�줿Ȣ��꡼���辡��Ǥߤ���ͥ������${HtagMoney_}$str${H_tagMoney}�ηкѸ��̤�������ޤ�����",$id);
}

# TITANIC�ǲ貽
sub logTitanicEnd { #1
	my($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>�����פϱǲ貽���졢¿���οͤ��ޤ�ή���ޤ�����(${HtagMoney_}$str${H_tagMoney}�����׼���)",$id);
}

# ����õ������μ���
sub logTansaku { #1
	my($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��������ȯ����${HtagMoney_}$str${H_tagMoney}�β��ͤ����뤳�Ȥ��狼��ޤ�����",$id);
	logHistory("${HtagName_}${name}${H_tagName}��<B>$lName</B>��������ȯ����");
}

# ����õ��������
sub logTansakuoil { #1
	my($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>�����Ĥ�ȯ����",$id);
}

# ����
sub logOilMoneyt { #1
	my($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>����Ȥ���������${HtagMoney_}$str${H_tagMoney}���ͤ��դ��ޤ�����",$id);
}

# ������
sub logParkEventt { #2
    my ($id, $name, $lName, $point, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>���⤿�餷��˭��ˤ�ꡢ�����${HtagFood_}$str${H_tagFood}�ο���������ޤ�����",$id);
}

# �ϥ��ƥ���Ȥξ���
sub logFactoryHT { #2
    my ($id, $name, $lName, $str) = @_;
    logSecret("${HtagName_}${name}${H_tagName}��<B>$lName</B>�ϡ�${HtagMoney_}$str${H_tagMoney}����񤷤ޤ�����",$id);
}

# ���μ���
sub logParkEventf { #2
    my ($id, $name, $lName, $point, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>�ϡ�${HtagFood_}$str${H_tagFood}�ο��������ޤ�����",$id);
}

# �ɱһ��ߡ��������å�
#sub logBombSet { #1
#   my($id, $name, $lName, $point) = @_;
#   logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��<B>�������֤����å�</B>����ޤ�����",$id);
#}

# �ɱһ��ߡ�������ư
#sub logBombFire { #1
#   my($id, $name, $lName, $point) = @_;
#   logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��${HtagDisaster_}�������ֺ�ư����${H_tagDisaster}",$id);
#}

# ��ǰ�ꡢȯ��
sub logMonFly { #1
	my($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��<B>�첻�ȤȤ������Ω���ޤ���</B>��",$id);
}

# ��ǰ�ꡢ�
sub logMonDamage { #1
	my($id, $name, $point) = @_;
	logOut("<B>�����ȤƤĤ�ʤ����</B>��${HtagName_}${name}$point${H_tagName}����������ޤ�������",$id);
}

# ����or�ߥ��������
sub logPBSuc { #3
	my($id, $name, $comName, $point) = @_;
	logSecret("${HtagName_}${name}$point${H_tagName}��${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ�����",$id);
	logOut("������ʤ�����${HtagName_}${name}${H_tagName}��<B>��</B>���������褦�Ǥ���",$id);
}

# �ϥ�ܥ�
sub logHariSuc { #1
	my($id, $name, $comName, $comName2, $point) = @_;
	logSecret("${HtagName_}${name}$point${H_tagName}��${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ�����",$id);
	logLandSuc($id, $name, $comName2, $point);
}

# ������˲��ä����ʤ�
sub logNoTarget {
	my($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}$comName${H_tagComName}�ϡ�������˲��ä����ʤ�������ߤ���ޤ�����",$id);
}

# �ߥ������ä����ϰϳ�
sub logMsOut { #1
	my($id, $tId, $name, $tName, $comName, $point) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������<B>�ΰ賰�γ�</B>����������ͤǤ���",$id, $tId);
}

# ���ƥ륹�ߥ������ä����ϰϳ�
sub logMsOutS { #1
	my($id, $tId, $name, $tName, $comName, $point) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������<B>�ΰ賰�γ�</B>����������ͤǤ���",$id);
	logLate("<B>���Ԥ�</B>��${HtagName_}${tName}$point${H_tagName}�ظ�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������<B>�ΰ賰�γ�</B>����������ͤǤ���",$tId);
}

# �����˲�����
sub logEiseiAtts { #1
	my($id, $tId, $name, $tName, $comName, $tEiseiname) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}${H_tagName}�˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���<B>$tEiseiname</B>��̿�档<B>$tEiseiname</B>���׷���ʤ��ä����Ӥޤ�����",$id, $tId);
}

# �����˲�����
sub logEiseiAttf { #1
	my($id, $tId, $name, $tName, $comName, $tEiseiname) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}${H_tagName}��<B>$tEiseiname</B>�˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ����������ˤ�̿�椻������������ؤ����ӵ�äƤ��ޤ��ޤ�������",$id, $tId);
}

# �ߥ������ä����ɱһ��ߤǥ���å�
sub logMsCaught { #2
	my($id, $tId, $name, $tName, $comName, $point, $tPoint) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��������ˤ��Ͼ��ª����졢<B>������ȯ</B>���ޤ�����",$id, $tId);
}

# ���ƥ륹�ߥ������ä����ɱһ��ߤǥ���å�
sub logMsCaughtS { #2
	my($id, $tId, $name, $tName, $comName, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��������ˤ��Ͼ��ª����졢<B>������ȯ</B>���ޤ�����",$id);
	logLate("<B>���Ԥ�</B>��${HtagName_}${tName}$point${H_tagName}�ظ�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��������ˤ��Ͼ��ª����졢<B>������ȯ</B>���ޤ�����",$tId);
}

# �ߥ������ä����ɱұ����ǥ���å�(ST�Х�ޤ�)
sub logMsCaughtE { #1
	my($id, $tId, $name, $tName, $comName, $point, $tPoint) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������<B>�ɱұ���</B>�˷����Ȥ���ޤ�����",$id, $tId);
}

# �ߥ������ä������̤ʤ�
sub logMsNoDamage { #3
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $flag) = @_;
	my $noga = '��';
	$noga = '��' if($flag);
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}${noga}<B>$tLname</B>��������Τ��ﳲ������ޤ���Ǥ�����",$id, $tId);
}

# ���ƥ륹�ߥ������ä������̤ʤ�
sub logMsNoDamageS { #2
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $flag) = @_;
	my $noga = '��';
	$noga = '��' if($flag);
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}${noga}<B>$tLname</B>��������Τ��ﳲ������ޤ���Ǥ�����",$id);
	logLate("<B>���Ԥ�</B>��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}${noga}<B>$tLname</B>��������Τ��ﳲ������ޤ���Ǥ�����",$tId);
}

# �̾�ߥ����롢���ä�̿�桢���᡼�������� or Φ���˲���(LD)������̿��
sub logMsMonster { #3
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>��̿�档<B>$tLname</B>��$str",$id, $tId);
}

# ���ƥ륹�ߥ����롢���ä�̿�桢���᡼��������
sub logMsMonsterS { #1
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>��̿�档<B>$tLname</B>��$str",$id);
	logLate("<B>���Ԥ�</B>��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>��̿�档<B>$tLname</B>��$str",$tId);
}

# Φ���˲���(LD)���Ϸ�δ����(LR)��������Ϥ�̿��
sub logMsLSbase { #3
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��������ȯ��Ʊ�����ˤ��ä�<B>$tLname</B>��$str",$id, $tId);
}

# Φ���˲���(LD)���Ϸ�δ����(LR)�����ä�̿��
sub logMsLMonster { #2
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}�����Ƥ���ȯ��Φ�Ϥ�<B>$tLname</B>���Ȥ�$str",$id, $tId);
}

# Φ���˲���(LD)�Ϸ�δ����(LR)�������峤������¾���Ϸ���̿��
sub logMsLOther { #7
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>�����ơ�$str",$id, $tId);
}

# �˥ߥ����롢����
sub logMsSS { #1
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>�����Ƥ�����ȯ���ޤ�����",$id, $tId);
}

# �̾�ߥ������̾��Ϸ����峤������(�Ų���)��̿��
sub logMsNormal { #3
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>��̿�桢$str",$id, $tId);
}

# ���ƥ륹�ߥ������̾��Ϸ����峤������(�Ų���)��̿��
sub logMsNormalS { #3
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>��̿�桢$str",$id);
	logLate("<B>���Ԥ�</B>��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>��̿�桢$str",$tId);
}

# ���äλ���
sub logMsMonMoney { #6
	my($tId, $mName, $value) = @_;
	logOut("<B>$mName</B>�λĳ��ˤϡ�<B>$value$HunitMoney</B>���ͤ��դ��ޤ�����",$tId);
}

# �ߥ�������̱����
sub logMsBoatPeople { #1
	my($id, $name, $achive) = @_;
	logOut("${HtagName_}${name}${H_tagName}�ˤɤ�����Ȥ�ʤ�<B>$achive${HunitPop}�����̱</B>��ɺ�夷�ޤ�����${HtagName_}${name}${H_tagName}�ϲ����������줿�褦�Ǥ���",$id);
}

# ���ƥ륹�ߥ����롢���Ϥ�����
sub logMsWasteS { #1
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>������ޤ�����",$id);
	logLate("<B>���Ԥ�</B>��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>������ޤ�����",$tId);
}

# ���ƥ륹�ߥ����롢���äˤ�������Ȥ����
sub logMsMonsCautS { #1
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>�ˤ�������Ȥ���ޤ�����",$id);
}

# ���ƥ륹�ߥ����롢ŷ�Ȥˤ�������Ȥ����
sub logMsMonsCauttS { #1
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>���Ǥ��ä���ޤ�����",$id);
}

# ���ƥ륹�ߥ����롢���饤��ˤ�������Ȥ����
sub logMsMonsCautlS { #1
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>�˰��߹��ޤ�ޤ�����",$id);
}

# ���ƥ륹�ߥ����롢�ᥫ�ˤ�������Ȥ����
sub logMsMonsCautmS { #1
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>�ˤ��޷�ߥ�����˷�����ޤ�����",$id);
}

# �̾�ߥ����롢���äˤ�������Ȥ���롦���Ϥ�����
sub logMsMonsCaut { #5
	my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$point${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�������${HtagName_}$tPoint${H_tagName}��<B>$tLname</B>��$str",$id, $tId);
}

# ���ä����⤹��
sub logMonsAttack { #2
	my($id, $name, $mName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>��$tPoint<B>$tName</B>�˸����äƱ���Ǥ��Ĥ��ޤ�����",$id, $tId);
}

# ŷ�Ȥ����⤹��
sub logMonsAttackt { #1
	my($id, $name, $mName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>��$tPoint<B>$tName</B>�򹶷⤷�ޤ�����",$id, $tId);
}

# ���줬���⤹��
sub logIreAttackt { #2
	my($id, $name, $mName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<B>$mName</B>��$tPoint<B>$tName</B>�򹶷⤷${HtagDisaster_}$point${H_tagDisaster}�Υ��᡼����Ϳ���ޤ�����",$id, $tId);
}

# ����Ǽ�Ϥ�
sub logItiAttack { #1
	my($id, $name, $mName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>��$tPoint<B>$tName</B>�μ����ͤޤ�����",$id, $tId);
}

# �Ͼ�ǲ��ä�����
sub logBariaAttack { #1
	my($id, $name, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$tPoint${H_tagName}��<B>$tName</B>�����Ϥ��Ͼ�˲����٤���ޤ�����",$id, $tId);
}

# ��ˡ��ƥ�����������
sub logMgSpel { #3
	my($id, $name, $mName, $point, $spel) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>��${HtagDisaster_}$spel${H_tagDisaster}�򾧤��ޤ�����",$id);
}

# ��ˡ�ɥ쥤��
sub logMgDrain { #1
	my($id, $name, $mName, $tName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>��<B>$tName</B>���Ф���${HtagDisaster_}�ɥ쥤��${H_tagDisaster}�򾧤��ޤ�����",$id);
}

# ����
sub logShoukan { #1
	my($id, $name, $nName, $mName, $point) = @_;
	logOut("<B>$nName</B>��${HtagName_}${name}$point${H_tagName}��<B>$mName</B>��${HtagDisaster_}����${H_tagDisaster}���ޤ�����",$id);
}

# �網��
sub logKyoukou { #1
	my($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>��${HtagName_}${name}${H_tagName}��${HtagDisaster_}�網��${H_tagDisaster}��⤿�餷�ޤ�����",$id);
}

# �忩
sub logFushoku { #2
	my($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>��${HtagName_}${name}${H_tagName}���ߤ��Ƥ���<B>����</B>��${HtagDisaster_}����${H_tagDisaster}�����Ƥ��ޤä��褦�Ǥ���",$id);
}

# big�޷⡩��
sub logEiseiBigcome { #0
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<B>�޷����</B>��${HtagName_}${name}${H_tagName}�˸����äƤ���${HtagDisaster_}�������${H_tagDisaster}������Ȥ����褦�Ǥ�����",$id);
}

# �޷⡩��
sub logEiseicome { #0
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<B>�޷����</B>��${HtagName_}${name}${H_tagName}�˸����äƤ���${HtagDisaster_}���${H_tagDisaster}������Ȥ����褦�Ǥ�����",$id);
}

# �������ǡ���
sub logEiseiEnd { #4
	my($id, $name, $tEiseiname) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<B>$tEiseiname</B>��${HtagDisaster_}����${H_tagDisaster}�����褦�Ǥ�����",$id);
}

# �������
sub logUmlimit { #1
	my($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>��<B>����</B>��${HtagDisaster_}���${H_tagDisaster}����Ƥ��ޤä��褦�Ǥ���",$id);
}

# ��������ﳲ
sub logUmlimitDamage { #1
	my($id, $name, $mName, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��<B>$mName</B>��${HtagDisaster_}�������줿���ͥ륮��${H_tagDisaster}�ˤ����Ǥ��ޤ�����",$id);
}

# ���ꥨ��Υ���åȡ�
sub logUrieruMeteo { #1
	my($id, $name, $lName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>�������󤻤�${HtagDisaster_}�����${H_tagDisaster}��${HtagName_}$tPoint${H_tagName}��<B>$tName</B>��������Ӥ����Ǥ��ޤ�����",$id, $tId);
}

# �������Ϥ����⤹��
sub logFuneAttack { #1
	my($id, $name, $lName, $point, $tName, $tPoint) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��¿��Ƭ�ߥ������ȯ�ͤ���${HtagName_}$tPoint${H_tagName}��<B>$tName</B>��̿�椷�ޤ�����",$id, $tId);
}

# �ᥫ�ι���
sub logMekaAttack { #4
	my($id, $name, $lName, $point, $tName, $tPoint, $kind, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��ȯ�ͤ���$kind��${HtagName_}$tPoint${H_tagName}��<B>$tName</B>�����Ƥ�$str�ޤ�����",$id, $tId);
}

# �峤�����ޤ줿
sub logRottenSeaBorn { #2
	my($id, $name, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>���</B>����<B>�峤</B>�����ޤ�ޤ�����",$id);
}

# æ�餷�Ƥߤ�
sub logNuginugi { #1
	my($id, $name, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>���</B>��æ�餷�ޤ�����",$id);
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
    my($id, $tId, $name, $tName, $comName, $tLname, $point, $tPoint, $str) = @_;
    logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$tPoint${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ���<B>$tLname</B>��̿�桢<B>$tLname</B>��$str",$id, $tId);
}

# �졼��������
sub logLzrFail { #3
    my($id, $tId, $name, $tName, $comName, $tPoint) = @_;
    logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}$tPoint${H_tagName}�����˸�����${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ��������ɱһ��ߤˤ�����ޤ�����",$id, $tId);
}

# �����ɸ�
sub logMonsSend { #1
	my($id, $tId, $name, $tName , $mName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<B>${mName}</B>���¤��${HtagName_}${tName}${H_tagName}�����ꤳ�ߤޤ�����",$id, $tId);
}

# �����ɸ� ����
sub logSecretMonsSend { #1
	my($id, $tId, $name, $tName , $mName) = @_;
	logSecret("${HtagName_}${name}${H_tagName}��<B>${mName}</B>��${HtagName_}${tName}${H_tagName}�����ꤳ�ߤޤ�����",$id, $tId);
}


# �̤�Ʊ����������Ƥ���
sub logLeaderAlready {
	my($id, $name, $tName, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagName_}${tName}${H_tagName}��${HtagComName_}${comName}${H_tagComName}�ϡ����Ǥ˼�ʬ��Ʊ����������Ƥ��뤿����ߤ���ޤ�����",$id);
}

# �̤�Ʊ���˲������Ƥ���
sub logOtherAlready {
	my($id, $name, $tName, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagName_}${tName}${H_tagName}��${HtagComName_}${comName}${H_tagComName}�ϡ����Ǥ��̤�Ʊ���˲������Ƥ��뤿����ߤ���ޤ�����",$id);
}

# ����
sub logAlly {
	my($id, $tId, $name, $allyName) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagName_}${allyName}${H_tagName}�٤�${HtagNumber_}����${H_tagNumber}���ޤ�����", $id, $tId);
}

# æ��
sub logAllyEnd {
	my($id, $tId, $name, $allyName) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagName_}${allyName}${H_tagName}�٤���${HtagDisaster_}æ��${H_tagDisaster}���ޤ�����", $id, $tId);
}

# ͢��
sub logSell { #1
	my($id, $name, $comName, $value) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagFood_}$value$HunitFood${H_tagFood}��${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�����",$id);
}

# ���
sub logAid { #1
	my($id, $tId, $name, $tName, $comName, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagName_}${tName}${H_tagName}��$str��${HtagComName_}${comName}${H_tagComName}��Ԥ��ޤ�����",$id, $tId);
}

# �رĳ��ؤα�����Ե��ġ�
sub logAidFail {
	my($id, $tId, $name, $tName, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagName_}${tName}${H_tagName}�ؤ�${HtagComName_}${comName}${H_tagComName}�ϵ��Ĥ���Ƥ��ʤ�������ߤ��ޤ�����",$id, $tId);
}

# ����ػ�
sub logNotAvail {
	my($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}${comName}${H_tagComName}�ϵ��Ĥ���Ƥ��ʤ�������ߤ��ޤ�����",$id);
}

# Ͷ�׳�ư����ⷫ��(�����ȥ����Ȥ��Ƥޤ�)
sub logPropaganda { #4
	my($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagComName_}${comName}${H_tagComName}���Ԥ��ޤ�����",$id);
}

# ����
sub logGiveup { #1
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}���������졢<B>̵��${AfterName}</B>�ˤʤ�ޤ�����",$id);
	logHistory("${HtagName_}${name}${H_tagName}����������<B>̵��${AfterName}</B>�Ȥʤ롣");
}

# ���ε���������˺��
sub logSaveLoad { #5
	my($id, $name, $comName, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagComName_}${comName}${H_tagComName}$str",$id);
}

# ���ε���������˺�ѡ�����
sub logSaveLoadFail { #3
	my($id, $name, $comName) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagComName_}${comName}${H_tagComName}",$id);
}

# ���ε����ǡ����ü�
sub logSaveLoadVanish { #1
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}�ǡ����λ��Ԥ����������򵯤���${HtagDisaster_}���ε�����ä����ޤ�����${H_tagDisaster}",$id);
}

# �Хȥ�ե�����ɥ���������
sub logBF_SCORE { #1
	my($id, $name ,$score) = @_;
    my($va);
    $va = $score * $HBF_Point_Value;
	logOut("<b>�Хȥ�ե������</b>����${HtagName_}${name}${H_tagName}�ء�<B>${va}${HunitMoney}</B>�ξ޶⤬£���ޤ�����",$id);
}

# ����
sub logDead { #1
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}����ͤ����ʤ��ʤꡢ<B>̵��${AfterName}</B>�ˤʤ�ޤ�����",$id);
	logHistory("${HtagName_}${name}${H_tagName}���ͤ����ʤ��ʤ�<B>̵��${AfterName}</B>�Ȥʤ롣");
}

# ����(���Х��Х�⡼��)
sub logTDead { #1
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}�ϡ�<B>����</B>���׷���ʤ��ʤ�ޤ�����",$id);
	logHistory("${HtagName_}${name}${H_tagName}��<B>����</B>���롣");
}

# ����
sub logStarve { #1
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagDisaster_}��������­${H_tagDisaster}���Ƥ��ޤ�����",$id);
}

# �����ѡ���
sub logStarvefood { #1
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<B>�������ȴ�����ʪ</B>��${HtagDisaster_}������${H_tagDisaster}�����ä��褦�Ǥ�����",$id);
}

# ˦�ҡ���
sub logRotsick { #1
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<B>�峤</B>�����߽Ф���<B>˦��</B>��${HtagName_}${name}${H_tagName}��${HtagDisaster_}����${H_tagDisaster}��⤿�餷���褦�Ǥ�����",$id);
}

# ���¡���
sub logSatansick { #1
	my($id, $name) = @_;
	logOut("<B>�Ⲧ������</B>��${HtagName_}${name}${H_tagName}��<B>����</B>��${HtagDisaster_}����${H_tagDisaster}������${HtagName_}${name}${H_tagName}�Ǥ�${HtagDisaster_}����${H_tagDisaster}��ή�ԤäƤ���褦�Ǥ�����",$id);
}

# ���ø���
sub logMonsCome { #3
	my($id, $name, $mName, $point, $lName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<B>$mName</B>�и�����${HtagName_}$point${H_tagName}��<B>$lName</B>��Ƨ�߹Ӥ餵��ޤ�����",$id);
}

# ��������
sub logMonsFree { #1
	my($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>����������֤��ޤ�����",$id);
}

# ����ư��
sub logMonsMove { #1
	my($id, $name, $lName, $point, $mName , $msg) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��<B>$mName</B>$msg",$id);
}

# ���á��ɱһ��ߤ�Ƨ��
sub logMonsMoveDefence { #1
	my($id, $name, $lName, $point, $mName) = @_;
	logOut("<B>$mName</B>��${HtagName_}${name}$point${H_tagName}��<B>$lName</B>����ã��<B>${lName}�μ������֤���ư����</B>",$id);
}

# ���å��
sub logMonsWarp { #1
	my($id, $name, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>����$mName</B>���ä����ޤ�����",$id);
}

# ���äμ����Ϸ����
sub logMonsWarpLand { #2
	my($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>���и����ޤ�����",$id);
}

# ���饤�बʬ������
sub lognewMonsterBorn { #1
	my($id, $name, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>���饤��</B>��ʬ�����ޤ�����",$id);
}

# �����Ƥ��
sub lognewKaiju { #1
	my($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>����������ޤ�����",$id);
}

# ���á������Ǥ�
sub logMonsBomb { #1
	my($id, $name, $lName, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>��${HtagDisaster_}���ȥ�����${H_tagDisaster}�򵯤����������ޤ�����",$id);
}

# ���á���֤�Ƥ�
sub logMonsHelpMe { #1
	my($id, $name, $mName, $point) = @_;
	logOut("${HtagName_}${name}${point}${H_tagName}��<B>����$mName</B>��ŷ�˸����ä���Ӭ���ޤ�����",$id);
}

# ���ä���ȯ����
sub logMonsExplosion { #1
	my($id, $name, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>����$mName</B>��<B>����ȯ</B>�򵯤����ޤ�����",$id);
}

# ���á����Ϥ�Ƥ��Ԥ���
sub logMonsFire { #1
	my($id, $name, $lName, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��<B>$mName</B>�ˤ��׷��Ȥǲ��Ǥ��ޤ�����",$id);
}

# ���á����Ϥ�Ƥ��Ԥ���
sub logMonsFireS { #1
	my($id, $name, $lName, $point, $mName) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��<B>����$mName</B>���Ǥ��Ф�����ǾƤ��Ԥ�����ޤ�����",$id);
}

# ���á������Ƨ��
sub logMonsMine { #3
	my($id, $name, $lName, $point, $mName, $str) = @_;
	logOut("<B>����$mName</B>��${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��Ƨ�����ȯ��<B>����$mName</B>��$str",$id);
}

# ���á���������
sub logMonsMoneyStole {
	my($id, $name, $smoney, $mName) = @_;
	logOut("<B>����$mName</B>��${HtagName_}${name}${H_tagName}����${HtagDisaster_}${smoney}${HunitMoney}${H_tagDisaster}����ߤޤ�����",$id);

}

# ���á���������
sub logMonsMoneyStoleMiss {
	my($id, $name, $mName) = @_;
	logOut("<B>����$mName</B>��${HtagName_}${name}${H_tagName}���餪�����⤦�Ȼ�ߤޤ��������Ԥ����褦�Ǥ���",$id);

}

# ���á����������
sub logMonsFoodStole {
	my($id, $name, $sfood, $mName) = @_;
	logOut("<B>����$mName</B>��${HtagName_}${name}${H_tagName}���鿩��${HtagDisaster_}${sfood}${HunitFood}${H_tagDisaster}����ߤޤ�����",$id);

}

# ���á����������
sub logMonsFoodStoleMiss {
	my($id, $name, $mName) = @_;
	logOut("<B>����$mName</B>��${HtagName_}${name}${H_tagName}���鿩������⤦�Ȼ�ߤޤ��������Ԥ����褦�Ǥ���",$id);

}

# �к�
sub logFire { #1
	my($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��${HtagDisaster_}�к�${H_tagDisaster}�ˤ����Ǥ��ޤ�����",$id);
}

# �к�̤��
sub logFirenot { #1
	my($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��${HtagDisaster_}�к�${H_tagDisaster}�ˤ���ﳲ������ޤ�����",$id);
}

# ��¢��
sub logMaizo { #1
	my($id, $name, $comName, $value) = @_;
	logOut("${HtagName_}${name}${H_tagName}�Ǥ�${HtagComName_}$comName${H_tagComName}��ˡ�${HtagMoney_}$value$HunitMoney${H_tagMoney}���<B>��¢��</B>��ȯ������ޤ�����",$id);
}

# ���
sub logGold { #1
	my($id, $name, $comName, $value) = @_;
	logOut("${HtagName_}${name}${H_tagName}�Ǥ�${HtagComName_}$comName${H_tagComName}��ˡ�<B>���</B>��ȯ������${HtagMoney_}$value$HunitMoney${H_tagMoney}�����פ�������ޤ�����",$id);
}

# ��ϳ�
sub logGoldEnd { #1
	my($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>����⤬�Τ�ʤ��ʤä��褦�Ǥ���",$id);
}

# �Ͽ�ȯ��
sub logEarthquake { #2
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}���絬�Ϥ�${HtagDisaster_}�Ͽ�${H_tagDisaster}��ȯ������",$id);
}

# ������­�ﳲ
sub logSvDamage { #1
	my($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��<B>��������ƽ�̱������</B>��<B>$lName</B>�ϲ��Ǥ��ޤ�����",$id);
}

# ����ȯ��
sub logTsunami { #1
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}�ն��${HtagDisaster_}����${H_tagDisaster}ȯ������",$id);
}

# ����ȯ��
sub logTyphoon { #1
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagDisaster_}����${H_tagDisaster}��Φ����",$id);
}

# ��С��
sub logMeteo { #10
    my ($id, $name, $lName, $point, $str) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��${HtagDisaster_}���${H_tagDisaster}���$str�ޤ�����",$id);
}

# ��С�� 2
sub logMeteo2 {
    my ($id, $name, $lName, $point, $str , $metro) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��${HtagDisaster_}${metro}${H_tagDisaster}���$str�ޤ�����",$id);
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
	my($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��${HtagDisaster_}���${H_tagDisaster}���$str�ޤ�����",$id);
}

# ��С�����
sub logMeteoMonster { #2
	my($id, $name, $lName, $point) = @_;
	logOut("<B>$lName</B>������${HtagName_}${name}$point${H_tagName}������${HtagDisaster_}���${H_tagDisaster}�����Φ�Ϥ�<B>$lName</B>���Ȥ���פ��ޤ�����",$id);
}

# �������
sub logHugeMeteo { #2
	my($id, $name, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}������${HtagDisaster_}�������${H_tagDisaster}�������",$id);
}

# ʮ��
sub logEruption { #1
	my($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}������${HtagDisaster_}�л���ʮ��${H_tagDisaster}��<B>��</B>������ޤ�����",$id);
}

# ʮ�У�
sub logEruption2 { #3
	my($id, $name, $lName, $point, $str) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}������<B>$lName</B>�ϡ�${HtagDisaster_}ʮ��${H_tagDisaster}�αƶ���$str",$id);
}

# ��������ȯ��
sub logFalldown { #1
	my($id, $name) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${HtagDisaster_}��������${H_tagDisaster}��ȯ�����ޤ�������",$id);
}

# �����ﳲ�����ÿ���
sub logWideDamageMonsterSea { #1
	my($id, $name, $lName, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��Φ�Ϥ�<B>$lName</B>���Ȥ���פ��ޤ�����",$id);
}

# ����
sub logPrize { #10
	my($id, $name, $pName) = @_;
	logOut("${HtagName_}${name}${H_tagName}��<B>$pName</B>����ޤ��ޤ�����",$id);
	logHistory("${HtagName_}${name}${H_tagName}��<B>$pName</B>�����");
}

# ���ȼԤ��ǥ�
sub logUnemployedDemo { #1
	my($id, $name, $pop, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${str}<B>$pop${HunitPop}</B>���ǥ�Կʤ�Ԥ��ޤ�����",$id);
}

# ���ȼԤ�˽ư
sub logUnemployedRiot { #1
	my($id, $name, $lName, $pop, $point, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}��${str}<B>$pop${HunitPop}</B>��${HtagDisaster_}˽ư${H_tagDisaster}�򵯤�����${HtagName_}$point${H_tagName}������<B>$lName</B>��<B>����</B>��<B>$lName</B>�ϲ��Ǥ��ޤ�����",$id);
}

# ���ȼԤ���̱
sub logUnemployedMigrate { #1
	my($id, $tId, $name, $tName, $pop, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagName_}${tName}${H_tagName}��${str}<B>$pop${HunitPop}</B>�ΰ�̱�����夷�ޤ�����${HtagName_}${tName}${H_tagName}�ϲ����������줿�褦�Ǥ���",$id, $tId);
}

# ��̱���䡼��
sub logUnemployedReturn { #1
	my($id, $tId, $name, $lName, $tName, $pop, $str) = @_;
	logOut("${HtagName_}${name}${H_tagName}����${HtagName_}${tName}${H_tagName}��${str}<B>$pop${HunitPop}</B>�ΰ�̱�����夷�ޤ�������${HtagName_}${tName}${H_tagName}��<B>$lName</B>�ϼ����������ݤ����褦�Ǥ���",$id, $tId);
}

# �͸�����
sub logPopDecrease { #5
	my($id, $name, $lName, $tName, $str, $point) = @_;
	logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��${HtagDisaster_}${str}${H_tagDisaster}�ˤ��͸�������<B>$tName</B>�ˤʤ�ޤ�����",$id);
}

# ������Į���Ǥ���
sub logPlains2Town {
    my ($island, $lName, $point) = @_;

    my $id = $island->{'id'};
    #require './hako-io.cgi';
    my ($name) = islandName($island);

    logOut("${HtagName_}${name}$point${H_tagName}��<B>ʿ��</B>�˿�����<B>${lName}</B>���Ǥ��ޤ�����",$id);
}

# ����꤬ͽ����
sub logYakusho_Plains2 {
    my($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>������꤬<B>ͽ����</B>�ˤ��ޤ�����",$id);
}

# ����꤬���ʤ餷
sub logYakusho_Prepare {
    my($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>������꤬<B>ʿ��</B>�ˤ��ޤ�����",$id);
}

# ���ѥ������ޥ�
sub logSpiderMan {
    my($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>${lName}</B>��<B>���ѥ������ޥ���</B>�����졢�ӥ�β���ǿ�������ݤ������郎����ޤ�����",$id);
}

# ���äε��ݤˤ�뼺��
sub logBokuFail2 {
    my($id, $name, $comName, $kind, $point) = @_;
    logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���${HtagComName_}$comName${H_tagComName}�ϡ�ͽ����${HtagName_}$point${H_tagName}��<b>$kind</b>�������򤷤�������ߤ���ޤ�����",$id);
}

# ���
sub logFishing {
    my($id, $name, $lName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>${lName}</B>�Ǥϡ����̾�ͤ���ʪ�����夲���˥塼���ǻ�������Ǥ���",$id);
}

# ���ñۤ�����
sub logHikkosi_miss {
    my($id, $name) = @_;
    my($comName);
    $comName = $HcomName[$HcomBoku2];
    logOut("${HtagName_}${name}${H_tagName}��ͽ�ꤵ��Ƥ���<B>${comName}</B>�ϡ���Ū�Ϥ�Ŭ���ʤ����ᡢ���Ԥ��ޤ�����",$id);
}

# ���󥹥ȥա���
sub logFoodsute {
    my($id, $name, $fd , $money) = @_;
    #������λ�������ʤ��ʤä�����X�ȥ�ϡ�Y���ߤ˴��⤵��ޤ�����
    logSecret("${HtagName_}${name}${H_tagName}�λ�������ʤ��ʤä�����${HtagFood_}${fd}${HunitFood}${H_tagFood}��${HtagMoney_}${money}${HunitMoney}${H_tagMoney}�˴��⤵��ޤ�����",$id);
}

# �ա���
sub logGiveFoodUpdate {
    my($id, $sta, $update ) = @_;
    #������λ�������ʤ��ʤä�����X�ȥ�ϡ�Y���ߤ˴��⤵��ޤ�����
    logOut("<b>$sta</b>����$update�˥��åפ�����",$id);
}

# �����ƥ��ΤƤ�
sub logItemThrow {
    my($id, $name, $iName) = @_;
    logSecret("${HtagName_}${name}${H_tagName}��<B>${iName}</B>��ΤƤޤ�����",$id);
}

# �����ƥप����
sub logItemPuton {
    my($id, $name,$point, $iName ) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>${iName}</B>���֤��ޤ�����",$id);
}

# �����ƥब�ʤ�
sub logItemisNoting {
    my($id, $name) = @_;
    logOut("${HtagName_}${name}${H_tagName}�ϻ��äƤʤ������ƥ��Ȥ����Ȥ��ޤ�����",$id);
}

# �����ƥब�����ʤ�
sub logItemDeny {
    my($id, $name, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}�������ƥ���֤��Τ�Ŭ���ʤ����ᡢ���Ԥ��ޤ�����",$id);
}

# �������Ⱦ줷����
sub logSkateDown {
    my ($island, $landname, $x, $y) = @_;
    my ($point) = "($x,$y)";
    my ($id) = $island->{'id'};
    my ($name) = islandName($island);
    logOut("${HtagName_}${name}$point${H_tagName}��<B>${landname}</B>�ϡ�ɹ���Ȥ��Ƥʤ��ʤ�ޤ�����",$id);
}

# �Ƥ��ϴ�
sub logLavaAttack {
  my($id, $name, $mName, $point, $tName, $tPoint) = @_;
  logOut("${HtagName_}${name}$point${H_tagName}��<B>$mName</B>�θƤӵ�������${HtagDisaster_}�ϴ�${H_tagDisaster}��${HtagName_}$tPoint${H_tagName}��<B>$tName</B>��Ƥ��ޤ�����",$id, $tId);
}

# ����
sub logNige {
my($id, $name, $lName, $mName, $point) = @_;
logOut("${HtagName_}${name}$point${H_tagName}��<B>ưʪ��</B>����<B>$mName</B>��${HtagDisaster_}æ��${H_tagDisaster}���ޤ�����",$id);
}

# ���û�����
sub logSiire {
    my($id, $name, $lName, $mName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>��<B>$mName</B>�����٤��������Ǥ��ޤ���",$id);
END
}

# ���Ĥ���μ���
sub logOilMoney2 {
    my($id, $name, $lName, $point, $str, $str2) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>$lName</B>���顢<B>$str</B>�μ��פ��夬��ޤ�����(����<B>$str2</B>����)",$id);
END
}

# ����
sub logNige2 {
    my($id, $name, $lName, $mName, $point) = @_;
    logOut("${HtagName_}${name}$point${H_tagName}��<B>ưʪ��</B>����<B>$mName</B>��${HtagDisaster_}æ��${H_tagDisaster}�����ޤ�����",$id);
}

1;
