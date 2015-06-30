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

def getExclInt(samples,bSetIdx,aSet):
    """
    Returns the set of sites that A shares with B and only B
    """
    bSet = set(samples[bSetIdx].getKeys())
    intAB = set.intersection(aSet,bSet)
    for i in range(0,len(samples)):
        if i != bSetIdx:
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


    CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
    CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
    CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
    CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")
CCC  = vcfDict("../data/compareSNPs/tmp/CC_C_m0.vcf")




    samples = [GPB,GPC,GPD,GPE,GPF,GPG,GPH,GPI,GPJ,GPK,GPL,GPM,GPN,GPO]
    for x in samples:
        x.loadDict() 
    
    sample = sys.argv[1]
    sDict = vcfDict(sample)
    sDict.loadDict()
    

    for i in range(0,len(samples)):
        outFile = open(os.path.basename(sample) + ":" + samples[i].getFileName() + ".csv","w")
        iSet = getExclInt(samples,i,set(sDict.getKeys()))
        print "Sites CCM excl shares with %i: %i" %(i,len(getExclInt(samples,i,set(sDict.getKeys()))))
        writeColumns(outFile)
        for key in iSet:
            writeInfo(sDict.getLine(key),outFile)
        outFile.close()

    sys.exit()
