class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:   
        """Сложность O((n+1)*(m+1))

        Args:
            obstacleGrid: grid which we should research.
        Returns:
            int: he number of possible unique paths that the robot can take to reach the bottom-right corner.
        """     
        #создаём дупликат obstacleGrid с нулевыми значениями
        dp=[[0] * (len(obstacleGrid[0])+1) for m in range(len(obstacleGrid)+1)]  
        dp[0][1]=1 #место с которого робот начнёт ходить равно 1
                        
        for row in range(1, len(obstacleGrid)+1):
            for col in range(1, len(obstacleGrid[0])+1):
                if not obstacleGrid[row-1][col-1]: # Если путь свободен складываем сумму верхней и левой ячейки дупликата
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]

