#!/bin/bash
LOC=$1
arr=($LOC*_readgroup.bam)
size=${#arr[@]}
for ((i=0; i<$size; i+=1)); do
    java -Xmx4g -jar ~/tools/picard-tools-1.96/SortSam.jar INPUT=${arr[$i]} OUTPUT=${arr[$i]/.bam/_sorted.bam} SORT_ORDER=coordinate

done













