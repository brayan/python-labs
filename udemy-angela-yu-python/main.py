
def askAndPrintName():
    name = input("What's your name?\n")
    print("Hello, " + name + "!")

    nameSize = len(name)
    print(f"String size: {nameSize}")


def printDataTypes():
    # string
    print("String with 'single quotes' " + " inside")

    print("Hello"[0])

    # int
    print(str(123_456_789) + " same thing as " + str(123456789))

    #float
    print(type(3.14159))

    #boolean
    print(type(True))


def sumTwoDigits():
    numbers = input("Enter two digits here:\n")
    print(int(numbers[0]) + int(numbers[1]))


def mathOperators():
    print(3 + 5)
    print(7 - 4)
    print(3 * 2)
    print(6 / 3)
    print(2 ** 3)
    print(round(8 / 3, 2))
    print (8 // 3) # // divide and convert to integer


def calculateBmi():
    weight = input("Weight: ")
    height = input("Height: ")

    # bmi = float(weight) / float(height) ** 2
    bmi = float(weight) / (float(height) * 2)

    print(f"Your body mass index is {int(bmi)}")


# calculateBmi()
# mathOperators()
# sumTwoDigits()
# printDataTypes()
# askAndPrintName()