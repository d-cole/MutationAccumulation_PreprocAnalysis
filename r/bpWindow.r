library(ggplot2)

args <- commandArgs(TRUE)
if(length(args) < 2) {
  cat("Please specify location of .csv file \n")
}

#Read in csv file
CC_window<-read.csv(args[1],stringsAsFactors=FALSE,na.string=".")
#GP_window<-read.csv(args[2],stringsAsFactors=FALSE,na.string=".")
CC_window<-transform(CC_window,altCount<-as.numeric(altCount),refCount<-as.numeric(refCount))
print(head(CC_window))

CC_window<-transform(CC_window,altRatio<-as.numeric(altCount/refCount))

CC_window$altRatio <- CC_window$altCount/CC_window$refCount

CC_w<-CC_window[CC_window$altCount != 0,]
print(head(CC_w))

jpeg("CC_window.jpg")
#plot(hist(CC_w$altRatio,breaks="FD",
#   main=paste("CC alt reads")))
ggplot(data=CC_w,aes(CC_w$altRatio)) + geom_histogram(binwidth=0.01) + xlim(c(0,1))
dev.off()



