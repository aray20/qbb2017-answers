#!/usr/bin/env python

import sys

fh = sys.stdin
string = "NM:i:0"

count = 0

for line in fh:
    if string in line:
        count += 1
    
print count