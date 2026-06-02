class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        landSchedule = []
        for start, end in zip(landStartTime, landDuration):
            landSchedule.append((start, start + end))

        waterSchedule = []
        for start, end in zip(waterStartTime, waterDuration):
            waterSchedule.append((start, start + end))

        ans = int(1e9)

        for lStart, lEnd in landSchedule:
            for wStart, wEnd in waterSchedule:
                if lEnd <= wStart:
                    ans = min(ans, wEnd)
                elif wEnd <= lStart:
                    ans = min(ans, lEnd)
                else:
                    ans = min(ans, lEnd + wEnd - wStart, wEnd + lEnd - lStart)
        return ans
