
def bubsort(nums):
    for i in range (0,len(nums)-1):
        for j in range(0,len(nums)-(i+1)):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

numsList = [80,9,78,96,69,86,100]

print("Before sorting")
print(numsList)

bubsort(numsList)

print("After sorting")
print(numsList)






