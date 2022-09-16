#   https://leetcode.com/problems/set-matrix-zeroes/
  #sc=1,tc=m*n
  #https://www.geeksforgeeks.org/a-boolean-matrix-question/
     
class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flag=False
        col_flag=False
        
        r=len(m)
        c=len(m[0])
        
        for i in range(r):
            for j in range(c):
                if i==0 and m[i][j]==0:
                    row_flag=True
                if j==0 and m[i][j]==0:
                    col_flag=True
                if m[i][j]==0:
                    m[0][j]=0
                    m[i][0]=0
                
        for i in range(1,r):
            for j in range(1,c):
                if m[0][j]==0 or m[i][0]==0:
                    m[i][j]=0
        if row_flag:
            for j in range(c):
                m[0][j]=0
        
        if col_flag:
            for i in range(r):
                m[i][0]=0
        return m
        