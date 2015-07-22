import sys
from vcfLine import vcfLine
import traceback
"""
pyWindow.py

Analyzes vcf files from sites in a variable sized window
"""
WINDOW_SIZE = 1

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
        wlen = float(len(inWindow))
        csvOutLine = ""
        #Add site range info
        csvOutLine = csvOutLine + inWindow[0].chrom +","+ inWindow[0].pos + ","
        csvOutLine = csvOutLine + inWindow[-1].chrom +"," + inWindow[-1].pos +","

        #Add number of alt sites in window
        csvOutLine = csvOutLine + str(alt_sites) +","
        #Add number of ref sites in window
        csvOutLine = csvOutLine + str(wlen - alt_sites) + ","
        #Add average site depth
        csvOutLine = csvOutLine + str(DPtotal/wlen) + ","
        #Add average refReadTotal,altReadTotal, and otherReadTotal
        csvOutLine = csvOutLine + str(refReadTotal/wlen) + "," +  str(altReadTotal/wlen) + "," +  str(otherReadTotal/wlen) +  "\n"

        outFile.write(csvOutLine)


if __name__ == "__main__":
    vcf_loc,out_loc = sys.argv[1], sys.argv[2]
    inWindow = []
    outFile = open(out_loc,"w")    
    
# CSV output file format 
# start,        stop,       #Alt sites,      #Ref sites,     Average depth, Alt Reads (sum from all samples), ref reads (sum from all samples), 
# pseudo0:1000, pseudo0:1050, 5,                45,             197
#
    outFile.write("start_chrom,start_pos,stop_chrom,stop_pos,altSiteCount,refSiteCount,avgDepth,avgRefReads,avgAltReads,avgOtherReads" + "\n")
    
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



