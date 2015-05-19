#!/bin/bash
LOC=$1
arr=($LOC*_readgroup.bam)
size=${#arr[@]}
for ((i=0; i<$size; i+=2)); do
    i2=$((i+1))
    java -Xmx2g -jar ~/tools/picard-tools-1.96/SortSam.jar INPUT=${arr[$i]} OUTPUT=${arr[$i]/.bam/_sorted.bam} SORT_ORDER=coordinate &
    if [ $i2 -lt $size ]
        then
            java -Xmx2g -jar ~/tools/picard-tools-1.96/SortSam.jar INPUT=${arr[$i2]} OUTPUT=${arr[$i2]/.bam/_sorted.bam} SORT_ORDER=coordinate  
    fi

done













