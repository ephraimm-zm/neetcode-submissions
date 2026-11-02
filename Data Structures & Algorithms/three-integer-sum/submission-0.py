class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = sorted(nums)
        final = []
        for i in range(len(res) - 1):
            if i > 0 and res[i] == res[i - 1]:
                continue
            left = i + 1
            right = len(res) - 1
            while left < right:
                total = res[i] + res[left] + res[right]
                if total == 0:
                    final.append([res[i], res[left], res[right]])
                    left += 1
                    while res[left] == res[left - 1] and left < right:
                        left += 1
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
        return final