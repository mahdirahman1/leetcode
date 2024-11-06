class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        """
        # sort the array and compare sorted array with original array
        # keep calculating the bit set for each num
        # if current bit set is not same as prev, this number must be larger than prev bitset nums, otherwise it means we need to swap from previous group which isnt possible
        [8,4,2,30,15]
        1 1 1  4  4

        [1,2,3,4,5]
        1 1 2 1 2

        [3,16,8,4,2]
        2 1  1 1 1

        [75,34,30]
        4, 2,  4
        """
        prev_bit_set = -1
        old_bit_set = -1
        prev_largest = 0
        curr_largest = 0

        for num in nums:
            count = 0
            curr = num
            while curr > 0:
                if curr % 2 == 1:
                    count += 1
                curr >>= 1
            

            if count != prev_bit_set:
                old_bit_set = prev_bit_set
                prev_bit_set = count
                prev_largest = curr_largest

            if count != old_bit_set and num < prev_largest:
                return False


            curr_largest = max(curr_largest, num)
            

        
        return True


        