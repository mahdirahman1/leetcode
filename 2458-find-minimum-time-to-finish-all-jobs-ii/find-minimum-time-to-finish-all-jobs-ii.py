class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        """
        greedy: assign longest task to worker with most hours per day

        """
        jobs.sort()
        workers.sort()

        max_time = 0
        for i, time_required in enumerate(jobs):
            max_time = max(max_time, math.ceil(time_required/workers[i]))
        
        return max_time