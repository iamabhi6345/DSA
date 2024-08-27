'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def length(head) :
    #Your code goes here
    ans =0
    while(head!=None):
        ans+=1
        head=head.next
    return ans
