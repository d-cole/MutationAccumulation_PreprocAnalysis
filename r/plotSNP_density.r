library(ggplot2)
args <- commandArgs(TRUE)
pos_idx <- 3
lapply(args,function(x) {
    data<-read.csv(x,stringsAsFactors=FALSE,na.string=".")
    name<-sub(".csv","",x)
    data<-transform(data,POS=as.numeric(POS))

    window_size<-1000

    chromosomes = unique(data$CHROM)
    for(chrom in chromosomes){
        pos_data<-sapply(subset(data,CHROM==chrom,select=POS),as.numeric)
        min_pos = min(pos_data)
        max_pos = max(pos_data)

        break_seq = seq(from=min_pos,to=max_pos + window_size,by=window_size)

        png(file=paste(name,chrom,".jpg",sep="_"))
        plot(hist(data[data$CHROM == chrom,pos_idx],prob=F,break_seq),
             main=paste(name,chrom,".jpg",sep="_"),ylim=c(0,35),
             xlab="Position")

    dev.off()

    }    
})


#For printing multiple graphs on one page
# chromosomes = unique(data$CHROM)
#     rowcol = ceiling(sqrt(length(chromosomes)))
#     #Plots SNP distributions for every chromosome
#     png(file=paste(name,"chromosomes",".jpg",sep="_"),width=480*rowcol,height=480*rowcol)
#     #jpeg(paste(name,"chromosomes",".jpg",sep="_"))
#     par(mfcol=c(rowcol,rowcol), oma=c(1,1,0,0), mar=c(1,1,1,0), tcl=-0.1, mgp=c(0,0,0))
#     #par(mfrow = c(length(chromosomes)%/%2 + 1,2),mar=c(35,35,35,35))
#     for(chrom in chromosomes){
#         sub<-sapply(subset(data,CHROM==chrom,select=POS),as.numeric)
#         plot(hist(sub,prob=F,breaks=length(sub)),
#              main=paste(name,chrom,".jpg",sep="_"),
#              xlab="Position")
# #        dev.off()






