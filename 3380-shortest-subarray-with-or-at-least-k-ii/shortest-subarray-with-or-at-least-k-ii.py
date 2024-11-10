class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        curr_or = 0
        ans = float("inf")
        bits = [0] * 32 # count of how many numbers have each bit set

        for r in range(len(nums)):
            num_add = nums[r]
            b = 0
            while num_add > 0:
                bits[b] += num_add % 2
                num_add >>= 1
                b += 1

            curr_or = 0
            for i in range(32):
                if bits[i]:
                    curr_or += (1 << i)

            while l <= r and curr_or >= k:
                ans = min(ans, r-l+1)

                num_remove = nums[l]
                b = 0
                while num_remove > 0:
                    bits[b] -= num_remove % 2
                    num_remove >>= 1
                    b += 1

                curr_or = 0
                for i in range(32):
                    if bits[i]:
                        curr_or += (1 << i)

                l += 1
                    
        return -1 if ans == float('inf') else ans            
                