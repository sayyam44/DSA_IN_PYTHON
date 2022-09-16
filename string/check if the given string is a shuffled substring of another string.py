# https://www.geeksforgeeks.org/check-if-the-given-string-is-shuffled-substring-of-another-string/
# Input: str1 = “onetwofour”, str2 = “hellofourtwooneworld” 
# Output: YES 

# Approach: 
# Let n = length of str1, m = length of str2. 

# If n > m, then string str1 can never be the substring of str2.
# Else sort the string str1.
# Traverse string str2 
# Put all the characters of str2 of length n in another string str.
# Sort the string str and Compare str and str1.
# If str = str1, then string str1 is a shuffled substring of string str2.
# else repeat the above process till ith index of str2 such that (i +n – 1 > m)(as after 
# this index the length of remaining string str2 will be less than str1.
# If str is not equals to str1 in above steps, then string str1 can never be substring of str2.

def check(A,B):
    n=len(A)
    m=len(B)

    if n>m:
        return False
    
    A=sorted(A)
    for i in range(m):
        if (n+i-1)>m:
            return False
        str=""
        for j in range(n):
            str+=(B[i+j])
        str=sorted(str)
        if str==A:
            return True
        return False


def check(A,B):
    n=len(A)
    m=len(B)

    if n>m:
        return False
    A=sorted(A)
    for i in range(m):
        if (n+i-1)>m:
            return False
        str=''
        for j in range(n):
            str.add(B[i+j])
        str=sorted(str)
        if A==str:
            return True
        return False
