library(ggplot2)
library("reshape2")

args <- commandArgs(TRUE)
if(length(args) < 2) {
  cat("Please specify location of .csv file & name of output file\n")
}

#Read in csv file
pValues<-read.csv(args[1],stringsAsFactors=FALSE,na.string=".")

#transform appropriate columns to numeric
#window<-transform(window,
#    B<-as.numeric(altSiteCount),
#    refSiteCount<-as.numeric(refSiteCount),
#    avgRefReads<-as.numeric(avgRefReads),
#    avgAltReads<-as.numeric(avgAltReads),
#    avgOtherReads<-as.numeric(avgAltReads))

name <- (args[2])
print(head(pValues))

for(col in names(pValues)){
    print(col)
    pValues <-transform(pValues,col<-as.numeric(col))
    col_data  <- pValues[,col]
    plot <- ggplot() + aes(col_data) + geom_histogram()
    ggsave(plot,file=paste(name,col,".jpg",sep=""))
}

#refPlot <- ggplot(data=window,aes(start_pos,refAvgByDepth,colour = start_chrom)) + geom_point() + 
#     scale_colour_manual(breaks = window$start_chrom,values = colours)
#
#otherPlot <- ggplot(data=window,aes(start_pos,otherAvgByDepth,colour = start_chrom)) + geom_point() + 
#     scale_colour_manual(breaks = window$start_chrom,values = colours)
#
#testPlot <- ggplot(data=window,aes(start_pos,avgDepthByDepth,colour = start_chrom)) + geom_point() + 
#     scale_colour_manual(breaks = window$start_chrom,values = colours)
#
#refPlotHist <- ggplot(data=window,aes(refAvgByDepth)) + geom_histogram()
#otherPlotHist <- ggplot(data=window,aes(otherAvgByDepth)) + geom_histogram()
#altPlotHist <- ggplot(data=window,aes(altAvgByDepth)) + geom_histrogram()
#ggsave(refPlotHist,file=paste(name,"_refPlotHist.jpg",sep=""))
#ggsave(otherPlotHist,file=paste(name,"_otherPlotHist.jpg",sep=""))
#ggsave(altPlotHist,file=paste(name,"_altPlotHist.jpg",sep=""))
#
##ggsave(altPlot,file=paste(name,"altAvgByDepth.jpg",sep=""),dpi=600)
##ggsave(refPlot,file=paste(name,"refAvgByDepth.jpg",sep=""),dpi=600)
#ggsave(otherPlot,file=paste(name,"otherAvgByDepth.jpg",sep=""),dpi=600)
##ggsave(testPlot,file=paste(name,"avgDepthAvgByDepth.jpg",sep=""),dpi=600)






