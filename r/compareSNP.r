#!/usr/bin/Rscript
#Columns
#"varID","CHROM","POS","REF","ALT","QUAL","FILTER","AC",
#"AF","AN","BaseQRankSum","siteDP","Dels","FS","HaplotypeScore",
#"InbreedingCoeff","MLEAC","MLEAF","MQ","MQ0","MQRankSum","QD",
#"ReadPosRankSum","SOR"

## Collect arguments
#Commandline arg info from http://www.r-bloggers.com/parse-arguments-of-an-r-script/
args <- commandArgs(TRUE)
if(length(args) < 2) {
  cat("Please specify location of .csv file \n")
}

#Read in CC csv file
CC_samples<-read.csv(args[[1]],stringsAsFactors=FALSE,na.string=".",sep=",")
#Read GP csv file
GP_samples<-read.csv(args[[2]],stringsAsFactors=FALSE,na.string=".",sep=",")



#Modify columns to be numeric
CC_samples<-transform(CC_samples,MQ <- as.numeric(MQ),QUAL <- as.numeric(QUAL),siteDP<-as.numeric(siteDP),
    HaplotypeScore<-as.numeric(HaplotypeScore),FS<-as.numeric(FS),QD<-as.numeric(QD),ReadPosRankSum<-as.numeric(ReadPosRankSum),SOR<-as.numeric(SOR))
GP_samples<-transform(GP_samples,MQ <- as.numeric(MQ),QUAL <- as.numeric(QUAL),siteDP<-as.numeric(siteDP),
    HaplotypeScore<-as.numeric(HaplotypeScore),FS<-as.numeric(FS),QD<-as.numeric(QD),ReadPosRankSum<-as.numeric(ReadPosRankSum),SOR<-as.numeric(SOR))



jpeg("CC_QD.jpg")
plot(hist((CC_samples$QD),prob=F,breaks="FD"),
    main="CC QD",xlab="")
dev.off()

jpeg("GP_QD.jpg")
plot(hist((GP_samples$QD),prob=F,breaks="FD"),
    main="GP QD",xlab="")
dev.off()
















#Plot mutant alternate reads / sum of alternate reads at site
#jpeg("CC_MQ.jpg")
#plot(hist((CC_samples$MQ),prob=F,breaks="FD"),
#    main="CC_G & CC",xlab="")
#dev.off()
#
#jpeg("GP_MQ.jpg")
#plot(hist((GP_samples$MQ),prob=F,breaks="FD"),
#    main="CC_G & GP GQ",xlab="")
#dev.off()
#
#jpeg("CC_QUAL.jpg")
#plot(hist((CC_samples$QUAL),prob=F,breaks="FD"),
#    main="CC_G & CC",xlab="")
#dev.off()
#
#jpeg("GP_QUAL.jpg")
#plot(hist((GP_samples$QUAL),prob=F,breaks="FD"),
#    main="CC_G & GP GQ",xlab="")
#dev.off()
#







