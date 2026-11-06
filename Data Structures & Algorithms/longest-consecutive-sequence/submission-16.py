class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = set(nums)
        total = 0
        final = 0
        for num in result:
            if not num - 1 in result:
                while num + total in result:
                    total += 1
                final = max(total, final)
                total = 0
        return final