class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i','o','u'])
        vowel_word = []
        for word in words:
            if word[-1] in vowels and word[0] in vowels:
                if vowel_word:
                    vowel_word.append(vowel_word[-1]+1)
                else:
                    vowel_word.append(1)
            else:
                if vowel_word:
                    vowel_word.append(vowel_word[-1])
                else:
                    vowel_word.append(0)
        
        res = []
        for start, end in queries:
            temp = vowel_word[end]
            if start-1 >= 0:
                temp -= vowel_word[start-1]
            res.append(temp)
        
        return res