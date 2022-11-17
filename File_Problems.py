import os.path
import sys

PUNCT_DICT = {0: ",", 1: ".", 2: "!", 3: "?", 4: "[", 5: "]", 6: ":", 7: "#"}


class FileProblems:
    ROOT_DIR = ""
    fileName = ""
    outfileName = "boujee.txt"

    def __init__(self):
        pass

    def setNewFileName(self):
        fileName = str(input("Please input fileName.ext: "))
        self.fileName = fileName
        self.ROOT_DIR = os.path.dirname(os.path.realpath(fileName))

    def setNewByFileName(self, fileName):
        self.fileName = fileName
        self.ROOT_DIR = os.path.dirname(os.path.realpath(fileName))

    def readFile(self):
        with open(self.fileName, 'r') as file:
            for each in file:
                print(each)

    def readFileByName(self, fileName):
        with open(fileName, 'r') as file:
            for each in file:
                print(each)

    def readLines(self):
        numLines = 0
        with open(self.fileName, 'r') as file:
            numLines = len(file.readlines())
        return numLines

    def countWords(self):
        with open(self.fileName, 'r') as file:
            numw = 0
            for line in file:
                words = line.split()
                numw += len(words)

        return numw

    def removeDuplicateLines(self):
        checked = set()
        out = open(self.outfileName, "w")
        for line in open(self.fileName, "r"):
            if self.checkForDuplicates(self, line, checked):
                out.write(line)
                checked.add(line)
        out.close()


    def checkForDuplicates(self, line, checkedLines):
        if line not in checkedLines:
            return True
        else:
            return False
