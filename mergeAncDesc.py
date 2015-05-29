import sys
import spirodelaFiltering

CC3_3idx = 9
GP2_3idx = 10

def getMergeLine(desc_line,ancFile):
    desc_line_col = desc_line.split()
    var_loc = desc_line_col[0] + "\t" + desc_line_col[1]
    merged_line = ""

    for anc_line in ancFile:
        if var_loc == anc_line[0:len(var_loc)]:
            anc_col = anc_line.split()
            merged_line = desc_line.strip("\n") + " " + anc_col[CC3_3idx] + " " + anc_col[GP2_3idx]
            break
    
    return merged_line


if __name__ == "__main__":
    anc_loc,desc_loc,merge_name = sys.argv[1],sys.argv[2],sys.argv[3]
    ancFile = open(anc_loc,'r')
    mergeFile = open(merge_name,'w')

    with open(desc_loc) as desc_f:
        for desc_line in desc_f:
            if spirodelaFiltering.isDataLine(desc_line):
                mergeLine = getMergeLine(desc_line,ancFile)
                print("merged line",mergeLine)
                if mergeLine != "":
                    print(mergeLine)
                    mergeFile.write(mergeLine + "\n")
            else:
                mergeFile.write(desc_line + "\n")

    ancFile.close()
    mergeFile.close()
    desc_f.close()

