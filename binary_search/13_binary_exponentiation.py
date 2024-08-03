"""  
   ??????? find x^n 
    
    if n is even : (x^n)= (x^2)^(n/2) = (x*x)^(n/2)
    if n is odd : (x^n) = [x*  ((x)^(n-1))]
"""


def pown(x,n):
    p=n
    if n<0:
        p=-1*n
    ans=1
    while(p>0):
        if(p%2==1):
            ans=ans*x
            p=p-1
        else:
            x=x*x
            p=p//2
    
    if (n<0):
        res= 1/ans
        return res 

    return ans
    
print(pown(2,-20))