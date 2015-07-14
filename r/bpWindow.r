args <- commandArgs(TRUE)
<<<<<<< HEAD
if(length(args) < 2) {
=======
if(length(args) < 1) {
>>>>>>> f7ff8ac3b3b76196c721602384e7519d8e91ef6e
  cat("Please specify location of .csv file \n")
}

#Read in csv file
CC_window<-read.csv(args[1],stringsAsFactors=FALSE,na.string=".")
GP_window<-read.csv(args[2],stringsAsFactors=FALSE,na.string=".")

print(head(CC_window))
print(head(GP_window))

<<<<<<< HEAD
print(CC_window$altCount)
print(CC_window[CC_window$altCount != 0,])

=======
>>>>>>> f7ff8ac3b3b76196c721602384e7519d8e91ef6e
jpeg("CC_window.jpg")
plot(hist(CC_window$altCount,prob=F,breaks="FD",
   main=paste("CC alt reads")))
dev.off()


jpeg("GP_window.jpg")
plot(hist(GP_window$altCount,prob=F,breaks="FD",
    main=paste("GP alt reads")))
dev.off()



