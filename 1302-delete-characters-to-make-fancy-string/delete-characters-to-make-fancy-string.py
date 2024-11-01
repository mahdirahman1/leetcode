class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and len(stack) > 1 and stack[-1] == stack[-2] == char:
                continue
            stack.append(char)
        
        return "".join(stack)