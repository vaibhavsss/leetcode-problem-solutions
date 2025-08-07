class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num # This is a default bitwise operator ^=
        return ans
    
    '''
    Personal Note: 
    Time Complexity: O(n)
    Space Complexity: O(1)
    Approach used: XOR-wise (bitwise operator)
    How it works:
    When we XOR all numbers in the array:
        - If a number is repeated, the result will be 0
        - If a number is unique, the result will be that number
        
    '''