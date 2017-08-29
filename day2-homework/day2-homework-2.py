#!/usr/bin/env python

import sys

f1 = open(sys.argv[1]) #File day2_homework.out
f2 = open(sys.argv[2]) #File t_data.ctab
#f3 = open(sys.argv[3]) 

count = 0

dic = {}
for line in f1:
    cut = line.strip().split(" ")
    fly = cut[0]
    uni = cut[1]
    dic[fly] = uni
    
for line in f2:
    fields = line.strip("\r\n").split("\t")
    eight = fields[8]
   # print eight
    if eight in dic:
        name = dic[eight]
       # print eight, name
        fields[8] = name
    count += 1
    if count > 100:
        break
    print "\t".join(fields) 