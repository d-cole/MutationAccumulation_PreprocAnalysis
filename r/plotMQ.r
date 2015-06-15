#!/usr/bin/Rscript
library(tools)

#Columns
#"varID","CHROM","POS","REF","ALT","QUAL","FILTER","AC",
#"AF","AN","BaseQRankSum","siteDP","Dels","FS","HaplotypeScore",
#"InbreedingCoeff","MLEAC","MLEAF","MQ","MQ0","MQRankSum","QD",
#"ReadPosRankSum","SOR","odd_GT","odd_sample","cohort_GT","AD_alt",
#"AD_ref","AD_altSum","AD_refSum","odd_GQ","odd_PL","Anc_GT","Anc_sample"

## Collect arguments
#Commandline arg info from http://www.r-bloggers.com/parse-arguments-of-an-r-script/
args <- commandArgs(TRUE)
if(length(args) < 1) {
  cat("Please specify location of .csv file \n")
}

#Read in csv file
all_samples<-read.csv(args[1],stringsAsFactors=FALSE,na.string=".")
print(args)

name_ext<-basename(args[1])
name<-sub(".csv","",name_ext)
setwd(sub(name_ext,"",args[1]))

#Plot mutant alternate reads / sum of alternate reads at site
jpeg(paste(name,"_MQ.jpg",sep=""))
plot(hist((all_samples$MQ),prob=F,breaks="FD"),
    main=paste(name," MQ",sep=" "),xlab="MQ")
dev.off()







