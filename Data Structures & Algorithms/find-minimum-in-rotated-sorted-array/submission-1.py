class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        smallestNum = nums[i]
        for i in range(len(nums)):
            if smallestNum > nums[i]:
                smallestNum = nums[i]
        return smallestNum

