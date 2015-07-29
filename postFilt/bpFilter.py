import sys
from vcfDict import vcfDict


if __name__ == "__main__":
    vcfFile,bpFile,outFile_loc = sys.argv[1],sys.argv[2],sys.argv[3]    

    vcfSites = vcfDict(vcfFile)
    vcfSites.loadDict() 
    outFile = open(outFile_loc,"w")

    with open(vcfFile) as vcf_f:
        for line in vcf_f:
            if line[0] == "#":
                outFile.write(line)

    with open(bpFile) as bp:
        for line in bp:
            if line[0] != '""':
                sline = line.split(",") 
                id = sline[1][1:-1]
                
                resp = vcfSites.getLine(id) 
                if resp != "":
                    outFile.write(resp)
                
             
    outFile.close()
    vcf_f.close()
    bp.close()



