class Solution:
    def isUgly(self, n: int) -> bool:
        # we need to divide the input by 2, 3 and 5 again and again
        if n <= 0:
            return False
        
        for prime in [2, 3, 5]:
            while n % prime == 0:
                n//= prime
        
        return n == 1
# Time Complexity: O(log n)
# Space Complexity: O(1)
        