class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        1 2 5 7 9

        [0,1,4,4,5,7]
        for each num i, do binary search on its right elements
        largest x + nums[i] < target (upper) - would find index of largest x
        largest x  + nums[i] < target (lower) - would find index just before largest x
        pairs = difference of lower and upper index (window size)
        """
        def binary_search(l,r, target):
            while l <= r:
                mid = (l+r)//2

                if nums[mid] >= target:
                    r = mid-1
                else:
                    l = mid + 1
                
            return r

        pairs = 0
        nums.sort()
        for i in range(len(nums)):
            lower_index = binary_search(i+1, len(nums)-1, lower - nums[i])
            upper_index = binary_search(i+1, len(nums)-1, upper - nums[i] + 1)
            pairs += upper_index - lower_index

        return pairs