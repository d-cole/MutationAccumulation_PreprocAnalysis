#!/usr/bin/Rscript

#Columns
#"varID","CHROM","POS","REF","ALT","QUAL","FILTER","AC",
#"AF","AN","BaseQRankSum","siteDP","Dels","FS","HaplotypeScore",
#"InbreedingCoeff","MLEAC","MLEAF","MQ","MQ0","MQRankSum","QD",
#"ReadPosRankSum","odd_GT","odd_sample","cohort_GT","AD_alt",
#"AD_ref","AD_altSum","AD_refSum","odd_GQ","odd_PL","Anc_GT","Anc_sample"

## Collect arguments
#Commandline arg info from http://www.r-bloggers.com/parse-arguments-of-an-r-script/
args <- commandArgs(TRUE)
## Default setting when no arguments passed

if(length(args) < 1) {
  cat("Please specify location of .csv file")
}
all_samples<-read.csv(args,stringsAsFactors=FALSE,na.string=".")
all_samples <- transform(all_samples,alt_ADvADSum = AD_alt/AD_altSum)
print(head(all_samples))

case_AD <- (all_samples[all_samples$odd_GT=='0/1' & all_samples$cohort_GT=='0/0',all_samples$alt_ADvADsum])
str(case_AD)
jpeg("CC3-3_f7_o0.1_c0.0_ADalt.ADaltSum.jpg")
plot(hist((all_samples$AD_alt/all_samples$AD_altSum),prob=F,50),
    main="CC3-3_f7 (Mutant alt reads) / (Sum of alt reads)",xlab="(Odd AD alt)/(AD alt Sum)")
dev.off()





