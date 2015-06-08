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



print("Mutation case counts")
odd_GT = unique(all_samples$odd_GT) 
cohort_GT = unique(all_samples$cohort_GT)

cat("odd_GT   Cohort_GT    mCount   \n")
for (s_gt in odd_GT) {
    for(c_GT in cohort_GT){
        if (s_gt != c_GT){
            cat(paste(s_gt,c_GT,"    ",sep="       "))
            cat(NROW(all_samples[all_samples$odd_GT==s_gt & all_samples$cohort_GT==c_GT,]))
            cat("\n")
        }
    }
}


print("Individual counts")
sample_names = unique(all_samples$odd_sample)
samples <- list()
invisible(lapply(sample_names,function(x) print(paste(x,NROW(all_samples[all_samples$odd_sample==x,]),sep=": "))))



jpeg(paste("GP2-3_f4","_oddGQ.jpg",sep=""))
plot(hist(all_samples$odd_GQ,prob=F,100),
   main=paste("GP2-3_f4","_oddGQ",sep=""),
   xlab="Genotype Quality")
dev.off()









