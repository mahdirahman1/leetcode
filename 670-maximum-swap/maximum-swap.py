class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(char) for char in str(num)]
        maxHeap = []
        for i,n in enumerate(num):
            heapq.heappush(maxHeap, (-n, -i))
        
        for i in range(len(num)):
            number, index = heapq.heappop(maxHeap)
            while -index < i:
                number, index = heapq.heappop(maxHeap)

            if num[i] != -number:
                # swap
                num[i], num[-index] = num[-index], num[i]
                break
            elif i != -index:
                # num is same, if index is different put it back in heap
                heapq.heappush(maxHeap, (number,index))
        
        return int("".join([str(n) for n in num]))