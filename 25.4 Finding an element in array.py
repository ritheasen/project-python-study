#def findingElementInArray(arr, sno):
#    for i in range(0,len(arr)):
#        if arr[i] == sno:
 #           return f"Element fout at index {i}"
  #      return "Element not found in the array..."

def findingElementInArray(arr, sno):
    for num in arr:
        if num == sno:
            return f"Element found at index {arr.index(num)}"

        return "Element no found in the array..."

result = findingElementInArray([51,45,78,32,98], 98)
print(result)



