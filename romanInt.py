def romanInt(s):
    nums = {"I":1, "V":5, "X":10, "L":50, "C":100,"D":500,"M":1000}
    result = 0
    flag = True
    for i in range(len(s)):
        if i +1 < len(s) and nums[s[i]] < nums[s[i+1]]:
            result -= nums[s[i]]
        else:
            result += nums[s[i]]
    return result
print(romanInt("LV"))