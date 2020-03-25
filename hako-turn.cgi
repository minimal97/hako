#----------------------------------------------------------------------
# Ȣ����� ver2.30
# ������ʹԥ⥸�塼��(ver1.02)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# Hakoniwa R.A. ver1.11
# �ᥤ�󥹥���ץ�(Ȣ����� ver2.30)
# ���Ѿ�������ˡ���ϡ�read-renas.txt�ե�����򻲾�
#
# KEI PAGE: http://www5b.biglobe.ne.jp/~k-e-i/
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# ���
#----------------------------------------------------------------------
    # ���ϣ��إå����κ�ɸ
    @ax = (0,1,1,1,0,-1,0,1,2,2,2,1,0,-1,-1,-2,-1,-1,0,2,2,3,3,3,2,2,1,0,-1,-2,-2,-3,-2,-2,-1,0,1,2,3,3,4,4,4,3,3,2,1,0,-1,-2,-2,-3,-3,-4,-3,-3,-2,-2,-1,0,1,3,3,4,4,5,5,5,4,4,3,3,2,1,0,-1,-2,-3,-3,-4,-4,-5,-4,-4,-3,-3,-2,-1,0,1,2,3,4,4,5,5,6,6,6,5,5,4,4,3,2,1,0,-1,-2,-3,-3,-4,-4,-5,-5,-6,-5,-5,-4,-4,-3,-3,-2,-1,0,1,2,4,4,5,5,6,6,7,7,7,6,6,5,5,4,4,3,2,1,0,-1,-2,-3,-4,-4,-5,-5,-6,-6,-7,-6,-6,-5,-5,-4,-4,-3,-2,-1,0,1,2,3,4,5,5,6,6,7,7,8,8,8,7,7,6,6,5,5,4,3,2,1,0,-1,-2,-3,-4,-4,-5,-5,-6,-6,-7,-7,-8,-7,-7,-6,-6,-5,-5,-4,-4,-3,-2,-1,0,1,2,3);
    @ay = (0,-1,0,1,1,0,-1,-2,-1,0,1,2,2,2,1,0,-1,-2,-2,-3,-2,-1,0,1,2,3,3,3,3,2,1,0,-1,-2,-3,-3,-3,-4,-3,-2,-1,0,1,2,3,4,4,4,4,4,3,2,1,0,-1,-2,-3,-4,-4,-4,-4,-5,-4,-3,-2,-1,0,1,2,3,4,5,5,5,5,5,5,4,3,2,1,0,-1,-2,-3,-4,-5,-5,-5,-5,-5,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,6,6,6,6,6,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-6,-6,-6,-6,-6,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,7,7,7,7,7,7,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-7,-7,-7,-7,-7,-7,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,8,8,8,8,8,8,8,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-8,-8,-8,-8,-8,-8,-8);

    @Htowns = ($HlandTown, $HlandProcity, $HlandMinato,
               $HlandFrocity, $HlandNewtown, $HlandBigtown, $HlandBettown, $HlandUmicity, $HlandOilCity,
               $HlandOnsen, $HlandRizort, $HlandBigRizort, $HlandShuto, $HlandUmishuto,
               $HlandSeatown, $HlandSeacity, $HlandInaka);

    @Htowns_CrimeLine = ($HlandBigtown,$HlandBettown,$HlandUmicity,$HlandOilCity,$HlandShuto, $HlandUmishuto,$HlandSeatown, $HlandSeacity);

    @Hseas = ($HlandSea, $HlandSbase, $HlandSeacity, $HlandSeatown, $HlandIce, $HlandFrocity, $HlandUmishuto, $HlandFune, $HlandUmiamu, $HlandOil, $HlandNursery);

    #----------------------------------------
    # �ҳ�
    #----------------------------------------
    # ���ϡ�������Ψ(�̾�򣱤Ȥ��������Ф�����Ψ%)
    # �����Ƴ�������hako-init.cgi
    # 0:����ʤ�              0, 1��, 2��, 3��, 4��, 5��, 6��, 7��, 8��, 9��,10��,11��,12��
    @Hfood1Incom        = ( 100,  80,  80,  80, 100, 100, 100, 100, 100, 100, 120, 120, 120); # ����(����)
    @Hfood2Incom        = ( 100, 100, 100, 100, 100, 100, 100,  80,  80,  80, 120, 120, 120); # ����(����)
    @Hmoney1Incom       = ( 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100); # ���(����)
    @Hmoney2Incom       = ( 100, 100,  80, 120, 120, 100,  80, 120, 100, 100, 100, 100, 120); # ���(����)
    # ����������(�̾�򣱤Ȥ��������Ф�����Ψ%)
    @HeatenFoodS        = ( 100,  90,  90,  90, 100, 100, 100,  90,  80,  90, 150, 150, 150);

    # �̾�ҳ�ȯ��Ψ(��Ψ��0.1%ñ��)
    # 0:����ʤ�        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12��
    @HdisEarthquake = ( 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5); # �Ͽ�
    @HdisTsunami    = ( 5,15, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5); # ����
    @HdisTyphoon    = ( 6, 1, 1, 1, 2, 3, 5, 7, 8, 9, 9, 5, 2); # ����
    @HdisMeteo      = ( 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6); # ���
    @HdisHugeMeteo  = ( 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1); # �������
    @HdisEruption   = ( 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5); # ʮ��
    @HdisFire       = ( 5, 9, 9, 8, 7, 5, 3, 2, 1, 1, 1, 2, 5); # �к�
    $HdisMaizo      = 15 ; # ��¢��

    # ��������
    $HdisFallBorder = 250; # �����³��ι���(Hex��)
    @HdisFalldown   = (15,15,15,15,15,15,15,15,15,15,15,15,15); # ���ι�����Ķ�������γ�Ψ


#----------------------------------------------------------------------
# include
#----------------------------------------------------------------------
require ('./hako-turn_log.cgi');     # �����ϥե�����
require ('./hako-turn_monster.cgi'); # ���ѥ��åƥ� ���ý�������ñۤ��Ƥ椯
require ('./hako-turn_food.cgi');
require ('./hako-turn_land.cgi');
require ('./hako-trade.cgi');

#use strict;
#use warnings;
use LWP::Simple;

#----------------------------------------------------------------------
# static
#----------------------------------------------------------------------
my ($HnoDisFlag);
my ($HflagKai);           # ����������
my ($InoraParkEvent) = 0;
my ($Hyosengameend) = 0;

my ($Appearance_monster) = "none";


my (@order);
#----------------------------------------------------------------------


#----------------------------------------------------------------------
# ������ʹԥ⡼��
#----------------------------------------------------------------------
# �ᥤ��
sub turnMain {
    # ���ַ��
    my (@line,$sepTurn);
    $HsepTurnFlag = 0;
    $InoraParkEvent = 0;            #���Τ���ɤΥ��٥��
    $sepTurn = $HsepTurn;
    $HDayEvent_Edge = 0;

    $Appearance_monster = "none";

    if (!$HsepTurn || $HsepTurn >= $HislandNumber) {

        @order = randomArray($HislandNumber);
        $sepTurn = $HislandNumber;
    }
    else {

        $HsepTurnFlag = 1;
        unless (-e "${HdirName}/septurn.cgi") {

            @order = randomArray($HislandNumber);
            if (!open(SOUT, ">${HdirName}/septurn.cgi")) {

                unlock();
                tempProblem();
                exit(0);
            }

            my ($c) = 0;
            foreach (@order) {
                $c++;
                print SOUT $_;
                if (   ($c % $HsepTurn == 0)
                    || ($c == $HislandNumber)  ) {
                    print SOUT "\n";
                }
                else {
                    print SOUT ",";
                }
            }
            close(SOUT);
        }

        if (!open(IN, "${HdirName}/septurn.cgi")) {
            unlock();
            tempProblem();
            exit(0);
        }

        @line = <IN>;
        close(IN);
        if ($line[0] ne '') {

            chomp($line[0]);
            @order = split(',', $line[0]);
            close(IN);
            $rest = $#order + 1;
            $sepTurn = $rest if($HsepTurn > $rest);
            if (!open(SOUT, ">${HdirName}/septurn.cgi")) {

                unlock();
                tempProblem();
                exit(0);
            }
            shift(@line);
            print SOUT join('', @line);
            close(SOUT);
        }
        else {
            unlink("${HdirName}/septurn.cgi");
            $HsepTurnFlag = 0;
            $sepTurn = 0;
        }
    }

    $HislandLastTime += $HunitTime;    # �ǽ��������֤򹹿�

    $HislandTurn++;             # �������ֹ�

    my ($i, $j);

    # ��ɸ�������
    makeRandomPointArray();

    # Hakoniwa Cup��
    unlink("${HdirName}/hakojima.lhc") if ((-e "${HdirName}/hakojima.lhc") && !($HislandTurn % 100));

    CalcNoDisFlag();        #  �ҳ�̵ͭ����

    # ����������ե�����
    for ($i = 0; $i < $sepTurn; $i++) {

        # �����󳫻����Υݥ���ȡ���⡢�͸������
        $Hislands[$order[$i]]->{'oldPts'}   = $Hislands[$order[$i]]->{'pts'};
        $Hislands[$order[$i]]->{'oldMoney'} = $Hislands[$order[$i]]->{'money'};
        $Hislands[$order[$i]]->{'lastFood'} = $Hislands[$order[$i]]->{'food'};
        $Hislands[$order[$i]]->{'oldPop'}   = $Hislands[$order[$i]]->{'pop'};
        $Hislands[$order[$i]]->{'lastarea'} = $Hislands[$order[$i]]->{'area'};
        $Hislands[$order[$i]]->{'missileAlert'} = 0;    # �����ǥߥ�����������������

        # �Ƽ���ͤ�׻�
        estimate($order[$i]);
        next if ($Hislands[$order[$i]]->{'predelete'});

        income($Hislands[$order[$i]]); # �����ե�����
        $Hislands[$order[$i]]->{'ally_turn'}++ if ($Hislands[$order[$i]]->{'ally_turn'} < 50);
    }

    # ��ǰ�����٥��
    DayEvent();

    # ���ޥ�ɽ���
    my ($island);
    for ($i = 0; $i < $sepTurn; $i++) {

        $island = $Hislands[$order[$i]];
        $island->{'missiled'} = 0;
        next if ($island->{'predelete'});
        # �����1�ˤʤ�ޤǷ����֤�
        while (!doCommand($island)){};
        # ���ϥ�(�ޤȤ�ƥ�����)
        logMatome($island, $HlogOmit2, 'seichi') if ($HlogOmit2);
        logHikkosi_miss( $island->{'id'} , islandName($island)) if ($island->{'stockflag'} == 55);
    }

    TradeEvent();

    # ��Ĺ�����ñ�إå����ҳ�
    for ($i = 0; $i < $sepTurn; $i++) {

        HakoCup_TeamReset($Hislands[$order[$i]]);
        next if($Hislands[$order[$i]]->{'predelete'});  #���������������Ф�
        $HflagKai = 0;
        doEachHex($Hislands[$order[$i]]);
    }

    # ������ؤ��������Ƥ��ɤ߹���
    readPunishData();

    my ($remainCampNumber);
    if ($HarmisticeTurn) {
        # �رľ���Ƚ��
        $remainCampNumber = $HallyNumber;
        if ($HcampDeleteRule) {

            my ($threshold) = 100 / $HallyNumber / 2;
            for ($i=0; $i<$HallyNumber; $i++) {
                if ($Hally[$i]->{'occupation'} < $threshold) {
                    islandDeadAlly('', $Hally[$i]->{'id'}, $Hally[$i]->{'name'});
                    foreach (@{$Hally[$i]->{'memberId'}}){
                        $Hislands[$HidToNumber{$_}]->{'dead'} = 1;
                    }
                    $remainCampNumber--;
                    logCampDelete($Hally[$i]->{'name'});
                }
            }
        }
    }

    # �����ν��� �ҳ���
    for ($i = 0; $i < $sepTurn; $i++) {

        $island = $Hislands[$order[$i]];
        next if ($island->{'predelete'});
        doIslandProcess($order[$i], $island);
        if (   ($island->{'id'} <= 100)
            && ( !$island->{'BF_Flag'} )
                                         ) {
            doIslandunemployed($order[$i], $island) ;
        }
    }

    if (!$HsepTurnFlag) {
        my ($remainNumber) = $HislandNumber;
        @order = randomArray($HislandNumber) if ($HsepTurn);
        # �޴ط�������Ψ����
        foreach $i (0..$islandNumber) {
            $island = $Hislands[$order[$i]];
            doPrize($order[$i], $island) if (!$HsepTurn || $HsepTurn > $islandNumber);

            # ����Ƚ��
            if ($island->{'dead'}) {

                $island->{'pop'} = 0;
                $island->{'pts'} = 0;
                $island->{'field'} = 0;
                $remainNumber--;

            } elsif(   ($island->{'pop'} == 0)
                    && ($island->{'id'} <= 100)
                    && ( !$island->{'BF_Flag'} ) ) {

                OutAlly($island);
                $island->{'dead'} = 1;
                $island->{'pts'} = 0;
                $remainNumber--;
                # ���ǥ�å�����
                my ($tmpid) = $island->{'id'};
                $HidToNumber{$tmpid} = undef;
                logDead($tmpid, islandName($island));
                unlink("${HdirName}/${tmpid}.${HsubData}");
                unlink("${HdirName}/savedata.$tmpid") if (-e "${HdirName}/savedata.$tmpid");
            }
            else {

                $island->{'dead'} = 0;
            }
        }

        # Ranking��Ͽ
        makeRankingData();

        # Ȣ���å�
        if ( ($HislandTurn % 100) == 41) {
            my ($stsin) = '';
            my @HCislands = @Hislands;
            my @idx = (0..$#Hislands);
            @idx = sort { $Hislands[$a]->{'field'} <=> $Hislands[$b]->{'field'} ||
                          $Hislands[$a]->{'hcover'} <=> $Hislands[$b]->{'hcover'} ||
                          $Hislands[$b]->{'hcdata'}[3] <=> $Hislands[$a]->{'hcdata'}[3] ||
                          $Hislands[$b]->{'hcdata'}[4] <=> $Hislands[$a]->{'hcdata'}[4] ||
                          $Hislands[$a]->{'hcdata'}[5] <=> $Hislands[$b]->{'hcdata'}[5] ||
                          $Hislands[$b]->{'hcdata'}[6] <=> $Hislands[$a]->{'hcdata'}[6] ||
                          $Hislands[$b]->{'hcdata'}[7] <=> $Hislands[$a]->{'hcdata'}[7] ||
                          $Hislands[$a]->{'hcdata'}[8] <=> $Hislands[$b]->{'hcdata'}[8] ||
                          $a <=> $b } @idx;
            @HCislands = @HCislands[@idx];

            for ($i = 0; $i < 8; $i++) {
                my ($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $HCislands[$i]->{'eisei4'});
                if ($stshoka != 0) {
                    $stshoka = 6;
                    $HCislands[$i]->{'eisei4'} = "$sto,$std,$stk,$stwin,$stdrow,$stlose,$stwint,$stdrowt,$stloset,$styusho,$stshoka";
                    $stsin .= islandName($HCislands[$i]) . "��";
                }
            }
            logHCsin($id, $name, $stsin) if ($stsin ne '');
        }

        # �ݥ���Ƚ�˥�����
        islandSort('pts', 1);

        # �����¿�͸���Ͽ����
        islandReki();

        # ���������оݥ�������ä��顢���ν���
        if (   !($HislandTurn % $HturnPrizeUnit)
            || (zorome($HislandTurn) ) ) {

            my ($island) = $Hislands[$HbfieldNumber];
            my ($value, $str);

            $value = $HislandTurn + random(1001);
            $island->{'money'} += $value;
            logPrizet($island->{'id'}, islandName($island), "$HislandTurn${Hprize[0]}", "$value$HunitMoney");

            # ���¤Τ��פ�
            Sinden_Omaturi($island , $HislandTurn , 1001);

            # ���ҤΤ��פ�
            Jinja_Omaturi($island , $HislandTurn , 1001);

            my ($prize1, $prize2) = split(/\t/, $island->{'prize'});
            $prize1 .= "${HislandTurn},";
            $island->{'prize'} = "$prize1\t$prize2";
        }

        # ������å�
        $HislandNumber = $remainNumber;
        $islandNumber = $remainNumber - 1;

        if ($HallyNumber) { # Ʊ����Ϣ����

            # �رĥ��å�(���ǥ롼��)
            $HallyNumber = $remainCampNumber if ($HarmisticeTurn);
            for ($i = 0; $i < $HallyNumber; $i++) {

                $Hally[$i]->{'score'} = 0;
                # �ݻ���(���ʤ��ʤä��礬���äƤ⤤������Ƭ���ǽ���)
                my ($keepCost) = int($HcostKeepAlly / $Hally[$i]->{'number'}) if($Hally[$i]->{'number'});
                $Hally[$i]->{'number'} = 0;
                my ($allyMember) = $Hally[$i]->{'memberId'};
                foreach (@$allyMember) {

                    my ($no) = $HidToNumber{$_};
                    if (defined $no) {

                        $Hally[$i]->{'score'} += $Hislands[$no]->{'pts'};
                        $Hally[$i]->{'number'}++;
                        # �ݻ���ħ��
                        $Hislands[$no]->{'money'} -= $keepCost  if(!$HarmisticeTurn);;
                        $Hislands[$no]->{'money'} = 0 if($Hislands[$no]->{'money'} < 0);
                        # �׸���(�͸��ʤ�1���ͤˤĤ�1�ݥ����)
                        $Hislands[$no]->{'ext'}[1] += int($island->{'pop'}/10);
                    }
                }
                $Hally[$i]->{'Takayan'} = makeRandomString();
            }
            allyOccupy();
            allySort();
        }

        # ��λ����Ƚ��
        GameOver_wrap();

        # Hakoniwa Cup���ť�
        logHC($id, $name, $Hstsanka) if (!($HislandTurn % 100) && $Hstsanka);

        # BF����
        if ( !($HislandTurn % 100) ) {
            my ($i);
            my ($max_point) = -1;
            my ($land_id) = -1;

            # �����ν���
            for ($i = 0; $i < $sepTurn; $i++) {
                $island = $Hislands[$order[$i]];
                $island->{'tha_point'} = $island->{'pts'};      # 100������

                if ($island->{'predelete'}) {
                    $island->{'landscore'} = 0;
                    next;
                }
                if ( $island->{'landscore'} ) {

                    if (   ($max_point == -1)                       # ���
                        || ($max_point < $island->{'landscore'} )   # �����⤤
                        || (   ($max_point < $island->{'landscore'} )  
                            && ($Hislands[$order[$land_id]]->{'pts'} > $island->{'pts'} ) ) ) {

                        $max_point = $island->{'landscore'};
                        $land_id = $island->{'id'};
                    }

                    $island->{'money'} += ($island->{'landscore'} * $HBF_Point_Value);
                    logBF_SCORE($island->{'id'}, islandName($island) , $island->{'landscore'});
                    $island->{'landscore'} = 0 ;
                }
            }

            my ($presentID) = $land_id;
            ItemPresent($Hislands[$HidToNumber{$presentID}] , $HlandOmamori , 84);
        }

        # �����ν���
        for ($i = 0; $i < $sepTurn; $i++) {
            my ($max_point) = -1;
            my ($land_id) = -1;

            $island = $Hislands[$order[$i]];
            next if($island->{'predelete'});

            if ( $island->{'landscore'} ) {

                if (   ($max_point == -1 )                      # ���
                    || ($max_point < $island->{'landscore'} )   # �����⤤
                    || (   ($max_point < $island->{'landscore'} )  
                        && ( $Hislands[$order[$land_id]]->{'pts'} > $island->{'pts'} ) ) ) {
                    $max_point = $island->{'landscore'};
                    $land_id = $island->{'id'};
                }
            }
        }

        # �����ν��� ���������å�
        for ($i = 0; $i < $sepTurn; $i++) {

            $island = $Hislands[$order[$i]];
            next if($island->{'predelete'});
            weather_calc($island);
            food_product_check($island);
        }


        CivReqestEvent();

        # ���ڡ����ǥ֥� ��������
        CalcSpaceDebri();

        # ----------------------------------------------------------------------
        # �Хå����åץ�����Ǥ���С�������rename
        if (!($HislandTurn % $HbackupTurn)) {

            my ($i);
            my ($tmp) = $HbackupTimes - 1;
            myrmtree("${HdirName}.bak$tmp");
            for ($i = $tmp; $i > 0; $i--) {

                my ($j) = $i - 1;
                rename("${HdirName}.bak$j", "${HdirName}.bak$i");
            }
            rename("${HdirName}", "${HdirName}.bak0");
            mkdir("${HdirName}", $HdirMode);

            # ���ե�����򥳥ԡ�
            for ($i = 0; $i <= $HlogMax; $i++) {

                copy("${HdirName}.bak0/hakojima.log$i", "${HdirName}/hakojima.log$i") if(-e "${HdirName}.bak0/hakojima.log$i");
            }
            copy("${HdirName}.bak0/hakojima.his", "${HdirName}/hakojima.his") if(-e "${HdirName}.bak0/hakojima.his");
            copy("${HdirName}.bak0/hakojima.lhc", "${HdirName}/hakojima.lhc") if(-e "${HdirName}.bak0/hakojima.lhc");
            copy("${HdirName}.bak0/rekidai.dat", "${HdirName}/rekidai.dat") if(-e "${HdirName}.bak0/rekidai.dat");
            copy("${HdirName}.bak0/$HtradeFile", "${HdirName}/$HtradeFile") if(-e "${HdirName}.bak0/$HtradeFile");

            # savedata(���ε���)������Х��ԡ�
            # ALLY����å�
            foreach $i (0..$islandNumber) {

                my ($island) = $Hislands[$i];
                copy("${HdirName}.bak0/savedata.$island->{'id'}", "${HdirName}/savedata.$island->{'id'}") if(-e "${HdirName}.bak0/savedata.$island->{'id'}");
                copy("${HdirName}.bak0/${HallychatDataName}$island->{'id'}.cht", "${HdirName}/${HallychatDataName}$island->{'id'}.cht") if(-e "${HdirName}.bak0/${HallychatDataName}$island->{'id'}.cht");
            }

            if ($HsepTurn) {
                rename("${HdirName}.bak0/secret.tmp", "${HdirName}/secret.tmp");
                rename("${HdirName}.bak0/late.tmp", "${HdirName}/late.tmp");
                rename("${HdirName}.bak0/log.tmp", "${HdirName}/log.tmp");
            }
        }

        # �ե�����˽񤭽Ф�
        writeIslandsFile(-1);

        # ���ե��������ˤ��餹
        LogFileSlide();

        PerformanceLog();   #    ��ٷ�¬

        if (   ($HsepTurn)
            && ($HsepTurn < $HislandNumber) ) {

            my (@tmpSecretLogPool, @tmpLateLogPool, @tmpLogPool);

            open(LIN, "${HdirName}/secret.tmp");
            @tmpSecretLogPool = <LIN>;
            chomp(@tmpSecretLogPool);
            close(LIN);
            unlink("${HdirName}/secret.tmp");

            open(LIN, "${HdirName}/late.tmp");
            @tmpLateLogPool = <LIN>;
            chomp(@tmpLateLogPool);
            close(LIN);
            unlink("${HdirName}/late.tmp");

            open(LIN, "${HdirName}/log.tmp");
            @tmpLogPool = <LIN>;
            chomp(@tmpLogPool);
            close(LIN);
            unlink("${HdirName}/log.tmp");

            @HsecretLogPool = (@tmpSecretLogPool, @HsecretLogPool);
            @HlateLogPool = (@tmpLateLogPool, @HlateLogPool);
            @HlogPool = (@tmpLogPool, @HlogPool);
        }

        logFlush();             # ���񤭽Ф�
        logHistoryTrim();       # ��Ͽ��Ĵ��
#       logHcupTrim();# ������ɽ���Τ��ᥫ�å�
        MakeHtmlLog();

        # �ȥåפ�
        require('./hako-top.cgi');
        topPageMain();
    }
    else {

        for ($i = 0; $i < $sepTurn; $i++) {
            $island = $Hislands[$order[$i]];
            doPrize($order[$i], $island);

            # ����Ƚ��
            if ($island->{'dead'}) {
                $island->{'pop'} = 0;
                $island->{'pts'} = 0;
                $island->{'field'} = 0;
            }
        }
        # �ǽ��������֤򹹿�
        $HislandLastTime -= $HunitTime;
        # �������ֹ�
        $HislandTurn--;
        # �ե�����˽񤭽Ф�
        writeIslandsFile(-1);

        PerformanceLog();       #    ��ٷ�¬

        # tmp���񤭽Ф�
        tempLogFlush();
        MakeHtmlLog();

        {
            my ($all) = $HislandNumber / $HsepTurn + 1;
            $all = ($all == int($all)) ? $all : int($all) + 1;
            my ($count) = $all - $#line - 2;
            tempRefresh($Hrefresh, "�����󹹿���(${count}/${all})<BR>���Τޤޤ��Ф餯���Ԥ���������");
        }
    }

    {
        if (!(DEBUG_MODE)) {
            my ($url) = 'http://localhost:8123/hako/hakoniwa_bot.php?turn=';
            if ($Appearance_monster eq "none") {
                $url = "$url$HislandTurn&monster=-1";

            }
            else {
                $url = "$url$HislandTurn&monster=$Appearance_monster";

            }
            # LWP::Simple�Ρ�get�״ؿ������

            my ($html) = get("$url") or die "";
        }
    }
}



#----------------------------------------------------------------------
#
#   ��̱���׵�
#

sub CivReqestEvent {

    my ($i);
    my ($island);
    my ($id);

    # �����ν���
    for ($i = 0; $i < $HislandNumber; $i++) {

        $island = $Hislands[$order[$i]];
        next if($island->{'predelete'});

        $id = $island->{'id'};

        if ($island->{'civreq'}) {

            $island->{'civreq_abs'}++;

            if ($island->{'civreq_abs'} > 8) {
                $island->{'civreq'} = 0;
                $island->{'civreq_abs'} = 0;
                logOut("debug:��̱�ϡ���˾������������ʤ��ä��Ȥ����ᤷ��Ǥ��ޤ������ǥХå�����ä����Ȥ˵��Ť��ƾФäƤ��ޤäƤ��ޤ���" , $id);
            }
        }
        else {

            $island->{'civreq_abs'} = 0;
            if (random(100) < 10){ 

                my ($req) = random($CivReqNum-1)+1;
                $island->{'civreq'} = $req;

                if ($CivReqkind[($req)] eq 'tax') {

                    $island->{'civreq_num'} = random(9);
                }
                else {
                    $island->{'civreq_num'} = random(20) + 10;
                }

                my ($unit) = $CivReqDispUnit[$req];
                logOut("debug:��̱����˾��Ф��ޤ�����:$CivReqDisp[$req] $island->{'civreq_num'}$CivReqDispUnit[$req]" , $id);
            }
        }

    }
}


#----------------------------------------------------------------------
#
#   ��󥭥󥰥ǡ���
#

sub makeRankingData {

    my ($i);

    # Ranking��Ͽ
    @HrankingID = ();
    foreach $i (0..$islandNumber) {

        my @hcdata = split(/,/, $Hislands[$i]->{'eisei4'});
        $Hislands[$i]->{'hcdata'} = \@hcdata;
        if ($hcdata[10] >= 10) {
            $Hislands[$i]->{'hcover'} = 1;
        }

        $Hislands[$i]->{'kachiten'} = $hcdata[3]*3 + $hcdata[4];
        $Hislands[$i]->{'kachitent'} = $hcdata[6]*3 + $hcdata[7];
        my ($siaisu) = $hcdata[6] + $hcdata[7] + $hcdata[8];
        $siaisu = 1 if($siaisu == 0);
        $Hislands[$i]->{'shoritu'} = int($hcdata[6] / $siaisu * 100);
        $Hislands[$i]->{'teamforce'} = $hcdata[0] + $hcdata[1] + $hcdata[2];
        $Hislands[$i]->{'styusho'} = $hcdata[9];

        my ($mshp, $msap, $msdp, $mssp) = (split(/,/, $Hislands[$i]->{'eisei5'}))[0..3];
        $Hislands[$i]->{'force'} = $mshp + $msap + $msdp + $mssp;

        foreach (split(/,/, $Hislands[$i]->{'eisei6'})) {
            # $Hislands[$i]->{'tuni'} += $_;
            $Hislands[$i]->{'uni'}++ if($_ > 0);
        }
    }

    my @elements   = ( 'pop'   , 'farm'  , 'factory', 'mountain'   , 'fore' ,
                       'tare'  , 'zipro' , 'leje'   , 'monsterlive', 'taiji',
                      'monta'  , 'hamu'  , 'pika'   , 'kei'        , 'rena' ,
                      'force'  , 'eisei2', 'uni'    , 'teamforce'  , 'styusho',
                      'shoritu', 'kachitent', 'kachiten' , 'tha_diff' , 'zoo_Mons_cnt' , 'factoryHT','area');

    my @islands;
    foreach (@elements) {
        $islands{$_} = islandSort($_);
        push(@HrankingID, $islands{$_}->{'id'});
    }
}


#----------------------------------------------------------------------
#
#   ���ڡ����ǥ֥긺��
#
sub CalcSpaceDebri {

    $HSpace_Debris -= $HSpaceDebri_evapo;       # ���ڡ����ǥ֥� ��������

    if ($HSpace_Debris < 0 ) {

        $HSpace_Debris = 0;
    }
}


#----------------------------------------------------------------------
#
#   ���ե��������ˤ��餹
#
sub LogFileSlide {

    my ($i , $j , $s , $d);
    # ���ե��������ˤ��餹
    for ($i = ($HlogMax - 1); $i >= 0; $i--) {
        $j = $i + 1;
        $s = "${HdirName}/hakojima.log$i";
        $d = "${HdirName}/hakojima.log$j";
        unlink($d);
        rename($s, $d);
    }
}


#----------------------------------------------------------------------
#    ��ٷ�¬
##### �ɲ� ����20020307
#                       ���ư
sub PerformanceLog {
##### �ɲ� ����20020307
        if ($Hperformance) {
            my ($uti, $sti, $cuti, $csti) = times();
            $uti += $cuti;
            $sti += $csti;
            my ($cpu) = $uti + $sti;
#            ���ե�����񤭽Ф�(�ƥ��ȷ�¬�� ���ʤϥ����Ȥˤ��Ƥ����Ƥ�������)
#            open(POUT,">>cpu-t.log");
#            print POUT "CPU($cpu) : user($uti) system($sti)\n";
#            close(POUT);
            my ($timea) = sprintf("%.3f",Time::HiRes::time - $Hakoniwa_start_time);
            logLate("<small>��ٷ�¬[1] CPU($cpu) : user($uti) system($sti) t:$timea</small>",0);
        }
#####
}


#----------------------------------------------------------------------
#
#  �ҳ�̵ͭ����
#
sub CalcNoDisFlag {

    if (   ($HarmisticeTurn)
        && ($HislandTurn < $HarmisticeTurn) ) {

        $HnoDisFlag = 1;        # ������֤�̵�ҳ�
    }
    else {

        $HnoDisFlag = 0;        # �ҳ�����
    }
}


#----------------------------------------------------------------------
sub zorome {

    my ($num) = @_;
    my ($ret) = 0;

    my ($tar) = substr($num, 0, 1);
    my ($len) = length($num);

    if (   ($num > 1000)
        && ($num =~ /${tar}{$len}/)) {

        $ret = 1;
    }

    return ($ret);
}


#----------------------------------------------------------------------
sub MakeHtmlLog {

    if (HTML_LOG_MAKE) {
        if (-e "${HhtmlDir}/hakolog.html") {
            unlink("${HhtmlDir}/hakolog.html");
        }
    }
}


#----------------------------------------------------------------------
sub weather_calc {
    my ($island) = @_;

    my ($wet);
    my ($wet_old);
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $mon += 1;

    $wet_old = $island->{'weather'};

    temperature_calc($island);

    $wet = weather_role($HWeather_table[$mon][0],$HWeather_table[$mon][1],$HWeather_table[$mon][2]);

    if ($island->{'temperature'} < 3) {

        $wet = $HWeather_Snow;
    }

    if ($wet_old == $wet) {

        $island->{'weather_chain'}++;
    }
    else {

        $island->{'weather_chain'} = 1 ;
    }
    $island->{'weather'} = $wet;
    $island->{'weather_old'} = $wet_old;
}


#----------------------------------------------------------------------
# ŷ�������
#----------------------------------------------------------------------
sub weather_role {
    my ($sun , $clu , $rain) = @_;

    my ($sum) = $sun + $clu + $rain;
    my ($rand) = random($sum);

    if ($rand < $sun) {

        return 0;
    }
    elsif ($rand < $sun + $clu) {

        return 1;
    }
    else {

        return 2;
    }

    return 0;
}


#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub temperature_calc {
    my ($island) = @_;

    my ($ra);
    my ($sec,$dummy,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $mon += 1;

    my ($temp) = $island->{'temperature'};

    my ($max) = $HTemperatureMax[$mon];
    my ($ave) = $HTemperatureAve[$mon];
    my ($min) = $HTemperatureMin[$mon];

    if (random(100) > 50){

        $temp += random(4);
    }
    else {

        $temp -= random(4);
    }

    if (random(100) < 70){

        if ($temp < $ave) {

            $temp += random(2);
            $temp += random(3) if(random(100) < 10);
        }
        else {

            $temp -= random(2);
            $temp -= random(3) if(random(100) < 10);
        }
    }

    $temp = $max if ($temp > $max);
    $temp = $min if ($temp < $min);

    $island->{'temperature'} = $temp;
}

#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub DayEvent {

    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $mon += 1;

    #$HDayEvent = 0;

    if (($mon == 1) && ($mday == 1) ) {      # ����

        if (!$HDayEvent) {
            $HDayEvent = 1;

            my ($val) = (5) ; #���� HP5
            ItemPresent_ALL_island($HlandBigFood , $val ,  0, 0);
        }
    }
    elsif (isPockeyDay($mon , $mday)) {
        if (!$HDayEvent) {
            $HDayEvent = 1;
            $HDayEvent_Edge = 1;
        }
    }
    elsif (($mon == 2) && ($mday == 14)) {

        if (!$HDayEvent) {
            $HDayEvent = 1;

            my ($mKind) = 1 + (seqnum($HislandTurn) % 2);
            my ($val) = ($mKind << $Food_Kind_Shift) + (5) ; #���祳�졼�� HP5
            ItemPresent_ALL_island($HlandBigFood , $val ,  0, 0);
        }

    }
    elsif (($mon == 3) && ($mday == 3)) {

        if (!$HDayEvent) {
            $HDayEvent = 1;
            $HDayEvent_Edge = 1 + int($HislandNumber / 12);

            my ($mKind) = 1 + (seqnum($HislandTurn) % 2);
            my ($val) = (3 << $Food_Kind_Shift) + (5) ; #�Ҥ���� HP5
            ItemPresent_ALL_island($HlandBigFood , $val ,  0, 0);
        }

    }
    else {
        $HDayEvent = 0;
    }
}

#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub TradeEvent {

    my ($HtradeFile) = "trade.trd";

    open(IN, "<" , "${HdirName}/${HtradeFile}");
    my @lines = <IN>;
    close(IN);

    # �񤭹��ߤȥ��٥��
    my ($data);
    open(OUT, ">" , "${HdirName}/${HtradeFile}");
    chomp($lines[0]);
    print OUT "$lines[0]\n";

    for ($i = 1 ; $i < (@lines) ; $i++) {

        $data = TradeDataConv($lines[$i]);

        doTrade($data);

        if ($data->{'absent'} < 12) {

            print OUT TradeDataToStr($data);
        }
    }
    close(OUT);
}


#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub doTrade {
    my ($data) = @_;

    if (   ($data->{'check1'} == 1)
        && ($data->{'check2'} == 1) ) {

        $data->{'absent'} = 0;

        # --------

        my ($island1_id , $island2_id);
        my ($island1 , $island2);
        my ($island_pay_m , $island_pay_obj);

        $island1_id = $data->{'island1_id'};
        $island2_id = $data->{'island2_id'};

        # �����ǽ�������å�
        $island1 = $Hislands[$HidToNumber{$island1_id}];
        $island2 = $Hislands[$HidToNumber{$island2_id}];

        unless ($island1->{'trade_max'} > $island1->{'trade_cnt'}) {
            logOut("����������¤Ǽ���Ǥ��ޤ���Ǥ�����" , $island1_id);
            logOut("����������¤Ǽ���Ǥ��ޤ���Ǥ�����" , $island2_id);
            return ;
        }
        unless ($island2->{'trade_max'} > $island2->{'trade_cnt'}) {
            logOut("����������¤Ǽ���Ǥ��ޤ���Ǥ�����" , $island1_id);
            logOut("����������¤Ǽ���Ǥ��ޤ���Ǥ�����" , $island2_id);
            return ;
        }

        # ����
        if ($data->{'payside'}) {
            $island_pay_m = $island1;
        }
        else {
            $island_pay_m = $island2;
        }

        if ($island_pay_m->{'money'} < $data->{'money'}) {
            logOut("�����­�Τ��ᡢ������Ǥ��ޤ���Ǥ�����" , $island1_id);
            logOut("�����­�Τ��ᡢ������Ǥ��ޤ���Ǥ�����" , $island2_id);
            return ;
        }

        # ���֥���
        if ($data->{'objside'}) {
            $island_pay_obj = $island1;
        }
        else {
            $island_pay_obj = $island2;
        }

        # --------

        my ($name) = islandName($island2);
        logOut("debug:${HtagName_}$name${H_tagName}�Ȥμ�����Ԥ��ޤ�����" , $island1_id);
        my ($name) = islandName($island1);
        logOut("debug:${HtagName_}$name${H_tagName}�Ȥμ�����Ԥ��ޤ�����" , $island2_id);

        $island1->{'trade_cnt'}++;
        $island2->{'trade_cnt'}++;
    }
    else {

        $data->{'absent'} += 1;
    }
}


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
sub ItemPresent_ALL_island {
    my ($kind , $val , $val2 , $val3) = @_;

    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $mon += 1;

    my ($i);
    my ($island);
    my ($name);
    my ($ItemName);
    my ($mKind);
    # $ItemName = landName($kind, $val,$val2);
    # �����ν���
    for ($i = 0; $i < $HislandNumber; $i++) {

        $island = $Hislands[$i];
        $name = islandName($island);
        next if ($island->{'predelete'});
        next if ($island->{'BF_Flag'});

        if (   ($mon == 2)
            && ($mday == 14) ) {

            $mKind = 1 + (seqnum($i) % 2);
            $val = ($mKind << $Food_Kind_Shift) + (5) ; #���祳�졼�� HP5
            $ItemName = landName($kind, $val, $val2);
        }

        ItemPresent($island, $kind,$val);
        logOut("${HtagName_}${name}${H_tagName}��<B>$ItemName</B>�������ޤ�����",$island->{'id'} );
    }

}


#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub ItemPresent {
    my ($island, $itemland,$itemland_value) = @_;

    my ($i);
    my ($item);
    my ($item_lv);
    my ($item_lv2);
    my ($item_lv3);
    my ($item_ret);

    $item     = $island->{'item_land'};
    $item_lv  = $island->{'item_landValue'};
    $item_lv2 = $island->{'item_landValue2'};
    $item_lv3 = $island->{'item_landValue3'};
    $item_ret = 0;

    for ($i = 0; $i < $HItem_MAX; $i++) {

        if ($item->[$i] == $HItem_Nothing ) {

            $item_ret = 1;
            $item->[$i] = $itemland;
            $item_lv->[$i] = $itemland_value;
            $item_lv2->[$i] = 0;
            $item_lv3->[$i] = 0;
            last;
        }
    }

    return $item_ret;
}


#----------------------------------------------------------------------
# ��λ���ɤ���
#----------------------------------------------------------------------
sub GameOver_wrap {

    # ��λ����Ƚ��
    my ($n) = gameOver();
    if (   ($HarmisticeTurn)
        && ($HislandTurn <= $HgameLimitTurn)
        && ($n != -1)) {

        logHistory("${HtagName_}${Hally[$n]->{'name'}}${H_tagName}��<B>����</B>���ޤ�����");
        $Hally[$n]->{'name'} = '�ھ��ԡ���' . $Hally[$n]->{'name'};
        $HplayNow = 0;
    }
}

#----------------------------------------------------------------------
# ��λ���ɤ���
#----------------------------------------------------------------------
sub gameOver {
    # �����ڤ�
    if ($HgameLimitTurn) {
        if ($HislandTurn >= $HgameLimitTurn) {
            # �ȥåפοرĤ򤫤���
            return 0;
        }
    }
    # �������
    my ($i);
    for ($i = 0; $i < $HallyNumber; $i++) {
        if ($Hally[$i]->{'occupation'} >= $HfinishOccupation) {
            #return $i;
        }
    }
    return -1;
}


#----------------------------------------------------------------------
# ������ؤ��������Ƥ��ɤ߹���
#----------------------------------------------------------------------
sub readPunishData {

    if (open(Fpunish, "<${HdirName}/punish.dat")) {

        local(@_);
        my ($island);
        while (<Fpunish>) {
            chomp;
            @_ = split(',');
            my($obj);
            $obj->{id} = shift;
            $obj->{punish} = shift;
            $obj->{x} = shift;
            $obj->{y} = shift;
            $HpunishInfo{$obj->{id}} = $obj;
        }
        close(Fpunish);
    }
    # ���ۥǡ�����������
    unlink("${HdirName}/punish.dat");
}


#----------------------------------------------------------------------
# ̤����
#----------------------------------------------------------------------
sub tempRefresh {
    my ($delay, $str) = @_;
    my ($next) = $HislandTurn + 1;
        out(<<END);
<meta http-equiv='refresh' content='$delay; url="$HthisFile?UNLOCK=$HsepTurnFlag"'>
<h1><small>������</small> ${HislandTurn} => ${next}</h1>
<h2>$str</h2>
END
}


#----------------------------------------------------------------------
# ����������ե�����
#----------------------------------------------------------------------
sub income {
    my ($island) = @_;
    my ($pop, $farm, $factory, $mountain, $factoryHT , $park_work) =
    (
        $island->{'pop'},
        $island->{'farm'} * 10,
        $island->{'factory'},
        $island->{'mountain'},
        $island->{'factoryHT'},
        $island->{'park_work'}
    );
    my ($co0) = $island->{'co0'};            # ��ؤθ���
    my ($co1) = $island->{'co1'};            # ��ؤθ���

    $island->{'farmer'} = 0;
    $island->{'business'} = 0;

    if ($island->{'effect'} & $g_Island_Retro) {
        $factoryHT = 0;
        $factory = $island->{'park_work'};
    }

    # ����
    if ($pop > $farm) {
        # ���Ȥ�������꤬;����
        Calc_Product_Food($island , $farm); # ����ե��Ư
        $island->{'money'} += int(min(int(($pop - $farm) / 10), $factory + $factoryHT + $mountain) * ($co1 + 1) * $Hmoney1Incom[0]/100);
        $island->{'farmer'} = 1;
        $island->{'business'} = 1;
    }
    else {
        # ���Ȥ����Ǽ���դξ��
        Calc_Product_Food($island , $pop);  # �������ɻŻ�
        $island->{'farmer'} = 1;
    }

    # ��������
    my ($foodkind);
    $foodkind = food_product_consumption($island , int($pop * $HeatenFood * $HeatenFoodS[0]/100) );
    # logOut("debug:��������:$foodkind" , $island->{'id'});
}


#----------------------------------------------------------------------
# food�λ���
#----------------------------------------------------------------------
sub Calc_Product_Food {
    my ($island , $pop) = @_;

    return if ($pop <= 0);

    my ($debug_pop);
    my ($debug_in) = "pop:$pop/";

    my ($co0) = ($island->{'co0'}) ? ($island->{'co0'}) : 0;            # �������
    $island->{'food'} += int($pop * ($co0 + 1) * $Hfood1Incom[0]/100);

    $debug_pop = int($pop * ($co0 + 1) * $Hfood1Incom[0]/100);

    my (%product_wk) = ();
    my ($product_num , $product_sum) = (0,0);
    {
        my ($product);
        foreach $product (@HProduct_Food_hash_table) {

            $product_wk{$product} = ($island->{$product . '_work'} * 10);
            $product_sum += ($island->{$product . '_work'}) ? ($island->{$product . '_work'}*10) : 0;
            $product_num += ($island->{$product . '_work'}) ? 1 : 0;
            $debug_in .="$product:($island->{$product . '_work'})/"
        }
    }

    return if ($product_num <= 0);

    my ($ave) = int($product_sum / $product_num);
    my ($woker) = 0;
    my ($val) = 0;

    my ($debug_prodct) = 0;

    for my $key (sort {$product_wk{$a} <=> $product_wk{$b}} keys %product_wk) {

        $val = ($product_wk{$key}) ? ($product_wk{$key}) : 0 ;
        next if ($val <= 0);

        $val = ($ave <= $val) ? $ave : $val;
        $woker = ($val <= $pop) ? $val : $pop;
        $woker = ($woker < 0) ? 0 : $woker;

        $island->{$key} += int($woker * ($co0 + 1) * $Hfood1Incom[0]/100);
        $debug_prodct += int($woker * ($co0 + 1) * $Hfood1Incom[0]/100);

        $product_sum -= $woker;
        $pop -= $woker;
        last if ($pop <= 0);

        $product_num--;
        next if ($product_num <= 0);

        $ave = int($product_sum / $product_num);
    }

    if ($debug_prodct != $debug_pop) {
        logOut("�����԰��ס�$debug_in" , $island->{'id'});
        logOut("�����԰��ס�$debug_pop / $debug_prodct" , $island->{'id'});
    }
}


#----------------------------------------------------------------------
# ���¤Τ��פ�
#----------------------------------------------------------------------
sub Sinden_Omaturi {
    my ($island,$base,$rand) = @_;

    if ($island->{'sin'} > 0) {
        my ($value);
        $value = $base + random($rand);
        $island->{'money'} += $value;
        logSinMoney($island->{'id'}, islandName($island), "$value$HunitMoney");
    }
}


#----------------------------------------------------------------------
# ���ҤΤ��פ�
#----------------------------------------------------------------------
sub Jinja_Omaturi {
    my ($island,$base,$rand) = @_;

    if ($island->{'jin'} > 0) {
        my ($value);
        $value = $base + random($rand);
        $island->{'money'} += $value;
        logJinMoney($island->{'id'}, islandName($island), "$value$HunitMoney");
    }
}


#----------------------------------------------------------------------
# ���ޥ�ɥե�����
#----------------------------------------------------------------------
sub doCommand {
    my ($island) = @_;
    # ���ޥ�ɼ��Ф�
    my ($comArray, $command);
    $comArray = $island->{'command'};
    $command = $comArray->[0]; # �ǽ�Τ���Ф�
    slideFront($comArray, 0); # �ʹߤ�ͤ��

    # �����Ǥμ��Ф�
    my($kind, $target, $x, $y, $arg) =
    (
        $command->{'kind'},
        $command->{'target'},
        $command->{'x'},
        $command->{'y'},
        $command->{'arg'}
    );

    # Ƴ����
    my ($name) = islandName($island);
    my ($id) = $island->{'id'};
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};
    my ($landKind) = $land->[$x][$y];
    my ($lv) = $landValue->[$x][$y];
    my ($lv2) = $landValue2->[$x][$y];
    my ($lv3) = $landValue3->[$x][$y];
    my ($cost) = $HcomCost[$kind];
    my ($comName) = $HcomName[$kind];
    my ($point) = "($x, $y)";
    my ($landName) = landName($landKind, $lv, $lv2, $lv3);

    if (   ($kind == $HcomDoNothing)
        && (   ($id <= 100)
            && (!$island->{'BF_Flag'}))) {
        # ��ⷫ��
#       logPropaganda($id, $name, $comName);
        $island->{'money'} += int(10 * $Hmoney1Incom[$Hmonth]/100);
        if ($HeasyMode) {
            $island->{'money'} += random(100);
            if (random(100) < 5) {
                my $value = 1+ random(1999);
                $island->{'money'} += $value;
                # ������
                logEnjo($id, $name, $landName, $point , "$value$HunitMoney") if ($value > 0);
            }
        }
        $island->{'absent'}++;

        # ��ư����
        if ($island->{'absent'} >= $HgiveupTurn) {
            $comArray->[0] = {
                'kind' => $HcomGiveup,
                'target' => 0,
                'x' => 0,
                'y' => 0,
                'arg' => 0
            }
        }
        return 1;
    }

    $island->{'absent'} = 0;        #��ⷫ������0��

    # ���ʻ���
    {
        my ($temp_cost);
        $temp_cost = $cost;
        if ($temp_cost =~ s/Pointx(.*)$//g) {
            $cost = $island->{'pts'} * int($1);
        }
        else {
            $cost = $temp_cost;
        }
    }

    if (   ($kind != $HcomGivefood)
        && ($kind != $HcomSell)
        && ($kind != $HcomSave)
        && ($kind != $HcomLoad)
        && ($kind != $HcomFood)
        && ($kind != $HcomMoney) ){

        if ($island->{'business'} > 0) {
            if ($island->{'shtf'} > 0) {        #�ϥ��ƥ���� ��¤ �һ���

                $cost = int($cost * 9 / 10);
            }
            elsif ($island->{'htf'} > 0){

                $cost = int($cost * 2 / 3);
            }
        }
    }

    # �����ȥ����å�
    if (   ($cost > 0)
        && ($island->{'money'} < $cost)
        && ($kind != $HcomFarmcpc)
            ) { # ��ξ��(��������ξ�硢�����ȥ����å����ʤ�)

        logNoAny($id, $name, $comName, '�����­��');
        return 0;
    }
    elsif (   ($cost < 0)
           && ($island->{'food'} < (-$cost) ) ) {# �����ξ��
        logNoAny($id, $name, $comName, '���߿�����­��');
        return 0;
    }

    # ���ޥ�ɤ�ʬ��
    if (   ($kind == $HcomPrepare)
        || ($kind == $HcomPrepare2) ) {
        # ���ϡ��Ϥʤ餷
        if ( ($landKind == $HlandSea) ||
             ($landKind == $HlandIce) ||
             ($landKind == $HlandGold) ||
             ($landKind == $HlandYougan) ||
             ($landKind == $HlandShrine) ||
             ($landKind == $HlandRottenSea) ||
             ($landKind == $HlandMountain) ||
             ($landKind == $HlandGomi) ||
             ($landKind == $HlandGomiFactory) ||
             ($landKind == $HlandMonster)) {
            # �����⻳�����ο��¡��峤���������ä����ϤǤ��ʤ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

        if ($landKind == $HlandMonument) {       # ��ǰ��

            if (   (79 < $lv)
                && ($lv < 84) ) {
                #$island->{'food'} += 20000; # ���٤��㤨
                food_product_plus($island , 'tamago' ,20000);
            }
            elsif ((73 < $lv) && ($lv < 80)) {
                $island->{'money'} += 20000; # ���в�����
            }

        }
        elsif ($landKind == $HlandEgg) {       # ��
            #$island->{'food'} += 20000; # ���٤��㤨
            food_product_plus($island , 'tamago' ,20000);

        }
        elsif ( $landKind == $HlandTown ) {
            logTownDel($id, $name, $landName ,'����', $point , $lv);
        }

        # ��Ū�ξ���ʿ�Ϥˤ���
        if (($landKind == $HlandOil) ||         # ����
            ($landKind == $HlandFune) ||        # ��
            ($landKind == $HlandSbase) ||       # �������
            ($landKind == $HlandSeacity) ||     # �����Ի�
            ($landKind == $HlandSeatown) ||     # ���쿷�Ի�
            ($landKind == $HlandFrocity) ||     # �����Իԥᥬ�ե���
            ($landKind == $HlandUmiamu) ||      # �����ߤ�
            ($landKind == $HlandUmishuto) ||    # �������
            ($landKind == $HlandNursery) ||     # �ܿ���
            ($landKind == $HlandUmicity) ||     # �ܿ���
            ($landKind == $HlandOilCity) ||     # �����Ի�
            (0)                          ) {

            if ($landKind == $HlandNursery) {

                SetSeaShallowLand($island , $x , $y);
            }
            else {

                $land->[$x][$y] = $HlandSea;
                $landValue->[$x][$y] = 0;
                $landValue->[$x][$y] = 1 if ($landKind == $HlandNursery);    # �ܿ����������
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }
        }
        else {
            SetPlains_Normal($island , $x , $y);
        }

        # ���ϥ����ܲ�
        if ($HlogOmit2) {

            my ($sno) = $island->{'seichi'};
            $island->{'seichi'}++;

            if ($HlogOmit2 == 1) {
                my ($seichipnt);
                ($seichipnt->{x}, $seichipnt->{y}) = ($x, $y);
                $island->{'seichipnt'}->[$sno] = $seichipnt;
            }
        }
        else {
            logLandSuc($id, $name, '����', $point);
        }

        # ��򺹤�����
        $island->{'money'} -= $cost;

        if ($kind == $HcomPrepare2) { # �Ϥʤ餷

            $island->{'prepare2'}++;
            # ��������񤻤�
            return 0;
        }
        else {
            # ���Ϥʤ顢��¢��β�ǽ������
            if (!$HnoDisFlag && (random(1000) < $HdisMaizo) ) {
                my ($v) = 100 + random(901);
                $island->{'money'} += $v;
                logMaizo($id, $name, $comName, $v);
            }
            return 1;
        }

    } elsif ( ($kind == $HcomReclaim) || 
              ($kind == $HcomReclaim2) ||
              ($kind == $HcomReclaim_spd) ||
              ($kind == $HcomMinato) ||
              ($kind == $HcomSeki) ||
              ($kind == $HcomReclaim2dan) ) {
        # ���Ω�ơ����Υ���Ω�ơ������ؽ�

        my ($flag) = 1;
        # �����Φ�����뤫�����å�
        my ($seaCount) = countAround($land, $x, $y, 7, @Hseas);
        if (   ($seaCount == 7)
            && ($kind != $HcomReclaim2)
            && ($kind != $HcomSeki)) {

            # �������ΤȤ������Ω�ơ������ߤ���ǽ
            logLandFail2($id, $name, $comName, $point, "���դ�Φ�Ϥ��ʤ��ä�");
            return 0;
        }

        if (   ($kind == $HcomReclaim)
            || ($kind == $HcomReclaim2)
            || ($kind == $HcomReclaim2dan)
            || ($kind == $HcomReclaim_spd) ) {
            # ���Ω��
            if ( ($landKind != $HlandSea) &&
                 ($landKind != $HlandSbase) &&
                 ($landKind != $HlandSeacity) &&
                 ($landKind != $HlandSeatown) &&
                 ($landKind != $HlandNursery) &&
                 ($landKind != $HlandUmicity) &&
                 ($landKind != $HlandOil) &&
                 ($landKind != $HlandUmiamu) &&
                 ($landKind != $HlandPlains) &&
                 ($landKind != $HlandUmishuto) &&
                 ($landKind != $HlandWaste) ) {
                # �������ġ������ߤ塢������ϡ������Իԡ����쿷�Իԡ�ʿ�ϡ����ϡ��ܿ��졢�������Ω�ƤǤ��ʤ�
                logLandFail($id, $name, $comName, $landName, $point);
                return 0;
            }

            # 2�����Ω��
            if ($kind == $HcomReclaim2dan) {

                if (   ($landKind == $HlandSea) && ($lv == 1) ) {
                    # �����ξ��
                    # ��Ū�ξ��򻳤ˤ���
                    SetMountain_Normal($island,$x,$y);

                } elsif(   ($landKind == $HlandPlains)
                        || ($landKind == $HlandWaste) ) {
                    # ʿ�ϡ����Ϥʤ顢��Ū�ξ��򻳤ˤ���
                    SetMountain_Normal($island,$x,$y);
                    $flag = 0;

                } else {
                    # �������ġ��ܿ��졢�����ߤ塢������ϡ������Իԡ����쿷�ԻԤʤ顢
                    # ��Ū�ξ�����Ϥˤ���
                    SetWasteLand_Normal($island,$x,$y);     # $HlandWaste
                }
            }
            else {
                #�̾�����Ω��
                if ( ($landKind == $HlandSea) && ($lv == 1) ) {
                    # �����ξ��
                    # ��Ū�ξ�����Ϥˤ���
                    SetWasteLand_Normal($island,$x,$y);     # $HlandWaste

                } elsif(   ($landKind == $HlandPlains)
                        || ($landKind == $HlandWaste) ) {
                    # ʿ�ϡ����Ϥʤ顢��Ū�ξ��򻳤ˤ���
                    SetMountain_Normal($island,$x,$y);
                    $cost = $HcomCost[$HcomReclaim]; #�����Ȥ����Ƥ����Ѥ���
                    $flag = 0;
                } else {
                    # �������ġ��ܿ��졢�����ߤ塢������ϡ������Իԡ����쿷�ԻԤʤ顢��Ū�ξ��������ˤ���
                    SetSeaShallowLand($island , $x , $y);
                    $flag = 0;
                }

                if ($kind == $HcomReclaim_spd) {
                    $comName = $HcomName[$HcomReclaim];
                }
            }

        } elsif ($kind == $HcomMinato) {
            # ��
            unless (   ($landKind == $HlandSea)
                    && ($lv == 1) ){
                # �����������ˤǤ��ʤ�
                logLandFail($id, $name, $comName, $landName, $point);
                return 0;
            }
            # ��Ū�ξ�����ˤ���
            $land->[$x][$y] = $HlandMinato;
            $landValue->[$x][$y] = 0;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;

        } elsif ($kind == $HcomSeki) {
            # �ؽ�
            if (($landKind != $HlandSea) || ($lv != 1)) {
                # ���������ؽ�ˤǤ��ʤ�
                logLandFail($id, $name, $comName, $landName, $point);
                return 0;
            }
            # ��Ū�ξ���ؽ�ˤ���
            $land->[$x][$y] = $HlandSeki;
            $landValue->[$x][$y] = 0;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
        }
        logLandSuc($id, $name, $comName, $point);

        if ($flag) {
            $island->{'area'}++;
            if ($seaCount <= 4) {
            # ����γ���3�إå�������ʤΤǡ������ˤ���
                my ($i, $sx, $sy);
                for ($i = 1; $i < 7; $i++) {
                    $sx = $x + $ax[$i];
                    $sy = $y + $ay[$i];
                    # �Ԥˤ�����Ĵ��
                    $sx-- if(!($sy % 2) && ($y % 2));
                    # �ϰ���ξ��
                    if (   ($sx >= 0) && ($sx < $HislandSize)
                        && ($sy >= 0) && ($sy < $HislandSize)
                        && ($land->[$sx][$sy] == $HlandSea)) {
                        $landValue->[$sx][$sy] = 1;
                    }
                }
            }
        }
        # ��򺹤�����
        $island->{'money'} -= $cost;
        if ($kind == $HcomReclaim_spd) {
            $island->{'prepare2'}++;
            return 0;
        }
        else {
            return 1;
        }

    } elsif($kind == $HcomPropaganda) {             # Ͷ�׳�ư

        logPropaganda($id, $name, $comName);
        $island->{'propaganda'} = 1;
        $island->{'money'} -= $cost;
        if ($arg > 1) {
            $arg--;
            slideBack($comArray, 0);
            $comArray->[0] = {
                'kind' => $kind,
                'target' => $target,
                'x' => $x,
                'y' => $y,
                'arg' => $arg
            };
        }
        return 1;

    } elsif ($kind == $HcomFune) {
        # ¤�����й�
        if ($landKind != $HlandSea) {
            # ������¤���Ǥ��ʤ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        # ����˹������뤫�����å�
        my ($seaCount) = countAround($land, $x, $y, 7, $HlandMinato);
        if ($seaCount == 0) {
            # �����ʤ�����¤����ǽ
            logLandFail2($id, $name, $comName, $point, "���դ˹�Į���ʤ��ä�");
            return 0;
        }
        # �����ȥ����å�
        my ($value) = ($arg * $cost);
        if ($island->{'money'} < $value) {
            logNoAny($id, $name, $comName, "�����­��");
            return 0;
        }
        if ($arg == $HcomFrocity_num) {
            # �����ԻԤˤ���
            $land->[$x][$y] = $HlandFrocity;
            $landValue->[$x][$y] = 1;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
        }
        else {
            # ��Ū�ξ������ˤ���
            $land->[$x][$y] = $HlandFune;
            $arg = 1 if($arg >= $HfuneNumber || !$arg);
            $landValue->[$x][$y] = $arg;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
        }
        logLandSuc($id, $name, $comName, $point);
        # ��򺹤�����
        $island->{'money'} -= $value;
        return 1;

    } elsif($kind == $HcomDestroy) {
        # ����
        if(    ($landKind == $HlandSbase)
            || ($landKind == $HlandSeacity)
            || ($landKind == $HlandSeatown)
            || ($landKind == $HlandNursery)
            || ($landKind == $HlandUmicity)
            || ($landKind == $HlandOil)
            || ($landKind == $HlandFune)
            || ($landKind == $HlandUmiamu)
            || ($landKind == $HlandFrocity)
            || ($landKind == $HlandRottenSea)
            || ($landKind == $HlandUmishuto)
            || ($landKind == $HlandMonster)
            || ($landKind == $HlandYougan)
            || ($landKind == $HlandBigFood)
                                            ) {
            # ������ϡ������Իԡ����쿷�Իԡ����ġ������ܿ��졢�����ߤ塢�峤�����äϷ���Ǥ��ʤ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

        if (($landKind == $HlandSea) && !$lv) {
            # ���ʤ顢����õ��
            # ���۷���
            if ($HarmisticeTurn && ($HislandTurn <= $HgameLimitTurn)) {
                # ��ȯ����������Ķػ�
                logNotAvail($id, $name, $comName);
                return 0;
            }
            $arg = 1 if($arg == 0);
            my ($value, $p);
            $p = ($arg * $cost > $island->{'money'}) ? int($island->{'money'} / $cost) : $arg;
            $value = $p * $cost;
            $island->{'money'} -= $value;
            # ���Ĥ��뤫Ƚ��
            if ($p > random(100) + $island->{'oil'} * 25) {
                # ���ĸ��Ĥ���
                if ($arg == 1) {

                    logOil200Found($id, $name, $point, $comName, "$value$HunitMoney");
                    SetMonument_Normal($island ,$x , $y , 95);
                }
                else {

                    logOilFound($id, $name, $point, $comName, "$value$HunitMoney");
                    SetOilLand($island ,$x , $y);
                }

                $island->{'oil'}++;

                Sinden_Omaturi($island , 0 , 1001);     # ����
                Jinja_Omaturi($island , 0 , 1001);      # ����
            }
            else {
                # ̵�̷���˽����
                logOilFail($id, $name, $point, $comName, "$value$HunitMoney");
            }
            return 1;
        }
        # ��Ū�ξ��������ˤ��롣�����⻳�����ο��¤ʤ���Ϥˡ������ʤ鳤�ˡ�
        if (   ($landKind == $HlandMountain)
            || ($landKind == $HlandGold)
            || ($landKind == $HlandShrine)
            || ($landKind == $HlandOnsen) ) {

            SetWasteLand_Normal($island,$x,$y);     # $HlandWaste

        } elsif($landKind == $HlandSea) {
            SetSeaLand_Normal($island , $x , $y);

        } else {
            SetSeaShallowLand($island , $x , $y);
            $island->{'area'}-- if($landKind != $HlandIce);
        }
        logLandSuc($id, $name, $comName, $point);
        # ��򺹤�����
        $island->{'money'} -= $cost;
        return 1;

    } elsif($kind == $HcomDestroy2) {
        # ����
        if (   ($landKind == $HlandSbase)
            || ($landKind == $HlandSeacity)
            || ($landKind == $HlandSeatown)
            || ($landKind == $HlandUmicity)
            || ($landKind == $HlandOilCity)
            || ($landKind == $HlandNursery)
            || ($landKind == $HlandOil)
            || ($landKind == $HlandFune)
            || ($landKind == $HlandUmiamu)
            || ($landKind == $HlandFrocity)
            || ($landKind == $HlandRottenSea)
            || ($landKind == $HlandYougan)
            || ($landKind == $HlandUmishuto)
            || (   ($landKind == $HlandSea)
                && ($lv == 0) )
            || ($landKind == $HlandMonster)
            || ($landKind == $HlandYougan)
            || ($landKind == $HlandBigFood)
                                            ) {
            # ������ϡ������Իԡ����쿷�Իԡ����ġ������ܿ��졢�����ߤ塢�峤�����äϷ���Ǥ��ʤ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

        # ��Ū�ξ��������ˤ��롣�����⻳�����ο��¤ʤ���Ϥˡ������ʤ鳤�ˡ�
        if (   ($landKind == $HlandMountain)
            || ($landKind == $HlandGold)
            || ($landKind == $HlandShrine)
            || ($landKind == $HlandOnsen)
                                                ){

            SetWasteLand_Normal($island,$x,$y);     # $HlandWaste
        } elsif($landKind == $HlandSea) {
            SetSeaLand_Normal($island , $x , $y);

        } else {
            SetSeaShallowLand($island , $x , $y);
            $island->{'area'}-- if($landKind != $HlandIce);
        }

        $comName = $HcomName[$HcomDestroy];
        logLandSuc($id, $name, $comName, $point);
        # ��򺹤�����
        $island->{'money'} -= $cost;
        $island->{'prepare2'}++;
        return 0;

    } elsif($kind == $HcomOnsen) {# ��������

        if (   ($landKind == $HlandMountain)
            && ($lv == 0)
                                    ) {
            # ���ʤ顢����õ��
            # ���۷���
            $arg = 1 if(!$arg);
            my ($value, $p);
            $value = min($arg * ($cost), $island->{'money'});
            $p = int($value / $cost);
            $value = $p * $cost;
            $island->{'money'} -= $value;

            # ���Ĥ��뤫Ƚ��
            if(random(10000) < $p * 15) {
                my($v) = 1000 + random(2001);
                $island->{'money'} += $v;
                $land->[$x][$y] = $HlandGold;
                $landValue->[$x][$y] = 1;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                logGold($id, $name, $comName, $v);

                # ����
                Sinden_Omaturi($island , 0 , 1001);

                # ����
                Jinja_Omaturi($island , 0 , 1001);

            } elsif(random(1000) < 50) {
                logEggFound($id, $name, $comName);
                $land->[$x][$y] = $HlandEgg;
                $landValue->[$x][$y] = random($HEggKindMax);
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

            } elsif(random(1000) < 50) {
                logIsekiFound($id, $name, $comName);
                SetMonument_Normal($island , $x , $y , 84);

            } elsif($p > random(100) + $island->{'hot'} * 30) {
                # �������Ĥ���
                logHotFound($id, $name, $point, $comName, "$value$HunitMoney");
                $land->[$x][$y] = $HlandOnsen;
                $landValue->[$x][$y] = 1;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

            } else {
                # ̵�̷���˽����
                logHotFail($id, $name, $point, $comName, "$value$HunitMoney");
            }

            if(random(1000) < 15) {
                my($v) = 100 + random(901);
                $island->{'money'} += $v;
                logMaizo($id, $name, $comName, $v);
            }
            return 1;
        } else {
            # ���ʳ��Ϸ���Ǥ��ʤ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

    } elsif($kind == $HcomYotei) {
        if(!($landKind == $HlandPlains)){

            # ��Ŭ�����Ϸ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0; # ���������ʤ�
        }
        # ��Ū�ξ���ʿ�Ϥˤ���
        $land->[$x][$y] = $HlandPlains;
        if ( $lv == 0 ) {
            $landValue->[$x][$y] = 1;
        }else{
            $landValue->[$x][$y] = 0;
        }
        $landValue2->[$x][$y] = 0;
        $landValue3->[$x][$y] = 0;
        return 0; # ���������ʤ�

    } elsif($kind == $HcomSellTree) {
        # Ȳ��
        if($landKind != $HlandForest) {
            # ���ʳ���Ȳ�ΤǤ��ʤ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        # ��Ū�ξ���ʿ�Ϥˤ���
        SetPlains_Normal($island, $x,$y);
        logLandSuc($id, $name, $comName, $point);
        if(random(1000) < 75) {
            logEggFound($id, $name, $comName);
            $land->[$x][$y] = $HlandEgg;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            $landValue->[$x][$y] = random($HEggKindMax);
        }
        # ��Ѷ������
        $island->{'money'} += $HtreeValue * $lv;
        return 0; # ���������ʤ�

    # �Ͼ���߷�
    } elsif(($kind == $HcomPlant) ||    # ����
            ($kind == $HcomFarm) ||        # ����
            ($kind == $HcomFoodim) ||    # ��ʪ�����
            ($kind == $HcomFarmcpc) ||    # �Ҿ�
            ($kind == $HcomCollege) ||    # �������
            ($kind == $HcomFactory) ||    # ����
            ($kind == $HcomBase) ||        # �ߥ��������
            ($kind == $HcomMonument) ||    # ��ǰ��
            ($kind == $HcomHaribote) ||    # �ϥ�ܥ�
            ($kind == $HcomMonbuy) ||    # ���ù���
            ($kind == $HcomMonbuyt) ||    # �ƥȥ����
            ($kind == $HcomPark) ||        # ͷ����
            ($kind == $HcomMine) ||        # ����
            ($kind == $HcomNursery) ||    # �ܿ���
            ($kind == $HcomKyujo) ||    # ����
            ($kind == $HcomYakusho) ||    # ��ꥳ�ޥ��
            ($kind == $HcomUmiamu) ||    # �����ߤ�
            ($kind == $HcomNewtown) ||    # �˥塼������
            ($kind == $HcomRizort) ||    # �꥾����
            ($kind == $HcomDbase) || # �ɱһ���
            ($kind == $HcomFire) || # ���ɽ����
            ($kind == $HcomZoo) || # ưʪ��
            (0)) {

        if(!
            (   ($landKind == $HlandPlains)
             || ($landKind == $HlandTown)
             || (   ($landKind == $HlandPark)
                 && ($kind == $HcomPark) )
             || (   ($landKind == $HlandIce)
                 && ($kind == $HcomPark) )
             || (   ($landKind == $HlandBeachPark)
                 && ($kind == $HcomPark) )
             || (   ($landKind == $HlandSunahama)
                 && ($lv == 0)
                 && ($kind == $HcomPark) )
             || (   ($kind == $HcomUmiamu)
                 && (   ($landKind == $HlandSea) && (!$lv)
                     || ($landKind == $HlandUmiamu) ) )
             || (   ($landKind == $HlandMonument)
                 && ($kind == $HcomMonument)  )
             || (   ($kind == $HcomFarm)
                 && (   ($landKind == $HlandFarm)
                     || ($landKind == $HlandForest)
                     || ($landKind == $HlandSunahama)
                                                     ) )
             || (   (   ($landKind == $HlandFarmchi)
                     || ($landKind == $HlandFarmpic)
                     || ($landKind == $HlandFarmcow) )
                 && ($kind == $HcomFarmcpc) )
             || (   ($landKind == $HlandCollege)
                 && ($kind == $HcomCollege)  )
             || (   ($landKind == $HlandFoodim)
                 && ($kind == $HcomFoodim) )
             || (   ($landKind == $HlandFactory)
                 && ($kind == $HcomFactory) )
             || (   (($landKind == $HlandSea) && !$lv)
                 && ($kind == $HcomMine) )
             || (   ($landKind == $HlandForest)
                 && ($kind == $HcomFactory) )
             || (   (   ($landKind == $HlandSea) && ($lv)
                     || ($landKind == $HlandNursery))
                 && ($kind == $HcomNursery) )
             || (   ($landKind == $HlandZoo)
                 && ($kind == $HcomZoo) )
                                            ) ) {
            # ��Ŭ�����Ϸ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

        # �����ʬ��
        if($kind == $HcomPlant) {
            # ����
            $land->[$x][$y] = $HlandForest;
            $landValue->[$x][$y] = 1; # �ڤϺ���ñ��
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logPBSuc($id, $name, $comName, $point);

        } elsif(($kind == $HcomMonbuy) || ($kind == $HcomMonbuyt)) {
            # ���ù������ƥȥ����
            my $mKind = MonsterBuySpawn();

            $mKind = 29 if($kind == $HcomMonbuyt); # ���åƥȥ�
            $lv = Calc_MonsterLandValue($mKind);
            $land->[$x][$y] = $HlandMonster;
            $landValue->[$x][$y] = $lv;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            $island->{'monsterlive'}++;
            # ���þ���
            my($mName) = (monsterSpec($lv))[1];
            # ��å�����
            logMonsFree($id, $name, $mName, $point);

        } elsif($kind == $HcomBase) {
            # �ߥ��������
            $land->[$x][$y] = $HlandBase;
            $landValue->[$x][$y] = 0; # �и���0
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logPBSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomFactory) {
            # ����
            if($landKind == $HlandFactory) {
                # ���Ǥ˹���ξ��
                $landValue->[$x][$y] += $HFactory_add; # ���� + 10000��
                $landValue->[$x][$y] = $HFactory_limit if($landValue->[$x][$y] > $HFactory_limit); # ���� 100000��

            } elsif($landKind == $HlandForest) {
                # ��Ū�ξ��򹩾��
                $land->[$x][$y] = $HlandFactory;
                $landValue->[$x][$y] = $HFactory_base; # ���� = 30000��
                $landValue2->[$x][$y] = 1;
                $landValue3->[$x][$y] = 0;

            } else {
                # ��Ū�ξ��򹩾��
                $land->[$x][$y] = $HlandFactory;
                $landValue->[$x][$y] = $HFactory_base; # ���� = 30000��
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomPark) {
            # ͷ����
            if($landKind == $HlandPark) {
                # ���Ǥ�ͷ���Ϥξ��
                $landValue->[$x][$y] += $HPark_add; # ���� + 30000��
                $landValue->[$x][$y] = $HPark_limit if($landValue->[$x][$y] > $HPark_limit); # ���� 100000��
            } elsif($landKind == $HlandIce) {
                # ���Ǥ�ɹ�Ϥξ��
                $landValue->[$x][$y] += $HIce_add; # ���� + 25000��
                $landValue->[$x][$y] = $HPark_limit if($landValue->[$x][$y] > $HPark_limit); # ���� 100000��
            } elsif($landKind == $HlandSunahama) {
                # ���Ǥ�ɹ�Ϥξ��
                $land->[$x][$y] = $HlandBeachPark;
                $landValue->[$x][$y] = $HPark_base; # ���� + 25000��
            } elsif($landKind == $HlandBeachPark) {
                # ���Ǥ�ɹ�Ϥξ��
                $landValue->[$x][$y] += $HIce_add; # ���� + 25000��
                $landValue->[$x][$y] = $HPark_limit if($landValue->[$x][$y] > $HPark_limit); # ���� 100000��
            } else {
                # ��Ū�ξ���ͷ���Ϥ�
                $land->[$x][$y] = $HlandPark;
                $landValue->[$x][$y] = $HPark_base; # ���� = 10000��
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                $island->{'par'}++;
            }
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomZoo) {

            my (@mons_list);
            my ($tmp);

            if ($landKind == $HlandZoo) {
                # ưʪ��
                my ($nigekaiju);
                my ($nigeflag);

                $tmp = $island->{'zoo'};
                chomp($tmp);
                @mons_list = split(/\,/,$tmp);

                $nigekaiju = $arg;
                $nigeflag = 0;

                # ���ä���äƤ뤫��
                if ($mons_list[$nigekaiju] > 0) {
                    my ($i, $sx, $sy, $la_Kind, $mlv);

                    # ����1HEX�����Ϥ��ǧ
                    for ($i = 1; $i < 7; $i++) {
                        $sx = $x + $ax[$i];
                        $sy = $y + $ay[$i];

                        # �Ԥˤ�����Ĵ��
                        if ((($sy % 2) == 0) && (($y % 2) == 1)) {
                            $sx--;
                        }

                        if ( ($sx < 0) || ($sx >= $HislandSize) ||
                             ($sy < 0) || ($sy >= $HislandSize)) {

                        } else {
                            # �ϰ���ξ��
                            $la_Kind = $land->[$sx][$sy];
                            $mlv = $landValue->[$sx][$sy];
                            $point = "($sx, $sy)";

                            if (   ($la_Kind == $HlandWaste)
                                || ($la_Kind == $HlandPlains) 
                                || ($la_Kind == $HlandTown)
                                || ($la_Kind == $HlandForest)
                                || ($la_Kind == $HlandHaribote)
                                                                 ) {

                                if ($nigeflag < 1) {
                                    $nigeflag = 1;
                                    $mons_list[$nigekaiju] -= 1;
                                    # $lv = ($mKind << $Mons_Kind_Shift) + $HmonsterBHP[$mKind] + random($HmonsterDHP[$mKind]);
                                    $mlv = ($nigekaiju << $Mons_Kind_Shift)
                                         + $HmonsterBHP[$nigekaiju] + random($HmonsterDHP[$nigekaiju]);

                                    my ($mval2) = 0;
                                    $land->[$sx][$sy] = $HlandMonster;
                                    $landValue->[$sx][$sy] = $mlv;
                                    $landValue2->[$sx][$sy] = $mval2;
                                    $landValue3->[$sx][$sy] = 0;
                                    $island->{'monsterlive'}++;

                                    my ($mKind, $mName, $mHp) = monsterSpec($mlv);
                                    logNige2($id, $name, landName($la_Kind, $mlv, $mval2), $mName, "($x, $y)");
                                    Write_ZooState($island , $nigekaiju , $mons_list[$nigekaiju] );
                                    last;
                                }
                            }
                        }
                    }

                    if ($nigeflag < 1) {
                        $mlv = ($nigekaiju << $Mons_Kind_Shift)
                            + $HmonsterBHP[$nigekaiju] + random($HmonsterDHP[$nigekaiju]);

                        # �ɤ��˸���뤫����
                        my ($bx, $by, $i ,$la_Kind);

                        for ($i = 0; $i < $HpointNumber; $i++) {
                            $bx = $Hrpx[$i];
                            $by = $Hrpy[$i];

                            $la_Kind = $land->[$bx][$by];

                            if (   ($la_Kind == $HlandWaste)
                                || ($la_Kind == $HlandPlains) 
                                || ($la_Kind == $HlandTown)
                                || ($la_Kind == $HlandForest)
                                || ($la_Kind == $HlandFarm)
                                || ($la_Kind == $HlandFactory)
                                || ($la_Kind == $HlandHaribote)
                                || ($la_Kind == $HlandNewtown)
                                                                 ) {

                                # �Ϸ�̾
                                my($lName) = landName($la_Kind, $landValue->[$bx][$by],$landValue2->[$bx][$by]);

                                # ���Υإå�������ä�
                                $land->[$bx][$by] = $HlandMonster;
                                $landValue->[$bx][$by] = $mlv;
                                $landValue2->[$bx][$by] = 0;
                                $landValue3->[$bx][$by] = 0;
                                $island->{'monsterlive'}++;

                                $mons_list[$nigekaiju] -= 1;
                                Write_ZooState($island , $nigekaiju , $mons_list[$nigekaiju]);

                                # ���þ���
                                my($mKind, $mName, $mHp) = monsterSpec($mlv);

                                # ��å�����
                                logMonsCome($id, $name, $mName, "($bx, $by)", $lName);
                                last;
                            }
                        }
                    }
                }
                return 0;

            }
            else {
                my ($zlv);
                my ($first);
                my ($safe2) = 0 ;

                # ��Ū�ξ���ưʪ���
                $zlv = 10 + $island->{'zoo_capacity'};
                $land->[$x][$y] = $HlandZoo;
                $landValue->[$x][$y] = 10; # ���� = 10000��
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

                my ($zookazu, $zookazus, $m_syurui) = Get_ZooState($island);

                $first = 1;
                while((random(4) != 0) || ($first == 1)) {

                    # �����֤���ʸ�Τ��ᡢ������ zoo����
                    $tmp = $island->{'zoo'};
                    chomp($tmp);
                    @mons_list = split(/\,/,$tmp);

                    # ��������������
                    my ($flag , $monster , $plus);
                    my ($siire);
                    my ($safe);

                    # ��������������
                    if ($island->{'taiji'}) {

                        $safe = 0;
                        # �����֤�
                        while (1) {

                            $flag = 0;
                            $siire = random($#HmonsterName);    # ���٤Ƥβ��ä���

                            if (random(100) < $HmonsterZoo[$siire]) {
                                $flag = GetTaijiFlag($island , $siire);

                                if ($flag) {
                                    last;
                                }
                            }

                            $safe++;

                            if ($safe > 30) {
                                # �����֤��� 30Ķ������ ���Τ����
                                $siire = 1;
                                last;
                            }
                        }
                    }
                    else {
                        # �����ݤ������Ȥʤ��ʤ顢���Τ����
                        $siire = 1;
                    }

                    # �������߻��ϡ��ޤ������뤫������
                    if (   ($zlv > $zookazu)            # ���ä��ޤ������뤫�ɤ�����
                                                    ) {

                        $plus = ($mons_list[$siire]) ? ($mons_list[$siire] + 1) : 1 ;
                        logSiire($id, $name, landName($HlandZoo, 1,0), "$HmonsterName[$siire]", "($x, $y)");
                        Write_ZooState($island , $siire , $plus );
                        $first = 0;
                    }
                    else{
                        last;
                    }

                    $safe2++;
                    if ($safe2 > 30) {
                        # �����֤��� 30Ķ������ ���Τ����
                        last;
                    }
                }
            }

        } elsif($kind == $HcomFire) {
            # ���ɽ����
            $land->[$x][$y] = $HlandFiredept;
            $landValue->[$x][$y] = 0;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomNursery) {
            # �ܿ���
            if ($landKind == $HlandNursery) {
                # ���Ǥ��ܿ���ξ��
                $landValue->[$x][$y] += $HNursery_add; # ���� + 5000��
                $landValue->[$x][$y] = $HNursery_limit if($landValue->[$x][$y] > $HNursery_limit); # ���� 100000��
            } elsif(($landKind == $HlandSea) && $lv) {
                # ��Ū�ξ����ܿ����
                $land->[$x][$y] = $HlandNursery;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                $landValue->[$x][$y] = $HNursery_base; # ���� = 20000��
            }
            else {
                # ��Ŭ�����Ϸ�
                logLandFail($id, $name, $comName, $landName, $point);
                return 0;
            }
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomKyujo) {
            # ����
            $land->[$x][$y] = $HlandKyujo;
            $landValue->[$x][$y] = 0;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomNewtown) {
            # �˥塼������
            my($pop);
            if ( $land->[$x][$y] == $HlandTown ) {
                $pop = $landValue->[$x][$y];
            }
            else {
                $pop = 1;
            }
            $land->[$x][$y] = $HlandNewtown;
            $landValue->[$x][$y] = $pop;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomRizort) {
            # ��Ū�ξ���꥾���Ȥˤ���
            $land->[$x][$y] = $HlandRizort;
            $landValue->[$x][$y] = 1;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomUmiamu) {
            # �����ߤ�
            if ($landKind == $HlandUmiamu) {
                # ���Ǥ˳����ߤ�ξ��
                $landValue->[$x][$y] += $HUmiamu_add; # ���� + 30000��
                $landValue->[$x][$y] = $HUmiamu_limit if($landValue->[$x][$y] > $HUmiamu_limit); # ���� 1000000��
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

            }
            elsif(($landKind == $HlandSea) && !$lv) {
                # ���ʤ顢��Ū�ξ��򳤤��ߤ��
                $land->[$x][$y] = $HlandUmiamu;
                $landValue->[$x][$y] = $HUmiamu_base; # ���� = 50000��
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                $island->{'amu'}++;

            }
            else {
                # ��Ŭ�����Ϸ�
                logLandFail($id, $name, $comName, $landName, $point);
                return 0;
            }
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomFarm) {
            # ����
            if($landKind == $HlandFarm) {
                # ���Ǥ�����ξ��
                $landValue->[$x][$y] += $HFarm_add; # ���� + 2000��
                $landValue->[$x][$y] = $HFarm_limit if($landValue->[$x][$y] > $HFarm_limit); # ���� 50000��

            } else {
                # ��Ū�ξ��������
                $land->[$x][$y] = $HlandFarm;
                $landValue->[$x][$y] = $HFarm_base; # ���� = 10000��
                if ($landKind == $HlandForest) {
                    $landValue2->[$x][$y] = 1;
                } elsif($landKind == $HlandSunahama) {
                    $landValue2->[$x][$y] = 2;
                }else{
                    $landValue2->[$x][$y] = 0;
                }
                $landValue3->[$x][$y] = 0;
            }
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomFoodim) {
            # ��ʪ�����
            if($landKind == $HlandFoodim) {
                # ���Ǥ˿�ʪ�����ξ��
                $landValue->[$x][$y] += $HFoodim_add; # ���� + 10000��
                $landValue->[$x][$y] = $HFoodim_limit if($landValue->[$x][$y] > $HFoodim_limit); # ���� 500000��
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

            } else {
                # ��Ū�ξ���ʪ������
                $land->[$x][$y] = $HlandFoodim;
                $landValue->[$x][$y] = $HFoodim_base; # ���� = 30000��
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomCollege) {
            # �������
            my ($col_name);
            if (   ($landKind == $HlandCollege)
                && (   ($lv == 4)
                    || ($lv == 96) )
                                     ) {
                $landValue->[$x][$y] = 100 - $lv;
                logLandSuc($id, $name, $comName, $point);
                return 0;

            } elsif(($landKind == $HlandCollege) && (($lv == 97) || ($lv == 98))) {
                $landValue->[$x][$y] = 195 - $lv;
                logLandSuc($id, $name, $comName, $point);
                return 0;

            } else {
                # ��ط���

                $land->[$x][$y] = $HlandCollege;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                if(random(100) < 30) {
                    $landValue->[$x][$y] = 0;
                    $col_name = '(�������)';

                } elsif(random(100) < 30) {
                    $landValue->[$x][$y] = 1;
                    $col_name = '(�������)';

                } elsif(random(100) < 15) {
                    $landValue->[$x][$y] = 2;
                    $col_name = '(������)';

                } elsif(random(100) < 15) {
                    $landValue->[$x][$y] = 3;
                    $col_name = '(�������)';

                } elsif(random(100) < 15) {
                    $landValue->[$x][$y] = 4;
                    $col_name = '(��ʪ���)';

                    if(($island->{'co4'} == 0) && ($island->{'co99'} == 0) && ($island->{'c28'} == 0)) {
                        $island->{'eisei5'} = "3,5,5,5,0,0,0";
                    }

                } else {
                    $landValue->[$x][$y] = 5;
                    $col_name = '(�������)';

                }
            }
            my($comLog);

            $comLog = "${comName}${col_name}";
            logLandSuc($id, $name, $comLog, $point);

        } elsif($kind == $HcomFarmcpc) {
            # �Ҿ�
            $arg = 1 if(($arg >= 4) || ($arg == 0));
            my @ltmp = ($HlandFarmchi, $HlandFarmpic, $HlandFarmcow);
            my @mtmp = (10, 20, 50);
            my($l, $flag);
            $flag = 0;
            foreach $l (@ltmp) {
                if($landKind == $l) {
                    $island->{'money'} += $lv * $mtmp[$flag];
                    last;
                }
                $flag++;
            }
            if($flag == 3){
                # �����ȥ����å�
                my $value = $arg * $cost;
                if($island->{'money'} < $value) {
                    logNoAny($id, $name, $comName, "�����­��");
                    return 0;
                }
                $land->[$x][$y] = $ltmp[$arg - 1];
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                $island->{'money'} -= $value;
            }
            $landValue->[$x][$y] = 1;
            logLandSuc($id, $name, $comName, $point);
            if($flag == 3){
                return 1;
            } else {
                return 0;
            }

        } elsif($kind == $HcomDbase) {
            # �ɱһ���
            # ��Ū�ξ����ɱһ��ߤ�
            $land->[$x][$y] = $HlandDefence;
            $landValue->[$x][$y] = 0;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomYakusho) {
            my($shutoCount) = countAround($land, $x, $y, 7, $HlandShuto, $HlandUmishuto);

            if(   ($island->{'shu'} == 0)
               || ($shutoCount == 0)
               || ($island->{'yaku'} > 0) ) {
                logLandFail2($id, $name, $comName, $point, "�����������Ƥ��ʤ�<B>$landName</B>��");
                return 0;
            }
            $land->[$x][$y] = $HlandYakusho;                    # ���ˤ���
            $island->{'yaku_work'} |= $HYakushoWorkExist;       # ��꤬¸��
            $island->{'yaku_work'} |= $HYakushoWorkYotei;       # ͽ���ϳ��ݤ�ON
            $landValue->[$x][$y] = 1;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomMine) {
            # ��������
            $arg = 1 if($arg == 0);
            $arg = $HMine_limit if($arg > $HMine_limit);
            $arg = min($arg, int($island->{'money'} / $cost));
            $cost *= $arg;
            $land->[$x][$y] = $HlandMine;

            $landValue->[$x][$y] = $arg;
            $landValue->[$x][$y] |= $Hmine_SEA_FLAG if($landKind == $HlandSea);
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logPBSuc($id, $name, $comName, $point);

        } elsif($kind == $HcomHaribote) {

            if (   ($arg >= $HTrainBase)
                && ($arg <= $HTrainMAX) ) {

                $land->[$x][$y] = $HlandTrain;
                $landValue->[$x][$y] = $arg;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                logLandSuc($id, $name, "��ϩ����", $point);

            }
            else {
                # �ϥ�ܥ�
                $land->[$x][$y] = $HlandHaribote;
                $landValue->[$x][$y] = 0;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                logHariSuc($id, $name, $comName, $HcomName[$HcomDbase], $point);
            }

        } elsif ($kind == $HcomMonument) {
            # ��ǰ��
            if ($landKind == $HlandMonument) {
                return 0 if (!$HuseBigMissile);
                # ���Ǥ˵�ǰ��ξ��
                # �������åȼ���
                my ($tn) = $HidToNumber{$target};
                # �������åȤ����Ǥˤʤ���硢������鷺�����
                return 0 unless(defined $tn);

                my ($aId, %amityFlag);
                foreach $aId (@{$island->{'allyId'}}) {
                    foreach (@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}) {
                        next if($_ == $id);
                        $amityFlag{$_} = $HcampAtk;
                    }
                }
                # ��ȯ���֤ʤ饳�ޥ�ɤ�̵��
                if ($HarmisticeTurn && ($HislandTurn <= $HarmisticeTurn || $amityFlag{$target})) {
                    # ���⤬���Ĥ���Ƥ��ʤ�
                    logNotAvail($id, $name, $comName);
                    return 0;
                }

                my ($tIsland) = $Hislands[$tn];
                # ����ο͸������ʤ�������ɸ��ο͸������ʤ���BattleField�ʤ顢�¹Ԥϵ��Ĥ���ʤ�
                if (   ($tIsland->{'id'} != $id)
                    && (   ($island->{'pop'} < $HguardPop)
                        || ($tIsland->{'pop'} < $HguardPop)
                        || ($tIsland->{'id'} > 100) ) ) {
                    logNoAny($id, $name, $comName, "�¹Ԥ����Ĥ���ʤ�");
                    return 0;
                }
                $tIsland->{'bigmissile'}++;
                # ���ξ��Ϲ��Ϥ�
                SetWasteLand_Normal($island,$x,$y);     # $HlandWaste
                logMonFly($id, $name, $landName, $point);

            } else {

                if ( $arg == 94 ) {
                    # ��Ū�ξ����褯���
                    $land->[$x][$y] = $HlandKatorikun;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    logLandSuc($id, $name, "�ڤι�褯�����", $point);

                } elsif($arg == 17) {
                    # ��Ū�ξ�����åȤ�
                    $land->[$x][$y] = $HlandRocket;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    logLandSuc($id, $name, "���åȷ���", $point);

                } elsif($arg == 42) {
                    # ��Ū�ξ���ؤ�
                    $land->[$x][$y] = $HlandStation;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    logLandSuc($id, $name, "�ط���", $point);

                }else{
                    # ��Ū�ξ���ǰ���
                    $land->[$x][$y] = $HlandMonument;
                    $arg = 0 if($arg >= $HmonumentNumber);
                    $landValue->[$x][$y] = $arg;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    logLandSuc($id, $name, $comName, $point);
                }
            }
        }

        #�ʾ塢�Ͼ���߷Ϥ�return���Ƥʤ����ޥ�ɤ�ޤȤ��
        # ��򺹤�����
        $island->{'money'} -= $cost;
        # ����դ��ʤ顢���ޥ�ɤ��᤹
        if (    ($kind == $HcomFarm)
            || ($kind == $HcomFoodim)
            || ($kind == $HcomNursery)
            || ($kind == $HcomPark)
            || ($kind == $HcomUmiamu)
            || ($kind == $HcomFactory) ) {

            if ($arg > 1) {
                $arg--;
                slideBack($comArray, 0);
                $comArray->[0] = {
                    'kind' => $kind,
                    'target' => $target,
                    'x' => $x,
                    'y' => $y,
                    'arg' => $arg
                };
            }
        }
        return 1;

    } elsif($kind == $HcomMountain) {
        # �η���
        if ($landKind == $HlandMountain) {
            # ���Ǥ˺η���ξ��
            $landValue->[$x][$y] += $HMountain_add; # ���� + 5000��
            $landValue->[$x][$y] = $HMountain_limit if($landValue->[$x][$y] > $HMountain_limit); # ���� 200000��
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;

        } elsif($landKind == $HlandGold) {
            # ���Ǥ˶⻳�ξ��
            $landValue->[$x][$y] += $HGold_add; # ���� + 20000��
            $landValue->[$x][$y] = $HGold_limit if($landValue->[$x][$y] > $HGold_limit); # ���� 200000��
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;

        } else {
            # ��Ŭ�����Ϸ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        logLandSuc($id, $name, $comName, $point);

        if(random(1000) < 9) { # 0.9%�Ƕ⻳��
            my($v) = 1000 + random(4001); # 1000��5000���μ���
            $island->{'money'} += $v;
            $land->[$x][$y] = $HlandGold;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logGold($id, $name, $comName, $v);

            Sinden_Omaturi($island , 0 , 1001);

            # ����
            Jinja_Omaturi($island , 0 , 1001);
        }
        # ��򺹤�����
        $island->{'money'} -= $cost;
        # ����Ĥ��ʤ饳�ޥ�ɤ��᤹
        if($arg > 1) {
            $arg--;
            slideBack($comArray, 0);
            $comArray->[0] = {
                'kind' => $kind,
                'target' => $target,
                'x' => $x,
                'y' => $y,
                'arg' => $arg
            };
        }
        return 1;

    } elsif($kind == $HcomHTget) {
        # �ϥ��ƥ�
        if($landKind == $HlandHTFactory) {
            # ���Ǥ˺η���ξ��
            $landValue->[$x][$y] += $HHTFactory_add; # ���� + 10000��
            $landValue->[$x][$y] = $HHTFactory_limit if($landValue->[$x][$y] > $HHTFactory_limit); # ���� 500000��
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;

        } elsif($landKind == $HlandFactory) {
            if($lv == $HFactory_limit) {
                $land->[$x][$y] = $HlandHTFactory;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            } else {
                logLandFail2($id, $name, $comName, $point, "�����������Ƥ��ʤ�<B>$landName</B>��");
                return 0;
            }

        } elsif(   ($landKind == $HlandMonument)
                && ($landValue->[$x][$y] == 10)
                                                ) {
            if ( random(2) ) {
                $landValue->[$x][$y] = 72;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

            }else{
                $landValue->[$x][$y] = 73;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }

        } else {
            # ��Ŭ�����Ϸ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        logLandSuc($id, $name, $comName, $point);

        # ��򺹤�����
        $island->{'money'} -= $cost;
        if ($arg > 1) {
            $arg--;
            slideBack($comArray, 0);
            $comArray->[0] = {
                'kind' => $kind,
                'target' => $target,
                'x' => $x,
                'y' => $y,
                'arg' => $arg
            };
        }
        return 1;


    } elsif($kind == $HcomBettown) {
        my ($shutoCount) = countAround($land, $x, $y, 7, $HlandShuto, $HlandUmishuto);
        my ($betCount) = countAround($land, $x, $y, 7, $HlandBettown);

        if ($landKind != $HlandBigtown){
            # ��Ŭ�����Ϸ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

        if (($island->{'shu'} > 0) && (($shutoCount > 0) || ($betCount > 1))) {
            $land->[$x][$y] = $HlandBettown;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);
            # ��򺹤�����
            $island->{'money'} -= $cost;
            return 1;
        } else {
            logLandFail2($id, $name, $comName, $point, "�����������Ƥ��ʤ�<B>$landName</B>��");
            return 0;
        }

    } elsif ($kind == $HcomKai) {

        if ($landKind == $HlandKyujo) {
            if ( !$island->{'stadiumnum'} ) {
                $island->{'eisei4'} = "1,1,1,0,0,0,0,0,0,0,10";
            }
            $land->[$x][$y] = $HlandKyujokai;
            $landValue->[$x][$y] = 0;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            $island->{'stadiumnum'}++;
            logLandSuc($id, $name, $comName, $point);
            # ��򺹤�����
            $island->{'money'} -= $cost;
            return 1;

        } elsif ($landKind == $HlandKyujokai) {
            my ($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $island->{'eisei4'});
            $sto++;
            $std++;
            $stk++;
            $island->{'eisei4'} = "$sto,$std,$stk,$stwin,$stdrow,$stlose,$stwint,$stdrowt,$stloset,$styusho,$stshoka";
            logLandSuc($id, $name, $comName, $point);
            # ��򺹤�����
            $island->{'money'} -= $cost;
            if($arg > 1) {
                $arg--;
                slideBack($comArray, 0);
                $comArray->[0] = {
                    'kind' => $kind,
                    'target' => $target,
                    'x' => $x,
                    'y' => $y,
                    'arg' => $arg
                };
            }
            return 1;

        } elsif (($landKind == $HlandFune) && ($lv == 10)) {
            $landValue->[$x][$y] = 19;
            logLandSuc($id, $name, $comName, $point);
            # ��򺹤�����
            $island->{'money'} -= $cost;
            return 1;

        } elsif ($landKind == $HlandRizort) {
            my ($seaCount) = countAround($land, $x, $y, 7, @Hseas);
            my ($rizortCount) = countAround($land, $x, $y, 7, $HlandRizort, $HlandBigRizort);
            my ($value);
            $value = $lv+$island->{'eis1'}+$island->{'eis2'}+$island->{'eis3'}+$island->{'eis5'}+int($island->{'fore'}/10)+int($island->{'rena'}/10)-$island->{'monsterlive'}*100;

            if (   ($seaCount > 2)
                && ($value > 500)
                && ($rizortCount > 2) ) {

                $land->[$x][$y] = $HlandBigRizort;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                logLandSuc($id, $name, $comName, $point);
                # ��򺹤�����
                $island->{'money'} -= $cost;
                return 1;
            }
            else {
                logLandFail2($id, $name, $comName, $point, "�����������Ƥ��ʤ�<B>$landName</B>��");
                return 0;
            }

        } elsif (   ($landKind == $HlandYakusho)
                 && ($lv < 6) ) {

            $landValue->[$x][$y] ++;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;

            if ($landValue->[$x][$y] == 2) {
                $island->{'yaku_work'} |= $HYakushoWorkSeiti;
            }
            logLandSuc($id, $name, $comName, $point);
            # ��򺹤�����
            $island->{'money'} -= $cost;
            if ($arg > 1) {
                $arg--;
                slideBack($comArray, 0);
                $comArray->[0] = {
                    'kind' => $kind,
                    'target' => $target,
                    'x' => $x,
                    'y' => $y,
                    'arg' => $arg
                };
            }
            return 1;
        }
        elsif ($landKind == $HlandDefence) {

            my ($deflv , $defHP) = GetDefenceSpec($landValue->[$x][$y]);

            if ( $deflv == 0 ) {

                $landValue->[$x][$y] = 1;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }
            elsif ($deflv == 1) {

                $landValue->[$x][$y] = 82;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }
            elsif ($deflv == 2) {

                if ( $defHP < 10 ) {
                    $defHP += 2;
                    $defHP = 10 if ( $defHP > 10 );
                    $landValue->[$x][$y] = 2 + ($defHP << $HDefenceHP_SHIFT);
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;

                }else{
                    # ��Ŭ�����Ϸ�
                    logLandFail($id, $name, $comName, $landName, $point);
                    return 0;
                }

            }
            logLandSuc($id, $name, $comName, $point);
            # ��򺹤�����
            $island->{'money'} -= $cost;
            return 1;

        } elsif($landKind == $HlandHTFactory) {# �ϥ��ƥ�����
            $land->[$x][$y] = $HlandSHTF;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);
            # ��򺹤�����
            $island->{'money'} -= $cost;
            return 1;

        } elsif(   ($landKind == $HlandSunahama)
                && ($lv == 0)  ) {# ����
            $landValue->[$x][$y] = 1;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;

            logLandSuc($id, $name, $comName, $point);
            # ��򺹤�����
            $island->{'money'} -= $cost;
            return 1;

        } elsif(   ($landKind == $HlandZoo) ) {     # ưʪ��  ����

            my ($limit) = 200;
            my ($div) = 75;
            my ($add) = 10;

            $landValue->[$x][$y] += $add;
            if ($landValue->[$x][$y] > int($island->{'rena'}/$div)) {
                $landValue->[$x][$y] = int($island->{'rena'}/$div);
            }

            if ($landValue->[$x][$y] > $limit) {
                $landValue->[$x][$y] = $limit;
            }

            logLandSuc($id, $name, $comName, $point);
            # ��򺹤�����
            $island->{'money'} -= $cost;
            if ($arg > 1) {
                $arg--;
                slideBack($comArray, 0);
                $comArray->[0] = {
                    'kind' => $kind,
                    'target' => $target,
                    'x' => $x,
                    'y' => $y,
                    'arg' => $arg
                };
            }
            return 1;

        } elsif (   ($landKind == $HlandPark)
                && ($lv >= $HPark_limit)
                && ($island->{'inoraland'} == 0 ) ) {

            $land->[$x][$y] = $HlandInoraLand;
            $landValue->[$x][$y] = $HPark_limit;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);
            # ��򺹤�����
            $island->{'money'} -= $cost;
            return 1;

        } elsif ($landKind == $HlandInoraLand) {

            # ���Τ���ɤ���Ĺ
            $landValue->[$x][$y] += $HInoraland_add; # ����++
            $landValue->[$x][$y] = $HInoraland_limit if($landValue->[$x][$y] > $HInoraland_limit); # ����

            logLandSuc($id, $name, $comName, $point);
            # ��򺹤�����
            $island->{'money'} -= $cost;
            if ($arg > 1) {
                $arg--;
                slideBack($comArray, 0);
                $comArray->[0] = {
                    'kind' => $kind,
                    'target' => $target,
                    'x' => $x,
                    'y' => $y,
                    'arg' => $arg
                };
            }
            return 1;

        } elsif(   ($landKind == $HlandTown)
                && ($lv <= $HInaka_limit)
                                            ) {
            # ���ʤ�
            $land->[$x][$y] = $HlandInaka;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            logLandSuc($id, $name, $comName, $point);
            # ��򺹤�����
            $island->{'money'} -= $cost;

        } else {
            # ��Ŭ�����Ϸ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }

    } elsif ($kind == $HcomSbase) {
        # �������
        unless (($landKind == $HlandSea) && !$lv){
            # ���ʳ��ˤϺ��ʤ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        $land->[$x][$y] = $HlandSbase;
        $landValue->[$x][$y] = 0;                   # �и���0
        $landValue2->[$x][$y] = 0;
        $landValue3->[$x][$y] = 0;
        logLandSuc($id, $name, $comName, '(?, ?)');
        # ��򺹤�����
        $island->{'money'} -= $cost;
        return 1;

    } elsif ($kind == $HcomSeacity) {
        # �����Ի�
        if (($landKind != $HlandSea) || $lv) {
            # ���ʳ��ˤϺ��ʤ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        $land->[$x][$y] = $HlandSeacity;
        $landValue->[$x][$y] = 0;           # �͸�0
        $landValue2->[$x][$y] = 0;
        $landValue3->[$x][$y] = 0;
        logLandSuc($id, $name, $comName, '(?, ?)');
        # ��򺹤�����
        $island->{'money'} -= $cost;
        return 1;

    } elsif($kind == $HcomProcity) {
        # �ɺҲ�
        if(($landKind != $HlandTown) || ($lv < 100)){
            # �������Ի԰ʳ��ˤϺ��ʤ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        $land->[$x][$y] = $HlandProcity;
        $landValue->[$x][$y] = 100; # �͸�10000
        $landValue2->[$x][$y] = 0;
        $landValue3->[$x][$y] = 0;
        logLandSuc($id, $name, $comName, $point);
        # ��򺹤�����
        $island->{'money'} -= $cost;
        return 1;

    } elsif ($kind == $HcomBigtown) {
        # ���岽
        if ( ($landKind != $HlandNewtown) || ($lv < 150) ||
             (countAround($land, $x, $y, 19, @Htowns) < 16) ) {
            # 15000�Ͱʾ�Υ˥塼������Ǥʤ��Ⱥ��ʤ�
            # ������ԻԤθĿ������ʤ��ȷ�����ǽ
            logLandFail2($id, $name, $comName, $point, "�����������Ƥ��ʤ�<B>$landName</B>��");
            return 0;
        }
        $land->[$x][$y] = $HlandBigtown;
        $landValue2->[$x][$y] = 0;
        $landValue3->[$x][$y] = 0;
        logLandSuc($id, $name, $comName, $point);
        # ��򺹤�����
        $island->{'money'} -= $cost;
        return 1;

    } elsif($kind == $HcomSeatown) {
        # ���쿷�Ի�
        if(   ($landKind != $HlandSeacity)
           || ($lv < 200)
           || (countAround($land, $x, $y, 19, @Htowns) < 16)){
            # 20000�Ͱʾ�γ����ԻԤǤʤ��Ⱥ��ʤ�
            # ������ԻԤθĿ������ʤ��ȷ�����ǽ
            logLandFail2($id, $name, $comName, '(?, ?)', "�����������Ƥ��ʤ�<B>$landName</B>��");
            return 0;
        }
        $land->[$x][$y] = $HlandSeatown;
        $landValue2->[$x][$y] = 0;
        $landValue3->[$x][$y] = 0;
        logLandSuc($id, $name, $comName, '(?, ?)');
        # ��򺹤�����
        $island->{'money'} -= $cost;
        return 1;

    } elsif($kind == $HcomBoku) {
        # �ͤΰ��ۤ�
        my($towncount) = countAround($land, $x, $y, 19, $HlandTown,$HlandNewtown);
        my($pop_limit);
        if(   (!$towncount)
           || (   ($landKind != $HlandProcity)
               && ($landKind != $HlandShuto)
               && ($landKind != $HlandUmishuto)
                                                )  ) {
            # �ɺ��Ի԰ʳ��Ǥϼ¹���ǽ
            # ������ԻԤ��ʤ��ȼ¹���ǽ
            if (!$towncount) {
                logLandFail2($id, $name, $comName, $point, "���(���Ϥ��ԻԿ�)�����������ԻԤǤʤ��ä�");
            }else{
                logLandFail2($id, $name, $comName, $point, "�������������ԻԤǤʤ��ä�");
            }
            return 0;
        }
        $landValue->[$x][$y] += int(10 * ($towncount / 2) ); # ���� + 1000��

        $pop_limit = $HProcity_limit if($landKind == $HlandProcity);
        $pop_limit = $HShuto_limit if(($landKind == $HlandShuto) || ($landKind == $HlandUmishuto));

        $landValue->[$x][$y] = $pop_limit if($landValue->[$x][$y] > $pop_limit);
        my($i,$sx,$sy);

        for($i = 1; $i < 19; $i++) {

            $sx = $x + $ax[$i];
            $sy = $y + $ay[$i];

            if(   ($land->[$sx][$sy] == $HlandTown)
               || ($land->[$sx][$sy] == $HlandNewtown) ){
                $landValue->[$sx][$sy] -= int(20 / $towncount);
                if($landValue->[$sx][$sy] <= 0) {
                    # ʿ�Ϥ��᤹
                    $land->[$sx][$sy] = $HlandPlains;
                    $landValue->[$sx][$sy] = 0;
                    next;
                }
            }
        }

        logLandSuc($id, $name, $comName, $point);
        # ��򺹤�����
        $island->{'money'} -= $cost;
        # ����Ĥ��ʤ饳�ޥ�ɤ��᤹
        if($arg > 1) {
            $arg--;
            slideBack($comArray, 0);
            $comArray->[0] = {
                'kind' => $kind,
                'target' => $target,
                'x' => $x,
                'y' => $y,
                'arg' => $arg
                };
        }
        return 1;

    } elsif($kind == $HcomBoku2) {  # �ͤΰ��ۤ�2

        # ���äϥ���󥻥�
        if($landKind == $HlandMonster) {
            my($mKind, $mName, $mHp) = monsterSpec($landValue->[$x][$y]);
            logBokuFail2($id, $name, $comName, $mName, $point);
            return 0;
        }

        # ���Ǥ˾�����Ѥ�
        if (($island->{'stockflag'} == 55)) {

            if (   ($landKind == $HlandPlains)
                || ($landKind == $HlandSea)
                                            ) {

                # �̾�ΰ��ñۤ�
                my($bck,$sx,$sy);
                $bck = $island->{'pointb'};
                # ��å��������� x y �����
                if($bck =~ s/\((.*),(.*)\)��$//g) {
                    $sx = int($1);
                    $sy = int($2);
                }

                $island->{'pointb'} .= "($x, $y)";
                $land->[$x][$y] = $island->{'stocklandkind'};
                $landValue->[$x][$y] = $island->{'stocklandvalue'};
                $landValue2->[$x][$y] = $island->{'stocklandvalue2'};
                $landValue3->[$x][$y] = $island->{'stocklandvalue3'};

                $island->{'money'} -= $cost;

                logLandSuc($id, $name, $comName, $island->{'pointb'});

                # ���ΰ��֤�ʿ�Ϥˤ���
                $land->[$sx][$sy] = $HlandPlains;
                $landValue->[$sx][$sy] = 0;
                $island->{'stockflag'} = 0;         #���ۺѤ�
                return 1;

            }elsif(   ($landKind == $HlandFrocity)                  # ���ԻԺ���
                   && ($island->{'stocklandkind'} == $HlandBettown)
                   && ($island->{'stocklandvalue'} >= 1000 ) ){
                my($bck,$sx,$sy);
                $bck = $island->{'pointb'};
                # ��å��������� x y �����
                if($bck =~ s/\((.*),(.*)\)��$//g) {
                    $sx = int($1);
                    $sy = int($2);
                }

                $island->{'pointb'} .= "($x, $y)";
                $land->[$x][$y] = $HlandUmicity;
                $landValue->[$x][$y] += $island->{'stocklandvalue'};
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

                $island->{'money'} -= $cost;

                logLandSuc($id, $name, $comName, $island->{'pointb'});

                # ���ΰ��֤�ʿ�Ϥˤ���
                $land->[$sx][$sy] = $HlandPlains;
                $landValue->[$sx][$sy] = 0;
                $landValue2->[$sx][$sy] = 0;
                $landValue3->[$sx][$sy] = 0;
                $island->{'stockflag'} = 0;         #���ۺѤ�
                return 1;

            }elsif(   ($landKind == $HlandOil)                      # �����ԻԺ���
                   && ($island->{'stocklandkind'} == $HlandBettown)
                   && ($island->{'stocklandvalue'} >= 1000 ) ){

                my($bck,$sx,$sy);
                $bck = $island->{'pointb'};
                # ��å��������� x y �����
                if($bck =~ s/\((.*),(.*)\)��$//g) {
                    $sx = int($1);
                    $sy = int($2);
                }

                $island->{'pointb'} .= "($x, $y)";
                $land->[$x][$y] = $HlandOilCity;
                $landValue->[$x][$y] = $island->{'stocklandvalue'};
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

                $island->{'money'} -= $cost;

                logLandSuc($id, $name, $comName, $island->{'pointb'});

                # ���ΰ��֤�ʿ�Ϥˤ���
                $land->[$sx][$sy] = $HlandPlains;
                $landValue->[$sx][$sy] = 0;
                $landValue2->[$sx][$sy] = 0;
                $landValue3->[$sx][$sy] = 0;
                $island->{'stockflag'} = 0;         #���ۺѤ�
                return 1;

            }
            elsif (   ($landKind == $HlandMountain)                  # ����ߤ뤷��
                #   && ($lv == 0)
                   && (0)# �����ɤ�̵��
                   && ($island->{'stocklandkind'} == $HlandEgg) ){
                my($bck,$sx,$sy);
                $bck = $island->{'pointb'};
                # ��å��������� x y �����
                if($bck =~ s/\((.*),(.*)\)��$//g) {
                    $sx = int($1);
                    $sy = int($2);
                }

                $island->{'pointb'} .= "($x, $y)";
                $land->[$x][$y] = $HlandMonument;
                $landValue->[$x][$y] += $island->{'stocklandvalue'};
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

                $island->{'money'} -= $cost;

                logLandSuc($id, $name, $comName, $island->{'pointb'});

                # ���ΰ��֤�ʿ�Ϥˤ���
                $land->[$sx][$sy] = $HlandPlains;
                $landValue->[$sx][$sy] = 0;
                $landValue2->[$sx][$sy] = 0;
                $landValue3->[$sx][$sy] = 0;
                $island->{'stockflag'} = 0;         #���ۺѤ�
                return 1;

            }elsif(   ($landKind == $HlandWaste)                        # �����κ���
                   && ($lv == 2)                                        # ��Ф���
                   && ($island->{'stocklandkind'} == $HlandMonument)    # ����
                   && ($island->{'stocklandvalue'} == 1 )               # ����
                                                            ){

                # ���Ҥ�õ��
                my ($i,$cx,$cy);
                my ($check);
                $check = 0;
                for($i = 1; $i < 7; $i++) {

                    $cx = $x + $ax[$i];
                    $cy = $y + $ay[$i];

                    # ���Ҥ�õ��
                    if(   ($land->[$cx][$cy] == $HlandMonument)
                       && ($landValue->[$cx][$cy] == 27) ){
                        $check = 1;
                        last;
                    }
                }

                if ($check == 1) {

                    my($bck,$sx,$sy);
                    $bck = $island->{'pointb'};
                    # ��å��������� x y �����
                    if($bck =~ s/\((.*),(.*)\)��$//g) {
                        $sx = int($1);
                        $sy = int($2);
                    }

                    $island->{'pointb'} .= "($x, $y)";
                    $land->[$x][$y] = $HlandMonument;
                    $landValue->[$x][$y] = 96;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;

                    $island->{'money'} -= $cost;

                    logLandSuc($id, $name, $comName, $island->{'pointb'});

                    # ���ΰ��֤�ʿ�Ϥˤ���
                    $land->[$sx][$sy] = $HlandPlains;
                    $landValue->[$sx][$sy] = 0;
                    $island->{'stockflag'} = 0;         #���ۺѤ�
                    return 1;

                } else {
                    # Ŭ���ʤ�
                    my ($tmp_point);
                    $tmp_point = $island->{'pointb'};
                    $tmp_point .= "($x, $y)";
                    logLandFail($id, $name, $comName, $landName, $tmp_point);
                    return 0;
                }

            }
            else {
                # Ŭ���ʤ�
                my($tmp_point);
                $tmp_point = $island->{'pointb'};
                $tmp_point .= "($x, $y)";
                logLandFail($id, $name, $comName, $landName, $tmp_point);
                return 0;
            }

        } else {

            $island->{'stocklandkind'} = $land->[$x][$y];
            $island->{'stocklandvalue'} = $landValue->[$x][$y];
            $island->{'stocklandvalue2'} = $landValue2->[$x][$y];
            $island->{'stocklandvalue3'} = $landValue3->[$x][$y];
            $island->{'pointb'} = "($x, $y)��";
            $island->{'stockflag'} = 55;
            return 0;
        }

    }
    elsif($kind == $HcomHouse) {
        # ���β�
        if($island->{'hou'} > 0) {
            # ��Ψ�ѹ�
            $island->{'eisei1'} = $arg;
            logLandSuc($id, $name, $comName, $point);
            return 0;
        } else {
            if(($landKind != $HlandPlains) && ($landKind != $HlandTown)) {
                # ��Ŭ�����Ϸ�
                logLandFail($id, $name, $comName, $landName, $point);
                return 0;
            } else {
                $arg = 5 if(!$arg);
                $island->{'eisei1'} = $arg;
                $land->[$x][$y] = $HlandHouse;
                my $hlv;
                foreach (0..9) {
                    $hlv = 9 - $_;
                    last if($island->{'pts'} > $HouseLevel[$hlv]);
                }
                $landValue->[$x][$y] = $hlv;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                logLandSuc($id, $name, $comName, $point);
                # ��򺹤�����
                $island->{'money'} -= $cost;
                return 1;
            }
        }

    }
    elsif ($kind == $HcomEisei) {
        # �͹������Ǥ��夲
        $arg = 1 if(($arg > 6) || !$arg);
        my $value = $arg * $cost;
        #             ����, ��¬, �޷�, ����, �ɱ�, ����
        my @rocket = (   1,   1,   2,   3,    4, 10);
        my @tech   = (  10,  40, 100, 250, 1000, 2000);
        my @failp  = ( 700, 500, 600, 400,  200, 3000);
        my @failq  = ( 100, 100 , 10,  10,   10, 1);

        if($island->{'m17'} < $rocket[$arg - 1]) { # ���åȤ�$rocket�ʾ�ʤ��ȥ���
            logNoAny($id, $name, $comName, "���åȤ�­��ʤ�");
            return 0;
        } elsif($island->{'rena'} < $tech[$arg - 1]) { # ��������Lv$tech�ʾ�ʤ��ȥ���
            logNoAny($id, $name, $comName, "�������Ѥ�­��ʤ�");
            return 0;
        } elsif($island->{'money'} < $value) {
            logNoAny($id, $name, $comName, "�����­��");
            return 0;
        } elsif(random(10000) > $failp[$arg - 1] + $failq[$arg - 1] * $island->{'rena'}) {
            logEiseifail($id, $name, $comName, $point);
            # ��򺹤�����
            $island->{'money'} -= $value;
            $HSpace_Debris += $HRocketMiss_SpaceDebri;
            return 1;
        }
        my $nkind = 'eis' . $arg;
        $island->{$nkind} = ($arg == 6) ? 250 : 100;
        logPropaganda($id, $name, $comName);
        # ��򺹤�����
        $island->{'money'} -= $value;
        $HSpace_Debris += $HRocket_SpaceDebri;
        return 1;

        # �͹���������
    } elsif($kind == $HcomEiseimente) {
        if ($island->{'m17'} > 0) {
            $arg = 1 if(($arg > 5) || !$arg);
            my $nkind = 'eis' . $arg;
            if($island->{$nkind}) {
                $island->{$nkind} = 150;
                logPropaganda($id, $name, $comName);
            } else {
                logNoAny($id, $name, $comName, "����ο͹��������ʤ�");
                return 0;
            }
            # ��򺹤�����
            $island->{'money'} -= $cost;
            $HSpace_Debris += $HRocket_SpaceDebri;
            return 1;
        }else{

            logNoAny($id, $name, $comName, "���åȤ�­��ʤ�");
            return 0;
        }

        # �����˲�ˤ
    } elsif($kind == $HcomEiseiAtt) {
        my ($aId, %amityFlag);
        foreach $aId (@{$island->{'allyId'}}) {
            foreach (@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}) {
                next if($_ == $id);
                $amityFlag{$_} = $HcampAtk;
            }
        }
        # ��ȯ���֤ʤ饳�ޥ�ɤ�̵��
        if ($HarmisticeTurn && ($HislandTurn <= $HarmisticeTurn || $amityFlag{$target})) {
            # ���⤬���Ĥ���Ƥ��ʤ�
            logNotAvail($id, $name, $comName);
            return 0;
        }
        # �������åȼ���
        my ($tn) = $HidToNumber{$target};
        if ($tn eq '') {
            # �������åȤ����Ǥˤʤ�
            logNoAny($id, $name, $comName, "��ɸ��${AfterName}�˿ͤ���������ʤ�");
            return 0;
        }
        # ��������
        my ($tIsland) = $Hislands[$tn];
        my ($tName) = islandName($tIsland);

        my ($tkind, $eName, $p, $nkind);
        $arg = 1 if (($arg > 6) || !$arg);
        $tkind = 'eis' . $arg;
        my ($eis6, $eis4) = ($island->{'eis6'}, $island->{'eis4'});

        if ($eis6 || $eis4) { # ���쥮��顼������������������

            $eName = $HeiseiName[$arg];
            $p = ($eis6 >= 1) ? 110 : 70;
            if ($tIsland->{$tkind}) {

                if (random(100) < $p - 10 * $arg) {

                    $tIsland->{$tkind} = 0;
                    $HSpace_Debris += $HRocketBroken_SpaceDebri;
                    logEiseiAtts($id, $target, $name, $tName, $comName, $eName);
                }
                else {
                    logEiseiAttf($id, $target, $name, $tName, $comName, $eName);
                }
            }
            else {
                logNoAny($id, $name, $comName, "����ο͹��������ʤ�");
                return 0;
            }

            $nkind = ($eis6 >= 1) ? 'eis6' : 'eis4';
            $island->{$nkind} -= 30;
            if ($island->{$nkind} < 1) {
                $island->{$nkind} = 0;
                logEiseiEnd($id, $name, ($eis6 >= 1) ? $HeiseiName[6] : $HeiseiName[4]);
            }
            # ��򺹤�����
            $island->{'money'} -= $cost;
            return 1;

        } else { # ���쥮��顼�ⷳ��������ʤ����
            logNoAny($id, $name, $comName, "ɬ�פʿ͹��������ʤ�");
            return 0;
        }

    } elsif($kind == $HcomEiseiLzr) {
        # �����졼����
        my($aId, %amityFlag);
        foreach $aId (@{$island->{'allyId'}}) {
            foreach (@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}) {
                next if($_ == $id);
                $amityFlag{$_} = $HcampAtk;
            }
        }
        # ��ȯ���֤ʤ饳�ޥ�ɤ�̵��
        if ($HarmisticeTurn && ($HislandTurn <= $HarmisticeTurn || $amityFlag{$target})) {
            # ���⤬���Ĥ���Ƥ��ʤ�
            logNotAvail($id, $name, $comName);
            return 0;
        }
        my($tn) = $HidToNumber{$target};
        unless(defined $tn) {
            # �������åȤ����Ǥˤʤ�
            logNoAny($id, $name, $comName, "��ɸ��${AfterName}�˿ͤ���������ʤ�");
            return 0;
        }
        # ��������
        my ($tIsland) = $Hislands[$tn];
        my ($tName) = islandName($tIsland);
        my ($tLand) = $tIsland->{'land'};
        my ($tLandValue) = $tIsland->{'landValue'};
        my ($tLandValue2) = $tIsland->{'landValue2'};
        my ($tLandValue3) = $tIsland->{'landValue3'};
        # ����ο͸������ʤ�������ɸ��ο͸������ʤ���BattleField�ʤ顢�¹Ԥϵ��Ĥ���ʤ�
        if(   ($tIsland->{'id'} != $id)
           && (   ($island->{'pop'} < $HguardPop)
               || ($tIsland->{'pop'} < $HguardPop)
               || ($tIsland->{'id'} >100)  )  ) {
            logNoAny($id, $name, $comName, "�¹Ԥ����Ĥ���ʤ�");
            return 0;
        }

        if ($tIsland->{'predelete'}) {
            logNoAny($id, $name, $comName, "�¹Ԥ����Ĥ���ʤ�");
            return 0;
        }

        # ���������ʤ�
        # ���������Ϸ�������
        my ($tL) = $tLand->[$x][$y];
        my ($tLv) = $tLandValue->[$x][$y];
        my ($tLv2) = $tLandValue2->[$x][$y];
        my ($tLv3) = $tLandValue3->[$x][$y];
        my ($tLname) = landName($tL, $tLv, $tLv2);
        my ($tPoint) = "($x, $y)";

        my ($eis6, $eis4) = ($island->{'eis6'}, $island->{'eis4'});

        if ($eis6 || $eis4) { # ���쥮��顼������������������

            LazerAttack($island, $tIsland,$x,$y,$comName,'');

            my ($nkind) = ($eis6 > 0) ? 'eis6' : 'eis4';
            $island->{$nkind} -= (($eis6 > 0) ? 5 : 10);
            if ($island->{$nkind} < 1) {
                $island->{$nkind} = 0;
                logEiseiEnd($id, $name, ($eis6 > 0) ? $HeiseiName[6] : $HeiseiName[4]);
            }
            $island->{'money'} -= $cost;
            return 1;
        } else {
            logNoAny($id, $name, $comName, "ɬ�פʿ͹��������ʤ�");
            return 0;
        }

        # �ߥ������
    }
    elsif (($kind == $HcomMissileNM)  || # �̾�ߥ�����
           ($kind == $HcomMissilePP)  || # PP�ߥ�����
           ($kind == $HcomMissileSPP) || # SPP�ߥ�����
           ($kind == $HcomMissileST)  || # ST�ߥ�����
           ($kind == $HcomMissileSS)  || # �˥ߥ�����
           ($kind == $HcomMissileLR)  || # �Ϸ�δ����
           ($kind == $HcomMissileLD)) {  # Φ���˲���

        my ($NextCommandNotMissile);
        my ($TurnCost);

        $NextCommandNotMissile = 0;
        $TurnCost = 0;

        my ($aId, %amityFlag);
        foreach $aId (@{$island->{'allyId'}}) {
            foreach (@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}) {
                next if($_ == $id);
                $amityFlag{$_} = $HcampAtk;
            }
        }

        if ($HanyMissileMode){#ʣ���ߥ�����ȯ�Ͳ�ǽ�⡼��
            # ���Υ��ޥ�ɤ�ߥ�����Ϥ���
            my ($tempkind);
            $tempkind = $comArray->[0]->{'kind'};
            if (   ($tempkind == $HcomMissileNM)
                || ($tempkind == $HcomMissilePP)
                || ($tempkind == $HcomMissileST)
                || ($tempkind == $HcomMissileSPP)
                || ($tempkind == $HcomMissileLD)
                || ($tempkind == $HcomMissileLR)
                                                ) {
                # �ߥ������
                $NextCommandNotMissile = 0;
            }else{
                $NextCommandNotMissile = 1;
            }
        }else{
            $NextCommandNotMissile = 1;

        }

        # �����ǡ��ߥ���������ȡ����Υ��ޥ�ɤ��ߥ����뤫�ɤ�������롣

        $TurnCost = $NextCommandNotMissile & $island->{'missiled'};

        # ��ȯ���֤ʤ饳�ޥ�ɤ�̵��
        if ($HarmisticeTurn && ($HislandTurn <= $HarmisticeTurn || $amityFlag{$target})) {
            # ���⤬���Ĥ���Ƥ��ʤ�
            logNotAvail($id, $name, $comName);
            return $TurnCost;
        }

        # �������åȼ���
        my($tn) = $HidToNumber{$target};
        unless(defined $tn) {
            # �������åȤ����Ǥˤʤ�
            logNoAny($id, $name, $comName, "��ɸ��${AfterName}�˿ͤ���������ʤ�");
            return $TurnCost;
        }

        my ($flag) = 0;
        if (   (INIT_USE_ARM_SUPPLY)
            && (!$island->{'army'}) ) {
            logNoAny($id, $name, $comName, "����ʪ�񤬤ʤ�");
            return $TurnCost;
        }

        if (   (!$arg)
            || (   (INIT_USE_ARM_SUPPLY)
                && ($arg > $island->{'army'}))) {
            # 0���ޤ��ϡ�����ʪ����¿�����
            $arg = (INIT_USE_ARM_SUPPLY) ? $island->{'army'} : 100;
            # �ң���Max��100ȯ�ߤ����Ǥ�
        }

        # ��������
        my ($tIsland) = $Hislands[$tn];
        my ($tName) = islandName($tIsland);
        my ($tLand) = $tIsland->{'land'};
        my ($tLandValue) = $tIsland->{'landValue'};
        my ($tLandValue2) = $tIsland->{'landValue2'};
        my ($tLandValue3) = $tIsland->{'landValue3'};
        my ($tx, $ty, $err);

        # BattleField�Ǥʤ��ơ�����ο͸������ʤ�������ɸ��ο͸������ʤ��ʤ顢�¹Ԥϵ��Ĥ���ʤ�
        if(   ($tIsland->{'id'} <= 100)
           && ($tIsland->{'BF_Flag'} == 0)
           && ($tIsland->{'id'} != $id)
           && (   ($island->{'pop'} < $HguardPop)
               || ($tIsland->{'pop'} < $HguardPop)) ) {
            logNoAny($id, $name, $comName, "�¹Ԥ����Ĥ���ʤ�");
            return $TurnCost;
        }

        if ($tIsland->{'predelete'}) {

            logNoAny($id, $name, $comName, "�¹Ԥ����Ĥ���ʤ�");
            return $TurnCost;
        }

        # �Хȥ�ե�����ɤؤΥߥ���������å�
        if ( $tIsland->{'BF_Flag'} ) {
            if ( $island->{'BF_Missile'} >= $HBF_Missile_Limit ) {
                logNoAny($id, $name, $comName, "�¹Ԥ����Ĥ���ʤ�(�Хȥ�ե�����ɾ��30)");

                return $TurnCost;
            }
        }

        # ��
        if($kind == $HcomMissilePP) { # PP�ߥ�����
            $err = 7;
        } elsif($kind == $HcomMissileSS) { # �˥ߥ�����
            $err = 7;
        } elsif($kind == $HcomMissileSPP) { # SPP�ߥ�����
            $err = 1;
        } else {
            $err = 19;
        }

        # BattleField�ʤ顢@HkindBFM�ʳ��ϵ��Ĥ���ʤ�
        my $flagBFM = 1;
        foreach (@HkindBFM) {
            if($kind == $_) {
                $flagBFM = 0;
                last;
            }
        }

        if (   ($tIsland->{'id'} > 100)
            || ($tIsland->{'BF_Flag'}) ) {

            if ($flagBFM) {
                logNoAny($id, $name, $comName, "���Ĥ���Ƥ��ʤ�����Υߥ�����Ǥ���");
                return $TurnCost;
            }
        }
        elsif(   ($HtargetMonster)
                && ($tIsland->{'id'} != $id)
                && (!countAround($tLand, $x, $y, $err, $HlandMonster, $HlandRottenSea)) ) {
            # ������˲��á��峤���ʤ���С�ȯ�����
            logNoTarget($id, $name, $comName);
            return $TurnCost;
        }

        # ��̱�ο�
        my ($boat) = 0;

        my ($mukou, $bouei, $kaijumukou, $kaijuhit, $total, $fuhatu, $alltotal) =
           (0     , 0     , 0          , 0        , 0     , 0      , 0);

        # �⤬�Ԥ��뤫�������­��뤫������������Ĥޤǥ롼��
        my ($bx, $by, $count) = (0,0,0);

        while (($arg > 0) && ($island->{'money'} >= $cost)) {
            # ���Ϥ򸫤Ĥ���ޤǥ롼��
            while($count < $HpointNumber) {
                $bx = $Hrpx[$count];
                $by = $Hrpy[$count];
                last if(($land->[$bx][$by] == $HlandBase) || ($land->[$bx][$by] == $HlandSbase));
                $count++;
            }
            last if($count > $pointNumber); # ���Ĥ���ʤ��ä��餽���ޤ�

            $flag = 1; # �����Ĵ��Ϥ����ä��Τǡ�flag��Ω�Ƥ�

            # ���ϤΥ�٥�򻻽�
            my ($missiles) = $island->{'missiles'}->[$bx][$by];
            my ($level) = expToLevel($land->[$bx][$by], $landValue->[$bx][$by]) - $missiles;
            if ($level <= 0) { $count++; next; }; # ���δ��Ϥ�����ȯ�ͤ��Ƥ���

            my ($tid);      # Ũ����ID

            # ������ǥ롼��
            while (   ($level > 0)
                   && ($arg > 0)
                   && ($island->{'money'} > $cost) ) {

                $tid = $tIsland->{'id'};        #id ���ԡ�

                if (random(300) < $alltotal-int($island->{'rena'}/100)) {
                    $level--;
                    $arg--;
                    $island->{'money'} -= $cost;
                    $total++;
                    $alltotal++;
                    $fuhatu++;
                    # ����ʪ��򸺤餹
                    $island->{'army'}-- if($HuseArmSupply);
                    last if (!$level || !$arg || ($island->{'money'} < $cost));
                }

                if ($kind != $HcomMissileST) {
                    $island->{'ext'}[1] += $cost; # �׸���
                    $island->{'ext'}[6]++; # ȯ�ͤ����ߥ�����ο�
                    if ($HallyNumber) {
                        foreach (@{$island->{'allyId'}}) {
                            $Hally[$HidToAllyNumber{$_}]->{'ext'}[0]++ if ( ($tIsland->{'BF_Flag'} == 0 ) );
                        }
                    }
                }

                if ($HallyNumber) {
                    my ($allyflag) = 0;
                    my ($ai);
                    foreach $ai (@{$island->{'allyId'}}) {
                        foreach (@{$tIsland->{'allyId'}}) {
                            if($_ == $ai) {
                                $allyflag = 1;
                                last;
                            }
                        }
                    }
                    if ($allyflag) {
                        # ̣���˷⤿�줿���׸��٥ޥ��ʥ�(�������ߥ�����ο��ϥ�����Ȥ��ʤ�)
                        $tIsland->{'ext'}[1] -= $cost; # �׸���
                    }
                    else {
                        # Ũ�˷⤿�줿���׸��٥ץ饹
                        $tIsland->{'ext'}[1] += $cost; # �׸���
                        $tIsland->{'ext'}[5]++; # �������ߥ�����ο�
                    }
                    foreach (@{$tIsland->{'allyId'}}) {
                        $Hally[$HidToAllyNumber{$_}]->{'ext'}[1]++ if ( ($tIsland->{'BF_Flag'} == 0 ) );
                    }
                }


                # ��ä��Τ�����ʤΤǡ����ͤ���פ�����
                $level--;
                $missiles++;
                $arg--;
                $island->{'money'} -= $cost;
                $island->{'missiled'} = 1;
                $total++;
                $alltotal++;
                # ����ʪ��򸺤餹
                $island->{'army'}-- if($HuseArmSupply);


                if ( $tIsland->{'BF_Flag'} ) {
                    if ( $island->{'BF_Missile'} >= $HBF_Missile_Limit ) {
                        logNoAny($id, $name, $comName, "�¹Ԥ����Ĥ���ʤ�(�Хȥ�ե�����ɾ��$HBF_Missile_Limit)");
                        return 1;

                    }
                    else {
                        $island->{'BF_Missile'} ++ ;
                    }
                }

                # ����������
                my ($r) = random($err);
                $tx = $x + $ax[$r];
                $ty = $y + $ay[$r];
                $tx-- if((($ty % 2) == 0) && (($y % 2) == 1));

                # �������ϰ��⳰�����å�
                if (($tx < 0) || ($tx > $islandSize) || ($ty < 0) || ($ty > $islandSize)) {
                    # �ϰϳ�
                    $mukou++;
                    next;
                }

                if ( !$tIsland->{'BF_Flag'} ) {
                    $tIsland->{'missileAlert'} = 1;
                }

                # ���������Ϸ�������
                my ($tL) = $tLand->[$tx][$ty];
                my ($tLv) = $tLandValue->[$tx][$ty];
                my ($tLv2) = $tLandValue2->[$tx][$ty];
                my ($tLv3) = $tLandValue3->[$tx][$ty];
                my ($tLname) = landName($tL, $tLv,$tLv2,$tLv3);
                my ($tPoint) = "($tx, $ty)";

                # �ɱһ���Ƚ��
                my ($defence) = 0;
                my ($defper) = 0;

                if (($HdefenceHex[$tid][$tx][$ty] == 1) && !($HdBaseSelfNoDefence) ) {
                    $defence = 1;
                } elsif ($HdefenceHex[$tid][$tx][$ty] == -1) {
                    $defence = 0;
                } else {

                    if(   (!($HdBaseSelfDefence)) 
                       && (   ($tL == $HlandDefence)
                           || (   ($tL == $HlandProcity)
                               && ($tLv < 160) )
                                                )) {
                        # �ɱһ��ߡ��ɱ��ԻԤ�̿��
                        my($defLv , $defHP ,$defper);

                        $defence = 1;
                        $defHP = 0;
                        $defLv = 0;

                        $defper = -1; # �μ¤�̿��
                        if($tL == $HlandDefence) {
                            # �ɱһ��ߤ�̿��

                            $defLv = ($tLv & $HDefenceLevelMask) ;

                            if ($kind == $HcomMissileSPP) {
                                # SPP�ߥ�����

                                if (   !($HdBaseSelfNoDefence) 
                                    ||  ($id != $tIsland->{'id'}) 
                                                                ) {
                                    $defper = $HdNoPerfectP;
                                    if($HdBaseNoPerfect){

                                        $defper = $HdNoPerfectP;
                                        if ( $defLv >=2 ) {
                                            $defHP = 0;
                                            $defHP = $lv >> $HDefenceHP_SHIFT;
                                            $defper = $defper - ( $defHP * 2);
                                        }
                                    }
                                }
                            }
                        }

                        if (   ($defLv >= 2)
                            && (random(100) < $defper) ) {

                            $defHP = $tLv >> $HDefenceHP_SHIFT;
                            $defHP = $defHP - 4;
                            $defHP = 0 if ( $defHP < 0 );
                            $tLandValue->[$tx][$ty] = $defLv + ( $defHP << $HDefenceHP_SHIFT ) ;
                        }

                        if ( $defHP <= 0 ) {
                            # �ե饰�򥯥ꥢ
                            $defence = 0;
                            my($i, $count, $sx, $sy);
                            for($i = 0; $i < 19; $i++) {
                                $sx = $tx + $ax[$i];
                                $sy = $ty + $ay[$i];

                                # �Ԥˤ�����Ĵ��
                                $sx-- if(!($sy % 2) && ($ty % 2));
                                # �ϰ���ξ��
                                $HdefenceHex[$tid][$sx][$sy] = 0 if(($sx >= 0) && ($sx < $HislandSize) && ($sy >= 0) && ($sy < $HislandSize));
                            }
                            if(($tL == $HlandDefence) && ($kind != $HcomMissileST)) {
                                $island->{'ext'}[2]++; # �˲������ɱһ��ߤο�
                            }
                        }

                    } elsif(countAround($tLand, $tx, $ty, 19, $HlandDefence)) {
                        if((!$HdBaseSelfNoDefence) || ($id != $tIsland->{'id'})) {
                            $HdefenceHex[$tid][$tx][$ty] = 1;
                            $defence = 1;
                            #$defence = 0 if($HdBaseNoPerfect && (random(100) < $HdNoPerfectP));
                        }

                    } elsif(countAround($tLand, $tx, $ty, 7, $HlandProcity)) {

                        if(!($HdProcitySelfNoDefence) || ($id != $tIsland->{'id'})) {
                            $HdefenceHex[$tid][$tx][$ty] = 1;
                            $defence = 1;
                            #$defence = 0 if($HdProcityNoPerfect && (random(100) < $HdNoPerfectP));
                        }

                    } elsif(countAround($tLand, $tx, $ty, 1, $HlandHouse)) {
                        $HdefenceHex[$tid][$tx][$ty] = 1;
                        $defence = 1;

                    } elsif(countAround($tLand, $tx, $ty, 7, $HlandShuto)) {
                        if(!($HdProcitySelfNoDefence) || ($id != $tIsland->{'id'})) {
                            $HdefenceHex[$tid][$tx][$ty] = 1;
                            $defence = 1;
                        }
                    } else {
                        $HdefenceHex[$tid][$tx][$ty] = -1;
                        $defence = 0;
                    }
                }

                if($defence == 1) {
                    # ��������
                    $bouei++;
                    $tIsland->{'ext'}[7]++; # �ɱһ��ߤ��Ƥ����ߥ�����ο�
                    next;
                }

                if($tIsland->{'eis5'}) { # �ɱұ�����������
                    if(random(5000) < $tIsland->{'rena'}) {
                        $tIsland->{'eis5'} -= 2;
                        if($tIsland->{'eis5'} < 1) {
                            $tIsland->{'eis5'} = 0;
                            logEiseiEnd($target, $tName, $HeiseiName[5]);
                        }
                        $bouei++;
                        next;
                    }
                }

                # �ָ��̤ʤ���hex��ǽ��Ƚ��
                if(($kind != $HcomMissileLR) &&                     # �Ϸ�δ���ƤǤʤ���
                    ((($tL == $HlandSea) && ($tLv == 0)) ||         # ������
                    ((($tL == $HlandSea)     ||                     # ���ޤ��ϡ�����
                      ($tL == $HlandSbase)    ||                      # ������Ϥޤ��ϡ�����
                      ($tL == $HlandSeacity) ||                     # �����ԻԤޤ��ϡ�����
                      ($tL == $HlandSeatown) ||                     # ���쿷�ԻԤޤ��ϡ�����
                      ($tL == $HlandUmishuto) ||                    # �����Ԥޤ��ϡ�����
                      ($tL == $HlandUmiamu)  ||                     # �����ߤ�ޤ��ϡ�����
                      ($tL == $HlandGold)    ||                      # �⻳�ޤ��ϡ�����
                      ($tL == $HlandShrine)  ||                     # ���ο��¤ޤ��ϡ�����
                      ($tL == $HlandMountain))                      # ���ǡ�����
                     && ($kind != $HcomMissileLD)))){               # Φ���ƤǤ�ʤ�

                    # ������ϡ������Իԡ����쿷�ԻԤξ�硢���Υե�
                    if(isBehindSea($tL)) {
                        $tL = $HlandSea;
                    }
                    $tLname = landName($tL, $tLv, $tLv2);

                    # ̵����
                    $mukou++;
                    next;
                }

                # �Ƥμ����ʬ��
                if ($kind == $HcomMissileLR) {
                    # �Ϸ�δ����

                    if (   ($tL == $HlandMountain)
                        || ($tL == $HlandGold)
                        || ($tL == $HlandShrine)
                                                 ) {
                        # �������ο��¤����Ƥ������̵��
                        $mukou++;
                        next;

                    } elsif (   ($tL == $HlandSbase)
                             || ($tL == $HlandSeacity)
                             || ($tL == $HlandSeatown)
                             || ($tL == $HlandUmishuto)
                             || ($tL == $HlandOil)
                             || ($tL == $HlandFune)
                             || ($tL == $HlandFrocity)
                             || ($tL == $HlandUmiamu)
                                                        ) {
                        # ������ϡ������Իԡ����쿷�Իԡ����ġ����������ߤ�ʤ顢��Ū�ξ��������ˤ���
                        SetSeaShallowLand($tIsland,$tx,$ty);
                        logMsLSbase($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "δ�����������ˤʤ�ޤ�����");
                        next;

                    } elsif($tL == $HlandRottenSea) {
                        # �峤�ʤ顢��Ū�ξ��򻳤ˤ���
                        SetMountain_Normal($tIsland,$tx,$ty);
                        logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "�峤��δ�������ˤʤ�ޤ�����");
                        next;

                    } elsif(($tL == $HlandSea) || ($tL == $HlandIce)) {
                        if(($tLv == 1) || ($tL == $HlandIce)){
                            # �����ξ��
                            SetWasteLand_Normal($tIsland,$tx,$ty);     # $HlandWaste
                            $tIsland->{'area'}++;
                            logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "δ�������ϤȤʤ�ޤ�����");

                            my($seaCount) = countAround($tLand, $tx, $ty, 7, @Hseas);
                            if($seaCount <= 4) {
                            # ����γ���3�إå�������ʤΤǡ������ˤ���
                                my($i, $sx, $sy);
                                for($i = 1; $i < 7; $i++) {
                                    $sx = $x + $ax[$i];
                                    $sy = $y + $ay[$i];

                                    # �Ԥˤ�����Ĵ��
                                    $sx-- if(!($sy % 2) && ($y % 2));

                                    if(($sx >= 0) && ($sx < $HislandSize) && ($sy >= 0) && ($sy < $HislandSize) &&
                                        ($tLand->[$sx][$sy] == $HlandSea)) {
                                        # �ϰ���ξ��
                                        $tLandValue->[$sx][$sy] = 1;
                                    }
                                }
                            }
                            next;

                        } else {
                            # ���ʤ顢��Ū�ξ��������ˤ���
                            SetSeaShallowLand($tIsland,$tx,$ty);
                            logMsLSbase($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "δ�����������ˤʤ�ޤ�����");
                            next;
                        }

                    } elsif($tL == $HlandMonster){
                        my($mKind, $mName, $mHp) = monsterSpec($tLv);
                        if (isSeaMonster($mKind)){        # ���β���
                            # ���ʤ顢��Ū�ξ��������ˤ���
                            SetSeaShallowLand($tIsland,$tx,$ty);
                            logMsLSbase($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "δ�����������ˤʤ�ޤ�����");
                            next;

                        }else{
                            # ���äʤ�
                            logMsLMonster($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "δ������������ޤ�����");
                            # ���ˤʤ�
                            SetMountain_Normal($tIsland,$tx,$ty);
                            next;
                        }
                    } elsif(   ($tL == $HlandTown)
                            || ($tL == $HlandMinato)
                            || ($tL == $HlandNewtown)
                            || ($tL == $HlandOnsen)
                            || ($tL == $HlandBigtown)
                                                        ) {
                        # �Իԡ������˥塼�����󡢸����ԻԤξ��
                        if(($land->[$bx][$by] == $HlandBase) ||
                            ($land->[$bx][$by] == $HlandSbase)) {
                            # �и���
                            # �ޤ����Ϥξ��Τ�
                            $landValue->[$bx][$by] += int($tLv / 20);
                            $landValue->[$bx][$by] = $HmaxExpPoint if($landValue->[$bx][$by] > $HmaxExpPoint);
                        }
                        logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "δ������������ޤ�����");
                        # ���ˤʤ�
                        SetMountain_Normal($tIsland,$tx,$ty);
                        if (random(1000) < 22) {
                            SetMonument_Normal($tIsland,$tx,$ty,75);
                        }
                        next;
                    } else {
                        # ����¾
                        logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "δ������������ޤ�����");
                        # ���ˤʤ�
                        SetMountain_Normal($tIsland,$tx,$ty);
                        if (random(1000) < 22) {
                            SetMonument_Normal($tIsland,$tx,$ty,75);
                        }
                        next;
                    }
                    # �Ϸ�δ���Ƥ����ޤ�

                } elsif($kind == $HcomMissileSS) {
                    # �˥ߥ�����
                    logMsSS($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint);
                    wideDamageli($target, $tName, $tLand, $tLandValue,$tLandValue2, $tx, $ty);

                } elsif($kind == $HcomMissileLD) {
                    # Φ���˲���
                    if (($tL == $HlandMountain) || ($tL == $HlandGold) || ($tL == $HlandShrine) || ($tL == $HlandOnsen)) {
                        # ��(���Ϥˤʤ�)
                        logMsMonster($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "�ä����ӡ����ϤȲ����ޤ�����");
                        # ���Ϥˤʤ�
                        SetWasteLand_Normal($tIsland,$tx,$ty);
                        next;

                    } elsif(($tL == $HlandSbase)    ||
                            ($tL == $HlandFune)    ||
                            ($tL == $HlandFrocity)  ||
                            ($tL == $HlandUmiamu)  ||
                            ($tL == $HlandSeatown) ||
                            ($tL == $HlandUmishuto) ||
                            ($tL == $HlandSeacity)) {
                        # ������ϡ����������ߤ塢�����Իԡ����쿷�Ի�
                        logMsLSbase($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "�׷���ʤ��᤭���Ӥޤ�����");

                    } elsif ($tL == $HlandMonster) {
                        # ����
                        my($mKind, $mName, $mHp) = monsterSpec($tLv);
                        if ($mKind == $Mons_Unbaba){
                            #����ХФˤ�ʹ���ʤ�
                        }else{
                            logMsLMonster($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "���פ��ޤ�����");
                        }
                    } elsif($tL == $HlandRottenSea) {
                        # �峤
                        logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "�峤�ϳ������ߤޤ�����");
                    } elsif(($tL == $HlandSea) || ($tL == $HlandIce)) {
                        # ����
                        logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "���줬�������ޤ�����");
                    } else {
                        # ����¾
                        logMsLOther($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "Φ�ϤϿ��פ��ޤ�����");
                    }

                    if (($tL == $HlandTown)    ||
                        ($tL == $HlandMinato)  ||
                        ($tL == $HlandNewtown) ||
                        ($tL == $HlandBigtown)) {
                        # �Իԡ������˥塼�����󡢸����ԻԤξ��
                        if(($land->[$bx][$by] == $HlandBase) ||
                            ($land->[$bx][$by] == $HlandSbase)) {
                            # �и���
                            # �ޤ����Ϥξ��Τ�
                            $landValue->[$bx][$by] += int($tLv / 20);
                            $landValue->[$bx][$by] = $HmaxExpPoint if($landValue->[$bx][$by] > $HmaxExpPoint);
                        }
                    }

                    if ( !isSeaMonster($mKind) ){     #���β��äǤʤ�
                        # �����ˤʤ�
                        $tIsland->{'area'}--;
                        SetSeaShallowLand($tIsland,$tx,$ty);
                        # �Ǥ����ġ�������������Ϥ��ä��鳤
                        if(($tL == $HlandOil)     ||
                            ($tL == $HlandSea)     ||
                            ($tL == $HlandSeacity) ||
                            ($tL == $HlandIce) ||
                            ($tL == $HlandSeatown) ||
                            ($tL == $HlandUmishuto)    ||
                            ($tL == $HlandFune)    ||
                            ($tL == $HlandFrocity)  ||
                            ($tL == $HlandUmiamu)  ||
                            ($tL == $HlandSbase)) {
                            SetSeaLand_Normal($tIsland,$tx,$ty);
                        }
                    }
                    # Φ���˲��Ƥ����ޤ�

                } else {

                    # ����¾�ߥ�����
                    if (($tL == $HlandWaste) || ($tL == $HlandYougan)) {
                        $mukou++;

                    } elsif ($tL == $HlandRottenSea) {
                        # �峤
                        if ($kind == $HcomMissileST) {
                            # ���ƥ륹
                            logMsNormalS($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "�峤�ϾƤ�ʧ���ޤ�����");
                        } else {
                            # �̾�
                            logMsNormal($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "�峤�ϾƤ�ʧ���ޤ�����");
                        }

                    } elsif ($tL == $HlandMonster) {
                        # ����
                        my ($mKind, $mName, $mHp) = monsterSpec($tLv);

                        # �Ų���?
                        if (isMonsterCuring($mKind)) {
                            # �Ų���
                            $kaijumukou++;
                            next;

                        } else {
                            # �Ų��椸��ʤ�

                            my ($special) = $HmonsterSpecial[$mKind];
                            my $rflag = random(1000)+$island->{'co4'}*100+$island->{'co99'}*100;
                            if((($special == 5) || ($mKind == 15)) && ($rflag < $HmonsterDefence)){
                                $kaijumukou++;
                                next;

                            } elsif(   ($mKind == $Mons_Mikael   && $rflag < 900)
                                    || ($mKind == $Mons_Ethereal && $rflag < 300)
                                    || ($mKind == $Mons_Satan    && $rflag < 200)
                                    || ($mKind == $Mons_Ice_scorpion && $rflag < 250)
                                    || ($mKind == $Mons_Volgenom && $rflag < 500)
                                    || ($mKind == $Mons_Kisinhei && $rflag < (500))
                                    || ($mKind == $Mons_Retro_inora && $rflag < 100)
                                    || ($mKind == $Mons_Uriel && $rflag < (100+random(400)))
                                    || ($mKind == $Mons_SuperTetra && $rflag < (800+random(50)))
                                    || ($mKind == $Mons_Alfr && $rflag < (400+random(400)))
                                    || ($mKind == $Mons_SlimeLegend && $rflag < 100)
                                    || ($mKind == $Mons_f20 && $rflag < (400+random(500)))
                                                                                            ) {
                                $kaijumukou++;
                                next;
                            }

                            if($mHp == 1) {
                                # ���ä��Ȥ᤿
                                if(($land->[$bx][$by] == $HlandBase) ||
                                    ($land->[$bx][$by] == $HlandSbase)) {
                                    # �и���
                                    $landValue->[$bx][$by] += $HmonsterExp[$mKind];
                                    $landValue->[$bx][$by] = $HmaxExpPoint if($landValue->[$bx][$by] > $HmaxExpPoint);
                                }

                                if($kind == $HcomMissileST) {
                                    # ���ƥ륹
                                    logMsMonsterS($id, $target, $name, $tName, $comName, $mName, $point, $tPoint, "�ϿԤ����ݤ�ޤ�����");
                                } else {
                                    # �̾�
                                    logMsMonster($id, $target, $name, $tName, $comName, $mName, $point, $tPoint, "�ϿԤ����ݤ�ޤ�����");
                                }

                                if ($mKind == $Mons_Omu) { # ������ʤ�
                                    # �峤ȯ��
                                    my($point) = "($tx, $ty)";
                                    logRottenSeaBorn($id, $tName, $point);
                                    SetRottenSea($tIsland , $tx , $ty);
                                }

                                if ($mKind != $Mons_Omu) { # ������Ǥʤ�

                                    # ����
                                    my ($value) = $HmonsterValue[$mKind];

                                    if ($value > 0) {

                                        if (   ( $tIsland->{'id'} <= 100)
                                            && (!$tIsland->{'BF_Flag'})
                                                                        ) {
                                            $tIsland->{'money'} += $value;
                                            logMsMonMoney($target, $mName, $value);

                                        } else {

                                            $island->{'money'} += $value;
                                            $island->{'landscore'} += $HmonsterBHP[$mKind] if ( $kind != $HcomMissileSPP );
                                            logMsMonMoney($id, $mName, $value);
                                        }

                                        if(!$tIsland->{'BF_Flag'}){

                                            Sinden_Omaturi($island , $HmonsterValue[$mKind] , 101);

                                            # ����
                                            Jinja_Omaturi($island , $HmonsterValue[$mKind] , 101);
                                        }
                                    }
                                }

                                # �����༣
                                TaijiPrize($island , $mKind);

                                next if ($mKind == $Mons_Omu);      # ������Ϥ����ǽ����ˤ���

                            } else {

                                $island->{'landscore'}++ if ( ($tIsland->{'BF_Flag'} == 1 ) && ( $kind != $HcomMissileSPP ));
                                # ���������Ƥ�
                                $kaijuhit++;
                                # HP��1����
                                $tLandValue->[$tx][$ty]--;
                                next;
                            }
                        }

                    }
                    else {
                        # �̾��Ϸ�
                        if ($kind == $HcomMissileST) {
                            # ���ƥ륹
                            logMsNormalS($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "���Ӥ����Ǥ��ޤ�����");
                        }
                        else {
                            # �̾�
                            logMsNormal($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "���Ӥ����Ǥ��ޤ�����");
                            $island->{'ext'}[3]++ if ($tL == $HlandBase); # ���ˤ����ߥ�������Ϥο�
                        }
                    }

                    # �и���
                    if (   ($tL == $HlandTown)
                        || ($tL == $HlandMinato)
                        || ($tL == $HlandNewtown)
                        || ($tL == $HlandProcity)
                        || ($tL == $HlandBigtown)
                        || ($tL == $HlandBettown)
                                                  ) {

                        if (   ($land->[$bx][$by] == $HlandBase)
                            || ($land->[$bx][$by] == $HlandSbase)  ) {

                            $landValue->[$bx][$by] += int($tLv / 20);
                            $boat += $tLv; # �̾�ߥ�����ʤΤ���̱�˥ץ饹
                            $landValue->[$bx][$by] = $HmaxExpPoint if($landValue->[$bx][$by] > $HmaxExpPoint);
                        }
                    }

                    my ($mKind, $mName, $mHp) = monsterSpec($tLv);

                    # ���Ϥˤʤ�
                    if ($tL == $HlandMonster) {
                        MonsterDead( $tIsland , $tx , $ty , $mKind , 1 );
                    }else{
                        MonsterDown( $tIsland , $tx , $ty , $mKind , 1 );

                    }

                    if (   ($mKind == 17)
                        && ($tL == $HlandMonster) ) {
                        SetMonument_Normal($tIsland , $tx , $ty , 86);
                    }

                    # ��ˡ��
                    if (   ( ($tL == $HlandMonument) && ($tLv == 25) )
                        && (random(10000) < $island->{'rena'}) && ($island->{'rena'} > 2000)
                                                                                            ) {

                        my ($lv2,$lv);
                        ($kind,$lv2) = MonsterSpawnKind($tIsland , 0);
                        $lv = ($kind << $Mons_Kind_Shift) + $HmonsterBHP[$kind] + random($HmonsterDHP[$kind]);
                        $tLand->[$tx][$ty] = $HlandMonster;
                        $tLandValue->[$tx][$ty] = $lv;
                        $tLandValue2->[$tx][$ty] = $lv2;
                        $tLandValue3->[$tx][$ty] = 0;
                        $tIsland->{'monsterlive'}++;
                        # ���þ���
                        my($mKind, $mName, $mHp) = monsterSpec($lv);

                        # ��å�����
                        logMonsComemagic($id, $tIsland->{'name'}, $mName, "($bx, $by)", '');
                    }

                    # ������
                    if (   ($tLv == 70)
                        && ($tL == $HlandMonument)  ) {

                        SetMonument_Normal($tIsland , $tx , $ty , 70);
                    }

                    # �Ǥ����Ĥ��ä��鳤
                    if (   ($tL == $HlandOil)
                        || ($tL == $HlandFrocity)
                        || ($tL == $HlandUmicity)
                        || ($tL == $HlandOilCity)
                        || ($tL == $HlandFune) ) {

                        $tLand->[$tx][$ty] = $HlandSea;
                        $tLandValue->[$tx][$ty] = 0;

                    } elsif(($tL == $HlandNursery) || ($tL == $HlandIce)) {
                        # �Ǥ��ܿ���ʤ�����
                        $tLand->[$tx][$ty] = $HlandSea;
                        $tLandValue->[$tx][$ty] = 1;
                    } elsif($tL == $HlandOnsen) {
                        # �Ǥⲹ���ʤ黳
                        $tLand->[$tx][$ty] = $HlandMountain;
                        $tLandValue->[$tx][$ty] = 0;
                    }
                }
            }

            # ���δ��ϤΥߥ�����ȯ�Ϳ��򵭲�����
            $island->{'missiles'}->[$bx][$by] = $missiles;
            # ����������䤷�Ȥ�
            $count++;
        }

        # ��
        if ($kind == $HcomMissileST) {
            # ���ƥ륹
            logMsTotalS($id, $target, $name, $tName, $comName, '', $point, $tPoint, $total, $mukou, $bouei, $kaijumukou, $kaijuhit, $fuhatu);
        } else {
            # �̾�
            logMsTotal($id, $target, $name, $tName, $comName, '', $point, $tPoint, $total, $mukou, $bouei, $kaijumukou, $kaijuhit, $fuhatu);
        }

        if (!$flag) {
            # ���Ϥ���Ĥ�̵���ä����
            logMsNoBase($id, $name, $comName);
            return 0;
        }

        # ��̱Ƚ��
        $boat = int($boat / 2);
        if ($boat && ($id != $target) && ($kind != $HcomMissileST)) {
            # ��̱ɺ��
            my($achive); # ��ã��̱
            my($i);
            my($pop_limit);
            $achive = 0;

            for($i = 0; ($i < $HpointNumber && $boat > 0); $i++) {
                $bx = $Hrpx[$i];
                $by = $Hrpy[$i];

                if (   ($land->[$bx][$by] == $HlandTown)
                    || ($land->[$bx][$by] == $HlandNewtown)
                    || (($land->[$bx][$by] == $HlandBigtown) && ($island->{'yaku'} >= 4))
                    || (($land->[$bx][$by] == $HlandBettown) && ($island->{'yaku'} >= 6))
                                                                                            ) {

                    $pop_limit = $HTown_limit if($land->[$bx][$by] == $HlandTown);
                    $pop_limit = $HNewtown_limit if($land->[$bx][$by] == $HlandNewtown);
                    $pop_limit = $HBigtown_limit if($land->[$bx][$by] == $HlandBigtown);
                    $pop_limit = $HBettown_limit if($land->[$bx][$by] == $HlandBettown);

                    # Į�ξ��
                    my ($lv) = $landValue->[$bx][$by];
                    if ($boat > 50) {

                        $lv += 50;
                        $boat -= 50;
                        $achive += 50;
                    } else {

                        $lv += $boat;
                        $achive += $boat;
                        $boat = 0;
                    }

                    if ($lv > $pop_limit) {

                        $boat += ($lv - $pop_limit);
                        $achive -= ($lv - $pop_limit);
                        $lv = $pop_limit;
                    }

                    $landValue->[$bx][$by] = $lv;

                } elsif (   ($land->[$bx][$by] == $HlandPlains)
                         && ($landValue->[$bx][$by] == 0 )) {    # ��̱ɺ��
                    # ʿ�Ϥξ��
                    if ( $landValue->[$bx][$by] == 0 ){
                        $land->[$bx][$by] = $HlandTown;

                        if($boat > 10) {
                            $landValue->[$bx][$by] = 5;
                            $boat -= 10;
                            $achive += 10;

                        } elsif($boat > 5) {
                            $landValue->[$bx][$by] = $boat - 5;
                            $achive += $boat;
                            $boat = 0;
                        }
                    }
                }
                last if($boat <= 0);
            }

            if ($achive > 0) {
                # �����Ǥ����夷����硢�����Ǥ�
                logMsBoatPeople($id, $name, $achive);
                $island->{'ext'}[4] += int($achive); # �߽Ф�����̱�ι�׿͸�

                # ��̱�ο���������ʾ�ʤ顢ʿ�¾ޤβ�ǽ������
                if ($achive >= 200) {

                    my ($prize) = $island->{'prize'};
                    my ($prize1, $prize2) = split(/\t/, $prize);
                    $prize1 =~ /([0-9]*),([0-9]*),(.*)/;
                    my ($flags) = $1;
                    my ($monsters) = $2;
                    my ($turns) = $3;

                    if (    (!($flags & 8))
                        &&  ($achive >= 200) ) {

                        $flags |= 8;
                        logPrize($id, $name, $Hprize[4]);
                    } elsif((!($flags & 16)) &&  $achive > 500){
                        $flags |= 16;
                        logPrize($id, $name, $Hprize[5]);
                    } elsif((!($flags & 32)) &&  $achive > 800){
                        $flags |= 32;
                        logPrize($id, $name, $Hprize[6]);
                    }
                    $island->{'prize'} = "$flags,$monsters,$turns\t$prize2";
                }
            }
        }

        if (   ($HanyMissileMode) ){  #ʣ���ߥ�����ȯ�Ͳ�ǽ�⡼��
            # ���Υ��ޥ�ɤ�ߥ�����Ϥ���
            my ($kind2) = $comArray->[0]->{'kind'};
            if (   (   ($kind2 == $HcomMissileNM)
                    || ($kind2 == $HcomMissilePP)
                    || ($kind2 == $HcomMissileST)
                    || ($kind2 == $HcomMissileSPP)
                    || ($kind2 == $HcomMissileLD)
                    || ($kind2 == $HcomMissileLR) )
                && ($kind != $HcomMissileSS)
                                                ) {
                # �ߥ������

                # �ߥ�����ȯ�Ϳ��˻Ĥ꤬���뤫Ĵ�٤�
                my($flag);
                $count--;
                while ($count < $HpointNumber) {
                    $bx = $Hrpx[$count];
                    $by = $Hrpy[$count];
                    if(($land->[$bx][$by] == $HlandBase) ||
                        ($land->[$bx][$by] == $HlandSbase)) {
                        $flag = expToLevel($land->[$bx][$by], $landValue->[$bx][$by]) - $island->{'missiles'}->[$bx][$by];
                        return 0 if($flag); # �Ĥ꤬����Х�������񤷤ʤ�
                    }
                    $count++;
                }
            }
        }

        return 1;

    } elsif (   ($kind == $HcomSendMonster)
             || ($kind == $HcomSendPirates)) {
        # �����ɸ�  ��±�ɸ�
        my($aId, %amityFlag);
        foreach $aId (@{$island->{'allyId'}}) {
            foreach (@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}) {
                next if($_ == $id);
                $amityFlag{$_} = $HcampAtk;
            }
        }
        # ��ȯ���֤ʤ饳�ޥ�ɤ�̵��
        if ($HarmisticeTurn && ($HislandTurn <= $HarmisticeTurn || $amityFlag{$target})) {
            # ���⤬���Ĥ���Ƥ��ʤ�
            logNotAvail($id, $name, $comName);
            return 0;
        }
        # �������åȼ���
        my ($tn) = $HidToNumber{$target};
        my ($tIsland) = $Hislands[$tn];
        my ($tName) = islandName($tIsland);

        unless(defined $tn) {
            # �������åȤ����Ǥˤʤ�
            logNoAny($id, $name, $comName, "��ɸ��${AfterName}�˿ͤ���������ʤ�");
            return 0;
        }

        if ($tIsland->{'predelete'}) {

            logNoAny($id, $name, $comName, '�¹Ԥ����Ĥ���ʤ�');
            return 0;
        }

        # ����ο͸������ʤ�������ɸ��ο͸������ʤ��ʤ顢�¹Ԥϵ��Ĥ���ʤ�
        if (   ($tIsland->{'id'} != $id)
            && (!$tIsland->{'BF_Flag'})
            && (   ($island->{'pop'} < $HguardPop)
                || ($tIsland->{'pop'} < $HguardPop) )  ) {
            logNoAny($id, $name, $comName, '�¹Ԥ����Ĥ���ʤ�');
            return 0;
        }

        $tIsland->{'monstersend'}++;

        my ($send) = $tIsland->{'monstersend'};
        my ($sendmo_kind , $sendmo_id);

        if ($kind == $HcomSendPirates) {

            $sendmo_kind = $tIsland->{'sendmo_kind'};
            $sendmo_kind->[$send] = $Mons_Pirates;
            logSecretMonsSend($id, $target, $name, $tName , '��±');
        }else{
            $sendmo_kind = $tIsland->{'sendmo_kind'};
            $sendmo_kind->[$send] = $Mons_MechaInora;
            logMonsSend($id, $target, $name, $tName , '��¤����');
        }
        $sendmo_id = $tIsland->{'sendmo_id'};
        if ($tIsland->{'id'} != $id) {
            $sendmo_id->[$send] = $id;
        } else{
            $sendmo_id->[$send] = 0;
        }

        # ��å�����

        $island->{'money'} -= $cost;
        return 1;

    } elsif($kind == $HcomAlly) {
        # Ʊ�� ������æ��
        # �������åȼ���
        return if(!$HallyUse || !$HallyJoinComUse || $HarmisticeTurn);
        my ($tn) = $HidToNumber{$target};
        my ($tan) = $HidToAllyNumber{$target};
        if (   ($tn eq '')
            || ($tan eq '') ) {
            # �������åȤ����Ǥˤʤ�
            logNoAny($id, $name, $comName, "��ɸ��${AfterName}�˿ͤ���������ʤ�");
            return 0;
        }
        my $tName = islandName($Hislands[$tn]);
        if (defined $HidToAllyNumber{$id}) {
            logLeaderAlready($id, $name, $tName, $comName);
            return;
        }

        my $ally = $Hally[$tan];
        if ($HallyJoinOne && ($island->{'allyId'}[0] ne '') && ($island->{'allyId'}[0] != $ally->{'id'})) {
            logOtherAlready($id, $name, $tName, $comName);
            return;
        }
        my $allyMember = $ally->{'memberId'};
        my @newAllyMember = ();
        my $flag = 0;

        foreach (@$allyMember) {
            if (!(defined $HidToNumber{$_})) {
            }
            elsif($_ == $id) {
                $flag = 1;
            }
            else {
                push(@newAllyMember, $_);
            }
        }

        if ($flag) {
            logAllyEnd($id, $target, islandName($island), $ally->{'name'});

            my @newAlly = ();
            foreach (@{$island->{'allyId'}}) {
                if($_ != $ally->{'id'}) {
                    push(@newAlly, $_);
                }
            }

            $island->{'allyId'} = \@newAlly;
            $ally->{'score'} -= $island->{'pts'};
            $ally->{'number'}--;

        } else {
            logAlly($id, $target, islandName($island), $ally->{'name'});
            push(@newAllyMember, $id);
            push(@{$island->{'allyId'}}, $ally->{'id'});
            $ally->{'score'} += $island->{'pts'};
            $ally->{'number'}++;
        }
        $island->{'money'} -= $HcomCost[$HcomAlly];
        $ally->{'memberId'} = \@newAllyMember;
        return 1;

    } elsif ($kind == $HcomSell) {
        # ����͢��
        # ͢���̷���
        $arg = 1 if(!$arg);
        my ($value) = min($arg * (-$cost), $island->{'food'});

        # ͢�Х�
        logSell($id, $name, $comName, $value);
        #$island->{'food'} -=  $value;
        food_product_Random_consumption($island , $value);
        $island->{'money'} += ($value / 10);
        return 0;

    } elsif (   ($kind == $HcomFood)
             || ($kind == $HcomMoney) ) {
        # �����
        my ($aId, %amityFlag);
        foreach $aId (@{$island->{'allyId'}}) {
            foreach (@{$Hally[$HidToAllyNumber{$aId}]->{'memberId'}}) {
                next if($_ == $id);
                $amityFlag{$_} = $HcampAtk;
            }
        }
        # �������åȼ���
        my ($tn) = $HidToNumber{$target};
        my ($tIsland) = $Hislands[$tn];
        my ($tName) = islandName($tIsland);

        # ¾�οرĤˤϱ���Ǥ��ʤ�
        if ($HarmisticeTurn && $HcampAidOnly && !$amityFlag{$target}) {
            logAidFail($id, $target, $name, $tName, $comName);
            return 0;
        }

        # ����ο͸������ʤ��ʤ顢�¹Ԥϵ��Ĥ���ʤ�
        if (($tIsland->{'id'} != $id) && ($island->{'pop'} < $HguardPop)) {
            logNoAny($id, $name, $comName, "�¹Ԥ����Ĥ���ʤ�");
            return 0;
        }

        # �¤������
        if ($tIsland->{'predelete'}) {
            logNoAny($id, $name, $comName, "�¹Ԥ����Ĥ���ʤ�");
            return 0;
        }

        # ����̷���
        $arg = 1 if(!$arg);
        my ($value, $str);
        if ($cost < 0) {
            $value = min($arg * (-$cost), $island->{'food'});
            $str = "${HtagFood_}$value$HunitFood${H_tagFood}";
        }
        else {
            $value = min($arg * ($cost), $island->{'money'});
            $str = "${HtagMoney_}$value$HunitMoney${H_tagMoney}";
        }

        # �����
        logAid($id, $target, $name, $tName, $comName, $str);

        if ($cost < 0) {
            food_export($island , $tIsland , $value);
        } else {
            $island->{'money'} -= $value;
            $tIsland->{'money'} += $value;
            $island->{'ext'}[1] += $value; # �׸���
            $tIsland->{'ext'}[1] -= $value; # �׸���
        }
        return 0;

    } elsif ($kind == $HcomGivefood) {
        # ����
        if($landKind == $HlandMonster) {
            my ($mKind, $mName, $mHp) = monsterSpec($landValue->[$x][$y]);
            $lv += random(5) if($mHp < 10);
            $landValue->[$x][$y] = $lv;
        } elsif( (($landKind == $HlandCollege) && ($lv == 4))  ||
                 (($landKind == $HlandCollege) && ($lv == 96)) ||
                 (($landKind == $HlandCollege) && ($lv == 97)) ||
                 (($landKind == $HlandCollege) && ($lv == 98))    ) {

            my ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
            if (random(100) < 30) {
                $msap++;
                logGiveFoodUpdate($id,"AP",$msap);
            } elsif (random(100) < 30) {
                $msdp++;
                logGiveFoodUpdate($id,"DP",$msdp);
            } elsif (random(100) < 30) {
                $mssp++;
                logGiveFoodUpdate($id,"SP",$mssp);
            } else {
                $mshp++;
                $mshp = 15 if($mshp > 15);
                logGiveFoodUpdate($id,"HP",$mshp);
            }
            $island->{'eisei5'} = "$mshp,$msap,$msdp,$mssp,$mswin,$msexe,$tet";

        } else {
            # ��Ŭ�����Ϸ�
            logLandFail($id, $name, $comName, $landName, $point);
            return 0;
        }
        logLandSuc($id, $name, $comName, $point);

        # ��򺹤�����
        $island->{'food'} += $cost;
        if ($arg > 1) {
            $arg--;
            slideBack($comArray, 0);
            $comArray->[0] = {
                'kind' => $kind,
                'target' => $target,
                'x' => $x,
                'y' => $y,
                'arg' => $arg
            };
        }
        return 1;

    } elsif ($kind == $HcomItemThrow) {
        # �����ƥ�ΤƤ�
        if ($arg > $HItem_MAX) {
            logItemisNoting($id, $name);
            return 0;
        }
        my ($item) = $island->{'item_land'};
        my ($item_lv) = $island->{'item_landValue'};
        my ($item_lv2) = $island->{'item_landValue2'};
        my ($item_lv3) = $island->{'item_landValue3'};

        if ($item->[$arg] == $HItem_Nothing){

            logItemisNoting($id, $name);
            return 0;

        }else{

            my ($itemname)= landName($item->[$arg], $item_lv->[$arg], $item_lv2->[$arg]);

            $item->[$arg] = $HItem_Nothing;
            $item_lv->[$arg] = $HItem_Nothing;
            $item_lv2->[$arg] = $HItem_Nothing;
            $item_lv3->[$arg] = $HItem_Nothing;

            logItemThrow($id, $name, $itemname);

            return 0;
        }
        return 0;   # ǰ�Τ���

    } elsif ($kind == $HcomItemUse) {
        # �����ƥप��
        if ($arg > $HItem_MAX) {
            logItemisNoting($id, $name);
            return 0;
        }

        my ($item) = $island->{'item_land'};
        my ($item_lv) = $island->{'item_landValue'};
        my ($item_lv2) = $island->{'item_landValue2'};
        my ($item_lv3) = $island->{'item_landValue3'};

        if ($item->[$arg] == $HItem_Nothing){
            logItemisNoting($id, $name);
            return 0;

        }
        else {
            my ($itemname) = landName($item->[$arg], $item_lv->[$arg], $item_lv2->[$arg]);

            if(   ($landKind == $HlandPlains)
               || ($landKind == $HlandSea)   ) {

                $land->[$x][$y] = $item->[$arg];
                $landValue->[$x][$y] = $item_lv->[$arg];
                $landValue2->[$x][$y] = $item_lv2->[$arg];
                $landValue3->[$x][$y] = $item_lv3->[$arg];

                $item->[$arg] = $HItem_Nothing;
                $item_lv->[$arg] = $HItem_Nothing;
                $item_lv2->[$arg] = $HItem_Nothing;
                $item_lv3->[$arg] = $HItem_Nothing;
                logItemPuton($id, $name, $point ,$itemname );

            }else{
                logItemDeny($id, $name, $point);
                return 0;
            }
        }
        return 0;

    } elsif ($kind == $HcomSave) {
        # ���ε���
        return 0 unless($island->{'shr'});
        if (-e "${HdirName}/${id}.${HsubData}") {
            copy("${HdirName}/${id}.${HsubData}", "${HdirName}/savedata.$id");
            $island->{'money'} -= $cost;
            logSaveLoad($id, $name, $comName, "��Ԥ��ޤ�����");
            my ($sx, $sy);
            foreach $sy (0..$islandSize) {
                foreach $sx (0..$islandSize) {
                    $landValue->[$sx][$sy] = $HislandTurn if($land->[$sx][$sy] == $HlandShrine);
                }
            }
        } else {
            logSaveLoad($id, $name, $comName, "�˼��Ԥ��ޤ�����");
            return 0;
        }
        return 1;

    } elsif($kind == $HcomLoad) {
        # ����˺��
        return 0 unless($island->{'shr'});
        if (-e "${HdirName}/savedata.$id") {
            # �Ϸ��ǡ������ɤ߹���
            if (!open(IIN, "${HdirName}/savedata.$id")) {
                logSaveLoad($id, $name, $comName, "�˼��Ԥ��ޤ�����");
                return 0;
            }
            my (@sland, @slandValue, $sline, $sx, $sy);
            foreach $sy (0..$islandSize) {
                $sline = <IIN>;
                foreach $sx (0..$islandSize) {
                    $sline =~ s/^(..)(......)(..)(....)(..)//;
                    $sland[$sx][$sy] = hex($1);
                    $slandValue[$sx][$sy] = hex($2);
                    $landValue2[$sx][$sy] = hex($3);
                    $landValue3[$sx][$sy] = hex($4);
                    $landValue->[$sx][$sy] = 0 if($land->[$sx][$sy] == $HlandShrine);
                }
            }
            close(IIN);
            $island->{'land'} = \@sland;
            $island->{'landValue'} = \@slandValue;
            unlink("${HdirName}/savedata.$id");
            logSaveLoad($id, $name, $comName, '��Ԥ��ޤ�����');
            $island->{'money'} -= $cost;
            return 1;
        }
        else {
            logSaveLoad($id, $name, $comName, '�˼��Ԥ��ޤ�����');
            return 0;
        }

    } elsif($kind == $HcomGiveup) {
        # ����
        $island->{'dead'} = 1;
        OutAlly($island);
        logGiveup($id, $name);
        unlink("${HdirName}/${id}.${HsubData}");
        unlink("${HdirName}/savedata.$id") if(-e "${HdirName}/savedata.$id");
        return 1;
    }

    return 1;
}


#------------------------------------------------------------------------------------
# ��
#------------------------------------------------------------------------------------
sub logDeleteAlly_forTurn {
    my ($name) = @_;
    logHistory("Ʊ����${HtagName_}${name}${H_tagName}�٤�${HtagDisaster_}�򻶡�${H_tagDisaster}");
}


#------------------------------------------------------------------------------------
# Ʊ������ȴ����
#------------------------------------------------------------------------------------
sub OutAlly {
    my ($island) = @_;

        my ($target) = $island->{'allyId'}[0];
        my ($id) = $island->{'id'};

        my ($tn) = $HidToNumber{$target};
        my ($tan) = $HidToAllyNumber{$target};

        my $tName = islandName($Hislands[$tn]);

        my $ally = $Hally[$tan];


        if (   $HallyJoinOne
            && ($island->{'allyId'}[0] ne '')
                                              ) {
            #Ʊ���˲������Ƥ���
        my $allyMember = $ally->{'memberId'};

            
            my @newAllyMember = ();
            my $flag = 0;

            foreach (@$allyMember) {
                if(!(defined $HidToNumber{$_})) {

                } elsif($_ == $id) {
                    $flag = 1;
                } else {
                    push(@newAllyMember, $_);
                }
            }

            if($flag) {
                logAllyEnd($id, $target, islandName($island), $ally->{'name'});

                my @newAlly = ();
                foreach (@{$island->{'allyId'}}) {
                    if($_ != $ally->{'id'}) {
                        push(@newAlly, $_);
                    }
                }

                $island->{'allyId'} = \@newAlly;
                $ally->{'score'} -= $island->{'pts'};
                $ally->{'number'}--;

                $ally->{'memberId'} = \@newAllyMember;
            }

        }
}


#------------------------------------------------------------------------------------
# �����ԲĤ������å�
#------------------------------------------------------------------------------------
sub NoAnyCheck {
    my($island,$tIsland) = @_;

    # �������¤���
    if ($tIsland->{'predelete'}) {
        return 1;
    }

    # ����ο͸������ʤ�������ɸ��ο͸������ʤ��ʤ顢�¹Ԥϵ��Ĥ���ʤ�
    if (   (!$tIsland->{'BF_Flag'})                 # ���ΥХȥ�ե�����ɤǤʤ�
        && ($tIsland->{'id'} != $island->{'id'})    # ��ʬ�Τ��ޤǤʤ�
        && (   ($island->{'pop'} < $HguardPop)      # ��ʬ����οͿ�������ʤ�
            || ($tIsland->{'pop'} < $HguardPop) )   # ������οͿ�������ʤ�
                                                  ) {
        return 1;
    }

    return 0;
}


#------------------------------------------------------------------------------------
# ��̱ȯ������Į
#------------------------------------------------------------------------------------
sub isExpTown {
    my($land) = @_;


}


#------------------------------------------------------------------------------------
# ��Ĺ�����ñ�إå����ҳ�
#------------------------------------------------------------------------------------
sub doEachHex {
    my ($island) = @_;

    my (@monsterMove);
    my (@funeMove);

    # Ƴ����
    my ($name) = islandName($island);
    my ($id) = $island->{'id'};
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};
    my ($reason);

    my ($TurndoEachHex);

    my ($zooflag) = 0;

    my ($msseigen, $kougekiseigen, $kougekiseigenm) = (0, 0, 0);

    # ������͸��Υ�����
    my ($addpop)  = 10;  # ¼��Į
    $addpop = 1 if($island->{'unemployed'} >= 100);     # ���ȼԤ�����������ȡ��ͤ������ʤ�
    $addpop = 20 if($island->{'BF_Flag'} == 1);         # bf

    $TurndoEachHex->{'reason_mode'} = $Reason_Normal;

    my($addpop2) = 0; # �Ի�
    if($island->{'food'} < 0) {
        # ������­
        $addpop = -30;
        $reason = '������­';
        $TurndoEachHex->{'reason_mode'} = $Reason_FoodShort;

    } elsif(random(20) < $island->{'rot'}) {
        # ˦�ҡ���
        $addpop = -10;
        $reason = '˦��';
        logRotsick($id, $name);
        $TurndoEachHex->{'reason_mode'} = $Reason_Rotten;

    } elsif(random(2) < $island->{'c21'}) {
        # ���¡���
        $addpop = -3;
        food_product_Random_consumption($island , int($island->{'food'} / 2));

        $reason = '����';
        logSatansick($id, $name);
        $TurndoEachHex->{'reason_mode'} = $Reason_Plague;

    } elsif(   $island->{'fim'}
            && !random(100) ) {
        # �����ѡ���
        $addpop = -20;
        logStarvefood($id, $name);
        $reason = '������';
        $TurndoEachHex->{'reason_mode'} = $Reason_SideEffect;

    } elsif($island->{'propaganda'}) {
        # Ͷ�׳�ư��
        $addpop += 10;
        $addpop += 2 if ($island->{'yaku'} >= 3);
        $addpop += 3 if ($island->{'yaku'} >= 5);

        $addpop2 = 3;
        $addpop2 = 5 if ($island->{'yaku'} >= 3);
        $addpop2 = 6 if ($island->{'yaku'} >= 5);
    }
    $TurndoEachHex->{'reason'} = $reason;
    $TurndoEachHex->{'addpop'} = $addpop;
    $TurndoEachHex->{'addpop2'} = $addpop2;

    # �롼��
    my ($x, $y, $i);
    my ($landKind);
    my ($lv, $lv2, $lv3);
    my ($lName);
    my ($monsterCount);

    my ($on_train) = 0;
    $on_train = random($island->{'train'});
    my ($train_sta) = 0;

    my ($this_pos);

    $island->{'happy'} = 100;
    $island->{'tax_income'} = -1;

    foreach $i (0..$pointNumber) {

        $x = $Hrpx[$i];
        $y = $Hrpy[$i];
        $landKind = $land->[$x][$y];
        $lv = $landValue->[$x][$y];
        $lv2 = $landValue2->[$x][$y];
        $lv3 = $landValue3->[$x][$y];
        $lName = landName($landKind, $lv,$lv2);

        $TurndoEachHex->{'y'} = $y;
        $TurndoEachHex->{'x'} = $x;

        $this_pos = "($x, $y)";

        if( 0 ){
            # ���򤤤��ȥ����С��إåɤ��ä���

        }elsif(   ($landKind == $HlandTown)         # Į ���٥��
               || ($landKind == $HlandMinato)       # �� ���٥��
               || ($landKind == $HlandSeacity)      # �����Ի� ���٥��
               || ($landKind == $HlandUmicity)      # ���٥��
               || ($landKind == $HlandNewtown)      # ���٥��
               || ($landKind == $HlandInaka)        # ���٥��
                                                ) {

            {
                $monsterCount = CityAttack($island, $x, $y);
                $lv = $landValue->[$x][$y];

                if ($monsterCount > 0) {
                    if (($lv <= 0) ) {

                        if (   ($landKind == $HlandSeacity)
                            || ($landKind == $HlandUmicity)
                                                            ){
                            # �����᤹
                            SetSeaLand_Normal($island, $x, $y);
                            next;

                        }else{
                            # ʿ�Ϥ��᤹
                            SetWasteLand_Normal($island, $x, $y);
                            next;
                        }
                    }
                }

                if ($addpop < 0) {
                    # ��­
                    $lv -= (random(-$addpop) + 1);
                    if($lv <= 0) {

                        if (   ($landKind == $HlandTown)
                            || ($landKind == $HlandNewtown)
                            || ($landKind == $HlandInaka)
                                                            ) {                        # ʿ�Ϥ��᤹
                            SetPlains_Normal($island , $x , $y);

                        } else {
                            if($landKind == $HlandMinato) {
                                SetWasteLand_Normal_val($island, $x, $y,4);   # ���Ϥ��᤹
                            }else{
                                SetSeaLand_Normal($island, $x, $y);     # �����᤹
                            }
                        }
                        my($tName) = landName($land->[$x][$y], $landValue->[$x][$y],$landValue2->[$x][$y]);
                        logPopDecrease($id, $name, $lName, $tName, $reason, $this_pos);
                        next;
                    }

                } else {
                    # ��Ĺ
                    my ($grstop);
                    $grstop = 100;      # �Իԡ����졢��
                    $grstop = $HUmicity_growstop if ($landKind == $HlandUmicity) ;
                    $grstop = $HNewtown_growstop if ($landKind == $HlandNewtown) ;
                    $grstop = $HInaka_growstop if ($landKind == $HlandInaka) ;

                    $lv = Town_Growup($lv , $addpop , $addpop2 , $grstop);
                }

                my ($poplimit);
                $poplimit = $HTown_limit;   # �Իԡ����졢��
                $poplimit = $HUmicity_limit if ($landKind == $HlandUmicity) ;
                $poplimit = $HNewtown_limit if ($landKind == $HlandNewtown) ;
                $poplimit = $HInaka_limit if ($landKind == $HlandInaka) ;

                $lv = $poplimit if($lv > $poplimit);
                $landValue->[$x][$y] = $lv;

                if (   ($landKind == $HlandTown)
                    || ($landKind == $HlandNewtown) ) {

                    my ($townCount) = countAround($land, $x, $y, 19, @Htowns);

                    $land->[$x][$y] = $HlandBigtown if(($landKind == $HlandTown) && ($townCount > 17) && !random(1000) && ($lv > 195));
                    $land->[$x][$y] = $HlandBigtown if(($landKind == $HlandNewtown) && ($townCount > 17) && (random(1000) < 3) && ($lv > 295));
                }

                if ($landKind == $HlandMinato) {        # �ߤʤ�

                    if (random(1000) < 10 ) {
                        logFishing($id, $name, $lName , $this_pos);
                    }
                }
            }

        }elsif($landKind == $HlandPlains) {     # ʿ�ϥ��٥��

            my ($bf_flag) = $island->{'BF_Flag'};

            if (   ($lv == 0) # ͽ���ϤǤʤ���
                && (   ($bf_flag)
                    || (   (!($bf_flag))
                        && ($island->{'unemployed'} <= 10)  # ���ȼԤ���롣
                        && (  $island->{'farm'} + $island->{'factory'}
                            + $island->{'factoryHT'} + $island->{'mountain'} > 5) ) )
                                                                              ) {

                my ($tflag) = ($id > 100) ? 1 : countGrow($land, $landValue, $x, $y, $bf_flag);

                if (!random(5) && $tflag) {
                    # ��������졢Į������С�������Į�ˤʤ�
                    $land->[$x][$y] = $HlandTown;
                    $landValue->[$x][$y] = 1;
                    $landValue2->[$x][$y] = 0;
                    $landValue->[$x][$y] = 1 + random(10) if ($bf_flag);
                    if (random(1000) < $island->{'nto'}*3) {
                        $land->[$x][$y] = $HlandNewtown;
                        $landValue->[$x][$y] = 1;
                        $landValue2->[$x][$y] = 0;
                    }

                    if (!($bf_flag)) {
                        logPlains2Town($island, landName($land->[$x][$y], $landValue->[$x][$y],$landValue2->[$x][$y]) ,$this_pos);
                    }
                }
            }

            if (   ($island->{'BF_Flag'} == 1)
                && ($island->{'defcnt'} < 6) ) {

                if (!random(5)) {
                    if (   (!countAround($land, $x, $y, 19, $HlandDefence ) )
                        && (!countAround($land, $x, $y, 19, $HlandMonster ) ) ){

                        $land->[$x][$y] = $HlandDefence;
                        $landValue->[$x][$y] = 0;
                        $island->{'defcnt'}++;
                    }
                }
            }

        } elsif ($landKind == $HlandWaste) {         # ���ϥ��٥��

            WastelandEvent($island,$x,$y);

        } elsif ($landKind == $HlandProcity) {       # ���٥��
            # �ɺ��Ի�
            if ($addpop < 0) {
                # ��­
                $lv -= (random(-$addpop) + 1);
                if ($lv <= 0) {
                    # ʿ�Ϥ��᤹
                    SetPlains_Normal($island , $x , $y);
                    logPopDecrease($id, $name, $lName, "ʿ��", $reason, $this_pos);
                    next;
                }
            }
            else {
                # ��Ĺ
                $lv = Town_Growup( $lv , $addpop , $addpop2 , $HProcity_growstop );
            }

            $lv = min($lv , $HProcity_limit);

            $landValue->[$x][$y] = $lv;

            if ($lv == $HProcity_limit) {

                if ( ($island->{'monsterlive'}) ) {
                    ProCity_MonsterSmash($island,$x,$y);
                }
            }

        } elsif ($landKind == $HlandFiredept) {      # ���ɽ� ���٥��
            FiredeptlandEvent($island,$x,$y);

        } elsif ($landKind == $HlandKatorikun) {     # ��路���٥��

            if ( ($island->{'monsterlive'}) ) {
                ProCity_MonsterSmash($island,$x,$y);
            }

        } elsif ($landKind == $HlandBigtown) {            # �����ԻԷ� ���٥��

            $monsterCount = CityAttack($island, $x, $y);
            $lv = $landValue->[$x][$y];

            if ($monsterCount > 0) {
                if ($lv <= 0) {
                    # ʿ�Ϥ��᤹
                    SetWasteLand_Normal_val($island , $x , $y,4);
                    logPopDecrease($id, $name, $lName, "����", "���äι���", $this_pos);
                    next;
                }
            }

            my ($townCount)  = countAround($land, $x, $y, 19, @Htowns);
            my ($houseCount) = countAround($land, $x, $y, 7, $HlandHouse);
            if (   ($island->{'shu'} == 0) && ($houseCount == 1)
                && ($townCount > 16) && (random(1000) < 300) ) {

                $land->[$x][$y] = $HlandShuto;
                my ($onm);
                $onm = $island->{'onm'};
                $island->{'shutomessage'} = "$onm���ƥ���";
                logShuto($id, $name, $lName, "$onm���ƥ���", $this_pos);
                $island->{'shu'}++;
            }
            if ($addpop < 0) {
                # ��­
                $lv -= (random(-$addpop) + 1);
                if($lv <= 0) {
                    # ʿ�Ϥ��᤹
                    SetPlains_Normal($island,$x , $y);
                    logPopDecrease($id, $name, $lName, "ʿ��", $reason, $this_pos);
                    next;
                }

            }
            else {
                # ��Ĺ
                $lv = Town_Growup( $lv , $addpop , $addpop2 , 200 );
            }
            $lv = $HBigtown_limit if($lv > $HBigtown_limit);
            $landValue->[$x][$y] = $lv;

        } elsif ($landKind == $HlandSeatown) {               # ���쿷�ԻԷ�

            my ($townCount)  = countAround($land, $x, $y, 19, @Htowns);
            my ($houseCount) = countAround($land, $x, $y, 7, $HlandHouse);

            if (   ($island->{'shu'} == 0)
                && ($houseCount == 1)
                && ($townCount > 16)
                && (random(1000) < 300)) {

                $land->[$x][$y] = $HlandUmishuto;
                my($onm);
                $onm = $island->{'onm'};
                $island->{'shutomessage'} = "$onm���ƥ���";
                logShuto($id, $name, $lName, $island->{'shutomessage'}, $this_pos);
                $island->{'shu'}++;
            }

            if ($addpop < 0) {
                # ��­
                $lv -= (random(-$addpop) + 1);
                if ($lv <= 0) {
                    # ʿ�Ϥ��᤹
                    SetSeaLand_Normal($island, $x, $y);     # �����᤹
                    logPopDecrease($id, $name, $lName, '��', $reason, $this_pos);
                    next;
                }

            } else {
                # ��Ĺ
                $lv = Town_Growup( $lv , $addpop , $addpop2 , 250 );
            }
            $lv = min($lv,$HSeatown_limit);
            $landValue->[$x][$y] = $lv;

        } elsif ($landKind == $HlandBettown) {   # �������Ի� ���٥��

            $monsterCount = CityAttack($island, $x, $y);
            $lv = $landValue->[$x][$y];
            if ($monsterCount > 0) {
                if ($lv <= 0) {
                    # ʿ�Ϥ��᤹
                    SetWasteLand_Normal_val($island , $x , $y , 4);
                    logPopDecrease($id, $name, $lName, "����", "���äι���", $this_pos);
                    next;
                }
            }

            if ($addpop < 0) {
                # ��­
                $lv -= (random(-$addpop) + 1);
                if ($lv <= 0) {
                    # ʿ�Ϥ��᤹
                    SetPlains_Normal($island , $x , $y);
                    logPopDecrease($id, $name, $lName, "ʿ��", $reason, $this_pos);
                    next;
                }
            } else {
                # ��Ĺ
                my($shutoCount) = countAround($land, $x, $y, 7, $HlandShuto, $HlandUmishuto);
                my($betCount) = countAround($land, $x, $y, 7, $HlandBettown);

                if(($island->{'shu'} > 0) &&
                    (($shutoCount > 0) || ($betCount > 1))) {
                    # ��Ĺ
                    $lv = Town_Growup( $lv , $addpop , $addpop2 , 1000 );
                }
            }
            $landValue->[$x][$y] = min($lv , $HBettown_limit);

        } elsif(   ($landKind == $HlandShuto)            # ���Է�
                || ($landKind == $HlandUmishuto) ) {     # ���Է�

            $monsterCount = CityAttack($island, $x, $y);
            $lv = $landValue->[$x][$y];
            if ($monsterCount > 0) {
                if ($lv <= 0) {
                    if($landKind == $HlandUmishuto) {
                        # �����᤹
                        $land->[$x][$y] = $HlandSea;
                    } elsif($landKind == $HlandShuto) {
                        # ʿ�Ϥ��᤹
                        SetPlains_Normal($island , $x , $y);
                    }
                    $landValue->[$x][$y] = 0;       #���� reset
                    my ($tName) = landName($land->[$x][$y], $landValue->[$x][$y],$landValue2->[$x][$y]);
                    logPopDecrease($id, $name, $lName, $tName, "���äι���", $this_pos);
                    next;
                }
            }

            if ($addpop < 0) {
                # ��­
                $lv -= (random(-$addpop) + 1);
                if ($lv <= 0) {
                    if ($landKind == $HlandUmishuto) {
                        # �����᤹
                        $land->[$x][$y] = $HlandSea;
                    } elsif($landKind == $HlandShuto) {
                        # ʿ�Ϥ��᤹
                        SetPlains_Normal($island , $x , $y);
                    }
                    $landValue->[$x][$y] = 0;
                    my ($tName) = landName($land->[$x][$y], $landValue->[$x][$y],$landValue2->[$x][$y]);
                    logPopDecrease($id, $name, $lName, $tName, $reason, $this_pos);
                    next;
                }

            } else {
                # ��Ĺ
                $lv = Town_Growup( $lv , $addpop , $addpop2 , $HShuto_growstop );
            }
            $landValue->[$x][$y] = min($lv , $HShuto_limit);

        } elsif(   ($landKind == $HlandRizort)          # �꥾���ȷ� ���٥��
                || ($landKind == $HlandBigRizort) ) {   # �꥾���ȷ� ���٥��

            if(   (   ($landKind == $HlandRizort)
                   && ($lv < 400)
                   && (random(100) < 25) )
               || (   ($landKind == $HlandBigRizort)
                   && ($lv < 1000)
                   && (random(100) < 30) ) ) {

                my (@order) = randomArray($HislandNumber);
                my ($migrate);

                # �Ѹ����õ��
                my ($tIsland);
                my ($n) = min($HislandNumber, 5);
                my ($i);

                my ($seaCount) = countAround($land, $x, $y, 19, $HlandSea,$HlandStation);
                my ($forestCount) = countAround($land, $x, $y, 19, $HlandForest, $HlandMountain,$HlandOnsen);
                my ($parkCount) = countAround($land, $x, $y, 19, $HlandPark, $HlandKyujo, $HlandKyujokai);
                my ($umiamuCount) = countAround($land, $x, $y, 19, $HlandUmiamu,$HlandInoraLand);
                my ($sunahamaCount) = countAround($land, $x, $y, 19, $HlandSunahama,$HlandBeachPark);
                my ($rizortCount) = (countAround($land, $x, $y, 19, $HlandRizort, $HlandBigRizort));
                $migrate =   $seaCount * 2
                           + $forestCount * 3
                           + $parkCount * 4
                           + $umiamuCount * 7
                           + $sunahamaCount * 6
                           + $rizortCount * 5;

                for ($i = 0; $i < $n; $i++) { # ����ޤ�Ĵ�٤�
                    $tIsland = $Hislands[$order[$i]];

                    next if ($tIsland->{'BF_Flag'});        # �Хȥ�ե�����ɤ����
                    next if ($tIsland->{'predelete'});      # ��������Ͻ���

                    # �͸���¿����˴Ѹ�����
                    if ($island->{'pop'} < $tIsland->{'pop'}) {
                        $lv += $migrate;
                        logKankouMigrate($id, $tIsland->{'id'}, $name, $lName, islandName($tIsland), $this_pos, $migrate);
                    }
                    last if ($employed <= 0);
                }

                $island->{'eisei2'} += $migrate;
                $island->{'pop'} += $migrate;
                $tIsland->{'pop'} -= $migrate;

                # �Ѹ��ˤ��Ƥ��줿ʬ�͸�����
                my ($tLand) = $tIsland->{'land'};
                my ($tLandValue) = $tIsland->{'landValue'};
                my ($employed) = $migrate;
                my ($x, $y, $landKind, $lv);
                foreach $i (0..$pointNumber) {
                    $x = $Hrpx[$i];
                    $y = $Hrpy[$i];
                    $landKind = $tLand->[$x][$y];
                    $lv = $tLandValue->[$x][$y];

                    if(($lv > 1) && (($landKind == $HlandTown) ||
                        ($landKind == $HlandProcity) ||
                        ($landKind == $HlandMinato) ||
                        ($landKind == $HlandFrocity) ||
                        ($landKind == $HlandNewtown) ||
                        ($landKind == $HlandBigtown) ||
                        ($landKind == $HlandBettown) ||
                        ($landKind == $HlandUmicity) ||
                        ($landKind == $HlandOilCity) ||
                        ($landKind == $HlandOnsen) ||
                        ($landKind == $HlandRizort) ||
                        ($landKind == $HlandBigRizort) ||
                        ($landKind == $HlandShuto) ||
                        ($landKind == $HlandUmishuto) ||
                        ($landKind == $HlandSeatown) ||
                        ($landKind == $HlandSeacity) ||
                        ($landKind == $HlandInaka)
                            )) {
                        # Į
                        $n = min($lv - 1, $employed);
                        $tLandValue->[$x][$y] -= $n;
                        $employed -= $n;
                    }
                }
            }

            if($addpop < 0) {
                # ��­
                $lv -= (random(-$addpop) + 1);
                if($lv <= 0) {
                    # ʿ�Ϥ��᤹
                    SetPlains_Normal($island , $x , $y);
                    next;
                }
            } else {
                # ��Ĺ
                $lv = Town_Growup( $lv , $addpop , $addpop2 , 10 );
            }

            if ($landKind == $HlandRizort) {

                $lv = min($lv , 400);
                my $value = $lv+$island->{'eis1'}+$island->{'eis2'}+$island->{'eis3'}+$island->{'eis5'}+int($island->{'fore'}/10)+int($island->{'rena'}/10)-$island->{'monsterlive'}*100;
                $island->{'money'} += $value if ($value > 0);

            } else {

                $lv = min($lv , 1000);
                $landValue->[$x][$y] = $lv;

                $monsterCount = CityAttack($island, $x, $y);
                $lv = $landValue->[$x][$y];
                if ($monsterCount > 0) {
                    if ($lv <= 0) {
                        # ʿ�Ϥ��᤹
                        SetWasteLand_Normal_val($island,$x,$y,4);
                        logPopDecrease($id, $name, $lName, "����", "���äι���", $this_pos);
                        next;
                    }
                }
            }
            $landValue->[$x][$y] = $lv;

        }
        elsif($landKind == $HlandHTFactory) {     # �ϥ��ƥ���ȥ��٥��

            if (random(1000) < 5 ){
                logSpiderMan($id, $name, $lName ,$this_pos);
            }

            if ( $island->{'business'} > 0 ) {

                if ($island->{'pika'} > 0) {

                    my $wk = $HlandHTFactory_add;
                    if ($island->{'shtf'} > 0) {
                        if (random(100) < 70 ){
                            $wk = 0;
                        }
                    }
                    $landValue->[$x][$y] += $wk;
                    $landValue->[$x][$y] = $HlandHTFactory_limit if($landValue->[$x][$y] > $HlandHTFactory_limit);
                }
            }

        } elsif ($landKind == $HlandSHTF) {          # �ϥ��ƥ���� ���٥��

            if (random(1000) < 5 ){
                logSpiderMan($id, $name, $lName , $this_pos);
            }
            if ( $island->{'business'} > 0 ) {
                if ($island->{'pika'} > 0) {
                    $landValue->[$x][$y] += $HlandSHTF_add;
                    if ($landValue->[$x][$y] > $HlandSHTF_limit) {
                        $landValue->[$x][$y] = $HlandSHTF_limit;
                    }
                }
            }

        } elsif($landKind == $HlandOnsen) {         # �������٥��

            if($addpop < 0) {
                # ��­
                $lv -= (random(-$addpop) + 1);
                if($lv <= 0) {
                    # �����᤹
                    SetMountain_Normal($island,$x,$y);
                    next;
                }
            } else {
                # ��Ĺ
                $lv = Town_Growup( $lv , $addpop , $addpop2 , 50 );
            }

            $lv = min( $lv , $HOnsen_limit);

            $landValue->[$x][$y] = $lv;

            if ($landKind == $HlandOnsen) {
                my ($nt) = countAround($land, $x, $y, 19, @Htowns);
                my ($value) = random($nt * 20 + $lv * 5 + int($island->{'pop'} / 20)) + random(100) + 100;
                if ($value > 0) {
                    $island->{'money'} += $value;

                    # ������
                    my ($str) = "$value$HunitMoney";
                    logOilMoney($id, $name, $lName, $this_pos, $str, "����");
                }

                # �����ϳ�Ƚ��
                if(!$HnoDisFlag && random(1000) < $HonsenRatio) {
                    # �ϳ�
                    logDamageAny($id, $name, $lName, $this_pos, "�ϳ餷���褦�Ǥ���");
                    $land->[$x][$y] = $HlandMountain;
                    $landValue->[$x][$y] = 0;
                }
            }

        } elsif( ($landKind == $HlandSea) ) {

            if ( ($lv == 1) ) {
                # ����

                my ($par) = $To_Sunahama_par;
                if (   ($island->{'weather'} == 0)
                    && ($island->{'temperature'} > 15) ) {
                    $par += 5;
                }

                if ($island->{'weather'} == 2) {
                    $par -= 5;
                }

                if (random(100) < $par) {
                    $land->[$x][$y] = $HlandSunahama;
                    $landValue->[$x][$y] = 0;
                }

                $par = $To_Ice_par;

                if ($island->{'temperature'} < 7) {
                    $par += 8;
                }

                if(random(100) < $par) {
                    $land->[$x][$y] = $HlandIce;
                    $landValue->[$x][$y] = 0;
                }
            }

        } elsif($landKind == $HlandBeachPark) {

            if ($island->{'temperature'} >= 22) {
                if ($island->{'weather'} != $HWeather_Rain) {
                    my($lv) = $landValue->[$x][$y];
                    if($lv > 0) {
                        my $value = $lv * 12 + random(200);
                        $island->{'money'} += $value;
                        # ������
                        logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", "����");
                    }
                }
            }

            SunahamaToSea($island,$x,$y);

        } elsif($landKind == $HlandSunahama) {
            # ����
            if ( !$landValue->[$x][$y] ){

                SunahamaToSea($island,$x,$y);
            }

        } elsif($landKind == $HlandIce) {
            # ɹ��
            my($lv) = $landValue->[$x][$y];
            if($lv > 0) {
                if ($island->{'weather'} != $HWeather_Rain) {
                    my $value = $lv * 25 + random(501);
                    $island->{'money'} += $value;
                    # ������
                    logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", "����");
                }
            }

            if(random(100) < $Ice_To_Sea_par) {
                logSkateDown($island, $lName, $x, $y) if($lv > 0);        #�������Ⱦ�Τ�
                $land->[$x][$y] = $HlandSea;
                $landValue->[$x][$y] = 1;
                $landValue2->[$x][$y] = 0;
            }

        } elsif($landKind == $HlandForest) {
            # ��
            ForestEvent($island,$x,$y);

            my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
            $island->{'happy'} += $happy;

        } elsif(   ($landKind == $HlandFarmchi)
                || ($landKind == $HlandFarmpic)
                || ($landKind == $HlandFarmcow) ){
            # �ܷܾ졢���ھ졢�Ҿ�
            my($FarmCount) = countAround($land, $x, $y, 7, $HlandFarm,$HlandInaka);
            my(@rflag);

            if($landKind == $HlandFarmchi) {
                @rflag = (1, 8 + $FarmCount * 2, 5);
            } elsif($landKind == $HlandFarmpic){
                @rflag = (2, 4 + $FarmCount * 2, 3);
            } else {
                @rflag = (3, 4 + $FarmCount, 1);
            }

            my ($value) = $lv * $rflag[0];
            if ($landKind == $HlandFarmchi) {
                my ($egg , $niku) ;
                $egg = int($value / 4);
                $niku = $value - $egg;
                if ($egg) {
                    food_product_plus($island , 'tamago' , $egg);
                }
                food_product_plus($island , 'toriniku' , $niku);

            } elsif($landKind == $HlandFarmpic){
                food_product_plus($island , 'butaniku' , $value);

            } else {
                food_product_plus($island , 'gyuniku' , $value);
            }

            $lv += random($rflag[1]) + $rflag[2];
            $landValue->[$x][$y] = min($lv , $HLivestock_limit);

        } elsif($landKind == $HlandDefence) { # �ɱһ��ߥ��٥��
            my ($deflv);
            $deflv = $lv & $HDefenceLevelMask;

            if ( $deflv == 0 ) {

            }elsif ($deflv == 2) {
                $island->{'money'} -= $HDefenceTurnCost;
                $island->{'money'} = 0 if ( $island->{'money'} < 0 );
            }


        } elsif($landKind == $HlandOilCity) {       # �����Ի� ���٥��

            $monsterCount = CityAttack($island, $x, $y);
            $lv = $landValue->[$x][$y];

            if ($monsterCount > 0) {
                if($lv <= 0) {
                    # �������
                    SetSeaLand_Normal($island, $x, $y);     # �����᤹
                    next;
                }
            }else{
                if($addpop < 0) {
                    # ��­
                    $lv -= (random(-$addpop) + 1);
                    if($lv <= 0) {
                        # ʿ�Ϥ��᤹
                        SetSeaLand_Normal($island, $x, $y);     # �����᤹
                        next;
                    }
                } else {
                    # ��Ĺ
                    $lv = Town_Growup( $lv , $addpop , $addpop2 , 2000 );
                }
                if($lv > 3000) {
                    $lv = 3000;
                }
                $landValue->[$x][$y] = $lv;

                if (!random(5)){
                    my ($value) = 1 + random(1200);
                    $island->{'oilincome'} += $value if($HlogOmit1);
                    # ������
                    logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", "����") if(!$HlogOmit1);
                }
            }

        } elsif($landKind == $HlandOil) {       # �������ġ����٥��
            my($value, $str);
            $value = $HoilMoney + random(1001);
            $island->{'money'} += $value;

            $island->{'oilincome'} += $value if($HlogOmit1);
            # ������
            logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", "����") if(!$HlogOmit1);

            # �ϳ�Ƚ��
            if(!$HnoDisFlag && random(1000) < ( $HoilRatio + ($island->{'oil'}*2) ) ) {
                # �ϳ�
                logDamageAny($id, $name, $lName, $this_pos, "�ϳ餷���褦�Ǥ���");
                SetSeaLand_Normal($island, $x, $y);     # �����᤹
            }

        } elsif($landKind == $HlandSeki) {
            # �ؽ�
            if(random(1000) < 7) {
                my $value = $HoilMoney + random(1001);
                $island->{'money'} += $value;

                # ������
                logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", '���Ǽ���');
            }

        } elsif(   ($landKind == $HlandPark)
                || ($landKind == $HlandInoraLand)
                || ($landKind == $HlandKyujo)
                || ($landKind == $HlandUmiamu) ) {
            # ͷ���ϡ����졢�����ߤ塢���Τ����

            my ($value, $event, $closed) = (0, 0, 0);
            my ($inoraevent) = 0;

            if($landKind == $HlandPark) {
                # ͷ����
                $closed = 2;

                if ( $island->{'business'} > 0 ) {
                    $event = 3;
                    unless(($island->{'par'} + $island->{'inoraland'}) > 5) {
                        my ($Guest) = 45 + random(10);
                        $Guest -= (random(10)) if ($island->{'weather'} == $HWeather_Rain);
                        $Guest = (70 + random(10)) if ($island->{'weather'} == $HWeather_Sunny);

                        my($nv) = (countAround($land, $x, $y, 7, $HlandPark, $HlandKyujo, $HlandUmiamu,$HlandInoraLand));
                        my($nx) = 3 * ($nv + 10) / 10;
                        $value = int(int($island->{'pop'} / $Guest) * $nx * $Hmoney2Incom[0]/100);
                    }
                }

            } elsif($landKind == $HlandInoraLand) {                # ���Τ����

                $closed = 0;
                if ( $island->{'business'} > 0 ) {
                    if ( $HislandTurn && !$InoraParkEvent) {
                        $event = 60; 
                        if(random(100) < $event) {
                            unless(($island->{'par'}) > 5) {

                                my ($Guest) = 20 + random(10);
                                $Guest -= (random(10)) if ($island->{'weather'} == $HWeather_Rain);
                                $Guest = (30 + random(10)) if ($island->{'weather'} == $HWeather_Sunny);

                                my ($nt) = (countAround($land, $x, $y, 19, @Htowns) - 3);
                                my ($np) = ( 1 + 3 * countAround($land, $x, $y, 19, $HlandPark));
                                my ($na) = ( 1 + 4 * countAround($land, $x, $y, 19, $HlandKyujo) );
                                my ($nqk) = (1 + 4 * countAround($land, $x, $y, 19, $HlandKyujokai) );
                                my ($nu) = ( 5 + random(5));
                                $value = int(($nt * $np * $na * $nqk * $nu + int($island->{'pop'} / $Guest)+ random(200)) * $Hmoney2Incom[$Hmonth]/100);
                                $inoraevent = 1;
                                $InoraParkEvent = 1;
                            }
                        }
                    }
                }

            } elsif($landKind == $HlandKyujo) {
                # ����
                $closed = 1;

                my ($Guest) = 20 + random(10);
                $Guest -= (random(10)) if ($island->{'weather'} == $HWeather_Rain);
                $Guest = (30 + random(10)) if ($island->{'weather'} == $HWeather_Sunny);

                unless(($island->{'kyu'} > 1) || ($island->{'amu'} > 1)) {
                    my($nt) = (countAround($land, $x, $y, 19, @Htowns) - 6);
                    my($np) = ( 1 + 2 * countAround($land, $x, $y, 19, $HlandPark));
                    my($na) = ( 1 + 3 * countAround($land, $x, $y, 19, $HlandUmiamu, $HlandInoraLand));
                    my($nu) = ( 10 + random(10));
                    $value = int(($nt * $np * $na * $nu + int($island->{'pop'} / $Guest)) * $Hmoney2Incom[0]/100);
                }

                if(random(100) < 3) {

                    my($value, $str);
                    $value = 500+ random(500);
                    $island->{'money'} += $value;
                    $str = "$value$HunitMoney";
                    # ������
                    logYusho($id, $name, $lName, $this_pos, $str);
                }

            } elsif($landKind == $HlandUmiamu) {    # �����ߤ�

                $closed = 0;
                $closed = 2 if( ($island->{'amu'} >= 4) );
                if ( $island->{'business'} > 0 ) {
                    unless(($island->{'kyu'} > 1) || ($island->{'amu'} > 1)) {

                        my ($Guest) = 20 + random(10);
                        $Guest -= (random(10)) if ($island->{'weather'} == $HWeather_Rain);
                        $Guest = (30 + random(10)) if ($island->{'weather'} == $HWeather_Sunny);

                        my($nt) = (countAround($land, $x, $y, 19, @Htowns) - 3);
                        my($np) = ( 1 + 3 * countAround($land, $x, $y, 19, $HlandPark));
                        my($na) = ( 1 + 4 * countAround($land, $x, $y, 19, $HlandKyujo , $HlandInoraLand) );
                        my($nqk) = (1 + 4 * countAround($land, $x, $y, 19, $HlandKyujokai) );
                        my($nu) = ( 5 + random(5));
                        $value = int(($nt * $np * $na * $nqk * $nu + int($island->{'pop'} / $Guest)+ random(200)) * $Hmoney2Incom[$Hmonth]/100);
                    }
                }
            }

            if($value > 0) {
                $island->{'money'} += $value;
                # ������
                if($HlogOmit1 && $event && (!$inoraevent) ) {
                    $island->{'parkincome'} += $value;
                } else {
                    logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", "����");
                }
            }

            # ���٥��Ƚ��
            if (   ( $island->{'business'} > 0 )
                && (   ( (random(100) < $event) && ( $landKind != $HlandInoraLand) )   # �西���� 10% �γ�Ψ�ǥ��٥�Ȥ�ȯ������
                    || ($inoraevent) ) ) {       # ���Τ���ɤΥ��٥��

                if ($landKind == $HlandInoraLand) {

                    $value = int($island->{'pop'} / 40 * 10 * $Hmoney2Incom[0]/100); # �͸�4��ͤ��Ȥ�1000�ȥ�ο�������
                    food_product_consumption($island , $value);
                    logParkEvent($id, $name, $lName, $this_pos, "$value$HunitFood") if($value);

                } else {

                    $value = int($island->{'pop'} / 50 * 10 * $Hmoney2Incom[0]/100); # �͸�5��ͤ��Ȥ�1000�ȥ�ο�������
                    food_product_consumption($island , $value);
                    logParkEvent($id, $name, $lName, $this_pos, "$value$HunitFood") if($value);
                }
            }

            # Ϸ�ಽȽ��
            if (random(100) < $closed) {
                # ���ߤ�Ϸ�ಽ���������ı�
                logDamageAny($id, $name, $lName, $this_pos, "���ߤ�Ϸ�ಽ���������������ޤ�����");
                SetPlains_Normal($island , $x , $y);
                $land->[$x][$y] = $HlandSea if ($landKind == $HlandUmiamu);
                $landValue->[$x][$y] = 0;
                $landValue2->[$x][$y] = 0;
            }

        } elsif($landKind == $HlandStation) {

            if ($island->{'train'} < 5) {

                my ($i,$bx,$by);
                my ($fx,$fy);
                my ($check) = 0;

                foreach $i (0..$pointNumber) {

                    $fx = $Hrpx[$i];
                    $fy = $Hrpy[$i];

                    if (   (0)
                        || ($land->[$fx][$fy] == $HlandTown)
                        || ($land->[$fx][$fy] == $HlandNewtown)
                        || ($land->[$fx][$fy] == $HlandBigtown)
                        || ($land->[$fx][$fy] == $HlandMinato)
                                                                ) {
                        if ($landValue->[$fx][$fy] > 4) {
                            $check = 1;
                            last;
                        }
                    }

                    if (   (0)
                        || ($land->[$fx][$fy] == $HlandFactory)
                        || ($land->[$fx][$fy] == $HlandPark)
                        || ($land->[$fx][$fy] == $HlandUmiamu)
                                                                ) {
                        if ($landValue->[$fx][$fy] > 4) {
                            $check = 2;
                            last;
                        }
                    }

                }

                next if (!$check);

                for ($i = 0; $i < 19; $i++) {
                    $bx = $x + $ax[$i];
                    $by = $y + $ay[$i];

                    # �Ԥˤ�����Ĵ��
                    $bx-- if(!($by % 2) && ($y % 2));

                    # �ϰ���ξ��
                    if (($bx >= 0) && ($bx < $HislandSize) && ($by >= 0) && ($by < $HislandSize)) {
                        if (random(100) < 30) {

                            if (   (   ($check == 1)
                                    && (   (   ($land->[$bx][$by] == $HlandTown)
                                            && ($landValue->[$bx][$by] < $HTown_limit) )
                                        || (   ($land->[$bx][$by] == $HlandNewtown)
                                            && ($landValue->[$bx][$by] < $HNewtown_limit) )
                                        || (   ($land->[$bx][$by] == $HlandProcity)
                                            && ($landValue->[$bx][$by] < $HProcity_limit) )
                                        || (   ($land->[$bx][$by] == $HlandBettown)
                                            && ($landValue->[$bx][$by] < $HBettown_limit) )
                                        || (   ($land->[$bx][$by] == $HlandShuto)
                                            && ($landValue->[$bx][$by] < $HShuto_limit) )
                                                                                          ) )
                                || (   ($check == 2)
                                    && (   (   ($land->[$bx][$by] == $HlandFactory)
                                            && ($landValue->[$bx][$by] < $HFactory_limit) )
                                        || (   ($land->[$bx][$by] == $HlandPark)
                                            && ($landValue->[$bx][$by] < $HPark_limit) )
                                        || (   ($land->[$bx][$by] == $HlandUmiamu)
                                            && ($landValue->[$bx][$by] < $HUmiamu_limit) )
                                                                                          ) )
                                                                                              ) {
                                my ($ra);
                                $ra = random(2) + 1;
                                $landValue->[$bx][$by] += $ra;
                                $landValue->[$fx][$fy] -= $ra;
                                $check = 5;

                                my ($value);
                                $value = $island->{'train'};
                                if ($value) {
                                    $island->{'money'} += $value;
                                    logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", '����');
                                }
                                last;
                            }
                        }
                    }
                }
            }

        } elsif($landKind == $HlandMountain) {          # �������٥��

            if ($lv > 0) {
                my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
                $island->{'happy'} -= $happy;
            }

        } elsif($landKind == $HlandKyujokai) {

            {
                $island->{'happy'} += 10;
                my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
                $island->{'happy'} -= $happy;
            }

            # �����
            # ���٥��Ƚ��
            if (random(100) < 10) { # �西���� 30% �γ�Ψ�ǥ��٥�Ȥ�ȯ������
                my ($Guest) = 45 + random(10);
                $Guest -= (random(10)) if ($island->{'weather'} == $HWeather_Sunny);
                $Guest = (70 + random(10)) if ($island->{'weather'} == $HWeather_Rain);
                # ����Υ��٥��
                my ($value) = int($island->{'pop'} / $Guest) * 10; # �͸�����ͤ��Ȥ�1000�ȥ�ο�������
                food_product_consumption($island , $value);
                logParkEvent($id, $name, $lName, $this_pos, "$value$HunitFood") if ($value > 0);
            }

            my ($escape) = 0;
            my ($i, $sx, $sy);
            my ($tkind);

            for ($i = 1; $i < 7; $i++) {
                $sx = $x + $ax[$i];
                $sy = $y + $ay[$i];

                # �Ԥˤ�����Ĵ��
                $sx-- if(!($sy % 2) && ($y % 2));
                # �ϰϳ�
                next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

                if (random(100) < 12) {
                    $tkind = $land->[$sx][$sy];
                    if (   ($tkind == $HlandTown)
                        || ($tkind == $HlandMinato)
                        || ($tkind == $HlandNewtown)
                        || ($tkind == $HlandBigtown)
                        || ($tkind == $HlandFrocity)
                        || ($tkind == $HlandShuto)
                        || ($tkind == $HlandBettown)
                        || ($tkind == $HlandRizort)
                        || ($tkind == $HlandBigRizort)
                        || ($tkind == $HlandOilCity)
                        || ($tkind == $HlandUmicity)
                                                        ) {
                        $escape++;
                        $landValue->[$sx][$sy]--;
                        if ($landValue->[$sx][$sy] <= 0 ) {
                            SetPlains_Normal($island , $sx , $sy);

                            if (   ($tkind == $HlandFrocity)
                                || ($tkind == $HlandOilCity)
                                || ($tkind == $HlandUmicity) ) {
                                $land->[$sx][$sy] = $HlandSea;
                            }
                        }
                    }
                }

            }
            logSouon($id, $name, $this_pos, $lName ,$escape) if ($escape);

            next if($HflagKai);     # �����Ѥ�
            $HflagKai = 1;

            # �����λ���
            unless(($island->{'kyu'} > 1) || ($island->{'amu'} > 1)) {

                my ($Guest) = 20 + random(10);
                $Guest -= (random(10)) if ($island->{'weather'} == $HWeather_Sunny);
                $Guest = (30 + random(10)) if ($island->{'weather'} == $HWeather_Rain);

                my($nt) = (countAround($land, $x, $y, 19, @Htowns) - 6);
                my($ns) = ( 1 + 2 * countAround($land, $x, $y, 19, $HlandPark));
                my($nr) = ( 1 + 3 * countAround($land, $x, $y, 19, $HlandUmiamu, $HlandInoraLand));
                my($nu) = ( 10 + random(10));
                my($value);
                $value = ($nt * $nu * $ns * $nr + int($island->{'pop'} / $Guest));
                if ($value > 0) {
                    $island->{'money'} += $value;
                    # ������
                    logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", "����");
                }
            }

            # HakoniwaCup
            my ($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $island->{'eisei4'});
            my ($yosengameendm) = 0;
            my ($hcgameseigen) = 1;
            my ($turn) = $HislandTurn % 100;
            my ($otry) = 3;
            my ($turn1, $goal, $tgoal);

            if ((0 < $turn) && ($turn < 41)) {                  # ͽ��
                $turn1 = int(($turn + 9) / 10);
                $hcgameseigen = 3 unless($HislandNumber < 21);
                $otry = 5;

            } elsif((41 < $turn) && ($turn < 47)) {             # �ࡹ�辡��
                $turn1 = 6;

            } elsif((46 < $turn) && ($turn < 50)) {             # ��辡��
                $turn1 = 7;

            } elsif((49 < $turn) && ($turn < 52)) {             # �辡��
                $turn1 = 8;

            } elsif($turn == 0) {                               # �����

                HakoCup_TeamReset($island);
                $Hstsanka++;
                # 100��������¿��Ū�ǳ��Ť��Ԥ��롣
                if ($Hstsanka == 1) {
                    $island->{'stsankahantei'}++;
                }
            }

            # ����
            if (!$turn1) {
                if (   ($stshoka == 10)
                    || ($stshoka == 11)) {

                    my ($stup);
                    $stup = random(3);
                    if ($stup == 0) {
                        $sto++;             # ����++
                    } elsif ($stup == 1) {
                        $std++;             # ���++
                    } else {
                        $stk++;             # KP++
                    }
                }
                next;
            }

            if(   ($stshoka == $turn1)
               && ($Hyosengameend < $hcgameseigen)  ) {

                my($tIsland);
                my($i);

                my(@order) = randomArray($HislandNumber);

                foreach $i (0..$islandNumber) {

                    last if($yosengameendm);

                    $tIsland = $Hislands[$order[$i]];               #����������Ф�
                    next if ($island->{'id'} == $tIsland->{'id'});  #��ʬ�Ȥ����ʤ�
                    next if ($tIsland->{'predelete'});              #�¤���ξ��Ͻ���

                    my($tSto, $tStd, $tStk, $tStwin, $tStdrow, $tStlose, $tStwint, $tStdrowt, $tStloset, $tStyusho, $tStshoka) = split(/,/, $tIsland->{'eisei4'});

                    next if (($tStshoka != $turn1) || ($Hyosengameend >= $hcgameseigen));

                    my($uphey, $tuphey, $uppoint, $tuppoint, $value, $str, $str1, $str2);

                    $goal = 0;
                    $tgoal = 0;

                    foreach (1..$otry) {
                        if(   (random($sto) > random($tStd))            # �� ���� > ��� ���
                           && (random($sto) > random($tStk)) ) {        # �� ���� > ��� KP
                            $goal++;                                    # �� ����++
                        }

                        next if($_ > 3);
                        if(   (random($tSto) > random($std))            # ��� ���� > �� ���
                           && (random($tSto) > random($stk))  ) {       # ��� ���� > �� KP
                            $tgoal++;                                   # ��� ����++
                        }
                    }

                    if(   ($turn1 > 5)
                       && ($goal == $tgoal) ) {                         # Ʊ��

                        if(random(100) < 60) {                          # 60 %
                            $goal++;                                    # �� ����++
                        } else {
                            $tgoal++;                                   # ��� ����++
                        }
                    }

                    $uphey    = int(($sto + $std + $stk) / 3);          # ��ʬ�ι���KP ��ʿ��
                    $tuphey   = int(($tSto + $tStd + $tStk) / 3);       # ���ι���KP ��ʿ��
                    $uppoint  = int(($tuphey - $uphey) / 2) + 5;        # ���-��ʬ /2 +5
                    $tuppoint = int(($uphey - $tuphey) / 2) + 5;        # ��ʬ-��� /2 +5

                    if ($turn1 == 8) {
                        $str1 = '�辡��';
                        $str2 = 'ͥ��';
                        $uppoint = 50;
                        $tuppoint = 50;

                    } elsif ($turn1 == 7) {
                        $str1 = '��辡��';
                        $str2 = '�辡�ʽ�';
                        $uppoint = 30;
                        $tuppoint = 30;

                    } elsif ($turn1 == 6) {
                        $str1 = '�ࡹ�辡��';
                        $str2 = '��辡�ʽ�';
                        $uppoint = 30;
                        $tuppoint = 30;

                    } else {
                        $str1 = "ͽ����${turn1}��";
                        $str2 = '����';
                    }

                    my($stup) = random(3);          # 0 - 2

                    $Hyosengameend++;
                    $yosengameendm++;
                    $stshoka++;
                    $tStshoka++;

                    if($goal > $tgoal) {

                        $stwin++;
                        $stwint++;
                        $styusho++ if($turn1 == 8);
                        $tStlose++;
                        $tStloset++;
                        $tStshoka = $turn1 + 6 if($turn1 > 5);
                        $value = (($stwin * 3 + $stdrow) * 1000);
                        $value *= 2 if($turn1 == 8);
                        $island->{'money'} += $value;
                        $str = "$value$HunitMoney";
                        logHCwin($id, $name, $str2, $str);

                        if($stup == 0) {
                            $tSto += $tuppoint;
                            $tStd += $tuppoint if($turn1 < 5);
                        } elsif($stup == 1) {
                            $tStd += $tuppoint;
                            $tStk += $tuppoint if($turn1 < 5);
                        } else {
                            $tStk += $tuppoint;
                            $tSto += $tuppoint if($turn1 < 5);
                        }

                    } elsif($goal < $tgoal) {
                        $tStwin++;
                        $tStwint++;
                        $tStyusho++ if($turn1 == 8);
                        $stlose++;
                        $stloset++;
                        $stshoka = $turn1 + 6 if($turn1 > 5);
                        my($value);
                        $value = (($tStwin * 3 + $tStdrow) * 1000);
                        $value *= 2 if($turn1 == 8);
                        $tIsland->{'money'} += $value;
                        $str = "$value$HunitMoney";
                        logHCwin($tIsland->{'id'}, islandName($tIsland), $str2, $str);
                        if ($stup == 0) {
                            $sto += $uppoint;                       # ����+
                            $std += $uppoint if($turn1 < 5);
                        } elsif($stup == 1) {
                            $std += $uppoint;
                            $stk += $uppoint if($turn1 < 5);
                        } else {
                            $stk += $uppoint;
                            $sto += $uppoint if($turn1 < 5);        # ����+
                        }

                    } else {
                        $stdrow++;
                        $stdrowt++;
                        $tStdrow++;
                        $tStdrowt++;
                    }
                    logHCgame($id, $tIsland->{'id'}, $name, islandName($tIsland), $lName, "${str1}", $goal, $tgoal,$island->{'hakoteam'},$tIsland->{'hakoteam'});
                    if($turn1 == 8) {
                        if($goal > $tgoal) {
                            logHCwintop($id, $name, int($HislandTurn / 100) * 100);
                        } elsif($goal < $tgoal) {
                            logHCwintop($tIsland->{'id'}, islandName($tIsland), int($HislandTurn / 100) * 100);
                        }
                    }
                    $tIsland->{'eisei4'} = "$tSto,$tStd,$tStk,$tStwin,$tStdrow,$tStlose,$tStwint,$tStdrowt,$tStloset,$tStyusho,$tStshoka";
                }
            }

            if ((($turn == 10) && ($stshoka == 1)) ||
                (($turn == 20) && ($stshoka == 2)) ||
                (($turn == 30) && ($stshoka == 3)) ||
                (($turn == 40) && ($stshoka == 4))) {
                logHCantiwin($id, $name, "ͽ����${stshoka}��");
                $stwin++;
                $stwint++;
                $stshoka++;
            }
            if (($turn1 == 6) && ($stshoka < 6)) {
                $stshoka = 11;
            }
            if (($turn == 46) && ($stshoka == 6)) {
                $stwin++;
                $stwint++;
                $stshoka++;
                logHCantiwin($id, $name, '�ࡹ�辡��');
            }
            if(($turn == 49) && ($stshoka == 7)) {
                $stwin++;
                $stwint++;
                $stshoka++;
                logHCantiwin($id, $name, '��辡��');
            }
            if(($turn == 51) && ($stshoka == 8)) {
                $stwin++;
                $stwint++;
                $stshoka++;
                $styusho++;
                logHCantiwin($id, $name, '�辡��');
                my($value);
                $value = (($stwin * 3 + $stdrow) * 1000)*2;
                $island->{'money'} += $value;
                logHCwin($id, $name, '�Ȥꤢ������ͥ��', "$value$HunitMoney");
                $hcturn = int($HislandTurn/100)*100;
                logHCwintop($id, $name, $hcturn);
            }

            if(($turn == 52) && ($stshoka != 9)) {
                $stshoka = 10;
            }
            if(($stshoka == 10) || ($stshoka == 11)) {
                my($stup);
                $stup = random(3);
                if($stup == 0) {
                    $sto++;
                } elsif($stup == 1) {
                    $std++;
                } else {
                    $stk++;
                }
            }
            $island->{'eisei4'} = "$sto,$std,$stk,$stwin,$stdrow,$stlose,$stwint,$stdrowt,$stloset,$styusho,$stshoka";

        } elsif ($landKind == $HlandGold) {
            # �⻳
            my $DepletionPar = 7;
            my $value = $lv * 25 + random(501);
            $island->{'money'} += $value;

            # ������
            logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", '����');

            # �ϳ�Ƚ��
            if(random(100) < $DepletionPar) {
                # �ϳ�
                logGoldEnd($id, $name, $lName, $this_pos);
                $land->[$x][$y] = $HlandMountain;
            }

        } elsif ($landKind == $HlandRottenSea) {
            # �峤
            if ( ($island->{'BF_Flag'} == $HBF_MONSTER_HOUSE) ) {
                $land->[$x][$y] = $HlandPlains;
                $landValue->[$x][$y] = 0;
                $landValue2->[$x][$y] = 0;

            }else {
                my ($i, $sx, $sy, $kind, $lv);
                for ($i = 1; $i < 7; $i++) {
                    $sx = $x + $ax[$i];
                    $sy = $y + $ay[$i];

                    # �Ԥˤ�����Ĵ��
                    $sx-- if(!($sy % 2) && ($y % 2));
                    # �ϰϳ�
                    next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

                    my $sL = $land->[$sx][$sy];
                    my $sLv = $landValue->[$sx][$sy];
                    my $sLv2 = $landValue2->[$sx][$sy];
                    my $lName = landName($sL, $sLv, $sLv2);
                    # �������𡢳����Իԡ����쿷�Իԡ����������ߤ塢���ġ��ܿ��졢�峤�ʳ�
                    unless (   ($sL == $HlandSea)
                            || ($sL == $HlandSbase)
                            || ($sL == $HlandIce)
                            || ($sL == $HlandSeacity)
                            || ($sL == $HlandSeatown)
                            || ($sL == $HlandUmishuto)
                            || ($sL == $HlandFune)
                            || ($sL == $HlandFrocity)
                            || ($sL == $HlandUmiamu)
                            || ($sL == $HlandOil)
                            || ($sL == $HlandUmicity)
                            || ($sL == $HlandNursery)
                            || ($sL == $HlandYougan)
                            || ($sL == $HlandOmamori)
                            || ($sL == $HlandOilCity)
                            || ($sL == $HlandEgg)
                            || ($sL == $HlandRottenSea)
                            || (   ($sL == $HlandMonster)
                                && (isSeaMonster($sLv)) )
                                                          ) {
                        my ($n) = countAround($land, $sx, $sy, 7, $HlandRottenSea);
                        my ($point) = "($sx, $sy)";

                        if (   (($n >= 4) && (random(100) < 30))    # ���Ϥ��峤�����ޥ��ʾ夢���30% �γ�Ψ�ǰ��߹���
                            || ($n && (random(100) < 10))) {        # ���Ϥ��峤�����ޥ��ʾ夢���10% �γ�Ψ�ǰ��߹���
                            
                            logDamageAny($id, $name, $lName, $point, '<B>�峤</B>�˰��߹��ޤ�ޤ�����');
                            SetRottenSea($island , $sx , $sy);
                        }
                    }
                }
            }

            my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
            $island->{'happy'} -= ($happy * 2);

        } elsif ($landKind == $HlandHouse) {
            # ���β�
            my ($hlv);
            my ($zeikin);
            my ($tax) = 0;

            foreach (0..9) {
                $hlv = 9 - $_;
                last if($island->{'pts'} > $HouseLevel[$hlv]);
            }

            $island->{'turntax'} = 0;

            $landValue->[$x][$y] = $hlv;
            $zeikin = int($island->{'pop'} * ($hlv + 1) * $island->{'eisei1'} / 100);
            if ($zeikin > 10000) {
                if ($HislandTurn % 5 == 0) {
                    $tax = 1;
                }
                $island->{'turntax'} = int($zeikin / 5);
            } elsif ($zeikin > 5000) {
                if ($HislandTurn % 2 == 0) {
                    $tax = 1;
                }
                $island->{'turntax'} = int($zeikin / 2);
            } else {
                if ($zeikin > 0) {
                    $tax = 1;
                }
                $island->{'turntax'} = $zeikin;
            }

            if ($tax) {

                $island->{'money'} += $zeikin;
                $island->{'tax_income'} = $zeikin;
                logSecret("${HtagMoney_}${zeikin}${HunitMoney}${H_tagMoney}���Ǽ�������ޤ�����",$id);
            }

            my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
            $island->{'happy'} += $happy;

        } elsif ($landKind == $HlandCollege) {
            # ���
            # �����Ǥμ��Ф�
            my ($clv) = $landValue->[$x][$y];

            if (($clv == 99) && !$island->{'c28'}) {
                logMstakeoff($id, $name, $lName,$this_pos);
                $land->[$x][$y] = $HlandPlains;
                $landValue->[$x][$y] = 0;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
            }

            # ����
            if ($landValue2->[$x][$y] > 0) {
                $landValue2->[$x][$y]--;
            }

            my ($monsno) = $island->{'monsterlive'};
            next if(!$monsno);

            $monsterCount = countAroundMonster_wo_Pet($island, $x, $y, 7) if ($island->{'monsterlive'});
            if ($monsterCount) {
                logMonsAttacks($id, $name, $lName, $this_pos);
                $landValue2->[$x][$y] += 1 + random(2);
            }

            my ($take) = 0;
            my ($i, $sx, $sy, $monsArray, $monspnt);
            $monsArray = $island->{'monspnt'};

            if ($clv == 4) {        # ��ʪ���
                for ($i = 0; $i < $monsno; $i++){
                    $monspnt = $monsArray->[$i];
                    ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                    if ($land->[$sx][$sy] == $HlandMonster) {
                        # �оݤȤʤ���äγ����Ǽ��Ф�
                        my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                        # my($tlv) = $landValue->[$sx][$sy];
                        if ($tKind == 28) {

                        }
                        else {
                            my($ssx, $ssy, $i, $landKind, $lv, $point);
                            for($i = 1; $i < 7; $i++) {
                                $ssx = $sx + $ax[$i];
                                $ssy = $sy + $ay[$i];
                                # �Ԥˤ�����Ĵ��
                                $ssx-- if(!($ssy % 2) && ($sy % 2));
                                # �ϰϳ�Ƚ��
                                next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));

                                if (   (!$take)
                                    && ($land->[$ssx][$ssy] == $HlandWaste)
                                    && (!$island->{'c28'})) {
                                    my($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
                                    my $kind = 28;
                                    $landValue->[$ssx][$ssy] = ($kind << $Mons_Kind_Shift) + $mshp;
                                    $land->[$ssx][$ssy] = $HlandMonster;
                                    $landValue2->[$ssx][$ssy] = 0;
                                    $landValue3->[$ssx][$ssy] = 0;
                                    logMstakeon($id, $name, '��ʪ��ؤΥޥ����åȤ��Τ�',$this_pos);

                                    $landValue->[$x][$y] = 99;
                                    $take++;
                                    $island->{'co99'}++;
                                    $island->{'monsterlive'}++;
                                    last;
                                }
                            }
                        }
                    }
                    last if($take);
                }

            } elsif($clv == 98) {       # ��ʪ���
                for ($i = 0; $i < $monsno; $i++){
                    $monspnt = $monsArray->[$i];
                    ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});

                    if ($land->[$sx][$sy] == $HlandMonster) {
                        # �оݤȤʤ���äγ����Ǽ��Ф�
                        my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                        # my($tlv) = $landValue->[$sx][$sy];
                        # my($tspecial) = $HmonsterSpecial[$tKind];
                        if ($tKind == 30) {

                        } else {

                            my ($ssx, $ssy, $i, $landKind, $lv, $point);
                            for ($i = 1; $i < 7; $i++) {
                                $ssx = $sx + $ax[$i];
                                $ssy = $sy + $ay[$i];
                                # �Ԥˤ�����Ĵ��
                                $ssx-- if (!($ssy % 2) && ($sy % 2));
                                # �ϰϳ�Ƚ��
                                next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));

                                if (!$take && ($land->[$ssx][$ssy] == $HlandWaste) && !$island->{'c28'}) {
                                    my($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
                                    my ($kind) = 30;
                                    $land->[$ssx][$ssy] = $HlandMonster;
                                    $landValue->[$ssx][$ssy] = ($kind << $Mons_Kind_Shift) + $mshp;
                                    $landValue2->[$ssx][$ssy] = 0;
                                    $landValue3->[$ssx][$ssy] = 0;
                                    logMstakeon($id, $name, 'Ķ���åƥȥ�',$this_pos);

                                    $landValue->[$x][$y] = 99;
                                    $take++;
                                    $island->{'co99'}++;
                                    $island->{'monsterlive'}++;
                                    last;
                                }
                            }
                        }
                    }
                    last if($take);
                }
            }

        } elsif ($landKind == $HlandShrine) {
            # ���ο���
            if($landValue->[$x][$y]) {
                # �����С��ȥ�֥�ʤɤǥǡ������ʤ��ʤäƤ�����ͤ򣰤�
                unless(-e "${HdirName}/savedata.$id") {
                    $landValue->[$x][$y] = 0 ;
                    logSaveLoadVanish($id, $name);
                }
            }
            unless((countAround($land, $x, $y, 7, $HlandForest) == 6) &&
                    (countAround($land, $x, $y, 19, $HlandSea , $HlandFrocity) == 12)) {
                # ����1Hex���٤ƿ�������ˤ��μ��Ϥ��٤Ƥ���(������)�ξ�郎�����
                unlink("${HdirName}/savedata.$id") if(-e "${HdirName}/savedata.$id");
                $land->[$x][$y] = $HlandMountain;
                $landValue->[$x][$y] = 0;
                $landValue2->[$x][$y] = 0;
            }

        } elsif($landKind == $HlandEgg) {
            # ������
            my ($molv) = $landValue->[$x][$y];
            my @rflag = (5, 3, 3, 5);
            my @mflag = ([5, 25, 35, 25], [3, 20, 40, 15], [3, 30, 40, 30], [10, 25, 30, 30]);
            if(random(100) < $rflag[$molv]) {
                my ($i, $sx, $sy);
                for($i = 0; $i < 7; $i++) {
                    $sx = $x + $ax[$i];
                    $sy = $y + $ay[$i];
                    # �Ԥˤ�����Ĵ��
                    $sx-- if(!($sy % 2) && ($y % 2));
                    # �ϰϳ�
                    next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

                    my $sLname = landName($land->[$sx][$sy], $landValue->[$sx][$sy], $landValue2->[$sx][$sy]);
                    my ($mKind, $mName, $mHp);
                    # �ϰϤˤ��ʬ��
                    if ($i < 1) {
                        # �濴�������1�إå���
                        if (random(100) < $mflag[$molv][0]) {
                            $mKind = $Mons_Mikael;  # �ߥ�����
                        } elsif(random(100) < $mflag[$molv][1]) {
                            $mKind = $Mons_Tetra;  # �ƥȥ�
                        } elsif(random(100) < $mflag[$molv][2]) {
                            $mKind = $Mons_SlimeLegend;  # ����쥸��
                        } elsif(random(100) < $mflag[$molv][3]) {
                            $mKind = $Mons_HaneHamu;  # �ϤͤϤ�
                        } else {
                            $mKind = $Mons_Inora;  # ���Τ�(�Ϥ���)
                        }

                        $mHp = $HmonsterBHP[$mKind] + random($HmonsterDHP[$mKind]);
                        my $sLv = ($mKind << $Mons_Kind_Shift) + $mHp;
                        $land->[$sx][$sy] = $HlandMonster;
                        $landValue->[$sx][$sy] = $sLv;
                        $landValue2->[$sx][$sy] = 0;
                        $island->{'monsterlive'}++;
                        logEggBomb($id, $name, $sLname, $HmonsterName[$mKind], "($sx, $sy)");

                    } else {
                        # 2�إå���
                        if (($landKind == $HlandSea) ||
                            ($landKind == $HlandOil) ||
                            ($landKind == $HlandMountain) ||
                            ($landKind == $HlandGold) ||
                            ($landKind == $HlandOnsen) ||
                            ($landKind == $HlandSeacity) ||
                            ($landKind == $HlandUmishuto) ||
                            ($landKind == $HlandSeatown) ||
                            ($landKind == $HlandUmiamu) ||
                            ($landKind == $HlandSbase)  ) {

                            # �ʤˤ�ʤ�
                        }else{
                            logEggDamage($id, $name, $sLname, "($sx, $sy)");
                            SetSeaLand_Normal($island, $sx, $sy);     # �����᤹
                        }
                    }
                }
            }

        } elsif($landKind == $HlandMonument) {      #��ǰ�ꥤ�٥��
            # �����Ǥμ��Ф�
            my($molv) = $landValue->[$x][$y];

            if(($molv == 0) || ($molv == 10) || ($molv == 15) || ($molv == 16) || ($molv == 33)) {
                if(random(100) < 5) {
                    # �ߤ䤲
                    my $value = 1+ random(49);
                    $island->{'money'} += $value;
                    logMiyage($id, $name, $lName, $this_pos, "$value$HunitMoney") if($value);
                }

            } elsif($molv == 1) {
                if(random(100) < 1) {
                    # ����
                    my $value = int($island->{'pop'} / 100) * 10+ random(11); # �͸������ͤ��Ȥ�1000�ȥ�μ���
                    #$island->{'food'} += $value;
                    food_product_plus($island , 'yasai' ,$value);
                    logParkEventt($id, $name, $lName, $this_pos, "$value$HunitFood") if($value);
                }

            } elsif($molv == 84) {                # �������

                if(random(100) < 75) {
                    # ����
                    my ($nt) = countAround($land, $x, $y, 19, @Htowns);
                    my $value = random($nt * 20 + $lv * 5 + int($island->{'pop'} / 20)) + random(100) + 100;
                    if ($value > 0) {
                        $island->{'money'} += $value;
                        # ������
                        logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", '����');
                    }
                }

                if(($island->{'shr'} < 1) &&
                    (countAround($land, $x, $y, 7, $HlandForest) == 6) &&
                    (countAround($land, $x, $y, 19, $HlandSea) == 12)) {
                    # ����1Hex���٤ƿ�������ˤ��μ��Ϥ��٤Ƥ���(������)�ʤ�ֻ��ο��¡פˤʤ�
                    $land->[$x][$y] = $HlandShrine;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                }

            } elsif($molv == 93) {                # ����

                Mikael_Luck($island , $this_pos , $landKind , $lName);

            } elsif($molv == 95) {
                if(random(100) < 20) {
                    # ����
                    my $value = 1 + random(1234);
                    $island->{'money'} += $value;
                    logOilMoney($id, $name, $lName, $this_pos, "$value$HunitMoney", '����');

                }
            }

            my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
            $island->{'happy'} += $happy;

        } elsif($landKind == $HlandYougan) {           # �ϴ䥤�٥��
            $landValue->[$x][$y]--;
            if ($landValue->[$x][$y] <= 0) {
                $land->[$x][$y] = $HlandWaste;
                $landValue->[$x][$y] = 0 ;
                $landValue2->[$x][$y] = 0 ;
                $landValue3->[$x][$y] = 0 ;
            }

        } elsif($landKind == $HlandOmamori) {           # �����

            if(!$landValue->[$x][$y]) {
                $land->[$x][$y] = $HlandPlains;
                $landValue->[$x][$y] = 0;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;

            } else {
                $landValue->[$x][$y]--;
            }

        } elsif($landKind == $HlandZoo) {               # ưʪ��

            my ($zookazu);
            my ($zookazus);
            my ($m_syurui);      #���ü���

            my ($tmp);
            my (@mons_list);
            $tmp = $island->{'zoo'};
            chomp($tmp);

            @mons_list = split(/\,/,$tmp);

            my ($kazu);
            my ($valuef);

            ($zookazu, $zookazus, $m_syurui) = Get_ZooState($island);

            # 1���1��
            if ($zooflag > 0) {

            } else {

                $zooflag = 1;       # 1���1��

                my ($value);
                $value  = ($zookazus * 15) + ($m_syurui * 150);
                $valuef = $zookazu * 250;                       # ��������

                # ���Ϥˤ��������㲼
                # ���Ϥʤ�����ޥ���
                #if($island->{'shouhi'} > $island->{'ene'}) {
                #    $value = int($value/10);
                #}

                # ���������
                # $s08 �� ���� �Ϥʤ��Τ� 0
                if (random(100) < 60 + 0) {

                    my ($i,$sx,$sy);
                    my ($zlv) = (0);
                    # ���ưʪ�ॵ�������פ��롣
                    for ($i = 0; $i < $HpointNumber; $i++) {
                        $sx = $Hrpx[$i];
                        $sy = $Hrpy[$i];
                        if ($land->[$sx][$sy] == $HlandZoo) {
                            $zlv += $landValue->[$sx][$sy];
                        }
                    }

                    # ��������������
                    my ($siire);
                    my ($flag , $plus);
                    $siire = random($#HmonsterName);

                    $flag = GetTaijiFlag($island , $siire);

                    if (   ($flag)                      # �ݤ������Ȥ������
                        && ($zlv > $zookazu)            # ���ä��ޤ������뤫�ɤ�����
                        && (random(100) < $HmonsterZoo[$siire])
                                                                ) {

                        $plus = ($mons_list[$siire]) ? ($mons_list[$siire] + 1) : 1 ;
                        logSiire($id, $name, $lName, "$HmonsterName[$siire]", "($x, $y)");
                        Write_ZooState($island , $siire , $plus );
                    }

                }

                if (($value > 0) && ($zookazu > 0)) {
                    $island->{'money'} += $value;
                    food_product_consumption($island , $valuef);
                    # ������
                    my($str) = "$value$HunitMoney";
                    my($str2) = "$valuef$HunitFood";
                    logOilMoney2($id, $name, $lName, $this_pos, $str, $str2);
                }
            }

            my ($escape_par) = int( ((($zookazus * 25) - $island->{'rena'}) / 10) );

            if ($escape_par < 0) {
                $escape_par = 0;
            }

            if (   ($island->{'rena'} < ($zookazus * 25))
                && (random(100) < 15 + $escape_par)
                                        ) {

                my ($nigekaiju);
                my ($lp);
                my ($limit) = random($zookazu * 2);

                for ($lp = 1 ; $lp < $limit ; $lp++) {

                    if ($mons_list[$lp] > 0) {
                        $lp++;
                        $nigekaiju = $lp;
                    }
                }

                if ($mons_list[$nigekaiju] > 0) {

                    $mons_list[$nigekaiju] -= 1;
                    $lv = Calc_MonsterLandValue($nigekaiju);
                    $land->[$x][$y] = $HlandMonster;
                    $landValue->[$x][$y] = $lv;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    $island->{'monsterlive'}++;
                    my($mKind, $mName, $mHp) = monsterSpec($lv);
                    logNige($id, $name, $lName, $mName, $this_pos);
                    logMonsMove($id, $name, $lName, $this_pos, $mName , "��Ƨ�߹Ӥ餵��ޤ�����");
                    Write_ZooState($island , $nigekaiju , $mons_list[$nigekaiju]);
                }
            }

        } elsif($landKind == $HlandBigFood) {           # �����

            BigFoodEvent($island,$x,$y);

        } elsif($landKind == $HlandFrocity) {

            $monsterCount = CityAttack($island, $x, $y);
            $lv = $landValue->[$x][$y];

            if ($monsterCount > 0) {

                if ($lv <= 0) {

                    SetSeaLand_Normal($island, $x, $y);     # �����᤹
                    next;
                }
            }

            if($addpop < 0) {
                # ��­
                $lv -= (random(-$addpop) + 1);
                if($lv <= 0) {

                    SetSeaLand_Normal($island, $x, $y);     # �����᤹
                    next;
                }
            } else {
                # ��Ĺ
                $lv = Town_Growup( $lv , $addpop , $addpop2 , 100 );
            }
            if($lv > $HFrocity_limit) {
                $lv = $HFrocity_limit;
            }
            $landValue->[$x][$y] = $lv;

            # ư�����������
            my($d, $sx, $sy);
            my($i);

            for($i = 0; $i < 3; $i++) {
                $d = random(6) + 1;
                $sx = $x + $ax[$d];
                $sy = $y + $ay[$d];

                # �Ԥˤ�����Ĵ��
                if((($sy % 2) == 0) && (($y % 2) == 1)) {
                    $sx--;
                }

                # �ϰϳ�Ƚ��
                if (   ($sx < 0) || ($sx > $islandSize)
                    || ($sy < 0) || ($sy > $islandSize)) {
                    next;
                }

                if (countAround($land, $sx, $sy, 19, $HlandShrine) > 0){
                    next;
                }

                # �������𡢳����Իԡ����ġ����á�������ǰ��ʳ�
                if(   ($land->[$sx][$sy] == $HlandSea) ) {
                    last;
                }
            }

            if($i == 3) {
                # ư���ʤ��ä�
                next;
            }

            # ư��������Ϸ��ˤ���å�����
            my($l) = $land->[$sx][$sy];
            my($lv) = $landValue->[$sx][$sy];
            my($lv2) = $landValue2->[$sx][$sy];
            my($lName) = landName($l, $lv,$lv2);
            my($point) = "($sx, $sy)";

            # ��ư
            $land->[$sx][$sy] = $land->[$x][$y];
            $landValue->[$sx][$sy] = $landValue->[$x][$y];
            $landValue2->[$sx][$sy] = $landValue2->[$x][$y];
            $landValue3->[$sx][$sy] = $landValue3->[$x][$y];

            # ��ȵ錄���֤򳤤�
            SetSeaLand_Normal($island, $x, $y);     # �����᤹

        } elsif($landKind == $HlandTrain) {     # ��ϩ

            my ($rail) = $lv & $Train_Mask;

            if ($on_train == $train_sta) {

                $rail = $rail | $Train_Exist;
            }

            $landValue->[$x][$y] = $rail;
            $train_sta++;

        } elsif($landKind == $HlandFune) {      #�����٥��
            # ��
            # ���Ǥ�ư������
            next if($funeMove[$x][$y] == 2);

            # �����Ǥμ��Ф�
            my($funespe) = $HfuneSpecial[$lv];
            my($mvalue, $tvalue, $fvalue, $fvalue2, $movalue) = (0, 0, 0, 0, 0);

            my($sinkflag) = ((($lv > 7) && ($lv < 11) || ($lv == 19)) ? 5 : 30);

            # ����Ƚ��
            if(random(1000) < $sinkflag) {
                # ���ΤΤ�������
                logDamageAny($id, $name, $lName, $this_pos, '���ΤΤ������פ��ޤ�����');
                SetSeaLand_Normal($island, $x, $y);     # �����᤹

                # �ݸ�����
                $mvalue = 1+ random(399);
                $island->{'money'} += $mvalue;
                logHoken($id, $name, $lName, $this_pos, "$mvalue$HunitMoney");
                next;
            }

            if(!$lv) { # ��������(����)
                $lv = 1;
                $landValue->[$x][$y] = 1;
            }

            if($lv == 1) { # ��������
                $mvalue = -5; # �ݻ���
                $fvalue = 290+ random(30); # ����

            } elsif($lv == 2) { # �淿����
                $mvalue = -20; # �ݻ���
                $fvalue = 490+ random(40); # ����

            } elsif($lv == 3) { # ����õ����
                $mvalue = -300; # �ݻ���
                if(random(1000) < 5) {
                    # ����ȯ��(�ݻ����Ƚ�)
                    $tvalue = 1 + random(49999);
                }

            } elsif($lv == 4) { # ����
                $mvalue = int((150+ random(250)) * $Hmoney2Incom[$Hmonth]/100); # �Ѹ�����
                $fvalue2 = -1000; # �ݻ�����

            } elsif($lv == 5) { # �緿����
                $mvalue = -60; # �ݻ���
                $fvalue = 690+ random(40); # ����

            } elsif($lv == 6) { # ��®����
                $mvalue = -30; # �ݻ���
                $fvalue = 490+ random(40); # ����

            } elsif($lv == 7) { # ����õ��������
                $mvalue = -500; # �ݻ���
                if(random(100) < 1) {
                    # ����ȯ��(�ݻ����Ƚ�)
                    $tvalue = 500 + random(99999);
                }

            } elsif ($lv == 8) { # ��ڵ���TITANIC
                $mvalue = int((1500 + int($island->{'pop'} / 10) * 1) * $Hmoney2Incom[$Hmonth]/100);    # �Ѹ�����
                $fvalue2 = -3000; # �ݻ�����

                if (random(100) < 10) {
                    # ɹ��
                    $land->[$x][$y] = $HlandIce;
                    $landValue->[$x][$y] = 0;
                    $movalue = int($island->{'pop'} / 10) * 2;    # �ǲ貽
                }

            } elsif ($lv == 9) { # ���RENAS
                $mvalue = -100; # �ݻ���

                my ($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};

                if ($monsno > 0) {
                    my($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for($i = 0; $i < $monsno; $i++){
                        last if($kougekiseigen > 1);        # ���RENAS�� 1��ˤĤ���2ȯ�ι��⤬�Ǥ��롣
                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if($land->[$sx][$sy] == $HlandMonster){
                            my $value = 100;
                            $island->{'money'} -= $value;

                            # �оݤȤʤ���äγ����Ǽ��Ф�
                            my($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                            my($tlv) = $landValue->[$sx][$sy];

                            # �оݤ��Ų���ʤ���̤ʤ�
                            next if (isMonsterCuring($tKind));

                            logMonsAttackt($id, $name, $lName, $this_pos, $tName, $tPoint);
                            $kougekiseigen++;

                            # �оݤ����Ϥ򸺤餹
                            $tHp--;

                            if($tHp > 1){
                                $tlv--;
                                $landValue->[$sx][$sy] = $tlv;
                            } else {
                                # �оݤβ��ä��ݤ�ƹ��Ϥˤʤ�
                                MonsterDead($island , $sx , $sy , $tKind , 0 );
                                # �󾩶�
                                AddMonsterReward($island , $tKind);
                            }
                            next;
                        }
                    }
                }

            } elsif($lv == 10) {    # ���ERADICATE
                $mvalue = -400;     # �ݻ���

                my ($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};
                if ($monsno > 0) {
                    my ($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};

                    for ($i = 0; $i < $monsno; $i++) {

                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster) {
                            my $value = 3000;
                            $island->{'money'} -= $value;

                            # �оݤȤʤ���äγ����Ǽ��Ф�
                            my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                            logFuneAttack($id, $name, $lName, $this_pos, $tName, "($sx, $sy)");

                            my ($ssx, $ssy, $i, $sLandKind, $sLandName, $sLv, $sLv2 ,$point);

                            my ($lp);
                            for($lp = 0; $lp < 7; $lp++) {
                                $ssx = $sx + $ax[$lp];
                                $ssy = $sy + $ay[$lp];

                                # �Ԥˤ�����Ĵ��
                                $ssx-- if(!($ssy % 2) && ($sy % 2));

                                # �ϰϳ�Ƚ��
                                next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));
                                if ( countAround($land, $ssx, $ssy, 19, $HlandShrine) > 0 ){
                                    next;
                                }

                                $sLandKind = $land->[$ssx][$ssy];
                                $sLv = $landValue->[$ssx][$ssy];
                                $sLv2 = $landValue2->[$ssx][$ssy];
                                $sLandName = landName($sLandKind, $sLv, $sLv2);
                                $point = "($ssx, $ssy)";

                                # �ϰϤˤ��ʬ��
                                if($lp < 1) {
                                    # �濴
                                    SetSeaShallowLand($island , $ssx,$ssy);
                                    $island->{'monsterlive'} -= 1;
                                    logDamageAny($id, $name, $sLandName, $point, "�᤭���ӿ��פ��ޤ�����");
                                } else {
                                    # 1�إå���
                                    if (NoDamage_by_Bomb1HEX($sLandKind)) {
                                        # ���᡼���Τʤ��Ϸ�
                                    } else {
                                        SetWasteLand_Normal($island , $ssx,$ssy);
                                        if($sLandKind == $HlandMonster) {
                                            $island->{'monsterlive'} -= 1;
                                            logDamageAny($id, $name, $sLandName, $point, "�ä����Ӥޤ�����");
                                        } else {
                                            logDamageAny($id, $name, $sLandName, $point, "��֤ˤ���<B>����</B>�Ȳ����ޤ�����");
                                        }
                                    }
                                }
                            }
                            next;
                        }
                    }
                }

            } elsif($lv == 11) { # ����MASTER
                $mvalue = -60; # �ݻ���
                $fvalue = 690+ random(40); # ����

            } elsif($lv == 19) { # �������

                $mvalue = -1000; # �ݻ���

                my ($heat) = 0;
                my($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};
                if($monsno > 0) {
                    my ($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for($i = 0; $i < $monsno; $i++){
                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster) {

                            my $value = 50000;
                            $island->{'money'} -= $value;
                            # �оݤȤʤ���äγ����Ǽ��Ф�
                            my($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                            logFuneAttackSSS($id, $name, $lName, $this_pos, $tName, "($sx, $sy)");
                            $land->[$sx][$sy] = $HlandWaste;
                            $landValue->[$sx][$sy] = 0;
                            $heat++;

                            my $rena = $island->{'rena'};
                            if (random($rena) > (3000 + $heat * 1000)) {
                                logFuneAttackSSSR($id, $name, $lName, $this_pos, $tName, "($sx, $sy)");
                            } else {
                                logFuneAttackSSST($id, $name, $lName, $this_pos, $tName, "($sx, $sy)");
                                my ($ssx, $ssy, $i, $sLandKind, $sLandName, $sLv, $sLv2, $point);
                                my ($lp);
                                for ($i = 0; $i < 7; $i++) {
                                    $ssx = $x + $ax[$i];
                                    $ssy = $y + $ay[$i];

                                    # �Ԥˤ�����Ĵ��
                                    $ssx-- if(!($ssy % 2) && ($y % 2));

                                    # �ϰϳ�Ƚ��
                                    next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));
                                    if ( countAround($land, $ssx, $ssy, 19, $HlandShrine) > 0 ){
                                        next;
                                    }
                                    $sLandKind = $land->[$ssx][$ssy];
                                    $sLv = $landValue->[$ssx][$ssy];
                                    $sLv2 = $landValue2->[$ssx][$ssy];
                                    $sLandName = landName($sLandKind, $sLv, $sLv2);
                                    $point = "($ssx, $ssy)";

                                    # �ϰϤˤ��ʬ��
                                    if($i < 1) {
                                        # �濴
                                        SetSeaShallowLand($island , $ssx,$ssy);
                                        $island->{'monsterlive'} -= 1;
                                        logDamageAny($id, $name, $sLandName, $point, "�᤭���ӿ��פ��ޤ�����");
                                    } else {
                                        # 1�إå���
                                        if (NoDamage_by_Bomb1HEX($sLandKind)) {
                                            # ���᡼���Τʤ��Ϸ�
                                        } else {
                                            SetWasteLand_Normal($island , $ssx,$ssy);
                                            if($sLandKind == $HlandMonster) {
                                                my ($tKind, $tname, $thp) = monsterSpec($sLv);
                                                MonsterDead($island , $ssx , $ssy , $tKind , 0 );
                                                logDamageAny($id, $name, $sLandName, $point, "�ä����Ӥޤ�����");
                                            } else {
                                                SetWasteLand_Normal($island , $ssx,$ssy);
                                                logDamageAny($id, $name, $sLandName, $point, "��֤ˤ���<B>����</B>�Ȳ����ޤ�����");
                                            }
                                        }
                                    }
                                }
                                next;
                            }
                        }
                    }
                }
            }

            # �Ѹ��������ݻ���
            $island->{'money'} += $mvalue;
            logOilMoney($id, $name, $lName, $this_pos, "$mvalue$HunitMoney", "�Ѹ�����") if($mvalue > 0);
            # ����
            $island->{'money'} += $tvalue;
            logTansaku($id, $name, $lName, $this_pos, "$tvalue$HunitMoney") if($tvalue);
            # �ǲ貽
            $island->{'money'} += $movalue;
            logDamageAny($id, $name, $lName, $this_pos, "ɹ���˷��ͤ�������Ĥˤʤ����פ��ޤ�����") if($movalue);
            logTitanicEnd($id, $name, $lName, $this_pos, "$movalue$HunitMoney") if($movalue);
            # ����
            $fvalue = int($fvalue * $Hfood2Incom[$month]/100);
            $fvalue2 = int($fvalue2 * $HeatenFoodS[$month]/100);
            food_product_consumption($island , -$fvalue2);
            food_product_plus($island , 'seafood' , $fvalue);
            logParkEventf($id, $name, $lName, $this_pos, "$fvalue$HunitFood") if(($fvalue + $fvalue2 > 0) && !$HlogOmit1);
            $island->{'fishcatch'} += $fvalue if($HlogOmit1);
            $island->{'fishcatch'} += $fvalue2 if($HlogOmit1 == 2);

            # ư�����������
            my($d, $sx, $sy);
            my($i);
            for($i = 0; $i < 3; $i++) {
                $d = random(6) + 1;
                $sx = $x + $ax[$d];
                $sy = $y + $ay[$d];

                # �Ԥˤ�����Ĵ��
                $sx-- if(!($sy % 2) && ($y % 2));
                # �ϰϳ�Ƚ��
                next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));
                if ( countAround($land, $sx, $sy, 19, $HlandShrine) > 0 ){
                    next;
                }
                # ���ʤ��ư
                last if($land->[$sx][$sy] == $HlandSea);
            }

            # ư���ʤ��ä�
            next if($i == 3);

            # ��ư
            $land->[$sx][$sy] = $land->[$x][$y];
            $landValue->[$sx][$sy] = $landValue->[$x][$y];
            $landValue2->[$sx][$sy] = $landValue2->[$x][$y];
            $landValue3->[$sx][$sy] = $landValue3->[$x][$y];
            # ��ȵ錄���֤򳤤�
            SetSeaLand_Normal($island, $x, $y);     # �����᤹

            if ( $island->{'oil'} < 10 ){
                if( (($lv == 3) && (random(100) < 2)) || # ���ĸ��ä�
                    (($lv == 7) && (random(100) < 4)) ) {
                    logTansakuoil($id, $name, $lName, $this_pos);
                    $land->[$x][$y] = $HlandOil;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    $island->{'oil'}++;
                }
            }

            # ��ư�Ѥߥե饰
            if($funespe == 2) {
                # ��ư�Ѥߥե饰��Ω�Ƥʤ�
            } elsif($funespe) {
                # ®����
                $funeMove[$sx][$sy] = $funeMove[$x][$y] + 1;
            } else {
                # ���̤���
                $funeMove[$sx][$sy] = 2;
            }

        } elsif ($landKind == $HlandFactory) {              # ���� ���٥��

            FactoryEvent($island , $x , $y);

            if ($landValue2->[$x][$y] == 0) {
                my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
                $island->{'happy'} -= $happy;
            }

        } elsif ($landKind == $HlandGomi) {                 # ���ߥ��٥��

            my ($kaisyu);
            my ($gomi_const) = 1500;
            my ($gomi_minus) = 5;
            my ($gomi_limit) = 800000;

            if ($landValue->[$x][$y] < $gomi_limit) {

                $kaisyu = ($island->{'gomi'} < $gomi_const) ? $island->{'gomi'} : $gomi_const;

                $island->{'gomi'} -= $kaisyu;
                $landValue->[$x][$y] += $kaisyu;
            }
            $landValue->[$x][$y] -= $gomi_minus;

        } elsif ($landKind == $HlandFoodim) {              # ��ʪ����� ���٥��

            my ($happy) = Calc_Happiness_Town($island,$x,$y,7);
            $island->{'happy'} -= $happy;

        } elsif ($landKind == $HlandMonster) {           # ���� ���٥��
            next if ($monsterMove[$x][$y] == 2);
            # ���Ǥ�ư������

            # �����Ǥμ��Ф�
            my ($mKind, $mName, $mHp) = monsterSpec($lv);
            my ($special) = $HmonsterSpecial[$mKind];

            # ----------------------------------------- #
            # ��ư�Ǥ��ʤ��Ƥ�Ǥ����ư
            #
            # ----------------------------------------- #

            if ($mKind == $Mons_hime_inora) { # �Ҥᤤ�Τ�
                my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
                $mon += 1;

                if (   ($mon != 3)
                    || ($mday != 3)) {

                    $land->[$x][$y]      = $HlandBigFood;
                    $landValue->[$x][$y] = (3 << $Food_Kind_Shift) + 5;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    logHimeKaeru($id, $name, $mName);
                }
            }

            # ��פ��롩
            if (   ($special == 14)
                || ($special == 15)
                || ($special == 16)
                || ($special == 20)     # �Ҥᤤ�Τ�
                                    ) {

                my ($r) = random(100);
                my ($warp_par) = 60;

                $r = 0 if ($special == 16);                     # special 16��ɬ�����
                $r = 0 if ($special == 20);                     # special 20���Ҥᤤ�Τ��ɬ�����
                $r = 0 if ($island->{'pop'} < $HguardPop);      # $HguardPop �ʲ���ɬ�����
                # ��פ���
                if ($r < $warp_par) { # 60%

                    my ($tIsland) = $island;                    # ��ư�����

                    $r = random(100);
                    # 50%�γ�Ψ��¾����ˤ���
                    if (($r < 50) && ($special != 16)) {
                        my ($tar);
                        my ($ch_flag) = 0;
                        for ($tar = 0; $tar < $HislandNumber; $i++) {
                            $tIsland = $Hislands[random($HislandNumber)];
                            next if($tIsland->{'predelete'});
                            next if(($special == 20) && ($tIsland->{'BF_Flag'}));
                            next if(($special == 20) && ($Island->{'id'} == $tIsland->{'id'}));
                            $ch_flag = 1;
                            last;
                        }
                        $tIsland = $island if(!$ch_flag);
                    }

                    my ($tId)   = $tIsland->{'id'};

                    # ������������
                    my ($i, $bx, $by);
                    my ($tLand)      = $tIsland->{'land'};
                    my ($tLandValue) = $tIsland->{'landValue'};
                    my ($tLandValue2) = $tIsland->{'landValue2'};
                    my ($tLandValue3) = $tIsland->{'landValue3'};
                    my ($warped) = 0;

                    foreach $i (0..$pointNumber) {
                        $bx = $Hrpx[$i];
                        $by = $Hrpy[$i];

                        if ($special == 16) {           # ��פ��� �ۤ�����ʤ� ���磲��
                            if (MonsterWarpLanding($tIsland, $tLand->[$bx][$by], $tLandValue->[$bx][$by] ,$bx ,$by) ){
                                $warped = 1;
                                last;
                            }
                        } elsif ($special == 20) {      # ���סܤ��
                            if (MonsterWarpLandingForQueen($tIsland, $tLand->[$bx][$by],$tLandValue->[$bx][$by] ,$bx ,$by) ){
                                $warped = 1;
                                last;
                            }
                        } else {
                            if (MonsterWarpLanding($tIsland, $tLand->[$bx][$by],$tLandValue->[$bx][$by] ,$bx ,$by) ){
                                $warped = 1;
                                last;
                            }
                        }
                    }
                    next if($warped == 0);

                    my ($tName) = islandName($tIsland);

                    # ��ס�
                    logMonsWarp($id, $name, $this_pos, $mName);
                    $island->{'monsterlive'} -= 1;
                    logMonsCome($tId, $tName, $mName, "($bx, $by)", landName($tLand->[$bx][$by], $tLandValue->[$bx][$by], $tLandValue2->[$bx][$by]));
                    $tIsland->{'monsterlive'} += 1;

                    # �Ԥ������
                    my ($tland_before) = $tLand->[$bx][$by];
                    my ($tlv_before) = $tLandValue->[$bx][$by];
                    my ($tlv2_before) = $tLandValue2->[$bx][$by];
                    my ($tlv3_before) = $tLandValue3->[$bx][$by];

                    # ���ԡ�
                    $tLand->[$bx][$by]      = $land->[$x][$y];
                    $tLandValue->[$bx][$by] = $landValue->[$x][$y];
                    $tLandValue2->[$bx][$by] = $landValue2->[$x][$y];
                    $tLandValue3->[$bx][$by] = $landValue3->[$x][$y];

                    if ($special == 20) {
                        $land->[$x][$y]      = $HlandBigFood;
                        $landValue->[$x][$y] = (3 << $Food_Kind_Shift) + 3;
                        $landValue2->[$x][$y] = 0;
                        $landValue3->[$x][$y] = 0;
                    }
                    elsif ($mKind == $Mons_EnderInora) {
                        $land->[$x][$y]      = $tland_before;
                        $landValue->[$x][$y] = $tlv_before;
                        $landValue2->[$x][$y] = $tlv2_before;
                        $landValue3->[$x][$y] = $tlv3_before;
                    }
                    else {
                        $land->[$x][$y]      = $HlandWaste;
                        $landValue->[$x][$y] = 0;
                        $landValue2->[$x][$y] = 0;
                        $landValue3->[$x][$y] = 0;
                    }

                    # ���Ϥ��Ϸ��򴬤�����
                    if (($special == 15) && (random(100) < 50)) { # 50%

                        my ($sx, $sy, $tx, $ty, $sKind, $sLv, $tKind, $tLv, $tLv2);
                        for ($i = 1; $i < 7; $i++) {
                            $sx = $x + $ax[$i];
                            $sy = $y + $ay[$i];
                            $tx = $bx + $ax[$i];
                            $ty = $by + $ay[$i];

                            $sx-- if(!($sy % 2) && ($y % 2));
                            $tx-- if(!($ty % 2) && ($by % 2));

                            if (($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)) {
                                $sKind = $HlandSea;
                                $sLv   = 0;
                            } else {
                                $sKind = $land->[$sx][$sy];
                                $sLv   = $landValue->[$sx][$sy];
                            }
                            if (($tx < 0) || ($tx > $islandSize) || ($ty < 0) || ($ty > $islandSize)) {
                                $tKind = $HlandSea;
                                $tLv   = 0;
                                $tLv2  = 0;
                            } else {
                                $tKind = $tLand->[$tx][$ty];
                                $tLv   = $tLandValue->[$tx][$ty];
                                $tLv2  = $tLandValue2->[$tx][$ty];
                            }

                            if (($sx >= 0) && ($sx < $HislandSize) && ($sy >= 0) && ($sy < $HislandSize)) {
                                # �ϰ���ξ��
                                $land->[$sx][$sy]      = $tKind;
                                $landValue->[$sx][$sy] = $tLv;
                                logMonsWarpLand($id, $name, landName($tKind, $tLv, $tLv2), "($sx, $sy)");
                            }
                            if (($tx >= 0) && ($tx < $HislandSize) && ($ty >= 0) && ($ty < $HislandSize)) {
                                # �ϰ���ξ��
                                $tLand->[$tx][$ty]      = $sKind;
                                $tLandValue->[$tx][$ty] = $sLv;
                                logMonsWarpLand($tId, $tName, landName($sKind, $sLv, $tLv2), "($tx, $ty)");
                            }
                        }
                    }
                    next;
                }
                else {

                    # ��פ��ʤ�
                }
            }

            if ($special == 12) {
                # �λ�ˤʤ����ȯ���ƹ����ﳲ��ȯ�����������
                if ($mHp <= 1) { # �Ĥ����ϣ��ʤ�
                    # �λ�ˤʤä��Τ���ȯ����
                    logMonsExplosion($id, $name, $this_pos, $mName);
                    $island->{'monsterlive'} -= 1;
                    wideDamage($id, $name, $land, $landValue, $x, $y);
                    next;
                }
            }

            if ($special == 13) {
                # ��֤�Ƥֲ���
                if (random(100) < 50) { # 50%

                    # ��������
                    my ($nLv, $nKind,$lv2);
                    ($nKind,$lv2) = MonsterSpawnKind($island , 0);

                    # ���ýи�
                    logMonsHelpMe($id, $name, $mName, $this_pos);

                    # lv���ͤ����
                    $nLv = ($nKind << $Mons_Kind_Shift) + $HmonsterBHP[$nKind] + random($HmonsterDHP[$nKind]);

                    # �ɤ��˸���뤫����
                    my ($bx, $by, $i);
                    my ($check);
                    my ($tar_land);
                    foreach $i (0..$pointNumber) {
                        $bx = $Hrpx[$i];
                        $by = $Hrpy[$i];
                        $check = 0;
                        if (isSeaMonster($nKind)) {
                            if ($land->[$bx][$by] == $HlandSea) {
                                $check = 1;
                            }
                        }
                        else {
                            if (   ($land->[$bx][$by] == $HlandTown)
                                || ($land->[$bx][$by] == $HlandWaste)
                                || ($land->[$bx][$by] == $HlandPlains) ){
                                $check = 1;
                            }
                        }

                        if ($check) {
                            # �Ϸ�̾
                            my ($lName) = landName($land->[$bx][$by], $landValue->[$bx][$by],$landValue2->[$bx][$by]);

                            # ���Υإå�������ä�
                            $land->[$bx][$by] = $HlandMonster;      #��ư
                            $landValue->[$bx][$by] = $nLv;
                            $landValue2->[$bx][$by] = 0;
                            $landValue3->[$bx][$by] = 0;

                            # ���þ���
                            my ($nName) = (monsterSpec($nLv))[1];

                            # ��å�����
                            logMonsCome($id, $name, $nName, "($bx, $by)", $lName);
                            $island->{'monsterlive'} += 1;
                            last;
                        }
                    }
                }
            }

            if ($mKind == $Mons_Mikael) { # ŷ�ȥߥ�����
                # ����
                Mikael_Luck($island , $this_pos , $landKind , $lName);
            }

            # ��ȥ�
            if ($special == 19) {
                my ($par) = 20;
                if (random(100) < $par) {
                    RetroBeam($island , $mName);
                }
            }

            # �Ų���?
            if (isMonsterCuring($mKind)) {
                # �Ų���
                next;

            } elsif(   ($mKind == $Mons_Queen_inora) 
                    && (   ($HislandTurn % 2) == 0)
                        && ($mHp < 4)
                        && (random(100) < 70) ) { # ��å������󤤤Τ�
                logMonsBomb($id, $name, $lName, $this_pos, $mName);
                # �����ﳲ�롼����
                wideDamage($id, $name, $land, $landValue, $x, $y);
                if (random(1000) < 250) {
                    $land->[$x][$y] = $HlandMonument;
                    $landValue->[$x][$y] = 78;
                }

            } elsif($mKind == $Mons_f20) { # ��¤����f02
                my ($tx, $ty, $tL, $tLv, $tLv2);
                # ȯ��
                $tx = random($HislandSize);
                $ty = random($HislandSize);
                $tL = $land->[$tx][$ty];
                $tLv = $landValue->[$tx][$ty];
                $tLv2 = $landValue2->[$tx][$ty];

                if (random(1000) < 600) {

                    if (   ($tL == $HlandSea)
                        || ($tL == $HlandMountain)
                        || ($tL == $HlandGold)
                        || ($tL == $HlandShrine)
                        || ($tL == $HlandSeacity)
                        || ($tL == $HlandOnsen)
                        || ($tL == $HlandIce)
                        || ($tL == $HlandUmishuto)
                        || ($tL == $HlandSeatown)
                        || ($tL == $HlandUmiamu)
                        || ($tL == $HlandSbase)
                                                ) {
                        logMekaAttack($id, $name, $mName, $this_pos, landName($tL, $tLv,$tLv2), "($tx, $ty)", "�ߥ�����");
                        next;
                    }

                    logMekaAttack($id, $name, $mName, $this_pos, landName($tL, $tLv,$tLv2), "($tx, $ty)", "�ߥ�����", "���Ӥ����Ǥ�");

                    if (   ($tL == $HlandOil)
                        || ($tL == $HlandFune)
                        || ($tL == $HlandNursery)
                        || ($tL == $HlandFrocity)
                        || ($tL == $HlandUmicity)
                        || ($tL == $HlandOilCity)
                                                    ) {
                        # ���ˤʤ��Ϸ�
                        $land->[$tx][$ty] = $HlandSea;
                        $landValue->[$tx][$ty] = 0;
                        $landValue2->[$tx][$ty] = 0;
                        $landValue3->[$tx][$ty] = 0;

                    }
                    else {

                        $land->[$tx][$ty] = $HlandWaste;
                        $landValue->[$tx][$ty] = 1;
                        $landValue2->[$tx][$ty] = 0;
                        $landValue3->[$tx][$ty] = 0;
                    }

                }
                elsif (random(1000) < 400) {

                    logMekaAttack($id, $name, $mName, $this_pos, landName($tL, $tLv,$tLv2), "($tx, $ty)", "${HtagDisaster_}¿��Ƭ�ߥ�����${H_tagDisaster}");
                    my ($ssx, $ssy, $i, $ssL, $ssLv, $ssLv2);
                    for ($i = 0; $i < 7; $i++) {
                        $ssx = $tx + $ax[$i];
                        $ssy = $ty + $ay[$i];

                        # �Ԥˤ�����Ĵ��
                        $ssx-- if(!($ssy % 2) && ($ty % 2));

                        # �ϰϳ�Ƚ��
                        next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));

                        $ssL = $land->[$ssx][$ssy];
                        $ssLv = $landValue->[$ssx][$ssy];
                        $ssLv2 = $landValue2->[$ssx][$ssy];

                        # �ϰϤˤ��ʬ��
                        if ($i < 1) {
                            # �濴
                            if (   ($ssL == $HlandSea)
                                || ($ssL == $HlandSeacity)
                                || ($ssL == $HlandSeatown)
                                || ($ssL == $HlandUmishuto)
                                || ($ssL == $HlandUmiamu)
                                || ($ssL == $HlandSbase)
                                                            ) {
                                next;
                            }
                            logDamageAny($id, $name, landName($ssL, $ssLv,$ssLv2), "($ssx, $ssy)", "�᤭���ӿ��פ��ޤ�����");
                            SetSeaShallowLand($island,  $ssx , $ssy);
                        }
                        else {
                            # 1�إå���
                            if (NoDamage_by_Bomb1HEX($sL) ) {
                                # ���᡼���Τʤ��Ϸ�
                                next;
                            }
                            elsif ($sL == $HlandMonster) {
                                my ($tKind, $tName, $tHp) = monsterSpec($ssLv);
                                logDamageAny($id, $name, landName($ssL, $ssLv,$ssLv2), "($ssx, $ssy)", "�ä����Ӥޤ�����");
                                MonsterDead($island , $ssx , $ssy , $tKind , 0);
                            }
                            else {
                                logDamageAny($id, $name, landName($ssL, $ssLv,$ssLv2), "($ssx, $ssy)", "��֤ˤ���<B>����</B>�Ȳ����ޤ�����");
                                SetWasteLand_Normal($island,  $ssx , $ssy);
                            }
                        }
                    }

                } elsif(random(1000) < 200) {
                    my($sx, $sy, $sL, $sLv, $sLv2);
                    # �
                    $sx = random($HislandSize);
                    $sy = random($HislandSize);
                    $sL = $land->[$sx][$sy];
                    $sLv = $landValue->[$sx][$sy];
                    $sLv2 = $landValue2->[$sx][$sy];
                    # ��å�����
                    logMekaAttack($id, $name, $mName, $this_pos, landName($sL, $sLv, $sLv2), "($sx, $sy)", "${HtagDisaster_}���ȥߥå����ܥ�${H_tagDisaster}", "����ȯ��");
                    # �����ﳲ�롼����
                    wideDamage($id, $name, $land, $landValue, $sx, $sy);
                }

            } elsif($mKind == $Mons_Uriel) { # ŷ�ȥ��ꥨ��

                my ($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};
                if ($monsno > 0) {
                    my($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for ($i = 0; $i < $monsno; $i++){
                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster) {
                            # ����̤β��ä������硢���β��ä򹶷⤹��

                            # �оݤȤʤ���äγ����Ǽ��Ф�
                            my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                            my ($tlv) = $landValue->[$sx][$sy];

                            if (isMonsterCuring($tKind)) {
                                # �оݤ��Ų���ʤ���̤ʤ�
                                next;
                            }
                            if (random(1000) < 600) {
                                if (   ($tKind == 28)
                                    || ($tKind == 30)) {

                                    logItiAttackms($id, $name, $mName, $this_pos, $tName, "($sx, $sy)");
                                    my ($dmge) = random(4);
                                    $tHp -= $dmge;
                                    $tlv -= $dmge;
                                    $landValue->[$sx][$sy] = $tlv;

                                    if ($tHp < 1){
                                        # �оݤβ��ä��ݤ�ƹ��Ϥˤʤ�
                                        MonsterDead($island , $sx , $sy , $tKind , 0);
                                        # �󾩶�
                                        AddMonsterReward($island , $tKind);
                                    }
                                } elsif ($tKind != $Mons_Uriel) { # ŷ�ȥ��ꥨ��
                                    logItiAttack($id, $name, $mName, $this_pos, $tName, "($sx, $sy)");

                                    # �оݤβ��ä��ݤ�ƹ��Ϥˤʤ�
                                    MonsterDead($island , $sx , $sy , $tKind , 0);
                                    # �󾩶�
                                    AddMonsterReward($island , $tKind);
                                }
                            }
                        }
                    }

                    if (random(1000) < 600) {
                        my ($tx, $ty, $tL, $tLv,$tLv2);
                        # ȯ��
                        $tx = random($HislandSize);
                        $ty = random($HislandSize);
                        $tL = $land->[$tx][$ty];
                        $tLv = $landValue->[$tx][$ty];
                        $tLv2 = $landValue2->[$tx][$ty];

                        if (   ($tL == $HlandSea)
                            || ($tL == $HlandMountain)
                            || ($tL == $HlandShrine)
                            || ($tL == $HlandGold)
                                                    ) {
                            next;
                        }
                        SetSeaShallowLand($island, $tx , $ty);
                        logUrieruMeteo($id, $name, $mName, $this_pos, landName($tL, $tLv,$tLv2), "($tx, $ty)");
                        if (random(1000) < 100) {
                            $land->[$tx][$ty] = $HlandMonument;
                            $landValue->[$tx][$ty] = 79;
                            $landValue2->[$tx][$ty] = 0;
                        }
                    }
                }

            } elsif ($mKind == $Mons_Ice_scorpion) { # �������������ԥ���
                my ($i, $sx, $sy);
                foreach $i (0..$pointNumber) {
                    $sx = $Hrpx[$i];
                    $sy = $Hrpy[$i];
                    if ($land->[$sx][$sy] == $HlandMonster) {
                        # ����̤β��ä������硢���β��ä򹶷⤹��

                        # �оݤȤʤ���äγ����Ǽ��Ф�
                        my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                        my ($tlv) = $landValue->[$sx][$sy];
                        # my($tSpecial) = $HmonsterSpecial[$tKind];

                        if (isMonsterCuring($tKind)) {
                            # �оݤ��Ų���ʤ���̤ʤ�
                            next;
                        }
                        if (random(1000) < 600) {
                            if (($tKind == $Mons_Mascot_inora) || ($tKind == $Mons_SuperTetra)) {
                                logIceAttack($id, $name, $mName, $this_pos, $tName, "($sx, $sy)");
                                my ($dmge) = random(4);
                                $tHp -= $dmge;
                                $tlv -= $dmge;
                                $landValue->[$sx][$sy] = $tlv;

                                if ($tHp < 1){
                                    # �оݤβ��ä��ݤ��ɹ�Ϥˤʤ�
                                    $land->[$sx][$sy] = $HlandIce;
                                    $landValue->[$sx][$sy] = 0;
                                    $landValue2->[$sx][$sy] = 0;
                                    $landValue3->[$sx][$sy] = 0;
                                    $island->{'monsterlive'} -= 1;
                                    # �󾩶�
                                    AddMonsterReward($island,$tKind);
                                }
                            }
                            elsif($tKind != $Mons_Ice_scorpion) {
                                logIceAttack($id, $name, $mName, $this_pos, $tName, "($sx, $sy)");

                                # �оݤβ��ä��ݤ��ɹ�Ϥˤʤ�
                                $land->[$sx][$sy] = $HlandIce;
                                $landValue->[$sx][$sy] = 0;
                                $island->{'monsterlive'} -= 1;

                                if (random(1000) < 100) {
                                    $land->[$sx][$sy] = $HlandMonument;
                                    $landValue->[$sx][$sy] = 76;
                                }
                                # �󾩶�
                                AddMonsterReward($island,$tKind);
                            }
                        }

                    } elsif(($land->[$sx][$sy] == $HlandBase) ||
                        ($land->[$sx][$sy] == $HlandDefence) ||
                        ($land->[$sx][$sy] == $HlandOil) ||
                        ($land->[$sx][$sy] == $HlandFune)) {
                        # ��ˤ���ߥ�������ϡ��ɱһ��ߡ����ġ�������ɹ����ɹ�Фˤ���

                        if (random(1000) < 200) {
                            my $tKind = $land->[$sx][$sy];
                            my $tlv = $landValue->[$sx][$sy];
                            my $tlv2 = $landValue2->[$sx][$sy];
                            logIceAttack($id, $name, $mName, $this_pos, landName($tKind, $tlv,$tlv2), "($sx, $sy)");
                            $land->[$sx][$sy] = $HlandIce;
                            $landValue->[$sx][$sy] = 0;
                            if (random(1000) < 100) {
                                $land->[$sx][$sy] = $HlandMonument;
                                $landValue->[$sx][$sy] = 76;
                            }
                        }
                    }
                }

            } elsif ($mKind == $Mons_Alfr) { # ��ѻե������

                if (random(1000) < 300) {
                    logMgSpel($id, $name, $mName, "($x, $y)", "�ؼ���ƥ�");
                    $HdisMeteo[$Hmonth] = 500;
                    my ($sx, $sy, $sL, $sLv, $sLv2, $first, $sName);
                    $first = 1;
                    while (!random(2) || $first) {
                        $first = 0;
                        # �
                        $sx = random($HislandSize);
                        $sy = random($HislandSize);
                        $sL = $land->[$sx][$sy];
                        $sLv = $landValue->[$sx][$sy];
                        $sLv2 = $landValue2->[$sx][$sy];
                        $sName = landName($sL, $sLv,$sLv2);

                        next if($sL == $HlandHugeMonster);

                        if ( ($sL == $HlandSea) && ($sLv == 0)){
                            # ���ݥ���
                            logMeteo($id, $name, $sName, "($sx, $sy)", "��");
                        }
                        elsif (($sL == $HlandMountain) || ($sL == $HlandGold) || ($sL == $HlandShrine) || ($sL == $HlandOnsen)){
                            # ���˲�
                            logMeteo($id, $name, $sName, "($sx, $sy)", "��<B>$sName</B>�Ͼä�����");
                            SetWasteLand_Normal($island,$sx,$sy);
                            next;
                        }
                        elsif (   ($sL == $HlandSbase)
                               || ($sL == $HlandSeacity)
                               || ($sL == $HlandSeatown)
                               || ($sL == $HlandUmishuto)
                               || ($sL == $HlandFrocity)
                               || ($sL == $HlandFune)
                               || ($sL == $HlandUmiamu)) {

                            logMeteo($id, $name, $sName, "($sx, $sy)", "��<B>$sName</B>��������");
                        }
                        elsif ($sL == $HlandMonster) {
                            $island->{'monsterlive'} -= 1;
                            logMeteoMonster($id, $name, $sName, "($sx, $sy)");
                        }
                        elsif (($sL == $HlandSea) || ($sL == $HlandIce)) {
                            # ����
                            logMeteo($id, $name, $sName, "($sx, $sy)", "�����줬�������");
                        }
                        else {
                            logMeteo($id, $name, $sName, "($sx, $sy)", "�����Ӥ����פ�");
                        }
                        SetSeaLand_Normal($island,$sx,$sy);
                    }
                }

                if (random(1000) < 200) {
                    logMgSpel($id, $name, $mName, "($x, $y)", "�ؼ���ƥ�");
                    $HdisMeteo[$Hmonth] = 300;
                    my ($sx, $sy);
                    # �
                    $sx = random($HislandSize);
                    $sy = random($HislandSize);
                    # ��å�����
                    logHugeMeteo($id, $name, "($sx, $sy)");
                    # �����ﳲ�롼����
                    wideDamage($id, $name, $land, $landValue, $sx, $sy);
                }

                if (random(1000) < 400) {
                    logMgSpel($id, $name, $mName, "($x, $y)", "��������");
                    $HdisEarthquake[0] = 500;
                    # �Ͽ�ȯ��
                    logEarthquake($id, $name);
                    my ($sx, $sy, $sL, $sLv, $sLv2, $i);
                    foreach $i (0..$pointNumber) {
                        $sx = $Hrpx[$i];
                        $sy = $Hrpy[$i];
                        $sL = $land->[$sx][$sy];
                        $sLv = $landValue->[$sx][$sy];
                        $sLv2 = $landValue2->[$sx][$sy];

                        if ((($sL == $HlandTown) && ($sLv >= 100)) ||
                            (($sL == $HlandFoodim) && ($sLv < 480)) ||
                            (($sL == $HlandProcity) && ($sLv < 130)) ||
                            (($sL == $HlandNewtown) && ($sLv < 300)) ||
                            (($sL == $HlandBigtown) && ($sLv < 300)) ||
                            (($sL == $HlandHTFactory) && ($sLv < 500)) ||
                            (($sL == $HlandSHTF) && ($sLv < 500)) ||
                            ($sL == $HlandRizort) ||
                            ($sL == $HlandBigRizort) ||
                            ($sL == $HlandHaribote) ||
                            ($sL == $HlandTrain) ||
                            ($sL == $HlandPark) ||
                            ($sL == $HlandMinato) ||
                            ($sL == $HlandKyujo) ||
                            ($sL == $HlandKyujokai) ||
                            ($sL == $HlandKatorikun) ||
                            ($sL == $HlandOnsen) ||
                            ($sL == $HlandFactory)) {
                            # 1/4�ǲ���
                            if (!random(4)) {
                                logDamageAny($id, $name, landName($sL, $sLv, $sLv2), "($sx, $sy)", "${HtagDisaster_}�Ͽ�${H_tagDisaster}�ˤ����Ǥ��ޤ�����");
                                if ($sL == $HlandOnsen) {
                                    # �����ϻ������
                                    SetMountain_Normal($island,$sx,$sy);
                                }
                                else {
                                    SetWasteLand_Normal($island,$sx,$sy);
                                }
                            }
                        }
                    }
                }

                my ($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};
                if ($monsno > 0) { # �ɥ쥤��
                    my ($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for ($i = 0; $i < $monsno; $i++) {
                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster){
                            my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                            my ($tlv) = $landValue->[$sx][$sy];
                            # my($tSpecial) = $HmonsterSpecial[$tKind];
                            if ($tKind != 19) {
                                if ($tHp > $mHp) {
                                    next if (isMonsterCuring($tKind));

                                    logMgDrain($id, $name, $mName, $tName, "($x, $y)");
                                    $tlv -= ($tHp-$mHp);
                                    $landValue->[$sx][$sy] = $tlv;
                                    $lv += ($tHp-$mHp) if($mHp < 9);
                                    $landValue->[$x][$y] = $lv;
                                }
                                next;
                            }
                        }
                    }
                    my ($nKind, $nName, $nHp) = monsterSpec($landValue->[$x][$y]);
                    $nKind = 21 if ($nKind > 21);
                    $nHp = 1 if ($nHp < 1);
                    $landValue->[$x][$y] = ($nKind << $Mons_Kind_Shift) + $nHp;
                }

            } elsif ($mKind == $Mons_Ethereal) { # ��ŷ�ȥ����ꥢ
                $lv += 2;
                $landValue->[$x][$y] = $lv;
                ($mKind, $mName, $mHp) = monsterSpec($lv);

                if (random(1000) < 200) {
                    food_product_Random_consumption($island , int($island->{'food'} / 2));
                    logFushoku($id, $name, $mName, "($x, $y)");
                }
                if ($mHp > 13) {
                    logUmlimit($id, $name, $mName, "($x, $y)");
                    # �����ﳲ�롼����
                    wideDamage($id, $name, $land, $landValue, $x, $y);
                    my ($sx, $sy, $sL, $sLv, $sLv2, $i);
                    foreach $i (0..$pointNumber) {
                        $sx = $Hrpx[$i];
                        $sy = $Hrpy[$i];
                        $sL = $land->[$sx][$sy];
                        $sLv = $landValue->[$sx][$sy];
                        $sLv2 = $landValue2->[$sx][$sy];

                        if (   (($sL == $HlandTown) && ($sLv >= 100))
                            || (($sL == $HlandFoodim) && ($sLv < 480))
                            || (($sL == $HlandProcity) && ($sLv < 130))
                            || ($sL == $HlandHaribote)
                            || ($sL == $HlandTrain)
                            || ($sL == $HlandPark)
                            || ($sL == $HlandMinato)
                            || ($sL == $HlandKyujo)
                            || ($sL == $HlandKyujokai)
                            || ($sL == $HlandBase)
                            || ($sL == $HlandFactory) ) {
                            # 1/6�ǲ���
                            if (!random(6)) {

                                logUmlimitDamage($id, $name, $mName, landName($sL, $sLv, $sLv2), "($sx, $sy)");
                                $land->[$sx][$sy] = $HlandWaste;
                                $landValue->[$sx][$sy] = 0;
                                $landValue2->[$sx][$sy] = 0;
                                $landValue3->[$sx][$sy] = 0;
                                if (random(1000) < 150) {
                                    $land->[$sx][$sy] = $HlandMonument;
                                    $landValue->[$sx][$sy] = 74;
                                    $landValue2->[$sx][$sy] = 0;
                                    $landValue3->[$sx][$sy] = 0;
                                }
                            }
                        }
                    }
                    # �Ⲧ��������ѿ�
                    $mKind = 21;
                    $lv = ($mKind << $Mons_Kind_Shift) + $HmonsterBHP[$mKind] + random($HmonsterDHP[$mKind]);
                    $land->[$x][$y] = $HlandMonster;
                    $landValue->[$x][$y] = $lv;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                }

            } elsif ($mKind == $Mons_Satan) { # �Ⲧ������
                $lv += 3 if ($mHp < 9);
                $landValue->[$x][$y] = $lv;
                if (random(1000) < 150) {
                    $island->{'money'} -= int($island->{'money'} / 2);
                    logKyoukou($id, $name, $mName, "($x, $y)");
                }
                if (random(1000) < 200) {
                    food_product_All_Clear($island);
                    logFushoku($id, $name, $mName, "($x, $y)");
                }

                my ($i,$sx,$sy,$tkind);
                foreach $i (0..$pointNumber) {
                    $sx = $Hrpx[$i];
                    $sy = $Hrpy[$i];
                    $tkind = $land->[$sx][$sy];
                    if (   ($land->[$sx][$sy] == $HlandPlains)
                        || ($land->[$sx][$sy] == $HlandForest)
                        || ($land->[$sx][$sy] == $HlandNursery)
                        || ($land->[$sx][$sy] == $HlandFarmchi)
                        || ($land->[$sx][$sy] == $HlandFarmpic)
                        || ($land->[$sx][$sy] == $HlandFarmcow)
                        || ($land->[$sx][$sy] == $HlandRottenSea)) {
                        # ��ˤ���ʿ�ϡ������ܿ��졢�ܷܾ졢���ھ졢�Ҿ졢�峤����Ϥ����Ф����Фˤ���
                        my ($tlv) = $landValue->[$sx][$sy];
                        my ($tlv2) = $landValue2->[$sx][$sy];
                        my ($tlv3) = $landValue3->[$sx][$sy];

                        if (random(1000) < 200) {
                            logHellAttack($id, $name, $mName, "($x, $y)", landName($tkind, $tlv, $tlv2), "($sx, $sy)");
                            if ($tkind == $HlandNursery) {

                                $land->[$sx][$sy] = $HlandSea;
                                $landValue->[$sx][$sy] = 1;
                                $landValue2->[$sx][$sy] = 0;
                            }
                            else {

                                SetWasteLand_Normal($island , $sx , $sy);
                            }
                            if (random(1000) < 100) {

                                $land->[$sx][$sy] = $HlandMonument;
                                $landValue->[$sx][$sy] = 78;
                            }
                            elsif (random(1000) < 100) {

                                $land->[$sx][$sy] = $HlandMonument;
                                $landValue->[$sx][$sy] = 74;
                            }
                        }
                    }
                }
            }
            elsif ($mKind == $Mons_SuperTetra) { # Ķ���åƥȥ�

                if ($island->{'monsterlive'} == $island->{'c28'}) {
                    # �ƥȥ����������
                    if ($island->{'co99'} == 0) {
                        logMstakeiede($id, $name, "�з����Ķ���åƥȥ�","($x, $y)",landName($landKind, $lv,$lv2));
                    }
                    else {
                        my ($i,$sx,$sy);
                        foreach $i (0..$pointNumber) {
                            $sx = $Hrpx[$i];
                            $sy = $Hrpy[$i];
                            $landKind = $land->[$sx][$sy];
                            $lv = $landValue->[$sx][$sy];
                            $lv2 = $landValue2->[$sx][$sy];
                            $landName = landName($landKind, $lv,$lv2,$landValue3->[$sx][$sy]);

                            if (   ($land->[$sx][$sy] == $HlandCollege)
                                && ($lv == 99) ) {

                                $landValue->[$sx][$sy] = 98;
                                $island->{'monsterlive'} -= 1;
                                logMstakeokaeri($id, $name, "�з����Ķ���åƥȥ�","($sx, $sy)",$landName);
                                last;
                            }
                        }
                    }
                    SetWasteLand_Normal($island , $x , $y);
                }

                my ($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};
                if ($monsno > 0) {

                    my ($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for ($i = 0; $i < $monsno; $i++) {

                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster) {

                            if ($msseigen < 1) {
                                # ����̤β��ä������硢���β��ä򹶷⤹��

                                # �оݤȤʤ���äγ����Ǽ��Ф�
                                my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                                my ($tlv) = $landValue->[$sx][$sy];
                                # my ($tSpecial) = $HmonsterSpecial[$tKind];

                                if (   ($tKind == $Mons_SuperTetra)
                                    || ($tKind == $Mons_hime_inora) ) {

                                }
                                else {
                                    my ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
                                    my ($m_str) = $HmonsterSTR[$tKind];

                                    $mHp = $mshp;

                                    my ($attackdamege , $counterdamege) = PetAttackCalc($island , 1);

                                    logMsAttackt($id, $name, "Ķ���åƥȥ�", $attackdamege, $counterdamege, $tName, $tPoint);
                                    $msseigen++;
                                    $tHp -= $attackdamege;
                                    $tlv -= $attackdamege;
                                    $landValue->[$sx][$sy] = $tlv;
                                    $mHp -= $counterdamege;
                                    $lv = Calc_MonsterLandValue_HP($mKind , $mHp);
                                    $landValue->[$x][$y] = $lv;

                                    if ($tHp < 1) {
                                        # �оݤβ��ä��ݤ�ƹ��Ϥˤʤ�
                                        MonsterDead( $island , $sx , $sy , $tKind , 0 );
                                        if ($tKind == $Mons_Mikael) {
                                            SetMonument_Normal($island , $sx , $sy , 93);
                                            logMsAttackmika($id, $name, "Ķ���åƥȥ�", $attackdamege, $counterdamege, $tName);
                                        }
                                        # �󾩶�
                                        AddMonsterReward($island , $tKind);
                                        my ($value) = $HmonsterValue[$tKind];

                                        if (random(1000) < $value) {
                                            if (random(100) < 30) {
                                                $msap++;
                                            } elsif (random(100) < 30) {
                                                $msdp++;
                                            } elsif (random(100) < 30) {
                                                $mssp++;
                                            } else {
                                                $mshp++;
                                                $mshp = 15 if($mshp > 15);
                                            }
                                        }

                                        $msexe += $HmonsterExp[$tKind];
                                        $mswin ++;
                                        $island->{'eisei5'} = "$mshp,$msap,$msdp,$mssp,$mswin,$msexe,$tet";

                                        # �����༣��
                                        TaijiPrize($island , $tKind);
                                    }

                                    if ($mHp < 1){
                                        # Ķ���åƥȥ餬�ݤ�ƹ��Ϥˤʤ�
                                        MonsterDead( $island , $x , $y , $mKind , 0 );
                                        # �󾩶�
                                        AddMonsterReward($island , $mKind);
                                    }
                                }
                            }
                            else {
                                last;
                            }
                        }
                    }
                }

            } elsif ($mKind == $Mons_Tetra) { #���åƥȥ�

                if ($island->{'monsterlive'} == 1){
                    # ���ƥȥ����������
                    if ($island->{'co99'} == 0){

                    }
                    else {

                        my($i,$sx,$sy);
                        # ������ؤ�õ��
                        foreach $i (0..$pointNumber) {
                            $sx = $Hrpx[$i];
                            $sy = $Hrpy[$i];
                            $landKind = $land->[$sx][$sy];
                            $lv = $landValue->[$sx][$sy];
                            if (   ($landKind == $HlandCollege)
                                && ($lv == 99) ) {

                                $landValue->[$sx][$sy] = 98;

                                # ��Ȥ���������Ϥ�
                                $landName = landName($landKind, $lv,$landValue2->[$sx][$sy],$landValue3->[$sx][$sy]);
                                SetWasteLand_Normal($island , $x , $y);
                                logMstakeokaeri($id, $name, "�ƥȥ�","($sx, $sy)",$landName);
                                last;
                            }
                        }
                    }
                }

            } elsif ($mKind == $Mons_Mascot_inora) {

                if ($island->{'monsterlive'} == $island->{'c28'}) {
                    # �ޥ����åȤ��Τ����������
                    if ($island->{'co99'} == 0){
                        logMstakeiede($id, $name, '�з���Υޥ����åȤ��Τ�',"($x, $y)",landName($landKind, $lv,$lv2));
                    } else {
                        my($i,$sx,$sy);
                        foreach $i (0..$pointNumber) {
                            $sx = $Hrpx[$i];
                            $sy = $Hrpy[$i];
                            $landKind = $land->[$sx][$sy];
                            $lv = $landValue->[$sx][$sy];
                            $lv2 = $landValue2->[$sx][$sy];
                            $landName = landName($landKind, $lv,$lv2,$landValue3->[$sx][$sy]);

                            if (   ($land->[$sx][$sy] == $HlandCollege)
                                && ($lv == 99) ){
                                $landValue->[$sx][$sy] = 4;
                                $island->{'monsterlive'} -= 1;
                                logMstakeokaeri($id, $name, '�з���Υޥ����åȤ��Τ�',"($sx, $sy)",$landName );
                                last;
                            }
                        }
                    }
                    SetWasteLand_Normal($island,$x,$y);     # $HlandWaste
                }

                my ($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};

                if ($monsno > 0) {
                    my ($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for ($i = 0; $i < $monsno; $i++) {

                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster){
                            if ($msseigen < 1) {
                                # ����̤β��ä������硢���β��ä򹶷⤹��

                                # �оݤȤʤ���äγ����Ǽ��Ф�
                                my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                                my ($tlv) = $landValue->[$sx][$sy];
                                my ($tSpecial) = $HmonsterSpecial[$tKind];

                                if (   ($tKind == $Mons_Mascot_inora)
                                    || ($tKind == $Mons_hime_inora) ) {

                                }
                                else {
                                    my ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
                                    my ($m_str) = $HmonsterSTR[$tKind];

                                    $mHp = $mshp;

                                    my ($attackdamege , $counterdamege) = PetAttackCalc($island , 1);

                                    logMsAttackt($id, $name, '�ޥ����åȤ��Τ�', $attackdamege, $counterdamege, $tName, $tPoint);
                                    $msseigen++;
                                    $tHp -= $attackdamege;
                                    $tlv -= $attackdamege;
                                    $landValue->[$sx][$sy] = $tlv;
                                    $mHp -= $counterdamege;
                                    $lv = Calc_MonsterLandValue_HP($mKind , $mHp);
                                    $landValue->[$x][$y] = $lv;

                                    if ($tHp < 1) {
                                        # �оݤβ��ä��ݤ�ƹ��Ϥˤʤ�
                                        MonsterDead( $island , $sx , $sy , $tKind , 0 );
                                        # �󾩶�
                                        my ($value) = $HmonsterValue[$tKind];
                                        $island->{'money'} += $value;

                                        if (random(1000) < $value) {
                                            if (random(100) < 30) {
                                                $msap++;
                                            } elsif (random(100) < 30) {
                                                $msdp++;
                                            } elsif (random(100) < 30) {
                                                $mssp++;
                                            } else {
                                                $mshp++;
                                                $mshp = 15 if($mshp > 15);
                                            }
                                        }

                                        $msexe += $HmonsterExp[$tKind];
                                        $mswin ++;
                                        $island->{'eisei5'} = "$mshp,$msap,$msdp,$mssp,$mswin,$msexe,$tet";
                                        # �����༣��
                                        TaijiPrize($island , $tKind);
                                        logMsMonMoney($id, $tName, $value);
                                    }
                                    if ($mHp < 1) {
                                        # �ޥ����åȤ��Τ餬�ݤ�ƹ��Ϥˤʤ�
                                        MonsterDead( $island , $x , $y , $mKind , 0 );
                                        # �󾩶�
                                        AddMonsterReward($island , $mKind);
                                    }
                                }
                            }
                            else {
                                last;
                            }
                        }
                    }
                }
            }

            if (   ($special == 6)
                || ($mKind == $Mons_Mikael) ) { # ŷ�ȥߥ�����

                my($i, $sx, $sy, $monsno);
                $monsno = $island->{'monsterlive'};
                if($monsno > 0) {
                    my($monsArray, $monspnt);
                    $monsArray = $island->{'monspnt'};
                    for ($i = 0; $i < $monsno; $i++){
                        $monspnt = $monsArray->[$i];
                        ($sx, $sy) = ($monspnt->{x}, $monspnt->{y});
                        if ($land->[$sx][$sy] == $HlandMonster){
                            # ����̤β��ä������硢���β��ä򹶷⤹��

                            # �оݤȤʤ���äγ����Ǽ��Ф�
                            my ($sLv) = $landValue->[$sx][$sy];
                            my ($sKind, $sName, $sHp) = monsterSpec($sLv);
                            my ($sSpecial) = $HmonsterSpecial[$sKind];

                            if ($mHp > $sHp){ # �оݤ�����Ϥ�¿���ä����
                                if (isMonsterCuring($sKind)) {
                                    # �оݤ��Ų���ʤ���̤ʤ�
                                    next;
                                }
                                last if ($kougekiseigenm > 1);

                                if ($mKind == 13) { # ŷ�ȥߥ�����
                                    logMonsAttackt($id, $name, $mName, "($x, $y)", $sName, "($sx, $sy)");
                                }
                                else {
                                    logMonsAttack($id, $name, $mName, "($x, $y)", $sName, "($sx, $sy)");
                                }

                                $kougekiseigenm++;
                                # �оݤβ��ä����Ϥ�å�äƼ�ʬ�����Ϥ����
                                $sHp--;
                                if ($sHp > 0){
                                    # �оݤ����Ϥ򸺤餹
                                    $sLv--;
                                    $landValue->[$sx][$sy] = $sLv;
                                }
                                else {
                                    # �оݤβ��ä��ݤ�ƹ��Ϥˤʤ�
                                    MonsterDead($island , $sx , $sy , $sKind , 0 );
                                    # �󾩶�
                                    my($value) = $HmonsterValue[$sKind];
                                    $island->{'money'} += $value;
                                    logMsMonMoney($id, $sName, $value);
                                }
                                $lv++ if($mHp < 9);
                                $landValue->[$x][$y] = $lv;
                            }
                            # �оݤ�����Ϥ��㤫�ä���硢���⤷�ʤ�
                        }
                    }
                    my ($nKind, $nName, $nHp) = monsterSpec($landValue->[$x][$y]);
                    $nKind = 30 if ($nKind > 30);
                    $nHp = 1 if ($nHp < 1);
                    $landValue->[$x][$y] = ($nKind << $Mons_Kind_Shift) + $nHp;
                }
            }

            if (   ($mKind == $Mons_Totten)
                || ($mKind == $Mons_Wario) ) {    # �ȥåƥ�
                if ( (!random(2) ) ) {
                    my ($stole);
                    $stole = 500 +  random(99999);
                    $stole = 5000 + random(999999) if ( ($mKind == $Mons_Wario) ) ;

                    if ( $island->{'money'} > $stole ) {
                        logMonsMoneyStole($id, $name, $stole , $mName);
                        $island->{'money'} -= $stole;
                    }
                    else {
                        if ($mKind == $Mons_Wario) {

                            $stole = int ($stole / 2) ;
                            if ( $island->{'money'} > $stole ) {
                                logMonsMoneyStole($id, $name, $stole , $mName);
                                $island->{'money'} -= $stole;
                            }
                        }
                    }

                }
                else {
                    logMonsMoneyStoleMiss($id, $name, $mName);
                }
            }

            if ($mKind == $Mons_Wario) {
                if ( (!random(2) ) ) {
                    my ($stole);
                    $stole = 5000 + random(500000);

                    if ( $island->{'food'} > $stole ) {
                        logMonsFoodStole($id, $name, $stole , $mName);
                        food_product_Random_consumption($island , $stole);
                    }else{
                        if ($mKind == $Mons_Wario) {

                            $stole = int ($stole / 2) ;
                            if ( $island->{'food'} > $stole ) {
                                logMonsFoodStole($id, $name, $stole , $mName);
                                food_product_Random_consumption($island , $stole);
                            }else{
                                $stole = int($island->{'food'} / 10) ;

                                if ( $island->{'food'} > $stole ) {
                                    logMonsFoodStole($id, $name, $stole , $mName);
                                    food_product_Random_consumption($island , $stole);
                                }
                            }
                        }
                    }
                }else{
                    logMonsFoodStoleMiss($id, $name, $mName);
                }
            }

            if ($mKind == $Mons_Kisinhei) {
                if ($mHp < 5) {
                    if ($landValue3->[$x][$y] >= 100) {

                        my ($kaihuku) = int($landValue3->[$x][$y] / 100);
                        if (($mHp + $kaihuku) > 10) {

                            $kaihuku = 10 - $mHp;
                        }
                        $landValue3->[$x][$y] -= ($kaihuku * 100);
                        $landValue->[$x][$y] += $kaihuku;
                        logKishinhei_Kaihuku($island , "($x,$y)");
                    }
                }
            }

            # ----------------------------------------- #
            # ��ư�Ǥ��ʤ��Ƥ�Ǥ����ư
            # �����ޤ�
            # ----------------------------------------- #

            # ư�����������
            my ($d, $sx, $sy);
            my ($i);

            for ($i = 0; $i < 3; $i++) {

                $d = random(6) + 1;
                $sx = $x + $ax[$d];
                $sy = $y + $ay[$d];
                # �Ԥˤ�����Ĵ��
                $sx-- if(!($sy % 2) && ($y % 2));
                # �ϰϳ�Ƚ��
                next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

                my $l = $land->[$sx][$sy];
                my ($lva) = $landValue->[$sx][$sy];
                my $def = 0;

                $def = countAround($land, $sx, $sy, 19, $HlandDefence ) if ($island->{'BF_Flag'} == 1);

                if (isSeaMonster($mKind)) {
                    if (   ($l == $HlandSea)
                        || ( ($l == $HlandMine) && ($lva & $Hmine_SEA_FLAG))
                        || ( ($l == $HlandIce) && ($mKind == $Mons_Unbaba) )
                        || ( ($l == $HlandNursery) && ($mKind == $Mons_Unbaba) )
                        || ( ($l == $HlandFrocity) && ($mKind == $Mons_Unbaba) )
                        || ( ($l == $HlandMinato) && ($mKind == $Mons_Unbaba) )
                        || ( ($l == $HlandOil) && ($mKind == $Mons_Unbaba) )
                        || ( ($l == $HlandFune) && ($mKind == $Mons_Unbaba) )
                        || ( ($l == $HlandUmiamu) && ($mKind == $Mons_Unbaba) )
                            ){
                        #ư����
                        last;
                    }
                    else {
                        #�������ʤ�
                    }

                }else{
                    # �������𡢳����Իԡ����ġ����á�������ǰ��ʳ�
                    if (   (   (   ($l != $HlandSea)
                                && ($l != $HlandSbase)
                                && ($l != $HlandSeacity)
                                && ($l != $HlandSeatown)
                                && ($l != $HlandUmicity)
                                && ($l != $HlandOilCity)
                                && ($l != $HlandNursery)
                                && ($l != $HlandOil)
                                && ($l != $HlandBigtown)
                                && ($l != $HlandBettown)
                                && ($l != $HlandShuto)
                                && ($l != $HlandCollege)
                                && ($l != $HlandUmishuto)
                                && ($l != $HlandFrocity)
                                && ($l != $HlandBigRizort)
                                && ($l != $HlandOnsen)
                                && ($l != $HlandHouse)
                                && ($l != $HlandFune)
                                && ($l != $HlandUmiamu)
                                && ($l != $HlandGold)
                                && ($l != $HlandShrine)
                                && ($l != $HlandMountain)
                                && ($l != $HlandMonument)
                                && ($l != $HlandYougan)
                                && ($l != $HlandEgg)
                                && ($l != $HlandZoo)
                                && ($l != $HlandRottenSea)
                                && ($l != $HlandMonster) )
                            || (   ($l == $HlandMine)           # ����
                                && !($lva & $Hmine_SEA_FLAG) )  # ������ʤ�
                            || (   ($l == $HlandYougan)         # �ϴ��
                                && ($mKind == 33) )             # �ϴ���ä�OK
                        && ($def == 0 )
                                       ) ) {
                        last;
                    }
                }
            }
            # ư���ʤ��ä�
            next if ($i == 3);

            if (   ($mKind == 28)
                || ($mKind == 30) ) {
                if ($land->[$sx][$sy] != $HlandWaste) {
                    next;
                }
            }

            # ư��������Ϸ��ˤ���å�����
            my ($sL) = $land->[$sx][$sy];
            my ($sLv) = $landValue->[$sx][$sy];
            my ($sLv2) = $landValue2->[$sx][$sy];
            my ($sName) = landName($sL, $sLv, $sLv2);
            my ($point) = "($sx, $sy)";

            my($mi, $mx, $my);

            for($mi = 0; $mi < $island->{'monsterlive'}; $mi++){
                ($mx, $my) = ($island->{'monspnt'}->[$mi]->{x}, $island->{'monspnt'}->[$mi]->{y});
                if(($mx == $x) && ($my == $y)) {
                    $island->{'monspnt'}->[$mi] = { x => $sx, y => $sy };
                    last;
                }
            }

            # ��ư���ν���
            if ($mKind == $Mons_Kisinhei) {
                my ($atk_kind);
                $atk_kind = $land->[$sx][$sy];

                foreach my $ta (@Htowns) {
                    if ($atk_kind == $ta) {
                        logKishinhei_kyusyu($island , $point ,$landValue->[$sx][$sy]);
                        $landValue3->[$x][$y] += $landValue->[$sx][$sy];
                        last;
                    }
                }
            }
            
            $land->[$sx][$sy] = $land->[$x][$y];
            $landValue->[$sx][$sy] = $landValue->[$x][$y];
            $landValue2->[$sx][$sy] = $landValue2->[$x][$y];
            $landValue3->[$sx][$sy] = $landValue3->[$x][$y];
            #��ư�����Ϸ�������
            MonsterDown( $island , $x , $y , $mKind , 0 );

            # ---------------------------------- #
            # ���äǤ��ü����                   #
            # elseif��� special������ʤ����ȡ� #
            # ---------------------------------- #
            if ($mKind == 11) { # ��å��饤��ʤ�(���Τ��ή��)

                if (   (   (random(1000) < 900)                 # ����% �γ�Ψ��ʬ������
                        && ($island->{'monsterlive'} < 7) )
                    || (   (random(20000) < 400-$island->{'monsterlive'})
                        && ($island->{'monsterlive'} > 7))      # ����% �γ�Ψ��ʬ������
                                                                ) {
                    lognewMonsterBorn($id, $name, "($x, $y)");
                    $lv =  Calc_MonsterLandValue($mKind);
                    $land->[$x][$y] = $HlandMonster;
                    $landValue->[$x][$y] = $lv;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                    $island->{'monspnt'}->[$island->{'monsterlive'}] = { x => $x, y => $y };
                    $island->{'monsterlive'}++;
                }

            } elsif (   ($mKind == 15)       # ��å쥤����,��ѻե�������ʤ�(���Τ��ή��)
                     || ($mKind == $Mons_Alfr)) {

                if ((random(1000) < 600) && ($island->{'monsterlive'} < 7)) { # ����% �γ�Ψ�Ǿ�������(����������)
                    my ($nKind) = random($HmonsterLevel3) + 1;
                    SetMonsterLand_Normal($island , $x , $y , $nKind);

                    my($nName) = $HmonsterName[$nKind];
                    if($mKind == 15) { # ��å쥤����
                        lognewKaiju($id, $name, $nName, "($x, $y)");
                    }else{
                        logShoukan($id, $name, $mName, $nName, "($x, $y)");
                    }
                }

            }elsif (   ($mKind == 8)
                    && ($island->{'BF_Flag'} == 0) ) { # ������ʤ顡���������ɲ�

                my ($RottenSeaBorn_Per) = 400;      #�峤ȯ��Ψ
                my ($Shedding_Per) = 200;           #æ��ȯ��Ψ

                if(random(1000) < $RottenSeaBorn_Per) { # 40% �γ�Ψ���峤�����ޤ��
                    logRottenSeaBorn($id, $name, "($x, $y)");
                    SetRottenSea($island , $x , $y);

                } elsif(random(1000) < $Shedding_Per) { # æ��
                    logNuginugi($id, $name, "($x, $y)");
                    SetMonument_Normal($island , $x , $y , 87);
                    SetMonsterLand_Normal($island , $sx , $sy , $Mons_Omu);
                }

            }elsif ($mKind == 33) {        # �ϴ����

                if (   ($mHp < 3)
                    && (random(100) < 50 ) ){
                    FiveHexFlame($island , $sx , $sy);

                }elsif (random(100) < 30) {
                    my ($tx, $ty);
                    $tx = random($HislandSize);
                    $ty = random($HislandSize);
                    logMgSpel($id, $name, $mName, "($x, $y)", "������");
                    Volcano($island,$tx,$ty);

                }elsif((random(100) < 50 )){
                    ThreeWayFlame($island , $sx , $sy);

                }elsif (random(100) < 50) {
                    my($i, $tx, $ty);
                    foreach $i (0..$pointNumber) {
                        $tx = $Hrpx[$i];
                        $ty = $Hrpy[$i];
                        my ($tkind) = $land->[$tx][$ty];
                        if($tkind == $HlandMonster) {
                            # ����̤β��ä������硢���β��ä򹶷⤹��

                            # �оݤȤʤ���äγ����Ǽ��Ф�
                            my ($tKind, $tName, $tHp) = monsterSpec($landValue->[$tx][$ty]);
                            my ($tlv) = $landValue->[$tx][$ty];
                            # my($tSpecial) = $HmonsterSpecial[$tKind];

                            if(isMonsterCuring($tKind)) {
                                # �оݤ��Ų���ʤ���̤ʤ�
                                next;
                            }
                            if (random(1000) < 600) {
                                if (   ($tKind == 28)
                                    || ($tKind == 30) ) {
                                    logFireAttack($id, $name, $mName, "($x, $y)", $tName, "($tx, $ty)");
                                    $dmge = random(4);
                                    $tHp -= $dmge;
                                    $tlv -= $dmge;
                                    $landValue->[$tx][$ty] = $tlv;

                                    if($tHp < 1){
                                        # �оݤβ��ä��ݤ��ɹ�Ϥˤʤ�
                                        $land->[$tx][$ty] = $HlandYougan;
                                        $landValue->[$tx][$ty] = 2+random(9);
                                        $island->{'monsterlive'} -= 1;
                                        # �󾩶�
                                        my($value) = $HmonsterValue[$tKind];
                                        $island->{'money'} += $value;
                                        logMsMonMoney($id, $tName, $value);
                                    }

                                } elsif($tKind != 33) {
                                    logFireAttack($id, $name, $mName, "($x, $y)", $tName, "($tx, $ty)");

                                    # �оݤβ��ä��ݤ��ɹ�Ϥˤʤ�
                                    SetYoganLand($island, $tx , $ty);
                                    $island->{'monsterlive'} -= 1;

                                    if (random(1000) < 100) {
                                        SetMonument_Normal($island, $tx , $ty , 78);
                                    }
                                    # �󾩶�
                                    my($value) = $HmonsterValue[$tKind];
                                    $island->{'money'} += $value;
                                    logMsMonMoney($id, $tName, $value);
                                }
                            }

                        } elsif (   ($tkind == $HlandBase)
                                 || ($tkind == $HlandDefence)
                                 || ($tkind == $HlandHaribote)
                                 || ($tkind == $HlandOil)
                                 || ($tkind == $HlandFune)
                                                            ) {
                            # ��ˤ���ߥ�������ϡ��ɱһ��ߡ����ġ�������ɹ����ɹ�Фˤ���
                            if (random(1000) < 200) {
                                my $tKind = $land->[$tx][$ty];
                                my $tlv = $landValue->[$tx][$ty];
                                my $tlv2 = $landValue2->[$tx][$ty];
                                logFireAttack($id, $name, $mName, "($x, $y)", landName($tKind, $tlv, $tlv2), "($tx, $ty)");
                                SetYoganLand($island, $tx , $ty);

                                if (random(1000) < 100) {
                                    SetMonument_Normal($island, $tx , $ty , 78);
                                }
                            }
                        }
                    }
                }

            }elsif ($mKind == $Mons_Pirates) {        # ��±

                my ($flag);
                $flag = 0;

                my ($i, $ssx, $ssy, $ssL, $ssLv, $ssLv2);

                for ($i = 1; $i < 19; $i++) {
                    $ssx = $sx + $ax[$i];
                    $ssy = $sy + $ay[$i];

                    # �Ԥˤ�����Ĵ��
                    $ssx-- if(!($ssy % 2) && ($sy % 2));
                    # �ϰϳ�
                    next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));

                    $ssL = $land->[$ssx][$ssy];
                    $ssLv = $landValue->[$ssx][$ssy];
                    $ssLv2 = $landValue2->[$ssx][$ssy];

                    if ($i < 7) {

                        if (   ($ssL == $HlandTown)
                            || ($ssL == $HlandProcity)
                            || ($ssL == $HlandMinato)
                            || ($ssL == $HlandFrocity)
                            || ($ssL == $HlandNewtown)
                            || ($ssL == $HlandBigtown)
                            || ($ssL == $HlandBettown)
                            || ($ssL == $HlandUmicity)
                            || ($ssL == $HlandOilCity)
                            || ($ssL == $HlandInaka)
                            || ($ssL == $HlandOnsen)
                            || ($ssL == $HlandRizort)
                            || ($ssL == $HlandBigRizort)
                            || ($ssL == $HlandShuto)
                            || ($ssL == $HlandFactory)
                                                        ) {
                            if (random(100) < 77) {

                                my ($tarland) = landName($ssL, $ssLv, $ssLv2);
                                my ($tpoint) = "($ssx,$ssy)";
                                my ($tname) = islandName($island);
                                my ($bag) = random((1000-20)) + 20;

                                if ($island->{'money'} < $bag) {
                                    $bag = $island->{'money'};
                                }

                                if ($bag) {
                                    my($haken);
                                    my($haken_island);
                                    $haken = $island->{'landValue2'}->[$sx][$sy];
                                    #logOut("debug ��±�������Ȥä���", $id);
                                    logOut("${HtagName_}${tname}$tpoint${H_tagName}��<B>$tarland</B>�ϡ���±�����齱������${HtagMoney_}$bag$HunitMoney${H_tagMoney}���äƤ�����ޤ�����",$id);

                                    if ($haken != 0) {
                                        logSecret("${HtagName_}${tname}$tpoint${H_tagName}�γ�±��Ư��${HtagMoney_}$bag$HunitMoney${H_tagMoney}��",$haken);
                                        $haken_island = $Hislands[$HidToNumber{$haken}];
                                        $haken_island->{'money'} += $bag;
                                    }
                                    $monsterMove[$sx][$sy] = 2;
                                }
                                last;
                            }
                        }

                    }else{
                        if (   ($ssL == $HlandTown)
                            || ($ssL == $HlandProcity)
                            || ($ssL == $HlandMinato)
                            || ($ssL == $HlandFrocity)
                            || ($ssL == $HlandNewtown)
                            || ($ssL == $HlandBigtown)
                            || ($ssL == $HlandBettown)
                            || ($ssL == $HlandUmicity)
                            || ($ssL == $HlandOilCity)
                            || ($ssL == $HlandInaka)
                            || ($ssL == $HlandOnsen)
                            || ($ssL == $HlandRizort)
                            || ($ssL == $HlandBigRizort)
                            || ($ssL == $HlandShuto)
                            || ($ssL == $HlandFactory)
                            || ($ssL == $HlandFarmchi)
                            || ($ssL == $HlandFarmpic)
                            || ($ssL == $HlandFarmcow)
                            || ($ssL == $HlandPark)
                            || ($ssL == $HlandNursery)
                            || ($ssL == $HlandFoodim)
                            || ($ssL == $HlandGold)
                            || ($ssL == $HlandInoraLand)
                            || ($ssL == $HlandBeachPark)
                                                        ) {
                            if (random(100) < 20) {

                                my ($tarland) = landName($ssL, $ssLv,$ssLv2);
                                my ($tpoint) = "($ssx,$ssy)";
                                my ($tname) = islandName($island);

                                logOut("${HtagName_}${tname}$tpoint${H_tagName}��<B>$tarland</B>�ϡ���±���������ˤ�ν��������ޤ�����",$id);

                                $ssLv = ($ssLv / 4);
                                $landValue->[$ssx][$ssy] = $ssLv;

                                if ($ssLv <= 0) {
                                    $land->[$ssx][$ssy] = $HlandWaste;
                                    $landValue->[$ssx][$ssy] = 0;
                                    $landValue2->[$ssx][$ssy] = 0;
                                    if (   ($ssL == $HlandOnsen)
                                        || ($ssL == $HlandOnsen) ) {
                                        $land->[$ssx][$ssy] = $HlandMountain;
                                    }elsif ($ssL == $HlandNursery) {
                                        $land->[$ssx][$ssy] = $HlandSea;
                                        $landValue->[$ssx][$ssy] = 1;
                                    }
                                }
                                $monsterMove[$sx][$sy] = 2;
                                last;
                            }
                        }

                        if (   ($ssL == $HlandForest)
                            || ($ssL == $HlandOil)
                            || ($ssL == $HlandHaribote)
                            || ($ssL == $HlandFune)
                            || ($ssL == $HlandKyujo)
                            || ($ssL == $HlandSeki)
                            || ($ssL == $HlandCollege)
                            || ($ssL == $HlandKyujokai)
                            || ($ssL == $HlandKatorikun)
                            || ($ssL == $HlandFiredept)
                            || ($ssL == $HlandRocket)
                            || ($ssL == $HlandTrain)
                            || ($ssL == $HlandStation)
                                                        ) {
                            if (random(100) < 5) {
                                my ($tarland) = landName($ssL, $ssLv,$ssLv2);
                                my ($tpoint) = "($ssx,$ssy)";
                                my ($tname) = islandName($island);

                                logOut("${HtagName_}${tname}$tpoint${H_tagName}��<B>$tarland</B>�ϡ���±���������ˤ�ν��������ޤ�����",$id);

                                $land->[$ssx][$ssy] = $HlandWaste;
                                $landValue->[$ssx][$ssy] = 0;
                                $landValue2->[$ssx][$ssy] = 0;
                                if (   ($ssL == $HlandOil)
                                    || ($ssL == $HlandFune) ) {
                                    $land->[$ssx][$ssy] = $HlandSea;
                                }
                                $monsterMove[$sx][$sy] = 2;
                                last;
                            }
                        }
                    }

                }

                if (random(100) < 5) {
                    my ($tpoint) = "($sx,$sy)";
                    my ($tname) = islandName($island);
                    SetSeaLand_Normal($island, $sx , $sy);
                    logOut("${HtagName_}${tname}$tpoint${H_tagName}��<b>��±��</b>�ϡ��ɤ����ص�äƤ椭�ޤ�����",$id);
                }
            }
            # ���ø�����ü���̤����ޤ�

            # ���ä����Ϥ�Ƥ��Ԥ���ǽ�ϡ��׷���
            if(   ($special == 7) 
               || ($special == 11)
               || ($mKind == 16)    # ��å������󤤤Τ�(����1�ȣ��)
               || ($mKind == 13)
               || ($mKind == 18) ) { # ŷ�ȥߥ�����,ŷ�ȥ��ꥨ��(����2�ȣ��)
                my $r = 7;
                $r = 19 if(($mKind == 13) || ($mKind == 18));
                my($i, $ssx, $ssy, $ssL, $ssLv,$ssLv2);
                for($i = 1; $i < $r; $i++) {
                    $ssx = $sx + $ax[$i];
                    $ssy = $sy + $ay[$i];

                    # �Ԥˤ�����Ĵ��
                    $ssx-- if(!($ssy % 2) && ($sy % 2));
                    # �ϰϳ�
                    next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));

                    $ssL = $land->[$ssx][$ssy];
                    $ssLv = $landValue->[$ssx][$ssy];
                    $ssLv2 = $landValue2->[$ssx][$ssy];

                    if (($ssL == $HlandSea) ||
                        ($ssL == $HlandSeacity) ||
                        ($ssL == $HlandSeatown) ||
                        ($ssL == $HlandUmishuto) ||
                        ($ssL == $HlandIce) ||
                        ($ssL == $HlandWaste) ||
                        ($ssL == $HlandUmiamu) ||
                        ($ssL == $HlandSbase)) {
                        # ���ȳ�����ϤϾƤ���ʤ�
                        next;
                    } elsif(($ssL == $HlandOil) ||
                             ($ssL == $HlandFrocity) ||
                             ($ssL == $HlandUmicity) ||
                             ($ssL == $HlandOilCity) ||
                             ($ssL == $HlandFune)) {
                        # ���ġ����ϳ������
                        $land->[$ssx][$ssy] = $HlandSea; # ���ˤʤ�
                        $landValue->[$ssx][$ssy] = 0;
                    } elsif($ssL == $HlandNursery) {
                        # �ܿ���ϳ������
                        $land->[$ssx][$ssy] = $HlandSea; # ���ˤʤ�
                        $landValue->[$ssx][$ssy] = 1;
                    } elsif(($ssL == $HlandGold) ||
                             ($ssL == $HlandShrine) ||
                             ($ssL == $HlandOnsen) ||
                             (($ssL == $HlandMountain) && ($ssLv > 0))) {
                        # �⻳���η��졦���ο��¤ϻ������
                        SetMountain_Normal($island,$ssx,$ssy);  # ���ˤʤ�

                    } elsif ($ssL == $HlandMonster) {
                        # ���ä�
                        # �оݤȤʤ���äγ����Ǽ��Ф�
                        my($tKind, $tName, $tHp) = monsterSpec($ssLv);
                        my($tlv) = $landValue->[$ssx][$ssy];
                        # my($tspecial) = $HmonsterSpecial[$tKind];
                        if (($tKind == 28) || ($tKind == 30)) {
                            my ($dmge) = random(4);
                            $tHp -= $dmge;
                            $tlv -= $dmge;
                            $landValue->[$ssx][$ssy] = $tlv;

                            if($tHp < 1){
                                # �оݤβ��ä��ݤ�ƹ��Ϥˤʤ�
                                MonsterDown($island , $ssx , $ssy , $tKind , 0);
                                # �󾩶�
                                my($value) = $HmonsterValue[$tKind];
                                $island->{'money'} += $value;
                                logMsMonMoney($id, $tName, $value);
                            }
                        }
                    } else {
                        # ���Ƥ��Ƥ��Ԥ������
                        SetWasteLand_Normal($island , $ssx , $ssy);
                    }

                    # �����������
                    if($special == 11) {
                        logMonsFireS($id, $name, landName($ssL, $ssLv,$ssLv2), "($ssx, $ssy)", $mName);
                    } else {
                        logMonsFire($id, $name, landName($ssL, $ssLv,$ssLv2), "($ssx, $ssy)", $mName);
                    }
                }
            }

            # �ե꡼�����ȡ���
            if (   ($special == 9)
                || ($mKind == $Mons_Ice_scorpion)) {
                my ($i, $ssx, $ssy, $kind, $lv);
                for ($i = 1; $i < 7; $i++) {
                    $ssx = $sx + $ax[$i];
                    $ssy = $sy + $ay[$i];

                    # �Ԥˤ�����Ĵ��
                    if((($ssy % 2) == 0) && (($sy % 2) == 1)) {
                        $ssx--;
                    }

                    if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize)) {
                        # �ϰϳ�
                        next;
                    }

                    $kind = $land->[$ssx][$ssy];
                    $lv   = $landValue->[$ssx][$ssy];

                    if (   (isBehindSea($kind))
                        || ($kind == $HlandIce)
                        || ($kind == $HlandUmiamu)
                                                    ) {
                        # ���ȳ�����ϤϾƤ���ʤ�
                        next;

                    } elsif(   ($kind == $HlandOil)
                            || ($kind == $HlandFune)
                            || ($kind == $HlandFrocity)
                            || ($kind == $HlandUmicity)
                            || ($kind == $HlandOilCity)
                            || ($kind == $HlandNursery)) {
                        # ���ġ����������Իԡ��ܿ���
                        $land->[$ssx][$ssy] = $HlandIce; # ɹ�Ϥˤʤ�
                        $landValue->[$ssx][$ssy] = 0;
                    } elsif ($kind == $HlandMonster) {
                        # ���ä�
                        # �оݤȤʤ���äγ����Ǽ��Ф�
                        my($tKind, $tName, $tHp) = monsterSpec($landValue->[$ssx][$ssy]);
                        my($tlv) = $landValue->[$ssx][$ssy];
                        my($tspecial) = $HmonsterSpecial[$tKind];
                        if(   ($tKind == 28)
                           || ($tKind == 30) ) {
                            my ($dmge) = random(4);
                            $tHp -= $dmge;
                            $tlv -= $dmge;
                            $landValue->[$ssx][$ssy] = $tlv;
                            if($tHp < 1){
                                # �оݤβ��ä��ݤ��ɹ�Ϥˤʤ�
                                $land->[$ssx][$ssy] = $HlandIce;
                                $landValue->[$ssx][$ssy] = 0;
                                # �󾩶�
                                my($value) = $HmonsterValue[$tKind];
                                $island->{'money'} += $value;
                                logMsMonMoney($id, $tName, $value);
                            }
                        }
                    } else {
                        # ���Ƥ�����դ�
                        $land->[$ssx][$ssy] = $HlandIce; # ɹ�Ϥˤʤ�
                        $landValue->[$ssx][$ssy] = 0;
                    }

                    # �����������
                    logMonsCold($id, $name, landName($kind, $lv,$landValue2->[$ssx][$ssy]), "($ssx, $ssy)", $mName);
                }
            }

            if (   ($mKind == 14)
                && ($island->{'monsterlive'} < 7) ) { # ���饤��쥸����ɤ�ʬ��

                my($i, $ssx, $ssy, $ssL, $ssLv);

                for($i = 1; $i < 7; $i++) {

                    $ssx = $sx + $ax[$i];
                    $ssy = $sy + $ay[$i];

                    # �Ԥˤ�����Ĵ��
                    $ssx-- if(!($ssy % 2) && ($sy % 2));
                    # �ϰϳ�
                    next if(($ssx < 0) || ($ssx > $islandSize) || ($ssy < 0) || ($ssy > $islandSize));

                    $ssL = $land->[$ssx][$ssy];
                    $ssLv = $landValue->[$ssx][$ssy];

                    unless (   ($ssL == $HlandSea)
                            || ($ssL == $HlandSeacity)
                            || ($ssL == $HlandIce)
                            || ($ssL == $HlandUmishuto)
                            || ($ssL == $HlandSeatown)
                            || ($ssL == $HlandOil)
                            || ($ssL == $HlandFune)
                            || ($ssL == $HlandNursery)
                            || ($ssL == $HlandUmiamu)
                            || ($ssL == $HlandMountain) 
                            || ($ssL == $HlandGold)
                            || ($ssL == $HlandShrine)
                            || ($ssL == $HlandOnsen)
                            || ($ssL == $HlandMonster)
                            || ($ssL == $HlandMonument)
                            || ($ssL == $HlandZoo)
                            || ($ssL == $HlandSbase) ) {
                        # ���Ϥȳ�����ϡ����Ϥˤ�ʬ�����ʤ�
                        # ʬ��
                        my $nKind = $Mons_Slime;
                        $lv = Calc_MonsterLandValue($nKind);
                        $land->[$ssx][$ssy] = $HlandMonster;
                        $landValue->[$ssx][$ssy] = $lv;
                        $landValue2->[$x][$y] = 0;
                        $landValue2->[$ssx][$ssx] = 0;
                        $island->{'monspnt'}->[$island->{'monsterlive'}] = { x => $ssx, y => $ssy };
                        $island->{'monsterlive'}++;
                    }

                    if (random(1000) < 50) {
                        $land->[$ssx][$ssy] = $HlandMonument;
                        $landValue->[$ssx][$ssy] = 77;
                        $landValue2->[$x][$y] = 0;
                    }

                    # �����������
                    lognewMonsterBorn($id, $name, "($ssx, $ssy)");
                }
            }

            # ��ư�Ѥߥե饰
            if (   ($HmonsterSpecial[$mKind] == 2)
                || ($mKind == $Mons_Kisinhei)
                || ($mKind == $Mons_Pirates) ) {
                # ��ư�Ѥߥե饰��Ω�Ƥʤ�

            } elsif (   ($HmonsterSpecial[$mKind] == 1)
                     || ($HmonsterSpecial[$mKind] == 16)
                                                    ) {
                # ®������
                $monsterMove[$sx][$sy] = $monsterMove[$x][$y] + 1;

            } else {
                # ���̤β���
                $monsterMove[$sx][$sy] = 2;
            }

            if (($sL == $HlandDefence) && $HdBaseAuto) {
                # �ɱһ��ߤ�Ƨ���
                logMonsMoveDefence($id, $name, $sName, $point, $mName);
                # �����ﳲ�롼����
                wideDamage($id, $name, $land, $landValue, $sx, $sy);

            } elsif($sL == $HlandMine) {
                # �����Ƨ���
                my($da) = $sLv & $Hmine_DAMAGE_MASK;
                if($mHp < $da) {
                    # ��˴���ƻ��Τ����ӻ��ä�
                    logMonsMine($id, $name, $sName, $point, $mName, "�ä����Ӥޤ�����");
                } elsif($mHp == $da) {
                    # ��˴���ƻ��Τ��Ĥä�
                    logMonsMine($id, $name, $sName, $point, $mName, "�ϿԤ����ݤ�ޤ�����");

                    # ����
                    my($value) = $HmonsterValue[$mKind];
                    if($value > 0) {
                        $island->{'money'} += $value;
                        logMsMonMoney($id, $mName, $value);
                    }

                    # �����༣��
                    TaijiPrize($island , $mKind);

                } else {
                    # �����Ĥä�
                    logMonsMine($id, $name, $sName, $point, $mName, "�줷��������Ӭ���ޤ�����");
                    $landValue->[$sx][$sy] -= $da;
                    next;
                }

                # ���äϹ��Ϥ�
                MonsterDown( $island , $sx , $sy , $mKind , 1 );

            } else {
                # ��ư��
                if ( $mKind == $Mons_Unbaba){
                    logMonsMove($id, $name, $sName, $point, $mName , "�˰��߹��ޤ�Ƥ��ޤ��ޤ�����") if (($sL != $HlandSea)&&($sLv != 0));

                } elsif($mKind == 32) {

                } else {
                    if (   ( ($sL != $HlandWaste) && ($sL != $HlandPlains) )
                        && (!$island->{'BF_Flag'}) ) {
                        logMonsMove($id, $name, $sName, $point, $mName , "��Ƨ�߹Ӥ餵��ޤ�����");
                    }
                }
            }

        }

        # �к�Ƚ��
        my $fflag = 0;
        my $fdept = 0;

        if ($island->{'weather'} != $HWeather_Rain) {

            if((($landKind == $HlandTown) && ($lv > 30)) ||
                ($landKind == $HlandHaribote) ||
                ($landKind == $HlandMinato) ||
                ($landKind == $HlandFoodim) ||
                ($landKind == $HlandOnsen) ||
                ($landKind == $HlandKatorikun) ||
                ($landKind == $HlandCollege) ||
                ($landKind == $HlandHTFactory) ||
                ($landKind == $HlandSHTF) ||
                ($landKind == $HlandFiredept) ||
                ($landKind == $HlandFactory)) {
                $fflag = 1;

            } elsif(($landKind == $HlandNewtown) ||
                ($landKind == $HlandRizort) ||
                ($landKind == $HlandBigRizort) ||
                ($landKind == $HlandBettown) ||
                ($landKind == $HlandBigtown)) {
                $fflag = 2;
            }

            if(    ( $island->{'firedept'} )
                && (random(100) < $HFiredept_save )
                && (   (($landKind == $HlandTown) && ($lv > 30))
                    || ($landKind == $HlandMinato)
                    || ($landKind == $HlandFoodim)
                    || ($landKind == $HlandHTFactory)
                    || ($landKind == $HlandSHTF)
                    || ($landKind == $HlandFactory)
                    || ($landKind == $HlandNewtown)
                    || ($landKind == $HlandRizort)
                    || ($landKind == $HlandBigRizort)
                    || ($landKind == $HlandBettown)
                    || ($landKind == $HlandBigtown) )
                ){

                $fflag = 3;
            }
        }

        $fdept = $HFiredept_guard if ( $island->{'firedept'} );

        if($fflag) {
            my $rfflag = ($fflag == 1) ? random(1000) : random(750);
            my $ffflag = 1 if(!$HnoDisFlag && $rfflag < $HdisFire[0] - $fdept - int($island->{'eis1'}/20));

            if($ffflag) {
                # ���Ϥο��ȵ�ǰ��������
                my $fw = countAround($land, $x, $y, 7, $HlandForest, $HlandProcity, $HlandHouse, $HlandMonument);
                $fw += countAround($land, $x, $y, 19, $HlandFiredept);
                $fw = 0 if($landKind == $HlandFiredept);
                unless($fw) {
                    # ̵���ä���硢�кҤǲ���
                    my($l) = $land->[$x][$y];
                    my($lv) = $landValue->[$x][$y];
                    my($point) = "($x, $y)";

                    if($fflag == 2) {
                        logFirenot($id, $name, $lName, $point);
                        $landValue->[$x][$y] -= random(100) + 50;
                    }
                    if($fflag == 3) {
                        logFirenot($id, $name, $lName, $point);
                        $landValue->[$x][$y] -= random(50) + 10;
                    }
                    if($fflag == 1 || ($landValue->[$x][$y] <= 0)) {
                        logFire($id, $name, $lName, $point);
                        SetWasteLand_Normal_val($island , $x , $y , 4);

                        if ($l == $HlandOnsen) {
                            # �����ϻ������
                            SetMountain_Normal($island,$x,$y);
                        }
                    }
                }
            }
        }
    }
}


#----------------------------------------------------------------------
sub PetAttackCalc {
    my ($island , $limit) = @_;  # 1�ǽ񤭹���

    my ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
    my ($m_str) = $HmonsterSTR[$tKind];

    my ($attackdamege) = random($msap-$m_str);
    my ($counterdamege) = random($m_str-$msdp);
    if (random(5 + $m_str) > $mssp) {

        $attackdamege = 0;
    }
    elsif ($attackdamege < 1){

        $attackdamege = $limit;
    }
    if (random(5 + $m_str) < $mssp) {
        $counterdamege = 0;
    } elsif($counterdamege < 1) {
        $counterdamege = 1;
    }

    return ($attackdamege , $counterdamege);
}


#----------------------------------------------------------------------
sub AddMonsterReward {
    my ($island , $mkind) = @_;

    # �󾩶�
    my ($value) = $HmonsterValue[$mkind];

    if ($value > 0) {
        my ($tName) = $HmonsterName[$mkind];
        my ($id) = $island->{'id'};
        $island->{'money'} += $value;
        logMsMonMoney($id, $tName, $value);
    }
}



#----------------------------------------------------------------------
# Mikael_Luck
#
sub Mikael_Luck {
    my ($island , $pos , $landkind , $lName) = @_;

    my ($name) = islandName($island);
    my ($id) = $island->{'id'};

    my $value = $HoilMoney + random(500); # ��������
    $island->{'money'} += $value;

    if ($landkind == $HlandMonster) {
        logOilMoneyt($id, $name, $lName, $pos, "$value$HunitMoney", "����");

    }else{
        if (STATUE_LOG_OMIT) {
            $island->{'statue_income'} += $value;
        }else{
            logMiyage($id, $name, $lName, $pos, "$value$HunitMoney");
        }
    }

    $value = int($island->{'pop'} / 20) + random(11); # �͸�����ͤ��Ȥ�1000�ȥ�ο�������
    #$island->{'food'} += $value;
    food_product_plus($island , 'yasai' ,$value);
    if (STATUE_LOG_OMIT) {
        $island->{'statue_income_food'} += $value;
    }else{
        logParkEventt($id, $name, $lName, $pos, "$value$HunitFood") if($value);
    }
}

#----------------------------------------------------------------------
# ������
sub GetTaijiFlag {
    my($island, $mKind) = @_;

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
# ̤����
#----------------------------------------------------------------------
sub FireConflagration {
    my ($island, $x ,$y) = @_;

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};

    my ($landKind) = $land->[$x][$y];
    my ($lv) = $landValue->[$x][$y];
    my ($lv2) = $landValue2->[$x][$y];

    # �к�Ƚ��
    my $fflag = 0;
    my $fdept = 0;

    if (   (   ($landKind == $HlandTown)
            && ($lv > 30) )
        || ($landKind == $HlandHaribote)
        || ($landKind == $HlandMinato)
        || ($landKind == $HlandFoodim)
        || ($landKind == $HlandOnsen)
        || ($landKind == $HlandKatorikun)
        || ($landKind == $HlandCollege)
        || ($landKind == $HlandHTFactory)
        || ($landKind == $HlandSHTF)
        || ($landKind == $HlandFiredept)
        || ($landKind == $HlandFactory)
                                        ) {
        $fflag = 1;

    } elsif (   ($landKind == $HlandNewtown)
             || ($landKind == $HlandRizort)
             || ($landKind == $HlandBigRizort)
             || ($landKind == $HlandBettown)
             || ($landKind == $HlandBigtown)
                                            ) {
        $fflag = 2;
    }

    if(    ( $island->{'firedept'} )
        && (random(100) < $HFiredept_save )
        && (   (($landKind == $HlandTown) && ($lv > 30))
            || ($landKind == $HlandMinato)
            || ($landKind == $HlandFoodim)
            || ($landKind == $HlandHTFactory)
            || ($landKind == $HlandSHTF)
            || ($landKind == $HlandFactory)
            || ($landKind == $HlandNewtown)
            || ($landKind == $HlandRizort)
            || ($landKind == $HlandBigRizort)
            || ($landKind == $HlandBettown)
            || ($landKind == $HlandBigtown) )
        ){

        $fflag = 3;
    }

    $fdept = $HFiredept_guard if ( $island->{'firedept'} );

    if($fflag) {
        my $rfflag = ($fflag == 1) ? random(1000) : random(750);
        my $ffflag = 1 if(!$HnoDisFlag && $rfflag < $HdisFire[0] - $fdept - int($island->{'eis1'}/20));

        if($ffflag) {
            # ���Ϥο��ȵ�ǰ��������
            my $fw = countAround($land, $x, $y, 7, $HlandForest, $HlandProcity, $HlandHouse, $HlandMonument);
            $fw += countAround($land, $x, $y, 19, $HlandFiredept);
            $fw = 0 if($landKind == $HlandFiredept);
            unless($fw) {
                # ̵���ä���硢�кҤǲ���
                my($l) = $land->[$x][$y];
                my($lv) = $landValue->[$x][$y];
                my($point) = "($x, $y)";
                my($lName) = landName($l, $lv,$landValue2->[$x][$y]);

                if ($fflag == 2) {
                    logFirenot($id, $name, $lName, $point);
                    $landValue->[$x][$y] -= random(100) + 50;
                }
                if ($fflag == 3) {
                    logFirenot($id, $name, $lName, $point);
                    $landValue->[$x][$y] -= random(50) + 10;
                }
                if ($fflag == 1 || ($landValue->[$x][$y] <= 0)) {
                    logFire($id, $name, $lName, $point);
                    SetWasteLand_Normal($island , $x , $y);

                    if ($l == $HlandOnsen) {
                        # �����ϻ������
                        $land->[$x][$y] = $HlandMountain; # ���ˤʤ�
                        $landValue->[$x][$y] = 0;
                    }
                }
            }
        }
    }
}


# ---------------------------------------------------------------------
# ����1HEX���Ρ����᡼�����Ϸ�
# ---------------------------------------------------------------------
sub NoDamage_by_Flame {
    my ($LandKind) = @_;

    if (   ($LandKind == $HlandMountain)
        || ($LandKind == $HlandOnsen)
        || ($LandKind == $HlandUmishuto)
        || ($LandKind == $HlandGold)
        || ($LandKind == $HlandShrine)
        || ($LandKind == $HlandSea)
        || ($LandKind == $HlandSbase)
        || ($LandKind == $HlandSeacity)
        || ($LandKind == $HlandSeatown)
        || ($LandKind == $HlandFune)
        || ($LandKind == $HlandUmiamu)
                                        ) {
        # ���᡼���Τʤ��Ϸ�
        return 1;
    }
    return 0;
}


# ---------------------------------------------------------------------
# Ȣ���å׾�Ψ�ꥻ�å�
# ---------------------------------------------------------------------
sub HakoCup_TeamReset {
    my($island) = @_;

    if ($island->{'stadiumnum'}) {
        # HakoniwaCup
        my($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = split(/,/, $island->{'eisei4'});
        my $turn = $HislandTurn % 100;

        if($turn == 0) {            # �����
            $stwin = 0;             # ������
            $stdrow = 0;            # ����ʬ��
            $stlose = 0;            # �餱��
            $stshoka = 1;

            $island->{'eisei4'} = "$sto,$std,$stk,$stwin,$stdrow,$stlose,$stwint,$stdrowt,$stloset,$styusho,$stshoka";
        }
    }
}


# ---------------------------------------------------------------------
# ����
# ---------------------------------------------------------------------
sub SunahamaToSea {
    my($island, $x ,$y) = @_;
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($landValue2) = $island->{'landValue2'};


    my ($par) = $Sunahama_To_Sea_par;
    $par += (3 *$island->{'weather_chain'}) if ( $island->{'weather'} == $HWeather_Rain);
    $par -= (3 *$island->{'weather_chain'}) if ( $island->{'weather'} == $HWeather_Sunny);

    $par += (3) if (15 > $island->{'temperature'});
    $par -= (3) if (22 < $island->{'temperature'});

    if (random(100) < $par) {
        $land->[$x][$y] = $HlandSea;
        $landValue->[$x][$y] = 1;
        $landValue2->[$x][$y] = 0;
    }
}

# ---------------------------------------------------------------------
# �ɱ��Իԡ��ڤΤ��Ȥ꤯��
# ---------------------------------------------------------------------
sub ProCity_MonsterSmash {
    my($island, $x ,$y) = @_;
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($name) = islandName($island);
    my($id) = $island->{'id'};
    my($i, $sx, $sy);

    for($i = 1; $i < 7; $i++) {
        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];
        # �Ԥˤ�����Ĵ��
        $sx-- if(!($sy % 2) && ($y % 2));
        # �ϰϳ�
        next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));
        if($land->[$sx][$sy] == $HlandMonster){
            # ����1Hex���̤β��ä������硢���β��ä򹶷⤹��

            # �оݤȤʤ���äγ����Ǽ��Ф�
            my($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);

            logBariaAttack($id, $name, $tName, "($sx, $sy)");
            # �оݤβ��ä��ݤ�ƹ��Ϥˤʤ�
            MonsterDead($island , $sx , $sy , $tKind , 1 );
        }
    }
}


# ---------------------------------------------------------------------
# ����1HEX���Ρ����᡼�����Ϸ�
# ---------------------------------------------------------------------
sub NoDamage_by_Bomb1HEX {
    my ($LandKind) = @_;

    if (   ($LandKind == $HlandWaste)
        || ($LandKind == $HlandMountain)
        || ($LandKind == $HlandIce)
        || ($LandKind == $HlandOnsen)
        || ($LandKind == $HlandUmishuto)
        || ($LandKind == $HlandFrocity)
        || ($LandKind == $HlandGold)
        || ($LandKind == $HlandShrine)
        || ($LandKind == $HlandSea)
        || ($LandKind == $HlandSbase)
        || ($LandKind == $HlandSeacity)
        || ($LandKind == $HlandSeatown)
        || ($LandKind == $HlandOil)
        || ($LandKind == $HlandFune)
        || ($LandKind == $HlandUmiamu)
                                        ) {
        # ���᡼���Τʤ��Ϸ�
        return 1;
    }
    return 0;
}


# ---------------------------------------------------------------------
# ���å�ײ�ǽ���Ϸ�
# ---------------------------------------------------------------------
sub MonsterWarpLandingForQueen {
    my($island, $landkind, $landValue , $x , $y) = @_;

    my ($def)=0;

    if ( $island->{'BF_Flag'} == 1) {
        return 0;
    }

    if (   ($landkind == $HlandSea)         # ��
        || ($landkind == $HlandPlains)      # �ؤ���
        || ($landkind == $HlandWaste)       # �Ӥ���
                                        ) {
        return 1;
    }

    return 0;
}



# ---------------------------------------------------------------------
# ���å�ײ�ǽ���Ϸ�
# ---------------------------------------------------------------------
sub MonsterWarpLanding {
    my($island, $landkind, $landValue , $x , $y) = @_;

    my ($def)=0;

    if ( $island->{'BF_Flag'} == 1) {
        my($land) = $island->{'land'};
        $def = countAround($land, $x, $y, 19, $HlandDefence);
    }

    if ($def > 0){
        return 0;
    }

    if (   ($landkind == $HlandTown)
        || ($landkind == $HlandPlains)
        || ($landkind == $HlandWaste)
        || ($landkind == $HlandForest)
        || ($landkind == $HlandFarm)
        || ($landkind == $HlandFactory)
        || ($landkind == $HlandBase)
        || ($landkind == $HlandDefence)
        || ($landkind == $HlandHaribote)
        || ($landkind == $HlandTrain)
        || ($landkind == $HlandFoodim)
        || ($landkind == $HlandNewtown)
        || ($landkind == $HlandBigtown)
        || ($landkind == $HlandFarmchi)
        || ($landkind == $HlandFarmpic)
        || ($landkind == $HlandFarmcow)
        || ($landkind == $HlandCollege)
        || ($landkind == $HlandSunahama)
        || ($landkind == $HlandBeachPark)
        || ($landkind == $HlandRizort)
        || ($landkind == $HlandBigRizort)
        || ($landkind == $HlandHTFactory)
        || ($landkind == $HlandSHTF)
        || ($landkind == $HlandBettown)
        || ($landkind == $HlandRocket)
                                        ) {
        return 1;
    }

    return 0;
}


#----------------------------------------------------------------------
# �͸�������ä�����
# �оݤ��� , send��ޤ�뤫
#----------------------------------------------------------------------
sub MonsterSpawnKind {
    my($island , $send) = @_;

    # ���ýи�
    # ��������
    my ($kind, $pop, $temp,$chflag);
    my ($lv2);
    $lv2 = 0;
    $pop = $island->{'pop'};

    $temp = 0 ;
    $chflag = 1;

    if( ($island->{'id'} > 100) || 
        ($island->{'BF_Flag'} == 1) ) {
        $pop = $HdisMonsBorder3;
    }

    if ($send > 0 && $island->{'monstersend'} > 0) {
        # ��¤
        my ($send) = $island->{'monstersend'};
        my ($sendmo_kind , $sendmo_id);
        $chflag = 0;

        $sendmo_kind = $island->{'sendmo_kind'};
        $kind = $sendmo_kind->[$send];

        $sendmo_id = $island->{'sendmo_id'};
        $lv2 = $sendmo_id->[$send];

        $island->{'monstersend'}--;

    } elsif ($send > 0 && $island->{'event_monstersend'}) {
        $island->{'event_monstersend'} = 0;
        $kind = 35; #�Ҥ�
        $chflag = 0;

    } elsif ($pop >= $HdisMonsBorder5) {
        # level5�ޤ�
        $temp = random($HmonsterLevel5TABLE_NUM) + 1;
    } elsif ($pop >= $HdisMonsBorder4) {
        # level4�ޤ�
        $temp = random($HmonsterLevel4TABLE_NUM) + 1;
    } elsif ($pop >= $HdisMonsBorder3) {
        # level3�ޤ�
        $temp = random($HmonsterLevel3TABLE_NUM) + 1;
    } elsif ($pop >= $HdisMonsBorder2) {
        # level2�ޤ�
        $temp = random($HmonsterLevel2TABLE_NUM) + 1;
    } else {
        # level1�Τ�
        $temp = random($HmonsterLevel1TABLE_NUM) + 1;
    }
    if ($chflag) {
        $kind = $HmonsterTABLE[$temp];
    }

    if (   ( ($kind == 11) || (isSeaMonster($kind)))
        && ($island->{'BF_Flag'} == 1) ){
        $kind = 0;
    }

    return ($kind, $lv2);
}

#----------------------------------------------------------------------
# ���ù��������������
#----------------------------------------------------------------------
sub MonsterBuySpawn {

    my ($kind);
    $kind = random($HmonsterLevel3TABLE_NUM) + 1;
    $kind = $HmonsterTABLE[$kind];

    if (   (isSeaMonster($kind))    # ���β���ʪ
                          ) {
        $kind = 1;
    }
    return $kind;
}


#----------------------------------------------------------------------
# ���β��ä��ɤ���
#----------------------------------------------------------------------
sub isSeaMonster {
    my($mKind) = @_;

    if (   ($mKind == $Mons_Unbaba)
        || ($mKind == 32)
        || (0)
                ){
        return 1;
    }
    return 0;
}


#----------------------------------------------------------------------
# �����ݤ�����
#----------------------------------------------------------------------
sub MonsterDead {
    my ($island , $x , $y , $mKind , $WasteVal ) = @_;

    if ($mKind == $Mons_Kisinhei) {
        my ($landValue3) = $island->{'landValue3'};
        my ($val) = int(($landValue3->[$x][$y] / 500));
        $val = $val * 100;

        if ($val > 0) {
            food_product_plus($island , 'nazoniku' , $val);
            logKishinhei_down($island , "($x,$y)" , $val);
        }
    }

    $island->{'monsterlive'} -= 1 if ($island->{'monsterlive'}); #���������ɥ�����
    MonsterDown( $island , $x , $y , $mKind , $WasteVal );
}


#----------------------------------------------------------------------
# �����ݤ�����
#----------------------------------------------------------------------
sub MonsterDown {

    my ($island , $x , $y , $mKind , $WasteVal ) = @_;
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    if (isSeaMonster($mKind)) {
        SetSeaLand_Normal($island , $x , $y);

    }else{

        if ($mKind == 33) {
            $land->[$x][$y] = $HlandYougan;
            $landValue->[$x][$y] = 1 + random(2);
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
        } else {
            $land->[$x][$y] = $HlandWaste;
            $landValue->[$x][$y] = $WasteVal;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
        }
    }
}

sub Food_Check_more_than {
    my($landkind) = @_;



}


#----------------------------------------------------------------------
# ���˸���������
# ������Ϥʤ�
#----------------------------------------------------------------------
sub isBehindSea {
    my($landkind) = @_;

    if (   ($landkind == $HlandSeacity)
        || ($landkind == $HlandSeatown)
        || ($landkind == $HlandUmishuto)
        || ($landkind == $HlandSbase) ) {
        return 1;
    }
        return 0;

}


#----------------------------------------------------------------------
# ���٤�Υ��٥��
#----------------------------------------------------------------------
sub BigFoodEvent {
    my($island , $x , $y) = @_;# ���٤��
    my($landValue) = $island->{'landValue'};
    my($baselv) = $landValue->[$x][$y];
    my($FoodHP) = $landValue->[$x][$y] & $Food_HP_MASK;
    my($Foodkind) = $landValue->[$x][$y] >> $Food_Kind_Shift;
    my($FoodName) = $BigFoodName[$Foodkind];

    my($point) = "($x,$y)";
    my($name) =islandName($island);

    my($land) = $island->{'land'};

    my($townCount) = countAround($land, $x, $y, 19, @Htowns);

    if ($townCount) {
        $FoodHP--;
        #$island->{'food'} += $townCount * 2;
        food_product_plus($island , 'yasai', ($townCount * 2) );
        if ($FoodHP > 0) {
            $landValue->[$x][$y] = ($Foodkind << $Food_Kind_Shift) | $FoodHP;
            logOut("${HtagName_}${name}$point${H_tagName}��<B>$FoodName</B>���Τΰ�������̱�˿��٤��Ƥ��ޤ���<B>$FoodName</B>�ϥ��᡼��������ޤ�����",$island->{'id'} );

        }else{
            my($Foodva) = $BigFoodMoney[$Foodkind];
            logMsMonMoney($island->{'id'} , $FoodName , $Foodva);
            $island->{'money'} += $Foodva;
            $land->[$x][$y] = $HlandPlains;
            $landValue->[$x][$y] = 0;
        }
    }
}

# ---------------------------------------------------------------------
sub Write_ZooState {
    my ($island, $num , $val) = @_;

    my ($wdata) = '';
    my ($cnt);
    my ($canma) = '';
    my ($temp) = '';

    my ($tmp);
    my (@mons_list);
    my ($list_num);

    $tmp = $island->{'zoo'};
    chomp($tmp);

    @mons_list = split(/\,/,$tmp);

    if ($val < 0) {
        $val = 0;
    }

    $mons_list[$num] = $val;

    $list_num = $#mons_list;

    $list_num = ($list_num <= $num) ? $num : $list_num;

    for ($cnt = 0 ; $cnt <= $list_num ; $cnt++) {

        $temp = ($mons_list[$cnt] eq '') ? '0' : $mons_list[$cnt];

        if ($temp < 0) {
            $temp = 0;
        }

        $wdata .= $canma . $temp;
        $canma = ',';
    }

    chomp($wdata);
    $island->{'zoo'} = $wdata;
}


#----------------------------------------------------------------------
# �����٥��
#----------------------------------------------------------------------
sub ForestEvent {
    my($island , $x , $y) = @_;# ��
    my($landValue) = $island->{'landValue'};
    my($lv) = $landValue->[$x][$y];

    $landValue->[$x][$y]++ if($lv < $HForest_Limit); # �ڤ����䤹
    if ( !random(3) ){
        $landValue->[$x][$y]++ if($lv < $HForest_Limit); # �ڤ����䤹
    }
}

#----------------------------------------------------------------------
# FactoryEvent
#----------------------------------------------------------------------
sub FactoryEvent {
    my ($island , $x , $y) = @_;

    if (!$island->{'business'}) {
        return 0;
    }

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};
    my ($lv2) = $landValue2->[$x][$y];

    if ($lv2 == 1) {
        if ($island->{'lumber_area'}) {

            my ($i , $fx,$fy);

            foreach $i (0..$pointNumber) {
                $fx = $Hrpx[$i];
                $fy = $Hrpy[$i];

                if (   ($land->[$fx][$fy] == $HlandForest)
                    && ($landValue->[$fx][$fy] >= $HForest_Limit) ) {

                    my ($cut) = $HForest_Limit - 5;
                    $landValue->[$fx][$fy] = 5;
                    my ($income) = $HtreeValue * $cut;
                    $island->{'money'} += $income;

                    my ($id) = $island->{'id'};
                    my ($name) = islandName($island);

                    my ($point) = "($x,$y)";
                    my ($fpoint) = "($fx,$fy)";

                    logSecret("${HtagName_}${name}$point${H_tagName}��<b>�ڹ���</b>��${HtagName_}${fpoint}${H_tagName}��<b>��</b>��Ȳ�Τ���${HtagMoney_}$income$HunitMoney${H_tagMoney}�μ���������ޤ�����",$id);
                    return 0;
                }
            }
        }
    }

    return 0;
}


#----------------------------------------------------------------------
# ���ϤΥ��٥��
#----------------------------------------------------------------------
sub WastelandEvent {
    my($island , $x , $y) = @_;

    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($landValue2) = $island->{'landValue2'};
    my($id) = $island->{'id'};

    # �Ӥ���(BattleField)
    if(   (   ($id > 100)
           || (   ($land->[0][0] == $HlandMonument ) 
               && ($landValue->[0][0] == 70) ))
       && (!random(8) )) {

        if(!$landValue->[$x][$y]) {
            $land->[$x][$y] = $HlandPlains;
            $landValue2->[$x][$y]=0;
        } else {
            $landValue->[$x][$y]--;
        }
    }

    if (!$island->{'BF_Flag'}) {
        if (random(100) < 5) {
            WastelandEvent2($island,$x,$y);
        }
    }

}


#----------------------------------------------------------------------
# ���ϤΥ��٥��
#----------------------------------------------------------------------
sub WastelandEvent2 {
    my ($island , $x , $y) = @_;

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};

    my ($seaCount) = countAround($land, $x, $y, 7, @Hseas);

    # �Ӥ���(BattleField)
    if($seaCount > 1) {
        if(!$landValue->[$x][$y]) {
            $landValue->[$x][$y] = 3;
        }
    }
}


#----------------------------------------------------------------------
# ���ɽ�����ϥ��٥��
#----------------------------------------------------------------------
sub FiredeptlandEvent {
    my ($island , $x , $y) = @_;

    if ( $island->{'money'} >= $HFiredept_cost ){
        $island->{'money'} -= $HFiredept_cost;

    }else{
        SetWasteLand_Normal($island , $x , $y);
    }
}

#----------------------------------------------------------------------
sub TaijiPrize {
    my ($island, $mKind) = @_;

    # �ǥХå����äϽ���
    if (grep {$_ == $mKind} @DebugMonster) {
        return;
    }

    # �����༣��
    $island->{'taiji'}++;

    # �޴ط�
    my ($prize) = $island->{'prize'};
    my ($prize1, $prize2) = split(/\t/, $prize);
    $prize1 =~ /([0-9]*),([0-9]*),(.*)/;
    my ($flags) = $1;
    my ($monsters) = $2;
    my ($turns) = $3;
    $monsters = $mKind if ( $mKind > $monsters);
    $island->{'prize'} = "$flags,$monsters,$turns\t$prize2";

    Set_taiji_list($island,$mKind);

}

#----------------------------------------------------------------------
sub Set_taiji_list {
    my ($island, $mKind) = @_;

    my ($block) = int($mKind/32);
    my ($tlist) = $island->{'taiji_list'}[$block];

    $tlist = $tlist | ( 1 << ($mKind % 32));

    $island->{'taiji_list'}[$block] = $tlist;
}


#----------------------------------------------------------------------
# ���Ϥ�Į�����줬���뤫Ƚ��
#----------------------------------------------------------------------
sub countGrow {
    my ($land, $landValue, $x, $y , $bf_flag) = @_;

    my ($i, $sx, $sy);
    for ($i = 1; $i < 7; $i++) {
        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # �Ԥˤ�����Ĵ��
        $sx-- if(!($sy % 2) && ($y % 2));

        if(   (($sx >= 0) && ($sx < $HislandSize) && ($sy >= 0) && ($sy < $HislandSize))  # �ϰ���ξ��
           && (   ($land->[$sx][$sy] == $HlandTown)
               || ($land->[$sx][$sy] == $HlandProcity)
               || ($land->[$sx][$sy] == $HlandNewtown)
               || ($land->[$sx][$sy] == $HlandRizort)
               || ($land->[$sx][$sy] == $HlandBigRizort)
               || ($land->[$sx][$sy] == $HlandBettown)
               || ($land->[$sx][$sy] == $HlandBigtown)
               || ($land->[$sx][$sy] == $HlandHouse)
               || ($land->[$sx][$sy] == $HlandStation)
               || ($land->[$sx][$sy] == $HlandFarm) ) ) {

                return 1 if($landValue->[$sx][$sy] != 1);
        }

        if (   (   ($bf_flag == 1)
                && ($sx >= 0)
                && ($sx < $HislandSize)
                && ($sy >= 0)
                && ($sy < $HislandSize) )   # �ϰ���ξ��
            && ($land->[$sx][$sy] == $HlandDefence)
                                                    ) {
                return 1 ;
        }
    }
    return 0;
}


#----------------------------------------------------------------------
# ���ȼԤϤɤ��ء�
#----------------------------------------------------------------------
sub doIslandunemployed {
    my ($number, $island) = @_;

    # Ƴ����
    my ($name) = islandName($island);
    my ($id) = $island->{'id'};
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};

    # ���ȼԤΰ�̱
    if (   (   ($island->{'unemployed'} >= 100)
            || ($island->{'migrateByMons'}) )
        && (random(100) < 25) 
        && (!$island->{'BF_Flag'})  ) {

        # ���ȼԤ������Ͱʾ夤��� 25% �γ�Ψ�ǰ�̱���˾����
        my (@order) = randomArray($HislandNumber);
        my ($migrate);
        # ��̱���õ��
        my ($tIsland);
        my ($n) = min($HislandNumber, 5);
        my ($i);
        my ($unemployed) = ($island->{'migrateByMons'}) ? int($island->{'pop'} * random(50) / 1000) : $island->{'unemployed'};
        my ($str) = ($island->{'migrateByMons'}) ? '������ä���ƨ���' : '�Ż������';

        for ($i = 0; $i < $n; $i++) { # ����ޤ�Ĵ�٤�
            $tIsland = $Hislands[$order[$i]];

            if ($tIsland->{'predelete'}) {
                next;
            }

            # �Ż��Τ�����˰�̱����
            if ($tIsland->{'unemployed'} < 0) {
                $migrate = min($unemployed, -$tIsland->{'unemployed'});
                last;
            }
        }

        if ($i >= $n) {
            # ��̱�褬���Ĥ���ʤ���С�˽ư���ǥ�Կ�

            $migrate = random($unemployed - 100) + 100;
            $n = 0;
            my($x, $y, $landKind, $lv, $lv2);
            foreach $i (0..$pointNumber) {
                $x = $Hrpx[$i];
                $y = $Hrpy[$i];
                $landKind = $land->[$x][$y];
                $lv = $landValue->[$x][$y];
                $lv2 = $landValue2->[$x][$y];

                if(($landKind == $HlandFarm) ||
                    ($landKind == $HlandFactory) ||
                    ($landKind == $HlandHTFactory) ||
                    ($landKind == $HlandSHTF) ||
                    ($landKind == $HlandFarmchi) ||
                    ($landKind == $HlandFarmpic) ||
                    ($landKind == $HlandFarmcow) ||
                    ($landKind == $HlandCollege) ||
                    ($landKind == $HlandBase) ||
                    ($landKind == $HlandFoodim) ||
                    ($landKind == $HlandNursery) ||
                    (($landKind == $HlandMine) && (!($lv & $Hmine_DAMAGE_MASK))) ||
                    ($landKind == $HlandKatorikun) ||
                    ($landKind == $HlandPark) ||
                    ($landKind == $HlandKyujo) ||
                    ($landKind == $HlandYakusho) ||
                    ($landKind == $HlandKyujo) ||
                    ($landKind == $HlandKyujokai)) {
                    # 25% �γ�Ψ�ǲ���
                    if(random(100) < 25) {
                        $n++;
                        logUnemployedRiot($id, $name, landName($landKind, $lv,$lv2), $migrate, "($x, $y)", $str);
                        SetWasteLand_Normal($island , $x , $y);
                    }
                }
            }

            # ��������ʤ��Ȥ��ϥǥ�Կʤ�Ԥ�
            logUnemployedDemo($id, $name, $migrate, $str) if(!$n);

        } else {
            # ��̱�褬���Ĥ��ä��Τǰ�̱
            my($tLand) = $tIsland->{'land'};
            my($tLandValue) = $tIsland->{'landValue'};
            my($tLandValue2) = $tIsland->{'landValue2'};

            {
                my($x, $y, $landKind, $lv, $lv2);
                foreach $i (0..$pointNumber) {
                    $x = $Hrpx[$i];
                    $y = $Hrpy[$i];
                    $landKind = $tLand->[$x][$y];
                    $lv = $tLandValue->[$x][$y];
                    $lv2 = $tLandValue2->[$x][$y];

                    if($landKind == $HlandSeki) {
                        logUnemployedReturn($id, $tIsland->{'id'}, $name, landName($landKind, $lv, $lv2), islandName($tIsland), $migrate, $str);
                        return 1;
                    }
                }
            }

            # ��̱���Į�˲Ȥ��Ѱդ���
            my($employed) = $migrate;
            my($x, $y, $landKind, $lv, $lv2);
            foreach $i (0..$pointNumber) {
                $x = $Hrpx[$i];
                $y = $Hrpy[$i];
                $landKind = $tLand->[$x][$y];
                $lv = $tLandValue->[$x][$y];
                $lv2 = $tLandValue2->[$x][$y];

                if(($landKind == $HlandOnsen) ||    # 100
                    ($landKind == $HlandTown) ||    # 200
                    ($landKind == $HlandMinato) ||  # 200
                    ($landKind == $HlandSeacity) || # 200
                    ($landKind == $HlandFrocity) || # 200
                    ($landKind == $HlandNewtown) || # 300
                    (($landKind == $HlandBigtown)&&($island->{'yaku'} >= 4)) || # 500
                    (($landKind == $HlandBettown)&&($island->{'yaku'} >= 6)) || # 2000
                                 (0)           ) {
                    # Į
                    # my $nMax = ($landKind == $HlandNewtown) ? 300 : ($landKind == $HlandOnsen) ? 100 : 200;
                    my $nMax = 0;
                    $nMax = $HOnsen_limit  if($landKind == $HlandOnsen);    # ����
                    $nMax = $HTown_limit     if($landKind == $HlandTown);       # Į
                    $nMax = $HTown_limit  if($landKind == $HlandMinato);    # �˥塼������
                    $nMax = $HTown_limit     if($landKind == $HlandSeacity);       # Į
                    $nMax = $HFrocity_limit     if($landKind == $HlandFrocity);       # Į
                    $nMax = $HNewtown_limit  if($landKind == $HlandNewtown);    # �˥塼������
                    $nMax = $HBigtown_limit  if($landKind == $HlandBigtown);    # �����ԻԷ�
                    $nMax = $HBettown_limit  if($landKind == $HlandBettown);    # �������Ի�

                    $n = int(($nMax - $lv) / 2);
                    if ($n == 0) {

                        $n = min( ($nMax - $lv) , $employed);
                    }else{
                        $n = min(int($n + random($n)), $employed);
                    }
                    $employed -= $n;
                    $tLandValue->[$x][$y] += $n;

                } elsif( ($landKind == $HlandPlains) && ($lv == 0)) {
                    # ʿ��
                    $n = int(($HTown_limit - $lv) / 2);
                    $n = min(int($n + random($n)), $employed);
                    $employed -= $n;
                    $tLand->[$x][$y] = $HlandTown;
                    $tLandValue->[$x][$y] = $n;
                    logPlains2Town($tIsland, landName($HlandTown, $n, $lv2) ,"($x, $y)");
                }
                last if($employed <= 0);
            }

            $migrate -= $employed;
            $island->{'unemployed'} -= $migrate;
            $tIsland->{'unemployed'} += $migrate;
            $island->{'pop'} -= $migrate;
            $tIsland->{'pop'} += $migrate;

            # ���ޤǽ���Ǥ����Ȥ��ʬ����
            $employed = $migrate;
            foreach $i (0..$pointNumber) {
                $x = $Hrpx[$i];
                $y = $Hrpy[$i];
                $landKind = $land->[$x][$y];
                $lv = $landValue->[$x][$y];

                if (   ($lv > 1)
                    && (   ($landKind == $HlandTown)
                        || ($landKind == $HlandMinato)
                        || ($landKind == $HlandProcity)
                        || ($landKind == $HlandNewtown)
                        || ($landKind == $HlandFrocity)
                        || ($landKind == $HlandBettown)
                        || ($landKind == $HlandShuto)
                        || ($landKind == $HlandUmishuto)
                        || ($landKind == $HlandBigtown)
                        || ($landKind == $HlandSeatown)
                        || ($landKind == $HlandOnsen)
                        || ($landKind == $HlandSeacity)
                        || ($landKind == $HlandUmicity)
                        || ($landKind == $HlandOilCity)
                        || ($landKind == $HlandInaka)
                                                        )) {
                    # Į
                    $n = min($lv - 1, $employed);
                    $landValue->[$x][$y] -= $n;
                    $employed -= $n;
                }
                last if($employed <= 0);
            }

            if ($migrate) {
                logUnemployedMigrate($id, $tIsland->{'id'}, $name, islandName($tIsland), $migrate, $str);
                # �����Ƚ��Τ���˰�̱�򵭲�
                $island->{'migrate'} = $migrate if(!$island->{'migrateByMons'});
            }
        }
    }
}


#----------------------------------------------------------------------
# ������
#----------------------------------------------------------------------
sub doIslandProcess {
    my($number, $island) = @_;

    # Ƴ����
    my($name) = islandName($island);
    my($id) = $island->{'id'};
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($landValue2) = $island->{'landValue2'};
    my ($landValue3) = $island->{'landValue3'};

    my $disdown    = 1;
    if ($HallyDisDown && ($island->{'allyId'}[0] ne '')) {
        $disdown   = $HallyDisDown;
    }
    my $pika2 = 0;

    # ������(�ޤȤ�ƥ�����)
    if ($HlogOmit1) {
        logOilMoney($id, $name, "����", "", "���$island->{'oilincome'}${HunitMoney}", "����") if(($island->{'oilincome'} > 0));
        logOilMoney($id, $name, "ͷ����", "", "���$island->{'parkincome'}${HunitMoney}", "����") if(($island->{'parkincome'} > 0));
        logParkEventf($id, $name, "�����ȹ�", "", "����͹�$island->{'fishcatch'}${HunitFood}") if(($island->{'fishcatch'} > 0));
    }

    # ������(�ߥ�������)
    if (STATUE_LOG_OMIT) {
        if ($island->{'statue_income'} > 0 ) {
            logMiyage($id, $name, "��ʡ�ν�����", "", "���$island->{'statue_income'}$HunitMoney");
        }
        if ($island->{'statue_income_food'} > 0 ) {
            logParkEventt($id, $name, "��ʡ�ν���", "", "$island->{'statue_income_food'}$HunitFood");
        }
    }

    if ($island->{'stsankahantei'} == 1) {
        $value = $Hstsanka*random(2000);
        $island->{'money'} += $value;
        logHCstart($id, $name, "$value$HunitMoney");
    }

    if($island->{'shtf'} > 0) {
        $pika2 = int($island->{'factory'}/2);
        if ($pika2 > 0) {
            $island->{'money'} -= $pika2;
            logFactoryHT($id, $name, "�ϥ��ƥ����", "$pika2${HunitMoney}") ;
        }

    }elsif($island->{'htf'} > 0) {
        $pika2 = int($island->{'pika'}/2);
        if ($pika2 > 0) {
            $island->{'money'} -= $pika2;
            logFactoryHT($id, $name, "�ϥ��ƥ����", "$pika2${HunitMoney}") ;
        }
    }

    # ����Ƚ��
    if(   ($HpunishInfo{$id}->{punish} == 2)
       || (!$HnoDisFlag && random(1000) < int($HdisTsunami[0] * $disdown - $island->{'eis2'}/15)) ) {
        # ����ȯ��
        logTsunami($id, $name);

        my($x, $y, $landKind, $lv, $i);
        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];
            $lv = $landValue->[$x][$y];

            if(   ($landKind == $HlandTown)
               || (   ($landKind == $HlandProcity)
                   && ($lv < 110) )
               || ($landKind == $HlandFarm)
               || ($landKind == $HlandFarmchi)
               || ($landKind == $HlandFarmpic)
               || ($landKind == $HlandFarmcow)
               || ($landKind == $HlandFoodim)
               || ($landKind == $HlandFactory)
               || ($landKind == $HlandHTFactory)
               || ($landKind == $HlandSHTF)
               || ($landKind == $HlandCollege)
               || ($landKind == $HlandStation)
               || ($landKind == $HlandBase)
               || ($landKind == $HlandDefence)
               || ($landKind == $HlandPark)
               || ($landKind == $HlandMinato)
               || ($landKind == $HlandFune)
               || ($landKind == $HlandSeki)
               || ($landKind == $HlandMine)
               || ($landKind == $HlandZoo)
               || ($landKind == $HlandNursery)
               || ($landKind == $HlandKyujo)
               || ($landKind == $HlandKyujokai)
               || ($landKind == $HlandBettown)
               || ($landKind == $HlandRizort)
               || ($landKind == $HlandYakusho)
               || ($landKind == $HlandBigRizort)
               || ($landKind == $HlandShuto)
               || ($landKind == $HlandNewtown)
               || ($landKind == $HlandUmicity)
               || ($landKind == $HlandBigtown)
               || ($landKind == $HlandOilCity)
               || ($landKind == $HlandKatorikun) ) {

                # 1d12 <= (���Ϥγ� - 1) ������
                my @seas = @Hseas;
                pop(@seas);
                if (random(12+$island->{'co5'}*5) < (countAround($land, $x, $y, 7, @seas) - 1)) {
                    logDamageAny($id, $name, landName($landKind, $lv,$landValue2->[$x][$y]), "($x, $y)", "${HtagDisaster_}����${H_tagDisaster}�ˤ���������ޤ�����");
                    if(   ($landKind == $HlandFune)
                       || ($landKind == $HlandUmicity)
                       || ($landKind == $HlandOilCity)
                                                    ) {
                        $land->[$x][$y] = $HlandSea;
                        $landValue->[$x][$y] = 0;
                        $landValue2->[$x][$y] = 0;
                        # �Ǥ��ܿ���ʤ�����
                    } elsif($landKind == $HlandNursery) {
                        $land->[$x][$y] = $HlandSea;
                        $landValue->[$x][$y] = 1;
                        $landValue2->[$x][$y] = 0;
                    } else {

                        SetWasteLand_Normal($island , $x , $y);     # $HlandWaste
                    }
                }
            }
        }
    }

    # �Ͽ�Ƚ��
    if (   ($HpunishInfo{$id}->{punish} == 1)
        || (   (!$HnoDisFlag) 
            && (random(1000) < int(($island->{'prepare2'} + 1) * $HdisEarthquake[0] * $disdown - $island->{'eis2'}/15)) )
                                                                                                                        ) {
        # �Ͽ�ȯ��
        logEarthquake($id, $name);
        $HdisTsunami[0] = $HdisTsunami[1];

        my($x, $y, $landKind, $lv,$lv2, $i);

        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];
            $lv = $landValue->[$x][$y];
            $lv2 = $landValue2->[$x][$y];

            if (
                 ($landKind == $HlandHaribote) ||
                 (($landKind == $HlandFoodim) && ($lv < 480)) || 
                 ($landKind == $HlandTrain) ||
                 ($landKind == $HlandPark) ||
                 ($landKind == $HlandOnsen) ||
                 ($landKind == $HlandStation) ||
                 ($landKind == $HlandKatorikun) ||
                 ($landKind == $HlandSeki) ||
                 ($landKind == $HlandRocket) ||
                 ($landKind == $HlandDefence) ||
                 ($landKind == $HlandFactory)
                                                ) {
                # 1/4�ǲ���
                if (!random(4+$island->{'co5'}*5)) {
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}�Ͽ�${H_tagDisaster}�ˤ����Ǥ��ޤ�����");
                    SetWasteLand_Normal($island , $x , $y);

                    if ($landKind == $HlandOnsen) {
                        # �����ϻ������
                        $land->[$x][$y] = $HlandMountain; # ���ˤʤ�
                        $landValue->[$x][$y] = 0;
                        $landValue2->[$x][$y] = 0;
                    }
                    next;
                }
            }

            if (   (($landKind == $HlandTown) && ($lv >= 100))
                || (($landKind == $HlandProcity) && ($lv < 130))
                || (($landKind == $HlandMinato) && ($lv >= 100))
                || (($landKind == $HlandNewtown) && ($lv >= 100))
                || (($landKind == $HlandBigRizort) && ($lv >= 100))
                || (($landKind == $HlandRizort) && ($lv >= 100))
                || (($landKind == $HlandBigtown) && ($lv >= 100))
                || (($landKind == $HlandBettown) && ($lv >= 100))
                || (($landKind == $HlandShuto) && ($lv >= 100))
                                                    ) {
                # 1/4�ǲ���
                if(!random(4+$island->{'co5'}*5)) {

                    if (countAround($land, $x, $y, 7, $HlandPlains,$HlandKyujo,$HlandYakusho,$HlandKyujokai,$HlandMonument,$HlandFiredept,$HlandCollege) ) {
                        logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}�Ͽ�${H_tagDisaster}�ˤ���ﳲ������ޤ�����");
                        $landValue->[$x][$y] -= random(30)+10;

                    }else{

                        logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}�Ͽ�${H_tagDisaster}�ˤ����Ǥ��ޤ�����");
                        $landValue->[$x][$y] -= random(100)+50;

                    }
                    if($landValue->[$x][$y] <= 0) {
                        # ʿ�Ϥ��᤹
                        SetWasteLand_Normal($island , $x , $y);
                        if ($landKind == $HlandOnsen) {
                            # �����ϻ������
                            $land->[$x][$y] = $HlandMountain; # ���ˤʤ�
                            $landValue->[$x][$y] = 0;
                            $landValue2->[$x][$y] = 0;
                        }
                        logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}�Ͽ�${H_tagDisaster}�ˤ����Ǥ��ޤ�����");
                        next;
                    }
                }
            }

            if (   (0)
                || (($landKind == $HlandHTFactory) && ($lv >= 10))
                || (($landKind == $HlandSHTF) && ($lv >= 10))
                || (($landKind == $HlandUmishuto) && ($lv >= 100))
                || (($landKind == $HlandSeatown) && ($lv >= 100))
                || (($landKind == $HlandSeacity) && ($lv >= 100))
                || (($landKind == $HlandUmicity) && ($lv >= 100))
                || (($landKind == $HlandOilCity) && ($lv >= 100))
                || (($landKind == $HlandUmiamu) && ($lv >= 10))
                || (($landKind == $HlandInoraLand) && ($lv >= 10))
                                                                    ) {
                # 1/4�ǲ���
                if (!random(3+$island->{'co5'}*5)) {
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}�Ͽ�${H_tagDisaster}�ˤ���ﳲ������ޤ�����");
                    $landValue->[$x][$y] -= random(100)+50;
                }
                if ($landValue->[$x][$y] <= 0) {
                    # ʿ�Ϥ��᤹
                    SetWasteLand_Normal($island , $x , $y);
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}�Ͽ�${H_tagDisaster}�ˤ����Ǥ��ޤ�����");
                    next;
                }
            }

            if (   ($landKind == $HlandFarmchi)
                || ($landKind == $HlandFarmpic)
                || ($landKind == $HlandFarmcow)
                                                    ) {

                if (!random(6)) {
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}�Ͽ�${H_tagDisaster}�ˤ���ﳲ������ޤ�����");
                    $landValue->[$x][$y] -= random(400)+50;
                }

                if ($landValue->[$x][$y] <= 0) {
                    # ʿ�Ϥ��᤹
                    SetWasteLand_Normal($island , $x , $y);
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}�Ͽ�${H_tagDisaster}�ˤ����Ǥ��ޤ�����");
                    next;
                }
            }
        }
    }

    # ���Ǥˤ���뽻̱
    if (random(100) < int(($island->{'eisei1'} - 10 - random(5)) * $disdown)) {
        # ��­��å�����
        logKire($id, $name);

        my($x, $y, $landKind, $lv, $i);
        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];
            $lv = $landValue->[$x][$y];

            if (   ($landKind == $HlandFarm)
                || ($landKind == $HlandCollege)
                || ($landKind == $HlandFactory)
                || ($landKind == $HlandHTFactory)
                || ($landKind == $HlandSHTF)
                || ($landKind == $HlandNursery)
                || ($landKind == $HlandBase)
                || ($landKind == $HlandKatorikun)
                || ($landKind == $HlandPark)
                || ($landKind == $HlandKyujo)
                || ($landKind == $HlandZoo)
                || ($landKind == $HlandKyujokai)
                || ($landKind == $HlandDefence)
                || ($landKind == $HlandYakusho)
                || ($landKind == $HlandHouse)
                                                ) {
                # 1/4�ǲ���
                if (random(100) < $island->{'eisei1'}) {
                    logKireDamage($id, $name, landName($landKind, $lv,$landValue2->[$x][$y]), "($x, $y)");
                    SetWasteLand_Normal($island , $x , $y);
                    # �Ǥ��ܿ���ʤ�����
                    if ($landKind == $HlandNursery) {
                        $land->[$x][$y] = $HlandSea;
                        $landValue->[$x][$y] = 1;
                        $landValue2->[$x][$y] = 0;
                    }
                }
            }

            if(($landKind == $HlandTown) ||
                ($landKind == $HlandMinato) ||
                ($landKind == $HlandFoodim) ||
                ($landKind == $HlandProcity) ||
                ($landKind == $HlandFarmchi) ||
                ($landKind == $HlandFarmpic) ||
                ($landKind == $HlandFarmcow)) {
                # 1/4�ǲ���
                if(random(100) < $island->{'eisei1'}-30) {
                    logKireDamage($id, $name, landName($landKind, $lv,$landValue2->[$x][$y]), "($x, $y)");
                    SetWasteLand_Normal($island , $x , $y);
                }
            }

            if (($landKind == $HlandSbase) ||
                ($landKind == $HlandSeacity) ||
                ($landKind == $HlandUmiamu) ||
                ($landKind == $HlandFrocity)) {
                # 1/4�ǲ���
                if (random(100) < $island->{'eisei1'}-60) {
                    logKireDamage($id, $name, landName($landKind, $lv,$landValue2->[$x][$y]), "($x, $y)");
                    $land->[$x][$y] = $HlandSea;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    $landValue3->[$x][$y] = 0;
                }
            }
        }
    }

    # ������­
    my ($landKind, $lv , $wo);
    $landKind = $land->[$x][$y];
    $lv = $landValue->[$x][$y];

    $wo = 0;
    if (   ($landKind == $HlandMonument)
        && ($lv == 70)) {
        $wo = 1;
    }

    if (($island->{'food'} <= 0) && ($id <= 100) && (!$wo)) {
        # ��­��å�����
        logStarve($id, $name);
        food_product_All_Clear($island);

        my ($x, $y, $i);

        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];
            $lv = $landValue->[$x][$y];

            if (   ($landKind == $HlandFarm)
                || ($landKind == $HlandFoodim)
                || ($landKind == $HlandFarmchi)
                || ($landKind == $HlandFarmpic)
                || ($landKind == $HlandFarmcow)
                || ($landKind == $HlandFactory)
                || ($landKind == $HlandHTFactory)
                || ($landKind == $HlandSHTF)
                || ($landKind == $HlandCollege)
                || ($landKind == $HlandNursery)
                || ($landKind == $HlandBase)
                || ($landKind == $HlandMine)
                || ($landKind == $HlandZoo)
                || ($landKind == $HlandYakusho)
                || ($landKind == $HlandKatorikun)
                || ($landKind == $HlandStation)
                || ($landKind == $HlandDefence)
                                                ) {
                # 1/4�ǲ���
                if(!random(4)) {
                    logSvDamage($id, $name, landName($landKind, $lv, $landValue2->[$x][$y]), "($x, $y)");
                    SetWasteLand_Normal($island , $x , $y);

                    # �Ǥ��ܿ���ʤ�����
                    if($landKind == $HlandNursery) {
                        $land->[$x][$y] = $HlandSea;
                        $landValue->[$x][$y] = 1;
                        $landValue2->[$x][$y] = 0;
                    }
                }
            }
        }
    }

    # ����Ƚ��
    my ($real) = ($HislandTurn + 8) % 12 ;
    my ($r, $pop, $num );

    $island->{'event_monstersend'} = 0;

    {
        if ($HDayEvent_Edge) {
            my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
            $mon += 1;
            if (($mon == 3) && ($mday == 3)) {
                $island->{'event_monstersend'} = 1;
                $HDayEvent_Edge--;
            }
        }
    }

    $num = 0;
    if( ($island->{'id'} > 100) || 
        (($land->[0][0] == $HlandMonument) && ($landValue->[0][0] == 70) ) ) {
        $r = random(10000);
        $r = -1 if( $island->{'monsterlive'} < 40 ) ;
        $pop = $HdisMonsBorder3;
        $num = random(4) + random(4) + random(4) + 1;
    } else {
        $r = random(10000);
        $pop = $island->{'pop'};
    }

    $r = $HdisMonster[$real] * $island->{'area'} if ($HnoDisFlag);
    $r = $HdisMonster[$real] * $island->{'area'} if ($island->{'omamori'});
    $r = 0 if ($HpunishInfo{$id}->{punish} == 3);

    my ($sea_build) = $island->{'sea_build'};

    do {
        $num-- ;
        if(   (   ($r < int($HdisMonster[$real] * $disdown * $island->{'area'})) 
               && ($pop >= $HdisMonsBorder1)) 
           || ($island->{'monstersend'} > 0)
           || ($island->{'event_monstersend'} > 0) ) {

            # ���ýи�
            # ��������
            my ($kind,$lv2);

            if (   ($island->{'BF_Flag'} == 1)
                || ($island->{'monstersend'} > 0)
                || ($island->{'event_monstersend'} > 0) ) {

                ($kind,$lv2) = MonsterSpawnKind($island , 1);
            }
            elsif (   (   ($sea_build < 20)
                       && (random(100) < 90) ) ) {

                ($kind,$lv2) = MonsterSpawnKind($island , 1);
            }
            else {
                $kind = (random(2)) ? $Mons_Unbaba : $Mons_Pirates ;
                $lv2 = 0;
            }

            my ($lv) = Calc_MonsterLandValue($kind);

            # �ɤ��˸���뤫����
            my ($bx, $by, $i, $def , $tar_kind);
            my ($escape) = 1;

            foreach $i (0..$pointNumber) {
                $bx = $Hrpx[$i];
                $by = $Hrpy[$i];
                $def = 0;
                $def = countAround($land, $bx, $by, 19, $HlandDefence) if ($island->{'BF_Flag'} == 1) ;

                $tar_kind = $land->[$bx][$by];

                if (   (   (   ($kind != $Mons_Unbaba)
                            && ($kind != $Mons_hime_inora)
                            && ($kind != $Mons_Pirates)
                            && (   ($tar_kind == $HlandTown)        # Į��
                                || ($tar_kind == $HlandNewtown)     # �˥塼������
                                || ($tar_kind == $HlandBigtown)     # �����Ի�
                                || ($tar_kind == $HlandBettown)     # �������Ի�
                                || ($tar_kind == $HlandRizort)      # �꥾������
                                || ($tar_kind == $HlandBigRizort)   # �׳��꥾���ȥۥƥ�
                                || ($tar_kind == $HlandForest)      # ��
                                || ($tar_kind == $HlandWaste)       # ����
                                || ($tar_kind == $HlandFarm)        # ����
                                || ($tar_kind == $HlandTrain)       # ��ϩ
                                || ($tar_kind == $HlandHaribote)    # �ϥ�ܥ�
                                || ($tar_kind == $HlandFactory)     # ����
                                || ($tar_kind == $HlandRocket)      # ���å�
                                                                 ))
                        || (   ($kind == $Mons_Unbaba)
                            && (   ($tar_kind == $HlandSea)         # ��
                                || ($tar_kind == $HlandOil)         # ��������
                                || ($tar_kind == $HlandMinato)      # ��
                                || ($tar_kind == $HlandFune)        # ����
                                || ($tar_kind == $HlandNursery)     # �ܿ���
                                || ($tar_kind == $HlandFrocity)     # �ե���
                                || ($tar_kind == $HlandSbase)       # �������
                                || ($tar_kind == $HlandSeacity)     # �����Ի�
                                || ($tar_kind == $HlandUmiamu)      # �����ߤ�
                                || ($tar_kind == $HlandIce)         # ɹ��
                                || (($tar_kind == $HlandSunahama) && (!$lv))   # ����
                                                                 ))
                        || (   ($kind == $Mons_Pirates)
                            && (   ($tar_kind == $HlandSea)         # ��
                                                                 ))
                        || (   ($kind == $Mons_hime_inora)
                            && (   ($tar_kind == $HlandSea)         # ��
                                || ($tar_kind == $HlandWaste)       # ����
                                || ($tar_kind == $HlandPlains)      # ʿ��
                                                                 ))
                                                                    )
                    && ($def == 0)          # BF��
                                     ) {

                    if ( (isSeaMonster($kind)) ) {
                        if (countAround($land, $bx, $by, 7, $HlandForest) > 0 ){
                            next;
                        }
                    }

                    my ($mlv3) = 0;

                    if ($kind == $Mons_Kisinhei) {

                        my ($atk_kind);
                        my ($temp);
                        $mlv3 = $landValue3->[$bx][$by];
                        my ($atkx , $atky);
                        for ($i = 1; $i < 7; $i++) {
                            $atkx = $bx + $ax[$i];
                            $atky = $by + $ay[$i];

                            # �Ԥˤ�����Ĵ��
                            $atkx-- if(!($atky % 2) && ($by % 2));

                            # �ϰ���ξ��
                            if (($atkx >= 0) && ($atkx < $HislandSize) && ($atky >= 0) && ($atky < $HislandSize)) {

                                $atk_kind = ($land->[$atkx][$atky]);

                                foreach my $ta (@Htowns) {
                                    if ($atk_kind == $ta) {
                                        if ($landValue->[$atkx][$atky] > 4) {
                                            $temp = ($landValue->[$atkx][$atky] >> 1);
                                            $landValue->[$atkx][$atky] -= $temp;
                                            $mlv3 += $temp;
                                        }
                                    }
                                }
                            }
                        }
                        logKishinhei_kyusyu($island , "($bx , $by)" , $mlv3);
                    }

                    # �Ϸ�̾
                    my($lName) = landName($tar_kind, $landValue->[$bx][$by], $landValue2->[$bx][$by]);
                    # ���Υإå�������ä�
                    $land->[$bx][$by] = $HlandMonster;
                    $landValue->[$bx][$by] = $lv;
                    $landValue2->[$bx][$by] = 0;
                    $landValue3->[$bx][$by] = $mlv3;
                    $escape = 0 ;

                    # �ĥ��å���bot�� BF�Ͻ���
                    if (!$island->{'BF_Flag'}) {
                        $Appearance_monster = $HmonsterImage[$kind];
                    }

                    # ���þ���
                    $mName = $HmonsterName[$kind];

                    # ��å�����
                    logMonsCome($id, $name, $mName, "($bx, $by)", $lName);
                    last;
                }
            }

            if ($escape) {
                $island->{'monstersend'} = 0;
                $num = 0;
                last;
            }
        }
    } while( ( $island->{'monstersend'} > 0 ) || ($num > 0) );


    # ��������Ƚ��
    if (    (   ($HpunishInfo{$id}->{punish} == 4) 
             || (!$HnoDisFlag && random(1000) < int($HdisFalldown[0] * $disdown))) 
         && ($island->{'area'} > $HdisFallBorder)
         && (!$island->{'BF_Flag'}) ) {

        # ��������ȯ��
        logFalldown($id, $name);

        my ($x, $y, $landKind, $lv, $lv2, $i);
        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];
            $lv2 = $landValue2->[$x][$y];
            $lv = $landValue->[$x][$y];

            if (($landKind != $HlandSea) &&
                ($landKind != $HlandSbase) &&
                ($landKind != $HlandIce) &&
                ($landKind != $HlandSeacity) &&
                ($landKind != $HlandSeatown) &&
                ($landKind != $HlandFune) &&
                ($landKind != $HlandUmishuto) &&
                ($landKind != $HlandUmiamu) &&
                ($landKind != $HlandOil) &&
                ($landKind != $HlandGold) &&
                ($landKind != $HlandShrine) &&
                ($landKind != $HlandOnsen) &&
                ($landKind != $HlandMountain)) {

                # ���Ϥ˳�������С��ͤ�-1��
                my @seas = @Hseas;
                pop(@seas);
                pop(@seas);
                if (countAround($land, $x, $y, 7, @seas)) {
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "����������ߤޤ�����");
                    $land->[$x][$y] = -1;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                }
            }
        }

        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];

            if($landKind == -1) {
                # -1�ˤʤäƤ�����������
                $land->[$x][$y] = $HlandSea;
                $landValue->[$x][$y] = 1;
            } elsif($landKind == $HlandSea) {
                # �����ϳ���
                $landValue->[$x][$y] = 0;
            }
        }
    }

    # ����Ƚ��
    if(    ($HpunishInfo{$id}->{punish} == 5)
        || (    (!$HnoDisFlag)
             && (random(1000) < int($HdisTyphoon[$Hmonth] * $disdown - $island->{'eis1'}/10)) ) ) {
        # ����ȯ��
        logTyphoon($id, $name);

        my($x, $y, $landKind, $lv, $lv2, $i);
        foreach $i (0..$pointNumber) {
            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            $landKind = $land->[$x][$y];
            $lv  = $landValue->[$x][$y];
            $lv2 = $landValue2->[$x][$y];

            if (   ($landKind == $HlandFarm)
                || ($landKind == $HlandHaribote)
                || ($landKind == $HlandTrain)
                                                ) {
                # 1d12 <= (6 - ���Ϥο�) ������
                if(random(12+$island->{'co5'}*5) < (6 - countAround($land, $x, $y, 7, $HlandForest, $HlandMonument))) {
                    logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}����${H_tagDisaster}�����Ф���ޤ�����");
                    $land->[$x][$y] = $HlandPlains;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    if (   ($landKind == $HlandFarm)
                        && ($lv2 == 2) ) {
                        $land->[$x][$y] = $HlandSunahama;
                    }

                    if (random(1000) < 100) {
                        $land->[$x][$y] = $HlandMonument;
                        $landValue->[$x][$y] = 77;
                    }
                }
            }

            if(   (   ($landKind == $HlandFune)
                   || ($landKind == $HlandNursery) )
               && (random(100+$island->{'co5'}*50) < 10) ) {
                logDamageAny($id, $name, landName($landKind, $lv,$lv2), "($x, $y)", "${HtagDisaster_}����${H_tagDisaster}�ˤ�ä���»���ޤ�����");
                $land->[$x][$y] = $HlandSea;
                $landValue->[$x][$y] = 1;
                $landValue2->[$x][$y] = 0;
            }
        }
    }

    my($def_flag);
    # �������Ƚ��
    if(   ($HpunishInfo{$id}->{punish} == 6)
       || (   (!$HnoDisFlag)
           && (random(1000) < int($HdisHugeMeteo[$Hmonth] * $disdown - $island->{'eis3'}/50)) )) {
        my($x, $y, $landKind, $lv, $point);

        # �
        $x = random($HislandSize);
        $y = random($HislandSize);

        $HSpaceDebri -= $HSpaceDebri_meteo;     #���ڡ����ǥ֥�

        if ($HpunishInfo{$id}->{punish} == 6) {
            $x = $HpunishInfo{$id}->{x};
            $y = $HpunishInfo{$id}->{y};
        }
        $landKind = $land->[$x][$y];
        $lv = $landValue->[$x][$y];
        $point = "($x, $y)";

        $def_flag = 0;
        if ( $landKind == $HlandDefence ) {
            my($defLv , $defHP );
            $defHP = 0;
            $defLv = 0;
            $defLv = ($lv & $HDefenceLevelMask);

            if ( $defLv >= 2 ) {
                $def_flag = 1;
                $defHP = $lv >> $HDefenceHP_SHIFT;
                $defHP = $defHP - 3;
                $defHP = 0 if ( $defHP < 0 );
                $landValue->[$x][$y] = 2 + ( $defHP << $HDefenceHP_SHIFT ) ;
            }

            if ( $defHP <= 0 ) {
                logMeteoDef($id, $name, $lName, $point, "����ľ�⤷");
                $def_flag = 0;
            }

        }else{
            $def_flag = countAround_DefBase($land,$landValue, $x, $y, 19, 1);
        }

        if( $def_flag ){
            logMeteoDef($id, $name, $lName, $point, "���ޤ��������ɱҴ��ϡ����˼���");
            next;
        }

        # ��å�����
        logHugeMeteo($id, $name, $point);

        # �����ﳲ�롼����
        wideDamage($id, $name, $land, $landValue, $x, $y);
        if (random(1000) < 100) {
            $land->[$x][$y] = $HlandMonument;
            $landValue->[$x][$y] = 79;
        }
    }

    # ����ߥ�����Ƚ��
    BigMissileRoutine($island);

    Flood($island);

    # ���Ƚ��
    my ($rnd) = random(1000);
    if (   ($HpunishInfo{$id}->{punish} == 7)
        || (   (!$HnoDisFlag)
            && ($rnd < int($HdisMeteo[0] * $disdown)))) {

        if ($rnd < int($HdisMeteo[0] * $disdown - $island->{'eis3'}/40)) {
            Meteo_disaster($island);
        }else{
            logMeteo_Safe($island);
        }
    }

    # �ݥå�������
    Pockey_Event($island);

    # ʮ��Ƚ��
    if(   ($HpunishInfo{$id}->{punish} == 8)
       || (!$island->{'BF_Flag'})
           && (!$HnoDisFlag && random(1000) < int($HdisEruption[0] * $disdown - $island->{'eis2'}/40))) {

        my($x, $y);

        $x = random($HislandSize);
        $y = random($HislandSize);
        if ($HpunishInfo{$id}->{punish} == 8) {
            $x = $HpunishInfo{$id}->{x};
            $y = $HpunishInfo{$id}->{y};
        }

        Volcano($island,$x,$y);
    }

    # �͹��������ͥ륮������
    Satellite_Energy($island);

    Satellite_Irregular_Attack($island);

    # �����ݽ���Ϥ��
    if ($island->{'yaku'}){
        Yakusyo_clean($island);
    }
}


#----------------------------------------------------------------------
sub isPockeyDay {
    my($mon , $mday) = @_;

    if (   ($mon == 11)
        && ($mday == 11) ) {

        return 1;
    }
    return 0;
}

#----------------------------------------------------------------------

sub Pockey_Event {
    my ($island) = @_;

    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $mon += 1;

    if ($HDayEvent_Edge) {

        if (isPockeyDay($mon , $mday) ) {
            logOut("isPockeyDay" , 1);

            my ($x,$y);
            my ($i);
            my ($landKind);
            my ($lv);
            my ($land) = $island->{'land'};
            my ($landValue) = $island->{'landValue'};

            for ($i = 0; $i < $HpointNumber; $i++){

                $x = $Hrpx[$i];
                $y = $Hrpy[$i];
                $landKind = $land->[$x][$y];
                $lv = $landValue->[$x][$y];

                if (   ($landKind == $HlandPlains)
                    || ($landKind == $HlandWaste)
                    || (($landKind == $HlandSea) && ($lv != 0) ) ) {

                    my ($point) = "($x, $y)";
                    my ($lv2) = $island->{'landValue2'};
                    my ($lv3) = $island->{'landValue3'};
                    # �ݥå���
                    my($mKind) = 4 + random(4);
                    $lv = ($mKind << $Food_Kind_Shift) + (5) ; #���祳�졼�� HP5
                    $ItemName = landName($HlandBigFood, $lv, 0);

                    $land->[$x][$y] = $HlandBigFood;
                    $landValue->[$x][$y] = $lv;
                    $lv2->[$x][$y] = 0;
                    $lv3->[$x][$y] = 0;

                    my ($name) = islandName($island);

                    logOut("${HtagName_}${name}${point}${H_tagName}�˱��褫��<B>$ItemName</B>�������ޤ�����",$island->{'id'} );

                    last;
                }
            }
        }
    }


}

#----------------------------------------------------------------------
sub Satellite_Irregular_Attack {
    my ($island) = @_;

    my ($name) = islandName($island);
    my ($id) = $island->{'id'};
    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    #my ($landValue2) = $island->{'landValue2'};
    #my ($landValue3) = $island->{'landValue3'};


    if ($island->{'eis6'}) {
        my ($i, $sx, $sy);
        for ($i = 0; $i < $HpointNumber; $i++){
            $sx = $Hrpx[$i];
            $sy = $Hrpy[$i];
            if ($land->[$sx][$sy] == $HlandMonster){
                # ���ä������硢���β��ä򹶷⤹��
                # �оݤȤʤ���äγ����Ǽ��Ф�
                my($tKind, $tName, $tHp) = monsterSpec($landValue->[$sx][$sy]);
                my($tlv) = $landValue->[$sx][$sy];
                #my($tspecial) = $HmonsterSpecial[$tKind];
                $point = int($island->{'rena'}/1000);
                logIreAttackt($id, $name, "���쥮��顼", $point, $tName, $tPoint);

                $island->{'eis6'} -= 10;

                $tHp -= int($island->{'rena'}/1000);
                $tlv -= int($island->{'rena'}/1000);
                $landValue->[$sx][$sy] = $tlv;
                if($tHp < 1){
                    # �оݤβ��ä��ݤ�ƹ��Ϥˤʤ�
                    MonsterDead($island , $sx , $sy , $tKind , 0 );
                    # �󾩶�
                    my($value) = $HmonsterValue[$tKind];
                    $island->{'money'} += $value;
                    logMsMonMoney($id, $tName, $value);
                }
                next;
            }
        }
    }
}


#----------------------------------------------------------------------
sub Meteo_disaster {
    my($island) = @_;

    my($name) = islandName($island);
    my($id) = $island->{'id'};
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($landValue2) = $island->{'landValue2'};
    my($landValue3) = $island->{'landValue3'};

    # ���Ƚ��

    my($x, $y, $landKind, $lv, $lName, $point, $first);
    my($def_flag);

    $first = 1;
    while (!random(2) || $first) {
        $first = 0;

        # ���ڡ����ǥ֥꤬����
        $HSpaceDebri -= $HSpaceDebri_meteo;

        # �
        $x = random($HislandSize);
        $y = random($HislandSize);
        $landKind = $land->[$x][$y];
        $lv = $landValue->[$x][$y];
        $point = "($x, $y)";
        $lName = landName($landKind, $lv,$landValue2->[$x][$y]);

        $def_flag = 0;
        if ( $landKind == $HlandDefence ) {
            my($defLv , $defHP );
            $defHP = 0;
            $defLv = 0;
            $defLv = ($lv & $HDefenceLevelMask);

            if ( $defLv >= 2 ) {
                $def_flag = 1;
                $defHP = $lv >> $HDefenceHP_SHIFT;
                $defHP = $defHP - 3;
                $defHP = 0 if ( $defHP < 0 );
                $landValue->[$x][$y] = 2 + ( $defHP << $HDefenceHP_SHIFT ) ;
            }

            if ( $defHP <= 0 ) {
                logMeteoDef($id, $name, $lName, $point, "����ľ�⤷");
                $def_flag = 0;
            }

        }else{
            $def_flag = countAround_DefBase($land,$landValue, $x, $y, 19, 1);
        }

        if ($def_flag) {
            logMeteoDef($id, $name, $lName, $point, "���ޤ��������ɱҴ��ϡ����˼���");
            next;

        } elsif (($landKind == $HlandSea) && !$lv){
            # ���ݥ���
            logMeteo($id, $name, $lName, $point, "��");

        } elsif (   ($landKind == $HlandMountain)
                 || ($landKind == $HlandGold)
                 || ($landKind == $HlandShrine)
                 || ($landKind == $HlandOnsen)  ) {
            # �����⻳�����ο����˲�
            logMeteo($id, $name, $lName, $point, "��<B>$lName</B>�Ͼä�����");
            $land->[$x][$y] = $HlandWaste;
            $landValue->[$x][$y] = 2;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
            next;

        } elsif(($landKind == $HlandSbase) ||
                ($landKind == $HlandSeacity) ||
                ($landKind == $HlandSeatown) ||
                ($landKind == $HlandFune) ||
                ($landKind == $HlandNursery) ||
                ($landKind == $HlandUmishuto) ||
                ($landKind == $HlandFrocity) ||
                ($landKind == $HlandOilCity) ||
                ($landKind == $HlandUmicity) ||
                ($landKind == $HlandOil) ||
                ($landKind == $HlandUmiamu)
                                            ) {
            logMeteo($id, $name, $lName, $point, "��<B>$lName</B>��������");

        } elsif($landKind == $HlandMonster) {
            logMeteoMonster($id, $name, $lName, $point);

        } elsif(($landKind == $HlandSea) || ($landKind == $HlandIce)) {
            # ����
            logMeteo($id, $name, $lName, $point, "�����줬�������");

        } else {

            if (random(100) < 20) {
                logMeteo($id, $name, $lName, $point, "��<B>$lName</B>�Ͼä�����");
                $land->[$x][$y] = $HlandWaste;
                $landValue->[$x][$y] = 2;
                $landValue2->[$x][$y] = 0;
                $landValue3->[$x][$y] = 0;
                next;

            }else{

                logMeteo($id, $name, $lName, $point, "�����Ӥ����פ�");
            }
        }
        $land->[$x][$y] = $HlandSea;
        $landValue->[$x][$y] = 0;
        $landValue2->[$x][$y] = 0;
        if (random(1000) < 50) {
            $land->[$x][$y] = $HlandMonument;
            $landValue->[$x][$y] = 79;
            $landValue2->[$x][$y] = 0;
            $landValue3->[$x][$y] = 0;
        }
    }

}


#----------------------------------------------------------------------
sub BigMissileRoutine {
    my($island) = @_;

    # ����ߥ�����Ƚ��
    while($island->{'bigmissile'}) {
        $island->{'bigmissile'}--;
        my($x, $y, $landKind, $lv, $point);

        # �
        $x = random($HislandSize);
        $y = random($HislandSize);
        $landKind = $land->[$x][$y];
        $lv = $landValue->[$x][$y];
        $point = "($x, $y)";

        # ��å�����
        logMonDamage($id, $name, $point);

        # �����ﳲ�롼����
        wideDamage($id, $name, $land, $landValue, $x, $y);
    }

}


#----------------------------------------------------------------------
# ����
#----------------------------------------------------------------------
sub Flood {
    my ($island) = @_;

    {
        my ($chain) = $island->{'weather_chain'};
        my ($weather) = $island->{'weather'};

        if (   ($weather == $HWeather_Rain)
            && ($chain > 5) ) {

            my ($name) = islandName($island);
            my ($id) = $island->{'id'};
            my ($land) = $island->{'land'};
            my ($landValue) = $island->{'landValue'};
            my ($landValue2) = $island->{'landValue2'};
            my ($landValue3) = $island->{'landValue3'};

            my ($par) = $chain;
            if (random(100) < $par) {

                logOut("${HtagName_}${name}${H_tagName}���絬�Ϥ�${HtagDisaster_}����${H_tagDisaster}��ȯ������",$id);

                my ($i, $sx, $sy);
                my ($lk);
                my ($lv, $lv2);
                my ($tar_landname);
                my ($tar_pos);
                for ($i = 0; $i < $HpointNumber; $i++) {
                    $sx = $Hrpx[$i];
                    $sy = $Hrpy[$i];

                    $tar_pos = "($sx, $sy)";

                    if ( !countAround($land, $sx, $sy, 7, $HlandForest) ) {

                        $lk = $land->[$sx][$sy];
                        $lv = $landValue->[$sx][$sy];
                        $lv2 = $landValue2->[$sx][$sy];
                        $tar_landname = landName($lk, $lv, $lv2);


                        if (   ($lk == $HlandSea) && ($lv)      # ����
                            && (random(100) < 50) ) {

                            logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}����${H_tagDisaster}�ˤ���ﳲ������ޤ�����");
                            $landValue->[$sx][$sy] = 0;         # ����
                            $landValue2->[$sx][$sy] = 0;
                            $landValue3->[$sx][$sy] = 0;
                        }
                        elsif (   ($lk == $HlandSunahama) && (!$lv)     # ����
                               && (random(100) < 50) ) {

                            logDamageAny($id, $name, $tar_landname, $tar_pos, "����������ߤޤ�����");
                            $land->[$sx][$sy] = $HlandSea;
                            $landValue->[$sx][$sy] = 1;
                            $landValue2->[$sx][$sy] = 0;
                            $landValue3->[$sx][$sy] = 0;
                        }
                        elsif (   ($lk == $HlandMinato)
                               && (random(100) < 2) ) {

                            $lv -= random(20)+1;

                            if ($lv < 0) {

                                logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}����${H_tagDisaster}�ˤ����Ǥ��ޤ�����");
                                $land->[$sx][$sy] = $HlandSea;
                                $landValue->[$sx][$sy] = 1;
                                $landValue2->[$sx][$sy] = 0;
                                $landValue3->[$sx][$sy] = 0;

                            }else{
                                logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}����${H_tagDisaster}�ˤ���ﳲ������ޤ�����");
                                $landValue->[$sx][$sy] = $lv;
                            }
                        }
                        elsif (   (   ($lk == $HlandMountain)
                                   && ($lv > 0) )
                               && (random(100) < 2)
                                                    ) {

                            $lv -= random(20)+1;

                            if ($lv < 0) {
                                logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}����${H_tagDisaster}�ˤ����Ǥ��ޤ�����");
                                $landValue->[$sx][$sy] = 0;
                                $landValue2->[$sx][$sy] = 0;
                                $landValue3->[$sx][$sy] = 0;

                            }else{
                                logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}����${H_tagDisaster}�ˤ���ﳲ������ޤ�����");
                                $landValue->[$sx][$sy] = $lv;
                            }
                        }
                        elsif (   (   ($lk == $HlandTown)
                                   || ($lk == $HlandNewtown)
                                   || ($lk == $HlandBigtown)
                                   || ($lk == $HlandFactory)
                                   || (($lk == $HlandFoodim) && ($lv < 480))
                                   || ($lk == $HlandRizort)
                                   || ($lk == $HlandInaka)
                                                            )
                               && (random(100) < 2) ) {

                            $lv -= random(6)+1;

                            if ($lv < 0) {
                                logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}����${H_tagDisaster}�ˤ����Ǥ��ޤ�����");
                                $landValue->[$sx][$sy] = 0;
                                $landValue2->[$sx][$sy] = 0;
                                $landValue3->[$sx][$sy] = 0;

                            }else{
                                logDamageAny($id, $name, $tar_landname, $tar_pos, "${HtagDisaster_}����${H_tagDisaster}�ˤ���ﳲ������ޤ�����");
                                $landValue->[$sx][$sy] = $lv;
                            }
                        }
                        elsif (   (   ($lk == $HlandFrocity)
                                   || ($lk == $HlandOilCity)
                                   || ($lk == $HlandUmicity)
                                                            )
                               && (random(100) < 2) ) {

                            $lv -= random(30)+7;

                            if ($lv < 0) {
                                logDamageAny($id, $name, landName($lk, $lv, $lv2), "($sx, $sy)", "${HtagDisaster_}����${H_tagDisaster}�ˤ����Ǥ��ޤ�����");
                                $land->[$sx][$sy] = $HlandSea;
                                $landValue->[$sx][$sy] = 0;
                                $landValue2->[$sx][$sy] = 0;
                                $landValue3->[$sx][$sy] = 0;

                            }else{
                                logDamageAny($id, $name, landName($lk, $lv, $lv2), "($sx, $sy)", "${HtagDisaster_}����${H_tagDisaster}�ˤ���ﳲ������ޤ�����");
                                $landValue->[$sx][$sy] = $lv;
                            }
                        }
                    }
                }
            }
        }
    }

}



#----------------------------------------------------------------------
# ʮ��Ƚ��
#----------------------------------------------------------------------
sub Volcano {
    my($island, $x,$y) = @_;

    my($name) = islandName($island);
    my($id) = $island->{'id'};
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($landValue2) = $island->{'landValue2'};

    {
        my($sx, $sy, $i, $landKind, $lv, $point);

        $landKind = $land->[$x][$y];
        $lv = $landValue->[$x][$y];
        $point = "($x, $y)";

            logEruption($id, $name, landName($landKind, $lv,$landValue2->[$x][$y]), $point);
            $land->[$x][$y] = $HlandMountain;
            $landValue->[$x][$y] = 0;
            if (random(1000) < 100) {
                $land->[$x][$y] = $HlandMonument;
                $landValue->[$x][$y] = 75;          # ����
                $landValue2->[$x][$y] = 0;
            } elsif (random(1000) < 50) {
                $land->[$x][$y] = $HlandMonument;
                $landValue->[$x][$y] = 78;          # ����01
                $landValue2->[$x][$y] = 0;
            }

        for($i = 1; $i < 7; $i++) {
            $sx = $x + $ax[$i];
            $sy = $y + $ay[$i];

            # �Ԥˤ�����Ĵ��
            $sx-- if(!($sy % 2) && ($y % 2));

            if (($sx >= 0) && ($sx < $HislandSize) && ($sy >= 0) && ($sy < $HislandSize)) {
                # �ϰ���ξ��
                $landKind = $land->[$sx][$sy];
                $lv = $landValue->[$sx][$sy];
                $point = "($sx, $sy)";
                if (   ($landKind == $HlandSea)
                    || ($landKind == $HlandOil)
                    || ($landKind == $HlandFune)
                    || ($landKind == $HlandUmiamu)
                    || ($landKind == $HlandIce)
                    || ($landKind == $HlandFrocity)
                    || ($landKind == $HlandUmishuto)
                    || ($landKind == $HlandSeacity)
                    || ($landKind == $HlandSeatown)
                    || ($landKind == $HlandSbase)
                                                    ) {
                    # ���ξ��
                    if(($lv == 1) || ($landKind == $HlandIce)) {
                        # ����
                        logEruption2($id, $name, landName($landKind, $lv,$landValue2->[$sx][$sy]), $point, "Φ�Ϥˤʤ�ޤ�����");
                    } else {
                        logEruption2($id, $name, landName($landKind, $lv,$landValue2->[$sx][$sy]), $point, "���줬δ���������ˤʤ�ޤ�����");
                        $land->[$sx][$sy] = $HlandSea;
                        $landValue->[$sx][$sy] = 1;
                        next;
                    }
                } elsif(   ($landKind == $HlandMountain)
                        || ($landKind == $HlandMonster)
                        || ($landKind == $HlandGold)
                        || ($landKind == $HlandShrine)
                        || ($landKind == $HlandOnsen)
                        || ($landKind == $HlandWaste) ) {

                    if (   ($landKind == $HlandWaste)
                        && (!random(5))
                                        ) {
                        $land->[$sx][$sy] = $HlandYougan;
                        $landValue->[$sx][$sy] = 3 + random(10);
                        $landValue2->[$sx][$sy] = 0;
                    }

                    next;
                } else {
                    # ����ʳ��ξ��
                    logEruption2($id, $name, landName($landKind, $lv,$landValue2->[$sx][$sy]), $point, "���Ǥ��ޤ�����");
                }

                if (random(1000) < 50) {
                    $land->[$sx][$sy] = $HlandMonument;
                    $landValue->[$sx][$sy] = 75;
                    $landValue2->[$sx][$sy] = 0;
                } elsif (!random(5)) {
                    $land->[$sx][$sy] = $HlandYougan;
                    $landValue->[$sx][$sy] = 3 + random(10);
                    $landValue2->[$sx][$sy] = 0;
                }else{

                    SetWasteLand_Normal($island,$sx,$sy);       # HlandWaste
                }
            }
        }
    }
}


#----------------------------------------------------------------------
# �͹��������ͥ륮������
#----------------------------------------------------------------------
sub Satellite_Energy {
    my($island) = @_;

    my($name) = islandName($island);
    my($id) = $island->{'id'};

    # �͹��������ͥ륮������
    my($kind, $i);
    for($i = 1; $i < 7; $i++) {
        $kind = 'eis' . $i;
        if($island->{$kind}) {
            $island->{$kind} -= 1;
            $island->{$kind} -= random(2) if( !random(10) ) ;
            if($island->{$kind} < 1) {
                $island->{$kind} = 0;
                logEiseiEnd($id, $name, $HeiseiName[$i]);
            }
        }
    }
}

#----------------------------------------------------------------------
# �����ݽ���Ϥ��
#----------------------------------------------------------------------
sub Yakusyo_clean {
    my($island) = @_;

    my($name) = islandName($island);
    my($id) = $island->{'id'};
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($landValue2) = $island->{'landValue2'};

    # �����ݽ���Ϥ��
    if ($island->{'yaku'}){
        my($x, $y, $i);
        foreach $i (0..$pointNumber) {

            $x = $Hrpx[$i];
            $y = $Hrpy[$i];
            my ($landKind) = $land->[$x][$y];
            my ($lv) = $landValue->[$x][$y];
            my ($lv2) = $landValue2->[$x][$y];
            my ($lName) = landName($landKind, $lv,$lv2);

            my ($work) = 0;

            if ($landKind == $HlandWaste) {         #���ϡ���ꡡ���٥��

                if ( ( $island->{'yaku'} >= 2)
                    && ($island->{'money'} > $HYakusho_Narasi2)
                    && ($island->{'yaku_work'} & $HYakushoWorkSeiti) ) {

                    $land->[$x][$y] = $HlandPlains;
                    $landValue->[$x][$y] = 0;
                    $landValue2->[$x][$y] = 0;
                    $island->{'money'} -= $HYakusho_Narasi2;
                    $work = 1;
                }
            }
            if( ($land->[$x][$y] == $HlandPlains) && ($landValue->[$x][$y] == 0) ) {    #ʿ�� ���

                if (   ( $island->{'yaku'} > 0)
                    && ($island->{'money'} > $HYakusho_Narasi)
                    && ($island->{'yaku_work'} & $HYakushoWorkYotei) ) {

                    $land->[$x][$y] = $HlandPlains;
                    $landValue->[$x][$y] = 1;
                    $landValue2->[$x][$y] = 0;
                    $island->{'money'} -= $HYakusho_Narasi;
                    $work = 2;
                }
            }

            if ( $work == 1 ) {
                logYakusho_Prepare($id, $name, $lName ,"($x, $y)");
            }elsif( $work == 2){
                logYakusho_Plains2($id, $name, $lName ,"($x, $y)");
            }else{
                #�ʤˤ⤷�ʤ�
            }
        }
    }
}

#----------------------------------------------------------------------
# �޴ط�������Ψ����
#----------------------------------------------------------------------
sub doPrize {
    my($number, $island) = @_;

    # Ƴ����
    my ($name) = islandName($island);
    my ($id) = $island->{'id'};

    # ���������դ�Ƥ��鴹��
    if($island->{'food'} > $HmaximumFood) {
        my ($amarifood) = int($island->{'food'} - $HmaximumFood);
        my ($salefood) = int(($island->{'food'} - $HmaximumFood) / 10);
        $island->{'money'} += $salefood;
        food_product_Random_consumption($island , $amarifood);
        food_product_overheadcut($island);
        logFoodsute($id , $name ,$amarifood , $salefood);
    }

    # ���������å�
    $island->{'pika'} = $island->{'money'} - $island->{'oldMoney'};

    # �⤬���դ�Ƥ����ڤ�Τ�
    if($island->{'money'} > $HmaximumMoney) {

        my ($over) = $HmaximumMoney - $island->{'money'};

        $island->{'money'} = $HmaximumMoney;

        if (   ($island->{'eisei1'} > 0)
            && ($island->{'tax_income'} != -1)
            && ( $island->{'tax_income'} < ($over)) ) {

            if (random(100) < 5) {

                logZeikin_fuman($id , islandName($island));
            }
        }
    }

    # Ʊ����Ϣ����
    if ($HallyNumber) {
        my($gnp) = int($island->{'money'} - $island->{'oldMoney'} + ($island->{'food'} - $island->{'oldFood'})/10);
        foreach (@{$island->{'allyId'}}) {
            ${Hally[$HidToAllyNumber{$_}]->{'ext'}[2]} += $gnp;
        }
    }

    # �Ƽ���ͤ�׻�
    estimate($number);

    # �˱ɡ������
    my ($pop) = $island->{'pop'};
    my ($damage) = $island->{'oldPop'} - $pop - $island->{'migrate'}; # ��̱�Ϻ���ˤ���ʤ�
    my ($prize) = $island->{'prize'};
    my ($prize1, $prize2) = split(/\t/, $prize);
    $prize1 =~ /([0-9]*),([0-9]*),(.*)/;
    my ($flags) = $1;
    my ($monsters) = $2;
    my ($turns) = $3;

    $island->{'hamu'} = $island->{'pop'} - $island->{'oldPop'};
    $island->{'monta'} = $island->{'pts'} - $island->{'oldPts'};
    $island->{'old_food'} = $island->{'food'} - $island->{'lastFood'};
    $island->{'old_area'} = $island->{'area'} - $island->{'lastarea'};

    $island->{'gomi'} = $island->{'gomi'} + ($pop);

    $island->{'gomi'} = 0 if ($island->{'gomi'} < 0);
    $island->{'gomi'} = 0 if (!($HislandTurn % 50));

    # �˱ɾ�
    if((!($flags & 1)) &&  $pop >= 3000){
        $flags |= 1;
        logPrize($id, $name, $Hprize[1]);

        Sinden_Omaturi($island , 0 , 3001);

        # ����
        Jinja_Omaturi($island , 0 , 3001);

    } elsif((!($flags & 2)) &&  $pop >= 5000){
        $flags |= 2;
        logPrize($id, $name, $Hprize[2]);

        Sinden_Omaturi($island , 0 , 4001);

        # ����
        Jinja_Omaturi($island , 0 , 4001);

    } elsif((!($flags & 4)) &&  $pop >= 10000){
        $flags |= 4;
        logPrize($id, $name, $Hprize[3]);

        Sinden_Omaturi($island , 0 , 5001);

        # ����
        Jinja_Omaturi($island , 0 , 5001);
    }

    # �����
    if((!($flags & 64)) &&  $damage >= 500){
        $flags |= 64;
        logPrize($id, $name, $Hprize[7]);
    } elsif((!($flags & 128)) &&  $damage >= 1000){
        $flags |= 128;
        logPrize($id, $name, $Hprize[8]);
    } elsif((!($flags & 256)) &&  $damage >= 2000){
        $flags |= 256;
        logPrize($id, $name, $Hprize[9]);
    }

    $island->{'prize'} = "$flags,$monsters,$turns\t$prize2";
}


#----------------------------------------------------------------------
# �졼��������
#----------------------------------------------------------------------
sub LazerAttack {
    my($island, $tisland, $x, $y, ,$comName ,$monName) = @_;

    my ($id) = $island->{'id'};
    my ($target) = $tisland->{'id'};
    my ($tLand) = $tisland->{'land'};
    my ($tLandValue) = $tisland->{'landValue'};
    my ($tLandValue2) = $tisland->{'tLandValue2'};

    my ($tL) = $tLand->[$x][$y];
    my ($tLv) = $tLandValue->[$x][$y];
    my ($tLv2) = $tLandValue2->[$x][$y];
    my ($tLname) = landName($tL, $tLv,$tLv2);
    my ($point) = "($x, $y)";
    my ($tPoint) = "($x, $y)";
    my ($name) = islandName($island);
    my ($tName) = islandName($tisland);
    my ($tmKind, $tmName, $tmHp) = monsterSpec($tLv);

    my ($defcnt);
    my ($def_lz);
    $defcnt = 0;
    $def_lz = 0;

    $defcnt = countAround_DefBase($tLand,$tLandValue, $x, $y, 19, 2);

    if ( ($tL == $HlandDefence) ) {
        # �ɱҴ��Ϥ��Ф��빶��

        my ($deflv , $defHP) = GetDefenceSpec($tLv);
        my ($defLv);

        if ($defLv >= 2) {

            if ($defHP) {
                #HP��������Τ��ɸ�
                $def_lz = 1;
                $tLandValue->[$x][$y] -= ( 1 << $HDefenceHP_SHIFT) ;
            }
        }

    }elsif ($defcnt > 0){
        # �ɱҴ��Ϥ����ä�
        $def_lz = 1;

        my($i,$sx,$sy);
        # �ޤ����ɱҴ��Ϥ�õ��
        for($i = 1; $i < 19; $i++) {
            $sx = $x + $ax[$i];
            $sy = $y + $ay[$i];

            my ($defLv , $defHP) = GetDefenceSpec($tLandValue->[$sx][$sy]);

            if(   ($tLand->[$sx][$sy] == $HlandDefence)
               && ($defLv >= 2)
               && ($defHP > 0)
                                ){

                $tLandValue->[$sx][$sy] = 2 + ( ($defHP-1) << $HDefenceHP_SHIFT);
                last;
            }
        }
    }

    if ( $def_lz == 0 ) {
        if (   ($tL == $HlandSea)
            || ($tL == $HlandWaste)
            || ($tL == $HlandMountain)
            || ($tL == $HlandGold)
            || ($tL == $HlandShrine)
            || ($tL == $HlandSeacity)
            || ($tL == $HlandSeatown)
            || ($tL == $HlandUmishuto)
            || ($tL == $HlandUmiamu)
            || ($tL == $HlandSbase)
                                    ) {
            # ���̤Τʤ��Ϸ�
            logLzr($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "�Ȥ����ʤ�ޤ�����");

        } elsif (   ($tL == $HlandYougan)
                                            ) {
            logLzr($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "�����Ǯ���ʤ�ޤ�����");

        } elsif (   ($tL == $HlandOil)
                 || ($tL == $HlandNursery)
                 || ($tL == $HlandUmicity)
                 || ($tL == $HlandOilCity)
                 || ($tL == $HlandFrocity)
                 || ($tL == $HlandIce)
                 || ($tL == $HlandFune)
                                        ) {

            logLzr($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "�Ƥ�ʧ���ޤ�����");
            SetSeaLand_Normal($tisland,$x,$y);

        } elsif (($tL == $HlandMonster) && ($tmKind == 35)) {      # �Ҥᤤ�Τ��̵Ũ

            # ���̤Τʤ��Ϸ�
            logLzr($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "�֤��Ĥá��פȤӤä��ꤷ�ޤ�����");

        } elsif ($tL == $HlandOnsen) {

            logLzr($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "�Ƥ�ʧ���ޤ�����");
            SetMountain_Normal($tisland,$x,$y);

        } else {

            logLzr($id, $target, $name, $tName, $comName, $tLname, $point, $tPoint, "�Ƥ�ʧ���ޤ�����");
            if ((($tL == $HlandMonster) && (isSeaMonster($tmKind)))) {

                SetSeaLand_Normal($tisland,$x,$y);

            }else{

                SetWasteLand_Normal($tisland,$x,$y);
            }

            if (random(1000) < 100) {
                SetMonument_Normal($tisland,$x,$y,79);
            }
        }

    }else{

        logLzrFail($id, $target, $name, $tName, $comName, $tPoint);
    }
}


#----------------------------------------------------------------------
# ���Ϥ�����
#----------------------------------------------------------------------
sub is_SeaGroup_woSea {
    my($landKind) = @_;

    my ($ret) = 0;
    if ($landKind == $HlandSea) {

    }else{
        $ret = is_SeaGroup($landKind);
    }

    return ($ret);
}


#----------------------------------------------------------------------
sub is_SeaGroup {

    my ($landKind) = $_;

    if (   ($landKind == $HlandSea)
        || ($landKind == $HlandSbase)
        || ($landKind == $HlandSeatown)
        || ($landKind == $HlandSeacity)
        || ($landKind == $HlandUmicity)
        || ($landKind == $HlandOil)
        || ($landKind == $HlandOilCity)
        || ($landKind == $HlandUmishuto)
        || ($landKind == $HlandFune)
        || ($landKind == $HlandFrocity)
        || ($landKind == $HlandUmiamu)
        || ($landKind == $HlandIce)
                                     ) {
        return (1);
    }

    return (0);
}


#----------------------------------------------------------------------
# �����ﳲ�롼����
#----------------------------------------------------------------------
sub wideDamage {
    my($id, $name, $land, $landValue, $x, $y) = @_;

    my($sx, $sy, $i, $landKind, $landName, $lv, $lv2, $point);

    my ($island) = $Hislands[$HidToNumber{$id}];

    my ($landValue2) = $island->{'landValue2'};

    for($i = 0; $i < 19; $i++) {
        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # �Ԥˤ�����Ĵ��
        $sx-- if(!($sy % 2) && ($y % 2));
        # �ϰϳ�Ƚ��
        next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

        $landKind = $land->[$sx][$sy];
        $lv  = $landValue->[$sx][$sy];
        $lv2 = $landValue2->[$sx][$sy];
        $landName = landName($landKind, $lv,$lv2);
        $point = "($sx, $sy)";

        # �ϰϤˤ��ʬ��
        if ($i < 7) {
            # �濴�������1�إå���
            if ($landKind == $HlandSea) {
                $landValue->[$sx][$sy] = 0;
                $landValue2->[$sx][$sy] = 0;
                next;
            } elsif(is_SeaGroup_woSea($landKind)) {
                logDamageAny($id, $name, $landName, $point, "�׷���ʤ��ʤ�ޤ�����");
                $land->[$sx][$sy] = $HlandSea;
                $landValue->[$sx][$sy] = 0;

            } else {
                if ($landKind == $HlandMonster) {
                    my($mKind, $mName, $mHp) = monsterSpec($lv);
                    next if((($mKind == 20) && !$i) || (($mKind == 21) && !$i));
                    logWideDamageMonsterSea($id, $name, $landName, $point);
                } else {
                    logDamageAny($id, $name, $landName, $point, "<B>����</B>���ޤ�����");
                }
                $land->[$sx][$sy] = $HlandSea;
                $landValue2->[$sx][$sy] = 0;
                if(!$i) {
                    # ��
                    $landValue->[$sx][$sy] = 0;
                } else {
                    # ����
                    $landValue->[$sx][$sy] = 1;
                }
            }
        } else {
            # 2�إå���
            if( ($landKind == $HlandWaste) ||
                ($landKind == $HlandMountain) ||
                ($landKind == $HlandGold) ||
                ($landKind == $HlandShrine) ||
                ($landKind == $HlandSea) ||
                ($landKind == $HlandSbase) ||
                ($landKind == $HlandSeacity) ||
                ($landKind == $HlandSeatown) ||
                ($landKind == $HlandUmishuto) ||
                ($landKind == $HlandOil) ||
                ($landKind == $HlandUmiamu)) {
                # ���᡼���Τʤ��Ϸ�
                next;
            } elsif(   ($landKind == $HlandOnsen)
                                                    ) {
                logDamageAny($id, $name, $landName, $point, "�ä����Ӥޤ�����");
                SetMountain_Normal($island,$sx,$sy);

            } elsif(   ($landKind == $HlandIce)
                    || ($landKind == $HlandFune)
                    || ($landKind == $HlandFrocity)
                    || ($landKind == $HlandUmicity)
                    || ($landKind == $HlandOilCity)
                                                    ) {
                logDamageAny($id, $name, $landName, $point, "�ä����Ӥޤ�����");
                $land->[$sx][$sy] = $HlandSea;
                $landValue->[$sx][$sy] = 0;
                $landValue2->[$sx][$sy] = 0;

            } elsif($landKind == $HlandMonster) {
                logDamageAny($id, $name, $landName, $point, "�ä����Ӥޤ�����");
                SetWasteLand_Normal($island,$sx,$sy);
            } else {
                logDamageAny($id, $name, $landName, $point, "��֤ˤ���<B>����</B>�Ȳ����ޤ�����");
                SetWasteLand_Normal($island,$sx,$sy);
            }
        }
    }
}


#----------------------------------------------------------------------
# �����ﳲ�롼���󡦥ߥ�2
#----------------------------------------------------------------------
sub wideDamageli2 {
    my ($target, $tx, $ty) = @_;

    my ($tName, $tLand, $tLandValue, $tLandValue2, $tLandValue3);

    my ($tName) = islandName($target);

    $tLand       = $target->{'land'};
    $tLandValue  = $target->{'landValue'};
    $tLandValue2 = $target->{'landValue2'};
    $tLandValue3 = $target->{'landValue3'};

    my ($sx, $sy, $i, $tL, $landName, $tLv, $tLv2, $point);

    for($i = 0; $i < 19; $i++) {
        $sx = $tx + $ax[$i];
        $sy = $ty + $ay[$i];

        # �Ԥˤ�����Ĵ��
        $sx-- if(!($sy % 2) && ($ty % 2));
        # �ϰϳ�Ƚ��
        next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

        $tL = $tLand->[$sx][$sy];
        $tLv = $tLandValue->[$sx][$sy];
        $tLv2 = $tLandValue2->[$sx][$sy];
        $landName = landName($tL, $tLv, $tLv2);
        $point = "($sx, $sy)";

        if (   ($tL == $HlandSea)
            || ($tL == $HlandWaste)
            || ($tL == $HlandSeacity)
            || ($tL == $HlandSeatown)
            || ($tL == $HlandUmishuto)
            || ($tL == $HlandUmiamu)
            || ($tL == $HlandSbase) ) {
            next;

        } elsif(   ($tL == $HlandFune)
                || ($tL == $HlandFrocity)
                || ($tL == $HlandUmicity)
                || ($tL == $HlandOilCity)
                || ($tL == $HlandOil) ) {
            logDamageAny($target, $tName, $landName, $point, "�ä����Ӥޤ�����");
            SetSeaLand_Normal($target,$sx,$sy);

        } elsif (   ($tL == $HlandIce)
                 || ($tL == $HlandSeki)
                 || ($tL == $HlandNursery) ) {
            logDamageAny($target, $tName, $landName, $point, "�ä����Ӥޤ�����");
            SetSeaShallowLand($target,$sx,$sy);

        }
        elsif ($tL == $HlandMonster) {

            my ($mKind, $mName, $mHp) = monsterSpec($lv);
            logDamageAny($target, $tName, $landName, $point, "�ä����Ӥޤ�����");
            if (isSeaMonster($mKind)) {
                SetSeaLand_Normal($target,$sx,$sy);
            }
            else {
                SetWasteLand_Normal($target,$sx,$sy);
            }
        }
        else {
            logDamageAny($target, $tName, $landName, $point, "��֤ˤ���<B>����</B>�Ȳ����ޤ�����");
            $tLand->[$sx][$sy] = $HlandWaste;
            SetWasteLand_Normal($target,$sx,$sy);
        }
    }
}


#----------------------------------------------------------------------
# �����ﳲ�롼���󡦥ߥ�
#----------------------------------------------------------------------
sub wideDamageli {

    my ($target, $tName, $tLand, $tLandValue, $tLandValue2, $tx, $ty) = @_;

    my ($sx, $sy, $i, $tL, $landName, $tLv, $tLv2, $point);

    for($i = 0; $i < 19; $i++) {
        $sx = $tx + $ax[$i];
        $sy = $ty + $ay[$i];

        # �Ԥˤ�����Ĵ��
        $sx-- if(!($sy % 2) && ($ty % 2));
        # �ϰϳ�Ƚ��
        next if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize));

        $tL = $tLand->[$sx][$sy];
        $tLv = $tLandValue->[$sx][$sy];
        $tLv2 = $tLandValue2->[$sx][$sy];
        $landName = landName($tL, $tLv, $tLv2);
        $point = "($sx, $sy)";

        if (   ($tL == $HlandSea)
            || ($tL == $HlandWaste)
            || ($tL == $HlandSeacity)
            || ($tL == $HlandSeatown)
            || ($tL == $HlandIce)
            || ($tL == $HlandUmishuto)
            || ($tL == $HlandUmiamu)
            || ($tL == $HlandSbase) ) {
            next;

        } elsif(   ($tL == $HlandFune)
                || ($tL == $HlandFrocity)
                || ($tL == $HlandUmicity)
                || ($tL == $HlandOilCity)
                || ($tL == $HlandOil)
                                            ) {
            logDamageAny($target, $tName, $landName, $point, "�ä����Ӥޤ�����");
            $tLand->[$sx][$sy] = $HlandSea;
            $tLandValue->[$sx][$sy] = 0;
            $tLandValue2->[$sx][$sy] = 0;

        } elsif($tL == $HlandMonster) {
            logDamageAny($target, $tName, $landName, $point, "�ä����Ӥޤ�����");
            $tLand->[$sx][$sy] = $HlandWaste;
            $tLandValue->[$sx][$sy] = 0;
            $tLandValue2->[$sx][$sy] = 0;

        } else {
            logDamageAny($target, $tName, $landName, $point, "��֤ˤ���<B>����</B>�Ȳ����ޤ�����");
            $tLand->[$sx][$sy] = $HlandWaste;
            $tLandValue->[$sx][$sy] = 0;
            $tLandValue2->[$sx][$sy] = 0;
        }
    }
}

#----------------------------------------------------------------------
# ����η�ʪ
#----------------------------------------------------------------------
sub isUnderSea {
    my ($land) = @_;

    if (   (0)
        || ($land == $HlandSbase)
        || ($land == $HlandSeacity)
        || ($land == $HlandUmiamu)
        || ($land == $HlandSeatown)
        || ($land == $HlandUmishuto)
                                        ) {
        return 1;
    }

    return 0;
}


#----------------------------------------------------------------------
# �Ϸ��θƤ���
#----------------------------------------------------------------------
sub landName2 {
    my ($island, $x, $y) = @_;

    my ($land) = $island->{'land'};
    my ($land_kind) = $land->[$x][$y];

    my ($landValue) = $island->{'landValue'};
    my ($lv) = $landValue->[$x][$y];

    my ($landValue2) = $island->{'landValue2'};
    my ($lv2) = $landValue2->[$x][$y];

    my ($landValue3) = $island->{'landValue3'};
    my ($lv3) = $landValue3->[$x][$y];

    return landName($land , $lv, $lv2 , $lv3);
}

sub landName {
    my ($land, $lv, $lv2) = @_;

    if($land == $HlandSea) {
        if($lv == 1) {
            return '����';
        } else {
            return '��';
        }
    } elsif($land == $HlandIce) {
        if($lv > 0) {
            return 'ŷ���������Ⱦ�';
        } else {
            return 'ɹ��';
        }
    } elsif($land == $HlandWaste) {
        return '����';
    } elsif($land == $HlandInaka) {
        return '���ʤ�';
    } elsif($land == $HlandPlains) {
        return 'ʿ��';
    } elsif($land == $HlandTown) {
        if($lv < 30) {
            return '¼';
        } elsif($lv < 100) {
            return 'Į';
        } else {
            return '�Ի�';
        }
    } elsif($land == $HlandProcity) {
        return '�ɺ��Ի�';
    } elsif($land == $HlandNewtown) {
        return '�˥塼������';
    } elsif($land == $HlandBigtown) {
        return '�����Ի�';
    } elsif($land == $HlandBettown) {
        return '�������Ի�';
    } elsif($land == $HlandSeatown) {
        return '���쿷�Ի�';
    } elsif($land == $HlandRizort) {
        return '�꥾������';
    } elsif($land == $HlandBigRizort) {
        return '�׳��꥾���ȥۥƥ�';
    } elsif($land == $HlandShuto) {
        return '����';
    } elsif($land == $HlandUmishuto) {
        return '�������';
    } elsif($land == $HlandForest) {
        return '��';
    } elsif($land == $HlandFarm) {
        return '����';
    } elsif($land == $HlandFoodim) {
        if($lv < 480) {
            return '��ʪ�����';
        } else {
            return '�ɺҷ���ʪ�����';
        }
    } elsif($land == $HlandFarmchi) {
        return '�ܷܾ�';
    } elsif($land == $HlandFarmpic) {
        return '���ھ�';
    } elsif($land == $HlandFarmcow) {
        return '�Ҿ�';

    } elsif($land == $HlandCollege) {
        if($lv == 0) {
            return '�������';
        } elsif($lv == 1) {
            return '�������';
        } elsif($lv == 2) {
            return '������';
        } elsif($lv == 3) {
            return '�������';
        } elsif($lv == 4) {
            return '��ʪ���(�Ե���)';
        } elsif($lv == 98) {
            return '��ʪ���(�Ե���)';
        } elsif($lv == 96) {
            return '��ʪ���(�ж���)';
        } elsif($lv == 97) {
            return '��ʪ���(�ж���)';
        } elsif($lv == 99) {
            return '��ʪ���(��ư��)';
        } else {
            return '�������';
        }

    } elsif($land == $HlandFactory) {
        return '����';
    } elsif($land == $HlandHTFactory) {
        return '�ϥ��ƥ�¿���Ҵ��';
    } elsif($land == $HlandSHTF) {
        return '�ϥ��ƥ�¿���Ҵ�ȡ���';
    } elsif($land == $HlandBase) {
        return '�ߥ��������';
    } elsif($land == $HlandDefence) {
        if($lv == 1) {
            return '�ɱһ��ߡ���';
        } else {
            return '�ɱһ���';
        }
    } elsif($land == $HlandMountain) {
        if($lv) {
            return '�η���';
        } else {
            return '��';
        }
    } elsif($land == $HlandGold) {
        return '�⻳';
    } elsif($land == $HlandOnsen) {
        return '������';
    } elsif($land == $HlandMonster) {
        my($name) = (monsterSpec($lv))[1];
        return $name;
    } elsif($land == $HlandSbase) {
        return '�������';
    } elsif($land == $HlandSeacity) {
        return '�����Ի�';
    } elsif($land == $HlandOil) {
        return '��������';
    } elsif($land == $HlandEgg) {
        return '���ޥ�';
    } elsif($land == $HlandMonument) {
        return $HmonumentName[$lv];
    } elsif($land == $HlandHaribote) {
        return '�ϥ�ܥ�';
    } elsif($land == $HlandTrain) {
        return '��ϩ';
    } elsif($land == $HlandPark) {
        return 'ͷ����';
    } elsif($land == $HlandMinato) {
        return '��Į';
    } elsif($land == $HlandFune) {
        return $HfuneName[$lv];
    } elsif($land == $HlandFrocity) {
        return '�����Ի�';
    } elsif($land == $HlandBeachPark) {
        return '�������';
    } elsif($land == $HlandSunahama) {
        if($lv > 0) {
            return '����';
        }else{
            return '����';
        }
    } elsif($land == $HlandMine) {
        return '����';
    } elsif($land == $HlandNursery) {
        return '�ܿ���';
    } elsif($land == $HlandKyujo) {
        return '����';
    } elsif($land == $HlandKyujokai) {
        return '¿��Ū����������';
    } elsif($land == $HlandUmiamu) {
        return '�����ߤ�';
    } elsif($land == $HlandSeki) {
        return '�ؽ�';
    } elsif($land == $HlandRottenSea) {
        return '�峤';
    } elsif($land == $HlandUmicity) {
        return '���Ի�';
    } elsif($land == $HlandOilCity) {
        return '�����Ի�';
    } elsif($land == $HlandYakusho) {
        return '�����';
    } elsif($land == $HlandInoraLand) {
        return '���Τ����';
    } elsif($land == $HlandYougan) {
        return '�ϴ�����';
    } elsif($land == $HlandShrine) {
        if($lv) {
            return "���ο���(������${lv})";
        } else {
            return '���ο���';
        }
    } elsif($land == $HlandHouse) {
        if($lv == 0) {
            return '����';
        } elsif($lv == 1) {
            return '�ʰ׽���';
        } elsif($lv == 2) {
            return '����';
        } elsif($lv == 3) {
            return '��齻��';
        } elsif($lv == 4) {
            return '��š';
        } elsif($lv == 5) {
            return '���š';
        } elsif($lv == 6) {
            return '����š';
        } elsif($lv == 7) {
            return '��';
        } elsif($lv == 8) {
            return '���';
        } else {
            return '�����';
        }
    } elsif($land == $HlandBigFood) {
        my($Foodkind) = $lv >> $Food_Kind_Shift;
        my($FoodName) = $BigFoodName[$Foodkind];

        return $FoodName;
    } elsif($land == $HlandRocket) {
        return '���å�';
    } elsif($land == $HlandZoo) {
        return 'ưʪ��';
    } elsif($land == $HlandStation) {
        return '��';
    } elsif($land == $HlandOmamori) {
        return '���ޤ��';
    } elsif($land == $HlandFiredept) {
        return '���ɽ�';
    } elsif($land == $HlandKatorikun) {
        return '�ڤι�褯��';
    }
}


#----------------------------------------------------------------------
# �͸�����¾���ͤ򻻽�
#----------------------------------------------------------------------
sub estimate {
    my ($number) = $_[0];

    my ($island);
    $island = $Hislands[$number];

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};
    my ($landValue2) = $island->{'landValue2'};

    my ($pop, $area, $farm, $factory, $mountain)
     = (0, 0, 0, 0, 0, 0);
    my  ($monslive, $monslivetype, $hmonslivetype, $missiles)
      = (0, 0, 0, 0);
    my  ($kei, $rena, $fore, $tare, $zipro, $leje)
      = (0, 0, 0, 0, 0, 0);
    my  ($oil, $bas, $kyu, $amu, $par, $fim, $rot, $sci, $sba, $pro, $kin, $shr, $nto, $m26, $m27, $m17, $c21)
      = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    my  ($c11, $c13, $c28, $co0, $co1, $co2, $co3, $co4, $co5, $co99, $hou, $shu, $sin, $jin)
      = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    my  ($m74, $m75, $m76, $m77, $m78, $m79, $m84, $m93, $ky2, $htf, $m95)
      = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    my (@monspnt);
    my ($shtf) = (0);           # �ϥ��ƥ���
    my ($factoryHT) = 0;
    my ($yaku) = (0);
    my ($effect) = (0);
    my ($inoralandnum) = (0);   # ���Τ����
    my ($train) = (0);          # ��ϩ�ο�
    my ($zoocnt) = 0;              # ưʪ��
    my ($zoo_capacity) = 0;
    my ($forest_area) = 0;
    my ($lumber_area) = 0;
    my ($gomi_herasu) = 0;
    my ($park_work) = 0;
    my ($kome_work , $nazoniku_work , $yasai_work , $seafood_work)
        = (0,0,0,0);
    my ($kudamono_work , $sio_work)
        = (0,0);
    my ($hot) = 0;
    my ($mwork , $hwork , $lwork) = (0,0,0);
    my ($sea_build) = 0;
    my ($sightsee) = 0;

    my ($mshp, $msap, $msdp, $mssp, $mswin, $msexe, $tet) = split(/,/, $island->{'eisei5'});
    $tet = 0;
    # ������
    my ($i, $x, $y, $kind, $value,$value2);
    $island->{'BF_Flag'} = 0;           # ����Τ��ᡢ���BF�������Ƥ��� 
    $island->{'stadiumnum'} = 0;
    $island->{'defcnt'} = 0 ;
    $island->{'omamori'} = 0 ;
    $island->{'firedept'} = 0;
    $island->{'BF_Missile'} = 0;
    $island->{'yaku_work'} &= 0xFF ^ $HYakushoWorkExist ;

    my (@foodkind);

    foreach $i (0..$pointNumber) {
        $x = $Hrpx[$i];
        $y = $Hrpy[$i];
        $kind = $land->[$x][$y];
        $value2 = $landValue2->[$x][$y];
        $value = $landValue->[$x][$y];
        my($mKind, $mName, $mHp) = monsterSpec($value);

        if(   ($kind != $HlandSea)
           && ($kind != $HlandSbase)
           && ($kind != $HlandIce)
           && ($kind != $HlandFrocity)
           && ($kind != $HlandFune)
           && ($kind != $HlandNursery)
           && ($kind != $HlandUmicity)
           && ($kind != $HlandUmiamu)
           && ($kind != $HlandOilCity)
           && ($kind != $HlandSeacity)
           && ($kind != $HlandSeatown)
           && ($kind != $HlandUmishuto)
           && ($kind != $HlandOil) ){

            $yaku = $value if ($kind == $HlandYakusho);

            if ($kind == $HlandYakusho){
                $island->{'yaku_work'} |= $HYakushoWorkExist;
            }

            if (($kind == $HlandTown) ||
                ($kind == $HlandProcity) ||
                ($kind == $HlandMinato)) {
                # Į
                $area++;
                $pop += $value;
                $pro++ if($kind == $HlandProcity);

            } elsif (   ($kind == $HlandFarm)
                     || ($kind == $HlandFoodim)) {
                # ����
                $area++;
                $farm += $value;
                $fim++ if(($kind == $HlandFoodim) && ($value < 480));
                if($kind == $HlandFoodim) {
                    $nazoniku_work += $value;
                    $foodkind[5] = 1;
                }

                if (($kind == $HlandFarm)){
                    if($value2 == 1){
                        $kudamono_work += $value;
                        $foodkind[9] = 1;

                    } elsif($value2 == 2) {
                        $sio_work += $value;
                        $foodkind[10] = 1;

                    }else{
                        $kome_work += $value;
                        $foodkind[1] = 1;
                    }
                }

            } elsif($kind == $HlandInaka) {
                # ���ʤ�
                $area++;
                $pop += $value;
                my($fm) = int($value / 10) + 1 ;
                $farm += $fm;
                $yasai_work += $fm;
                $foodkind[0] = 1;


            } elsif($kind == $HlandFarmchi) {
                # �ܷܾ�
                $area++;
                $tare += $value;
                $factory += int($value/100)+1;
                $foodkind[2] = 1;

            } elsif($kind == $HlandFarmpic) {
                # ���ھ�
                $area++;
                $zipro += $value;
                $factory += int($value/80)+1;
                $foodkind[3] = 1;

            } elsif($kind == $HlandFarmcow) {
                # �Ҿ�
                $area++;
                $leje += $value;
                $factory += int($value/50)+1;
                $foodkind[4] = 1;

            } elsif(   ($kind == $HlandFactory)
                    || ($kind == $HlandHTFactory) ) {
                # ����
                $area++;
                $factory += $value;
                $htf++  if ($kind == $HlandHTFactory);

            } elsif ($kind == $HlandPark) {
                $area++;
                $par++;
                $park_work += $value;

            } elsif ($kind == $HlandSHTF) {
                $area++;
                $factoryHT += $value;
                $shtf++

            } elsif(($kind == $HlandMountain) ||
                    ($kind == $HlandGold)) {
                # �����⻳
                $area++;
                $mountain += $value;
                $kin++ if($kind == $HlandGold);

            } elsif($kind == $HlandForest) {
                # ��
                $area++;
                $forest_area++;
                $lumber_area++;
                $fore += $value;

            } elsif($kind == $HlandNewtown) {
                # �˥塼������
                $area++;
                $pop += $value;
                my ($nwork) =  int($value/15);
                $factory += $nwork;
                $nto++; # �˥塼������

            } elsif($kind == $HlandBigtown) {
                # �����Ի�
                $area++;
                $pop += $value;
                $mwork =  int($value/20);
                $lwork =  int($value/30);
                $factory += $mwork;
                $farm += $lwork;
                $yasai_work += $lwork;
                $foodkind[0] = 1;

            } elsif($kind == $HlandDefence) {
                $area++;
                $island->{'defcnt'} ++ ;

            } elsif($kind == $HlandBettown) {
                # �������Ի�
                $area++;
                $pop += $value;

            } elsif($kind == $HlandRizort) {
                # �꥾������
                $area++;
                $pop += $value;

            } elsif($kind == $HlandBigRizort) {
                # �꥾������
                $area++;
                $pop += $value;

            } elsif($kind == $HlandOnsen) {
                $area++;
                $pop += $value;
                $hot++;

            } elsif($kind == $HlandHouse) {
                $area++;
                $hou++;

            } elsif($kind == $HlandShuto) {
                $area++;
                $pop += $value;
                $shu++;

            } elsif($kind == $HlandBase) {
                # ����
                $area++;
                $bas += $value;
                $rena += $value;
                $missiles += expToLevel($kind, $value);

            } elsif( ($kind == $HlandRocket) ) {
                $area++;
                $m17++;

            } elsif( ($kind == $HlandKatorikun) ) {
                $area++;

            } elsif( ($kind == $HlandMonument) ) {
                $area++;
                $kei++;

                if(0) {

                } elsif($value == 26) {
                    $sin++;
                } elsif($value == 27) {
                    $jin++;

                } elsif($value == 42) {
                    # ��
                    $land->[$x][$y] = $HlandStation;
                    $landValue->[$x][$y] = 0;

                } elsif($value == 86) {
                    $m26++;
                } elsif($value == 87) {
                    $m27++;
                } elsif($value == 70) {     #gate
                    $island->{'BF_Flag'} = $HBF_MONSTER_HOUSE;
                    food_product_plus($island , 'yasai' ,500000);

                } elsif($value == 71) {     #gate
                    food_product_plus($island , 'yasai' ,500000);
                    $island->{'money'} = 2000000;
                    $pop++;
                    $island->{'trade_max'} = 1;

                } elsif($value == 74) {
                    $m74++;

                } elsif($value == 75) {
                    $m75++;
                } elsif($value == 76) {
                    $m76++;
                } elsif($value == 77) {
                    $m77++;
                } elsif($value == 78) {
                    $m78++;
                } elsif($value == 79) {
                    $m79++;
                } elsif($value == 84) {
                    $m84++;
                } elsif($value == 93) {
                    $m93++;

                } elsif($value == 95) {
                    $m95++;
                    $oil++;
                    $area--;    #���ʤΤǡ�++����ä�

                } elsif($value == 80) {
                    # �������֤�����
                    $land->[$x][$y] = $HlandEgg;
                    $landValue->[$x][$y] = 0;
                } elsif($value == 81) {
                    # �������֤�����
                    $land->[$x][$y] = $HlandEgg;
                    $landValue->[$x][$y] = 1;
                } elsif($value == 82) {
                    # �������֤�����
                    $land->[$x][$y] = $HlandEgg;
                    $landValue->[$x][$y] = 2;
                } elsif($value == 83) {
                    # �������֤�����
                    $land->[$x][$y] = $HlandEgg;
                    $landValue->[$x][$y] = 3;

                } elsif($value == 28) {
                    # �������֤�����
                    $landValue->[$x][$y] = 13;

                } elsif($value == 17) {
                    $m17++;
                    # �������֤�����
                    $land->[$x][$y] = $HlandRocket;
                    $landValue->[$x][$y] = 0;
                }

            } elsif($kind == $HlandCollege) {
                $area++;
                if ($value2 == 0) {
                    if($value == 0) {
                        $co0++;             #�������
                    } elsif($value == 1) {
                        $co1++;             #�������
                    } elsif($value == 2) {
                        $co0++;             #������
                        $co1++;
                        $co2++;
                    } elsif($value == 3) {
                        $co3++;             #�������
                    } elsif($value == 5) {
                        $co5++;             # �������
                    }

                }

                # ��ʪ���(����)
                if ($value == 99) {
                    $co99++;
                } elsif(($value == 98) || ($value == 97)){
                        $co4++;
                        $tet++;

                } elsif(($value == 4) || ($value == 96)) {
                        $co4++;             # ��ʪ���
                }

            } elsif ($kind == $HlandMonster) {
                $area++;
                my ($special) = $HmonsterSpecial[$mKind];
                if ($mKind == 11) {
                    $c11++;
                } elsif($mKind == 13) {
                    $c13++;
                } elsif($mKind == 21) {
                    $c21++;
                } elsif($mKind == 28) {
                    $c28++;
                } elsif($mKind == 30) {
                    $c28++;
                    $tet++;
                }
                if ($special == 17) {
                    $effect |= $g_Island_Chaff;
                }
                if ($special == 19) {
                    $effect |= $g_Island_Retro;
                }

                $monslive++;
                push(@monspnt, { x => $x, y => $y });
                $monslivetype = $mKind;

            } elsif($kind == $HlandKyujokai) {
                $area++;
                $kyu++;
                $ky2++;
                $island->{'stadiumnum'}++;

            } elsif($kind == $HlandKyujo) {
                $area++;
                $kyu++;

            } elsif($kind == $HlandRottenSea) {
                $area++;
                $rot++;

            } elsif($kind == $HlandOmamori) {
                $area++;
                $island->{'omamori'} = 1;

            } elsif($kind == $HlandYougan) {
                $area++;
            } elsif($kind == $HlandFiredept) {
                $area++;
                $island->{'firedept'}++;

            } elsif($kind == $HlandShrine) {
                $area++;
                $shr++;

            } elsif($kind == $HlandInoraLand) {
                $area++;
                $inoralandnum++;
                $park_work += $value;

            } elsif($kind == $HlandZoo) {
                $area++;
                $zoocnt++;
                $zoo_capacity += $value;

            }else{
                $area++;
            }

        } elsif($kind == $HlandNursery) {
            # �ܿ��������ΰ��
            $farm += $value;
            $seafood_work += $value;
            $foodkind[6] = 1;

        } elsif($kind == $HlandUmicity) {
            # ���Ի�
            $pop += $value;
            $mwork =  int($value/30);
            $hwork =  int($value/30);

            $factoryHT += $hwork;
            $factory += $mwork;
            $sea_build++;

        } elsif($kind == $HlandOilCity) {
            # �����Ի�
            $pop += $value;
            $mwork =  int($value/40);
            $oil++;
            $factory += $mwork;
            $sea_build++;

        } elsif($kind == $HlandUmiamu) {
            # �����ߤ�
            $amu++;
            $park_work += $value;
            $sea_build++;

        } elsif($kind == $HlandIce) {
            # ���Ϥʤ�

        } elsif($kind == $HlandSeacity) {
            # �����Ի�
            $pop += $value;
            $sci++;

        } elsif ($kind == $HlandFrocity) {
            $pro++;
            $pop += $value;

        } elsif ($kind == $HlandUmishuto) {
            $pop += $value;
            $shu++;
            $sea_build++;

        } elsif ($kind == $HlandTrain) {
            $train++;

        } elsif ($kind == $HlandBigFood) {
            $foodkind[8] = 1;

        } elsif($kind == $HlandSeatown) {
            # ���쿷�Ի�
            $pop += $value;
            my ($owork) =  int($value/40);
            $factory += $owork;
            $farm += $owork;
            $yasai_work += $owork;
            $sci += 2;
            $foodkind[0] = 1;
            $sea_build++;

        } elsif($kind == $HlandSbase) {
            # �������
            $bas += $value;
            $rena += $value;
            $sba++;
            $missiles += expToLevel($kind, $value);
            $sea_build++;

        } elsif($kind == $HlandOil) {
            $oil++;
            $sea_build++;

        } elsif($kind == $HlandFune) {
            $foodkind[7] = 1 if ($HfuneFood[$value]);
            #$sightsee++;
        }
    }

    # ͷ������ε��Ϥ򾦶Ȥ��ɲ�
    $factory += $park_work;

    # ����
    $island->{'pop'} = $pop;
    $island->{'area'} = $area;
    $island->{'farm'} = $farm;
    $island->{'factory'} = $factory;
    $island->{'park_work'} = $park_work;
    $island->{'factoryHT'} = $factoryHT;
    $island->{'mountain'} = $mountain;
    $island->{'yaku'}      = $yaku;
    $island->{'oil'} = $oil;
    $island->{'bas'} = $bas;
    $island->{'kyu'} = $kyu;
    $island->{'ky2'} = $ky2;
    $island->{'amu'} = $amu;
    $island->{'par'} = $par;
    $island->{'fim'} = $fim;
    $island->{'rot'} = $rot;
    $island->{'sci'} = $sci;
    $island->{'sba'} = $sba;
    $island->{'pro'} = $pro;
    $island->{'kin'} = $kin;
    $island->{'shr'} = $shr;
    $island->{'nto'} = $nto;
    $island->{'m26'} = $m26;
    $island->{'m27'} = $m27;
    $island->{'m17'} = $m17;
    $island->{'c11'} = $c11;
    $island->{'c13'} = $c13;
    $island->{'c21'} = $c21;
    $island->{'c28'} = $c28;
    $island->{'co0'} = $co0;
    $island->{'co1'} = $co1;
    $island->{'co2'} = $co2;
    $island->{'co3'} = $co3;
    $island->{'co4'} = $co4;
    $island->{'co5'} = $co5;
    $island->{'co99'} = $co99;
    $island->{'tet'} = $tet;
    $island->{'hot'} = $hot;
    $island->{'hou'} = $hou;
    $island->{'shu'} = $shu;
    $island->{'sin'} = $sin;
    $island->{'jin'} = $jin;
    $island->{'m74'} = $m74;
    $island->{'m75'} = $m75;
    $island->{'m76'} = $m76;
    $island->{'m77'} = $m77;
    $island->{'m78'} = $m78;
    $island->{'m79'} = $m79;
    $island->{'m84'} = $m84;
    $island->{'m93'} = $m93;
    $island->{'htf'} = $htf;        # �ϥ��ƥ�
    $island->{'shtf'} = $shtf;
    $island->{'inoraland'} = $inoralandnum;
    $island->{'effect'} = $effect;
    $island->{'train'} = $train;
    $island->{'zoo_cnt'} = $zoocnt;
    $island->{'zoo_capacity'} = $zoo_capacity;
    $island->{'gomi_herasu'} = 0;

    $island->{'kome_work'} = $kome_work;
    $island->{'seafood_work'} = $seafood_work;
    $island->{'nazoniku_work'} = $nazoniku_work;
    $island->{'yasai_work'} = $yasai_work;

    $island->{'kudamono_work'} = $kudamono_work;
    $island->{'sio_work'} = $sio_work;
    $island->{'sea_build'} = $sea_build;

    # ���β�Ƚ��
    $island->{'eisei1'} = 0 if(!$hou);

    # ����Ƚ��
    if(!$shu) {
        $island->{'shutomessage'} = 555;
    } elsif($island->{'shutomessage'} == 555) {
        $island->{'shutomessage'} = '';
    }

    # �̻��Ѹ���
    $island->{'eisei2'} = 0 if($island->{'eisei2'} < 0);

    my($sto, $std, $stk, $stwin, $stdrow, $stlose, $stwint, $stdrowt, $stloset, $styusho, $stshoka) = map { int($_) } split(/,/, $island->{'eisei4'});
    $kachiten = $stwin*3 + $stdrow;
    $island->{'kachiten'} = $kachiten;

    if(!$ky2) {
#       $island->{'eisei4'} = "0,0,0,0,0,0,0,0,0,0,0";
        $island->{'eisei4'} = "0,0,0,0,0,0,$stwint,$stdrowt,$stloset,$styusho,0";
    } else {
        $island->{'eisei4'} = "$sto,$std,$stk,$stwin,$stdrow,$stlose,$stwint,$stdrowt,$stloset,$styusho,$stshoka";
    }

    $island->{'monsterlive'} = $monslive; # ���ýи���
    $island->{'monsterlivetype'} = $monslivetype; # ���ýи�����
    $island->{'hmonsterlivetype'} = $hmonslivetype; # ���ýи�����
    $island->{'monspnt'} = \@monspnt; # ���ýи���ɸ
    $island->{'missiles'} = $missiles; # �ߥ�����ȯ�Ͳ�ǽ��

    $island->{'kei'} = $kei;
    $island->{'rena'} = $rena + $co2*100 + $co3*500 + $msexe;
    $island->{'fore'} = $fore;
    $island->{'tare'} = $tare;
    $island->{'zipro'} = $zipro;
    $island->{'leje'} = $leje;
    $island->{'forest_area'} = $forest_area;
    $island->{'lumber_area'} = $lumber_area;

    # �ޥ����å�Ƚ��
    if(!$co4 && !$co99 && !$c28) {
        $island->{'eisei5'} = "0,0,0,0,0,0,0";
    } elsif($co4 && !$mshp) {
        $island->{'eisei5'} = "3,5,5,5,0,0,0";
    } else {
        $island->{'eisei5'} = "$mshp,$msap,$msdp,$mssp,$mswin,$msexe,$tet";
    }
    $island->{'eisei6'} = "$c13,$shu,$m26,$m27,$m74,$m75,$m76,$m77,$m78,$m79,$m84,$m93,$m95";

    # ���ȼԿ�
    $island->{'unemployed'} = $pop - ($farm + $factory + $mountain + $factoryHT) * 10;

    my $ep1 = ($island->{'eis1'}) ?  (100 + $island->{'eis1'}*2) : 0;
    my $ep2 = ($island->{'eis2'}) ?  (300 + $island->{'eis2'}*2) : 0;
    my $ep3 = ($island->{'eis3'}) ?  (500 + $island->{'eis3'}*2) : 0;
    my $ep4 = ($island->{'eis4'}) ?  (900 + $island->{'eis4'}*2) : 0;
    my $ep5 = ($island->{'eis5'}) ? (1500 + $island->{'eis5'}*2) : 0;
    my $ep6 = ($island->{'eis6'}) ? (2000 + $island->{'eis6'}*2) : 0;

    $island->{'absent'} = 0 if ( ($land->[0][0] == $HlandMonument) && ($landValue->[0][0] == 71)) ;
    $island->{'absent'} = 0 if ($Hdebug);

    # �����ݥ����  2���ܤ���ݥ���ȤʤΤǡ����1�������Ȥ�
    my ($foodkindPoint) = -20;

    my ($FoodKind_cnt) = 0;
    foreach (@foodkind){
        $foodkindPoint += 20 if ($_);
        $FoodKind_cnt++ if ($_);
    }

    if ( $FoodKind_cnt > 2) {
        my ($fktemp) =$FoodKind_cnt - 2;
        $foodkindPoint += (((($fktemp * $fktemp) + $fktemp ) / 2) * 5);
    }

    # ưʪ��
    if (!$zoocnt) {
        $island->{'zoo'} = 0;
        $island->{'zoo_Mons_cnt'} = 0;
    }else{
        my ($zookazu, $zookazus, $m_syurui) = Get_ZooState($island);
        $island->{'zoo_Mons_cnt'} = $zookazu;
    }

    $foodkindPoint = 0 if ( $foodkindPoint < 0);

    # ���Point
    $island->{'pts'} = int(  $pop + $island->{'money'}/100
                           + $island->{'food'}/100 + ($farm*2 + $factory + $mountain*2 + int(($factoryHT * 25)/10))
                           + $bas + $area*5 + $sci*30 + $pro*20 + $sba*10 + $amu*10 + $oil*500
                           + $kin*500 + $m26*300 + $m27*200 + $m74*250 + $m75*250 + $m76*250
                           + $m77*250 + $m78*250 + $m79*250 + $m93*500 + int($tare/15)
                           + int($zipro/12) + int($leje/10)
                           + ($m95 * 500)
                           + $ep1 + $ep2 + $ep3 + $ep4 + $ep5 + $ep6 + $hou*500 + $foodkindPoint);

    $island->{'pts'} = 0 if( ($land->[0][0] == $HlandMonument) && ($landValue->[0][0] == 71)) ;
    $island->{'pts'} = 1 if( ($land->[0][0] == $HlandMonument) && ($landValue->[0][0] == 70)) ;

    $island->{'tha_diff'} = $island->{'pts'} - $island->{'tha_point'}

}


#----------------------------------------------------------------------
# ���ä� landvalue�򻻽�
#----------------------------------------------------------------------
sub Calc_MonsterLandValue {
    my ($mKind) = @_;

    return ($mKind << $Mons_Kind_Shift) + $HmonsterBHP[$mKind] + random($HmonsterDHP[$mKind]);
}


#----------------------------------------------------------------------
# ���ä� landvalue�򻻽�
#----------------------------------------------------------------------
sub Calc_MonsterLandValue_HP {
    my ($mKind , $hp) = @_;

    return ($mKind << $Mons_Kind_Shift) + $hp;
}


#----------------------------------------------------------------------
# ��ʡ�٤�Ĵ��
#----------------------------------------------------------------------
sub Calc_Happiness_Town {
    my ($island , $x , $y , $range) = @_;

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};

    my ($i,$sx,$sy);
    my ($pop) = 0;
    my ($score) = 0;

    for ($i = 0; $i < $range; $i++) {

        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # �Ԥˤ�����Ĵ��
        $sx-- if(!($sy % 2) && ($y % 2));

        if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)) {
            # �ϰϳ��ξ��
        } else {
            # �ϰ���ξ��
            if (grep {$_ == $land->[$sx][$sy]} @Htowns) {
                $pop += $landValue->[$sx][$sy];
            }
        }
    }

    $score += int(($pop/100));

    return ($score);
}


#----------------------------------------------------------------------
# �����Ȥ�̵ͭ��Ĵ�٤�
#----------------------------------------------------------------------
sub CheckGate {
    my ($island) = @_;

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};

    if ($land->[0][0] == $HlandMonument && $landValue->[0][0] == 70) {
        return 1;
    }

    return 0;
}


#----------------------------------------------------------------------
# �ޤ�����Ĺ��ޤȤ᤿�Ĥ��
#----------------------------------------------------------------------
sub Town_Growup {
    my($lv, $adpop, $adpop2, $stop ) = @_;

    # ��Ĺ
    if($lv < $stop ) {
        $lv += random($adpop) + 1;
        if($lv > $stop) {
            $lv = $stop;
        }

    } else {
        # �ԻԤˤʤ����Ĺ�٤�
        if($adpop2 > 0) {
            $lv += random($adpop2) + 1;
        }
    }

    return ($lv);
}


#----------------------------------------------------------------------
# �ϰ�����Ϸ��������(New)
#----------------------------------------------------------------------
sub countAround {
    my ($land, $x, $y, $range, @kind) = @_;

    my ($i, $count, $sx, $sy, @list);
    $count = 0;
    for($i = 0; $i < $range; $i++) {
        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # �Ԥˤ�����Ĵ��
        $sx-- if(!($sy % 2) && ($y % 2));

        if (($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)) {
            # �ϰϳ��ξ��
            # ���˲û�
            $list[$HlandSea]++;
        } else {
            # �ϰ���ξ��
            $list[$land->[$sx][$sy]]++;
        }
    }
    foreach (@kind){
        $count += ($list[$_]) ? ($list[$_]) : 0;
    }
    return $count;
}


#----------------------------------------------------------------------
# �ϰ���β��ä������
#----------------------------------------------------------------------
sub countAroundMonster_wo_Pet {
    my ($island, $x, $y, $range) = @_;
    my ($i, $count, $sx, $sy);
    $count = 0;

    my ($land) = $island->{'land'};
    my ($landValue) = $island->{'landValue'};

    my ($mKind, $mName, $mHp);
    for($i = 1; $i < $range; $i++) {
        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # �Ԥˤ�����Ĵ��
        $sx-- if(!($sy % 2) && ($y % 2));

        if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)) {
            # �ϰϳ��ξ��
        } else {

            # �ϰ���ξ��
            if ($land->[$sx][$sy] == $HlandMonster) {
                ($mKind, $mName, $mHp) = monsterSpec($landValue->[$sx][$sy]);
                unless (   ($mKind == $Mons_SuperTetra)
                        || ($mKind == 28)
                                                            ) {
                    return 1;
                }
            }
        }
    }

    return 0;
}


#----------------------------------------------------------------------
# �ϰ�����ɱҴ��Ϥ������(New)
#----------------------------------------------------------------------
sub countAround_DefBase {
    my($land, $landValue, $x, $y, $range, $tvalue) = @_;
    my($i, $count, $sx, $sy,$deflv);
    $count = 0;
    for($i = 0; $i < $range; $i++) {
        $sx = $x + $ax[$i];
        $sy = $y + $ay[$i];

        # �Ԥˤ�����Ĵ��
        $sx-- if(!($sy % 2) && ($y % 2));
        if(($sx < 0) || ($sx > $islandSize) || ($sy < 0) || ($sy > $islandSize)) {
            # �ϰϳ�
        } else {

            $deflv = $landValue->[$sx][$sy] & $HDefenceLevelMask ;
            if(   ($land->[$sx][$sy] == $HlandDefence)
               && ($deflv >= $tvalue) ) {
                $count++;
            }
        }
    }
    return $count;
}


#----------------------------------------------------------------------
# 0����(n - 1)�ޤǤο��������ŤĽФƤ���������
#----------------------------------------------------------------------
sub randomArray {
    my($n) = @_;
    my(@list, $i);

    # �����
    $n = 1 if($n == 0);
    @list = (0..$n-1);

    # ����åե�
    for ($i = $n; --$i; ) {
        my($j) = int(rand($i+1));
        next if($i == $j);
        @list[$i,$j] = @list[$j,$i];
    }

    return @list;
}


#----------------------------------------------------------------------
# �����¿�͸���Ͽ
#----------------------------------------------------------------------
sub islandReki {
    my($line, $i, $id, $pop, $turn, $name, $n, $island, @rekidai, $reki);
    my $j = 0;

    if(!open(RIN, "<${HdirName}/rekidai.dat")) {
        rename("${HdirName}/rekidai.tmp", "${HdirName}/rekidai.dat");
        if(!open(RIN, "${HdirName}/rekidai.dat")) {
            # �͸���˥�����
            my @idx = (0..$#Hislands);
            @idx = sort {   $Hislands[$b]->{'field'} <=> $Hislands[$a]->{'field'}
                         || $Hislands[$b]->{'pop'} <=> $Hislands[$a]->{'pop'}
                         || $a <=> $b } @idx;
            open(ROUT, ">${HdirName}/rekidai.tmp");
            foreach $i ($HbfieldNumber..$islandNumber) {# ��¸�����礹�٤Ƥ�Ͽ
                $island = $Hislands[$idx[$i]];
                $id = $island->{'id'};
                $name = islandName($island);
                $pop = $island->{'pop'};
                print ROUT "$id,$pop,$HislandTurn,$name\n";
            }
            close(ROUT);
            rename("${HdirName}/rekidai.tmp", "${HdirName}/rekidai.dat");
            return;
        }
    }

    while($line = <RIN>) {
        $line =~ /^([0-9]*),([0-9]*),([0-9]*),(.*)$/;
        ($id, $pop, $turn, $name) = ($1, $2, $3, $4);
        if(defined $HidToNumber{$id}) {
            $HidToNumberR{$id} = $j;
            $rekidai[$j]->{'id'} = $id;
        }
        $rekidai[$j]->{'pop'} = $pop;
        $rekidai[$j]->{'turn'} = $turn;
        $rekidai[$j]->{'name'} = $name;
        $j++;
    }
    close(RIN);

    foreach $i ($HbfieldNumber..$islandNumber) {
        $island = $Hislands[$i];
        $id = $island->{'id'};
        $name = $island->{'name'};
        $pop = $island->{'pop'};
        $n = $HidToNumberR{$id};
        if(defined $n) {
            if($pop > $rekidai[$n]->{'pop'}) {
                $rekidai[$n]->{'pop'} = $pop;
                $rekidai[$n]->{'turn'} = $HislandTurn;
                $rekidai[$n]->{'name'} = $name;
            }
        } else {
            $rekidai[$j]->{'id'} = $id;
            $rekidai[$j]->{'pop'} = $pop;
            $rekidai[$j]->{'turn'} = $HislandTurn;
            $rekidai[$j]->{'name'} = $name;
            $j++;
        }
    }

    # �͸���Ʊ���Ȥ���ľ���Υ�����ν��֤Τޤ�
    my @idx = (0..$#rekidai);
    @idx = sort { $rekidai[$b]->{'pop'} <=> $rekidai[$a]->{'pop'} || $a <=> $b } @idx;
    @rekidai = @rekidai[@idx];

    open(ROUT, ">${HdirName}/rekidai.tmp");
    my $recordNo = ($HmaxIsland < 15) ? 15 : $HmaxIsland;
    for($i = 0; $i < $recordNo; $i++) { # �������κ������Ʊ��������Ͽ�������15�硣
        $reki = $rekidai[$i];
        $n = $i + 1;
        if(defined $reki->{'pop'}) {
            ($id, $pop, $turn, $name) = ($reki->{'id'}, $reki->{'pop'}, $reki->{'turn'}, $reki->{'name'});
            print ROUT "$id,$pop,$turn,$name\n";
        }
    }
    close(ROUT);
    unlink("${HdirName}/rekidai.dat");
    rename("${HdirName}/rekidai.tmp", "${HdirName}/rekidai.dat");
}


#----------------------------------------------------------------------
# ����ޤȤ��
#----------------------------------------------------------------------
sub logMatome {
    my($island, $flag, $kind) = @_;

    my($sno, $i, $sArray, $spnt, $x, $y, $point);
    $sno = $island->{$kind};
    $point = '';
    if($sno > 0) {
        if($flag == 1) {
            $kind .= 'pnt';
            $sArray = $island->{$kind};
            for($i = 0; $i < $sno; $i++) {
                $spnt = $sArray->[$i];
                last if($spnt eq "");
                ($x, $y) = ($spnt->{x}, $spnt->{y});
                $point .= "($x, $y)";
                $point .= "<br>������" unless(($i+1)%20);
            }
        }
        $point .= "��<B>$sno����</B>" if($i > 1 || $flag != 1);
    }
    unless($point eq "") {
        if(($flag == 1) && ($sno > 1)) {
            logLandSucMatome($island->{'id'}, islandName($island), '����', "$point");
        } else {
            logLandSuc($island->{'id'}, islandName($island), '����', "$point");
        }
    }
}


#----------------------------------------------------------------------
# ���ؤν���
# ��1����:��å�����
# ��2����:������
# ��3����:���
# �̾��
#----------------------------------------------------------------------
sub logOut {
    push(@HlogPool,"0,$HislandTurn,$_[1],$_[2],$_[0]");
}

# �ٱ��
sub logLate {
    push(@HlateLogPool,"0,$HislandTurn,$_[1],$_[2],$_[0]");
}

# ��̩��
sub logSecret {
    push(@HsecretLogPool,"1,$HislandTurn,$_[1],$_[2],$_[0]");
}

# ��Ͽ��
sub logHistory {
    open(HOUT, ">>${HdirName}/hakojima.his");
    print HOUT "$HislandTurn,$_[0]\n";
    close(HOUT);
}

# Hakoniwa Cup��
sub logHcup {
    open(COUT, ">>${HdirName}/hakojima.lhc");
    print COUT "$HislandTurn,$_[0]\n";
    close(COUT);
}

#----------------------------------------------------------------------
# ��Ͽ��Ĵ��
#----------------------------------------------------------------------
sub logHistoryTrim {
    open(HIN, "${HdirName}/hakojima.his");
    my (@line, $l, $count);
    $count = 0;
    while($l = <HIN>) {
        chomp($l);
        push(@line, $l);
        $count++;
    }
    close(HIN);

    if($count > $HhistoryMax) {
        open(HOUT, ">${HdirName}/hakojima.his");
        my($i);
        for($i = ($count - $HhistoryMax); $i < $count; $i++) {
            print HOUT "$line[$i]\n";
        }
        close(HOUT);
    }
}

#----------------------------------------------------------------------
# Hakoniwa Cup��Ĵ��
#----------------------------------------------------------------------
sub logHcupTrim {
# Hakoniwa Cup���ݻ��Կ�(������ɽ���Τ��ᥫ�å�)
#$HhcMax = 300; # ͥ������ޤǺ�����ʤ��ʤ顢���줯�餤���ʡ�(�ɤ���100�ǳ���ڤ�륿���󤴤Ȥ����������ޤ�)
    open(CIN, "${HdirName}/hakojima.lhc");
    my(@line, $l, $count);
    $count = 0;
    while($l = <CIN>) {
        chomp($l);
        push(@line, $l);
        $count++;
    }
    close(CIN);

    if($count > $HhcMax) {
        open(COUT, ">${HdirName}/hakojima.lhc");
        my($i);
        for($i = ($count - $HhcMax); $i < $count; $i++) {
            print COUT "$line[$i]\n";
        }
        close(COUT);
    }
}

#----------------------------------------------------------------------
# ���񤭽Ф�
#----------------------------------------------------------------------
sub logFlush {
    open(LOUT, ">${HdirName}/hakojima.log0");

    # �����ս�ˤ��ƽ񤭽Ф�
    my($i);
    for($i = $#HsecretLogPool; $i >= 0; $i--) {
        print LOUT $HsecretLogPool[$i];
        print LOUT "\n";
    }
    for($i = $#HlateLogPool; $i >= 0; $i--) {
        print LOUT $HlateLogPool[$i];
        print LOUT "\n";
    }
    for($i = $#HlogPool; $i >= 0; $i--) {
        print LOUT $HlogPool[$i];
        print LOUT "\n";
    }
    close(LOUT);
}

#----------------------------------------------------------------------
# ���񤭽Ф�(ʬ�乹��)
#----------------------------------------------------------------------
sub tempLogFlush {

    open(LOUT, ">>${HdirName}/secret.tmp");
    # ���Τޤ޽񤭽Ф�
    my($i);
    for($i =0 ; $i <= $#HsecretLogPool; $i++) {
        print LOUT $HsecretLogPool[$i];
        print LOUT "\n";
    }
    close(LOUT);
    open(LOUT, ">>${HdirName}/late.tmp");
    for($i = 0; $i <= $#HlateLogPool; $i++) {
        print LOUT $HlateLogPool[$i];
        print LOUT "\n";
    }
    close(LOUT);
    open(LOUT, ">>${HdirName}/log.tmp");
    for($i = 0; $i <= $#HlogPool; $i++) {
        print LOUT $HlogPool[$i];
        print LOUT "\n";
    }
    close(LOUT);
}

#----------------------------------------------------------------------
# �ե������ݤ��ȥ��ԡ�
#----------------------------------------------------------------------
sub copy {
    my($src, $dest) = @_;

    open(FS, "<$src")  || die $!;
    open(FD, ">$dest") || die $!;
    binmode(FS); # Windows������Ǥ�ɬ��
    binmode(FD); # Windows������Ǥ�ɬ��

    my $buf;
    while (read(FS, $buf, 1024 * 8) > 0) {
        print FD $buf;
    }
    close(FD);
    close(FS);
}

#----------------------------------------------------------------------
# �ǥ��쥯�ȥ�ä�
#----------------------------------------------------------------------
sub myrmtree {
    my($dn) = @_;
    opendir(DIN, "$dn/");
    my($fileName);
    while($fileName = readdir(DIN)) {
        unlink("$dn/$fileName");
    }
    closedir(DIN);
    rmdir($dn);
}

1;
