class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        dict = c.most_common(k)
        ans=[]
        for i in dict:
            ans.append(i[0])
        return ans
    
