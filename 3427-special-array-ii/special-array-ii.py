class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix_violations = [0]
        # stores number of violations ending at index i

        for i in range(1, len(nums)):
            if nums[i-1] % 2 == nums[i] % 2:
                prefix_violations.append(prefix_violations[-1] + 1)
            else:
                prefix_violations.append(prefix_violations[-1])
        
        res = []
        for start, end in queries:
            if prefix_violations[end] - prefix_violations[start] == 0:
                res.append(True)
            else:
                res.append(False)
        
        return res