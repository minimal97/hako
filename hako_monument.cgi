# すべての定数をここにまとめる！
require './init-server.cgi';
require './init-game.cgi';
require './hako-const.cgi';


#----------------------------------------------------------------------
# 
#----------------------------------------------------------------------
sub MonumentNumList {

    # 開放
    unlock();

    out(<<END);
<h1 align='center'>建設可能な記念碑</h1>

<script type="text/javascript">
<!--

function SetAmount(num) {
  window.opener.document.myForm.AMOUNT.options[num].selected = true;
  return true;
}

//-->
</script>

<table align='center'>
  <tr>
    <th class='TitleCell'>数量</th>
    <th class='TitleCell'>画像</th>
    <th class='TitleCell'>名前</th>
  </tr>

END

    my ($lp);
    my ($mo_name);
    my ($mo_img);


    for ($lp = 0; $lp < @HmonumentName; $lp++) {

        if ($HmonumentEnable[$lp] == 1) {

            $mo_name = $HmonumentName[$lp];
            $mo_img = $HmonumentImage[$lp];

            out(<<END);
  <tr>
    <td class='NameCell'>$lp</td>
    <td class='NameCell'>
      <a href='javascript:void(0);' onClick='SetAmount($lp);' style='text-decoration:none'>
        <img src="${HMapImgDir}${mo_img}" width='32' height='32' alt='$mo_name'></td>
      </a>
    <td class='NameCell'>$mo_name</td>
  </tr>
END
        }

    }


#                    $click_com[$m] .= "<a title='$l_cost' href='javascript:void(0);' onClick='window.opener.cominput(window.opener.document.myForm,6,$l_kind)' style='text-decoration:none'>$tag_s_s$HcomName[$l_kind]<font size='-1'>($l_cost)</font>$tag_s_e</a><br>\n";



    out(<<END);
</table>
END


}


1;
