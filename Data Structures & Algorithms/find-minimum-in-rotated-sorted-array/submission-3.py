class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[int(i)] < nums[int(j)]:
                return nums[int(i)]
            mid = (i + j) / 2
            if nums[int(mid)] > nums[int(j)]:
                i = mid + 1
            else:
                j = mid
        return nums[int(i)]

