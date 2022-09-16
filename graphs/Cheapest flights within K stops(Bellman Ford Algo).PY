#^^^^^^^^^^^^COPY^^^^^^^^^^^^
#BELLMAN FORD ALGORITHM 
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# https://www.youtube.com/watch?v=5eIK3zUdYmE
#BELLMAN FORD ALGORITHM 
#tc=E*K
#Bellman ford algo 
#BFScan work with negative weights also

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float("inf")]*n
        prices[src]=0
        
        for i in range(k+1): #k means number of stops so 1rtlydo for k=0 that is no stop then do for k+1=1 that is 1 stop at max
            tmpprices=prices.copy()
            
            for s,d,p in flights: #here it is doing bfs s#s=source,d=destination,p=price 
                if prices[s]==float("inf"):
                    continue
                if prices[s]+p<tmpprices[d]: #we are comparing it with tmpprices because we update the price in tmpprices 1st and then copy it into the prices array
                    tmpprices[d]=prices[s]+p #same comment as above
            prices=tmpprices#updatig the prices == tmpprices
        return -1 if prices[dst]==float("inf") else prices[dst]
                    