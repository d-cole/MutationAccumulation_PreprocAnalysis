from vcfDict import vcfDict
import sys

CC3_3idx = 9
GP2_3idx = 10

def getMergeLine(desc_line,CC3_sample,GP2_sample):
    """
    Returns the desc_line with the given sample information appended
    """
    return desc_line.strip("\n") + " " + CC3_sample + " " + GP2_sample + "\n"


if __name__ == "__main__":
    """

    """
    anc_loc,desc_loc,merge_loc = sys.argv[1],sys.argv[2],sys.argv[3]
    desc = vcfDict(desc_loc)
    desc.loadDict()
    merge_file = open(merge_loc,"w")

    with open(anc_loc) as anc_file:
        for anc_line in anc_file:
            if spirodela_filtering.isDataLine(anc_line):

                anc_line_col = str.split(anc_line)
                anc_line_key = anc_line_col[0] + ":" + anc_line_col[1]
                desc_line = desc.getLine(line_key)

                if desc_line != "":
                    merge_file.write(getMergeLine(desc_line,anc_line_col[CC3_3idx],anc_line_col[GP2_3idx]))
                    print anc_line
                    print anc_line_key
                    print desc_line
                    break

    anc_file.close()
    merge_file.close()


