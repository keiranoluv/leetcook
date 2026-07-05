class Solution {
public:
    vector<int> parent;

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unite(int a, int b) {
        int pa = find(a);
        int pb = find(b);

        if (pa != pb) {
            parent[pb] = pa;
        }
    }
    int minScore(int n, vector<vector<int>>& roads) {

        parent.resize(n + 1);
        for (int i = 1; i <= n; ++i) {
            parent[i] = i;
        }

        for (auto& road : roads) {
            unite(road[0], road[1]);
        }

        int root1 = find(1);
        int ans = INT_MAX;

        for (auto& road : roads) {
            int u = road[0];
            int v = road[1];
            int w = road[2];

            if (find(u) == root1) {
                ans = min(ans, w);
            }
        }
        return ans;
    }
};