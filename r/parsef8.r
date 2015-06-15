#!/usr/bin/Rscript

#Columns
#"varID","CHROM","POS","REF","ALT","QUAL","FILTER","AC",
#"AF","AN","BaseQRankSum","siteDP","Dels","FS","HaplotypeScore",
#"InbreedingCoeff","MLEAC","MLEAF","MQ","MQ0","MQRankSum","QD",
#"ReadPosRankSum","SOR","odd_GT","odd_sample","cohort_GT","AD_alt","odd_DP",
#"AD_ref","AD_altSum","AD_refSum","odd_GQ","odd_PL","Anc_GT","Anc_sample"

## Collect arguments
#Commandline arg info from http://www.r-bloggers.com/parse-arguments-of-an-r-script/
args <- commandArgs(TRUE)
if(length(args) < 1) {
  cat("Please specify location of .csv file \n")
}

#Read in csv file
all_samples<-read.csv(args,stringsAsFactors=FALSE,na.string=".")
#print(head(all_samples))
#Add column mAltvAltSum which is mutant alt reads divided by sum of alt reads at that site
all_samples$mAltvAltSum <- all_samples$AD_alt/all_samples$AD_altSum
all_samples <-transform(all_samples,MLEAC = as.numeric(MLEAC),MLEAF=as.numeric(MLEAF),
    AC=as.numeric(AC),AN=as.numeric(AN),BaseQRankSum=as.numeric(BaseQRankSum),
    siteDP=as.numeric(siteDP),Dels=as.numeric(Dels),FS=as.numeric(FS),
    HaplotypeScore=as.numeric(HaplotypeScore),InbreedingCoeff=as.numeric(InbreedingCoeff),
    MQ=as.numeric(MQ),MQ0=as.numeric(MQ0),
    MQRankSum=as.numeric(MQRankSum),QD=as.numeric(QD),ReadPosRankSum=as.numeric(ReadPosRankSum),
    SOR=as.numeric(SOR))



hard_filter<-all_samples[!is.na(all_samples$Anc_sample) & all_samples$mAltvAltSum > 0.7 & all_samples$Dels == 0.0 & all_samples$FS < 60 & all_samples$MQ > 40.0 & all_samples$QD > 2.0 & all_samples$MQRankSum > -12.5 & all_samples$ReadPosRankSum > -8.0,]

print(NROW(hard_filter))
print(NROW(hard_filter[hard_filter$AD_alt > 3,]))
samples<-unique(hard_filter$odd_sample)
#print(samples)

#for (i in samples){
#    cat(i)
#    print(NROW(hard_filter[hard_filter$odd_sample == i,]))
#
#}
#
#print(NROW(all_samples[!is.na(all_samples$Anc_sample) & all_samples$mAltvAltSum > 0.7 & all_samples$Dels == 0.0 & all_samples$FS < 60 & all_samples$MQ > 40.0 & all_samples$QD > 2.0 & all_samples$MQRankSum > -12.5 & all_samples$ReadPosRankSum > -8.0,]))
#
#for (i in all_samples[!is.na(all_samples$Anc_sample) & all_samples$mAltvAltSum > 0.7 & all_samples$Dels == 0.0 & all_samples$FS < 60 & all_samples$MQ > 40.0 & all_samples$QD > 2.0 & all_samples$MQRankSum > -12.5 & all_samples$ReadPosRankSum > -8.0,c(1,26)]){
#
#    cat(i)
#    cat("\n")
#}













