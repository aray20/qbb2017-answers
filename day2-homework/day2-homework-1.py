#!/usr/bin/env python

import sys

fh = open(sys.argv[1])

string = "DROME"

for line in fh:
    if string in line:
        fields = line.rstrip("\r\n").split()
        if len(fields) != 4:
            continue
        gene_name = fields[3]
        gene_name2 = fields[2]
        print gene_name, gene_name2