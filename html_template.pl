#----------------------------------------------------------------------
# Ȣ�����
# ���ꤷ�������ʴؿ�����櫓�Ƥ椯
#----------------------------------------------------------------------
package html_template;

use strict;
use warnings;

#----------------------------------------------------------------------
# �إå���
sub PrintHeader {

    print <<"_H_E_A_D_E_R_";
<div id="LinkHead">
  <div class="HeadFootLink">
    <small>[<a title="���ߤ����ۤ��Ƥ��ޤ���" href="http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html" target="_blank">Ȣ����祹����ץ����۸�</a>]
      [<a class='Nret' HREF="../frm/">miniverse</a>]
      [<a class='Nret' TITLE="�����������ɤ�������Ƥ��������ޤ���" HREF="http://uhyohyohyo.sakura.ne.jp/" target="_blank">¿��ݤι�</a>]
      [<a class='Nret' TITLE="�Ȥ����⤷���" href="http://www.propel.ne.jp/~yysky/gallery/" target="_blank">Ȣ�������Ǻರ����</a>]
      [<a class='Nret' TITLE="�Ȥ����⤷���" href="https://hakopedia.uhyohyo.net/wiki/" target="_blank">Ȣ��ڥǥ���</a>]
    </small>
  </div>
</div>
<hr>
_H_E_A_D_E_R_
}

#----------------------------------------------------------------------
# ��������ȯ��
sub tempProblem2 {
    out(<<END);
<span class='big'>����ȯ�����Ȥꤢ������äƤ���������</span>
END
}

1;
