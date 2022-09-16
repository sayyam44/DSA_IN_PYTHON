#^^^^^^^^^^^^^^COPY ^^^^^^^^^^^^
#https://www.youtube.com/watch?v=jDZQKzEtbYQ&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=75
# https://www.geeksforgeeks.org/implement-a-stack-using-single-queue/
class MyStack:

    def __init__(self):
        self.q=[]

    def push(self, x: int) -> None:
        self.q.append(x)
        size=len(self.q)
        for i in range(size): #initially i is pointing o top of the queue.
            x=self.q.pop() #poping the top value of queue
            self.q.append(x) #and appending the popped value above the last pushed value

    def pop(self) -> int:
        if len(self.q)==0:
            return -1
        x=self.q.pop()
        return x
        
    def top(self) -> int:
        if len(self.q)==0:
            return -1
        return self.q[-1]
        

    def empty(self) -> bool:
        return len(self.q)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()