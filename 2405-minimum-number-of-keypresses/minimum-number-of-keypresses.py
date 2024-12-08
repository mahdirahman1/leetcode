class Solution:
    def minimumKeypresses(self, s: str) -> int:
        click_map = defaultdict(int)
        for char in s:
            click_map[char] += 1

        max_heap = []
        for char, freq in click_map.items():
            heapq.heappush(max_heap, [-freq, char])

        idx = 0
        res = 0
        click_map = defaultdict(int)
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            if char not in click_map:
                click_map[char] = -freq * ((idx//9)+1)
                idx += 1

            res += click_map[char]

        return res