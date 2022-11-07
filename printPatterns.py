def PrintPattern(pattern ="", rows = 0):
    match pattern:

        case 'half pyramid r':
            x = 1
            while x <= rows:
                y = 1
                while y <= x:
                    print("*", end="")
                    y += 1
                print()
                x += 1

        case 'half pyramid l':
            x = 1
            while x <= rows:
                print(" " * (rows - x) + "*" * x)
                x += 1

        case 'pyramid':
            x = 0
            while (x < rows):
                x += 1
                spaces = rows - x

                spaces_counter = 0
                while (spaces_counter < spaces):
                    print(" ", end='')
                    spaces_counter += 1

                num_stars = 2 * x - 1
                while (num_stars > 0):
                    print("*", end='')
                    num_stars -= 1

                print()

        case 'inverted pyramid':
            x = rows
            while x >= 1:
                # printing stars
                print(" " * (rows - x) + "*" * x)
                x -= 1

        case "right pascal triangle":
            x = 1
            while x < rows:
                print("*" * x)
                x += 1
            x = rows
            while x > 0:
                print("*" * x)
                x -= 1

        case 'left pascal triangle':
            x = 1
            while x <= rows:
                y = x
                while y < rows:
                    print(' ', end=' ')
                    y += 1
                z = 1
                while z <= x:
                    print('*', end=' ')
                    z += 1
                print()
                x += 1

            x = rows
            while x >= 1:
                y = x
                while y <= rows:
                    print(' ', end=' ')
                    y += 1
                z = 1
                while z < x:
                    print('*', end=' ')
                    z += 1
                print('')
                x -= 1

        case 'star':
            x = 0
            while (x < rows):
                x += 1
                spaces = rows - x

                spaces_counter = 0
                while (spaces_counter < spaces):
                    print(" ", end='')
                    spaces_counter += 1

                num_stars = 2 * x - 1
                while (num_stars > 0):
                    print("*", end='')
                    num_stars -= 1

                print()

            x = rows
            while (x > 0):
                x -= 1
                spaces = rows - x

                spaces_counter = 0
                while (spaces_counter < spaces):
                    print(" ", end='')
                    spaces_counter += 1

                num_stars = 2 * x - 1
                while (num_stars > 0):
                    print("*", end='')
                    num_stars -= 1

                print()

        case 'hollow star':
            x = 1
            while x <= rows:
                y = rows
                while y > x:
                    # display space
                    print(' ', end=' ')
                    y -= 1
                print('*', end=' ')
                z = 1
                while z < 2 * (x - 1):
                    print(' ', end=' ')
                    z += 1
                if x == 1:
                    print()
                else:
                    print('*')
                x += 1

            x = rows - 1
            while x >= 1:
                y = rows
                while y > x:
                    print(' ', end=' ')
                    y -= 1
                print('*', end=' ')
                z = 1
                while z < 2 * (x - 1):
                    print(' ', end=' ')
                    z += 1
                if x == 1:
                    print()
                else:
                    print('*')
                x -= 1

        case 'hourglass':
            x = 0
            while x <= rows - 1:
                y = 0
                while y < x:
                    print('', end=' ')
                    y += 1
                z = x
                while z <= rows - 1:
                    print('*', end=' ')
                    z += 1
                print()
                x += 1

            x = rows - 1
            while x >= 0:
                y = 0
                while y < x:
                    print('', end=' ')
                    y += 1
                z = x
                while z <= rows - 1:
                    print('*', end=' ')
                    z += 1
                print('')
                x -= 1


class patternPrinter:


    availablePatterns = ["half pyramid r", "half pyramid l", "pyramid", "inverted pyramid", "right pascal triangle", "left pascal triangle", "star", "hollow star", "hourglass"]

    def __init__(self):
        pattern = input("Please enter pattern type i.e. pyramid (type 'help' for pattern types): ")
        if pattern == 'help':
            print("Avaliable patterns: ", self.availablePatterns)
            pattern = input("Please enter pattern type i.e. pyramid (type 'help' for pattern types: ")
        rows = int(input("Please enter number of rows (Integer)"))
        PrintPattern(pattern, rows)




