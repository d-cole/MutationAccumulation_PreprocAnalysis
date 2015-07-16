
class vcfSample:
    """
    Represents a sample from a vcf file
    If the sample is at an alt site only GT and DP info is present
    If the sample is missing missingInfo = True and no other info is loaded


    UNSURE ABOUT ALT READS AT REF SITES 
    """ 

    def __init__(self,i_sampleString,i_atAltSite):# -> None 
        """ 
        Instantiate a vcfSample object and load appropriate info 
        """ 
        #Sample strings at alt sites have a different format than ref sites
        self.atAltSite = i_atAltSite
        self.sampleString = i_sampleString
        
        #Samples with missing info cannot be parsed
        self.missingInfo = False 
        self.GT = None

        self.altReads = None
        self.refReads = None
        self.otherReads = None

        self.GQ = None
        self.PL = None
        self.DP = None
        
        #Parse string representation of sample
        self.__parseVals() 
                
    def __parseVals(self):# -> None
        """
        Parses the string representation of this sample
        """
        #Do not load info for samples with missing info
        if "./." in self.sampleString:
            self.missingInfo = True
            return
        
        #Split sample string into various info GT, AD, DP ...
        splitSample = self.sampleString.split(":")

        if self.atAltSite:
            #Load sample info from the format GT:AD:DP:GQ:PL
            self.GT = splitSample[0] 

            self.DP = int(splitSample[2])
            self.GQ = float(splitSample[3])
            self.PL = splitSample[4]

            self.altReads = int(splitSample[1].split(",")[1])
            self.refReads = int(splitSample[1].split(",")[0])
            self.otherReads = self.DP - (self.refReads + self.altReads)


   
        else:#At ref site sample format is GT:DP

            self.GT = splitSample[0]
            self.DP = float(splitSample[1])

            #All ref sites seem to have no occurance of alt reads NOT SURE YET
            self.refReads = float(self.DP)
            self.altReads = 0
            self.otherReads = 0

            #Temp checking for other sample formats
            if len(splitSample) != 2:
                pass
                #print splitSample
    
    def getAltReads(self):# -> int
        """
        Returns number of alt reads for this sample
        """
        return self.altReads

    def getRefReads(self):# -> int
        """
        Return ref read counts from this sample
        """
        return self.refReads
    
    def getOtherReads(self):# -> int
        """ 
        Return nonmajor alt read counts from this sample
        """
        return self.otherReads

    def toString(self):# -> str
        """
        Return a string representation of this sample
        """
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s" \
            %(str(self.sampleString),\
            self.GT,\
            str(self.altReads),\
            str(self.refReads),\
            str(self.GQ),\
            self.PL,\
            str(self.DP),\
            str(self.missingInfo),\
            str(self.atAltSite))
   
