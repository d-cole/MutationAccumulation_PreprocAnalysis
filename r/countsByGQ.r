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
cat("Number of sites where mutant has GQ <= x \n")
cat("GQ     #Sites \n")
for (i in seq(from=0,to=100,by=10)) {
    cat(paste(i,"   ",sep=""))
    cat(NROW(all_samples[all_samples$FS <= i,]))
    cat("\n")
    
}

#print(class(all_samples[all_samples$odd_GT=='0/1' & all_samples$cohort_GT=='1/1',]$ref_ADvADsum))
#case_AD <- (all_samples[all_samples$odd_GT=='0/1' & all_samples$cohort_GT=='1/1',]$ref_ADvADsum)

#jpeg("CC3-3_f4_o0.1_c1.1_ADref.ADrefSum.jpg")
#plot(hist(case_AD,prob=F),
#    main="CC3-3_f4 oddGT:0/1 cohort:1/1 (Odd AD ref)/(AD ref Sum)",xlab="Odd AD ref)/(AD alt Ref)")
#dev.off()





