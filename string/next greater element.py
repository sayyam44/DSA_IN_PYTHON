# https://www.geeksforgeeks.org/find-next-greater-number-set-digits/
# https://leetcode.com/problems/next-greater-element-iii/

# Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller than the previously traversed digit. For example, if the input number is “534976”, we stop at 4 because 4 is smaller than next digit 9. If we do not find such a digit, then output is “Not Possible”.
# Now search the right side of above found digit ‘d’ for the smallest digit greater than ‘d’. For “534976″, the right side of 4 contains “976”. The smallest digit greater than 4 is 6.
# Swap the above found two digits, we get 536974 in above example.
# Now sort all digits from position next to ‘d’ to the end of number. The number that we get after sorting is the output. For above example, we sort digits in bold 536974. We get “536479” which is the next greater number for input 534976.

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n=str(n)
        for i in range(len(n)-1,0,-1):

            if i==1 and n[i-1]>=n[i]: #descending order ,4321, i is at 3
                return -1
            
            if n[i-1]<n[i]:#finding the value from behind that is smaller than the last traversed value
                break
            #now swapping this value with the just larger value than itself on its right side
            # Find the smallest digit on the right side of
            # (i-1)'th digit that is greater than number[i-1]
            x=n[i-1]
            smallest=i
            for j in range(i+1,len(n)):
                if n[j]>x and n[j]<n[smallest]: #it should not only greater than x but also smaller than all the values to its right
                    smallest=j
            # Swapping the above found smallest digit with (i-1)'th
            n[smallest],n[i-1]=n[i-1],n[smallest]
            
            x = 0
            # Converting list upto i-1 into number
            for j in range(i):
                x = x * 10 + n[j]
            
            n=sorted(n[i:])
            for j in range(len(n)-i):
                x=x*10+n[j]
            
            return x 
            
            
                
            
            