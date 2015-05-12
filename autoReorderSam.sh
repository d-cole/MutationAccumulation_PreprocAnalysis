#!/bin/bash

echo "Enter location of .bam files"
read FILES
echo "Enter directory to write _reorder.bam files"
read OUTLOC
echo "Enter location of reference: "
read REF


for bamFile in $FILES*.bam
    do
    outName=${bamFile##*/}
    java -Xmx2g -jar /data/daniel.cole/tools/picard-tools-1.96/ReorderSam.jar INPUT=$bamFile OUTPUT=$OUTLOC${outName/.bam/_reorder.bam} REFERENCE=$REF &

done
