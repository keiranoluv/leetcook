class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # lg[i] = floor(log2(i))
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        m = lg[n] + 1

        st_max = [[0] * n for _ in range(m)]
        st_min = [[0] * n for _ in range(m)]

        st_max[0] = nums[:]
        st_min[0] = nums[:]

        # Build sparse tables
        for p in range(1, m):
            length = 1 << p
            half = length >> 1

            for i in range(n - length + 1):
                st_max[p][i] = max(st_max[p - 1][i], st_max[p - 1][i + half])
                st_min[p][i] = min(st_min[p - 1][i], st_min[p - 1][i + half])

        def range_max(l: int, r: int) -> int:
            length = r - l + 1
            p = lg[length]
            return max(st_max[p][l], st_max[p][r - (1 << p) + 1])

        def range_min(l: int, r: int) -> int:
            length = r - l + 1
            p = lg[length]
            return min(st_min[p][l], st_min[p][r - (1 << p) + 1])

        def value(l: int, r: int) -> int:
            return range_max(l, r) - range_min(l, r)

        heap = []

        # Với mỗi l, bắt đầu từ subarray dài nhất nums[l..n-1]
        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)
            ans += -neg_v

            # Phần tử tiếp theo trong cùng dãy của l là nums[l..r-1]
            if r > l:
                nr = r - 1
                nv = value(l, nr)
                heapq.heappush(heap, (-nv, l, nr))

        return ans