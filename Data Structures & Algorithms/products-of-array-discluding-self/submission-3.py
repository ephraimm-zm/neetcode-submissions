class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        final = []
        while i < len(nums):
            result = 1
            j = 0
            while j < len(nums):
                if j != i:
                    result *= nums[j]
                j += 1
            final.append(result)
            i += 1
        return final