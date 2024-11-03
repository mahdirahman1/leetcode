class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # go through each char in s, if it is equal to goal[0] do a comparison
        # str[i:] + str[:i] == goal? true

        for i, char in enumerate(s):
            if char == goal[0]:
                if s[i:] + s[:i] == goal:
                    return True
        
        return False