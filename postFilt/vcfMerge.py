from vcfDict import vcfDict
import sys
import spirodelaFiltering
CC3_3idx = 9
GP2_3idx = 10
REF,ALT = 3,4

def getMergeLine(desc_line,CC3_sample,GP2_sample):
    """
    Returns the desc_line with the given sample information appended
    """
    return desc_line.strip("\n") + "" + CC3_sample + "" + GP2_sample + "\n"


if __name__ == "__main__":
    """

    """
    anc_loc,desc_loc,merge_loc = sys.argv[1],sys.argv[2],sys.argv[3]
    desc = vcfDict(desc_loc)
    desc.loadDict()
    merge_file = open(merge_loc,"w")
   
    #Write header information to merge file 
    not_in_anc = open("not_in_anc.vcf","w")
    with open(desc_loc) as desc_file:
        for desc_line in desc_file:
            if not spirodelaFiltering.isDataLine(desc_line):
                merge_file.write(desc_line)
            else:
                #data lines start
                break


    with open(anc_loc) as anc_file:
        for anc_line in anc_file:
            if spirodelaFiltering.isDataLine(anc_line):

                anc_line_col = str.split(anc_line)
                anc_line_key = anc_line_col[0] + ":" + anc_line_col[1]
                desc_line = desc.getLine(anc_line_key)

                if desc_line != "":
                    #merge_file.write(getMergeLine(desc_line, "    " + anc_line_col[CC3_3idx]+ ":"+ anc_line_col[REF] + "/" + anc_line_col[ALT],""))
                    merge_file.write(desc_line)
                else:
                    #merge_file.write(getMergeLine(desc_line,".","."))
                    merge_file.write(anc_line.strip("\n") + "    .\n")
                    pass

    anc_file.close()
    merge_file.close()
    not_in_anc.close()

