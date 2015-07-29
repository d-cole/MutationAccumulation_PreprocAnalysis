import sys
import subprocess
from vcfLine import vcfLine
from vcfSample import vcfSample

SAMPLES_CC = ["B","C","D","E","F","H","I","J","K","L","N","O"]
SAMPLES_GP = ["B","C","D","E","F","G","H","I","J","K","L","M","N","O"] 
SAMPLES = SAMPLES_CC


COLUMNS = ["sample","alt_count","ref_count","other_count"]


if __name__ == "__main__":
    file_in = sys.argv[1]
    file_out_loc = sys.argv[2]

    file_out = open(file_out_loc,"w") 
    file_out.write(",".join(COLUMNS) + "\n")

    with open(file_in) as vcfFile:
        for raw_line  in vcfFile:
            line = vcfLine(raw_line)

            if line.isDataLine:
                for i in range(0,len(line.samples)):
                    if line.samples[i].GT == "0/1":
                        line_out = ""
                        line_out = line_out + SAMPLES[i] + ","
                        line_out = line_out + str(line.samples[i].altReads) + ","
                        line_out = line_out + str(line.samples[i].refReads) + ","
                        line_out = line_out + str(line.samples[i].otherReads)
                        file_out.write(line_out + "\n")

    vcfFile.close()
    file_out.close()



