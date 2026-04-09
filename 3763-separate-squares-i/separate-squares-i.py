class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        sum_all_squares = 0

        # for square in squares:
        #     sum_all_squares += square[-1]**2

        L=0
        R=1e10

        while (L<R):
            #print(L,R, abs(L-R))
            if abs(L-R)<1e-6:
                break
            mid = (L+R)/2.0
            area_down = 0.
            area_up = 0.
            for square in squares:
                if (square[1]+square[2]<=mid):
                    area_down+=float(square[2]**2)
                    continue
                elif (square[1]>=mid):
                    area_up+=float(square[2]**2)
                    continue
                else:
                    area_down+=float(abs(mid-square[1])*square[2])
                    area_up += float(square[2]**2)- float(abs(mid-square[1])*square[2])          
           
            if (area_down>area_up):
                R=mid
            elif (area_down<area_up):
                L=mid
            elif (area_down==area_up):
                R=mid


        return L
        