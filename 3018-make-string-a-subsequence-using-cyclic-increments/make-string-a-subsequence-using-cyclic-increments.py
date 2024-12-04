class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        two pointers, go through each char in str2
        for each char in str2, keep checking str1
        if str1[c] == str2[c] or str1[c] == str2[c]-1
            move to next char of str2

        """
        if len(str2) > len(str1):
            return False
       
        s1 = 0
        s2 = 0
        while s1 < len(str1):
            if str1[s1] == str2[s2] or (ord(str1[s1]) - ord('a') + 1) % 26 == (ord(str2[s2])-ord('a')) % 26:
                s2 += 1

            if s2 == len(str2):
                return True

            s1 += 1

        return False