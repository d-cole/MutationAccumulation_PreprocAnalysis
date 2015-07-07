#!/usr/bin/Rscript

#Columns
#"varID","CHROM","POS","REF","ALT","QUAL","FILTER","AC",
#"AF","AN","BaseQRankSum","siteDP","Dels","FS","HaplotypeScore",
#"InbreedingCoeff","MLEAC","MLEAF","MQ","MQ0","MQRankSum","QD",
#"ReadPosRankSum","SOR","odd_GT","odd_sample","cohort_GT","AD_alt","odd_DP",
#"AD_ref","AD_altSum","AD_refSum","odd_GQ","odd_PL","Anc_GT","Anc_sample"

setwd("/Users/Daniel/Documents/spirodela/")
CC_rf3 <- read.csv("data/CC3-3/rerun/CC_rf3.csv",stringsAsFactors=FALSE,na.string=".")
CC_rf3_excl <- read.csv("data/CC3-3/rerun/CC_rf3_exclf10.csv",stringsAsFactors=FALSE,na.string=".")
CC_f10 <- read.csv("data/CC3-3/withContam/vcfFiles/CC3-3_f10.csv",stringsAsFactors=FALSE,na.string=".")

GP_rf3 <- read.csv("data/GP2-3/rerun/GP_rf3.csv",stringsAsFactors=FALSE,na.string=".")
GP_rf3_excl <- read.csv("data/GP2-3/rerun/GP_rf3_exclf10.csv",stringsAsFactors=FALSE,na.string=".")
GP_f10 <- read.csv("data/GP2-3/vcfFiles/GP2-3_f10.csv",stringsAsFactors=FALSE,na.string=".")

all_cases <- list(CC_rf3,CC_rf3_excl,CC_f10,GP_rf3,GP_rf3_excl,GP_f10)

makeNumeric <- function(table){
   table <- transform(table,MLEAC = as.numeric(MLEAC),MLEAF=as.numeric(MLEAF),
    AC=as.numeric(AC),AN=as.numeric(AN),BaseQRankSum=as.numeric(BaseQRankSum),
    siteDP=as.numeric(siteDP),Dels=as.numeric(Dels),FS=as.numeric(FS),
    HaplotypeScore=as.numeric(HaplotypeScore),InbreedingCoeff=as.numeric(InbreedingCoeff),
    MQ=as.numeric(MQ),MQ0=as.numeric(MQ0),
    MQRankSum=as.numeric(MQRankSum),QD=as.numeric(QD),ReadPosRankSum=as.numeric(ReadPosRankSum),
    SOR=as.numeric(SOR)) 
}
sampleCounts <- function(table){
    samples = unique(table$odd_sample)
    for (sample in samples){
        print(paste("Counts for ",sample,NROW(table[table$odd_sample == sample,])))
    } 
}

for (table in all_cases){
    makeNumeric(table)
}

binom <- function(alt,ref){
    n<- alt+ref
    if (pbinom(alt,n,0.5) > 0.01){
        return(TRUE)
    }
    return(FALSE)
}

binomCounts <- function(table){
    binom_count <- 0
    for (i in 1:nrow(table)){
        if (binom(table[i,"AD_alt"],table[i,"AD_ref"]) == TRUE){
            binom_count<-binom_count+1
        }
    }
}



getBinomRows <- function(table){
    filtered_table <- table[0,]
    for (i in 1:nrow(table)){
        if (binom(table[i,"AD_alt"],table[i,"AD_ref"]) == TRUE){
            filtered_table <- rbind(filtered_table,table[i,])
        }

    }
    return(filtered_table)
}

################################################################################


CC_rf4 <- getBinomRows(CC_rf3)
GP_rf4 <- getBinomRows(GP_rf3)
sampleCounts(CC_rf4)
sampleCounts(GP_rf4)













