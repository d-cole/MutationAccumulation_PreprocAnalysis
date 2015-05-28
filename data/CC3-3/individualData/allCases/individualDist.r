setwd("~/Documents/spirodela/data/CC3-3/individualData/allCases/")
files <-list.files(path="~/Documents/spirodela/data/CC3-3/individualData/allCases/",
                   pattern="*.csv",full.names=F,recursive=FALSE)
remExt <- function(x,ext){
  return (sub(ext,"",x))
}
l <-vector('list',length(files))
for (i in 1:length(files)){
    sData<-read.csv(files[i])
    l[[i]]<-median(sData$DP)
    names(l)[i]<-remExt(files[i],".csv")
}
do.call(cbind,l)
write.table(l,file="ind_DP_med.csv",append=FALSE,sep=" ",
            eol="\n",na = "NA",dec=".",row.names=FALSE,
            col.names=TRUE)


