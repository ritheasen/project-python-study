def selectionSort(nums):
    for i in range(0,len(nums)):
        min = i
        for j in range(i+1,len(nums)):
            if nums[j] > nums[min]:
                min = j
        nums[i],nums[min] = nums[min],nums[i]
        print(nums)
    print(nums)

selectionSort([12,50,25,65,6,78])