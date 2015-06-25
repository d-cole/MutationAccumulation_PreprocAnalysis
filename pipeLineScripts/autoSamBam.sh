#!/bin/bash
#Converts all .sam files in a given directory to .bam using picard tools

echo "Enter directory containing .sam files: "
read FILES
echo "Enter directory to write .bam files: "
read OUTLOC

for samFile in $FILES*.vcf
    do
    outName=${samFile##*/}
    echo "java -Xmx2g -jar ~/picard-tools-1.96/SamFormatConverter.jar INPUT=$samFile OUTPUT=$OUTLOC${outName/.sam/.bam} &"
done


