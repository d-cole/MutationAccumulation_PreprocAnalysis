#!/bin/bash
#Generates a file containing commands for all  

FILES=$1

for file in $FILES*.txt
    do
    outFile=${file/.txt/_50bp.csv}
    echo "python /data/daniel.cole/spirodela/filtering/pyWindow.py $file $outFile"
done


