# 2 method  


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2list(self , l1 , l2):
        hd = ListNode(-1)
        t1=hd
        while(l1 and l2):
            if l1.val <=l2.val:
                hd.next = l1
                hd=hd.next
                l1=l1.next
            else:
                hd.next=l2
                l2=l2.next
                hd=hd.next
        if l1:
            hd.next=l1
        elif l2:
            hd.next = l2

        return t1.next
        

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None

        # below values of -1e8 is taken because there may be null lists and with negative values as well 
        # biggest negative number will help from both problem
        head = ListNode(-1e8)

        t1=head
        for i in range(0,len(lists)):
            if not lists[i]:
                continue
            head = self.merge2list(head , lists[i])
        return t1.next



# ???????method 2 heap   

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        pq = []
        for head in lists:
            if head is not None:
                heapq.heappush(pq,(head.val , id(head) , head))
        
        head = ListNode(-1)
        tail = head
        while(pq):
            _ , _ , node = heapq.heappop(pq)
            tail.next = node
            tail = tail.next 
            if node.next is not None:
                heapq.heappush(pq , (node.next.val , id(node.next),node.next)) 
        return head.next
        