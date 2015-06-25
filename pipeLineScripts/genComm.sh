#!/bin/bash
#Generates a file containing commands for all  


FILES=$1

for file in $FILES*_m0.vcf
    do
    for fil2 in $FILES*_m0.vcf
        do
        python /data/daniel.cole/spirodela/postFilt/compareSNP.py $file $fil2 >> pairWise.txt
        done
done


