class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:

        n = len(online)

        # Rebuild graph with online node
        g = [[] for _ in range(n)]

        l, r = float("inf"), 0

        for u, v, w in edges:
            if (online[u] == False) or (online[v] == False):
                continue
            else:
                g[u].append((v, w))
                l = min(l, w)  # Store lowest weight to use BS
                r = max(r, w)  # Store highest weight to use BS

        # Check valid path
        def check(mid):
            dis = [float("inf")] * n  # dist[u] = smallest cost sum from 0 -> u
            pq = [(0, 0)]  # (current_distance, node)
            dis[0] = 0

            while pq:
                d, u = heapq.heappop(pq)

                if d > k:
                    return False
                if u == n - 1:
                    return True

                if d > dis[u]:  # current_distance > current cost from 0->v
                    continue

                for v, w in g[u]:
                    if w < mid:
                        continue
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        heapq.heappush(pq, (dis[v], v))
            return False

        if check(l) == False:
            return -1

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
