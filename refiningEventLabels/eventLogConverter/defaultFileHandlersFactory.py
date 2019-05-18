from fileHandlerBase import FileHandlerFactory

class FileConverterFactory(FileHandlerFactory):
    
    def create(self, fileType): 
        if fileType in self._fileHandlers:
            return self._fileHandlers[fileType]
        #TODO: raise WrongFileFromatError

class FileCreatorFactory(FileHandlerFactory):

    def __init__(self, defaultFileHandler):
        self._defaultFileHandler = defaultFileHandler
    
    def create(self, fileType): 
        if fileType in self._fileHandlers:
            return self._fileHandlers[fileType]
        else:
            return self._defaultFileHandler