import sys
from filterMethods import filterMethods


if __name__ == "__main__":
    vcf_in_loc,vcf_out_loc = sys.argv[1],sys.argv[2]
    vcf_out = open(vcf_out_loc,"w")
    filterManager = filterMethods("/data/daniel.cole/spirodela/data/CC3-3/individualData/ind_DP_med_v2_f0.csv") 
    with open(vcf_in_loc) as vcf_file:
        for line in vcf_file:
            if filterManager.isDataLine(line):
                line_col = str.split(line)
                if filterManager.callSiteFiltering(line_col):
                    if filterManager.callSampleFilterin(line_col[9:]):
                        vcf_out.write(line)
            else:
                #Write header information
                vcf_out.write(line)

    vcf_file.close()
    vcf_out.close()


    
