import math
def time(v,m):
    ans=0
    for i in v:
        ans=ans+math.ceil(i/m)
    return ans


def minimumRateToEatBananas(v: [int], thresh: int) -> int:
    # # Write Your Code Here.
    ans=max(v)

    l=1
    h=ans

    while(l<=h):
        m=(l+h)//2
        if ((time(v,m)) <=  thresh):
            ans = m
            h = m - 1
        else:
            l = m + 1
    return ans
