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
all_samples <- transform(all_samples,ref_ADvADsum = AD_ref/AD_refSum)
#print(head(all_samples))
#jpeg(paste("CC3-3_f4","_ADvADSum.jpg",sep=""))
#plot(hist(all_samples[all_samples$odd_GT=='0/1' & all_samples$cohort_GT=='0/0',]$ADvADSum,prob=F,100),
#   main=paste("CC3-3_f4","_ADvADSum",sep=""),
#   xlab="mutant AD alt / AD Sum")
#dev.off()

#print(class(all_samples[all_samples$odd_GT=='0/1' & all_samples$cohort_GT=='1/1',]$ref_ADvADsum))
case_FS <- (all_samples[all_samples$odd_GT=='0/0' & all_samples$cohort_GT=='0/1',]$FS)

jpeg("CC3-3_f4_o0.0_c0.1_StrandBias.jpg")
plot(hist(case_FS,prob=F,50),
    main="CC3-3_f4 oddGT:0/0 cohort:0/1 FS",xlab="Strand bias")
dev.off()





