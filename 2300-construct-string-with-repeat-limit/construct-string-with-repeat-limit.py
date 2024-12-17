class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0] * 26
        for char in s:
            idx = ord(char)-ord('a')
            freq[idx] += 1

        max_heap = []
        for i in range(26):
            if freq[i] > 0:
                heapq.heappush(max_heap, -i)
        
        res = []
        prev_char = -1
        repeat = 0
        while max_heap:
            char = heapq.heappop(max_heap)
            if -char == prev_char:
                if repeat == repeatLimit:
                    # we want to find another char here if possible
                    if not max_heap:
                        # if no more options left, break
                        break

                    next_char = heapq.heappop(max_heap)
                    res.append(-next_char)
                    freq[-next_char] -= 1
                    if freq[-next_char] != 0:
                        heapq.heappush(max_heap, next_char)
                    prev_char = -next_char
                    repeat = 1
                    heapq.heappush(max_heap, char)

                else:
                    # we can add this char to res
                    res.append(-char)
                    freq[-char] -= 1
                    if freq[-char] != 0:
                        heapq.heappush(max_heap, char)
                repeat += 1

            else:
                # we can add this char to res
                res.append(-char)
                freq[-char] -= 1
                if freq[-char] != 0:
                    heapq.heappush(max_heap, char)
                prev_char = -char
                repeat = 1
            
            

        for i in range(len(res)):
            res[i] = chr(ord('a') + res[i])
        
        return "".join(res)