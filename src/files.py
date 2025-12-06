
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
  
  
  
"""
  
import csv
import json

def loadJson(fileName):
    with open(fileName + '.json') as f:
        d = json.load(f)
        return d
    return None

def loadCsv(fileName):
    with open(fileName + ".csv") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        next(reader, None)  # skip the headers
        return [row for row in reader]

def writeCsv(name, content):
    with open(name + ".csv", "wt") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerows(content)

  
  """