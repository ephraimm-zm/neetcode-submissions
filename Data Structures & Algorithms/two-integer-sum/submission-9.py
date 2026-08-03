class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        i = 0
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            print(diff)
            if diff in result:
                return([result[diff], i])
            result[nums[i]] = i