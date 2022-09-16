# https://practice.geeksforgeeks.org/problems/minimize-the-heights-i/1/#
# https://www.youtube.com/watch?v=Av7vSnPSCtw

        # arr.sort()
        # s=arr[0]+k smallest value in the starting 
        # l=arr[n-1]-k largest value in the starting 
        # min_val=arr[n-1]-arr[0] for initial case
        # mi,ma=0,0
        # for i in range(1,n)
        #     mi=min(s,arr[i+1]-k) mi is the minimum of current smallest and the current's next-k 
        #     ma=max(l,arr[i]+k) ma is the max of current largest and current value+k
        #     if mi<0: min value may also be negative
        #         continue
        #     min_val=min(min_val,ma-mi)
        # return min_val
        # code here
    arr.sort()
    ans = arr[n - 1] - arr[0]  # Maximum possible height difference
 
    tempmin = arr[0]
    tempmax = arr[n - 1]
 
    for i in range(1, n): #i is on the 2nd tower , as weare comparing 1st 2 towers
        tempmin = min(arr[0] + k, arr[i] - k) #here we are not doing arr[i+1]-k because we have started loop from 1 not from 0
         #in upper case min means current-k i.e. arr[i]-k
        # Minimum element when we
        # add k to whole array
        # Maximum element when we
        tempmax = max( arr[n - 1] - k, arr[i - 1] + k)
         #in upper case max means current's prev+k i.e. arr[i-1]+kk
        # subtract k from whole array
        ans = min(ans, tempmax - tempmin)
 
    return ans