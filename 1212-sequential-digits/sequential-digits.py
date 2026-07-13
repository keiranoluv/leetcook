class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        all = []
        step = [None, None, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111]

        for i in range(2, 10):
            ans = 0
            for digit in range(i):
                ans = ans * 10 + (int(digit) + 1)

            all.append(ans)

            for j in range(9 - i):
                ans += step[i]
                all.append(ans)

        ans = []
        for val in all:
            if low <= val <= high:
                ans.append(val)

        print(all)
        return ans
