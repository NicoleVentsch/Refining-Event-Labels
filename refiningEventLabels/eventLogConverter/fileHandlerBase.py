from abc import ABC, abstractmethod 
  
class FileHandlerFactory(ABC): 

    def __init__(self):
        self._fileHandlers = {}

    def create(self, fileType): 
        pass

    def register(self, fileType, fileHandler):
        self._fileHandlers[fileType] = fileHandler

class FileCreator(ABC):

    def __init__(self):
        self.__destinationPath = "."
        self._fileType = ""
    
    def getFileType(self):
        return self._fileType 
    
    def setDestinationPath(self, destinationPath):
        self.__destinationPath = destinationPath
    
    def getDestinationPath(self):
        return self.__destinationPath

    def createFile(self, eventLog, fileName = ""), filePath = "":
        pass
        
class FileConverter(ABC):

    def __init__(self):
        self._fileType = ""
    
    def getFileType(self):
        return self._fileType 

    def convert(self, filePath):
        pass