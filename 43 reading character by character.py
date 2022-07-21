f = open("source.txt","r")

while True:
    myChar = f.read(1)
    if not myChar:
        break
    else:
        print(myChar)
    #print(f.read(1))