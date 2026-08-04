class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        smallest = [nums[i], i]
        smallestNum = nums[i]
        for i in range(len(nums)):
            if smallestNum > nums[i]:
                print(i)
                smallest = [nums[i], i]
                smallestNum = nums[i]
        return smallestNum

