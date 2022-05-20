num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))

if num1 > num2:
        if num1 > num3:
            print("Number 1 is the biggest")
        else:
            print("Number 3 is the biggest")
elif num2 > num3:
    print("Number 2 is the biggest")
else:
    print("Number 3 is the biggest")
else:
    if num2 > num3:
        print("Number 2 is the biggest")
    else:
        print("Number 3 is the biggest")