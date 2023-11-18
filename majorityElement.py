def majorityElemnt(nums):
    Elements = {}
    for i in range(len(nums)):
        if nums[i] not in Elements:
            Elements[nums[i]]=1
        else:
            Elements[nums[i]]+=1
    for key, value in Elements.items():
        if value > len(nums) // 2:
            return key

print(majorityElemnt([3,3,4]))