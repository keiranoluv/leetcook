class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pre = defaultdict(int)
        pre[0] = 1

        currentPrefixSum = 0
        validEndingHere = 0
        ans = 0

        for x in nums:
            if x == target:
                validEndingHere += pre[currentPrefixSum]
                currentPrefixSum += 1
                pre[currentPrefixSum] += 1
            else:
                currentPrefixSum -= 1
                validEndingHere -= pre[currentPrefixSum]
                pre[currentPrefixSum] += 1

            ans += validEndingHere

        return ans