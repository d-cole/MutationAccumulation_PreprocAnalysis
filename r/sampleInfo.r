# sampleInfo.r
# Given a .csv representing a .vcf file
#

library(ggplot2)
library("reshape2")

#"varID","CHROM","POS","REF","ALT","QUAL","FILTER","AC","AF","AN","BaseQRankSum","siteDP","Dels","FS",
#"HaplotypeScore","InbreedingCoeff","MLEAC","MLEAF","MQ","MQ0","MQRankSum","QD","ReadPosRankSum","SOR",
#"odd_GT","odd_sample","cohort_GT","AD_alt","AD_ref","odd_DP","AD_altSum","AD_refSum","odd_GQ","odd_PL"

args <- commandArgs(TRUE)
if(length(args) < 1) {
  cat("Please specify location of .csv file & name of output file\n")
}

#Read in csv file
file<-read.csv(args[1],stringsAsFactors=FALSE,na.string=".")

#transform appropriate columns to numeric
file<-transform(file,
    AD_alt<-as.numeric(AD_alt),
    AD_ref<-as.numeric(AD_ref))

samples <-unique(file$odd_sample)

mean_na<-function(x){
    mean(x[which(!is.na(x))])
}


for(s in samples){
   print(s)
   file_sample <- file[file$odd_sample == s,]
   print(NROW(file_sample))
   print(mean_na(file_sample$AD_alt)) 
}









