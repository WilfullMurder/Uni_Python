import random

import File_Problems
import List_Problems
import quick


def main():
    p = List_Problems.problem1
    # runProblem1(p)
    # runProblem2(p)
    # runProblem3(p)
    # runProblem4(p)
    # runProblem5(p)
    # runProblem6(p)
    f = File_Problems.FileProblems
    runProblem7(f)
    #runProblem8(f)
    runProblem9(f)


def runProblem1(problem=None):
    """python program that inserts a number into any position in a list"""
    p1 = problem
    p1.genNewArr(p1, 10)
    p1.printList(p1)
    p1.insertRandRand(p1)
    p1.printList(p1)
    p1.insertFixedRand(p1, 5)
    p1.insertRandFixed(p1, 18)
    p1.insertFixedFixed(p1, 6, 37)
    p1.printList(p1)


def runProblem2(problem=None):
    """ Python program that deletes an element from a list by index"""
    p2 = problem
    p2.removeAtIndex(p2, 4)
    p2.printList(p2)
    p2.removeValue(p2, 2)
    p2.removeValue(p2, 222)


def runProblem3(problem=None):
    """Python program that finds the odd numbers in a list of integers"""
    p3 = problem
    p3.findNotFactor(p3, p3.myList, 2)


def runProblem4(problem=None):
    """Python program that finds the largest number in a list without using built-in functions"""
    p4 = problem
    print("Largest value: ", p4.findLargestValue(p4, p4.myList))
    print("Smallest value: ", p4.findSmallestValue(p4, p4.myList))


def runProblem5(problem=None):
    """ Python program that searches a given number in a list of integers"""
    p5 = problem
    p5.findByValue(p5, 5)
    p5.findByValue(p5, 622)


def runProblem6(problem=None):
    """ Python program that removes duplicates from a list"""
    p6 = problem
    p6.removeDuplicates(p6, p6.myList)
    print(p6.myList)
    for i in range(5):
        p6.myList.append(5)
    print(p6.myList)
    p6.myList = p6.removeDuplicates(p6, p6.myList)
    print(p6.myList)


def runProblem7(problem=None):
    f = problem
    f.setNewByFileName(f, "problem7.txt")
    print("Number of lines: ", f.readLines(f))
    print("number of words: ", f.countWords(f))



def runProblem8(problem=None):
    f = problem
    f.setNewFileName(f)
    f.countWords(f)


def runProblem9(problem=None):
    f = problem
    f.countWords(f)
    f.removeDuplicateLines(f)
    f.countWords(f)
    f.readFileByName(f, f.outfileName)


main()
