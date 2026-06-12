class Solution {
public:
    static const int MOD = 1e9 + 7;
    static const int LOG = 17 + 1; // vì n <= 1e5, có thể dùng 20 cho chắc

    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        int LG = 20;

        vector<vector<int>> graph(n + 1);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        vector<int> depth(n + 1, 0);
        vector<vector<int>> up(LG, vector<int>(n + 1, 0));

        queue<int> q;
        q.push(1);
        up[0][1] = 0;

        vector<int> visited(n + 1, 0);
        visited[1] = 1;

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            for (int v : graph[u]) {
                if (visited[v]) continue;

                visited[v] = 1;
                depth[v] = depth[u] + 1;
                up[0][v] = u;

                q.push(v);
            }
        }

        for (int k = 1; k < LG; k++) {
            for (int node = 1; node <= n; node++) {
                up[k][node] = up[k - 1][up[k - 1][node]];
            }
        }

        auto lca = [&](int a, int b) {
            if (depth[a] < depth[b]) swap(a, b);

            int diff = depth[a] - depth[b];
            for (int k = 0; k < LG; k++) {
                if (diff & (1 << k)) {
                    a = up[k][a];
                }
            }

            if (a == b) return a;

            for (int k = LG - 1; k >= 0; k--) {
                if (up[k][a] != up[k][b]) {
                    a = up[k][a];
                    b = up[k][b];
                }
            }

            return up[0][a];
        };

        vector<long long> pow2(n + 1, 1);
        for (int i = 1; i <= n; i++) {
            pow2[i] = pow2[i - 1] * 2 % MOD;
        }

        vector<int> ans;

        for (auto &query : queries) {
            int u = query[0], v = query[1];
            int w = lca(u, v);

            int L = depth[u] + depth[v] - 2 * depth[w];

            if (L == 0) {
                ans.push_back(0);
            } else {
                ans.push_back(pow2[L - 1]);
            }
        }

        return ans;
    }
};