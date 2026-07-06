class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<bool> visited(n, false);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == j) {
                    continue;
                }

                int a = intervals[i][0], b = intervals[i][1];
                int c = intervals[j][0], d = intervals[j][1];

                if (c <= a && b <= d) {
                    visited[i] = true;
                    break;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (!visited[i])
                ans += 1;
        }
        return ans;
    }
};