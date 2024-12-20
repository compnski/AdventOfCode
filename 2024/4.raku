my $mem = '
MMMSXXMASM
MSAMXMSMXM
ASXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'.trim;

my $fh = open "4.txt", :r;
$mem = $fh.slurp.chop.trim;
$fh.close;


my $lineLen = $mem.index("\n");

$mem ~~ s:g/\n//;

my $len = $mem.chars;

sub seq-by-offset($n, $len, $offset) {
	my $max = $len + $n%$offset  - ($len % $offset);
	$max = $max >= $len ?? $max - abs($offset) !! $max;
	if $offset > 0 {
		($n, { $_ + $offset } ...  $max)[^4]
	}else{
		($n, { $_ - $offset } ...  $max)[^4].reverse
	}
}

my $foundItems = set().SetHash;

my $bufMem = $mem.encode('ascii');

sub check(@seq) {
	next unless @seq[3] ~~ Int and @seq[0] ~~ Int;
	my $buf = Buf($bufMem[@seq]).decode();
	return $buf eq "XMAS"
}

my $found = 0;
for (0..$len-1) -> $n {
	for (1,-1,$lineLen,$lineLen+1,$lineLen-1,  -$lineLen,-$lineLen-1,-$lineLen+1) -> $offset {
		next if $offset == 1  and $n % $lineLen > $lineLen - 3;
		next if $offset == -1  and $n % $lineLen < 3;

		my @seq = seq-by-offset($n,$len, $offset);
		if check(@seq) {
			$foundItems.set(@seq);
			$found++;
		}
	}


}
say $found;
my %foundItems = $foundItems.hash;

for (0..$len/$lineLen-1) {
	say Buf([ $_ ~~ %foundItems ??  $bufMem[$_] !! 0x2E for [$++*$lineLen..(1+$++)*($lineLen)-1]]).decode()
}

say $found;


# for (0..$len-1) -> $n {
# 	my $max = $len + $n%11  - ($len % 11);
# 	$max = $max >= $len ?? $max - 11 !! $max;
# 	say $max, { $_ - 11 } ...  $n
# }

# for (0..$len-1) -> $n {
# 	my $max = $len + $n%10  - ($len % 10);
# 	$max = $max >= $len ?? $max - 10 !! $max;
# 	say $n, { $_ + 10 } ...  $max
# }

# for (0..$len-1) -> $n {
# 	my $max = $len + $n%10  - ($len % 10);
# 	$max = $max >= $len ?? $max - 10 !! $max;
# 	say $max, { $_ - 10 } ...  $n
# }

# for (0..$len-1) -> $n {
# 	my $max = $len + $n%1  - ($len % 1);
# 	$max = $max >= $len ?? $max - 1 !! $max;
# 	say $n, { $_ + 1 } ...  $max
# }

# for (0..$len-1) -> $n {
# 	my $max = $len + $n%1  - ($len % 1);
# 	$max = $max >= $len ?? $max - 1 !! $max;
# 	say $max, { $_ - 1 } ...  $n
# }
