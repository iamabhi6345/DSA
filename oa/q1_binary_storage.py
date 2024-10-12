"""  

A scientist needs to store DNA information in a database. Each record will be a binary number, and all of the binary numbers will have the same number of bits set. These numbers can have many digits, but may have relatively few bits set.

To save space, they are stored using the following compression scheme:

• Instead of the storing a list of binary numbers, they are stored as a list of integers matching the indices of the set bits (1 bits)

• The bits are 0-indexed, starting from the right side (least significant bit).

• These indices are given in random order.

Given a list of numbers represented in this fashion, associate their indices with their values and sort them in descending order by value. Return a list or the indices in the order of the sorted array.

Example

bitArrays = [[0, 2], [2, 3], [2, 1]]
Return: [1, 2, 0]

The values sorted in descending order are [12, 6, 5]. The indices of those values are [1, 2, 0].  

"""

def f1(arr):
    n=len(arr)
    tmp=[]*n
    for i in range(n):
        arr[i].sort(reverse=True)
        tmp.append((arr[i],i))
    
    tmp.sort(reverse=True)
    ans=[]
    for i in tmp:
        ans.append(i[1])
    return ans


# arr = [[0, 2], [2, 3], [2, 1]]
arr = [[2,3], [4,2], [1,0],[5,6]]
print(f1(arr))
