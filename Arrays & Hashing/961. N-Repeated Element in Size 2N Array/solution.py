class Solution:
    def repeatedNTimes(self, nums):
        ans=set()
        for num in nums:
            if num in ans:
                return num
            ans.add(num)
        
        