'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''

def reverseDLL(head):
    # Write your code here
    if head==None or head.next ==None:
        return head
    
    prev = None
    curr = head 

    while(curr!=None):
        prev = curr.prev
        curr.prev = curr.next
        curr.next = prev

        curr = curr.prev
    
    return prev.prev
     