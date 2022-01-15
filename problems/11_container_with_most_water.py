class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l,r = 0, len(height)-1
        while r-l > 0:
            ans = max(ans,(r-l)*min(height[r],height[l]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return ans