setwd("/Users/Daniel/Documents/vcfParsing/spirodela/data/...")
files <-list.files(path="/Users/Daniel/Documents/vcfParsing/spirodela/...",
                   pattern="*.csv",full.names=F,recursive=FALSE)
remExt <- function(x,ext){
  return (sub(ext,"",x))
}



lapply(files, function(x) {
  sData<-read.csv(x)
  head(sData)
  x_name<-remExt(x,".csv")
  jpeg(paste(x_name,".jpg",sep=""))
  plot(hist(sData$DP,prob=F,breaks=200),xlim=c(0,125),
       main=paste(x_name,"DP Homz. Ref",sep=" "),
       xlab="Depth")
  dev.off()
})




