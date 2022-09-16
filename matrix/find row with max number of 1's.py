# https://www.youtube.com/watch?v=z092lX-nhik

#since the rows are sorted use binary search
#find the 1st row with 1's then iterate the next rows one by one and directly go to row which will have more 1's 
# in it than the previous row with 1's

# Step1: Get the index of first (or leftmost) 1 in the first row.
# Step2: Do following for every row after the first row 
# …IF the element on left of previous leftmost 1 is 0, ignore this row. 
# …ELSE Move left until a 0 is found. Update the leftmost index to this index and max_row_index to be the current row.
# The time complexity is O(m+n) because we can possibly go as far left as we came ahead in the first step.

def maxnum1(m):
    r=len(m)
    c=len(r[0])
    max_row_index=0 #index of the row with max 1's
    index=c-1 #as we have to check from back the number of 1's in each sorted array

    for i in range(r):
        flag=False #flag will be true if the current row have more 1's than previous row
        while (m[i][index]==1 and index>=0): #jab 2nd row k liye chalega toh index purane vale se shuru karega 
            flag=True
            index-=1 #now the no. of 1's will be calculated from the next index of the last 1 from previous row
            if (flag):
                max_row_index=i
        if max_row_index==0 and m[0][C-1]==0:
            return 0
    return max_row_index
 
# Driver Code
mat = [[0, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]]
print ("Index of row with maximum 1s is",
    rowWithMax1s(mat))


