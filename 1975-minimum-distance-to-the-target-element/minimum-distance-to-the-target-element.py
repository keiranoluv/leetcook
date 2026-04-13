class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = int(1e9)
        for (i,num) in enumerate(nums):
            if (num==target):
                ans=min(ans,abs(i-start))
        return ans