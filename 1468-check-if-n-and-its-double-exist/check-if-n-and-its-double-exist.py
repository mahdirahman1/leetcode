class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        num_index_map = set()

        for num in arr:
            if num/2 in num_index_map or num*2 in num_index_map:
                return True
            
            num_index_map.add(num)
        
        return False