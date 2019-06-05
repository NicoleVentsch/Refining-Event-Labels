
class customParameters:
    
    def __init__(self, candidateLabels, horizontalThreshold, verticalThreshold, weightStructure, weightMatch, weightNoMatch):
        self.__candidateLabels = candidateLabels
        self.__horizontalThreshold = horizontalThreshold
        self.__verticalThreshold = verticalThreshold
        self.__weightStructure = weightStructure
        self.__weightMatch = weightMatch
        self.__weightNoMatch = weightNoMatch
        
    def getCandidateLabels(self):
        return self.__candidateLabels
    
    def getHorizontalThreshold(self):
        return self.__horizontalThreshold
    
    def getVerticalThreshold(self):
        return self.__verticalThreshold
    
    def getStructureWeight(self):
        return self.__weightStructure
    
    def getNoMatchWeight(self):
        return self.__weightNoMatch
        
    def getMatchWeight(self):
        return self.__weightMatch
    
    def setcandidateLabels(self, candidateLabels):
        self.__candidateLabels = candidateLabels
    
    def setHorizontalThreshold(self, horizontalThreshold):
        self.__horizontalThreshold = horizontalThreshold
    
    def setVerticalThreshold(self, verticalThreshold):
        self.__verticalThreshold = verticalThreshold
    
    def setStructureWeight(self, weightStructure):
        self.__weightStructure = weightStructure
        
    def setNoMatchWeight(self, weightNoMatch):
        self.__weightNoMatch = weightNoMatch
        
    def setMatchWeight(self, weightMatch):
        self.__weightMatch = weightMatch
        
    