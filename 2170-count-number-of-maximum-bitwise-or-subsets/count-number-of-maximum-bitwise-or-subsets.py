class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # do a tree, for each index either include it or skip it
        # keep a max value seen so far, update it
        # if OR value == max, update a counter

        def dfs(index, curr_res):
            if index >= len(nums):
                return

            # include this number
            temp = curr_res | nums[index]
            if temp == self.max_res:
                self.counter += 1
            elif temp > self.max_res:
                self.max_res = temp
                self.counter = 1

            dfs(index+1, temp)

            # dont include this number
            dfs(index+1, curr_res)
        
        
        self.max_res = 0
        self.counter = 0
        dfs(0, 0)
        return self.counter
