#!/usr/bin/env python

import sys
fh = open(sys.argv[1])

totalspan = 0
genecnt = 0

for line in fh:
    line = line.rstrip()
    mylen = int(line)
    totalspan += mylen
    genecnt += 1
    
print "there are %d genes, with a total span of %d, average gene len is %f" % (genecnt, totalspan, float(totalspan)/genecnt)
#%f allows you to put float value