"""
digitSum class takes an INTEGER INPUT and OUTPUTS the SUM OF ALL DIGITS
"""
class digitSum:

    def __init__(self):
        num = int(input("Please input the desired Integer: "))
        total = 0

        while(num > 0):
            digit = num % 10
            total += digit
            num = num//10

        print("Sum of digits: ", total)

