def selectionSort(nums):
    for i in range(len(nums)-1,-1,-1):
        max = i
        for j in range(0,i):
            if nums[j] > nums[max]:
                max = j
        nums[i],nums[max] = nums[max],nums[i]
        print(nums)
    #print(nums)

selectionSort([12,50,25,65,6,78])