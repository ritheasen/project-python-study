myTuple = (20,30,40,50,60,"test","test1")
myList = [50,45,78,92,59]


print("Tuple element :", myTuple)
print("Lenght of Tuple:" , len(myTuple) )
print(f"The index of 40: {myTuple.index(40)}")

print("Tuple elements: ", myTuple)

print(f"The total occurrences in the tuple are : {myTuple.count('test')}")
print("The maximum element in the tuple is : {max(myTuple)}")
print("The minimum element in the tuple is : {min(myTuple)}")
print(myTuple)

myTuple2 = tuple(myList)
myList2 = list(myTuple)

print(type(myTuple2))
print(type(myList2))