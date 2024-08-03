""" 
    Given a list arr of n integers, return sums of all subsets in it. Output sums can be printed in any order.

 

        Example 1:

        Input:
        n = 2
        arr[] = {2, 3}
        Output:
        0 2 3 5
        Explanation:
        When no elements is taken then Sum = 0.
        When only 2 is taken then Sum = 2.
        When only 3 is taken then Sum = 3.
        When element 2 and 3 are taken then 
        Sum = 2+3 = 5.
        
        [1,2,3,4]
            [10, 6, 7, 3, 8, 4, 5, 1, 9, 5, 6, 2, 7, 3, 4, 0]
"""


#User function Template for python3
class Solution:
    def f(self,arr,ind, sumi,l):
        if ind==len(arr):
            l.append(sumi)
            return
        
        # pick
        self.f(arr,ind+1,sumi+arr[ind],l)
        
        # not pick
        self.f(arr,ind+1,sumi,l)
        
    def subsetSums(self, arr, n):
	    # code here
	    l=list()
	    self.f(arr,0,0,l)
	    return l

s=Solution()
print(s.subsetSums([1,2,3,4] , 4))