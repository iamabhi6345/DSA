import bisect
def search(nums: [int], target: int):
    # write your code logic !!
    pi=bisect.bisect_left(nums,target)
    if (pi!=len(nums)) and (nums[pi]==target):
        return pi
    return -1


if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 12
    ind = search(a, target)
    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind)

