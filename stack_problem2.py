'''
Given a list of daily temperatures T, return a list such that,
for each day in the input, tells you how many days you would have to wait
until a warmer temperature. If there is no future day for which this is possible,
put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].

'''
class Stack():
    def __init__(self):
        self.temps=[]
    def push(self,temp):
        self.temps.append(temp)
    def pop(self):
        self.temps.pop()
    def get_stack(self):
        return self.temps
    def len(self):
        c=0
        for i in self.temps:
            c+=1
        return c
    def peek(self):
        return self.temps[-2]
    def get_iteam(self,x):
        return self.temps[x]
    def index(self):
        return self.temps[-1]
s=Stack()
def DailyTemperature(arr):
    s=Stack()
    n=len(arr)
    z=[0]*n                   #0   1  2  3   
    for i in range(n-1,-1,-1):#73 74 75 71 69 72 76 73
        #print(s.get_stack())
        while s.get_stack()and arr[i]>=arr[s.index()]:#71>=69
            s.pop()#4
            print(s.get_stack(),'pop')
        s.push(i)#6 5 3
        print(s.get_stack())
        if s.len()==1:#
            z[i]=0#0 0
        else:
            #print(s.peek())
            z[i]=s.peek()-i#1 1
    print(z)
    


arr=[73, 74, 75, 71, 69, 72, 76, 73]
DailyTemperature(arr)
