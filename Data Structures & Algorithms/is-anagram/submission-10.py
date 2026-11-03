class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        for letter in s:
            count1[ord(letter) - ord('a')] += 1
        for letter in t:
            count2[ord(letter) - ord('a')] += 1
        return count1 == count2