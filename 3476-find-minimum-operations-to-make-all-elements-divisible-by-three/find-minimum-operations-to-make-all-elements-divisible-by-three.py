class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans+= 1 if num%3!=0 else 0
        
        return ans
        