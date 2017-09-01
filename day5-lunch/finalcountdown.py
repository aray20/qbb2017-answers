#!/usr/bin/env python

import sys
import pandas as pd
import statsmodels as sm
import numpy as np

df = pd.read_csv(sys.argv[1], sep="\t")

df["up"] = df["end"] + 500
df["down"] = df["end"] - 500
transcripts = df[ ["chr", "strand", "start", "end", "t_name", "up", "down"] ]

plus = transcripts["strand"] == "+"
df_plus = df[plus]


minus = transcripts["strand"] == "-"
df_minus = df[minus]

df_plus["up"] = df_plus["start"] - 500
df_plus["down"] = df_plus["start"] + 500

df_minus["up"] = df_minus["end"] - 500
df_minus["down"] = df_minus["end"] + 500

df = pd.concat([df_plus, df_minus])

coi = ["chr", "up", "down", "t_name"]

df[coi].to_csv(sys.argv[2], sep="\t", index=False, header=False)