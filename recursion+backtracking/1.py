class a:
    def __init__(self,s):
        print(id(s))
        self.s = s
        self.s.add(78)
        print(self.s)
        print(id(self.s))
        
s={90,89}
print(id(s))
a(s)
print(s)