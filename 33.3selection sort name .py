#["Daravuth","Sen","Panha","Sara pich","Thearin"]

def selectionSort(nameList):
    for i in range(0,len(nameList)):
        short = i
        for j in range(i+1,len(nameList)):
            if len(nameList[j]) < len(nameList[short]):
                short = j
        nameList[i],nameList[short] = nameList[short],nameList[i]
        print(nameList)
    #print(nameList)
selectionSort(["Daravuth","Sen","Panha","Sara pich","Thearin"])
