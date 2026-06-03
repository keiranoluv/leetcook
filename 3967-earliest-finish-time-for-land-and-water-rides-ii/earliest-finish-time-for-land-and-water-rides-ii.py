class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        MAX = 10**6
        m, n = len(landStartTime), len(waterStartTime)
        land = water = minLand = minWater = MAX

        for s, d in zip(landStartTime, landDuration):
            land = min(s + d, land)

        for s, d in zip(waterStartTime, waterDuration):
            water = min(s + d, water)

        for s, d in zip(landStartTime, landDuration):
            minWater = min(minWater, max(water, s) + d)

        for s, d in zip(waterStartTime, waterDuration):
            minLand = min(minLand, max(land, s) + d)

        return min(minLand, minWater)
