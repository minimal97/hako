#----------------------------------------------------------------------
# minimal97 �� Ȣ�����
# �ץ�����ȡ��ꥹ�ȥ⡼�ɥ⥸�塼��
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# �ᥤ��
sub ProductListMain {

    # ����
    unlock();

    tempHeader_woTopmenu();

    # id�������ֹ�����
    $HcurrentNumber = $HidToNumber{$HcurrentID};

    # �ʤ��������礬�ʤ����
    if($HcurrentNumber eq '') {
        tempProblem();
        return;
    }

    # ̾���μ���
    $HcurrentName = islandName($Hislands[$HcurrentNumber]);

    # �ɤ߹���
    ProductListHead();

    ProductList_Pirnt();

    # �եå�����
    tempFooter();
}


#----------------------------------------------------------------------
sub ProductList_Pirnt {

    my ($limit);
    my ($product);
    $limit = $#HProduct_Food_hash_table;

    $HcurrentNumber = $HidToNumber{$HcurrentID};
    $island = $Hislands[$HcurrentNumber];

    out(<<END);
<hr>
<div>
  <table>
    <tr>
      <th $HbgTitleCell >${HtagTH_}ʪ��${H_tagTH}</th>
      <th $HbgTitleCell >${HtagTH_}����${H_tagTH}</th>
    </tr>
END
    foreach $product (@HProduct_Food_hash_table) {

        out(<<END);
    <tr>
      <td>$HProduct_Name{$product}</td><td>$island->{$product}$HProduct_unitName{$product}</td>
    </tr>

END
    }
    out(<<END);
  </table>
</div>
END
}


#----------------------------------------------------------------------
sub ProductListHead {

    out(<<END);
<p align='center'>${HtagBig_}<span class='Nret'>${HtagName_}��${HcurrentName}��${H_tagName}��</span><span class='Nret'>ʪ��</span>${H_tagBig}</p>

END

}




1;
