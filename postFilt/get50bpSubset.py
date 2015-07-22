import sys
from vcfDict import vcfDict


if __name__ == "__main__":
    vcfLoc,bpFile,bpOut = sys.argv[1],sys.argv[2],sys.argv[3]
    outFile = open(bpOut,"w")
    vcf = vcfDict(vcfLoc)
    vcf.loadDict()

    with open(bpFile) as f:
        for line in f:
            if line[0] == "p":
                sline = line.split(",")
                windowID = sline[0]
                if vcf.getLine(windowID) != "":
                    #Site is present 
                    outFile.write(line)

            else:
                outFile.write(line)    


    outFile.close()


