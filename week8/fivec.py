#!/usr/bin/env/python

import sys
import numpy as np

"""
hhifive 5c-complete express Nora_Primers.bed -C Nora_ESC_male_E14.counts -P Nora

hifive 5c-heatmap Nora.fcp Nora_frag.heat -i Nora_frag.png -d fragment

hifive 5c-heatmap Nora.fcp Nora_enri.heat -i Nora_enri.png -d enrichment -b 0"""

data = np.load('Nora_enri.heat.npz')

print data.keys()