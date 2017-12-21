#!/usr/bin/env python
"""
Use: ./realign.py 1000_logs.fa alignpt.fa
"""
import sys
import fasta
import itertools

nuc = open(sys.argv[1])
pt = open(sys.argv[2])
doc = open("alignew.fa", "w")

for (nident, nseq), (pident, pseq) in itertools.izip(fasta.FASTAReader(nuc), fasta.FASTAReader(pt)):
    position = 0
    for p in pseq:
        if p == "-":
            doc.write("---")
        else:
            doc.write(nseq[position:position + 3])
            position = position + 3
    doc.write("\n")
 #   print doc