#!/bin/bash
#Converts all .sam files in a given directory to .bam using picard tools

FILES=$1
TE_LOC=$2
for chromFile in $FILES*_TEremoved.vcf
    do
    echo "python /data/daniel.cole/spirodela/filtering/removeTE.py $TE_LOC $chromFile"
done


