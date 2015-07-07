

class vcfLine:
    """
    Represents a vcf line
    """

    def __init__(self,raw_line):
        self.raw_line  = raw_line
        self.samples = loadSamples(raw_line) 
        
        self.chrom
        self.pos
        self.ref
        self.alt
        self.qual
        self.filt
        

        self.AC
        self.AF
        self.BaseQRankSum
        self.DP
        self.Dels
        self.FS
        self.HaplotypeScore
        self.InbreedingCoeff
        self.MLEAC
        self.MLEAF
        self.MQ
        self.MQ0
        self.MQRankSum
        self.QD
        self.ReadPosRankSum
        self.SOR

    def _loadSamples(self,sline):
        pass

    def getSamples(self):
        pass

    def isAltSite(self):
        pass    

    def get
