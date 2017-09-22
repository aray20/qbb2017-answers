#!/usr/bin/env python

import sys
import fasta
import itertools
import operator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


contig = open(sys.argv[1])

lencount = 0

for line in contig:
    lencount += 1
    if lencount == 1:
        pass
    else:
        fields = line.rstrip("\r\n").split("\t")
        plt.plot([lencount,lencount+(float(fields[1])-float(fields[0]))],[float(fields[0]),float(fields[1])])
        lencount += float(fields[1])-float(fields[0])
    
    
plt.xlim(0,50000)
plt.ylim(0,100000)
plt.xlabel("Contigs")
plt.ylabel("Position")
#plt.savefig("Velvet plot")
#plt.savefig("Spades plot")
#plt.savefig("Spades nano plot")
#plt.savefig("Better coverage velvet plot")
plt.savefig("Better coverage spades plot")