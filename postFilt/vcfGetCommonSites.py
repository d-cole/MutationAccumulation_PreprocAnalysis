from vcfDict import vcfDict
import sys
REF,ALT = 3,4
"""
Prints out sites that two .vcf files share
"""

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
    CC3_loc,GP2_loc,common_sites_loc = sys.argv[1],sys.argv[2],sys.argv[3]
    desc = vcfDict(GP2_loc)
    desc.loadDict()

    merge_file = open(common_sites_loc,"w")
   
    with open(CC3_loc) as anc_file:
        for anc_line in anc_file:
            if isDataLine(anc_line):

                anc_line_col = str.split(anc_line)
                anc_line_key = anc_line_col[0] + ":" + anc_line_col[1]
                desc_line = desc.getLine(anc_line_key)

                if desc_line != "":
                    merge_file.write(desc_line)
                    pass
                else:
                    pass

    anc_file.close()
    merge_file.close()

