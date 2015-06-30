import sys
from vcfDict import vcfDict

def isDataLine(line):
    """
    Determines in line contains site data
    """
    if len(line) > 1:
        return line[0] != "#"
    return False




if __name__ == "__main__":
    """
    """

    known_sites,ccm = sys.argv[1],sys.argv[2]
    sites = vcfDict(known_sites)
    sites.loadDict()
    
    with open(ccm) as ccm_vcf:
        for line in ccm_vcf:
            if isDataLine(line):
                key = str.split(line)[0] + ":"+ str.split(line)[1]
                siteLine = sites.getLine(key)
                if siteLine != "":
                    print siteLine
                else:
                    pass
#                    print key



