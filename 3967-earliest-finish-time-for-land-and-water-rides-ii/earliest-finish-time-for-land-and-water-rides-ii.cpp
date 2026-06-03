class Solution {
public:
    int earliestFinishTime(vector<int>& landStartTime,
                           vector<int>& landDuration,
                           vector<int>& waterStartTime,
                           vector<int>& waterDuration) {
        int water = INT_MAX;
        int land = INT_MAX;
        int waterAns = INT_MAX;
        int landAns = INT_MAX;

        int m = landStartTime.size();
        int n = waterStartTime.size();

        for (int i = 0; i < m; ++i) {
            land = min(land, landStartTime[i] + landDuration[i]);
        }

        for (int i = 0; i < n; ++i) {
            water = min(water, waterStartTime[i] + waterDuration[i]);
        }

        for (int i = 0; i < m; ++i) {
            waterAns =
                min(waterAns, max(water, landStartTime[i]) + landDuration[i]);
        }

        for (int i = 0; i < n; ++i) {
            landAns =
                min(landAns, max(land, waterStartTime[i]) + waterDuration[i]);
        }

        return min(waterAns, landAns);
    }
};