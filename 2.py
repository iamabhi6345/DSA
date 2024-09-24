class Node:
    def __init__(self, val):
        self.val = val
        self.uid = None
        self.parent = None
        self.children = []
        self.isLocked = False
        self.isDescendantLocked = 0
        
class Tree:
    def __init__(self, n, m, node_lst, queries):
        self.node_map = {node: Node(node) for node in node_lst}
        self.root = self.node_map[node_lst[0]]
        self.construct_tree(n, m, node_lst)
        self.processed_queries = [query.split() for query in queries]
    
    def construct_tree(self, n, m, node_lst):
        for i in range(n):
            node = self.node_map[node_lst[i]]
            start = i * m + 1
            end = min(start + m, n)
            node.children = [self.node_map[node_lst[j]] for j in range(start, end)]
            if i > 0:
                node.parent = self.node_map[node_lst[(i - 1) // m]]
    
    def lock(self, node, uid):
        if node.isDescendantLocked > 0 or node.isLocked or self.isAncestorLocked(node.parent):
            return False
        node.uid = uid
        node.isLocked = True
        self.updateAncestorLocks(node, 1)
        return True
        
    def unlock(self, node, uid):
        if uid != node.uid or not node.isLocked:
            return False
        node.isLocked = False
        node.uid = None
        self.updateAncestorLocks(node, -1)
        return True
        
    def upgrade(self, node, uid):
        if node.isDescendantLocked == 0 or self.isAncestorLocked(node.parent):
            return False
        self.unlockChildren(node, uid)
        return self.lock(node, uid)
        
    def isAncestorLocked(self, node):
        while node:
            if node.isLocked:
                return True
            node = node.parent
        return False

    def unlockChildren(self, node, uid):
        stack = [node]
        while stack:
            current = stack.pop()
            if current.isLocked and current.uid == uid:
                self.unlock(current, uid)
            stack.extend(current.children)
        
    def updateAncestorLocks(self, node, delta):
        while node:
            node.isDescendantLocked += delta
            node = node.parent
        
    def __str__(self):
        return self.__print_tree(self.root, "")

    def __print_tree(self, node, out):
        out += f"{node.val} No of Descendants Locked: {node.isDescendantLocked}, is Node Locked: {node.isLocked}\n"
        for child in node.children:
            out = self.__print_tree(child, out)
        return out

n = 7
m = 2
nodes = ["World", "Asia", "Africa", "China", "India", "SouthAfrica", "Egypt"]
queries = ["1 China 9", "1 India 9", "3 Asia 9", "2 India 9", "2 Asia 9"]
obj = Tree(n, m, nodes, queries)

res = []
for query in obj.processed_queries:
    if query[0] == "1":
        res.append(obj.lock(obj.node_map[query[1]], int(query[2])))
    elif query[0] == "2":
        res.append(obj.unlock(obj.node_map[query[1]], int(query[2])))
    elif query[0] == "3":
        res.append(obj.upgrade(obj.node_map[query[1]], int(query[2])))

print(res)
