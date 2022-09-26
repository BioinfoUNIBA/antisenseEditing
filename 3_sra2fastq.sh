#!/bin/bash
for file in RNAAtlas*; 
	do echo $file; 
	cd $file; 
	directories=$(ls | grep SRR); 
	for file2 in $directories; 
		do cd $file2; 
		sra=$(ls *.sra); 
		fasterq-dump --split-files  $sra; 
		cd ..; 
	done; 
cd ..; 
done;
echo "COMPLETE"
