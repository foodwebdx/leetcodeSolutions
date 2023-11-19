def removeElement(nums,val):
    lP = 0
    for i in range(len(nums)):
        if nums[i]!= val:
            nums[lP]=nums[i]
            lP +=1
    return lP
print(removeElement([3,2,2,3],3))