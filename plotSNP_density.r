#Plots sample depth and distribution on chromosomes given a .csv file
library(ggplot2)
setwd("~/Documents/spirodela/data/CC3-3/readData/allSites/graphs/")
files <- list.files(path="~/Documents/spirodela/data/CC3-3/vcfFiltes/dpFilters/",
                    pattern="*.csv",full.names=F,recursive=FALSE)

remExt <- function(x,ext) {
    #Removes the provided extension
    return (sub(ext,"",x))
}

lapply(files,function(x) {
    data<-read.csv(x,stringsAsFactors=FALSE,na.string=".")
    name<-remExt(x,".csv")
    
    #Plots depth
    jpeg(paste(name,"_DP.jpg",sep=""))
    plot(hist(data$DP,prob=F,breaks=length(data$DP)),
        main=paste(name,"DP",sep=" "),
        xlab="Depth")
    dev.off()

    chromosomes = unique(data$CHROM)
    for(chrom in chromosomes){
        png(file=paste(name,chrom,".jpg",sep="_"))
        pos_data<-sapply(subset(data,CHROM==chrom,select=POS),as.numeric)
        #plot(hist(pos_data,prob=F,breaks=length(pos_data)),
        #     main=paste(name,chrom,".jpg",sep="_"),
        #     xlab="Position")

        qplot(pos_data, binwidth = 1.0,geo="histogram",xlab="Position",ylab="Freq")
        dev.off()

    }    
})


#For printing multiple graphs on one page
# chromosomes = unique(data$CHROM)
#     rowcol = ceiling(sqrt(length(chromosomes)))
#     #Plots SNP distributions for every chromosome
#     png(file=paste(name,"chromosomes",".jpg",sep="_"),width=480*rowcol,height=480*rowcol)
#     #jpeg(paste(name,"chromosomes",".jpg",sep="_"))
#     par(mfcol=c(rowcol,rowcol), oma=c(1,1,0,0), mar=c(1,1,1,0), tcl=-0.1, mgp=c(0,0,0))
#     #par(mfrow = c(length(chromosomes)%/%2 + 1,2),mar=c(35,35,35,35))
#     for(chrom in chromosomes){
#         sub<-sapply(subset(data,CHROM==chrom,select=POS),as.numeric)
#         plot(hist(sub,prob=F,breaks=length(sub)),
#              main=paste(name,chrom,".jpg",sep="_"),
#              xlab="Position")
# #        dev.off()






