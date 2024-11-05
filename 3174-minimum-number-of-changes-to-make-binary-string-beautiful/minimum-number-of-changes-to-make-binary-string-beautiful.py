class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        ones = 0
        for i in range(len(s)):
            if s[i] == "1":
                ones += 1
            if i % 2 == 1:
                # reach size 2, find num changes
                changes += min(2-ones, ones)
                ones = 0

            
        return changes