class node:
    def __init__(self, val , next=None):
        self.val = val
        self.next = next

def printl(head):
    while(head!=None):
        print(head.val,end="  --> ")
        head=head.next
    print()

def create( arr):
        head = node(arr[0])
        n= len(arr)
        tmp = head
        for i in range(1,n):
            t = node(arr[i])
            tmp.next=t
            tmp = tmp.next
        return head
    
def insert_at_begin(head , val):
    new = node(val)
    t=head
    new.next = head
    return new



head = create([2,3,4,5])
printl(head)
head = insert_at_begin(head,1)
printl(head)

            