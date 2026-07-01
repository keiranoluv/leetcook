class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int n = grid.size();

        queue<pair<int, int>> q;
        vector<vector<int>> safety(n, vector<int>(n, -1));

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    safety[i][j] = 0;
                    q.push({i, j});
                }
            }
        }
        vector<pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();

            for (auto [dr, dc] : dirs) {
                int nr = r + dr;
                int nc = c + dc;

                if (nr >= 0 && nr < n && nc >= 0 && nc < n &&
                    safety[nr][nc] == -1) {
                    safety[nr][nc] = safety[r][c] + 1;
                    q.push({nr, nc});
                }
            }
        }

        priority_queue<tuple<int, int, int>> maxHeap;
        vector<vector<bool>> visited(n, vector<bool>(n, false));

        maxHeap.push({safety[0][0], 0, 0});
        visited[0][0] = true;

        while (!maxHeap.empty()) {
            auto [sf, r, c] = maxHeap.top();
            maxHeap.pop();

            if (r == n - 1 && c == n - 1) {
                return sf;
            }

            for (auto [dr, dc] : dirs) {
                int nr = r + dr;
                int nc = c + dc;

                if (nr >= 0 && nr < n && nc >= 0 && nc < n &&
                    !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    int newSf = min(sf, safety[nr][nc]);
                    maxHeap.push({newSf, nr, nc});
                }
            }
        }
        return 0;
    }
};