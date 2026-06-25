class Solution {
public:
    int stoneGameII(vector<int>& piles) {

        int n = piles.size();

        vector<int> suffix(n + 1, 0);

        for (int i = n - 1; i >= 0; --i) {
            suffix[i] = suffix[i + 1] + piles[i];
        }

        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));

        for (int i = n - 1; i >= 0; --i) {
            for (int m = 1; m <= n; ++m) {
                if (2 * m >= n - i) {
                    dp[i][m] = suffix[i];
                } else {
                    int best = 0;
                    for (int x = 1; x <= 2 * m; ++x) {
                        best = max(best, suffix[i] - dp[i + x][max(m, x)]);
                    }
                    dp[i][m] = best;
                }
            }
        }
        return dp[0][1];
    }
};