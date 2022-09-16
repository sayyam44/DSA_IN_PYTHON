#https://www.youtube.com/watch?v=lJwbPZGo05A
#GREEDY APPROACH (TC=N)

# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3

#sum of gas must be >= sum of cost else return -1

#eg if gas=[1,1,1],cost=[1,1,1] this is not possible becuase with total of 3 cost and total of 3 gas we can
#start from any point in gas station which will not be possible as we only need one unique solution 
#eg if gas=[3,0,0],cost=[1,1,1] we have total gas>=total cost and we have only one unique solution that is 
#starting from gas[0] position

# gas = [1,2,3,4,5], cost = [3,4,5,1,2] , diff=[-2,-2,-2,3,3] that is why we can only start from 3 circularly as 3+3-(-2-2-2)=0

#in above example we know that sum gas>=sum of cost then we know that solution is possible
#so traverse through diff and lets assume total=0 initially 
#now assume index 0 of diff as starting point but since it makes total -2 that is negative thats why 
#we need to make total as 0 again and start from index 0 till we reach some +ve value of total
#at index 3 we have total=3 then again at index 4 we have total=6 ans also since we knew earlier that the
#solution is possible and also at the end total is +ve so the 1st index which made total as positive i.e = 3
#will be the starting index of the circular gas station trip i.e. 3td index of gas therefore o/p = 3

def gas_station(gas,cost):
    if sum(gas)<sum(cost):
        return -1
    total=0 
    res=0
    for i in range(len(gas)):
        total+=gas[i]-cost[i]
        if total<0:
            total=0
            res=i+1
    return res

#end code


