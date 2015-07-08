

class vcfSample:
    """
    Represents a sample from a vcf file
    If the sample is at an alt site only GT and DP info is present
    If the sample is missing missingInfo = True and no other info is loaded
    """

    def __init__(self,i_sampleString,i_atAltSite):
        self.atAltSite = i_atAltSite
        self.sampleString = i_sampleString

        self.missingInfo = False 
        self.GT = None
        self.altReads = None
        self.refReads = None
        self.GQ = None
        self.PL = None
        self.DP = None
        
        self.__parseVals() #Parse string representation of sample
                
    def __parseVals(self):
        if "./." in self.sampleString:
            self.missingInfo = True
            return

        splitSample = self.sampleString.split(":")
        if self.atAltSite:
            #At alt sites
            self.GT = splitSample[0] 
            self.altReads = splitSample[1].split(",")[1]
            self.refReads = splitSample[1].split(",")[0]
            self.DP = float(splitSample[2])
            self.GQ = float(splitSample[3])
            self.PL = splitSample[4]
   
        else:
            #At ref site
            self.GT = splitSample[0]
            self.DP = float(splitSample[1])

    def toString(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s" \
            %(str(self.sampleString) + "\n",\
            self.GT,\
            str(self.altReads),\
            str(self.refReads),\
            str(self.GQ),\
            self.PL,\
            str(self.DP),\
            str(self.missingInfo),\
            str(self.atAltSite))
   
