"""
    
    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

        Example 1:

        Input: nums = [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        Explanation: After squaring, the array becomes [16,1,0,9,100].
        After sorting, it becomes [0,1,9,16,100].


    solve in O(n ) time using twi pointer
"""




def sort( nums: list[int]) -> list[int]:
        res= [0]*len(nums)
        l=0
        r= len(nums)-1

        for i in range(len(nums)-1 , -1 , -1):
            print(i)
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l]**2
                l = l+1
            else:
                res[i]= nums[r]**2
                r=r-1
            
        return res

def sort1(array):
        new_array = [0]*len(array)
        print(len(array))
        for i in range(len(array) - 1):
            print(i)
            new_array[i] = array[i] ** 2
        new_array.sort()
        return new_array

# print(sort1([-4,-1,0,3,10]))
print(reversed(range(5)))

