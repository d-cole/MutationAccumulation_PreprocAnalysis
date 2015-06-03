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
    TE_file_loc.close()
    return


if __name__ == "__main__":
    TE_file_loc = sys.argv[1]
    loadTEranges(TE_file_loc)
    print TE_ranges