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

print(head(window))

#Want to adjust for depth
window$refAvgByDepth <- window$avgRefReads/window$avgDepth
window$altAvgByDepth <- window$avgAltReads/window$avgDepth
window$otherAvgByDepth <- window$avgOtherReads/window$avgDepth
window$avgDepthByDepth <- window$avgDepth/window$avgDepth


#w2 <- window[window$otherAvgByDepth > 0.002,]
#print(NROW(w2))
#print(NROW(window))

#jpeg(args[2])
#ggplot(data=window,aes(avgRefReads)) + geom_histogram(binwidth=0.01) + xlim(c(0,1))
#dev.off()
name <- (args[2])
print(typeof(name))

#######################  Basic plots ################################
#p1 <- ggplot(window,aes(x=start_pos,y=altAvgByDepth))
#jpeg(paste(name,"_altAvgByDepth.jpg",sep=''))
#p1 + geom_point()
#dev.off()
#
#p2 <- ggplot(window,aes(x=start_pos,y=otherAvgByDepth))
#jpeg(paste(name,"_otherAvgByDepth.jpg",sep=''))
#p2 + geom_point()
#dev.off()
#
#p3 <- ggplot(window,aes(x=start_pos,y=refAvgByDepth))
#jpeg(paste(name,"_refAvgByDepth.jpg",sep=''))
#p3+geom_point()
#dev.off()
#
#p4 <- ggplot(window,aes(x=start_pos,y=avgDepthByDepth))
#jpeg(paste(name,"_avgDepthByDepth.jpg",sep=''))
#p4+geom_point()
#dev.off()
#
######################################################################

#Plot alt/other/ref reads count Vs. start_pos, coloured by chromosome
#Need 31 colours?
chroms <- unique(window$start_chrom)
colours <- list("cornsilk3","dodgerblue4","cornflowerblue",
                "coral3","darkviolet","orchid",
                "lawngreen","palegreen","orangered",
                "darkslateblue","hotpink4","orange4",
                "burlywood","darkorchid4","grey60",
                "lightskyblue","olivedrab2","royalblue",
                "salmon2","black","gold2",
                "aquamarine2","firebrick","peru",
                "lightgoldenrod2","grey39","sienna2",
                "chocolate1","indianred4","palevioletred4",
                "paleturquoise1","red")



altPlot <- ggplot(data=window,aes(start_pos,altAvgByDepth,colour = start_chrom)) + geom_point() + 
    scale_colour_manual(breaks = window$start_chrom,values = colours)

refPlot <- ggplot(data=window,aes(start_pos,refAvgByDepth,colour = start_chrom)) + geom_point() + 
     scale_colour_manual(breaks = window$start_chrom,values = colours)

otherPlot <- ggplot(data=window,aes(start_pos,otherAvgByDepth,colour = start_chrom)) + geom_point() + 
     scale_colour_manual(breaks = window$start_chrom,values = colours)

testPlot <- ggplot(data=window,aes(start_pos,avgDepthByDepth,colour = start_chrom)) + geom_point() + 
     scale_colour_manual(breaks = window$start_chrom,values = colours)

refPlotHist <- ggplot(data=window,aes(refAvgByDepth)) + geom_histogram()
otherPlotHist <- ggplot(data=window,aes(otherAvgByDepth)) + geom_histogram()
altPlotHist <- ggplot(data=window,aes(altAvgByDepth)) + geom_histrogram()
ggsave(refPlotHist,file=paste(name,"_refPlotHist.jpg",sep=""))
ggsave(otherPlotHist,file=paste(name,"_otherPlotHist.jpg",sep=""))
ggsave(altPlotHist,file=paste(name,"_altPlotHist.jpg",sep=""))

#ggsave(altPlot,file=paste(name,"altAvgByDepth.jpg",sep=""),dpi=600)
#ggsave(refPlot,file=paste(name,"refAvgByDepth.jpg",sep=""),dpi=600)
ggsave(otherPlot,file=paste(name,"otherAvgByDepth.jpg",sep=""),dpi=600)
#ggsave(testPlot,file=paste(name,"avgDepthAvgByDepth.jpg",sep=""),dpi=600)






