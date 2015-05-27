import spirodelaFiltering
import sys
"""
variantInfoCSV.py
Creates a .csv file with the variant information
"""

#SAMPLE INDICES
GT,AD,DP,GQ,PL = 0,1,2,3,4

HETZ = "0/1"
MIN_GQ = 60
INFO = 7
MIN_ALT_READ = 3

#INFO INDICES
AC,AF,AN,BaseQRankSum,DP,Dels,FS,HaplotypeScore, \
InbreedingCoeff,MLEAC,MLEAF,MQ,MQ0,MQRankSum,QD,\
ReadPosRankSum = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15

COLUMNS = "\"varID\",\"CHROM\",\"POS\",\"REF\",\"ALT\",\"QUAL\",\"FILTER\",\
\"AC\",\"AF\",\"AN\",\"BaseQRankSum\",\"DP\",\"Dels\",\"FS\",\
\"HaplotypeScore\",\"InbreedingCoeff\",\"MLEAC\",\"MLEAF\",\"MQ\",\
\"MQ0\",\"MQRankSum\",\"QD\",\"ReadPosRankSum\""

INFO_TAGS = ['AC','AF','AN','BaseQRankSum','DP','Dels','FS','HaplotypeScore','InbreedingCoeff','MLEAC',\
'MLEAF','MQ','MQ0,','MQRankSum','QD','ReadPosRankSum']

def writeColumns(outFile):
    """
    Writes column names to the .csv file
    """
    outFile.write(COLUMNS + "\n")
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
    csvLine = csvLine[:-1]
    outFile.write(csvLine + "\n")


if __name__ == "__main__":
    file_name = sys.argv[1]
    outFile = open(file_name[0:-4] + ".csv",'w')
    writeColumns(outFile)
    with open(file_name) as f:
        for line in f:
            if spirodelaFiltering.isDataLine(line):
                    writeInfo(line,outFile)
    f.close()
    outFile.close()     

