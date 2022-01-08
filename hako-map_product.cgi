#----------------------------------------------------------------------
# minimal97 の 箱庭諸島
# プロダクト・リストモードモジュール
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# メイン
sub ProductListMain {

    # 開放
    unlock();

    tempHeader_woTopmenu();

    # idから島番号を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};

    # なぜかその島がない場合
    if($HcurrentNumber eq '') {
        tempProblem();
        return;
    }

    # 名前の取得
    $HcurrentName = islandName($Hislands[$HcurrentNumber]);

    # 読み込み
    ProductListHead();

    ProductList_Pirnt();

    # フッタ出力
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
      <th $HbgTitleCell >${HtagTH_}物資${H_tagTH}</th>
      <th $HbgTitleCell >${HtagTH_}数量${H_tagTH}</th>
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
<p align='center'>${HtagBig_}<span class='Nret'>${HtagName_}「${HcurrentName}」${H_tagName}の</span><span class='Nret'>物資</span>${H_tagBig}</p>

END

}




1;
