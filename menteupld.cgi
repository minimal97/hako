#!/usr/bin/perl 
use strict;
use warnings;

use CGI;
use File::Basename;
use HTTP::Date;

use constant MAX_FILE_SIZE => 800000;

use strict; #zip
use warnings; #zip
use Archive::Zip;  #zip

#===============================================
sub main_html();
sub filezipcmd();
sub delete_file();
sub image_list();
#===============================================

our $mode = 0;

our $script_name = basename $0;


our $cgi = CGI->new;
$cgi->charset("utf-8");
print $cgi->header(-charset => 'utf-8');
print $cgi->start_html(
    -encoding => 'utf-8',
    -title => 'uploader',
    );

print q|<H1>manu用アプロダ</H1>
|;


#========
#
#========
our $delete_que;
our $dir;
our $dir_original;
$delete_que = $cgi->param('delete_target');
$dir_original = $cgi->param('dir');
$dir = ($dir_original) ? ($dir_original) . '/' : '';

if (   ($dir =~ /\.\./ )){
    $dir = '';
    $dir_original = '';
}

main_html();

my $delete_mode = 0 ;

if ( defined($delete_que) ){

    print $delete_que;
    $delete_mode = 1 ;

    my $delete_yes;
    $delete_yes = $cgi->param('yes');

    if ( defined($delete_yes) ){

        print $delete_que , "を削除しました<br>";
        print "<a href='./$script_name'>もどる</a>";
        $delete_mode = 1 ;

        if (-e $delete_que) {
            #ファイル削除
            unlink $delete_que;
        }else{
            #ファイルが無い場合はなにもしない
            print "ERR<br>";
        }

    }else{

        if (-e $delete_que) {

            print $delete_que , "を削除しますか？<br>";
            print qq|"<a href="./$script_name">もどる</a><br><br>"|;
            print qq|"<a href="./$script_name?yes=1&delete_target=$delete_que">はい</a>"|;

        }else{

            print "<br>",$delete_que , "は、既に削除されていたようです。";
            print qq|"<a href="./$script_name">もどる</a>"|;
        }
    }

}

if($delete_mode == 0){

    filezipcmd();
    image_list();
}


print $cgi->end_html, "$dir\n";

#END { system("/bin/ps -o rss -e -q $$"); }

exit(0);

#基本はここまで========================================================================


sub main_html() {

    my $zip = ($dir eq '') ? '<input type="submit" value="zip" NAME="zip1"/>' : '' ;
    my $backup = ($dir eq '') ? '<a href="./backup.zip">backup.zip</a><br>' : "<a href='./$script_name'>もどる</a><br>";

    print (<<END);
    <form method="post" enctype="multipart/form-data">
    <input type="file" name="upload_file" /><br>
    <input type="submit" value="アップロード" NAME="upbtn"/>
    <input type="submit" value="test" NAME="test1"/>
    <input type="hidden" value="$dir_original" NAME="dir"/>
    $zip
    </form>
    <a href="./data/hakojima.dat">hakojima.dat</a><br>
    <a href="./data/hakojima.log0">hakojima.log0</a>
    ${backup}
    <a href="./hako-main.cgi">main</a><br>
    <a href="./hako-mente.cgi">mente</a>$script_name
    $dir
END

	my $line;
	my $cwflag;
    $cwflag = 0;
	$line = $cgi->param('test1');
	$cwflag = 1 if defined($line);

    if ( $cwflag ) {

        print "test<br><a href='./ww.txt'>ワーニング</a><br>";
        system "perl -c -w hako-top.cgi >ww.txt";
        chmod(0777,"hako-main.cgi");
    }

	# アップロードボタンが押された

	if ((defined $cgi->upload('upload_file') ) && ($cgi->param('upbtn') ne 'POST') ) {

		my $fh = $cgi->upload('upload_file') or die(qq(Invalid file handle returned.));
		my $name = $1 if $cgi->uploadInfo($fh)->{'Content-Disposition'} =~ /filename="(.*)"/;
		$name = $1 if $name =~ /.*\\(.*)/;
		my $namechk = 1 if lc($name) =~ /.html|.gif|.cgi|.zip|.txt|.css|.log|.png|.dat/;
		my $err = 0 ;

		my $file_size = $ENV{'CONTENT_LENGTH'};

		if ( $namechk != 1) {
		    print "対応するファイルは　.jpg　.jpeg　.gif .png です！！";
		    $err = 1;
        }

        $name = $name;

		if ($err == 0) {
		    my $buf;

		    if ( $file_size < MAX_FILE_SIZE ) {
                chdir("/home/minimal97/www/hako/" . $dir);
		        open OUT, '>', $name or print $!;
		        binmode OUT;
		        while (read $fh, $buf, 1024) {
		            print OUT $buf;
		        }
		        close(OUT);
		        print "Upload!! : $name<br/>";
                if ($name =~ /.cgi/){
                    chmod(0777,$name);
                    print "chmod 777 $name <br/>"
                }
            }

           close($fh);
        }

    }
}


#========================================================================


sub image_list(){

	print '<table border="2">';
    print '<th>del</th><th>name</th>';
	print '<tr valign="top"><td>';
	print '<table border="2">';
	print "    <th>del</th><th>name</th><th>size</th><th>pic</th>\n";

    chdir("/home/minimal97/www/hako/" . $dir);
    my @file    = glob "*";
    my $name;
    foreach my $i (@file){

	    next if $i eq $script_name;

	    my $name = $i;
	    my $size = (-f $name) ? -s $name : '-';

        if (-f $name) {  #ファイルか

            print qq|    <tr>
        <td><a href="./menteupld.cgi?delete_target=$name">■</a></td>
        <td><a href="$name">$name</a></td>
        <td align="right">$size</td>
    |;

            if ($name =~ /.gif|.png/){
                print "<td align=\"right\"><img src=\"$dir$name\"></td>" ;
            }else{
                print "<td align=\"right\">-</td>" ;

            }

        }else{

            print qq|    <tr>
        <td><a href="./menteupld.cgi?delete_target=$name">■</a></td>
        <td><a href="./menteupld.cgi?dir=$dir$name">$name</a></td>
        <td align="right">$size</td>
    |;
            print "<td align=\"right\">◆</td>" ;
        }
        print qq|
        </tr>
    |;

    }


	print '</td></tr>';
	print "</table>";
}

#========================================================================
#hakoniwa のバックアップ

sub filezipcmd(){

	my $zicmd;
	$zicmd = $cgi->param('zip1');

	if ((defined($zicmd)) && ( $zicmd eq "zip" )) {
        unlink 'backup.zip';

		system "cd ../";
		system "zip -r backup.zip ./";
		system "cd hako";
		chmod(0777,"backup.zip");

	}


}
