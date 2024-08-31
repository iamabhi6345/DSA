"""   

    if we know range of answers and have to find min , max 
    always use binary search
    
    in squarerrotwe know ranges , have to find maximum number on squaring will be less than number given (x)

"""

def floorSqrt(n):
       # write your code logic here .
   l=1
   h=n

   while(h-l>0.1):
      m=(l+h)/2
      if(m*m <= n):
         l=m
      else:
         h=m
   
   return h

print(int(floorSqrt(16)))