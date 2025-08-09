from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        
        buckets = [[] for _ in range(len(s) + 1)]
        for char, freq in count.items():
            buckets[freq].append(char)
        result = []
        for freq in range(len(buckets) - 1, -1, -1):
            for char in buckets[freq]:
                result.append(char * freq)
        return ''.join(result)