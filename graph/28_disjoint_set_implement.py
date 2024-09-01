class DisjointSet:
    def __init__(self,n):
        self.rank=[0]*(n+1)
        self.parent=[i for i in range(n+1)]
        self.size = [1]*(n+1)
    
    # finding ultimate parent and also done path compression
    def findUPar(self , node):
        if self.parent[node]==node:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def union_by_rank(self , node1 , node2):
        up1 = self.findUPar(node1)
        up2 = self.findUPar(node2)
        
        if up1==up2:
            return 
        
        if self.rank[up1]<self.rank[up2]:
            self.parent[up1]=up2
        elif self.rank[up2]<self.rank[up1]:
            self.parent[up2]=up1
        else:
            self.parent[up1]=up2
            self.rank[up2]+=1
    
    def union_by_size(self , node1 , node2):
        up1 = self.findUPar(node1)
        up2 = self.findUPar(node2)
        
        if up1==up2:
            return 
        
        if self.size[up1] < self.size[up2]:
            self.parent[up1] = up2
            self.size[up2]+=self.size[up1]
        
        else:
            self.parent[up2]=up1
            self.size[up1]+=self.size[up2]

if __name__ == "__main__":
    ds = DisjointSet(7)
    
    ds.union_by_rank(1, 2)
    ds.union_by_rank(2, 3)
    ds.union_by_rank(4, 5)
    ds.union_by_rank(6, 7)
    ds.union_by_rank(5, 6)
    # ds.union_by_size(1, 2)
    # ds.union_by_size(2, 3)
    # ds.union_by_size(4, 5)
    # ds.union_by_size(6, 7)
    # ds.union_by_size(5, 6)
    
    # Check if 3 and 7 are in the same component
    if ds.findUPar(3) == ds.findUPar(7):
        print("Same")
    else:
        print("Not same")
    
    ds.union_by_rank(3, 7)
    # ds.union_by_size(3, 7)
    
    # Check again if 3 and 7 are in the same component
    if ds.findUPar(3) == ds.findUPar(7):
        print("Same")
    else:
        print("Not same")
