class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        digitSet = dict()

        for digit in str(n):
            if digit in digitSet:
                digitSet[digit]+=1
            else:
                digitSet[digit]=1

        ans = 0
        for k,v in digitSet.items():
            ans+=int(k)*v
        
        return ans
        