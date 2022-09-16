#^^^^^^^^^COPY^^^^^^^^^^^^^^^(1st logic,less optimized method)
# https://www.youtube.com/watch?v=3Et9MrMc02A&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=76
# https://www.geeksforgeeks.org/queue-using-stacks/
class queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def enqueue(self,x):
        
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(x)

        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
    #tc for enqueue=n,sc=2n


    def dequeue(self):
        if len(self.s1) == 0: 
            return -1
        else:
            x=self.s1[-1]
            self.s1.pop()
            return (x)

if __name__ == '__main__':
    q = Queue()
    q.enQueue(1) 
    q.enQueue(2) 
    q.enQueue(3) 
  
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())



