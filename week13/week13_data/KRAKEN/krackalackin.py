#!/usr/bin/env python

import sys

tax = {}

for line in open(sys.argv[1]):
    line = line.strip()
    cut_line = line.split("\t")
    column2 = cut_line[1]

    if column2 not in tax:
        tax[column2]=1
    else:
        tax[column2]+=1

for t in tax:
    count = tax[t]
    split_taxonomy = t.split("\t")
    taxonomy = "\t".join(split_taxonomy)


    
    
    
#
# for line in open(sys.argv[1]):
#     if line.strip().split("\t")[1] not in tax:
#         tax[line.strip().split("\t")[1]]=1
#     else:
#         tax[line.strip().split("\t")[1]]+=1
#
# for t in tax:
#     print str(tax[t]) + "\t" + "\t".join(t.split("."))