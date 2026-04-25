class Solution {
public:

    bool check(vector<long long>& arr, int side, int k, int limit){
        for (long long start:arr){
            long long end = start + side*4LL - limit;
            long long cur = start;

            for(int i=0; i<k-1;++i){
                auto it = ranges::lower_bound(arr, cur+limit);
                if (it == arr.end() || *it>end){
                    cur = -1;
                    break;
                }
                cur = *it;
            }
            if (cur>=0)
                return true;
        }
        return false;
    }
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        vector<long long> arr;

        for(auto&p: points){
            int x = p[0], y=p[1];
            if (x==0){
                arr.push_back(y);
            }
            else if (y==side){
                arr.push_back(x + side);
            }
            else if (x==side){
                arr.push_back(side*3LL-y);
            }
            else{
                arr.push_back(side*4LL-x);
            }
        }
        sort(arr.begin(),arr.end());

        long long lo=0, hi = side;
        int ans = 0;

        while (lo<=hi){
            long long mid = (lo+hi)/2;
            if (check(arr,side,k,mid)){
                ans = mid;
                lo = mid+1;
            } 
            else{
                hi = mid-1;
            }
        }

        return ans;
        
        return -1;
    }
};