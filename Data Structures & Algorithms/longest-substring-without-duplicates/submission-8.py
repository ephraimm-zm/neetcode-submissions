class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        counter = 0
        result = set()
        for r in range(len(s)):
            while s[r] in result:
                result.remove(s[l])
                l += 1
                counter -= 1
            result.add(s[r])
            counter += 1
            longest = max(longest, r - l + 1)
        return longest