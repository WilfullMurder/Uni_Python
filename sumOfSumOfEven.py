class sumOfSumOfEven:

    def __init__(self):
        maxA = int(input("Please enter the maximum value of a: "))
        maxB = int(input("Please enter the maximum value of b: "))
        totalA = 0
        totalB = 0
        total = 0

        for n in range(1, maxA + 1):
            if (n % 2 == 0):
                print("a: ", "{0}".format(n))
                totalA += nz
                total += n

        for n in range(1, maxB + 1):
            if (n % 2 == 0):
                print("b: ", "{0}".format(n))
                totalB += n
                total += n

        print("The Sum of even numbers from 1 to {0} = {1}".format(maxA, totalA))
        print("The Sum of even from 1 to {0} = {1}".format(maxB, totalB))
        print("The sum of a+b: ", total)


