class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi = 0
        new = sorted(nums)
        counter = 1
        print(new)
        for i in range(len(new) - 1):
            j = i + 1
            if new[i] == new[j]:
                continue
            if new[i] + 1 == new[j]:
                counter += 1
                if maxi < counter:
                    maxi = counter
            else:
                counter = 1
        return maxi