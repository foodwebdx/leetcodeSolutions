def validAnagram(s,t):
    cantLettersS = {}
    cantLettersT ={}
    flag = True
    if len(s) == len(t):
        for i in s:
            if i not in cantLettersS:
                cantLettersS[i]=1
            else:
                cantLettersS[i]+=1
        for j in t:
            if j not in cantLettersT:
                cantLettersT[j]=1
            else:
                cantLettersT[j]+=1
        for k in cantLettersS:
            if k not in cantLettersT:
                flag = False
                break
            else:
                if cantLettersS.get(k)!=cantLettersT.get(k):
                    flag = False
                    break
                else:
                    flag = True
    else:
        flag=False
    return flag
        
print(validAnagram("anagtam","nbgbram"))
