class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        sort(arr.begin(), arr.end());

        int mx = 0;

        for (int x : arr) {
            if (x > mx) {
                mx++;
            }
        }

        return mx;
    }
};