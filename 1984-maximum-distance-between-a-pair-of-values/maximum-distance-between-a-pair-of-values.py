class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for (i,num1) in enumerate(nums1):
            L,R = i, len(nums2)-1
            ans = -1
            while (L<=R):
                mid = (L+R)//2
                if (nums1[i] <= nums2[mid]):
                    ans = mid
                    L=mid+1
                else:
                    R=mid-1
                # print(L,R,ans)

            if (ans!=-1):
                res = max(res, ans-i)

        return res



"""
Solution 1: Binary search when keep i in nums1 and find j farthest in nums2
Solution 2: Two pointers
"""
