setwd("~/Documents/spirodela/sampleData/CC3-3/")
files <- list.files(path="~/Documents/spirodela/sampleData/CC3-3/",
                    pattern="*.csv",full.names=F,recursive=FALSE)

remExt <- function(x,ext){
    return (sub(ext,"",x))
}

lapply(files,function(x) {
    data<-read.csv(x,stringsAsFactors=FALSE,na.string=".")
    typeof(data$DP)
    print(head(data))
    name<-remExt(x,".csv")
    jpeg(paste(name,"_DP.jpg",sep=""))
    plot(hist(data$DP,prob=F,breaks=length(data$DP)),
        main=paste(name,"DP",sep=" "),
        xlab="Depth")
    dev.off()

})






