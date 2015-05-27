LOC=$1
comm="java -jar ~/tools/GenomeAnalysisTK.jar -R /data/maggie.bartkowska/spirodela_ma/reference/pseudo_plastids.fa -T \
UnifiedGenotyper"
i=" -I "
post=" -o /data/maggie.bartkowska/spirodela_ma/ugOutput/GP2-3_UG.vcf -out_mode EMIT_ALL_SITES"
for file in $LOC*CC_*.bam
    do
    comm=$comm$i$file

done

echo "$comm$post"
