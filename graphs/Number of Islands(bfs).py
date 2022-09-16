# https://www.youtube.com/watch?v=pV2kpPD66nE
# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #we will need to count all the islands that is all the ones interconnected with each other which
        #have 1s diagnolly and horizontally to that one and rest all are zerores around it it will be 
        #counted as one island , for another island should not be connected with the 1st island in any way 
        if not grid:
            return 0
        
        visit=set() # because we just want to add some row,col only once into this set
        isisland=0

        def bfs(r,c):
            q=collections.deque()
            q.append((r,c)) #appending the 1st "1" that we got in some island
            visit.add((r,c))
            while q:
                row,col=q.popleft()  #now we need to check all the lements around row,col must be 1 and should not be visited so that we append that row,col in visit
                directions=[[1,0],[-1,0],[0,1],[0,-1]] #right,left,up,down
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit):
                        #if this r,c that is if some "1" that is a part of island but still not visited 
                        # then we append this into q and visit set so that this whole process can be again
                        # done for this element
                        q.append((r,c))
                        visit.add((r,c))

        
        rows,cols=len(grid),len(grid[0])
        for i in rows:
            for j in cols:
                if grid[i][j]=="1" and (i,j) not in visit:
                    bfs(i,j)
                    isisland+=1 #is island will only increase when one complete island is completed 
                    #as in the above bfs function we are following the loop till we complete one island
        return isisland





def number_of_islands(grid):
    isilands=0
    visit=set()

    if not grid:
            return 0

    def bfs(r,c):
        q=collections.deque()
        q.append((r,c))
        visit.add((r,c))
        
        while q:
            row,col=q.popleft()
            directions=[[0,1],[0,-1],[1,0],[-1,0]]
            for r,c in directions:
                dr,dc=row+r,col+c
                if (r in range(rows) and c in range(cols) and (r,c) not in visit and grid[i][j]=='1' ):
                    visit.add((r,c))
                    q.append((r,c))

    rows,cols=len(grid),len(grid[0])
    for i in rows:
        for j in cols:
            if grid[i][j]=='1' and (i,j) not in visit:
                bfs(i,j)
                isislands+=1
    return isislands
