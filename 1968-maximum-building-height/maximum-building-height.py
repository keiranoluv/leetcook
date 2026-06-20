from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        r = restrictions

        r.append([1, 0])
        r.sort()

        if r[-1][0] != n:
            r.append([n, n - 1])

        m = len(r)


        for i in range(1, m):
            dist = r[i][0] - r[i - 1][0]
            r[i][1] = min(r[i][1], r[i - 1][1] + dist)

        for i in range(m - 2, -1, -1):
            dist = r[i + 1][0] - r[i][0]
            r[i][1] = min(r[i][1], r[i + 1][1] + dist)

        ans = 0

        for i in range(m - 1):
            dist = r[i + 1][0] - r[i][0]
            h1 = r[i][1]
            h2 = r[i + 1][1]

            peak = (dist + h1 + h2) // 2
            ans = max(ans, peak)

        return ans