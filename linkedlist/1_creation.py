class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def constructLL(arr: [int]) -> Node:
    # Write your code here
    head = Node(arr[0])
    n = len(arr)
    if n==1:
        return head
    tmp=head
    for i in range(1, n):
        t = Node(arr[i])
        tmp.next= t
        tmp =t
    return head

def printl(head):
    head.val=10000
    while(head!=None):
        print(head.val,end="  --> ")
        head=head.next

t =constructLL([1,2,3,67,89])
printl(t.copy())
print()
print(t.val)