#!/bin/bash
for file in RNAAtlas* 
	do cd $file 
	printf $file"\n"
	prefetch --option-file  SraAccList.txt
	printf "\n\n"
	cd .. 
done
echo "COMPLETE!"
