#!/usr/bin/env python

"""
Use: ./dsdn.py alignew.fa
"""

import sys
import fasta
from itertools import izip
import numpy as np
import scipy.stats as sp


base = ['T', 'C', 'A', 'G']
codon = [a+b+c for a in base for b in base for c in base]
amino_acid = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codon, amino_acid))


def codon_split(seq, n):
    return [seq[i:i+n] for i in range(0, len(seq), n)]

align = open(sys.argv[1])

refline = codon_split(align.readline(), 3)

dS = np.zeros(len(refline))
dN = np.zeros(len(refline))

for line in align:
    for index, (codon, ref) in enumerate(zip(codon_split(line, 3), refline)):
        if codon == ref:
            continue
        if not codon in codon_table or not ref in codon_table:
            continue
        if codon_table[codon] == codon_table[ref]:
            dS[index] += 1 
        else:
            dN[index] += 1 
            
d = dN - dS

for i in range(len(refline)):
    if dS[i] > 0:
        print ("%s \t %f \t %f" % (refline[i], float(dN[i])/dS[i], d[i]))