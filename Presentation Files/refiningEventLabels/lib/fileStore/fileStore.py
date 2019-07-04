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

    def storeFile(self, currentFilePath):
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
    def files(self):
        return self.__files

    @property
    def lastFile(self):
        return self.__files[0]

    @property
    def filesInfo(self):
        fileInfos = []
        for file in self.__files:
            fileInfos.append({"name": file, "tstamp": os.path.getmtime(file) })
        return fileInfos



    

    

    
    


        
    
