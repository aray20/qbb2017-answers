#!/usr/bin/env python

import sys
import pandas as pd
import statsmodels.api as sm

df = pd.read_csv(sys.argv[1], sep="\t")
df_k4 = pd.read_csv(sys.argv[2], sep="\t", header=None)
df_k9 = pd.read_csv(sys.argv[3], sep="\t", header=None)
df_k27 = pd.read_csv(sys.argv[4], sep="\t", header=None)
df_k36 = pd.read_csv(sys.argv[5], sep="\t", header=None)


fpkm = df["FPKM"]
k4 = df_k4[5]
k9 = df_k9[5]
k27 = df_k27[5]
k36 = df_k36[5]

combine = pd.concat([k4, k9, k27, k36], axis=1)

#sm.ols y,x
model = sm.OLS( fpkm, combine)
results = model.fit()
print (results.summary())


# print fpkm, k4, k9, k27, k36