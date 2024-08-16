class Solution:
    
    def __dfs(self, image, sr, sc, vis, newColor):
        nr = len(image)
        nc = len(image[0])
        
        initial = image[sr][sc]
        
        stack = []
        stack.append((sr, sc))
        vis[sr][sc] = True
        image[sr][sc] = newColor
        
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        
        while stack:
            r, c = stack.pop()
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                
                if 0 <= nrow < nr and 0 <= ncol < nc and image[nrow][ncol] == initial and not vis[nrow][ncol]:
                    stack.append((nrow, ncol))
                    vis[nrow][ncol] = True
                    image[nrow][ncol] = newColor
        
        return
    
    def floodFill(self, image, sr, sc, newColor):
        nr = len(image)
        nc = len(image[0])
        
        vis = [[False] * nc for _ in range(nr)]
        
        self.__dfs(image, sr, sc, vis, newColor)
        
        return image
