args <- commandArgs(TRUE)
if(length(args) < 1) {
    cat("Please specify location of .csv file")
}
all_samples<-read.csv(args,stringsAsFactors=FALSE,na.string=".")

jpeg(paste("CC3-3_f0","_oddGQ.jpg",sep=""))
plot(hist(all_samples$odd_GQ,prob=F,100),
   main=paste("CC3-3_f0","_oddGQ",sep=""),
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