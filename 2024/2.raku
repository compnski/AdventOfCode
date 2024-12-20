my $fh = open "2.txt", :r;
my $contents = $fh.slurp.chop;
$fh.close;


# my $contents = "7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9";


#say $contents;


sub to-deltas(@parts) {
    my @deltas = [];
    for @parts.kv -> $k,$v {
        #        say [$k,$v];
        if $k>0 {
            @deltas.append($v-@parts[$k-1])
        }
    }
    @deltas
}

sub find-unsafe(@deltas) {
    my $dir = @deltas[0] > 0;
    grep {
        my $k = $_.keys[0];
        my  $v = $_{$k};
        ($v > 0) != $dir || abs($v) > 3 || abs($v) < 1 }, @deltas.pairs;
}

my %resultCnt;
my @results = [];
for $contents.split("\n") -> $line {
    my @parts = $line.split(" ");
    my @deltas = to-deltas(@parts);
    my $bad = find-unsafe(@deltas);

    say @deltas;
    say $bad;
    say $bad.elems;
    my $result = $bad.elems ?? "broken" !! "okay";
    if $bad.elems >=1 {
        my $k = $bad[0].keys[0];
        say "k",$k;
        say @parts.grep: {$++ != $k};
        if find-unsafe(to-deltas(@parts.grep: {$++ != $k})).elems == 0 {
            $result = "fixed"
        }elsif find-unsafe(to-deltas(@parts.grep: {$++ != $k-1})).elems == 0 {
            $result = "fixed"
        }elsif find-unsafe(to-deltas(@parts.grep: {$++ != $k+1})).elems == 0 {
            $result = "fixed"
        }


    }


    @results.append($result);
    %resultCnt{$result} += 1;
}

say @results;
say %resultCnt;
