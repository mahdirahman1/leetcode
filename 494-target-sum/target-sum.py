class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dfs(index, sum_):
            if index == len(nums):
                if sum_ == target:
                    return 1
                else:
                    return 0
            
            total = 0
            # try - next num
            total += dfs(index+1, sum_ - nums[index])

            # try + next num
            total += dfs(index+1, sum_ + nums[index])
            
            return total

        return dfs(0, 0)