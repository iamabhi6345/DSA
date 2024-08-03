import bisect
def getFloorAndCeil(a, n, x):
    # Write your code here.
    floor=-1
    ceil=-1
    # check if floor is present
    # for floor there should be atleast one number less than x


    # for floor absent
    f=bisect.bisect_left(a,x)
    if (f==0) and (a[f]!=x):
        floor=-1
    # for floor present
    else:
        if(f==len(a)):
            floor=a[f-1]
        else:
            if (a[f]==x):
                floor= a[f]
            else:
                floor=a[f-1]



    c=bisect.bisect_right(a,x)
    
    # for ceil absent
    if (c==len(a)) and (a[len(a) -1]!=x):
        ceil=-1
    elif (c==len(a)) and (a[len(a)-1]==x):
        ceil = x
    else:
        if (f==0):
            ceil=a[f]
        else:
            if(a[f-1]==x):
                ceil=a[f-1]
            else:
                ceil=a[f]



    return floor,ceil