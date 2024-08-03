
class Solution:
    
    
    def step(self ,n, src, help, dest):
        if n==1:
            print(f"move disk {n} from rod {src} to rod {dest}")
            return
        
        self.step(n-1,src, dest, help)
        print(f"move disk {n} from rod {src} to rod {dest}")
        self.step(n-1, help,src,dest)
        
        
    def toh(self, n, fromm, to, aux):
        # Your code here
        self.step(n,fromm,aux,to)
        return ((2**n)   -1)
        
        
obj = Solution()
print(obj.toh(5,1,3,2))