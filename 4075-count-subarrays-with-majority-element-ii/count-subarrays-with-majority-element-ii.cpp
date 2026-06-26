class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        unordered_map<int, long long> pre;
        pre[0] = 1;

        int currentPrefixSum = 0;
        long long validEndingHere = 0;
        long long ans = 0;

        for (int num : nums) {
            if (num == target) {
                validEndingHere += pre[currentPrefixSum];

                currentPrefixSum++;
                pre[currentPrefixSum]++;
            } else {
                currentPrefixSum--;

                validEndingHere -= pre[currentPrefixSum];
                pre[currentPrefixSum]++;
            }

            ans += validEndingHere;
        }

        return ans;
    }
};