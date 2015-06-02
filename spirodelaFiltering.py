import sys
#Sample format
# GT:AD:DP:GQ:PL
GT,AD,DP,GQ,PL = 0,1,2,3,4;
#Line format
ALT,QUAL,FILTER,INFO = 4,5,6,7
HETZ = "0/1"
HOMZ_REF = "0/0"
HOMZ_ALT = "0/0"
#INFO indexes
MQ,QD,FS,MQ_RANK_SUM,READ_POS_RANK_SUM=11,14,6,13,15
SAMPLE_MEDIANS = []

###### FILTER PARAMETERS ######
MAX_IMPURE_F1 = 3
MIN_MAP_QUALITY = 20
MIN_IMPURE_READS = 1
MIN_ALT_READ = 3
MIN_GQ = 60
MIN_F0_DP = 10
FILTER_TXF1_F4 = True

MIN_MQ = 40
MIN_QD = 2.0
MAX_FS = 60.0
MIN_MQ_RANK_SUM = -12.5
MIN_READ_POS_RANK_SUM = -8.0
#Set at 2/3rds of number of samples
MIN_VALID_SAMPLES_DP = int(14.0*(2.0/3.0))
##### END OF FILTER PARAM. #####

SAMPLES = ["CC3-3_B","CC3-3_C","CC3-3_D","CC3-3_E","CC3-3_F","CC3-3_G",\
"CC3-3_H","CC3-3_I","CC3-3_J","CC3-3_K","CC3-3_L","CC3-3_M","CC3-3_N","CC3-3_O"]
SAMPLE_COUNT = [0]*14
SAMPLE_GT_COUNT=[{"0/0":0,"0/1":0,"1/1":0}]*14


def isDataLine(line):
    """
    Determines if the line in the vcf file contains
    data 
    """
    if len(line) > 1:
        return line[0] != "#"
    return False

def validSample(sample):
    """
    Returns if a sample is valid
    """
    return "./." not in sample

def getSampleMedians(medianFile):
    medFile = open(medianFile,"r")
    for i, line in enumerate(medFile):
        if i == 1:
            SAMPLE_MEDIANS = [[float(i)*0.5,float(i)*1.5] for i in line.strip("\n").split(" ")]
    return SAMPLE_MEDIANS

def validSampleDP(sample_idx,DP):
    DP = float(DP)
    if DP >= SAMPLE_MEDIANS[sample_idx][0] and DP <= SAMPLE_MEDIANS[sample_idx][1]:
            return True 
    return False

def filterSamples(samples,line):
    """
    Requirements to pass sample filters
        - No missing samples
        - At least 2/3 samples pass individual
            DP filters
        - One sample GT must be different than others
            - This samples must pass individual DP filters 
    """
    numValidDP = 0
    gt_counts={}

    for i in range(0,len(samples)):
        if validSample(samples[i]):
            s_col = samples[i].split(":")
            if validSampleDP(i,s_col[DP]):
                numValidDP += 1
            if consistantReads(s_col[AD],s_col[DP]):
                gt_counts[s_col[0]] = gt_counts.get(s_col[0],0) + 1
            else:
                return False
        else:
            return False 

    if numValidDP < MIN_VALID_SAMPLES_DP:
        #less than ~2/3 of samples pass DP filters
        return False 
    
    if (1 in gt_counts.values() and 13 in gt_counts.values()):
        #one of the GT is different than the rest
        if validateMutant(gt_counts,samples):
            return True
        else:
            #1 different GT did not pass filters
            return False

def validateMutant(gt_counts,samples):
    """
    Ensures that odd one out passes its depth filters
    """
    for key in gt_counts.keys():
        if gt_counts.get(key) == 1:
            break

    for i in range(0,len(samples)):
        if key in samples[i]:
            break
    SAMPLE_COUNT[i] = SAMPLE_COUNT[i] + 1
    s_col = samples[i].split(":")
    try:
        SAMPLE_GT_COUNT[i][s_col[GT]] = SAMPLE_GT_COUNT[i].get(s_col[GT],0) + 1
    except:
        print(SAMPLE_GT_COUNT[i].get(s_col[GT],"0"))
        print(s_col[GT])
        sys.exit()
    return validSampleDP(i,samples[i].split(":")[DP])

def writeCounts(outFile):
    """
    Writes count data to specified file
    """
    for i in range(0,len(SAMPLES)):
        outFile.write(SAMPLES[i] + ": " + str(SAMPLE_COUNT[i]) +  str(SAMPLE_GT_COUNT[i]) + "\n")  
        outFile.write(str(SAMPLE_GT_COUNT))  
    return

def consistantReads(AD,DP):
    """
    GT:AD:DP:GQ:PL  0/1:16,2:18:31:31
    Currently not used
    """
    #AD_REF = AD.split(",")[0]
    #AD_ALT = AD.split(",")[1]
    return True
    #return (float(AD_REF) / float(DP) >= 0.9) or (float(AD_ALT) / float(DP) >= 0.9)

def filterMapQuality(line_col):
    """
    Return true if variant info passes all filters
    """
    info = line_col[INFO].split(";")
    if line_col[ALT] != ".":
        return float(line_col[QUAL]) >= MIN_MAP_QUALITY and \
        line_col[FILTER] != "LowQual" and \
        getInfoValue("MQ",info) >= MIN_MQ and \
        getInfoValue("QD",info) >= MIN_QD and \
        getInfoValue("FS",info) <= MAX_FS and \
        getInfoValue("MQRankSum",info) >= MIN_MQ_RANK_SUM and \
        getInfoValue("ReadPosRankSum",info) >= MIN_READ_POS_RANK_SUM

    return False

def getInfoValue(tag,info_list):
    """
    Returns the value of a given tag. If tag not found return valid value,
    does not filter out when tag does not exist
    """
    for val in info_list:
        valIdx = val.find(tag)
        if valIdx != -1:
            return  float(val[valIdx + len(tag) + 1:])
    return  {"MQ":MIN_MQ + 1,"QD":MIN_QD + 1,"FS":MAX_FS - 1,"MQRankSum":MIN_MQ_RANK_SUM + 1,"ReadPosRankSum":MIN_READ_POS_RANK_SUM + 1}[tag]


def writeFilters(outFile):
    """
    Writes the filter parameters to file
    """
    filters = "##FILTER PARAMETERS##" + "\n" + \
                "#MIN_MAP_QUALITY: " + str(MIN_MAP_QUALITY) + "\n" + \
                "#MIN_IMPURE_READS: " + str(MIN_IMPURE_READS) + "\n" + \
                "#MIN_ALT_READ: " + str(MIN_ALT_READ) +  "\n" +\
                "#MIN_GQ: " + str(MIN_GQ) +  "\n" +\
                "#MIN_MQ(info): " + str(MIN_MQ) + "\n" +\
                "#MIN_QD: " + str(MIN_QD) + "\n" +\
                "#MAX_FS: " + str(MAX_FS) + "\n" +\
                "#MIN_MQ_RANK_SUM: " + str(MIN_MQ_RANK_SUM) + "\n" +\
                "#MIN_READ_POS_RANK_SUM: " + str(MIN_READ_POS_RANK_SUM) + "\n"

    outFile.write(filters)
    return
    
if __name__ == "__main__":

    SAMPLE_MEDIANS = getSampleMedians("/Users/Daniel/Documents/spirodela/data/CC3-3/individualData/allCases/ind_DP_med.csv")
    file_name,out_name= sys.argv[1],sys.argv[2]
    outFile = open(out_name,'w')
    writeFilters(outFile)

    with open(file_name) as f:
        for line in f:
            if isDataLine(line): #Check if line contains variant data
                line_col = str.split(line)
                if filterMapQuality(line_col):
                    if filterSamples(line_col[9:24],line):
                        outFile.write(line)
            else:
                #info line
                outFile.write(line)

    count_out = open("sampleCounts","w")
    writeCounts(count_out)

    count_out.close()
    f.close()
    outFile.close()








