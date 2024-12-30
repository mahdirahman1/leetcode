class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # dp 
        """
        let dp[i] be the number of ways to make string of length i
        if zero = 1
        and one = 1
        for a given string of length i
        dp[i] = dp[i-1] (number of ways of string length i concat the 0)
        dp[i] += dp[i-1] (number of ways of string length i add the 1)
        
        """
        dp = [0] * (high+1) # since we only need from low to high
        dp[0] = 1 # number of ways of empty string is 1

        for i in range(1, len(dp)):
            # for zeros
            if (i-zero) >= 0:
                dp[i] += dp[i-zero]

            if (i-one) >= 0:
                dp[i] += dp[i-one]
        
        return sum(dp[low:high+1]) % (10**9+7)