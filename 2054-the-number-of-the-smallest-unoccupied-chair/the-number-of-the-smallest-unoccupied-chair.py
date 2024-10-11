class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_start = times[targetFriend][0]
        times.sort()

        seats = [i for i in range(len(times))]
        heapq.heapify(seats)
        event_heap = []
    
        for start, end in times:
            while event_heap and event_heap[0][0] <= start:
                _, seat = heapq.heappop(event_heap)
                heapq.heappush(seats, seat)

            if start == target_start:
                return seats[0]
            
            seat = heapq.heappop(seats)
            heapq.heappush(event_heap, [end, seat])

        
            