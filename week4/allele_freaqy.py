#!/usr/bin/env python

import sys
import numpy as np
import math
import itertools
import matplotlib.pyplot as plt

vcf = open(sys.argv[1])

freq = []

for i in vcf:
    if i.startswith("#"):
        continue
    line = i.rstrip("\t\n").split()
    af = line[7]
    af1 = af[3:]
    if "," in af1:
        af2 = af1.split(",")
        for i in af2:
            freq.append(float(i))
    else:
        freq.append(float(af1))
        
plt.figure()
plt.hist(freq, bins=80)
plt.savefig("histo_allele.png")
plt.close()