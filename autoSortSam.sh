#!/bin/bash

echo "Enter location of *_reorder.bam files: "
read FILES

for rgFile in $FILES*readgroup.bam
    do
    java -Xmx2g -jar ~/tools/picard-tools-1.98/SortSam.jar INPUT=$rgFile OUTPUT=${rgFile/.bam/_sorted.bam} SORT_ORDER=coordinate &
done 


