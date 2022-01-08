#----------------------------------------------------------------------
# 箱庭諸島
# 確定した便利な関数からわけてゆく
#----------------------------------------------------------------------
package html_template;

use strict;
use warnings;

#----------------------------------------------------------------------
# ヘッダー
sub PrintHeader {

    print <<"_H_E_A_D_E_R_";
<div id="LinkHead">
  <div class="HeadFootLink">
    <small>[<a title="現在は配布していません" href="http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html" target="_blank">箱庭諸島スクリプト配布元</a>]
      [<a class='Nret' HREF="../frm/">miniverse</a>]
      [<a class='Nret' TITLE="ソースコードを公開していただけました" HREF="http://uhyohyohyo.sakura.ne.jp/" target="_blank">多趣旨の国</a>]
      [<a class='Nret' TITLE="使うかもしれん" href="http://www.propel.ne.jp/~yysky/gallery/" target="_blank">箱庭諸島の素材屋さん</a>]
      [<a class='Nret' TITLE="使うかもしれん" href="https://hakopedia.uhyohyo.net/wiki/" target="_blank">箱庭ペディア</a>]
    </small>
  </div>
</div>
<hr>
_H_E_A_D_E_R_
}

#----------------------------------------------------------------------
# 何か問題発生
sub tempProblem2 {
    out(<<END);
<span class='big'>問題発生、とりあえず戻ってください。</span>
END
}

1;
