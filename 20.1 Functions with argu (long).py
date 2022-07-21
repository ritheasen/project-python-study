def printNameForNTimes(name,numOfTimes):
    print((name+"\n")*numOfTimes)

name = input("Input your name")
num = int(input("Input number of times to be printed: "))
printNameForNTimes(name, num)