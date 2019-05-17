from abc import ABC, abstractmethod 
  
class FileHandlerFactory(ABC): 

    def __init__(self):
        self._fileHandlers = {}

    def create(self, fileType): 
        pass

    def register(self, fileType, fileHandler):
        self._fileHandlers[fileType] = fileHandler