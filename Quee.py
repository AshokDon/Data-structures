'''
Que data structure
books-->A B C D
Que representation
A B C D
FIFO-->first in first out
LILO-->last in last out
stack contains push and pop operations
'''
class Que():
    def __init__(self):
        self.items=[]
    def EnQue(self,item):
        self.items.append(item)
    def DeQue(self):
        self.items.pop(0)
    def get_Que(self):
        return self.items
    def is_empty(self):
        if self.items==[]:
            return 'Que is empty'
Q=Que()
Q.EnQue('A')
Q.EnQue('B')
Q.EnQue('C')
Q.EnQue('D')
Q.EnQue('E')
print(Q.get_Que())
Q.DeQue()
print(Q.get_Que())
        
