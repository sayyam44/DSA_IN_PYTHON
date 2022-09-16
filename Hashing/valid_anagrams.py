
def isAnagram(s,t):
    #using hashmaps
    if len(s)!=len(t):
        return False
    
    countS,countt={},{}
    for i in range(len(s)):
        #here we creating the hashmaps with keys as the character and the values as count of thier occurance
        #we using get method in order to define the default value ==0
        # +countS.get(s[i],0) this gives the previous value(no. of counts)
        countS[s[i]]=1+countS.get(s[i],0)#keys=chars,values=their no.of  times occurances
        countt[t[i]]=1+countt.get(t[i],0)#keys=chars,values=their no.of  times occurances
    for c in countS:
        if countS[c]!=countt.get(c,0): #here we are checking the value(frequency/count) for particular keys (c) in each 
            return False
    return True
#tc=s+t,sc=s+t
        
    
