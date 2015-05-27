library(ggplot2)
setwd("~/Documents/spirodela/sampleData/CC3-3/allsites/")
files <- list.files(path="~/Documents/spirodela/sampleData/CC3-3/allsites/",
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
        sub<-sapply(subset(data,CHROM==chrom,select=POS),as.numeric)
        plot(hist(sub,prob=F,breaks=length(sub)),
             main=paste(name,chrom,".jpg",sep="_"),
             xlab="Position")
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






