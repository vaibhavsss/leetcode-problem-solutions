class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left+1, right+1] # We write +1 as our index condition is 1-indexed array
            elif current_sum < target:
                left += 1 # Number too small so move our 'left' towards Right
            else:
                right -= 1 # Number too large so move our 'right' towards Left