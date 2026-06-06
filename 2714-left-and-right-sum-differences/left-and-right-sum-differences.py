class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0]
        n = len(nums)

        prefixSum = 0
        for i in range(n - 1):
            prefixSum += nums[i]
            leftSum.append(prefixSum)

        rightSum = [0]
        suffixSum = 0
        for i in range(n - 1, 0, -1):
            suffixSum += nums[i]
            rightSum.append(suffixSum)
        rightSum = rightSum[::-1]

        ans = []
        for a, b in zip(leftSum, rightSum):
            ans.append(abs(a - b))

        return ans
