#!/bin/bash

for file in RNAAtlas*; 
	do cd $file; 
	./trimmer.py $file"_merged"; 
	cd ..; 
done
echo "COMPLETE!"
