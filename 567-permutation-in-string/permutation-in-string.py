class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create a dict of freq of chars in s1
        # go through s2, if char is in s2, check if next continous char makes up s1
        # sliding window with window size of len(s1)
        s1_freq = Counter(s1)
        test = defaultdict(int)
        current_freq = Counter(s2[:len(s1)-1])
        left = 0

        for right in range(len(s1)-1, len(s2)): 
            current_freq[s2[right]] += 1

            if current_freq == s1_freq:
                return True

            current_freq[s2[left]] -= 1
            if current_freq[s2[left]] == 0:
                del current_freq[s2[left]]
            left += 1

        return False

            
            
