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
if(length(args) < 1) {
  cat("Please specify location of .csv file \n")
}

#Read in csv file
all_samples<-read.csv(args,stringsAsFactors=FALSE,na.string=".")

#Add column mAltvAltSum which is mutant alt reads divided by sum of alt reads at that site
all_samples$mAltvAltSum <- all_samples$AD_alt/all_samples$AD_altSum
all_samples <-transform(all_samples,MLEAC = as.numeric(MLEAC),MLEAF=as.numeric(MLEAF),
    AC=as.numeric(AC),AN=as.numeric(AN),BaseQRankSum=as.numeric(BaseQRankSum),
    siteDP=as.numeric(siteDP),Dels=as.numeric(Dels),FS=as.numeric(Dels),
    HaplotypeScore=as.numeric(HaplotypeScore),InbreedingCoeff=as.numeric(InbreedingCoeff),
    MQ=as.numeric(MQ),MQ0=as.numeric(MQ0),
    MQRankSum=as.numeric(MQRankSum),QD=as.numeric(QD),ReadPosRankSum=as.numeric(ReadPosRankSum),
    SOR=as.numeric(SOR))

mLEAC <- all_samples[all_samples$MLEAC > 5,]

dels <- all_samples[all_samples$Dels > 0, ]
#print(head(mLEAC))
#print(NROW(mLEAC))
#print(str(mLEAC))
#print(NROW(dels))

#class(all_samples$AC)
#model <- lm(all_samples$AC ~ all_samples$AF ~ all_samples$AN ~ all_samples$BaseQRankSum ~ all_samples$siteDP ~ all_samples$Dels ~ all_samples$FS ~ all_samples$HaplotypeScore ~ all_samples$InbreedingCoeff ~ all_samples$MLEAC ~ all_samples$MLEAF ~ all_samples$MQ ~ all_samples$MQ0 ~ all_samples$MQRankSum ~ all_samples$QD ~ all_samples$ReadPosRankSum ~ all_samples$SOR ~ all_samples$mAltvAltSum)
#summary(model)


cols = c("AC","AF","AN","BaseQRankSum","siteDP","Dels","FS","HaplotypeScore","InbreedingCoeff","MLEAC","MLEAF","MQ","MQ0","MQRankSum","QD","ReadPosRankSum","SOR","mAltvAltSum")


for (c in cols){
    for (k in cols){
    print(paste("cor: ",c,k,sep=" "))
    print(cor(all_samples[[c]],all_samples[[k]],method="pearson"))

    print(paste("cov: ",c,k,sep=" "))
    print(cov(all_samples[[c]],all_samples[[k]],method="pearson"))
      
    }


}
