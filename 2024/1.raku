my $fh = open "1.txt", :r;
my $contents = $fh.slurp;
$fh.close;


my @l1 = [];
my @l2 = [];
for $contents.split("\n") -> $line {
    next unless $line;
    my ($a,$b) = $line.split("   ");
    @l1.append($a);
    @l2.append($b)
}

@l1 = @l1.sort();
@l2 = @l2.sort();


my %counts;
my $sum = 0;
for @l1 Z @l2 -> ($a, $b) {
    %counts{$b} += 1;
    $sum += abs $a - $b;
}

my $supersum = 0;
for @l1 -> $a {
    $supersum += $a * (%counts{$a} || 0);
}

say %counts;
say $sum;
say $supersum;
