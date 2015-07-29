import sys
import subprocess
from vcfLine import vcfLine
from vcfSample import vcfSample


def getPval(alt,ref):
    p = subprocess.Popen("../r/calcP.r " + str(alt) +" " + str(ref),\
            shell=True,stdout=subprocess.PIPE)
    pVal = (p.communicate()[0].strip("\n"))[4:]
    return pVal

if __name__ == "__main__":
    file_in = sys.argv[1]
    file_out_loc = sys.argv[2]

    file_out = open(file_out_loc,"w") 

    with open(file_in) as csvFile:
        for raw_line in csvFile:
            sline = raw_line.split(",")      
            sample = sline[25][1:-1]
            alt_read = sline[27][1:-1]
            ref_read = sline[28][1:-1]

            if sample == "odd_sample":
                pVal = "pVal"
            else:
                pVal = getPval(alt_read,ref_read)
            
            file_out.write(sample + "," + pVal + "\n")

    csvFile.close()
    file_out.close()



