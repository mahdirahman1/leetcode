class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_start = times[targetFriend][0]
        start_to_end = defaultdict(int)
        for start, end in times:
            start_to_end[start] = end
        

        seats = [i for i in range(len(times))]
        heapq.heapify(seats)
        event_heap = []

        for time in range(target_start+1):
            # see if any events end and add seat back
            while event_heap and event_heap[0][0] == time:
                _, seat = heapq.heappop(event_heap)
                heapq.heappush(seats, seat)
                
            if time == target_start:
                return seats[0]

            if time in start_to_end:
                seat = heapq.heappop(seats)
                heapq.heappush(event_heap, [start_to_end[time], seat])
               
        
        print(seats)
        return seats[0]
            