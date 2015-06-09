args <- commandArgs(TRUE)
if(length(args) < 1) {
    cat("Please specify location of .csv file")
}
all_samples<-read.csv(args,stringsAsFactors=FALSE,na.string=".")

print("Individual counts")
sample_names = unique(all_samples$odd_sample)
samples <- list()
invisible(lapply(sample_names,function(x) print(paste(x,NROW(all_samples[all_samples$odd_sample==x,]),sep=": "))))
