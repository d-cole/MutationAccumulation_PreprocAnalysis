#!/bin/bash
LOC=$1
arr=($LOC*_sorted.bam)
size=${#arr[@]}
for((i=0; i<$size; i+=1)); do
  echo  "java -Xmx2g -jar ~/tools/picard-tools-1.96/MarkDuplicates.jar INPUT=${arr[$i]} OUTPUT=${arr[$i]/.bam/_dedup.bam} M=${arr[$i]/.bam/_dups.bam} &"

done
