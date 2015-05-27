setwd("~/Documents/spirodela/data/CC3-3/individualData/allCases/")
files <-list.files(path="~/Documents/spirodela/data/CC3-3/individualData/allCases/",
                   pattern="*.csv",full.names=F,recursive=FALSE)
remExt <- function(x,ext){
  return (sub(ext,"",x))
}



lapply(files, function(x) {
  sData<-read.csv(x)
  head(sData)
  x_name<-remExt(x,".csv")
  med_dp<-median(sData$DP,na.nm=TRUE)
  print(paste(x_name,": ",med_dp,sep=""))
}

