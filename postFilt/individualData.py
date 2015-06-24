import sys

#pseudo0 11187   .       G       A       13607.42        .       AC=27;AF=0.964;AN=28;BaseQRankSum=3.988;DP=440;Dels=0.07;FS=0.000;HaplotypeScore=16.4649;InbreedingCoeff=-0.0224;MLEAC=28;MLEAF=1.00;MQ=91.47;MQ0=11;MQRankSum=8.205;QD=30.93;ReadPosRankSum=1.947;SOR=0.750    GT:AD:DP:GQ:PL  1/1:1,29:30:47:1037,47,0        1/1:3,31:34:66:1076,66,0        1/1:2,28:30:55:1047,55,0        1/1:1,21:22:32:714,32,0 0/1:5,25:30:2:741,0,2   1/1:2,27:29:50:985,50,0 1/1:2,35:37:77:1313,77,0        1/1:3,22:25:35:772,35,0 1/1:1,24:25:69:907,69,0 1/1:1,23:24:35:798,35,0 1/1:1,25:26:69:900,69,0 1/1:2,41:43:97:1545,97,0        1/1:0,22:22:54:738,54,0 1/1:1,29:31:81:1060,81,0

#GT:AD:DP:GQ:PL  1/1:1,29:30:47:1037,47,0
GT,AD,DP,GQ,PL = 0,1,2,3,4
#SAMPLES = ["CC3-3_B","CC3-3_C","CC3-3_D","CC3-3_E","CC3-3_F","CC3-3_G",\
#"CC3-3_H","CC3-3_I","CC3-3_J","CC3-3_K","CC3-3_L","CC3-3_M","CC3-3_N","CC3-3_O"]

SAMPLES = ["GP2-3_B", "GP2-3_C", "GP2-3_D", "GP2-3_E", "GP2-3_F", "GP2-3_G", "GP2-3_H", "GP2-3_I", "GP2-3_J", "GP2-3_K", "GP2-3_L", "GP2-3_M", "GP2-3_N", "GP2-3_O"]
COLUMNS = ["\"GT\"","\"AD_REF\"","\"AD_ALT\"","\"DP\"","\"GQ\"","\"PL\""]
SAMPLE_COUNT = [0]*14
def writeColumns(columns,outFile):
    column_string = ""
    for j in columns:
        column_string = column_string + "\"" + j +"\"" + ","
    outFile.write(column_string[:-1] + "\n")
    return

def countIndividuals(samples):
    """
    If a sample is heterozygous increases its count by 1
    """
    #print(len(samples))
    for i in range(0,len(samples)):
        if "./." not in (samples[i]):
            if samples[i].split(":")[0] == '0/1':
                SAMPLE_COUNT[i] = SAMPLE_COUNT[i] + 1
    return

def parseIndividual(sample):
    s_col = sample.split(":")
    s_csv_row = ""
    for i in range(0,len(s_col)):
        if i == 1:
            split_AD = s_col[i].split(",")
            s_csv_row = s_csv_row + "\"" + split_AD[0] + "\"" +",\"" + split_AD[1] +"\"," 
        else:
            s_csv_row = s_csv_row + "\"" + s_col[i] +"\"" + ","
    return s_csv_row[:-1]

def isDataLine(line):
    """
    Determines if the line in the vcf file contains
    data 
    """
    if len(line) > 1:
        return line[0] != "#"
    return False

if __name__ == "__main__":
    file_name = sys.argv[1]
    with open(file_name) as f:
        for line in f:
            if isDataLine(line):
                sline = str.split(line)
                countIndividuals(sline[9:])
    f.close()
    print(SAMPLE_COUNT)
#    for i in range(0,len(SAMPLES)):
#        outFile = open(SAMPLES[i] + ".csv",'w')
#        with open(file_name) as f:
#            writeColumns(COLUMNS,outFile)
#            for line in f:
#                if isDataLine(line):
#                    line_col = str.split(line)
#                    outFile.write(parseIndividual(line_col[9+i]) + "\n")
#                    
#        f.close()
#        outFile.close()
#
