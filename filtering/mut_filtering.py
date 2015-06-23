import sys
from filterMethods import filterMethods

CC3_3Midx = 11
REMOVE_CC3_3M = True

if __name__ == "__main__":
    file_loc,out_name = sys.argv[1],sys.argv[2]
    outFile = open(out_name,'w')
    sampleMediansLoc = "/data/daniel.cole/spirodela/data/CC3-3/individualData/ind_DP_med_v2_f0.csv"
    filterManager = filterMethods(sampleMediansLoc,1)

    with open(file_loc) as f:
        for line in f:
            if filterManager.isDataLine(line):
                line_col = str.split(line)
                if filterManager.siteFiltering(line_col):
                    #Site passed filters
                    #Only filter for sites with an alternate base and not LowQual
                    outFile.write(line)

            #Write header info        
            else:
                outFile.write(line)

    outFile.close()
    f.close()

