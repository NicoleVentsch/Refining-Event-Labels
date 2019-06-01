class FileStoreConfig():
    defaultMaxNumberFiles = 5
    def __init__(self, destinationFolder, numberFiles, allowedFileType):
        self.__destinationFolder = destinationFolder
        self.__numberFiles = numberFiles
        self.__allowedFileTypes = allowedFileType

    @staticmethod
    def CreateWithFileTypes(destinationFolder, allowedFileType):
        return FileStoreConfig(destinationFolder, FileStoreConfig.defaultMaxNumberFiles, allowedFileType)

    @staticmethod
    def CreateWithMaxNumberFiles(destinationFolder, numberFiles):
        return FileStoreConfig(destinationFolder, numberFiles, [])

    @staticmethod
    def CreateWithMaxNumberFilesAndFilesTypes(destinationFolder, numberFiles, allowedFileType):
        return FileStoreConfig(destinationFolder, numberFiles, allowedFileType)

    def addFilesType(self, type):
        self.__allowedFileTypes.add(type) 
    
    def getFilesTypes(self):
        return self.__allowedFileTypes
    
    @property
    def allowedFileTypes(self):
        return self.__allowedFileTypes
    
    @property
    def numberFiles(self):
        return self.__numberFiles
    
    @numberFiles.setter
    def numberFiles(self, numberFiles):
        self.__numberFiles = self

    @property
    def destinationFolder(self):
        return self.__destinationFolder