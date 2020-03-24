#!/usr/bin/perl 
use strict;
use warnings;

use CGI;
use File::Basename;
use HTTP::Date;

use constant MAX_FILE_SIZE => 400000;

use strict; #zip
use warnings; #zip
use Archive::Zip;  #zip

#===============================================
sub main_html();
sub filezipcmd();
sub image_list();
#===============================================

our $mode = 0;



our $cgi = CGI->new;
$cgi->charset("utf-8");
print $cgi->header(-charset => 'utf-8');
print $cgi->start_html(
    -encoding => 'utf-8',
    -title => 'uploader',
    );

print q|<H1>manu用アプロダ</H1>
|;

main_html();
filezipcmd();
image_list();

print $cgi->end_html, "\n";
exit(0);

#基本はここまで========================================================================


sub main_html() {

	print q|<form method="post" enctype="multipart/form-data">
	<input type="file" name="upload_file" /><br>
	<input type="submit" value="アップロード" NAME="upbtn"/>
	<input type="submit" value="test" NAME="test1"/>
	<input type="submit" value="zip" NAME="zip1"/>
	</form>
	|;

	my $line;
	$line = $cgi->param('test1');
	print $line if defined($line);

	# アップロードボタンが押された

	if ((defined $cgi->upload('upload_file') ) && ($cgi->param('upbtn') ne 'POST') ) {

		my $fh = $cgi->upload('upload_file') or die(qq(Invalid file handle returned.));
		my $name = $1 if $cgi->uploadInfo($fh)->{'Content-Disposition'} =~ /filename="(.*)"/;
		$name = $1 if $name =~ /.*\\(.*)/;
		my $namechk = 1 if lc($name) =~ /.html|.gif|.cgi|.zip/;
		my $err = 0 ;

		my $file_size = $ENV{'CONTENT_LENGTH'};
		if ( $namechk != 1) {
		    print "対応するファイルは　.jpg　.jpeg　.gif .png です！！";
		    $err = 1;
		}

		if ($err == 0) {
		    my $buf;

		    if ( $file_size < MAX_FILE_SIZE ) {
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


sub image_list(){

	my $script_name = basename $0;

	print '<table border="2">';
	print "    <th>name</th><th>size</th><th>pic</th>\n";
	opendir DIR, '.';
	for (readdir DIR) {
	    next if m|^\.|;
	    next if $_ eq $script_name;
	    next if lc($_) !~ /.html|.gif|.cgi|.zip/;
	    my $name = $_;
	    my $size = -s $name;
	    print qq|    <tr>
		<td><a href="$name">$name</a></td>
		<td align="right">$size</td>
	|;
        if ($name =~ /.gif/){
		    print "<td align=\"right\"><img src=\"./$name\"></td>" ;
        }else{
	    	print "<td align=\"right\">■</td>" ;
        }
		print qq|
	    </tr>
	|;
	}
	close(DIR);
	print "</table>";
}

#hakoniwa のバックアップ

sub filezipcmd(){

	my $zicmd;
	$zicmd = $cgi->param('zip1');

	if ((defined($zicmd)) && ( $zicmd eq "zip" )) {

		system "cd ../";
		system "zip -r backup.zip ./";
		system "cd hako";
		chmod(0777,"backup.zip");

	}


}
