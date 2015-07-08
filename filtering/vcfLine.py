from vcfSample import vcfSample
import sys
ALT_IDX = 4
INFO_IDX = 7
class vcfLine:
    """
    Represents a vcf line

    Fails for sites where there is more than one alt base
    Currently only works where possiblt genotypes are  0/0 and 0/1
    """

    def __init__(self,raw_line):
        self.infoValues = {"AC":None,"AF":None,"BaseQRankSum":None,"DP":None,"Dels":None,"FS":None,\
            "HaplotypeScore":None,"InbreedingCoeff":None,"MLEAC":None,"MLEAF":None,"MQ":None,\
            "MQ0":None,"MQRankSum":None,"QD":None,"ReadPosRankSum":None,"SOR":None}        
        self.chrom,self.pos,self.ref,self.alt,self.qual,self.filt = None,None,None,None,None,None
        self.isDataLine = True
        self.isAltSite = False
        self.samples = []
        self.raw_line  = raw_line
        self.multiHap = False
     
        if len(self.raw_line) > 1:
            if self.raw_line[0] == "#":
                self.isDataLine = False     
        
        if self.isDataLine:
            sline = str.split(self.raw_line)        

            if sline[ALT_IDX] != ".":
                #variant site
                self.isAltSite = True
                if "," in sline[ALT_IDX]:
                    self.multiHap = True

            self.__loadSamples(sline) 
            self.__loadInfoVals()

            self.chrom = sline[0]
            self.pos = sline[1]
            self.ref = sline[3]
            self.alt = sline[4]

            self.qual = sline[5]
            if str.isdigit(self.qual):
                self.qual = float(self.qual)

            self.filt = sline[6]
            
                

    def __loadSamples(self,sline):
        sampleStrings = sline[9:]        
        for s in sampleStrings:
            self.samples.append(vcfSample(s,self.isAltSite))
        
    def __loadInfoVals(self):
        #AC=1;AF=0.042;AN=24;BaseQRankSum=-0.093;DP=349;Dels=0.00;FS=0.000;HaplotypeScore=0.5762;InbreedingCoeff=-0.0435;MLEAC=1;MLEAF=0.042;MQ=98.43;MQ0=0;MQRankSum=-0.829;QD=2.06;ReadPosRankSum=0.267;SOR=0.846
        splitInfo = (str.split(self.raw_line)[INFO_IDX]).split(";")
        for readInfo in splitInfo:
            #populates self.infoValues for every value present
            eqIdx = readInfo.find("=")
            tag = readInfo[0:eqIdx] 
            value = (readInfo[eqIdx + 1:])
            if str.isdigit(value):
                value = float(value)
            self.infoValues[tag] = value 
        
    
    def isAltSite(self):
        return self.isAltSite 

    def repr(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s" \
            %(str(self.infoValues),str(self.chrom),str(self.pos),\
            str(self.ref),str(self.alt),str(self.qual),\
            str(self.filt),str(self.isDataLine),str(self.raw_line))

    def printLine(self):
        print self.raw_line


    def getAltTotal(self):
        altTotal = 0
        for s in self.samples:
            if isinstance(s.altReads,float):
                altTotal += s.altReads
            else:
                pass
                #print s.toString()

        return altTotal


    def getRefTotal(self):
        refTotal = 0
        for s in self.samples:
            if isinstance(s.refReads,float):
                refTotal += s.refReads
            else:
                pass
                #print s.toString()
        print refTotal
        print self.raw_line
        sys.exit()
        return refTotal






