class Solution:
    def countWaviness(self, num):
        if (num<100):
            return 0
        
        cnt = 0
        strNum = str(num)
        for i in range(1, len(strNum)-1):
            if (strNum[i]>strNum[i-1] and strNum[i]>strNum[i+1]):
                cnt+=1
            if (strNum[i]<strNum[i-1] and strNum[i]<strNum[i+1]):
                cnt+=1
        return cnt


    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for i in range(num1,num2+1):
            ans+=self.countWaviness(i)

        return ans
        