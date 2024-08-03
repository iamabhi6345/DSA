from collections import deque

def printf(dq , arr , ind):
    if ind == len(arr):
        print([q for q in dq])
        # print([q for q in dq], "  sum ====      ",sum([q for q in dq]))
        return
    
    # take
    dq.append(arr[ind])
    printf(dq,arr,ind+1)
    dq.pop()
    
    # not take
    printf(dq,arr,ind+1)


def sol(l):
    dq = deque()
    printf(dq,l,0)
    
# sol([1,2,3,4])


# =============================================================================================
""" 
    print subsequence whose sum is k
    
    method -1 bruteforce create all subsequences and print only those whose sum =k
    
"""

def printfk(dq , l,ind,k):
    if (ind== len(l)):
        if (sum([q for q in dq])==k):
            print([q for q in dq])
        return
    
    dq.append(l[ind])
    printfk(dq,l,ind+1 ,k)
    dq.pop()
    
    printfk(dq,l,ind+1,k)
    
def solve(l,k):
    dq = deque()
    printfk(dq, l , 0,k)

# solve([1,2,3,4,5,0],5)

# ------------------------------------------------------------------------------------------------
# above tc incraese by O(n) due to summation


def printfk2(dq , l,ind,k,sum1):
    if (ind== len(l)):
        if (sum1==k):
            print([q for q in dq])
        return
    
    dq.append(l[ind])
    sum1= sum1+ l[ind]
    printfk2(dq,l,ind+1 ,k,sum1)
    dq.pop()
    
    sum1=sum1- l[ind]
    printfk2(dq,l,ind+1,k,sum1)
    
def solve2(l,k):
    dq = deque()
    printfk2(dq, l , 0,k,0)

solve2([1,2,3,4,5,0,-2,-3],5)

# ------------------------------------------------------------------------
# return true if there is required subsequense



# if its not said to print a subsequence remove dq
def printfk3(dq , l,ind,k,sum1) -> bool:
    if (ind== len(l)):
        if (sum1==k):
            print([q for q in dq])
            return True
        return False
    
    dq.append(l[ind])
    sum1= sum1+ l[ind]
    if  printfk3(dq,l,ind+1 ,k,sum1) == True:
        return True
    dq.pop()
    
    sum1=sum1- l[ind]
    if printfk3(dq,l,ind+1,k,sum1)==True:
       return  True  
    
    return False
    
def solve3(l,k) -> bool:
    dq = deque()
    return printfk3(dq, l , 0,k,0)

# print(solve3([1,2,3,4,5,0],5))





# --------------------------------------------------------
""" 

    count total sunsequence whose sum is k 
"""




def count( l,ind,k,sum1) -> int:
    if (ind== len(l)):
        if (sum1==k):
            return 1
        return 0
    

    sum1= sum1+ l[ind]
    left= count(l,ind+1 ,k,sum1) 

    
    sum1=sum1- l[ind]
    right= count(l,ind+1,k,sum1)
  
    
    return (left+right)
    
def solve4(l,k) -> int:
    return count( l , 0,k,0)

# print(solve4([1,2,3,4,5,0,-2,-3],5))
