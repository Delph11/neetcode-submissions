class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def TimeCheck(k):
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / k)
            return time_taken <= h

        lo, hi = 1, max(piles)  # search k directly in range [1, max]
        k = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            if TimeCheck(mid):  # pass mid as k directly
                k = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return k