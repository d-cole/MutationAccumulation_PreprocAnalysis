#!/usr/bin/Rscript

args <- commandArgs(TRUE)
if(length(args) < 1) {
  cat("Please specify location of .csv file \n")
}

#Read in csv file
all_samples<-read.csv(args,stringsAsFactors=FALSE,na.string=".")

median_na<-function(x){
    median(x[which(!is.na(x))])
}


mean_na<-function(x){
    mean(x[which(!is.na(x))])
}


mode_na<-function(x){
    mode(x[which(!is.na(x))])
}



#apply(all_samples,2,median_na)

#apply(all_samples,2,mean_na)


jpeg("CCB_depths.jpg")
plot(hist((all_samples$CC_B),prob=F,breaks="FD"),
    main="",xlab="")
dev.off()





