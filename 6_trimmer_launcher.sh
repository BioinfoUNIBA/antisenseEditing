#!/bin/bash

for file in RNAAtlas*; 
	do cd $file; 
	/lustre/parkinsongiudice/aim_latest/trimmer.py $file"_merged"; 
	cd ..; 
done
echo "COMPLETE!"
