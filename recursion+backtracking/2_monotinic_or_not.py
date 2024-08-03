def isMonotonic( n: list[int]) -> bool:
        if len(n)==0 or len(n)==1:
            return True

        pre = n[0]

        def is_mon_inc(n):
            nonlocal pre
            for i in range(1,len(n),1):
                cur=n[i]
                if cur < pre:
                    return False
                pre= cur
            return True
        
        def is_mon_dec(n):
            nonlocal pre
            for i in range(1,len(n),1):
                cur = n[i]
                if cur > pre:
                    return False
                pre=cur
            return True
        
        if n[0] > n[-1]:
            return is_mon_dec(n)
        return is_mon_inc(n)

print(isMonotonic([1,2,7,2,3]))
print(isMonotonic([1]))
print(isMonotonic([]))