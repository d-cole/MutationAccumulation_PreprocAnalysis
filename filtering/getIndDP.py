import sys
from filterMethods import filterMethods

sampleDepths = [0]*12

def addDepths(sampleDepths,samples,altSite):
    #samples should be of length 12: samples [9:21)
    DPidx = 1
    if altSite:
       DPidx = 2     

    for i in range(0,len(samples)):
        if "./." not in samples[i]:
            s_col = samples[i].split(";")  
            samplesDepth[i].append(int(s_col[DPidx]))
    return


if __name__ == "__main__":
    filterManager = filterMethods()

    vcf_loc = sys.argv[1]
    with open(vcf_loc) as file:
        for line in file:
            if filterManager.isDataLine(line):
                sline = str.split(line)
                addDepths(sampleDepths,sline[9:21],sline[ALT] != ".")                   

    print sampleDepths












