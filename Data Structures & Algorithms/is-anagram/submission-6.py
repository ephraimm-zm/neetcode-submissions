class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        
        result1 = {}
        result2 = {}

        for char in s:
            if char in result1:
                result1[char] += 1
            else:
                result1[char] = 1
        
        for char in t:
            if char in result2:
                result2[char] += 1
            else:
                result2[char] = 1
        
        return result1 == result2