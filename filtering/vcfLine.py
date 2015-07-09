from vcfSample import vcfSample
import sys

#Constants for indexes of ALT base and Info strings in the line
ALT_IDX = 4
INFO_IDX = 7


class vcfLine:
    """
    Represents a vcf line

    Alt reads/ref reads not calculated correctly for sites with more than two haplotypes
    """

    def __init__(self,raw_line):# -> None
        """
        Instantiate the vcfLine object with associated information
        """
        self.infoValues = {"AC":None,"AF":None,"BaseQRankSum":None,"DP":None,\
            "Dels":None,"FS":None,"HaplotypeScore":None,"InbreedingCoeff":None,\
            "MLEAC":None,"MLEAF":None,"MQ":None,"MQ0":None,"MQRankSum":None,\
            "QD":None,"ReadPosRankSum":None,"SOR":None}        

        self.chrom,self.pos,self.ref,self.alt,self.qual,self.filt = None,None,\
            None,None,None,None

        self.isDataLine = True
        self.isAltSite = False
        self.samples = []
        self.raw_line  = raw_line
        self.multiHap = False

        #Determines if the line is represents a site     
        if len(self.raw_line) > 1:
            if self.raw_line[0] == "#":
                self.isDataLine = False     
       
        #For lines at sites process site info
        if self.isDataLine:
            sline = str.split(self.raw_line)        
            
            #Alt sites have a different format for samples, determine if the
            #   site has been called as heterozygous
            if sline[ALT_IDX] != ".":
                #variant site
                self.isAltSite = True
                
                #Sites with more than one alternate allele have a different
                #   format for samples
                if "," in sline[ALT_IDX]:
                    self.multiHap = True

            #Loads the vcfSample objects for each sample info at this site
            self.__loadSamples(sline) 
            
            #Load all info data about this site
            self.__loadInfoVals()

            #Load other data not contained in the INFO annotation
            self.chrom = sline[0]
            self.filt = sline[6]
            self.pos = sline[1]
            self.ref = sline[3]
            self.alt = sline[4]
            self.qual = sline[5]
            #If qual data is present cast as a float
            if str.isdigit(self.qual):
                self.qual = float(self.qual)
            
           

    def __loadSamples(self,sline):# -> None
        """
        Instantiates vcfSample objects for each sample at this site.
        Adds all samples to self.Samples list
        """
        #For this vcf format samples are from item 9 -> in the line
        sampleStrings = sline[9:]        
        for s in sampleStrings:
            self.samples.append(vcfSample(s,self.isAltSite))
        
    def __loadInfoVals(self):# -> None
        """
        Pareses the info data from this line storing it in self.infoValues
        """
        splitInfo = (str.split(self.raw_line)[INFO_IDX]).split(";")
        for readInfo in splitInfo:
            #populates self.infoValues for every value present
            eqIdx = readInfo.find("=")
            tag = readInfo[0:eqIdx] 
            value = (readInfo[eqIdx + 1:])
            #Converts numeric info values to float
            if str.isdigit(value):
                value = float(value)
            
            #Add info value to self.infoValues
            self.infoValues[tag] = value 
        
    
    def isAltSite(self):# -> bool
        return self.isAltSite 

    def repr(self):# -> str
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s" \
            %(str(self.infoValues),str(self.chrom),str(self.pos),\
            str(self.ref),str(self.alt),str(self.qual),\
            str(self.filt),str(self.isDataLine),str(self.raw_line))

    def getRawLine(self):# -> str
        """
        Returns the raw vcf line that this vcfLine obj represents. 
        None --> String
        """
        return self.raw_line


    def getAltTotal(self):# -> int
        """
        Calculates and returns the number of alternate 
            reads from all samples at this site.
        None --> int
        """
        altTotal = 0
        for s in self.samples:
            if isinstance(s.altReads,float):
                altTotal += s.altReads
            else:
                pass

        return altTotal


    def getRefTotal(self):# -> int
        """
        Calculates and returns number of reference reads 
            from all samples at the site.
        """
        refTotal = 0
        for s in self.samples:
            if isinstance(s.refReads,float):
                refTotal += s.refReads
            else:
                pass
        return refTotal






