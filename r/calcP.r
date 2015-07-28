#!/usr/bin/Rscript

args <- commandArgs(TRUE)
if(length(args) < 1) {
  cat("Please specify location of .csv file \n")
}

binom <- function(alt,ref){
    n<- alt+ref
    return(pbinom(alt,n,0.5)[1])
}

print(binom(as.numeric(args[1]),as.numeric(args[2])))

