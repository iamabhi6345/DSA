def c2(s:str , i) -> bool:
    if(i>=len(s)//2):
        return True
    if s[i] != s[len(s)-i-1]:
        return False
    return c2(s,i+1)        

def check(s: str) -> bool:
    return c2(s,0) 

print(check("madaam"))
    