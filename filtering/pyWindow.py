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

    refReadTotal = 0
    altReadTotal = 0
    otherReadTotal = 0


    for site in inWindow:
        if isinstance(site.infoValues["DP"],float):
            DPtotal = DPtotal + site.infoValues["DP"]

        if site.isAltSite:
            alt_sites += 1
        
        refReadTotal += site.getRefTotal()     
        altReadTotal += site.getAltTotal()
        otherReadTotal += site.getOtherTotal()
            
 
    if True:
        csvOutLine = ""
        csvOutLine  = csvOutLine + inWindow[0].chrom +","+ inWindow[0].pos + ","
        csvOutLine = csvOutLine + inWindow[-1].chrom +"," + inWindow[-1].pos +","
        csvOutLine = csvOutLine + str(alt_sites) +","
        csvOutLine = csvOutLine + str(len(inWindow) - alt_sites) + ","
        csvOutLine = csvOutLine + str(DPtotal/len(inWindow)) + ","
        csvOutLine = csvOutLine + "," + str(refReadTotal) + "," +  str(altReadTotal) + "," +  str(otherReadTotal) +  "\n"
        outFile.write(csvOutLine)


if __name__ == "__main__":
    vcf_loc,out_loc = sys.argv[1], sys.argv[2]
    inWindow = []
    outFile = open(out_loc,"w")    
    
# CSV output file format 
# start,        stop,       #Alt sites,      #Ref sites,     Average depth, Alt Reads (sum from all samples), ref reads (sum from all samples), 
# pseudo0:1000, pseudo0:1050, 5,                45,             197
#
    outFile.write("start_chrom,start_pos,stop_chrom,stop_pos,altSiteCount,refSiteCount,avgDepth,altReadTotal,refReadTotal,otherReadTotal" + "\n")
    
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
        #process last incomplete block
        processWindow(inWindow,outFile)   

    outFile.close()



