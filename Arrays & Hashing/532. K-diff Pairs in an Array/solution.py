from collections import Counter
from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0

        count = 0
        freq = Counter(nums)

        if k == 0:
            for num in freq:
                if freq[num] > 1: # WE SHALL CHECK MORE THAN ONCE OCCURRENCE
                    count += 1 
        else:
            for num in freq:
                if num + k in freq:
                    count += 1

        return count