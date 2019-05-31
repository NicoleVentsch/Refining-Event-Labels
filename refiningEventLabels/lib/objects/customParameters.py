
class customParameters:
    
    def __init__(self, horizontalTreshold, verticalTreshold, weightStructure, weightMatch, weightNoMatch):
        self.__horizontalTreshold = horizontalTreshold
        self.__verticalTreshold = verticalTreshold
        self.__weightStructure = weightStructure
        self.__weightMatch = weightMatch
        self.__weightNoMatch = weightNoMatch
        
    
    def getHorizontalTreshold(self):
        return self.__horizontalTreshold
    
    def getVerticalTreshold(self):
        return self.__verticalTreshold
    
    def getStructureWeight(self):
        return self.__weightStructure
    
    def getNoMatchWeight(self):
        return self.__weightNoMatch
        
    def getMatchWeight(self):
        return self.__weightMatch
    
    def setHorizontalTreshold(self, horizontalTreshold):
        self.__horizontalTreshold = horizontalTreshold
    
    def setVerticalTreshold(self, verticalTreshold):
        self.__verticalTreshold = verticalTreshold
    
    def setStructureWeight(self, weightStructure):
        self.__weightStructure = weightStructure
        
    def setNoMatchWeight(self, weightNoMatch):
        self.__weightNoMatch = weightNoMatch
        
    def setMatchWeight(self, weightMatch):
        self.__weightMatch = weightMatch
        
    