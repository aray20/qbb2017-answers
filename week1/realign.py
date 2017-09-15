"""DISCLAIMER: THIS CODE IS NOT WORKING. IT IS PURELY FOR THE SAKE OF TEMPORARY SUBMISSION. 
GIVES ERROR THAT NO MODULE NAMED FASTA EVEN THOUGH IT IS IMPORTED."""


#!/usr/bin/env python

import FASTAParser
import sys
import itertools

nt = open(sys.argv[1]) #nucleotides --> 1000_homo.fa
pt = open(sys.argv[2]) #proteins --> alignment_pt.fa

nt_pt = open("alignment_nuc.fa","w")

for (nt_id, nt_seq), (pt_id, pt_seq) in itertools.izip(fasta.FASTAReader(nt), fasta.FASTAReader(pt)):
    nt_pt.write(nt_id + "\n")
    for aa in pt_seq:
        if aa == "-":
            nt_pt.write("---")
        else:
            nt_pt.write(nt_seq[:3])
            nt_seq = nt_seq[3:]

    nt_pt.write("\n")
