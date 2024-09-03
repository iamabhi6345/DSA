from collections import defaultdict

V = 7
adj = defaultdict(list)
time = 0  # Global variable to keep track of discovery times

def DFS(u, disc, low, mystack, presentInStack):
    global time  # Use the global 'time' variable
    disc[u] = low[u] = time
    time += 1
    mystack.append(u)
    presentInStack[u] = True

    for v in adj[u]:
        if disc[v] == -1:  # If v is not visited
            DFS(v, disc, low, mystack, presentInStack)
            low[u] = min(low[u], low[v])
        elif presentInStack[v]:  # Back-edge case
            low[u] = min(low[u], disc[v])

    if low[u] == disc[u]:  # If u is head node of SCC
        print("SCC is:", end=" ")
        while mystack[-1] != u:
            print(mystack[-1], end=" ")
            presentInStack[mystack[-1]] = False
            mystack.pop()
        print(mystack[-1])
        presentInStack[mystack[-1]] = False
        mystack.pop()

def findSCCs_Tarjan():
    disc = [-1] * V
    low = [-1] * V
    presentInStack = [False] * V
    mystack = []

    for i in range(V):
        if disc[i] == -1:
            DFS(i, disc, low, mystack, presentInStack)

if __name__ == "__main__":
    adj[0].append(1)
    adj[1].append(2)
    adj[1].append(3)
    adj[3].append(4)
    adj[4].append(0)
    adj[4].append(5)
    adj[4].append(6)
    adj[5].append(6)
    adj[6].append(5)

    findSCCs_Tarjan()
