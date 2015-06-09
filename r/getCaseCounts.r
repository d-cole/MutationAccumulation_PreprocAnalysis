source("plotGQ.r")
args <- commandArgs(TRUE)
if(length(args) < 1) {
    cat("Please specify location of .csv file")
}
all_samples<-read.csv(args,stringsAsFactors=FALSE,na.string=".")

#print("Mutation case counts")
odd_GT = unique(all_samples$odd_GT)
cohort_GT = unique(all_samples$cohort_GT)

cat("odd_GT   Cohort_GT    mCount   \n")
for (s_gt in odd_GT) {
    for(c_GT in cohort_GT){
        if (s_gt != c_GT){
            cat(paste(s_gt,c_GT,"    ",sep="       "))
            cat(NROW(all_samples[all_samples$odd_GT==s_gt & all_samples$cohort_GT==c_GT,]))
            cat("\n")
            
            #if (NROW(all_samples[all_samples$odd_GT==s_gt & all_samples$cohort_GT==c_GT,]) != 0){
            #    plotGQ(all_samples[all_samples$odd_GT==s_gt & all_samples$cohort_GT==c_GT,],paste("CC3-3_f4_","o",gsub("/",".",s_gt),":c",gsub("/",".",c_GT),".jpg",sep=""),paste("Genotype Quality: CC3-3_f4 oddGT:",s_gt,"  cohortGT:",c_GT," n = ",NROW(all_samples[all_samples$odd_GT==s_gt & all_samples$cohort_GT==c_GT,]),sep=""))
            }
        }
    }
}
