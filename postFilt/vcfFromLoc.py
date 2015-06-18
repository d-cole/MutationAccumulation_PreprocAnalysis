from vcfDict import vcfDict
import sys
CC3_3idx = 9
GP2_3idx = 10
REF,ALT = 3,4

def getMergeLine(desc_line,CC3_sample,GP2_sample):
    """
    Returns the desc_line with the given sample information appended
    """
    return desc_line.strip("\n") + "" + CC3_sample + "" + GP2_sample + "\n"

def isDataLine(line):
    """
    Determines in line contains site data
    """
    if len(line) > 1:
        return line[0] != "#"
    return False


if __name__ == "__main__":
    """
    Given a .txt file of locations("CHROM:POS") and a vcf file, 
     creates a new vcf file of sites that match the given locations.
    """
    locations_dir,vcf_dir,out_loc = sys.argv[1],sys.argv[2],sys.argv[3]
    vcf_dict = vcfDict(vcf_dir)
    vcf_dict.loadDict()
    out_file = open(out_loc,"w")
   
    #Write header information to merge file 
    with open(vcf_dir) as vcf_file:
        for vcf_line in vcf_file:
            if not isDataLine(vcf_line):
                out_file.write(vcf_line)
            else:
                #data lines start
                break


    with open (locations_dir) as loc_file:
        for loc in loc_file:
            loc = loc.replace(" ","")
            loc = loc.strip("\n")
            print "'" + loc + "'"
            vcf_line = vcf_dict.getLine(loc)
            if vcf_line != "":
                out_file.write(vcf_line)
            else:
                #out_file.write(getMergeLine(desc_line,"    .",""))
                #out_file.write(loc.strip("\n") + "    .\n")
                pass

    loc_file.close()
    out_file.close()

