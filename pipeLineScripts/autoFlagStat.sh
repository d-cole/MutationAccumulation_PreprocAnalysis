#!/bin/bash
LOC=$1
arr=($LOC*.bam)
size=${#arr[@]}
for((i=0; i<$size; i+=1)); do
  echo "~/tools/samtools-1.2/samtools flagStat ${arr[$i]} > ${arr[$i]}.txt"

done
