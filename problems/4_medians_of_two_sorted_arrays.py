class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        
        if len(merged) % 2 == 1:
            ans = merged[len(merged)//2]
        else:
            ans = (merged[len(merged)//2-1] +merged[len(merged)//2]) / 2
            
        
        return ans
        