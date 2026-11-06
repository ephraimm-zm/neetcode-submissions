class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = set(nums)
        total = 0
        ret = 0
        for num in result:
            while num + total in result:
                total += 1
            ret = max(total, ret)
            total = 0
        return ret