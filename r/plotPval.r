library(ggplot2)
library("reshape2")

args <- commandArgs(TRUE)
if(length(args) < 2) {
  cat("Please specify location of .csv file & name of output file\n")
}

#Read in csv file
readVals<-read.csv(args[1],stringsAsFactors=FALSE,na.string=".")
name <- (args[2])

readVals<-transform(readVals,pVal<-as.numeric(pVal))
readVals$altRef<-readVals$AD_alt/readVals$AD_ref

#samples<-unique(readVals$sample)
#print(samples)
#for(s in samples){
#    sample_data <- readVals[readVals$sample == s,6]
#    print(NROW(sample_data))
#    print(head(sample_data))
#    plot <- ggplot() + aes(sample_data) + geom_histogram()
#    ggsave(plot,file=paste(name,s,".jpg",sep=""))
#}
#print(head(readVals))
#plot_alt_ref <- ggplot() + aes(readVals[readVals$AD_alt > 7,6]) + geom_histogram(binwidth = 0.1) + coord_cartesian(xlim=c(0,5))
#ggsave(plot_alt_ref,file=paste(name,"_alt_ref.jpg",sep=""))

#plot_pVal <- ggplot() + aes(readVals[readVals$AD_alt > 5,5]) + geom_histogram(binwidth = 0.01)
#ggsave(plot_pVal,file=paste(name,"_pVal.jpg",sep=""))

##plot_alt <- ggplot() + aes(readVals[readVals$AD_alt > 5,3]) + geom_histogram()
#ggsave(plot_alt,file=paste(name,"_alt.jpg",sep=""))

plot <- ggplot(readVals,aes(GQ,AD_alt)) + geom_scatter()
ggsave(plot,file=paste(name,"_GQ_Pval.jpg",sep=""))


#    print(col)
#    pValues <-transform(pValues,col<-as.numeric(col))
#    col_data  <- pValues[,col]
#    plot <- ggplot() + aes(col_data) + geom_histogram()
#    ggsave(plot,file=paste(name,col,".jpg",sep=""))
#}
