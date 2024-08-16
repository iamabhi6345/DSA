"""   

Problem statement
You are given a sorted array ‘arr’ of length ‘n’, which contains positive integer positions of ‘n’ gas stations on the X-axis.



You are also given an integer ‘k’.



You have to place 'k' new gas stations on the X-axis.



You can place them anywhere on the non-negative side of the X-axis, even on non-integer positions.



Let 'dist' be the maximum value of the distance between adjacent gas stations after adding 'k' new gas stations.

Find the minimum value of dist.


Example:
Input: ‘n' = 7 , ‘k’=6, ‘arr’ = {1,2,3,4,5,6,7}.

Answer: 0.5

Explanation:
We can place 6 gas stations at 1.5, 2.5, 3.5, 4.5, 5.5, 6.5. 

Thus the value of 'dist' will be 0.5. It can be shown that we can't get a lower value of 'dist' by placing 6 gas stations.


Note:
You will only see 1 or 0 in the output where:
  1 represents your answer is correct.
  0 represents your answer is wrong. 
Answers within 10^-6 of the actual answer will be accepted.
Detailed explanation ( Input/output format, Notes, Images )



Sample Input 1:
5 4
1 2 3 4 5


Expected Answer:
0.5


Output Printed On Console:
1


Explanation of sample output 1:
k = 4, arr = {1,2,3,4,5} 

One of the possible ways to place 4 gas stations is {1,1.5,2,2.5,3,3.5,4,4.5,5}

Thus the maximum difference between adjacent gas stations is 0.5. 

Hence, the value of ‘dist’ is 0.5. It can be shown that there is no possible way to add 4 gas stations in such a way that the value of ‘dist’ is lower than this. (Note: 1 will be printed in the output for the correct answer). 


Sample Input 2:
10 1
1 2 3 4 5 6 7 8 9 10


Expected Answer:
1


Output Printed On Console:
1


Explanation of sample output 2:
k = 1, arr = {1,2,3,4,5,6,7,8,9,10} 

One of the possible ways to place 1 gas station is {1,1.5,2,3,4,5,6,7,8,9,10} 

Thus the maximum difference between adjacent gas stations is still 1. 

Hence, the value of ‘dist’ is 1. It can be shown that there is no possible way to add 1 gas station in such a way that the value of ‘dist’ is lower than this. (Note: 1 will be printed in the output for the correct answer). 


Expected Time Complexity
Try solving this in O(n*log(A)), where A is the maximum value in array 'arr'.


Constraints:
2 <= n <= 10^5
1 <= k <= 10^6 
1 <= arr[i] <= 10^9

Time Limit: 1 sec


"""


# iterative approach   



def minimiseMaxDistance(arr: [int], k: int) -> float:
    # Write your code here.
    n=len(arr)
    how_many=[0]*(n-1)

    for _ in range(k):
        maxval=-1
        index=-1
        for j in range(n-1):
            diff=(arr[j+1]-arr[j])
            dist = diff/(how_many[j] + 1)
            if(dist > maxval):
                maxval=dist
                index=j
        how_many[index]+=1

    maxval=-1
    for j in range(n-1):
        diff=(arr[j+1]-arr[j])
        dist = diff/(how_many[j] + 1)
        maxval=max(maxval, dist)
    return round(maxval,6)


"""   
    above finding maximum is taking O(n)
    we can reduce by using priority queue that will take O(log n)
    in python its heapq 
    
"""



import heapq
def minimiseMaxDistance(arr: [int], k: int) -> float:
    # Write your code here.
    n=len(arr)
    l=[]
    for i in range(n-1):
        diff = arr[i+1]-arr[i]
        heapq.heappush(l,(-diff,i))
    
    how_many = [0]*(n-1)

    for _ in range(k):
        maxval , index = heapq.heappop(l)
        how_many[index]+=1
        dist = (arr[index+1]-arr[index])/(how_many[index]+1)
        heapq.heappush(l,(-dist,index))

    return (heapq.heappop(l)[0])*-1

"""  
    heapq stores min on top
    so used negative of it because we are working on maximum values
    
    also negative the final output value to get original value
    
    TC = O(n log n) + O(k log n)
    
    SC = O(N-1)
    
    now job is to minimize the space complexity





        ?????????below binary search method
 
    here we will have fixed search space of answer will eliminate some part 
"""



def total_station_for_given_distance(arr,dist):
    count=0
    for i in range(len(arr)-1):
        station_in_between= (arr[i+1]-arr[i])//(dist)
        if ((station_in_between*dist) == (arr[i+1]-arr[i])):
            station_in_between-=1
        count+=station_in_between

    return count

def minimiseMaxDistance(arr: [int], k: int) -> float:
    l=0
    h=0
    for i in range(len(arr)-1):
        h= max(h, arr[i+1]-arr[i])
    
    while(h-l>1e-6):
        mid=(l+h)/2
        if (total_station_for_given_distance(arr,mid) > k):
            l=mid
        else:
            h=mid
    return h    


