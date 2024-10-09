class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = 0
        closing = 0
        for char in s:
            if char == "(":
                opening += 1
            else:
                if opening > 0:
                    opening -= 1
                else:
                    closing += 1
        
        return opening + closing
        
        