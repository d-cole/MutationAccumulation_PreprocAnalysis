library(ggplot2)
library("reshape2")
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


#Want to adjust for depth
window$refAvgByDepth <- window$avgRefReads/window$avgDepth
window$altAvgByDepth <- window$avgAltReads/window$avgDepth
window$otherAvgByDepth <- window$avgOtherReads/window$avgDepth
window$avgDepthByDepth <- window$avgDepth/window$avgDepth

cat("Number of 50bp windows:")
print(NROW(window))

cat("otherAvg > 0.02: ")
print(NROW(window[window$otherAvgByDepth > 0.02,]))

cat("altAvg > 0.01: ")
print(NROW(window[window$altAvgByDepth > 0.01,]))

cat("refAvg < 0.99: ")
print(NROW(window[window$refAvgByDepth < 0.99,]))





