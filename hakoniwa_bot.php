<?php 
//API KeyとAccess Tokenの設定
define( 'C_TWITTER_KEY_CK', '*************************' );  //Consumer Key (API Key)
define( 'C_TWITTER_KEY_CS', '**************************************************' );  //Consumer Secret (API Secret)
define( 'C_TWITTER_KEY_AT', '**************************************************' );  //Access Token
define( 'C_TWITTER_KEY_ATS', '*********************************************' ); //Access Token Secret
 
//「twitteroauth」読み込み
require_once 'twitteroauth/autoload.php';

use Abraham\TwitterOAuth\TwitterOAuth;
 
// TwitterOAuthオブジェクト生成
$toa = new TwitterOAuth(constant('C_TWITTER_KEY_CK'),
                        constant('C_TWITTER_KEY_CS'),
                        constant('C_TWITTER_KEY_AT'),
                        constant('C_TWITTER_KEY_ATS'));

    if (isset($_GET['turn']) ) {
        $turn = htmlspecialchars( $_GET['turn'] , ENT_QUOTES);


        # 20ツイートさかのぼって削除する場合
        if (1) {
            $parameters = [
                'user_id' => 'ユーザーID' ,         # ユーザーID
                'count' => '20'                     # さかのぼるツイート数
            ];

            //投稿
            $result = $toa->get('statuses/user_timeline', $parameters);

            foreach ($result as $tw_obj) {

                if ( strcmp(substr($tw_obj->{'text'} , 0,22), "【自動】\n箱庭：") == 0) {

                    $del_param = [
                        'id' => $tw_obj->{'id_str'} ,
                        'trim_user' => 1
                    ];
                    $del_res = $toa->post('statuses/destroy', $del_param);
                }
            }
        }

//      $message = "【自動】\n箱庭：" . $turn . "ターンになりました。\nhttp://minimal97.mydns.jp:8123/hako/\n#箱庭諸島\n";
        // リダイレクト用
        $message = "【自動】\n箱庭：" . $turn . "ターンになりました。\n#箱庭諸島\n";


        $monster = "";
        if (isset($_GET['monster']) ) {

            $monster = htmlspecialchars( $_GET['monster'] , ENT_QUOTES);

            if ($monster != "-1") {

                $message = $message . "■どこかの島で怪獣がでました。\n";
            }
        }
        $message = $message . "箱庭諸島は無料で遊べるブラウザゲームです！";

        // ツイートするためのパラメータをセット
        $parameters = [
            'status' => $message
        ];

        //投稿
        $result = $toa->post('statuses/update', $parameters);

        // print ("OK");
    }


?>
