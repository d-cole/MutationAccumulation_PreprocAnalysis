#!/bin/bash
LOC=$1
arr=($LOC*_dedup.bam)
size=${#arr[@]}
for((i=0; i<$size; i+=1)); do
  echo  "java -Xmx2g -jar ~/tools/picard-tools-1.96/BuildBamIndex.jar INPUT=${arr[$i]}"

done
