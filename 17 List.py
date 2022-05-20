
nameList = ['Daravuth','Sarapich','Theany','Kim hong','Chatra']

print(nameList)
print(nameList[len(nameList)-1])
print(nameList[-1])

#The insert method adds new element to specific index
nameList.insert(len(nameList)-1,"Chatra")
nameList.insert(0,"Chatra")
print(nameList)

#The append method always add the elemend to last index
nameList.append("Thearin")
print(nameList)

#The pop method will remove and return the last element in the list
#The pop method will remove and return the last element in the list
removeElement = nameList.pop(2)
print(nameList)
print(f"The element removed: {removeElement}")

#count method will return the total no of occurrences of particular elemnt\
print(nameList.count('Chatra'))

#copy method will copy the element of one list to another
# copy method and = sign can be interchangable be used
#May not be a very useful method
list11 = [10,20,30,400,50,60]
list22 = list11.copy()
#list2 = list1

print(f"List 11: {list11}")
print(f"List 22: {list22}")

#extend method will add the list items into another list
list11.extend(list22)
print(f"List 1: {list11}")

#
list11.append(list22)
print(f"List 1: {list11}")

list22.sort()
print(list22)

#The lists can be sorted with the help of sort method
#Need to ensure if the leemts are the same datatype
listToSort = [10,40,20,60,2,9,100]
listToSort.sort()
print(listToSort)

#remove method will remove the element specified in the argument

print(list22)
list22.remove(60)
print(list22)

#clear method will remove all the element fro mthe list
print(list22)
list22.clear()
print(list22)