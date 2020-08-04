'''
satck problem
converting integer number into binary
Example-->242
242//2-->121-->0
121//2-->60--->1
60//2--->30--->0
30//2--->15--->0
15//2--->07--->1
7//2---->03--->1
3//2---->01--->1
1//2---->00--->1
'''
class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self):
        return self.items
    def is_empty(self):
        if self.items==[]:
            return True
    def Top(self):
        return self.items[-1]
s=Stack()
def Get_Binary(integer_num):
    while integer_num:
        r=integer_num%2
        integer_num=integer_num//2
        s.push(r)
    #print(s.get_stack())
    while not s.is_empty():
        x=s.pop()
        print(x,end="")
Get_Binary(242)
