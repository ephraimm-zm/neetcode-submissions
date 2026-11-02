class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = set()
        total = 0
        for num in nums:
            result.add(num)
        for num in result:
            if not (num - 1) in result:
                length = 0
                while (num + length) in  result:
                    length += 1
                    if total < length:
                        total = length
                length = 0
        return total