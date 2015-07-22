import sys
from vcfLine import vcfLine
from vcfSample import vcfSample

HET = "0/1"

def allHet(samples):
    """
    Determines if the list of samples is all HET samples
    """
    for sample in samples:
       if sample.GT != HET:
            return False
    return True



if __name__ == "__main__":
    vcf_in,vcf_out = sys.argv[1],sys.argv[2]

    outFile = open(vcf_out,"w")
    with open(vcf_in) as file:
        for line in file:
            vLine = vcfLine(line)
            if vLine.isDataLine:
                if allHet(vLine.samples):
                    outFile.write(line)
    outFile.close()






