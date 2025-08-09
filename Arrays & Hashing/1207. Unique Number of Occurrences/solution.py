from collections import Counter
class Solution:
    def uniqueOccurence(self, arr):
        ans = Counter(arr)
        
        return len(ans.values()) == len(set(ans.values()))
    
    '''
    Approach: HashSet
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''