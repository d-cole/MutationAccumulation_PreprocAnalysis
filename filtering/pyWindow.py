import sys
from vcfLine import vcfLine
import traceback
"""
pyWindow.py

Analyzes vcf files from sites in a variable sized window
"""
WINDOW_SIZE = 50

def processWindow(inWindow,outFile):
    """
    Given a list of the 50 sites in the window returns ...

    Percent of sites with depth below x?
    Average depth at sites?
    Percentage of alt/ref sites?
    Number of alt/ref reads across all samples
    Sites with buildign up depth --  rainbow areas??
    """

    DPtotal = 0 
    alt_reads = 0
    ref_reads = 0 
    alt_sites = 0    

    for site in inWindow:
        if isinstance(site.infoValues["DP"],float):
            DPtotal = DPtotal + site.infoValues["DP"]

        if site.isAltSite:
            alt_sites += 1
 
    if True:
        csvOutLine = ""
        csvOutLine  = csvOutLine + inWindow[0].chrom +":"+ inWindow[0].pos + ","
        csvOutLine = csvOutLine + inWindow[49].chrom +":" + inWindow[49].pos +","
        csvOutLine = csvOutLine + str(alt_sites) +","
        csvOutLine = csvOutLine + str(50 - alt_sites) + ","
        csvOutLine = csvOutLine + str(DPtotal/50.0) + "\n"
        outFile.write(csvOutLine)


if __name__ == "__main__":
    vcf_loc = sys.argv[1]
    inWindow = []
    outFile = open("CC_windowOut.csv","w")    
    
# CSV output file format 
# start,        stop,       #Alt sites,      #Ref sites,     Average depth
# pseudo0:1000, pseudo0:1050, 5,                45,             197
#
    outFile.write("start,stop,altCount,refCount,avgDepth" + "\n")
    
    with open(vcf_loc) as f:
        for raw_line in f:
            if len(inWindow) == WINDOW_SIZE:
                #Analyze site
                processWindow(inWindow,outFile)
                inWindow = []
            

            line = vcfLine(raw_line)
            if line.isDataLine:
                #Only add dataLines to the window
                inWindow.append(line) 
                    

    outFile.close()



