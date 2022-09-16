# WHENEVER A SORTED MATRIX IS GIVEN WE USE BINARY SEARCH
# Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. 

# https://www.geeksforgeeks.org/find-median-row-wise-sorted-matrix/
# Time Complexity: O(32 * r * log(c)). The upper bound function will take log(c) time and is performed for each row
from bisect import bisect_right as upper_bound
 
MAX = 100;
#BINARY SEARCH METHOD
# Function to find median in the matrix
def binaryMedian(m, r, d):
    mi = m[0][0]
    mx = 0
    for i in range(r): 
        if m[i][0] < mi: #finding the min value of the matrix
            mi = m[i][0]
        if m[i][d-1] > mx : #finding the max value of matrix
            mx =  m[i][d-1]
     
    desired = (r * d + 1) // 2 #this gives the index of the median of matrix when converted to an array .
    while (mi < mx):
        mid = mi + (mx - mi) // 2 #mid=max//2 that is we are finding a value that is == median
        place=[0] #place will store all the no.of values less than or equal to mid 

        # Find count of elements smaller than or equal to mid
        for i in range(r):
            j = upper_bound(m[i], mid) #this helps us find the no. of elements less than or equal tomid in that row
            place[0] = place[0] + j
            if place[0] < desired: #if count< desired value
                mi = mid + 1 #if count is smaller than the desired values than it means we have more grerater values so the median must be greater than the selected value
            else:
                mx = mid #the median must be less than or equal to the  selected value
    print ("Median is", mi)
    return   
     
# Driver code
r, d = 3, 3
 
m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]]
binaryMedian(m, r, d)

     