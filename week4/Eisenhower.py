#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

pca = open(sys.argv[1])

x = []
y = []

for line in pca: 
    split = line.rstrip("\r\n").split("\t")
    x.append(float(split[2]))
    y.append(float(split[3]))
    
plt.figure()
plt.scatter(x,y)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.savefig("pca_plot.png")
plt.close()