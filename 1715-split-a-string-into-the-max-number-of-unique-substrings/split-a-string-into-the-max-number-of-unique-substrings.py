class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # back tracking
        seen = set()
        
        def dfs(i, seen):
            if i == len(s):
                return 0
            
            res = 0
            for j in range(i, len(s)):
                if s[i:j+1] in seen:
                    continue

                seen.add(s[i:j+1])
                res = max(res, 1 + dfs(j+1, seen))
                seen.remove(s[i:j+1])
        
            return res
        
        return dfs(0, seen)