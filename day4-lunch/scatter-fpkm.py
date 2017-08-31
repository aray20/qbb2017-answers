#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv (sys.argv[1], sep="\t") #893
df2 = pd.read_csv (sys.argv[2], sep="\t") #915

coi = "FPKM"
x = np.log(df[coi] + 1)
y = np.log(df2[coi] + 1)

plt.figure()

plt.scatter(x, y, color="#008080", alpha=0.15)
plt.suptitle("SRR072893 vs SRR072915 FPKM Values")
plt.xlim((0, 10))
plt.ylim((0,10))
plt.xlabel("SRR072893")
plt.ylabel("SRR072915")

plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, deg=1))(np.unique(x)))

plt.savefig(sys.argv[3] + ".png")
plt.close
