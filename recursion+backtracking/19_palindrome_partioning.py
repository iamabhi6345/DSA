"""
    Given a string s, partition s such that every substring of the partition is 
    a palindrome
    
    . Return all possible palindrome partitioning of s.


        Example 1:
                Input: s = "aab"
                Output: [["a","a","b"],["aa","b"]]
        
        Example 2:
                Input: s = "a"
                Output: [["a"]]
 
    
"""


class Solution:
    def __f(self,ans,l,ind,s):
        if(ind==len(s)):
            ans.append(l.copy())
            return
        
        for i in range(ind,len(s),1):
            if (self.__is_palindrome(s[ind:i+1])):
                l.append(s[ind:i+1])
                self.__f(ans,l,i+1,s)
                l.pop()

    def __is_palindrome(self,s):
        i=0
        j=len(s)-1
        while(i<=j):
            if(s[i]!=s[j]):
                return False
            i+=1;j-=1
        return True          

    def partition(self, s: str) -> list[list[str]]:
        ans=[]
        l=[]
        self.__f(ans,l,0,s)
        return ans

sol = Solution()
print(sol.partition("abahiab"))