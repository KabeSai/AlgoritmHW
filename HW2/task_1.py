class Solution:

    def countSquares(self, matrix: list[list[int]]) -> int:
        """Сложность O(n*m).
        Args:
            matrix (List[List[int]]): matrix where we search squares.
        Returns:
            int: amount of squares in matrix.
        """
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] > 0:
                    matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j]) + 1
                    #проходами по матрице считаем возможные квадраты 
        return sum(list(map(sum, matrix)))


