import sys
"""
variantInfoCSV.py
Creates a .csv file with the variant information
"""

#SAMPLE INDICES
GT,AD,sDP,GQ,PL = 0,1,2,3,4

HETZ = "0/1"
MIN_GQ = 60
INFO = 7
MIN_ALT_READ = 3



#INFO INDICES
AC,AF,AN,BaseQRankSum,DP,Dels,FS,HaplotypeScore, \
InbreedingCoeff,MLEAC,MLEAF,MQ,MQ0,MQRankSum,QD,\
ReadPosRankSum = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15

COLUMNS = "\"varID\",\"CHROM\",\"POS\",\"REF\",\"ALT\",\"QUAL\",\"FILTER\",\
\"AC\",\"AF\",\"AN\",\"BaseQRankSum\",\"siteDP\",\"Dels\",\"FS\",\
\"HaplotypeScore\",\"InbreedingCoeff\",\"MLEAC\",\"MLEAF\",\"MQ\",\
\"MQ0\",\"MQRankSum\",\"QD\",\"ReadPosRankSum\",\"SOR\""

INFO_TAGS = ['AC','AF','AN','BaseQRankSum','DP','Dels','FS','HaplotypeScore','InbreedingCoeff','MLEAC',\
'MLEAF','MQ','MQ0','MQRankSum','QD','ReadPosRankSum','SOR']

SAMPLE_COLUMNS = ',\"odd_GT\",\"odd_sample\",\"cohort_GT\",\"AD_alt\",\"AD_ref\",\"odd_DP\",\"AD_altSum\",\"AD_refSum\",\"odd_GQ\",\"odd_PL\",\"Anc_GT\",\"Anc_sample\"'

SAMPLES_CC = ["CC3-3_B","CC3-3_C","CC3-3_D","CC3-3_E","CC3-3_F","CC3-3_G",\
"CC3-3_H","CC3-3_I","CC3-3_J","CC3-3_K","CC3-3_L","CC3-3_M","CC3-3_N","CC3-3_O"]


SAMPLES_GP = ["GP2-3_B", "GP2-3_C", "GP2-3_D", "GP2-3_E", "GP2-3_F", "GP2-3_G",\
 "GP2-3_H", "GP2-3_I", "GP2-3_J", "GP2-3_K", "GP2-3_L", "GP2-3_M", "GP2-3_N", "GP2-3_O"]


def isDataLine(line):
    """
    Determines in line contains site data
    """
    if len(line) > 1:
        return line[0] != "#"
    return False

def writeColumns(outFile):
    """
    Writes column names to the .csv file
    """
    outFile.write(COLUMNS + SAMPLE_COLUMNS + "\n")

    return

def getValue(tag,info_list):
    """
    Returns the value of a given tag, returns "." if not found
    """
    for val in info_list:
        valIdx = val.find(tag)
        if valIdx != -1:
            return "\"" + val[valIdx + len(tag) + 1:] + "\""
    return "\".\"" 


def getSampleString(samples):
    """
    Pareses the samples and returns a string to write to the .csv file
    """
    odd_idx = None
    gt_dict = {}
    ad_alt_sum = 0
    ad_ref_sum = 0
    csv_string = ""

    #Build dict mapping GT to a list of sample indexes that have that GT
    for i in range(0,len(samples)):
        s_col = samples[i].split(":")
        gt = s_col[GT]
        ad_split = s_col[AD].split(",")
        ad_alt = float(ad_split[1])
        ad_ref = float(ad_split[0])

        ad_alt_sum = ad_alt_sum + ad_alt
        ad_ref_sum = ad_ref_sum + ad_ref
        gt_dict.setdefault(gt,[]).append(i)
    #The GT with one index is the odd GT
    #append oddGT to the csv_string
    for key in gt_dict.keys():
        if len(gt_dict[key]) == 1:
            odd_idx = gt_dict[key][0]
            csv_string = '"' + key + '"' + ','
    odd_sample = samples[odd_idx].split(":")
    
    #Add which sample was the odd one out
    csv_string = csv_string + '"' + SAMPLES_CC[odd_idx] +'",'

    #Add the cohortGT the GT that maps to 13 samples
    for key in gt_dict.keys():
        if len(gt_dict[key]) == 13:
            csv_string = csv_string + '"' + key + '"' + ','

    #Add ADalt and ADref to csv string
    csv_string = csv_string + '"' + odd_sample[AD].split(",")[1] + '","' + odd_sample[AD].split(",")[0] + '",'
    
    #Add odd_DP to csv string
    csv_string = csv_string + '"' + odd_sample[sDP] + '",'    

    #add ADaltSum and ADrefSum to the csv_string
    csv_string = csv_string + '"' + str(ad_alt_sum) + '",' + '"' + str(ad_ref_sum) + '",'

    csv_string = csv_string + '"' + odd_sample[GQ] + '",'
    #Add PL to csv_string
    csv_string = csv_string + '"' + odd_sample[PL] + '"'

    return csv_string

def getAncestorInfo(ancestor):
    anc_string = ""
    if ancestor != ".":
        anc_col = ancestor.split(":")
        anc_string = anc_string + ',"' + anc_col[-1] + '","' + ":".join(anc_col[0:len(anc_col) - 1]) + '"'
        return anc_string
    else:
        return ',".","."'

def writeInfo(line,outFile):
    """
    Writes data for the variant site to a .csv file
    """
    line_col = str.split(line)

    infoData = []
    for tag in INFO_TAGS:
        infoData.append(getValue(tag,line_col[INFO].split(";")))

    #Initialize csvLine to be written to .csv file
    csvLine = ""
    #ID=CHROM:POS
    csvLine = csvLine + "\"" + line_col[0] + ":" + line_col[1] + "\","
    csvLine = csvLine + "\"" + line_col[0] + "\","
    csvLine = csvLine + "\"" + line_col[1] + "\","

    #Add all INFO data to csvLine
    for i in range(3,7):
        csvLine = csvLine + "\"" + line_col[i] + "\"," 

    for item in infoData:
        csvLine = csvLine + item + ","
    #remove last ","
    csvLine = csvLine + getSampleString(line_col[9:23])
    try:
        ancestor = line_col[23]
    except:
        ancestor = "."        
    csvLine = csvLine + getAncestorInfo(ancestor)
    outFile.write(csvLine + "\n")


if __name__ == "__main__":
    file_name = sys.argv[1]
    outFile = open(file_name[0:-4] + ".csv",'w')
    writeColumns(outFile)
    with open(file_name) as f:
        for line in f:
            if isDataLine(line):
                    writeInfo(line,outFile)
    f.close()
    outFile.close()     

