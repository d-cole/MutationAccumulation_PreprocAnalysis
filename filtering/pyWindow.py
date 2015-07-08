import sys
from vcfLine import vcfLine

if __name__ == "__main__":
    vcf_loc = sys.argv[1]
    siteCount = 0    
    with open(vcf_loc) as f:
        for raw_line in f:
            line = vcfLine(raw_line) 
            print line.repr()





