
#count duplicates
def count_duplicates(str):
    val={}
    for i in str:
        if i in val:
            val[i]+=1
            
        else:
            val[i]=1
    for k,v in val:
        if v >1:
            print(k,'-->',v)
        else:
            continue