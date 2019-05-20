from abc import ABC, abstractmethod 

# Defines Factory base class for file creation and conversion
class FileHandlerFactory(ABC): 

    def __init__(self):
        self._fileHandlers = {}

    # returns the right file handler depending on the file type
    def create(self, fileType): 
        pass

    # register a new file handler for a given file type
    def register(self, fileType, fileHandler):
        self._fileHandlers[fileType] = fileHandler

# Abstract class to create different files types from for event logs
class FileCreator(ABC):

    def __init__(self):
        self.__destinationPath = "."
        self._fileType = ""
    
    def getFileType(self):
        return self._fileType 
    
    # sets default path for a created file
    def setDestinationPath(self, destinationPath):
        self.__destinationPath = destinationPath
    
    # gets default path for a created file
    def getDestinationPath(self):
        return self.__destinationPath

    #create a file from a event log
    def createFile(self, eventLog, fileName = "", filePath = ""):
        pass

# Abstract class to convert different file types to event logs
class FileConverter(ABC):

    def __init__(self):
        self._fileType = ""
    
    # create the destination file type
    def getFileType(self):
        return self._fileType 

    # converts file to event log
    def convert(self, filePath):
        pass