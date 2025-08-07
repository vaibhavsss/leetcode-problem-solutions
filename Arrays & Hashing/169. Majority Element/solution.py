class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        appear = None

        for num in nums:
            if count == 0:
                appear = num
            count += (1 if num == appear else -1)
        return appear