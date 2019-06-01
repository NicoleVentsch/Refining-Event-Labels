import glob
import os

class FileStore():

    def __init__(self, config):
        self.__fileStoreConfig = config
        self.__files = []
        self.checkDir()

    def checkDir(self):
        self._getFiles()
        self._removeOldestFiles()

    def saveFileInDir(self, currentFilePath):
        fileName = os.path.basename(currentFilePath)
        newFilePath = os.path.join(self.__fileStoreConfig.destinationFolder, fileName)
        os.rename(currentFilePath, newFilePath)
        self.__files.insert(0, newFilePath)
        self._removeOldestFiles()

    def _getFiles(self):
        self.__files = glob.glob(os.path.join(self.__fileStoreConfig.destinationFolder, "*"))
        self.__files = filter(os.path.isfile, self.__files)
        self.__files = [os.path.join(self.__fileStoreConfig.destinationFolder, f) for f in self.__files]
        self.__files.sort(key=lambda x: os.path.getmtime(x))

    def _removeOldestFiles(self):
        numberToManyFiles = len(self.__files) - self.__fileStoreConfig.numberFiles
        self._delteFiles(numberToManyFiles)


    def _delteFiles(self, numberFiles):
         while numberFiles > 0:
            os.remove(self.__files[-1])
            del self.__files[-1]
            numberFiles -= 1
    
    @property
    def Files(self):
        return self.__files


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



    

    

    
    


        
    
