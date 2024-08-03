def f(nums , l, h,target):
    if (l>h):
        return -1

    mid=(l+h)//2

    if nums[mid]==target:
            return mid
    
    elif nums[mid]<target:
            return f(nums,mid+1,h,target )
    else:
        return f(nums,l,mid-1,target)

def search(nums: [int], target: int):
    # write your code logic !!
    n=len(nums)
    low=0
    high=n-1
    return f(nums,low,high,target)

if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 12
    ind = search(a, target)
    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind)

