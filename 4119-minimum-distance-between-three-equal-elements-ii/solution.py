class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        next_ = [-1]*n
        appear = {}

        res=1e10

        for i in range(n-1,-1,-1):
            if nums[i] in appear:
                next_[i] = appear[nums[i]]
            appear[nums[i]]=i

        print(next_)

        for i in range(n):
            second = next_[i]
            if (second!=-1):
                third = next_[second]
                if (third!=-1):
                    res=min(res,(third-i)*2)
                    # print(third,i)
        
        return -1 if res==1e10 else res







"""
successor array
distance=2*[max(i,j,k)-min(i,j,k)]
=> minimum distance if i,j,k is 3 three numbers consecutive

next: array
-> next[i] stores the next occur index of nums[i] in array
-> next[i] là lần xuất hiện kế tiếp của nums[i]
-> duyệt từ cuối về đầu, hiển nhiên next[n-1]=-1
"""