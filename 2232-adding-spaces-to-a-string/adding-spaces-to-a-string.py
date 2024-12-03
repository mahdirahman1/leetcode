class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        space_index = 0
        for i, char in enumerate(s):
            if space_index < len(spaces) and i == spaces[space_index]:
                res.append(" ")
                space_index += 1
            res.append(char)
        
        return "".join(res)