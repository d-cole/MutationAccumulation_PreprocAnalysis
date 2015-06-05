setwd("~/Documents/spirodela/data/GP2-3/individualData/")
files <-list.files(path="~/Documents/spirodela/data/GP2-3/individualData/",
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
write.table(l,file="ind_DP_med_v2.csv",append=FALSE,sep=" ",
            eol="\n",na = "NA",dec=".",row.names=FALSE,
            col.names=TRUE)


