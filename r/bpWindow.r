library(ggplot2)

# ----------- Column names ------------
#start_chrom,start_pos,stop_chrom,stop_pos,altSiteCount,refSiteCount
#avgDepth,avgRefReads,avgAltReads,avgOtherReads
# -------------------------------------

args <- commandArgs(TRUE)
if(length(args) < 2) {
  cat("Please specify location of .csv file & name of output file\n")
}

#Read in csv file
window<-read.csv(args[1],stringsAsFactors=FALSE,na.string=".")

#transform appropriate columns to numeric
window<-transform(window,
    altSiteCount<-as.numeric(altSiteCount),
    refSiteCount<-as.numeric(refSiteCount),
    avgRefReads<-as.numeric(avgRefReads),
    avgAltReads<-as.numeric(avgAltReads),
    avgOtherReads<-as.numeric(avgAltReads))

print(head(window))


jpeg(args[2])
ggplot(data=window,aes(avgRefReads)) + geom_histogram(binwidth=0.01) + xlim(c(0,1))
dev.off()

#jpeg(paste("pos_",args[2]))
#ggplot(date=window,aes(start_pos,avgRefReads)) + geom_point()
#dev.off()

