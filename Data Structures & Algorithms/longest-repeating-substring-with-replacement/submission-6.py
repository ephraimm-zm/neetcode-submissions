class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0
        longest = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1
        print(count)