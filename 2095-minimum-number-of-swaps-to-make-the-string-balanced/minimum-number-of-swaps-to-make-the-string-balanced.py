class Solution:
    def minSwaps(self, s: str) -> int:
        closing = 0
        opening = 0
        swaps = 0

        for char in s:
            if char == "[":
                opening += 1
            if char == "]":
                closing += 1
            
            if closing > opening:
                swaps += 1
                opening += 1
                closing -= 1
        
        return swaps
