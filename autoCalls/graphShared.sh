#!/bin/bash
#Generates a file containing commands for all  


FILES=$1

for file in $FILES*.csv
    do
    Rscript ~/Documents/spirodela/r/sharedSites.r $file $file
done


