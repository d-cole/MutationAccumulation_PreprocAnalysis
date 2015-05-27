setwd("~/Documents/spirodela/sampleData/CC3-3/one01rest00")
files <- list.files(path="~/Documents/spirodela/sampleData/CC3-3/one01rest00",
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

    #Plots SNP distributions for every chromosome
    chromosomes = unique(data$CHROM)
    for(chrom in chromosomes){
        print(chrom)
        sub<-sapply(subset(data,CHROM==chrom,select=POS),as.numeric)
        print(sub)
        jpeg(paste(name,chrom,".jpg",sep="_"))
        plot(hist(sub,prob=F,breaks=length(sub)),
             main=paste(name,chrom,".jpg",sep="_"),
             xlab="Position")
        dev.off()

    }    
    
})







