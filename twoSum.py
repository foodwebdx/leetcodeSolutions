def twoSums(nums,target):
        numMap = {}
        n = len(nums)
        for i in range(n):
            numMap[nums[i]] = i
        print(numMap)
        for i in range(n):
            numPos = target - nums[i]
            print(i)
            if numPos in numMap and numMap[numPos] != i:
                return [i, numMap[numPos]]

        return [] 

print(twoSums([1,1,1,1,1,1,1,1,2,3,424,23,4,100,10,100],200))