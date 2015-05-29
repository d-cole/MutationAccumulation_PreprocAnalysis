import spirodelaFiltering
import sys
"""
Extracts CC3-3 and GP2-3 samples from vcf file
"""
CC3_3_idx = 11
GP2_3_idx = 16



def parseAnc(line):
    """
    Constructs new line with only samples CC3-3 and GP2-3
    """
    line_col = str.split(line)
    new_line = ""
    for i in range(0,9):
        new_line = new_line + line_col[i] + " "
    return new_line + " " + line_col[11] + " " + line_col[16]

if __name__ == "__main__":
    anc_file,out_name = sys.argv[1],sys.argv[2]
    outFile = open(out_name,'w')
    with open(anc_file) as f:
        for line in f:
            if spirodelaFiltering.isDataLine(line):
                outFile.write(parseAnc(line))
            else:
                outFile.write(line)

    f.close()
    outFile.close()
