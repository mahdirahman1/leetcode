class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = defaultdict(int)
        def dfs(index, left, cache):
            if (index, left) in cache:
                return cache[(index, left)]

            if index == len(nums):
                if left == 0:
                    return 1
                else:
                    return 0
            
            total = 0
            # try - next num
            total += dfs(index+1, left - nums[index], cache)
            # try + next num
            total += dfs(index+1, left + nums[index], cache)

            cache[(index, left)] = total
            
            return cache[(index, left)]

        return dfs(0, target, cache)