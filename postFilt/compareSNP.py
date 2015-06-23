import sys
import os
from vcfDict import vcfDict

def sameAltBase(line_a,line_b):
    """
    Returns whether the sites have the same alternate base
    """
    altIdx = 4
    sline_a = str.split(line_a)
    sline_b = str.split(line_b)
    return sline_a[altIdx] == sline_b[altIdx]


if __name__ == "__main__":
    #Get location of both .vcf files and load vcfDicts for each
    file_a,file_b = sys.argv[1],sys.argv[2]
    dict_a = vcfDict(file_a)
    dict_b = vcfDict(file_b)
    dict_a.loadDict()
    dict_b.loadDict()

    #size information for each file before processing
    aSize = dict_a.getSize()
    bSize = dict_b.getSize()

    a_keys = dict_a.getKeys()
    bAnda = 0
    same_alt = 0    
    
    #Check every key in dict_a against dict_b 
    #if a site is present .getLine() removes the site after 
    for key in a_keys:
        bLine = ""
        bLine = dict_b.getLine(key)
        if bLine != "":
            bAnda +=1
            aLine = dict_a.getLine(key)
            if sameAltBase(aLine,bLine):
                #Same alternate base in b & a
                same_alt += 1 

    #Sites are removed from dict after .getLine(), remaining size is left over sites
    aNotb = dict_a.getSize()
    bNota = dict_b.getSize() 
    aName = os.path.basename(file_a)
    bName = os.path.basename(file_b)

    print "Size of %s: %i" % (aName,aSize)
    print "Size of %s: %i" % (bName,bSize)
    print "Number of total shared sites: %i (A:%d%%, B:%d%%)" % (bAnda,(float(bAnda)/float(aSize))*100,(float(bAnda)/float(bSize)*100))
   
    #Prevent divide by 0 
    if bAnda == 0:
        bAnda = 1

    print "Number of shared sites with same alt base: %i (%d%% of shared sites)" % (same_alt,(float(same_alt)/float(bAnda))*100)
    print "Number of unmatched sites in %s: %i (%d%%)" % (aName, aNotb,(float(aNotb)/float(aSize)*100))
    print "Number of unmatched sites in %s: %i (%d%%)" % (bName, bNota,(float(bNota)/float(bSize)*100))

