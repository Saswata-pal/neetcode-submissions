import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low =1
        high=max(piles)
        ans=high

        while low<=high:
            k=(low+high)//2

            total_hours=sum(math.ceil(p/k) for p in piles)

            if total_hours <= h:
                ans = k
                high = k-1
            else:
                low = k+1
        return ans