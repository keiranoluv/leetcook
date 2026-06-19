class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        current_altitude = 0
        for g in gain:
            current_altitude +=g
            altitudes.append(current_altitude)

        return max(altitudes)
        