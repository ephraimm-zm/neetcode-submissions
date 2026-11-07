class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        l = 0
        counter = 0
        total = 0
        for r in range(len(s)):
            while s[r] in result:
                result.remove(s[l])
                counter -= 1
                l += 1
            result.add(s[r])
            counter += 1
            total = max(counter, total)
        return total