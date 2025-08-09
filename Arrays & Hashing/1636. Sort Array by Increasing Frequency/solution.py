from collections import Counter
class Solution:
    def frequencySort(self, nums):
        freq = Counter(nums)
        def decreasingSort(n):
            return (freq[n], -n)
        nums.sort(key=decreasingSort)
        return nums
        