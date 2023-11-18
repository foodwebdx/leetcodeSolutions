def removeDuplicates(nums):
    lP = 1
    for i in range(1,len(nums)):
        if nums[i]!= nums[i-1]:
            nums[lP] = nums[i]
            lP += 1
    return lP

print(removeDuplicates([1,1,2]))