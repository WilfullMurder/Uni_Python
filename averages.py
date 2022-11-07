from collections import Counter

"""
Averages class takes an INTEGER INPUT for the amount of INPUTS, MULTIPLE
INTEGER INPUTS and OUTPUTS the AVERAGES OF INPUTS
"""
class Averages:
    nums = []
    inputs = 0
    count = 0
    total = 0
    occurrences = 0
    avg = {"Mean": 0, "Mode": 0, "Median": 0,
           "Range": 0}  ##we need to ensure a sorted the list for mode, median and range

    def __init__(self):
        self.inputs = int(input("Please input the amount of numbers to be averaged: "))

        while self.nums.__len__() < self.inputs:
            num = int(input("Please input an integer: "), 10)
            self.nums.append(num)
            self.total += self.nums[self.count]
            self.count += 1

        self.nums.sort()

        self.avg["Mean"] = self.total / self.count

        occurrences = Counter(self.nums).most_common()
        self.avg["Mode"] = occurrences[0][0]
        modeCount = occurrences[0][1]

        medianIndex = int((self.nums.__len__() + 1) / 2)
        self.avg["Median"] = self.nums[medianIndex]

        self.avg["Range"] = self.nums.__getitem__(self.nums.__len__() - 1) - self.nums[0]

        print("Total:", self.total)
        print("Count:", self.count)
        print("Averages:", "\n Mean:", self.avg["Mean"],
              "\n Mode:", self.avg["Mode"], "occurs: ", modeCount,
              "\n Median:", self.avg["Median"], "\n Range:", self.avg["Range"])
