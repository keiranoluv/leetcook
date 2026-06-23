MOD = 1000000007
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r-l+1
        dp=[1]*m

        for i in range(2,n+1):
            dp.reverse()
            s=0
            for j in range(m):
                dp[j],s = s, (s+dp[j])%MOD

        return ((sum(dp)%MOD)*2)%MOD
        