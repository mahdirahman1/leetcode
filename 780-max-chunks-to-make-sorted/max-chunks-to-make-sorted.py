class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        sorted [0,1,2,3,4]
        original [1,0,2,3,4]
        
        keep a set for each, when sets match, we can make a split
        e.g 
        s1 = (0,1) and s2 = (1,0) we can split here
        then
        s1 = (2) and s2 = (2) we can split 
        so we wanna be greedy when trying to split 

        sorted   [0,1,2,3,4]
        original [4,3,2,1,0]
        s1 and s2 will only match at the end
        """
        s1 = set()
        s2 = set()
        sorted_arr = sorted(arr)
        res = 0
        for i in range(len(arr)):
            s1.add(sorted_arr[i])
            s2.add(arr[i])
            if s1 == s2:
                res += 1
                s1 = set()
                s2 = set()
        
        return res