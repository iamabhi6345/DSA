import sys

def largestSumCycle( N, Edge):
        # Initialize the visited array to keep track of visited nodes
        v = [-1] * N

        def visit(i: int, s: int) -> int:
            if Edge[i] < 0:
                return -1
            if v[i] >= 0:
                # Return the sum of the cycle
                return s + i - v[i]

            v[i] = s + i
            result = visit(Edge[i], s + i)

            Edge[i] = -1
            return result

        return max(visit(i, 0) for i in range(N))

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    
    Edge = list(map(int , sys.stdin.readline().strip().split(" ")))

    ans = largestSumCycle(N, Edge)
    print(ans)