class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        ans = True
        p = q = None
        for i in range(len(nums)-1):
            if (p is None) and (nums[i]>=nums[i+1]):
                p = i
            if (p is not None) and (q is None) and (nums[i]<=nums[i+1]):
                q = i
        
        if (p is None) or (q is None) or (p==0) or (q==len(nums)-1):
            return False

        for i in range(q,len(nums)-1):
            if (nums[i]>=nums[i+1]):
                return False

        return ans


        