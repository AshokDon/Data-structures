'''
use a stack to check whether or not a string has balanced
usage of parenthesis.
Example
  {},(){},(({[]}))-->Balanced
  {(},{{{)}},[][]]]-->Not Balanced
balanced example-->{[]}
not balanced example-->(()
not balanced example--> )}
'''
from stack import Stack
def is_match(p1,p2):
    if p1=="(" and p2==")":
        return True
    elif p1=="{" and p2=="}":
        return True
    elif p1=='[' and p2==']':
        return True
    else:
        return False
def Check_Peren(paren_string):
    s=Stack()
    is_balance=True
    index=0
    while index<len(paren_string) and is_balance:
        paren=paren_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balance=False
            else:
                top=s.pop()
                if not is_match(top,paren):
                    is_balance=False
        index+=1
    if s.is_empty() and is_balance:
        return True
    else:
        return False

print(Check_Peren('(((}}}'))
    
