#!/usr/bin/env python
import os
dic_tissue = {}
with open('AtlasRNAtot.txt','r') as f:
    f.readline()
    for line in f:
        line = line.split(',')
        dic_tissue.setdefault((line[0], line[1], line[5]), []).append(line[2])

for k,v in dic_tissue.items():
    directory = os.getcwd() + '/'
    tissue = '{}_{}'.format(k[0],k[2].replace(' ','_').replace('_tissue',''))
    if not os.path.exists(directory + tissue):
        os.makedirs(directory + tissue)
    sra = directory + tissue + '/SraAccList.txt'
    with open(sra,'w+') as g:
        g.write('\n'.join(v))
