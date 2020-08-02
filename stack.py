'''
stack data structure
books-->A B C D
stack representation
D-->Top
C
B
A
stack contains push and pop operations
'''
class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items==[]
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items

s=Stack()
##print(s.is_empty())
##s.push('A')
##s.push('B')
##s.push('C')
##s.push('D')
##print(s.get_stack())
##print(s.peek())
