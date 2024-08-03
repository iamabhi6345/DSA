""" 
        Given an array of distinct integers candidates and a target integer target, 
        return a list of all unique combinations of candidates where the chosen 
        numbers sum to target. You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of 
        times. Two combinations are unique if the frequency
        of at least one of the chosen numbers is different. 
        
        
        
        
         ???????????????? self.a.append(dq.copy())  ????????????????? why
        The difference in behavior between self.a.append(dq.copy()) and 
        self.a.append(dq) is due to how lists (or deques) are handled in Python.

        When you append dq directly to self.a, you are appending a reference to 
        the same deque object. Any subsequent changes to dq will be reflected in
        self.a because they are pointing to the same object. This results in 
        self.a containing multiple references to the same, ultimately empty,
        deque after the recursion completes.
        
        
!!!!!!!!!!! tc = (2^n)*k     k due to putting result in diffrent data structureto store  

"""




from typing import List

class Solution:
    def __init__(self):
        self.a = []

    def ans(self, dq: List[int], i: int, arr: List[int],  tar: int):
        if tar==0:
            self.a.append(dq.copy())  
            return
        if i == len(arr) or tar<0:
            return
        
        
        dq.append(arr[i])
        self.ans(dq, i , arr,  tar-arr[i])
        # above index not increaded because a index can eb used multiple times
        dq.pop()  # Backtrack

        
        self.ans(dq, i + 1, arr, tar)
    
    def combinationSum(self, arr: List[int], k: int) -> List[List[int]]:
        self.a = []  # Reset the result list
        dq = []
        self.ans(dq, 0, arr, k)
        return self.a





# Example usage
s = Solution()
print(s.combinationSum([1, 2,1, 3], 7))  # Expected output: [[1, 2], [3]]



