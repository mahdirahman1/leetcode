class Solution:
    def compressedString(self, word: str) -> str:
        count = 0
        prev_char = word[0]

        res = []
        for char in word:
            if char != prev_char or count == 9:
                res.append(str(count))
                res.append(prev_char)
                prev_char = char
                count = 0

            count += 1
            

        res.append(str(count))
        res.append(prev_char)
        return "".join(res)
                
        