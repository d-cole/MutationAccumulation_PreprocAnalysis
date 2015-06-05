#Given a vcf file, writes all filtered variant sites to a specified output file.
import sys

#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  CC_B    CC_C    CC_D    CC_E    CC_F    CC_G    CC_H    CC_I    CC_J    CC_K    CC_L    CC_M    CC_N    CC_O
#pseudo0 1       .       C       .       1.51    LowQual AN=28;DP=131;MQ=73.45;MQ0=6     GT:DP   0/0:12  0/0:7   0/0:13  0/0:12  0/0:6   0/0:7   0/0:7   0/0:9   0/0:9   0/0:13  0/0:9   0/0:8   0/0:6   0/0:13

#pseudo0 19      .       G       A       287.25  .       AC=10;AF=0.357;AN=28;BaseQRankSum=-1.618;DP=184;Dels=0.03;FS=0.886;HaplotypeScore=37.0798;InbreedingCoeff=-0.4921;MLEAC=9;MLEAF=0.321;MQ=75.64;MQ0=6;MQRankSum=-0.968;QD=2.16;ReadPosRankSum=1.739;SOR=0.786    GT:AD:DP:GQ:PL  0/1:16,2:18:31:31,0,561 0/1:6,2:8:47:47,0,215   0/0:16,0:16:42:0,42,521 0/1:14,3:17:81:81,0,374 0/1:5,3:8:22:22,0,165   0/0:10,0:10:18:0,18,244 0/0:9,0:9:24:0,24,325   0/1:8,3:11:36:36,0,244  0/1:13,1:14:1:1,0,415   0/1:13,2:15:37:37,0,377 0/0:14,0:14:39:0,39,510 0/1:10,4:14:32:32,0,368 0/1:3,2:5:58:58,0,73    0/1:17,2:20:3:3,0,438i


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

###### FILTER PARAMETERS ######
MAX_IMPURE_F1 = 3
MIN_MAP_QUALITY = 20
MIN_IMPURE_READS = 1
MIN_ALT_READ = 3
MIN_GQ = 60
MIN_F0_DP = 10
FILTER_TXF1_F4 = True

MIN_MQ = 00
MIN_QD = 2.0
MAX_FS = 60.0
MIN_MQ_RANK_SUM = -12.5
MIN_READ_POS_RANK_SUM = -8.0
##### END OF FILTER PARAM. #####


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

def filterSamples(samples,line,
        one00rest01,one00rest11,
        one01rest11,one01rest00,
        one11rest00,one11rest01,other):
    """
    """
    gt_counts={}
    for s in samples:
        if validSample(s):
            s_col = s.split(":") #Should filter all genotype quality > 60?
            if consistantReads(0,0):
                gt_counts[s_col[0]] = gt_counts.get(s_col[0],0) + 1
            else:
                return False
        else:
            return False

    if (1 in gt_counts.values() and 13 in gt_counts.values()):
        write = False
        #Homz ref odd one 
        if gt_counts.get("0/0") == 1 and gt_counts.get("0/1") == 13:
            one00rest01.write(line)           
            write = True
        if gt_counts.get("0/0") == 1 and gt_counts.get("1/1") == 13:
            one00rest11.write(line)            
            write = True            
        #Hetz odd one 
        if gt_counts.get("0/1") == 1 and gt_counts.get("1/1") == 13:
            one01rest11.write(line)
            write = True
        if gt_counts.get("0/1") == 1 and gt_counts.get("0/0") == 13:
            one01rest00.write(line)        
            write = True   
        #Homz alt odd one    
        if gt_counts.get("1/1") == 1 and gt_counts.get("0/0") == 13:
           one11rest00.write(line)
           write = True 
        if gt_counts.get("1/1") == 1 and gt_counts.get("0/1") == 13:
           one11rest01.write(line) 
           write = True
        if not write:
           other.write(line)
        return True

def consistantReads(AD,DP):
    """
    GT:AD:DP:GQ:PL  0/1:16,2:18:31:31
    """
#    AD_REF = AD.split(",")[0]
#    AD_ALT = AD.split(",")[1]
    return True
    #return (float(AD_REF) / float(DP) >= 0.9) or (float(AD_ALT) / float(DP) >= 0.9)

def filterMapQuality(line_col):
    """
    Return true if variant info passes all filters
    """
    info = line_col[INFO].split(";")
    if line_col[ALT] != ".":
        return float(line_col[QUAL]) >= MIN_MAP_QUALITY
        #return line_col[FILTER] != "LowQual"
 #       getInfoValue("MQ",info) >= MIN_MQ and \
 #       getInfoValue("QD",info) >= MIN_QD and \
 #       getInfoValue("FS",info) <= MAX_FS and \
 #       getInfoValue("MQRankSum",info) >= MIN_MQ_RANK_SUM and \
 #       getInfoValue("ReadPosRankSum",info) >= MIN_READ_POS_RANK_SUM

    return True

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
                "#MIN_MAP_QUALITY: " + str(MIN_MAP_QUALITY) + "\n"
#                "#MIN_IMPURE_READS: " + str(MIN_IMPURE_READS) + "\n" + \
#                "#MIN_ALT_READ: " + str(MIN_ALT_READ) +  "\n" +\
#                "#MIN_GQ: " + str(MIN_GQ) +  "\n" +\
#                "#MIN_MQ(info): " + str(MIN_MQ) + "\n" +\
#                "#MIN_QD: " + str(MIN_QD) + "\n" +\
#                "#MAX_FS: " + str(MAX_FS) + "\n" +\
#                "#MIN_MQ_RANK_SUM: " + str(MIN_MQ_RANK_SUM) + "\n" +\
#                "#MIN_READ_POS_RANK_SUM: " + str(MIN_READ_POS_RANK_SUM) + "\n"

    outFile.write(filters)
    return
    
if __name__ == "__main__":
    file_name,out_name = sys.argv[1],sys.argv[2]
    outFile = open(out_name,'w')
    #removedBases = open('remBases.txt','w')
    #invalidLines = open('invalidLines.ttxt','w')
    writeFilters(outFile)
    #Create files to write calls based on 1/14 odd GT
    one00rest11 = open("one00rest11.txt","w")
    one00rest01 = open("one00rest01.txt","w")
    one01rest00 = open("one01rest00.txt","w")
    one01rest11= open("one01rest11.txt","w")
    one11rest00 = open("one11rest00.txt","w")
    one11rest01 = open("one11rest01.txt","w")
    other = open("other.txt","w")
    with open(file_name) as f:
        for line in f:
            if isDataLine(line): #Check if line contains variant data
                line_col = str.split(line)
                if filterMapQuality(line_col):

                    if filterSamples(line_col[9:23],line,
                            one00rest01,one00rest11,
                            one01rest11,one01rest00,
                            one11rest00,one11rest01,other):
                        outFile.write(line)
                else:
                    pass
                    #removedBases.write(line)
            else:
                pass
                #invalidLines.write(line)
    f.close()
    outFile.close()
    one00rest11.close()
    one00rest01.close()
    one01rest00.close()
    one01rest11.close()
    one11rest00.close()
    one11rest01.close()







