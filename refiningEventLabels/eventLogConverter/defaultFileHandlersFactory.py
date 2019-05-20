from fileHandlerBase import FileHandlerFactory

class FileConverterFactory(FileHandlerFactory):
    
    def create(self, fileType): 
        if fileType in self._fileHandlers:
            return self._fileHandlers[fileType]
        #TODO: raise WrongFileFromatError

class FileCreatorFactory(FileHandlerFactory):

    def __init__(self):
    
    def create(self, fileType): 
        if fileType in self._fileHandlers:
            return self._fileHandlers[fileType]
        else:
            return self._fileHandlers[0]