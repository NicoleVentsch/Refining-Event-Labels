from abc import ABC, abstractmethod 

# Defines Factory base class for file creation and conversion
class FileHandlerFactory(ABC):
    """
    defines factory base class for file creation and conversion
    """

    def __init__(self):
        self._fileHandlers = {}

    # returns the right file handler depending on the file type
    def create(self, fileType):
        """
        returns the right file handler depending on the file type
        :param fileType: the file type of the provided file
        :return: file handler according to file type
        """
        pass

    # register a new file handler for a given file type
    def register(self, fileType, fileHandler):
        """
        register a new file handler for a given file type
        :param fileType: the file type of the provided file
        :param fileHandler: the handler that should be registered
        """
        self._fileHandlers[fileType] = fileHandler

# Abstract class to create different files types from for event logs
class FileCreator(ABC):
    """
    Abstract class to create different files types from for event logs
    """

    def __init__(self):
        self.__destinationPath = "."
        self._fileType = ""
    
    def getFileType(self):
        """
        get function for the file type
        """
        return self._fileType 
    
    # sets default path for a created file
    def setDestinationPath(self, destinationPath):
        """
        set function for the destination path
        """
        self.__destinationPath = destinationPath
    
    # gets default path for a created file
    def getDestinationPath(self):
        """
        get function for the destination path
        """
        return self.__destinationPath

    #create a file from a event log
    def createFile(self, eventLog, fileName = "", filePath = ""):
        """
        function that creates a file from a given event log
        :param eventLog: event log
        :param fileName: name of the file that will be created
        :param filePath: path of the file that will be created
        :return: file created from an event log with the provided namen at the provided path
        """
        pass

# Abstract class to convert different file types to event logs
class FileConverter(ABC):
    """
    abstract class to convert different file types to event logs
    """

    def __init__(self):
        self._fileType = ""
    
    # create the destination file type
    def getFileType(self):
        """
        function that creates the destination file type
        """
        return self._fileType 

    # converts file to event log
    def convert(self, filePath):
        """
        function that converts a file to an event log
        :param filePath: path of the file
        """
        pass