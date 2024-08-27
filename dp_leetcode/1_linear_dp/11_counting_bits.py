""" 
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

"""

class Solution:
    def count(self , n):
        count=0
        while(n):
            n=n&(n-1)
            count+=1
        return count

    def countBits(self, n: int) -> List[int]:
        ans=[]
        ans.append(0)
        for i in range(1,n+1):
            ans.append(self.count(i))
        return ans

