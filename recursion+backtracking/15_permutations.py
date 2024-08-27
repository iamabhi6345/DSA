"""   
    Given an array nums of distinct integers, return all the possible 
    permutations. You can return the answer in any order.

"""

class array:
    def __init__(self,arr1):
        self.arr1=arr1


    def __f(self,arr,ans,ind):
        if ind==len(arr):
            ans.append(arr.copy())
            return
        for i in range(ind,len(arr),1):
            arr[ind],arr[i]= arr[i],arr[ind]
            self.__f(arr,ans,ind+1)
            arr[ind],arr[i]= arr[i],arr[ind]
    
    def permutations(self):
        ans=list()
        self.__f(self.arr1,ans,0)
        return ans

a= array([1,2,3])
print(a.permutations()) 












class string:
    def __init__(self,str1):
        self.str1=str1
    def __f(self,arr,ans,ind):
        if ind==len(arr):
            s=""
            for i in arr:
                s=s+i
            ans.append(s)
        for i in range(ind,len(arr),1):
            arr[ind],arr[i]= arr[i],arr[ind]
            self.__f(arr,ans,ind+1)
            arr[ind],arr[i]= arr[i],arr[ind]
    
    def permutations(self):
        ans=list()
        nums=[]
        for i in self.str1:
            nums.append(i)
            
        self.__f(nums,ans,0)
        ans = set(tuple(ans))
        ans =list(ans)
        return ans

# a= array([1,2,3])
s= string("abhh")
print(s.permutations())