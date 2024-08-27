n= 5

arr=[1,2,3,4,5]

for i in range(1<<n):
    subset=[]
    for j in range(n):
        if i &(1<<j):
            subset.append(arr[j])
    print(subset)


