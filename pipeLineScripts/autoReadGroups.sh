#!/bin/bash

echo "Enter location of *_reorder.bam files: "
read FILES
echo "Enter lane specifier (L3):"
read LANE
echo "Enter platform barcode (C5YABACXX):"
read BAR

for reFile in $FILES*_reorder.bam
    do
    SM=${reFile##*/}
    SM=${SM%_reorder.bam}
    java -Xmx2g -jar /data/daniel.cole/tools/picard-tools-1.96/AddOrReplaceReadGroups.jar \
INPUT=$reFile \
OUTPUT=${reFile/_reorder.bam/_reorder_readgroup.bam} \
RGLB=lib.$SM \
RGPL=illumina \
RGID=$BAR.$LANE.$SM \
RGPU=$BAR.$LANE \
RGSM=$SM & 

done 
