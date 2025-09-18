class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits)
        projects=sorted(zip(capital, profits))
        available = []

        ptr=0

        for _ in range(k):
            while ptr < n and projects[ptr][0] <= w:
                heapq.heappush(available, -projects[ptr][1])
                ptr+=1

            if available:
                w += -heapq.heappop(available)

        return w