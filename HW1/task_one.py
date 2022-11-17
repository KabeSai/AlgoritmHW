#Number of Steps to Reduce a Number to Zero
class Solution:
    def numberOfSteps(self, num: int) -> int:
        """Сложность O(n).
    
        Args:
            num (int): starting number.
        Returns:
            int: number of steps.
        """
        count = 0 #Счётчик шагов
        while num > 0:
            if num % 2 == 0:
                num = num // 2
                count += 1
                continue
            num -= 1
            count += 1
        return count

