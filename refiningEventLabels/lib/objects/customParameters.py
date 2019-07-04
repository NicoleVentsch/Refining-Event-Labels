
class customParameters:
    """
    customParameters class containing all the parameters needed for the algorithm
    """
    
    def __init__(self, candidateLabels, horizontalThreshold, verticalThreshold, weightStructure, weightMatch, weightNoMatch):
        """
         Instantiation of the the parameters
        """

        self.__candidateLabels = candidateLabels
        self.__horizontalThreshold = horizontalThreshold
        self.__verticalThreshold = verticalThreshold
        self.__weightStructure = weightStructure
        self.__weightMatch = weightMatch
        self.__weightNoMatch = weightNoMatch
        

    def getCandidateLabels(self):
        """
        Get the list of candidate labels
    
        :return: a list containing the candidate labels
        """

        return self.__candidateLabels

    def getHorizontalThreshold(self):
        """
        Get the horizontal threshold
    
        :return: horizontal threshold (floating point number)
        """

        return self.__horizontalThreshold


    def getVerticalThreshold(self):
        """
        Get the vertical threshold
    
        :return: vertical threshold (floating point number)
        """

        return self.__verticalThreshold

    def getStructureWeight(self):
        """
        Get the structure weight
    
        :return: structure weight (floating point number)
        """

        return self.__weightStructure


    def getNoMatchWeight(self):
        """
        Get the no match weight
    
        :return: no match weight (floating point number)
        """

        return self.__weightNoMatch


    def getMatchWeight(self):
        """
        Get the match weight
    
        :return: match weight (floating point number)
        """

        return self.__weightMatch


    def setcandidateLabels(self, candidateLabels):
        """
        Update the list of candidate labels
    
        :param candidateLabels: a list with the new candidate labels
        """

        self.__candidateLabels = candidateLabels


    def setHorizontalThreshold(self, horizontalThreshold):
        """
        Update the horizontal threshold parameter
    
        :param horizontalThreshold: a floating point number 
        """

        self.__horizontalThreshold = horizontalThreshold


    def setVerticalThreshold(self, verticalThreshold):
        """
        Update the horizontal threshold parameter
    
        :param horizontalThreshold: a floating point number 
        """

        self.__verticalThreshold = verticalThreshold


    def setStructureWeight(self, weightStructure):
        """
        Update the structure weight parameter
    
        :param weightStructure: a floating point number 
        """

        self.__weightStructure = weightStructure


    def setNoMatchWeight(self, weightNoMatch):
        """
        Update the no match weight parameter
    
        :param weightNoMatch: a floating point number 
        """

        self.__weightNoMatch = weightNoMatch


    def setMatchWeight(self, weightMatch):
        """
        Update the match weight parameter
    
        :param weightMatch: a floating point number 
        """

        self.__weightMatch = weightMatch
