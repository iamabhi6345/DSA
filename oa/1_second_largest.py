"""
Given an array arr, return the second largest distinct element from an array. If the second largest element doesn't exist then return -1.

Examples:

Input: arr = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr = [10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist so answer is -1.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arri ≤ 105 
"""

#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        f=-1e8
        s=-1e8
        for i in arr:
            if i> f:
                s=f
                f=i
                
            elif i >s and i!=f:
                s=i
        return max(s , -1)
