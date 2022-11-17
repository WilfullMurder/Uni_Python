import random
import sys

import binary
import quick


class problem1:
    myList = []


    def __init__(self):
        self.sorter = binary.binary
        self.searcher = quick.quick

    def genNewArr(self, count):
        for i in range(count):
            self.printInsertion(self, i, i)
            self.myList.insert(i, i)

    def printInsertion(self, index, value):
        print("value: ", value, " inserted @ index: ", index)

    def printList(self):
        print(self.myList)

    def getNewIndex(self):
        return random.randint(0, self.myList.__len__()-1)

    def getNewValue(self):
        return self.getNewIndex(self)

    def insertRandRand(self):
        """
        Insert a random integer between 0 and array length -1 into a random index between 0 and array length -1
        """
        index = self.getNewIndex(self)
        value = self.getNewValue(self)
        self.myList.insert(index, value)
        self.printInsertion(self, index, value)

    def insertFixedRand(self, index=0):
        """
        Insert a random integer between 0 and array length -1 into a fixed index
        """
        value = self.getNewValue(self)
        self.myList.insert(index, value)
        self.printInsertion(self, index, value)

    def insertRandFixed(self, value=0):
        """
        Insert a fixed integer into a random index between 0 and array length -1
        """
        index = self.getNewIndex(self)
        self.myList.insert(index, value)
        self.printInsertion(self, index, value)

    def insertFixedFixed(self, index=0, value=0):
        """
           Insert a fixed integer into a fixed
        """
        self.myList.insert(index, value)
        self.printInsertion(self, index, value)

    def findByValue(self, value=0):
        tmp = self.myList
        for i in range(self.myList.__len__()-1):
            if tmp.__getitem__(i) == value:
                print("Value: ", value, " found @ index: ", i)
                return True
        print("Value: ", value, " not found!!")
        return False

    def findValue(self, value=0, i=0):
        v = self.myList.__getitem__(i)
        if v == value:
            print("Value: ", value, " found @ index: ", i)
            return True

        return False


    def removeAtIndex(self, index=0):
        """Remove a value at the given index"""
        tmp = self.myList
        for i in range(self.myList.__len__()-1):
            if i == index:
                value = self.myList.__getitem__(i)
                print("Value: ", value, "removed @ index: ", i)
                tmp.remove(self.myList.__getitem__(i))
        self.myList = tmp

    def removeValue(self, value=0):
        """Remove first value only"""
        tmp = self.myList
        for i in range(self.myList.__len__()-1):
            if self.findValue(self, value, i):
                tmp.remove(self.myList.__getitem__(i))

        self.myList = tmp

    def removeDuplicates(self, toSearch=[]):
        """Uses in,not-in to track a list for any duplicates and returns the clean list."""
        toSearch.sort()
        checker = []
        for i in toSearch:
            if i not in checker:
                checker.append(i)
            else:
                print("Duplicate value: ", i, " removed")

        if checker.__len__() <= 1:
            print("No duplicates found!!")
            return toSearch
        else:
            return checker








    def findFactor(self, toSearch=[], multiple=0):
        """Determine whether any element of list is a  factor of multiple"""
        tmp = toSearch
        result = []
        count = 0
        for i in range(tmp.__len__()):
            if tmp.__getitem__(i) % multiple == 0:
                print("value: ", tmp.__getitem__(i), "is a factor of: ", multiple)
                result.insert(count, tmp.__getitem__(i))
                count += 1
        print("values from list that are multiples of ", multiple, ": ", result)

    def findNotFactor(self, toSearch=[], multiple=0):
        """Determine whether any element of list is not a  factor of multiple"""
        tmp = toSearch
        result = []
        count = 0
        for i in range(tmp.__len__()):
            if tmp.__getitem__(i) % multiple != 0:
                print("value: ", tmp.__getitem__(i), "is not a factor of: ", multiple)
                result.insert(count, tmp.__getitem__(i))
                count += 1
        print("values from list that are not multiples of ", multiple, ": ", result)

    def findLargestValue(self, toSearch=[]):
        tmp = toSearch
        result = 0
        for i in range(tmp.__len__() - 1):
            if result < tmp.__getitem__(i):
                result = tmp.__getitem__(i)
        return result

    def findSmallestValue(self, toSearch=[]):
        tmp = toSearch
        result = sys.maxsize * 2 + 1
        for i in range(tmp.__len__() - 1):
            if result > tmp.__getitem__(i):
                result = tmp.__getitem__(i)
        return result
