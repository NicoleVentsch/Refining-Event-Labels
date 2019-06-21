from .defaultFileHandlersFactory import FileConverterFactory, FileCreatorFactory
from pathlib import Path

import os


# Framework access to import and export event logs
# To expand framework functionality expand this class or register new file handlers
class FileUtilityBase:

    def __init__(self, defaultDirectory):
        self._fileConverterFactory = FileConverterFactory()
        self._fileCreatorFactory = FileCreatorFactory()
        self.__defaultDirectory = defaultDirectory

    # creates file from event log
    def createFile(self, eventLog, fileName ,fileType):
        fileCreator = self._fileCreatorFactory.create(fileType)
        return fileCreator.createFile(eventLog, self.__defaultDirectory, fileName)

    # converts file to event log
    def getEventLogFromFile(self, path):
        fileExtension = self.__getFileExtension(path)
        fileConverter = self._fileConverterFactory.create(fileExtension)
        return fileConverter.convert(path)
    
    # register a new file converter to expand import functionality
    def registerImport(self, fileType, fileConverter):
        self._fileConverterFactory.register(fileType, fileConverter)

    # register a new file creator to expand export functionality
    def registerExport(self, fileType, fileConverter):
        self._fileCreatorFactory.register(fileType, fileConverter)

    # private method to extract file extension from path
    def __getFileExtension(self, filePath):
        return Path(filePath).suffix


