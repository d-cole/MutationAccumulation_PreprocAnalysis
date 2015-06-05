setwd("/Users/Daniel/Documents/spirodela/data/CC3-3/readData/allSites")
files <-list.files(path="/Users/Daniel/Documents/spirodela/data/CC3-3/readData/allSites",
                   pattern="*.csv",full.names=F,recursive=FALSE)
remExt <- function(x,ext){
  return (sub(ext,"",x))
}



lapply(files, function(x) {
  sData<-read.csv(x)
  head(sData)
  x_name<-remExt(x,".csv")
  jpeg(paste(x_name,"_HapScore.jpg",sep=""))
  plot(hist(sData$HaplotypeScore,prob=F,length(sData$HaplotypeScore)),xlim=c(0,5),
       main=paste(x_name,"Haplotye Score",sep=" "),
       xlab="Haplotype Score")
  dev.off()
})




