class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        total = 0
        ret = 0
        for num in nums:
            while num + total in nums:
                total += 1
            ret = max(total, ret)
            total = 0
        return ret