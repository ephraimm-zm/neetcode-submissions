class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxh = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            if heights[i] < heights[j]:
                vol = heights[i] * (j - i)
                i += 1
            else:
                vol = heights[j] * (j - i)
                j -= 1
            if vol > maxh:
                maxh = vol
        return maxh