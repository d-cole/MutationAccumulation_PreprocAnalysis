import sys
"""
Takes a ordered .vcf file, splits it up by chromosome
"""
def isDataLine(line):
    if len(line)>1:
        return line[0] != "#"
    return False


if __name__ == "__main__":
    file_in = sys.argv[1]
    chrom = ""
    chrom_file = None
 
    with open(file_in) as f:
        for line in f:
            if isDataLine(line):
                chrom_line = str.split(line)[0]
                    
                if chrom == "":
                    #First line
                    chrom = chrom_line
                    chrom_file = open(chrom + ".txt","w")

                if chrom != chrom_line:
                    chrom_file.close()
                    chrom = chrom_line
                    chrom_file = open(chrom + ".txt","w") 
                
                if chrom == chrom_line:
                    chrom_file.write(line)

    chrom_file.close()
