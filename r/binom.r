#!/usr/bin/Rscript

#Commandline arg info from http://www.r-bloggers.com/parse-arguments-of-an-r-script/
args <- commandArgs(TRUE)
if(length(args) < 1) {
  cat("Please specify location of .csv file \n")
}


binom <- function(alt,ref){
    n<- alt+ref
    if (pbinom(alt,n,0.5) > 0.02){
        return(TRUE)
    }
#    print(alt)
#    print(ref)
#    print(pbinom(alt,n,0.5))
    return(FALSE)
}


print(binom(as.numeric(args[1]),as.numeric(args[2])))















