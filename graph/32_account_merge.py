"""   
Given a list of accounts of size n where each element accounts [ i ] is a list of strings, where the first
element account [ i ][ 0 ]  is a name, and the rest of the elements are emails representing emails of the
account.
Geek wants you to merge these accounts. Two accounts belong to the same person if there is some common email
to both accounts. Note that even if two accounts have the same name, they may belong to different people as
people could have the same name. A person can have any number of accounts initially, but all of their accounts 
have the same name.
After merging the accounts, return the accounts in the following format: The first element of each account
is the name, and the rest of the elements are emails in sorted order.

Note: Accounts themselves can be returned in any order.

Example 1:

Input:
n = 4
accounts [ ] =
[["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]
Output:
[["John","john00@mail.com","john_newyork@mail.com", "johnsmith@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com". The third John and Mary are different people as none of their email addresses are used by other accounts.We could return these arrays in any order, for example, the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input:
n = 5
accounts [ ] =
[["Gabe","Gabe00@m.co","Gabe3@m.co","Gabe1@m.co"],
["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output:
[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
Explanation:
We don't have any common emails in any of the users. We just sorted the emails of each person and we return a array of emails.(The details can be returned in any order).
Your Task:
You don't need to read or print anything. Your task is to complete the function accountsMerge() which takes a list of lists of strings representing accounts[][] as a parameter and returns a list of lists of strings denoting the details after merging.

Expected Time Complexity: O(n*m*logn) - where n is the size of accounts and m is the size of the number of strings for a name.
Expected Auxiliary Space: O(n*m) - where n is the size of accounts and m is the size of the number of strings for a name.

Constraints:
1 <= n <= 1000
2 <= accounts[ i ].size <= 10
1 <= accounts[ i ][ j ].size <= 30
accounts[i][0] consists of English letters.



"""


"""

class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


class Solution:
    def accountsMerge(self, details):
        n = len(details)
        ds = DisjointSet(n)
        mapMailNode = {}

        for i in range(n):
            for j in range(1, len(details[i])):
                mail = details[i][j]
                if mail not in mapMailNode:
                    mapMailNode[mail] = i
                else:
                    ds.unionBySize(i, mapMailNode[mail])

        mergedMail = [[] for _ in range(n)]
        for mail, node in mapMailNode.items():
            root = ds.findUPar(node)
            mergedMail[root].append(mail)
        # print("###########\n",n,"\n",mergedMail,"\n#################")

        ans = []
        for i in range(n):
            if not mergedMail[i]:
                continue
            mergedMail[i].sort()
            temp = [details[i][0]] + mergedMail[i]
            ans.append(temp)

        ans.sort()
        return ans


if __name__ == "__main__":
    accounts = [
        ["John", "j1@com", "j2@com", "j3@com"],
        ["John", "j4@com"],
        ["Raj", "r1@com", "r2@com"],
        ["John", "j1@com", "j5@com"],
        ["Raj", "r2@com", "r3@com"],
        ["Mary", "m1@com"]
    ]

    obj = Solution()
    ans = obj.accountsMerge(accounts)
    for acc in ans:
        print(f"{acc[0]}: {' '.join(acc[1:])}")

"""












# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class DisjointSet:
    def __init__(self , n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0]*(n+1)
        self.size = [1]*(n+1)
    
    def findUPar(self , node):
        if self.parent[node]==node:
            return node 
        self.parent[node]=self.findUPar(self.parent[node])
        return self.parent[node]
    
    def union_by_rank(self, u , v):
        upu = self.findUPar(u)
        upv= self.findUPar(v)
        
        if upu == upv:
            return 
        
        if self.rank[upu]<self.rank[upv]:
            self.parent[upu]=upv
        elif self.rank[upv]<self.rank[upu]:
            self.parent[upv]=upu 
        else:
            self.parent[upu]=upv
            self.rank[upv]+=1
    
    def union_by_size(self , u , v):
        upu = self.findUPar(u)
        upv=  self.findUPar(v)
        
        if upu == upv:
            return 
        
        if self.size[upu]<self.size[upv]:
            self.parent[upu]=upv
            self.size[upv]+=self.size[upu]
        else:
            self.parent[upv]=upu
            self.size[upu]+=self.size[upv]
        
class Solution:
    def accountsMerge(self, accounts):
        # Code here
        n = len(accounts)
        ds = DisjointSet(n)
        mapmail2node=dict()
        
        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail=accounts[i][j]
                if mail in mapmail2node:
                    ds.union_by_rank(i,mapmail2node[mail])
                else:
                    mapmail2node[mail]=i
        
        
        mergedmail = [[] for _ in range(n)]
        for mail , node in mapmail2node.items():
            upnode = ds.findUPar(node)
            mergedmail[upnode].append(mail)
        
        ans=[]
        for i in range(n):
            if not mergedmail[i]:
                continue
            mergedmail[i].sort()
            tmp = [accounts[i][0]] + mergedmail[i]
            ans.append(tmp)
        ans.sort()
        return ans
            

if __name__ == "__main__":
    accounts = [
        ["John", "j1@com", "j2@com", "j3@com"],
        ["John", "j4@com"],
        ["Raj", "r1@com", "r2@com"],
        ["John", "j1@com", "j5@com"],
        ["Raj", "r2@com", "r3@com"],
        ["Mary", "m1@com"]
    ]

    obj = Solution()
    ans = obj.accountsMerge(accounts)
    for acc in ans:
        print(f"{acc[0]}: {' '.join(acc[1:])}")
