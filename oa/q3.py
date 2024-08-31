from collections import deque

def shortPath(adj, c1, n):
    dist = [float('inf')] * n
    q = deque([c1])
    dist[c1] = 0

    while q:
        u = q.popleft()

        for v in adj[u]:
            if dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1
                q.append(v)
    
    return dist

def main():
    n = int(input())

    edges = list(map(int, input().split()))

    c1, c2 = map(int, input().split())

    adj = [[] for _ in range(n)]
    for i in range(n):
        if edges[i] == -1:
            continue
        adj[i].append(edges[i])

    v1 = shortPath(adj, c1, n)
    v2 = shortPath(adj, c2, n)

    mn = float('inf')
    node = -1
    for i in range(n):
        if v1[i] == float('inf') or v2[i] == float('inf'):
            continue
        if v1[i] + v2[i] < mn:
            mn = v1[i] + v2[i]
            node = i

    print(node)

if __name__ == "__main__":
    main()
