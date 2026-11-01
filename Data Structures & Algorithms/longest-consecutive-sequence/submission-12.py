class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        maxi = 0

        for num in new:
            if not num - 1 in new:
                length = 0
                while (num + length) in new:
                    length += 1
                    if length >= maxi:
                        maxi = length
                length = 0
        return maxi