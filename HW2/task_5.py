class Solution:

    def getDescentPeriods(self, prices: list[int]) -> int:
        """Сложность O(n).

        Args:
            prices: the daily price history of a stock.
        Returns:
            int: the number of smooth descent periods.
        """     
        #
        dp = [1]*len(prices)
        smooth = 1
        #
        for i in range(1, len(prices)):
            if prices[i-1]-prices[i] == 1:
                dp[i] = dp[i-1]+1
                print(dp)
            smooth += dp[i]

        return smooth