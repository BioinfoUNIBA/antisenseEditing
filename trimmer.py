#!/usr/bin/python2.7 -u 
import os
import sys
try:
	tissues = sys.argv[1]

except:
	sys.exit('<Tissues separated by space eg. Brain Heart etc..>')


dicf = {}
for dir in os.listdir('.'):
	if dir in tissues:
		os.chdir(dir)
		for file in os.listdir('.'):
			if file.endswith('.fastq'):
				dicf.setdefault(dir,[]).append(os.path.abspath(file))
		os.chdir('..')

for k,v in sorted(dicf.items()):
	r1 = v[0]
	r2 = v[1]
	print('Working on sample {}'.format(k))
	cmd = 'fastp -i {} -I {} -o {} -O {} -l 50 -w 8'.format(r1, r2, r1.replace('.fastq','_trimmed.fastq'), r2.replace('.fastq','_trimmed.fastq'))	
	#print cmd
	os.system(cmd)
print('ALL JOB COMPLETED!')

