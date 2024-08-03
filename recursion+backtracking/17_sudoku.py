
class Solution:
    
    def __is_valid(self,bd,row,col,c):
        for i in range(9):
            if (bd[i][col]==c):
                return False
            if (bd[row][i]==c):
                return False
            if (bd[3*(row//3) + i//3][3*(col//3) + i%3] ==c):
                return False
        return True


    def __solve(self,bd):
        for i in range(len(bd)):
            for j in range(len(bd)):
                if bd[i][j]==".":
                    for c in "123456789":
                        if (self.__is_valid(bd,i,j,c)):
                            bd[i][j]=c
                            if (self.__solve(bd)==True):
                                return True
                            else:
                                bd[i][j]="."
                    return False
        
        return True

    def solveSudoku(self, board: list[list[str]]) -> None:
        self.__solve(board)


def print1(bd):
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            print(int(bd[i][j]), end="   ")
        print()

sol=Solution()
board = [
        ["9", "5", "7", ".", "1", "3", ".", "8", "4"],
        ["4", "8", "3", ".", "5", "7", "1", ".", "6"],
        [".", "1", "2", ".", "4", "9", "5", "3", "7"],
        ["1", "7", ".", "3", ".", "4", "9", ".", "2"],
        ["5", ".", "4", "9", "7", ".", "3", "6", "."],
        ["3", ".", "9", "5", ".", "8", "7", ".", "1"],
        ["8", "4", "5", "7", "9", ".", "6", "1", "3"],
        [".", "9", "1", ".", "3", "6", ".", "7", "5"],
        ["7", ".", "6", "1", "8", "5", "4", ".", "9"],
    ]

sol.solveSudoku(board)
print1(board)