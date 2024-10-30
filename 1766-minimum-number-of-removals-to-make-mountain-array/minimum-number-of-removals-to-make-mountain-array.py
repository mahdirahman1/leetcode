class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # find longest increasing subsequnece for all indices LIS
        # find longest decreaseing subsequeunce for all indices starting from end
        # for each index, answer at index i = LIS ending at i + LDS from i 

        LIS = [1]
        LDS = [0 for _ in range(len(nums))]
        LDS[-1] = 1

        for i in range(1, len(nums)):
            max_prev = 0
            for j in range(i-1, -1,-1):
                if nums[j] < nums[i]:
                    max_prev = max(max_prev, LIS[j])
            LIS.append(1 + max_prev)
        
        for i in range(len(nums)-1, -1,-1):
            max_prev = 0
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    max_prev = max(max_prev, LDS[j])

            LDS[i] = 1 + max_prev
        
        ans = float('inf')
        # for each index, answer at index i = LIS ending at i + LDS from i, index should be from 1 to len(nums)-2
        # i.e not including first and last
        # we need to find how many to remve so ans is total nums - LIS[i] + LDS[i] - 1
        for i in range(1, len(nums)-1):
            if LIS[i] == 1 or LDS[i] == 1:
                continue
            ans = min(ans, len(nums) - LIS[i] - LDS[i] + 1)
        
        return ans
        
        