import sys
ALT,QUAL,FILTER,INFO = 4,5,6,7
MIN_MAP_QUALITY = 0
CC3_3Midx = 11
REMOVE_CC3_3M = True

def isDataLine(line):
    """
    Determines in line contains site data
    """
    if len(line) > 1:
        return line[0] != "#"
    return False

def siteFiltering(line_col):
    """
    Filters the site for:
        - presence of ALT base
        - no LowQual flag
    """
    if line_col[ALT] != ".":
        return float(line_col[QUAL] >= MIN_MAP_QUALITY) and \
            line_col[FILTER] != "LowQual"
    return False

def sampleFiltering(samples):
    """
    For the site to pass samples must:
        - no missing samples
        - One Sample GT must be different than others
    """
    gt_counts={}
    for i in range(0,len(samples)):
        if "./." not in samples[i]:
            s_col = samples[i].split(":")
            gt_counts[s_col[0]] = gt_counts.get(s_col[0],0) + 1

    if (1 in gt_counts.values() and 13 in gt_counts.values()):
        return True

    return filterMutant(gt_counts,samples)

def filterMutant(gt_counts,samples):
    """
    Filters on the odd GT individual
    """
    for key in gt_counts.keys():
        if gt_counts.get(key) == 1:
            break

    for i in range(0,len(samples)):
        if key in samples[i]:
            break

    if REMOVE_CC3_3M:
        if i == CC3_3Midx:
            return False

    return True


if __name__ == "__main__":
    file_loc,out_name = sys.argv[1],sys.argv[2]
    outFile = open(out_name,'w')

    with open(file_loc) as f:
        for line in f:
            if isDataLine(line):
                line_col = str.split(line)
                if siteFiltering(line_col):
                    if sampleFiltering(line_col[9:23]):
                        #Site passed filters
                        outFile.write(line)

            #Write header info        
            else:
                outFile.write(line)

    outFile.close()
    f.close()

