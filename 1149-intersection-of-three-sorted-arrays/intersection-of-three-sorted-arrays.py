class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        """
        3 pointers use arr1 as reference, if arr2 or arr3 cross arr1 move arr1 and continue
        """
        p_2 = 0
        p_3 = 0
        res = []
        for num in arr1:
            while p_2 < len(arr2) and arr2[p_2] < num:
                p_2 += 1

            while p_3 < len(arr3) and arr3[p_3] < num:
                p_3 += 1

            if p_2 < len(arr2) and p_3 < len(arr3) and num == arr2[p_2] == arr3[p_3]:
                res.append(num)
        
        return res
            


