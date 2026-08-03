class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = sorted(nums)
        n = len(new)
        for i in range(n - 1):
            if new[i] == new[i + 1]:
                return True
        return False