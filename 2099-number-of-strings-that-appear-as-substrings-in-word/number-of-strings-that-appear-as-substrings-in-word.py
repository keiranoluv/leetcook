class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for val in patterns:
            if val in word:
                ans += 1

        return ans
