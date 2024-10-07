class Solution:
    def minLength(self, s: str) -> int:
        temp_stack = []
        for char in s:
            if char == 'B':
                # look for AB
                if temp_stack and temp_stack[-1] == 'A':
                    temp_stack.pop()
                    continue
            elif char == "D":
                # look for CD
                 if temp_stack and temp_stack[-1] == 'C':
                    temp_stack.pop()
                    continue
            temp_stack.append(char)
        
        return len(temp_stack)