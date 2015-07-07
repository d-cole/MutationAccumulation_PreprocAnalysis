import sys
from vcftoCSV_siteData import * 
from vcfDict import vcfDict
import os


def isDataLine(line):
    """
    Determines in line contains site data
    """
    if len(line) > 1:
        return line[0] != "#"
    return False

def getExclInt(samples,bSetIdx,targetDict):
    """
    Returns the set of sites that A shares with B and only B
    """
    bSet = set(samples[bSetIdx].getKeys())
    aSet = set(targetDict.getKeys())
    intAB = set.intersection(aSet,bSet)

    #Removes sites from intAB present in other samples except for sample B and sample A
    for i in range(0,len(samples)):
        if i != bSetIdx and (samples[i].getFileName() != targetDict.getFileName()):
            for ele in samples[i].getKeys():
                try:
                    intAB.remove(ele)
                except:
                    pass 
    return intAB


if __name__ == "__main__":
    """
    """
    GPB = vcfDict("../data/compareSNPs/tmp/GP2-3_B_m0.vcf")
    GPC = vcfDict("../data/compareSNPs/tmp/GP2-3_C_m0.vcf")
    GPD = vcfDict("../data/compareSNPs/tmp/GP2-3_D_m0.vcf")
    GPE = vcfDict("../data/compareSNPs/tmp/GP2-3_E_m0.vcf")
    GPF = vcfDict("../data/compareSNPs/tmp/GP2-3_F_m0.vcf")
    GPG = vcfDict("../data/compareSNPs/tmp/GP2-3_G_m0.vcf")
    GPH = vcfDict("../data/compareSNPs/tmp/GP2-3_H_m0.vcf")
    GPI = vcfDict("../data/compareSNPs/tmp/GP2-3_I_m0.vcf")
    GPJ = vcfDict("../data/compareSNPs/tmp/GP2-3_J_m0.vcf")
    GPK = vcfDict("../data/compareSNPs/tmp/GP2-3_K_m0.vcf")
    GPL = vcfDict("../data/compareSNPs/tmp/GP2-3_L_m0.vcf")
    GPM = vcfDict("../data/compareSNPs/tmp/GP2-3_M_m0.vcf")
    GPN = vcfDict("../data/compareSNPs/tmp/GP2-3_N_m0.vcf")
    GPO = vcfDict("../data/compareSNPs/tmp/GP2-3_O_m0.vcf")

    CCB = vcfDict("../data/compareSNPs/tmp/CC_B_m0.vcf")
    CCC = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
    CCD = vcfDict("../data/compareSNPs/tmp/CC_D_m0.vcf")
    CCE = vcfDict("../data/compareSNPs/tmp/CC_E_m0.vcf")
    CCF = vcfDict("../data/compareSNPs/tmp/CC_F_m0.vcf")
    CCG = vcfDict("../data/compareSNPs/tmp/CC_G_m0.vcf")
    CCH = vcfDict("../data/compareSNPs/tmp/CC_H_m0.vcf")
    CCI = vcfDict("../data/compareSNPs/tmp/CC_I_m0.vcf")
    CCJ = vcfDict("../data/compareSNPs/tmp/CC_J_m0.vcf")
    CCK = vcfDict("../data/compareSNPs/tmp/CC_K_m0.vcf")
    CCL = vcfDict("../data/compareSNPs/tmp/CC_L_m0.vcf")
    CCM = vcfDict("../data/compareSNPs/tmp/CC_M_m0.vcf")
    CCN = vcfDict("../data/compareSNPs/tmp/CC_N_m0.vcf")
    CCO = vcfDict("../data/compareSNPs/tmp/CC_O_m0.vcf")

    samples_CC = [CCB,CCC,CCD,CCE,CCF,CCG,CCH,CCI,CCJ,CCK,CCL,CCM,CCN,CCO]
    samples_GP = [GPB,GPC,GPD,GPE,GPF,GPG,GPH,GPI,GPJ,GPK,GPL,GPM,GPN,GPO]
    for x in samples_CC:
        x.loadDict() 
 
    sample = sys.argv[1]
    sDict = vcfDict(sample)
    sDict.loadDict()
    sampleName = sDict.getFileName()

    for i in range(0,len(samples_CC)):
        outFile = open(os.path.basename(sample) + ":" + samples_CC[i].getFileName() + ".csv","w")
        iSet = getExclInt(samples_CC,i,sDict)
        print "Sites %s excl shares with %s: %i" %(sampleName,samples_CC[i].getFileName(),len(iSet))
        writeColumns(outFile)
        for key in iSet:
            writeInfo(sDict.getLine(key),outFile)
        outFile.close()

    for x in samples_GP:
        x.loadDict()


    for i in range(0,len(samples_GP)):
        outFile = open(os.path.basename(sample) + ":" + samples_GP[i].getFileName() + ".csv","w")
        iSet = getExclInt(samples_GP,i,sDict)
        print "Sites %s excl shares with %s: %i" %(sampleName,samples_GP[i].getFileName(),len(iSet))
        writeColumns(outFile)
        for key in iSet:
            writeInfo(sDict.getLine(key),outFile)
        outFile.close()

       






    sys.exit()
