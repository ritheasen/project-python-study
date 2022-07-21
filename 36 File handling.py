def createMyFile():
    myFile = open("firstfile.txt","a")
    print(myFile)

    myFile.write("This is new line")


createMyFile()

