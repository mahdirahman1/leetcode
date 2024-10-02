class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # sort the numbers, assign a rank to each and store in dict
        # go through array and replace num with rank
        # nlogn = 10^5 log 10^5 = 5 * 10^5 log 10^5 < 10^6
        sorted_arr = sorted(arr)
        rank_map = defaultdict(int)
        rank = 0
        for i in range(len(sorted_arr)):
            if i > 0 and sorted_arr[i-1] == sorted_arr[i]:
                rank_map[sorted_arr[i]] = rank
            else:
                rank += 1
                rank_map[sorted_arr[i]] = rank
        
        for i, num in enumerate(arr):
            arr[i] = rank_map[num]
        
        return arr