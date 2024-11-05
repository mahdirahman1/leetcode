class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        ones = 0
        for i in range(len(s)):
            ones += int(s[i])
            if i % 2 == 1:
                # reach size 2, find num changes
                changes += min(2-ones, ones)
                ones = 0

            
        return changes