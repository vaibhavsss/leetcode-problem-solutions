from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        frequency_counter = Counter(nums)  # count frequencies
        max_frequency = max(frequency_counter.values())  # find max frequency
        # sum frequencies of elements that have max frequency
        return sum(freq for freq in frequency_counter.values() if freq == max_frequency)
