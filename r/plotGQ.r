args <- commandArgs(TRUE)
if(length(args) < 1) {
    cat("Please specify location of .csv file")
}
all_samples<-read.csv(args,stringsAsFactors=FALSE,na.string=".")

jpeg(paste("GP2-3_f6","_oddGQ.jpg",sep=""))
plot(hist(all_samples$odd_GQ,prob=F,100),
   main=paste("GP2-3_f6","_oddGQ",sep=""),
   xlab="Genotype Quality")
dev.off()



plotGQ <- function(data,file_name,title){
    jpeg(file_name)
    print(head(data$odd_GQ))
    plot(hist(data$odd_GQ,prob=F,100),
        main=title,
        xlab="Genotype Quality")
    dev.off()

}
