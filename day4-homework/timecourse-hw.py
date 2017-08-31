#!/usr/bin/env python

"""if you are using a for loop, you are doing something wrong."""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

transcript = "FBtr0331261"

df_samples = pd.read_csv( sys.argv[1] )
soif = df_samples["sex"] == "female"
soim = df_samples["sex"] == "male"

fpkms_f = []
fpkms_m = []

for sample in df_samples["sample"][soif]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv( fname, sep="\t")
    roi = df["t_name"] == transcript
    fpkms_f.append( df[roi]["FPKM"].values )

for sample in df_samples["sample"][soim]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv( fname, sep="\t")
    roi = df["t_name"] == transcript
    fpkms_m.append( df[roi]["FPKM"].values )

df_replicates = pd.read_csv( sys.argv[3] )
soif_rep = df_replicates["sex"] == "female"
soim_rep = df_replicates["sex"] == "male"

fpkms_f_rep = [None, None, None, None]
fpkms_m_rep = [None, None, None, None]


for sample in df_replicates["sample"][soif_rep]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv( fname, sep="\t")
    roi = df["t_name"] == transcript
    fpkms_f_rep.append( df[roi]["FPKM"].values )

for sample in df_replicates["sample"][soim_rep]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv( fname, sep="\t")
    roi = df["t_name"] == transcript
    fpkms_m_rep.append( df[roi]["FPKM"].values )
    
    
plt.figure()
plt.plot( fpkms_f, c='red', lw=3.5)
plt.plot( fpkms_m, c='blue', lw=3.5)
plt.plot( fpkms_f_rep, 'o', c='red', lw=2, markersize=10)
plt.plot( fpkms_m_rep, 'o', c='blue', lw=2, markersize=10)

plt.suptitle("Sxl", fontsize=25)
plt.xlabel( 'Developmental Stage', fontsize=15)
plt.ylabel( 'Fragments per Kilobase of Transcripts per Million (FPKM)', fontsize=15)
artists = []
plt.legend( ['Female', 'Male', 'Female Replicates', 'Male Replicates'], loc = 'center right', bbox_to_anchor = (1.5, 0.5), frameon = False, numpoints=1)
plt.xticks( range(8), ('10', '11', '12', '13', '14A', '14B', '14C', '14D'), rotation=90)
plt.gca().tick_params(direction='out', top='off', right='off')

plt.savefig( "timecourse.png", additional_artists = artists, bbox_inches = "tight")
plt.close()