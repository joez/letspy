#!/usr/bin/env perl

use strict;
use v5.10;

my ($v, $c) = qw/[aeiou] [qwrtypsdfghjklzxcvbnm]/;
my @m = (<STDIN> =~ /(?<=$c)($v{2,})(?=$c)/ig);
say(@m ? join("\n", @m) : -1);
