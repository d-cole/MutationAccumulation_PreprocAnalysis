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


#Plot mutant alternate reads / sum of alternate reads at site
jpeg("CC3-3_f8_ADalt.ADaltSum.jpg")
plot(hist((all_samples$mAltvAltSum),prob=F,breaks="FD"),
    main="CC3-3 (Mutant alt reads) / (Sum of site alt reads)",xlab="(Odd AD alt)/(AD alt Sum)")
dev.off()


#jpeg("CC3-3_F8_ADaltSum.jpg")
#plot(hist((all_samples$AD_altSum),prob=F,breaks="FD"),
#    main="CC3_f8 AD alt Sum",xlab="AD alt sum")
#dev.off()
#



#jpeg("oddGQ-mAltvAltSum.jpg")
#with(all_samples,plot(odd_GQ ~ mAltvAltSum))
#dev.off()

#jpeg("Hscore-mAltvAltSum.jpg")
#with(all_samples,plot(HaplotypeScore ~ mAltvAltSum))
#dev.off()

#jpeg("MQ-mAltvAltSum.jpg")
#with(all_samples,plot(MQ ~ mAltvAltSum))
#dev.off()

#jpeg("MQ0-mAltvAltSum.jpg")
#with(all_samples,plot(MQ0 ~ mAltvAltSum))
#dev.off()

#jpeg("QD-mAltvAltSum.jpg")
#with(all_samples,plot(QD ~ mAltvAltSum))
#dev.off()

#jpeg("ReadPosRankSum-mAltvAltSum.jpg")
#with(all_samples,plot(ReadPosRankSum ~ mAltvAltSum))
#dev.off()

#jpeg("FS-mAltvAltSum.jpg")
#with(all_samples,plot(FS ~ mAltvAltSum))
#dev.off()

#jpeg("SOR-mAltvAltSum.jpg")
#with(all_samples,plot(SOR ~ mAltvAltSum))
#dev.off()

#jpeg("Dels-mAltvAltSum.jpg")
#with(all_samples,plot(Dels ~ mAltvAltSum))
#dev.off()

#jpeg("siteDP-mAltvAltSum.jpg")
#with(all_samples,plot(siteDP ~ mAltvAltSum))
#dev.off()

#jpeg("InbreedingCoeff-mAltvAltSum.jpg")
#with(all_samples,plot(InbreedingCoeff ~ mAltvAltSum))
#dev.off()

#jpeg("MLEAC-mAltvAltSum.jpg")
#with(all_samples,plot(MLEAC ~ mAltvAltSum))
#dev.off()

#jpeg("MLEAF-mAltvAltSum.jpg")
#with(all_samples,plot(MLEAF ~ mAltvAltSum))
#dev.off()






