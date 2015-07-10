import sys
from vcfLine import vcfLine
import traceback
"""
pyWindow.py

Analyzes vcf files from sites in a variable sized window
"""
WINDOW_SIZE = 50

def processWindow(inWindow):
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

 
    if float(DPtotal/50.0) < 200.00 or alt_sites > 5:
       print "Alt site: " + str(alt_sites)
       print "ref_sites: " + str(50 - alt_sites)

       print inWindow[0].chrom + inWindow[0].pos +":" + inWindow[49].chrom +\
            inWindow[49].pos
       print str(DPtotal/50.0) 
       print ""
       
    #print "% alt sites: " + str(alt_sites/50.0)
    #print "Average depth in window: " + str(DPtotal/50.0)
    #print "Ref reads #: " + str(site.getRefTotal())
    #print "Alt reads #: " +  str(site.getAltTotal())
    #


if __name__ == "__main__":
    vcf_loc = sys.argv[1]
    inWindow = []

    with open(vcf_loc) as f:
        for raw_line in f:
            if len(inWindow) == WINDOW_SIZE:
                #Analyze site
                processWindow(inWindow)
#                print raw_line
#                sys.exit()
                #Output results
                inWindow = []

            line = vcfLine(raw_line)
    #        try:
    #            line = vcfLine(raw_line) 
    #        except:
    #            e = sys.exc_info()[0]
    #            print e
    #            print traceback.format_exc()
    #            print raw_line + "\n"
    #
            if line.isDataLine:
                #Only add dataLines to the window
                inWindow.append(line) 
                    








