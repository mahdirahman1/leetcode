class Solution:
    def maxScore(self, s: str) -> int:
        """
        count 1s in one pass - total ones
        do a pass and count curr 1s, sum = (index - curr ones + 1) + (total ones - curr ones)
        """
        max_score = 0
        total_ones = 0
        for char in s:
            total_ones += int(char)
        
        curr_ones = 0
        for i in range(len(s)-1):
            curr_ones += int(s[i])
            max_score = max(max_score, (i - curr_ones + 1) + (total_ones - curr_ones))
        
        return max_score