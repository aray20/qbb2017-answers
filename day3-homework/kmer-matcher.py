#!/usr/bin/env python

import sys
import fasta

subset = open(sys.argv[1]) #target
droyak = open(sys.argv[2]) #query

count = 0
k = 11
kmer_counts = {}

ident, sequence = fasta.FASTAReader (droyak).next()

for ident, sequence in fasta.FASTAReader( subset ):
    sequence = sequence.upper()
    for i in range ( 0, len(sequence) -k ):
        kmer1 = sequence[i:i+k]
        if kmer1 not in kmer_counts:
            kmer_counts[kmer1] = [(ident, i)]
        else:
            kmer_counts[kmer1].append((ident, i))
            
for ident, sequence in fasta.FASTAReader( droyak ):
    sequence = sequence.upper()
    for i in range ( 0, len(sequence) -k ):
        kmer2 = sequence[i:i+k]
        if kmer2 in kmer_counts:
            
            for value in kmer_counts[kmer2]:
                count += 1
                if count > 1000:
                    break
                print "\t".join((str(value[0]), str(value[1]), str(i), str(kmer2)))