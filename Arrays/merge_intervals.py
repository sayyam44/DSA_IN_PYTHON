# https://leetcode.com/problems/merge-intervals/
def merge(I):
    # Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    # Output: [[1,6],[8,10],[15,18]]
    # Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
            
        #optimized -tc=nlogn(for sorting)+n(for iterating)=nlogn,,sc=1
        I.sort() #sorting is always done on the basis of the 1st element of each list.
        lst=[I[0]] #[1,3]
        
        #in the given example -- if 3>2 then update 3 by max(3,6)
        for i in I:
            # for 1st iteration --- lst[-1][1]=3,i[0]=1,i[1]=3
            if lst[-1][1]>=i[0]:
                lst[-1][1]=max(lst[-1][1],i[1])
            else:
                lst.append(i) #if not then directly adding that to the list
        return lst

    
        #brute force approach 1, tc=n2,sc=n , without sorting
        lst=[]
        lst1=[]
        for i in range(len(inter)):
            for j in range(i+1,len(inter)-1):
                if inter[i][1]>=inter[j][0]:
                    lst.append(inter[i][0])
                    lst.append(inter[j][1])
                    lst1.append(lst)

            lst1.append(inter[i])
        return lst1
                    
        #brute force approach 2, tc=nlogn+n2 ,sc=1
        #sort the given arr , and then chech whether the ith list mergers with (i+1)th list , if yes give the one combined list for both,i++
        
        #  intervals = [[1,3],[2,6],[8,10],[15,18]]




