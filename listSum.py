class listSum:
    numList = []

    def __init__(self):
        count = int(input("Please enter list length: "))

        while self.numList.__len__() < count:
            self.numList.append(int(input("Please enter an integer: ")))

        print("Sum: ", (sum(self.numList)))
