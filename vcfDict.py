import spirodelaFiltering
import sys

class vcfDict:
    """
    Represents a hastable for vcf files
    """
    file_loc = ""
    vcfFile = None
    vcf_dict = {}

    def __init__(self,file_loc):
        self.file_loc = file_loc

    def loadDict(self):
        """
        Loads dictionary of sites into dictionary.
        Uses 'CHROM:POS' as key
        """
        with open(self.file_loc) as f:
            for line in f:
                if spirodelaFiltering.isDataLine(line):
                    line_col = str.split(line)
                    line_key = line_col[0] + ":"+line_col[1]
                    self.vcf_dict[line_key] = self.vcf_dict.get(line_key,line)
            f.close()

    def getLine(self,key):
        """
        Returns the line correspinding to the given key,
        returns "" if line not present.
        """
        line = self.vcf_dict.get(key,"")
        self.vcf_dict.pop(key,None)
        return line

    def printDict(self):
        """
        
        """
        print(self.vcf_dict)

    def writeDict(outFile):
        for key in self.vcf_dict.keys():
            outFile.write(self.vcf_dict[key])
        return

