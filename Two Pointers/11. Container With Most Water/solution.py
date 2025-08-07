class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            width = j - i
            curr_area = width * min(height[i], height[j])
            max_area = max(max_area, curr_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area