#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np

from scipy.cluster.hierarchy import linkage, leaves_list
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt

"""use: ./cluster.py hema_data.txt"""

data_df = pd.read_csv(sys.argv[1], sep='\t')
labels = ['CFU', 'poly', 'unk', 'int', 'mys', 'mid']
data_df_oi = data_df[labels]
flipped = np.transpose(data_df_oi.values)
linkx, linky = linkage(data_df_oi.values), linkage(flipped)
leavesx, leavesy = leaves_list(linkx), leaves_list(linky)

transformed = data_df_oi.values[leavesx,: ][ :,leavesy]
labels = np.array(labels)[leavesy]

plt.figure()
plt.imshow( transformed, aspect = 'auto', interpolation = 'nearest')
plt.grid(False)
plt.colorbar()
plt.title("Clustered Gene Expression")
plt.xticks( [x for x in range(6)], labels)
plt.yticks( [] )
plt.show()
plt.savefig("Heatmap")
plt.close()