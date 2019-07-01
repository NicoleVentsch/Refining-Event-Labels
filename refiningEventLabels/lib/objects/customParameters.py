
class customParameters:
    """
    class for the custom parameters
    """
    def __init__(self, candidateLabels, horizontalThreshold, verticalThreshold, weightStructure, weightMatch, weightNoMatch):
        """
        initialization function

        """

        self.__candidateLabels = candidateLabels
        self.__horizontalThreshold = horizontalThreshold
        self.__verticalThreshold = verticalThreshold
        self.__weightStructure = weightStructure
        self.__weightMatch = weightMatch
        self.__weightNoMatch = weightNoMatch

    def getCandidateLabels(self):

        """
        function that returns the candidate labels

        """

        return self.__candidateLabels

    def getHorizontalThreshold(self):
        """
        function that returns the horizontal threshold

        """

        return self.__horizontalThreshold


    def getVerticalThreshold(self):

        """
        function that returns the vertical threshold

        """

        return self.__verticalThreshold

    def getStructureWeight(self):

        """

        function that returns the weight structure

        """

        return self.__weightStructure


    def getNoMatchWeight(self):
        """

        function that returns the weight for not matched pairs

        """

        return self.__weightNoMatch


    def getMatchWeight(self):
        """

        function that returns the weight for matched pairs

        """

        return self.__weightMatch


    def setcandidateLabels(self, candidateLabels):
        """

        function that sets the candidate labels

        """

        self.__candidateLabels = candidateLabels


    def setHorizontalThreshold(self, horizontalThreshold):
        """

        function that sets the horizontal threshold

        """

        self.__horizontalThreshold = horizontalThreshold


    def setVerticalThreshold(self, verticalThreshold):
        """
        function that sets the vertical threshold

        """

        self.__verticalThreshold = verticalThreshold


    def setStructureWeight(self, weightStructure):
        """
        function that sets the weight structure

        """

        self.__weightStructure = weightStructure


    def setNoMatchWeight(self, weightNoMatch):
        """

        function that sets the weight for not matched pairs

        """

        self.__weightNoMatch = weightNoMatch


    def setMatchWeight(self, weightMatch):
        """

        function that sets the weight for matched pairs

        """

        self.__weightMatch = weightMatch
