#!/bin/bash
for file in RNAAtlas*; 
	do echo $file; 
	cd $file; 
	mkdir $file"_merged";  
	cd ..; 
done

