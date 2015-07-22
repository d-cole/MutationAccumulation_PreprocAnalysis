import sys
sys.path.append('../postFilt/')
from vcfLine import vcfLine
from vcfDict import vcfDict

WINDOW_SIZE = 50

"""
get50bpSites.py

Given a vcf file of filtered variants grabs 50bp windows around these sites from unfiltered base calls
"""
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
    
    targetSite = inWindow[WINDOW_SIZE/2]
    siteID = targetSite.chrom + ":" + targetSite.pos
 
    if True:
        wlen = float(len(inWindow))
        csvOutLine = ""
        csvOutLine = csvOutLine + siteID + ","
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


def checkSite(lineVcf,targetSitesDict):
    """
    Return whether the given site is one of the target sites
    """
    lineID = lineVcf.chrom + ":" + lineVcf.pos    
    return targetSitesDict.getLine(lineID) != ""


if __name__ == "__main__":
    vcf_unfilt,vcf_targetSites,out_loc = sys.argv[1], sys.argv[2], sys.argv[3]

    outFile = open(out_loc,"w")    
    outFile.write("siteID,start_chrom,start_pos,stop_chrom,stop_pos,altSiteCount,refSiteCount,avgDepth,avgRefReads,avgAltReads,avgOtherReads" + "\n")

    targetSitesDict = vcfDict(vcf_targetSites)
    targetSitesDict.loadDict()

    window = []    

    with open(vcf_unfilt) as unfilt:
        for line in unfilt:
            lineVcf = vcfLine(line)

            if lineVcf.isDataLine:#Add data lines from unfiltered file to window
                window.append(lineVcf)
                
                if len(window) == WINDOW_SIZE + 1:#Remove oldest site seen keep size == WINDOW_SIZE
                    window.pop(0) 

                     
                    #Check if the site in the middle of the window is a target site
                    if checkSite(window[WINDOW_SIZE/2],targetSitesDict):
                        processWindow(window,outFile)
    
    outFile.close()
    unfilt.close()


