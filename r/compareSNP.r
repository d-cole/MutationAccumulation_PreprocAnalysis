#!/usr/bin/Rscript
#Columns
#"varID","CHROM","POS","REF","ALT","QUAL","FILTER","AC",
#"AF","AN","BaseQRankSum","siteDP","Dels","FS","HaplotypeScore",
#"InbreedingCoeff","MLEAC","MLEAF","MQ","MQ0","MQRankSum","QD",
#"ReadPosRankSum","SOR","odd_GT","odd_sample","cohort_GT","AD_alt",
#"AD_ref","AD_altSum","AD_refSum","odd_GQ","odd_PL","Anc_GT","Anc_sample"



## Collect arguments
#Commandline arg info from http://www.r-bloggers.com/parse-arguments-of-an-r-script/
args <- commandArgs(TRUE)
if(length(args) < 22) {
  cat("Please specify location of .csv file \n")
}

#Read in CC csv file
CC_samples<-read.csv(args[1],stringAsFactors=FALSE,na.string=".")

#Read GP csv file
GP_samples<-read.csv(args[2],stringAsFactors=FALSE,na.string=".")


#Plot mutant alternate reads / sum of alternate reads at site
jpeg("CC.jpg")
plot(hist((CC_samples$GQ),prob=F,breaks="FD"),
    main="",xlab="")
dev.off()

jpeg("GP.jpg")
plot(hist((CC_samples$GQ),prob=F,breaks="FD"),
    main="",xlab="")
dev.off()








