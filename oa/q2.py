import sys
def maxWeightCell(N, Edge):
        wt = [0] * N
        sum_weight = 0
        res = 0
        
        for i in range(N):
            if Edge[i] != -1:
                wt[Edge[i]] += i
                if sum_weight <= wt[Edge[i]]:
                    sum_weight = wt[Edge[i]]
                    res = Edge[i]
        
        return res


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    
    Edge = list(map(int , sys.stdin.readline().strip().split(" ")))
    # Function Call
    ans = maxWeightCell(N, Edge)
    print(ans)