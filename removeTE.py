import spirodelaFiltering
import sys
#
#TE = {Pseudo0:[(x,y),(z,l)...],Pseudo1:[(m,x)...]...}
TE_ranges = {}
CHROM,START,STOP = 0,1,2

def loadTEranges(TE_file_loc):
    with open(TE_file_loc) as TE_file:
        for line in TE_file:
            line_col = str.split(line)
            #Identify chromosome
            TE_ranges.setdefault(line_col[CHROM],[]).append((line_col[START],line_col[STOP]))
    TE_file.close()
    return

def validRange(line):
    return True



if __name__ == "__main__":
    TE_file_loc,vcf_file_loc = sys.argv[1],sys.argv[2]
    loadTEranges(TE_file_loc)

    trimmed_vcf = open(vcf_file_loc[:-4] + "_TEremoved.vcf", "w")
    removed_sites = open(vcf_file_loc[:-4] + "_TE_Sites.vcf","w")

    with open(vcf_file_loc) as vcf_file:
        for line in vcf_file:
            if spirodelaFiltering.isDataLine(line):
                if validRange(line):
                    trimmed_vcf.write(line)
                else:
                    removed_sites.write(line)
            else:
                #Write header info 
                trimmed_vcf.write(line)

    removed_sites.close()
    vcf_file.close()
    trimmed_vcf.close()
