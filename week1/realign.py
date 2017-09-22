#!/usr/bin/env python

import fasta
import sys
import itertools

nt = open(sys.argv[1]) #1000_homo.fa
pt = open(sys.argv[2]) #alignment_pt.fa

nt_pt = open("alignment_nuc.fa", "w")

for (nt_id, nt_seq), (pt_id, pt_seq) in itertools.izip(fasta.FASTAReader(nt), fasta.FASTAReader(pt)):
    nt_pt.write(nt_id + "\n")
    for aa in pt_seq:
        if aa == "-":
            nt_pt.write("---")
        else:
            nt_pt.write(nt_seq[:3])
            nt_seq = nt_seq[3:]
        
    nt_pt.write("\n")