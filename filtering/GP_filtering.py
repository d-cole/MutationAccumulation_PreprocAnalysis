import sys
from filterMethods import filterMethods
REMOVE_CC3_3M = False

if __name__ == "__main__":
    file_loc,out_name = sys.argv[1],sys.argv[2]
    outFile = open(out_name,'w')
    sampleMediansLoc = "/data/daniel.cole/spirodela/data/GP2-3/individualData/ind_DP_med_f0.csv"
    filterManager = filterMethods(sampleMediansLoc,14)

    with open(file_loc) as f:
        for line in f:
            if filterManager.isDataLine(line):
                line_col = str.split(line)
                if filterManager.siteFiltering(line_col):
                    if filterManager.sampleFiltering(line_col[9:23], REMOVE_CC3_3M, 0):
                        #Site passed filters
                        outFile.write(line)

            #Write header info        
            else:
                outFile.write(line)

    outFile.close()
    f.close()

