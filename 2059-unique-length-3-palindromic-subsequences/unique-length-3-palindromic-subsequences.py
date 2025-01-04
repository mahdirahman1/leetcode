class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        find first and last index of a char
        go through all chars in map, if it has two indexes (at least two appearances)
        calculate 3 subsequence palindrome as last_index - first_index - 1
        """
        index_map = defaultdict(list)

        for i, char in enumerate(s):
            if len(index_map[char]) < 2:
                index_map[char].append(i)
            else:
                index_map[char][-1] = i
        
        res = 0

        for indices in index_map.values():
            if len(indices) == 2:
                res += len(set(s[indices[0]+1:indices[1]]))
        
        return res