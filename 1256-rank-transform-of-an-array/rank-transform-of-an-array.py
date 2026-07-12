class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        n = len(arr)
        original = copy.deepcopy(arr)
        arr.append(int(-1e9 - 10))
        arr.sort()
        ranks = {}
        rank = 1

        for i in range(1, n + 1):
            if arr[i] not in ranks:
                ranks[arr[i]] = rank
            if arr[i] != arr[i - 1]:
                rank += 1

        ans = []
        for val in original:
            ans.append(ranks[val])

        return ans
