class Solution:
    def minimumSteps(self, s: str) -> int:
        # find index of first 0 from right, this is starting point of swaps
        # find 1s from right, swaps needed = (index of 0) - index of 1, update index of by -1 for next position
        last0 = len(s)-1
        while last0 >= 0 and s[last0] == "1":
            last0 -= 1

        if last0 < 0:
            return 0

        swaps = 0
        for i in range(last0-1, -1, -1):
            if s[i] == "1":
                swaps += last0 - i
                last0 -= 1
        
        return swaps