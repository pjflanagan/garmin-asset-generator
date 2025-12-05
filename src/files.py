
import os


def getFolderName(directory, size, subfolder):
  return f"{directory}/resources-round-{size}x{size}/{subfolder}/"

def makeFolderIfNotExists(folderPath):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
        
def getFolder(directory, size, subfolder):
    folderPath = getFolderName(directory, size, subfolder)
    makeFolderIfNotExists(folderPath)
    return folderPath