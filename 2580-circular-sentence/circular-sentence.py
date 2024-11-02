class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i, char in enumerate(sentence):
            if char == " ":
                if sentence[i-1] != sentence[i+1]:
                    return False
        
        return sentence[0] == sentence[-1]
        