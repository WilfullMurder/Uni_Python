class digitReversal:

    num = 0
    revNum = 0

    def __init__(self):
        self.num = int(input("Enter Integer: "))

        while(self.num > 0):

            remainder = self.num % 10
            self.revNum = (self.revNum * 10) + remainder
            self.num = self.num // 10

        print("The reverse is: {}".format(self.revNum))