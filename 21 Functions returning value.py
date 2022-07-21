def getName():

    print("This is a function with a return value...")
    name = input("Enter your name")
    return name

def getNameAndConvertToLowerCase():
    name = input("Enter your name to be converted into lower case:")
    convertedName = name.lower()
    return convertedName

def getNameAndConvertToUpperCase():

    return input("Enter your name tov convert into uppercase: ").upper()

#returnedValue = getName()
#print(returnedValue)

#returnedName = getNameAndConvertToLowerCase()
#print(returnedName)

print(getNameAndConvertToLowerCase())
print(getNameAndConvertToUpperCase())
