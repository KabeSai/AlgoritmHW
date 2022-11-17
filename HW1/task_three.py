class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """Сложность данной программы O(n).
    
        Args:
            jewels(str): jewels representing the types of stones that are jewels.
            stones(str): the stones you have.
        Returns:
            int: how many of the stones you have are also jewels.
        """
        count = 0
        for char in stones:
            if char in jewels:
                count += 1
        return count