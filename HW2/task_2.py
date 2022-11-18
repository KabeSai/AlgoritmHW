class Solution:
    
    def getMaximumGenerated(self, n: int) -> int:
        """Сложность O(n+1)

        Args:
            n (int): list's length.
        Returns:
            int: max element in this list.
        """        
        if not n: #nums[0] = 0
            return n
        nums = [0]*(n+1) #generate n+1
        nums[1] = 1
        for i in range(2, n+1):
            if i % 2:
                nums[i] = nums[i//2]+nums[i//2+1]
            else:
                nums[i] = nums[i//2]
        return max(nums)
