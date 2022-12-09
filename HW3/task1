from typing import List


class Solution:
    def numEnclaves(grid: List[List[int]]) -> int:
        """Cложность данной функции O(n)."""
        stack = {(0, 0)}
        #Расширам матрицу и добавим края
        for _ in range(len(grid)):
            stack.add((_, 0))
            stack.add((_, len(grid[i])-1))
        for _ in range(len(grid[0])):
            stack.add((len(grid)-1, _))
            stack.add((0, _))
        #Если это край зануляем его и проверяем соседей если они тоже единицы, то 
        # зануляем и их
        while stack:
            i, j = stack.pop()
            if grid[i][j] == 1: 
                grid[i][j] = 0 #когда находим край делаем его 0
                if len(grid) > i+1:
                    stack.add((i+1, j))
                if len(grid[i]) > j+1: #Если правый сосед 1 то она становится 0
                    stack.add((i, j+1))
                if 0 <= i-1:
                    stack.add((i-1, j))#Прошлое действие также для левого соседа
                if 0 <= j-1:
                    stack.add((i, j-1))
        summer = 0
        for i in grid:
            summer += sum(i)
        return summer