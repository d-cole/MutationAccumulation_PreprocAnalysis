ALT,QUAL,FILTER,INFO = 4,5,6,7
MIN_MAP_QUALITY = 0 
GT,AD,DP,GQ,PL = 0,1,2,3,4;
MIN_MUT_GQ = 20
HETZ,HOMZ='0/1','0/0'
CHROM=0
DELS = 5
MAX_DELS = 0.0
class filterMethods():

    def __init__(self):
        pass
    #def __init__(self,medianFileLoc):
    #    self.SAMPLE_MEDIANS = self.getSampleMedians(medianFileLoc)
    #    self.MIN_VALID_SAMPLES_DP = int(14.0*(2.0/3.0))


    def getSampleMedians(self,medianFileLoc):
        """
        Returns SAMPLE_MEDIANS a 2d list where each sublist 
            is the lower and upper DP bounds.
            SAMPLE_MEDIANS = [[5,15],[10,30]..]
        """
        medFile = open(medianFileLoc,"r")
        for i, line in enumerate(medFile):
            if i == 1:
                SAMPLE_MEDIANS = [[float(i)*0.5,float(i)*1.5] for i in line.strip("\n").split(" ")]
        return SAMPLE_MEDIANS

    def validSampleDP(self,sample_idx,DP):
        """
        Returns whether the sample has a depth within the specified range
        """
        DP = float(DP)
        if DP >= self.SAMPLE_MEDIANS[sample_idx][0] and DP <= self.SAMPLE_MEDIANS[sample_idx][1]:
            return True
        return False

    def isDataLine(self,line):
        """
        Determines in line contains site data
        """
        if len(line) > 1:
            return line[0] != "#"

        return False
    
    def validInfoValue(self,tag,info,min_bound = None,max_bound = None):
        """
        Returns whether the specified info value is withen the given range
        If 'tag' is not found returns true
        """
        info_col = info.split(";")
        val = None
        val_pass = False

        for inf in info_col:
            if tag in inf:
               val = float(inf[inf.find("=") + 1:])
       
        if val == None:
            return True
 
        if min_bound != None and max_bound != None:
            return (val >= min_bound and val <= max_bound)

        else:
            if min_bound != None:
                return val >= min_bound
            if max_bound != None:
                return val <= max_bound
            else:
                return True 


    def callSiteFiltering(self,line_col):
        """
        Filters the site for:
            - on chromosome 'pseudo0'
            - no LowQual flag
            - 
        """
        if line_col[CHROM] == 'pseudo0':
            return False  

        return float(line_Col[QUAL] >= MIN_MAP_QUALITY) and \
            line_col[FILTER] != "LowQual"



    def siteFiltering(self,line_col):
        """
        Filters the site for:
            - on chromosome 'pseudo0'
            - presence of ALT base
            - no LowQual flag
        """
        if line_col[CHROM] == 'pseudo0':
            return False        

        if line_col[ALT] != ".":
            return float(line_col[QUAL] >= MIN_MAP_QUALITY) and \
                line_col[FILTER] != "LowQual" and \

                #Not necessary
                self.validInfoValue("Dels",line_col[INFO],None,None)
        return False

    def callSampleFiltering(self,samples):
        """
        Filters samples based on the requirements for callable sites
        """
        gt_counts={}
        for i in range(0,len(samples)):
            if "./." not in samples[i]:
                s_col = samples[i].split(":")

                gt_counts[s_col[0]] = get_counts.get(s_col[0],0) + 1

        return ((gt_counts.get(HETZ,0) == 1 and gt_counts.get(HOMZ,0) == 13) \
            or (gt_counts.get(HOMZ) == 14))



    def sampleFiltering(self,samples,remSample,mutIdx):
        """
        For the site to pass samples must:
            - no missing samples
            - One Sample GT must be different than others
        """
        gt_counts={}
        numValidDP = 0

        for i in range(0,len(samples)):
            if "./." not in samples[i]:
                s_col = samples[i].split(":")

                if self.validSampleDP(i,s_col[DP]):
                    numValidDP += 1

                gt_counts[s_col[0]] = gt_counts.get(s_col[0],0) + 1

        if numValidDP < self.MIN_VALID_SAMPLES_DP:
            #less than 2/3 of samples passed DP filters
            return False

        if (1 in gt_counts.values() and 13 in gt_counts.values()):
            if gt_counts.get(HETZ,0) == 1 and gt_counts.get(HOMZ,0) == 13:
                return self.filterMutant(gt_counts,samples,remSample,mutIdx)

        return False

    def filterMutant(self,gt_counts,samples,remMut,mutIdx):
        """
        Filters on the odd GT individual
        """
        for key in gt_counts.keys():
            if gt_counts.get(key) == 1:
                break

        for i in range(0,len(samples)):
            if key in samples[i]:
                break

        if remMut:
            if i == mutIdx:
                return False
        if int(samples[i].split(":")[GQ]) <= MIN_MUT_GQ:
            return False

        return self.validSampleDP(i,samples[i].split(":")[DP])
