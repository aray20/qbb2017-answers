#!/usr/bin/env python

import sys
import fasta
import operator

total_l = 0
contigs = []

for name, seq in fasta.FASTAReader( open(sys.argv[1] )):
    if len(seq) == 0:
        pass
    else:
        sub = [name, seq, len(seq)]
        total_l += len(seq)
        contigs.append(sub)
        
contigs = sorted(contigs, key=operator.itemgetter(2), reverse=True)

ldiv = float(total_l) / 2.0

tot = 0
for each in contigs:
    tot += each[2]
    if tot >= ldiv:
        n50 = each
        break

print 'num contigs = %d' % (len(contigs))
print 'max contig = %d' % (contigs [0][2])
print 'min contig = %d' % (contigs [-1][2])
print 'avg contig =%f' % ( float(total_l) / float(len(contigs)))
print 'n50 = %s' % (n50[2])