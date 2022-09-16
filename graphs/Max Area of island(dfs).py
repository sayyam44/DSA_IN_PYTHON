#https://www.youtube.com/watch?v=iJGr1OtmH0c
# https://leetcode.com/problems/max-area-of-island/
#tc,sc=m*n
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        
        def dfs(r,c):
            if (r<0 or r==rows or c<0 or c==cols or grid[r][c]==0 or
               (r,c) in visit): #firstly remove all the not cases
                return 0
            visit.add((r,c))
            return (1+ dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)) #checking for area of an island in all directions 
                
        area=0
        for i in range(rows):
            for j in range(cols):
                area=max(area,dfs(i,j))
        return area
                



