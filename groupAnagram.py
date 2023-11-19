def groupsAnagrams(strs):
    res = []

    for words in range(len(strs)):
        pos = []
        cantLettersS = {}
        cantLettersT ={}
        flag = True
        s = strs[words]
        for i in s:
                if i not in cantLettersS:
                    cantLettersS[i]=1
                else:
                    cantLettersS[i]+=1
        
    
groupsAnagrams(["eat","tea","tan","ate","nat","bat"])