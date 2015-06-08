from vcfDict import vcfDict
import sys
REF,ALT = 3,4

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
    common_sites_loc,target_file,output_file = sys.argv[1],sys.argv[2],sys.argv[3]
    desc = vcfDict(common_sites_loc)
    desc.loadDict()

    outFile = open(output_file,"w")
   
    with open(target_file) as t_file:
        for t_line in t_file:
            if isDataLine(t_line):

                t_line_col = str.split(t_line)
                t_line_key = t_line_col[0] + ":" + t_line_col[1]
                desc_line = desc.getLine(t_line_key)

                if desc_line != "":
                    #outFile.write(desc_line)
                    #do not write line
                    pass
                else:
                    outFile.write(t_line)
                    pass
            else:
                #Write headers
                outFile.write(t_line)

    t_file.close()
    outFile.close()

