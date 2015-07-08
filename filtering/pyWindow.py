import sys
from vcfLine import vcfLine
import traceback

def processWindow(inWindow):
    """
    Given a list of the 50 sites in the window returns ...
    """

    #Percent of sites with a depth below x?
    #Average depth in sites
    #Percentage of alt reads/ref reads in site
    #Some sites with 0 depth --> building up to acceptable depths??
    DPtotal = 0 
    alt_reads = 0
    ref_reads = 0 
    alt_sites = 0    


    for site in inWindow:
        if isinstance(site.infoValues["DP"],float):
            DPtotal = DPtotal + site.infoValues["DP"]

        if site.isAltSite:
            alt_sites += 1
        
    print "% alt sites: " + str(alt_sites/50.0)
    print "Average depth in window: " + str(DPtotal/50.0)

    print "Alt reads #: " +  str(site.getAltTotal())
    print "Ref reads #: " + str(site.getRefTotal())


if __name__ == "__main__":
    vcf_loc = sys.argv[1]
    inWindow = []

    with open(vcf_loc) as f:
        for raw_line in f:
            if len(inWindow) == 50:
                #Analyze site
                processWindow(inWindow)
                #Output results
                
                inWindow = []
            try:

                line = vcfLine(raw_line) 
            except:
                e = sys.exc_info()[0]
                print e
                print traceback.format_exc()
                print raw_line + "\n"
    
            if line.isDataLine:
                inWindow.append(line) 
                








