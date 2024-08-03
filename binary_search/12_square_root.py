"""   

    if we know range of answers and have to find min , max 
    always use binary search
    
    in squarerrotwe know ranges , have to find maximum number on squaring will be less than number given (x)

"""

def floorSqrt(n):
       # write your code logic here .
   l=1
   h=n

   while(l<=h):
      m=(l+h)//2
      if(m*m <= n):
         l=m+1
      else:
         h=m-1
   
   return h

print(floorSqrt(6))