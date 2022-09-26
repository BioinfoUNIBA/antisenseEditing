#!/bin/bash
for file in RNAAtlas*; 
	do cd $file; 
	printf $file"\n\n"; 
	cat SRR*/*1.fastq >> $file"_merged/"$file"_1.fastq"; 
	cat SRR*/*2.fastq >> $file"_merged/"$file"_2.fastq"; 
	printf "\n\n"; 
	cd ..; 
done
echo "COMPLETE!"
