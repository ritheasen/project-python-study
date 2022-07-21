



def addTwoNumbers():
    firstNum = int(input("Enter first number"))
    secNum = int(input("Enter Second number"))
    numSum = firstNum + secNum
    print("The sum of two number is: ", numSum)

def substractTwoNumbers():
    firstNum = int(input("Enter first number"))
    secNum = int(input("Enter Second number"))
    numSub = firstNum - secNum
    print("The substract of two number is: ", numSub)

def multiplyTwoNumbers():
    firstNum = int(input("Enter first number"))
    secNum = int(input("Enter Second number"))
    numMul = firstNum * secNum
    print("The product of two number is: ", numMul)

def divTwoNumbersQ():
    firstNum = int(input("Enter first number"))
    secNum = int(input("Enter Second number"))
    numDiv = firstNum / secNum
    print("The Quotient of two number is: ", numDiv)

def divTwoNumbersR():
    firstNum = int(input("Enter first number"))
    secNum = int(input("Enter Second number"))
    numDivr = firstNum % secNum
    print("The Quotient of two number is: ", numDivr)

choice = int(input("Input your choice of operation\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division(Quotient)\n5. Division(Remainder)"))

if choice ==1:
    addTwoNumbers()
elif choice ==2:
    substractTwoNumbers()
elif choice ==3:
    multiplyTwoNumbers()
elif choice ==4:
    divTwoNumbersQ()
elif choice ==5:
    divTwoNumbersR()



