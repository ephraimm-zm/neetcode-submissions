class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = {}
        counter = 0
        total = 0
        i = 0
        n = len(s)
        for j in range(n):
            while s[j] in result:
                del result[s[i]]
                counter -= 1
                i += 1
            result[s[j]] = 5
            counter += 1

            if counter > total:
                total = counter
        print(result)
        return total