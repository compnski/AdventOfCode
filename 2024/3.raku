my $mem = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))';

my $fh = open "3.txt", :r;
$mem = $fh.slurp.chop;
$fh.close;



my $sum=0;
my $enabled = True;
for $mem ~~ m:g/ mul\((\d+)\,(\d+)\)|do|don\'t / -> $res {
    if $res eq "do" {
       $enabled = True
    }elsif $res eq "don't" {
       $enabled = False
    }elsif $enabled {
       $sum += $res[0]*$res[1]
    }
}
say $sum
