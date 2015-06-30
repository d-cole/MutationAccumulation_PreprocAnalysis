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


#Modify columns to be numeric
CC_samples<-transform(CC_samples,MQ <- as.numeric(MQ),QUAL <- as.numeric(QUAL),siteDP<-as.numeric(siteDP),
    HaplotypeScore<-as.numeric(HaplotypeScore),FS<-as.numeric(FS),QD<-as.numeric(QD),ReadPosRankSum<-as.numeric(ReadPosRankSum),SOR<-as.numeric(SOR))


jpeg(paste(args[[2]],"_QD.jpg",sep=""))
plot(hist((CC_samples$QD),prob=F,breaks="FD"),
    main=paste(args[[2]]," QD"),xlab="")
dev.off()


jpeg(paste(args[[2]],"_MQ.jpg",sep=""))
plot(hist((CC_samples$MQ),prob=F,breaks="FD"),
    main=paste(args[[2]], "MQ"),xlab="")
dev.off()

jpeg(paste(args[[2]],"_QUAL.jpg",sep=""))
plot(hist((CC_samples$QUAL),prob=F,breaks="FD"),
    main=paste(args[[2]]," QUAL"),xlab="")
dev.off()







