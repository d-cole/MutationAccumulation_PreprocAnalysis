#!/bin/bash
#Converts all .sam files in a given directory to .bam using picard tools

echo "Enter directory containing .sam files: "
FILES=$1
echo "Enter directory to write .bam files: "
OUTLOC=$2
for vcfFile in $FILES*.vcf
    do
    outName=${vcfFile##*/}
    echo "python ~/spirodela/filtering/mut_filtering.py $vcfFile OUTPUT=$OUTLOC${outName/.vcf/_m0.vcf}"
done


