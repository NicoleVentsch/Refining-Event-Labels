from .defaultFileHandlersFactory import FileConverterFactory, FileCreatorFactory
from pathlib import Path

import os


# Framework access to import and export event logs
# To expand framework functionality expand this class or register new file handlers
class FileUtilityBase:
    """
    Framework access to import and export event logs
    """

    def __init__(self, defaultDirectory):
        self._fileConverterFactory = FileConverterFactory()
        self._fileCreatorFactory = FileCreatorFactory()
        self.__defaultDirectory = defaultDirectory

    # creates file from event log
    def createFile(self, eventLog, fileName ,fileType):
        """
        function that creates a file from an event log

        :param eventLog: provided event log
        :param fileName: name of the created file
        :param fileType: file type of the created file
        :return: file created from the given event log with the given name and the given file type
        """
        fileCreator = self._fileCreatorFactory.create(fileType)
        return fileCreator.createFile(eventLog, self.__defaultDirectory, fileName)

    # converts file to event log
    def getEventLogFromFile(self, path):
        """
        function that converts a file to an event log

        :param path: path of the file
        """
        fileExtension = self.__getFileExtension(path)
        fileConverter = self._fileConverterFactory.create(fileExtension)
        return fileConverter.convert(path)
    
    # register a new file converter to expand import functionality
    def registerImport(self, fileType, fileConverter):
        """
        function that registers a new file converter to expand the import functionality

        :param fileType: type of the files that can be converted using the fileConverter
        :param fileConverter: file converter
        """
        self._fileConverterFactory.register(fileType, fileConverter)

    # register a new file creator to expand export functionality
    def registerExport(self, fileType, fileConverter):
        """
        function that registers a new file converter to expand the export functionality

        :param fileType: type of the files that can be converted using the fileConverter
        :param fileConverter: file converter
        """
        self._fileCreatorFactory.register(fileType, fileConverter)

    # private method to extract file extension from path
    def __getFileExtension(self, filePath):
        """
        function that extracts the file extension from the file path

        :param filePath: path of the file
        """
        return Path(filePath).suffix


