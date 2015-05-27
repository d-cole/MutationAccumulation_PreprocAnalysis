#!/bin/bash
LOC=$1
arr=($LOC*_dedup.bam)
size=${#arr[@]}
for((i=0; i<$size; i+=1)); do
  echo  "java -Xmx2g -jar ~/tools/GenomeAnalysisTK.jar -T IndelRealigner -R /data/maggie.bartkowska/spirodela_ma/reference/pseudo_plastids.fa -targetIntervals ${arr[$i]/.bam/.intervals} -I ${arr[$i]} -o ${arr[$i]/.bam/_realigned.bam}"

done
