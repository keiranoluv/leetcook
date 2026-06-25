class Solution {
public:
    int countMajoritySubarrays(vector<int>& nums, int target) {
        int sz = nums.size();
        int ans = 0;
        for (int i = 0; i < sz; ++i) {
            int cnt = 0;
            for (int j = i; j < sz; ++j) {
                int subArrayLength = j - i + 1;
                if (nums[j] == target) {
                    cnt++;
                }
                if (cnt > subArrayLength / 2) {
                    ans++;
                }
            }
        }
        return ans;
    }
};