#tc=n*m
# https://leetcode.com/problems/rotting-oranges/
# https://www.youtube.com/watch?v=y704fEOx0s0
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs will be used as there may occur more than 1 rotten oranges in begining and we would need to do the process on both the oranges simueltaneously
        rows,cols=len(grid),len(grid[0])
        q=deque()
        time,fresh=0,0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1 #calculating the total fresh orangesin begining
                if grid[r][c]==2:
                    q.append([r,c]) #adding all the rotten oranges in the begining 
       
        directions=[[1,0],[-1,0],[0,1],[0,-1]] #in order to make all the oranges around a rotten orange to be rotten
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if (row<0 or col<0 or 
                        row==len(grid) or col==len(grid[0]) or
                        grid[row][col]!=1): #all the conditions which are out of range or already rotten 
                        continue
                    grid[row][col]=2 #here a fresh orange is becoming rotten
                    q.append([row,col])
                    fresh-=1
            time+=1
        return time if fresh==0 else -1 #we will only return time when all the fresh oranges has been rotten



























