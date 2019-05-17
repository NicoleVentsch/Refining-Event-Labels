from defaultFileHandlersFactory import FileConverterFactory, FileCreatorFactory
from pathlib import Path



class FileUtilityBase:

    def __init__(self, defaultDirectory):
        self._fileConverterFactory = FileConverterFactory()
        self._fileCreatorFactory = FileCreatorFactory(None)
        self.__defaultDirectory = defaultDirectory

    def createFile(self, eventLog, fileName ,fileType):
        fileCreator = self._fileCreatorFactory.create(fileType)
        return fileCreator.createFile(eventLog, self.__defaultDirectory, fileName)

    def getEventLogFromFile(self, path):
        fileExtension = self.__getFileExtension(path)
        fileConverter = self._fileConverterFactory.create(fileExtension)
        return fileConverter.convert(path)
    
    def registerImport(self, fileType, fileConverter):
        self._fileConverterFactory.register(fileType, fileConverter)


    def registerExport(self, fileType, fileConverter):
        self._fileCreatorFactory.register(fileType, fileConverter)

    def __getFileExtension(self, filePath):
        return Path(filePath).suffix


