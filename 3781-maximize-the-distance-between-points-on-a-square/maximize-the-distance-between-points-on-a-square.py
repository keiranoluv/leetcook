class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:

        arr = []
        
        for x,y in points:
            if (x==0): #L
                arr.append(y)
            elif (y==side): #U
                arr.append(side+x)
            elif (x==side): #R
                arr.append(3*side-y)
            else: #D
                arr.append(4*side-x)

        arr.sort()
 
        def check(limit):
            p = 4*side
            for start in arr:
                end = start + p - limit #(1)
                cur = start
                for _ in range(k-1):
                    idx = bisect_left(arr,cur+limit) #(2)
                    if (idx == len(arr)) or arr[idx]>end:
                        cur=-1
                        break
                    cur=arr[idx]
                if cur >=0:
                    return True
            return False

        lo, hi = 1 , side
        ans = 0

        while (lo<=hi):
            mid = (lo+hi)//2
            if (check(mid)==True):
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
            
        return ans

"""
(1)
Ta cần: start - end >= limit, nhưng đây là mảng vòng tròn nên
start - (end-4p) >= limit
end - start <= 4p - limit
end <= 4p - limit + start

(2) bisect_left(arr,cur+limit)
Tìm vị trí trong mảng arr sao cho arr[vị trí đó]>=cur+limit
"""