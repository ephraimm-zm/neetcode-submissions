class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            total = 1
            for j in range(n):
                if i == j:
                    continue
                else:
                    total = total * nums[j]
            result.append(total)
        return(result)