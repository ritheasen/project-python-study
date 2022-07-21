def nameAsArgm():
    names = str(input("Enter name"))
    #print(names)
    #print(len(names))
    middleChar = int(len(names)/2 - 0.5)
    print(f"This is the middle character of name : {names[middleChar]}")
nameAsArgm()