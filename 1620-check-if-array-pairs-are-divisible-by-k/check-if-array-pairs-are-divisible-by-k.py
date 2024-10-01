class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_map = defaultdict(int)
        for num in arr:
            remainder = num % k
            remainder_map[remainder] += 1
        
        for remainder in range(1, k):
            compliment = k - remainder
            if remainder_map[remainder] != remainder_map[compliment]:
                return False
        
        if 0 in remainder_map:
            if remainder_map[0] % 2 != 0:
                return False
        
        return True