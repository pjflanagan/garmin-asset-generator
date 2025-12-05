
import os


def getFolderName(size, subfolder):
  return f"out/resources-round-{size}x{size}/{subfolder}/"

def makeFolderIfNotExists(folderPath):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
        
def getFolder(size, subfolder):
    folderPath = getFolderName(size, subfolder)
    makeFolderIfNotExists(folderPath)
    return folderPath