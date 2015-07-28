import sys
import subprocess
from vcfLine import vcfLine
from vcfSample import vcfSample

SAMPLES_CC = ["B","C","D","E","F","H","I","J","K","L","N","O"]
SAMPLES_GP = ["B","C","D","E","F","G","H","I","J","K","L","M","N","O"] 
SAMPLES = SAMPLES_CC

def getSamplePval(sample):
    p = subprocess.Popen("../r/calcP.r " + str(sample.altReads) +" " + str(sample.refReads),\
            shell=True,stdout=subprocess.PIPE)
    pVal = (p.communicate()[0].strip("\n"))[4:]
    return pVal

if __name__ == "__main__":
    file_in = sys.argv[1]
    file_out_loc = sys.argv[2]

    file_out = open(file_out_loc,"w") 
    file_out.write(",".join(SAMPLES) + "\n")

    with open(file_in) as vcfFile:
        for raw_line  in vcfFile:
            line = vcfLine(raw_line)

            if line.isDataLine:
                line_out = ""
                for sample in line.samples:
                    line_out = line_out + getSamplePval(sample) + ","
                
                file_out.write(line_out[:-1] + "\n")

    vcfFile.close()
    file_out.close()



