""" 
   same as previous one , only difference is 
   Each number in list may only be used once in the combination.
   
   
   no duplicate combination allowed
   [1,5,2] [1,2,5] -----> only one will be allowed
   
   

   ??????????????? why convert to tuple  ans.add(tuple(l.copy()))
   
   In Python, lists are mutable and cannot be added directly to sets because
   sets require their elements to be immutable and hashable. Tuples, on the other
   hand, are immutable and hashable, which makes them suitable for inclusion in 
   sets. By converting lists to tuples, you can take advantage of the set's
   properties to eliminate duplicates.
   
"""

# method -1 use set
class Solution:
    
    def f(self, arr,l, ind, tar, ans):
        if tar==0:
            ans.add(tuple(l.copy()))
            return
         
        if (ind>=len(arr))  or (tar<0):
            return
        
        l.append(arr[ind])
        self.f(arr,l,ind+1,tar-arr[ind],ans)
        l.pop()

        self.f(arr,l,ind+1,tar,ans)



    def combinationSum2(self, arr: List[int], tar: int) -> List[List[int]]:
        ans = set()
        tmp=list()
        arr.sort()
        self.f(arr,tmp, 0,tar,ans)
        a=list(ans)
        return a
        




"""  
  ?????????????? method2 optimised
  

    here concept  is first chooe a starting and that starting should not be 
    starting again 
    
    https://www.youtube.com/watch?v=G1fRTGRxXU8&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=11      

"""
from ty import List

class Solution1:
    
    def f(self,arr,q,ans,ind,tar):
        if (tar==0):
            ans.append(q.copy())
            return
        
        for i in range(ind, len(arr),1):
            if((i>ind) and (arr[i]==arr[i-1])):
                continue
            if(arr[i] > tar):
                break
            
            q.append(arr[i])
            self.f(arr,q,ans,i+1,tar-arr[i])
            q.pop()
            
    def combinationSum2(self, arr: List[int], tar: int) -> List[List[int]]:
        ans=list()
        q=list()
        arr.sort()
        self.f(arr,q,ans,0,tar)
        return ans



