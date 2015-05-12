#!/bin/bash

echo "Enter location of .bam files"
read FILES
echo "Enter directory to write _reorder.bam files"
read OUTLOC

for bamFile in $FILES*.bam
    do
    outName=${bamFile##*/}
    echo "java -Xmx2g -jar /data/daniel.cole/tools/picard-tools-1.96/ReorderSam.jar INPUT=$bamFile OUTPUT=$OUTLOC${outName/.bam/_reorder.bam} &"

done
