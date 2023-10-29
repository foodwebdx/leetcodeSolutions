
def problema(nums):
    hashset = set()

    for i in range(len(nums)):
        if nums[i] not in hashset:
            hashset.add(nums[i])
        else:
            return True
                  
                    
            
print(problema([0,2,3,5,1,7]))