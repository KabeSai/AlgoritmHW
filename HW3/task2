from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        "Сложность данной функции log(n)"
        if not grid: return 0  
        self.row = len(grid)  
        self.col = len(grid[0])  
          
        def is_edge(row, col):#Проверяет край ли это
            return r == 0 or r == self.row - 1 or c == 0 or c == self.col - 1  
        
        def is_Valid(grid, r, c):#Проверяет все вершины на наличее краёв 
            grid[r][c] = 1  
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]  
            edge = is_edge(r, c)  
            for i, j in dirs:  
                x, y = r + i, c + j  
                if 0 <= x < self.row and 0 <= y < self.col and grid[x][y] == 0:  
                    if not is_Valid(grid, x, y): edge = True     
            return not edge  
                  
        count = 0  
        for r in range(self.row):  
            for c in range(self.col):  
                if grid[r][c] == 0 and is_Valid(grid, r, c):  
                    count += 1  
        return count 