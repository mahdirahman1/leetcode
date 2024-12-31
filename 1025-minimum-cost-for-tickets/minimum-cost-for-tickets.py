class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        """
        Let dp[i] be the total cost of tickets at travel day i

        If the day is not a travel day, set the DP value equal to the DP value of the previous day.
        If the day is a travel day, set the DP value to the minimum cost of:
            buying a 1-day pass and adding its cost to the DP value of the previous day.
            buying a 7-day pass and adding its cost to the DP value of the day 7 days before.
            buying a 30-day pass and adding its cost to the DP value of the day 30 days before.
        """
        dp = [0] * (max(days)+1)
        travel_days = set(days)

        for i in range(1, len(dp)):
            if i in travel_days:
                dp[i] = min(dp[i- 1] + costs[0],
                               dp[max(0, i - 7)] + costs[1],
                               dp[max(0, i - 30)] + costs[2])
            else:
                dp[i] = dp[i-1]
        
        return dp[max(days)]