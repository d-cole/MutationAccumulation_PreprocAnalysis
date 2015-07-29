library(ggplot2)
library("reshape2")

args <- commandArgs(TRUE)
if(length(args) < 2) {
  cat("Please specify location of .csv file & name of output file\n")
}

binom <- function(alt,ref){
    n<- alt+ref
    return(pbinom(alt,n,0.5)[1])
}

#Read in csv file
readVals<-read.csv(args[1],stringsAsFactors=FALSE,na.string=".")
readVals <- transform(readVals,AD_alt <- as.numeric(AD_alt),AD_ref <- as.numeric(AD_ref))
print(head(readVals))

for(i in 1:nrow(readVals)){
    readVals[i,37] <- binom(readVals[i,28],readVals[i,29])
}
name <- (args[2])

write.csv(readVals[,c(26,28,29,37)],file=paste(name,".csv",sep=""))



#    print(col)
#    pValues <-transform(pValues,col<-as.numeric(col))
#    col_data  <- pValues[,col]
#    plot <- ggplot() + aes(col_data) + geom_histogram()
#    ggsave(plot,file=paste(name,col,".jpg",sep=""))
#}



