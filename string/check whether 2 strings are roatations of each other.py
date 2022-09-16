# https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)


def check(s1,s2):
    if len(s1)!=len(s2):
        return False
    
    q1=[]
    for i in s1:
        q1.insert(0,i)
    
    q2=[]
    for i in s2:
        q2.insert(0,i)
    
    k=len(q2)
    while k>0:
        a=q2[0]
        q2.pop(0)
        q2.append(a)
        if q2==q1:
            return True
        k-=1
    return False
    
