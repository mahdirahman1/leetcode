class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        curr = "0"
        while n > 1:
            next_curr = curr + "1"
            # generate right side
            right = str(bin(int(curr, 2) ^ (2**len(curr)-1)))[2:][::-1]
            # add 0s to start
            next_curr += "0" * (len(curr)-len(right)) 
            next_curr += right
            curr = next_curr
            if len(curr) >= k:
                return curr[k-1]
            n -= 1
        
        return curr[k-1]
        
    
