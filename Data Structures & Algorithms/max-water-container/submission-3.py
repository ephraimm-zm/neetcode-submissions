class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxi = 0
        while i < j:
            total = min(heights[i], heights[j]) * (j - i)
            if total > maxi:
                maxi = total
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return maxi