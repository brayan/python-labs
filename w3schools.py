# W3Schools - Python

print("Hello World")

if 5 > 2:
    print("Five is greater than two")

# Casting
print(str(3))
print(int(3))
print(float(3))

# Type

def printTypes():
    myString = "My string"
    print(type(myString))

    myInt = 20
    print(type(myInt))

    myFloat = 20.5
    print(type(myFloat))

    myComplex = 1j
    print(type(myComplex))

    myList = ["apple", "banana", "cherry"]
    print(type(myList))

    myTuple = ("apple", "banana", "cherry")
    print(type(myTuple))

printTypes()

# Values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"


# Unpack a collection
fruits = ["Orange", "Banana", "Cherry"]
a, b, c = fruits

def defineGlobalVariableInsideFunction():
    global myGlobalVariable
    myGlobalVariable = "My global string"
    print(myGlobalVariable)

defineGlobalVariableInsideFunction()

day = 8
month = 12
year = 2020
print(day, month, year, sep="/")

exit()