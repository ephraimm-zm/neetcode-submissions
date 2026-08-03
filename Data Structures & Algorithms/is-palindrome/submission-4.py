class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for char in s:
            if char.isalnum():
                result += char.lower()
        i = 0
        j = len(result) - 1
        while i < j:
            if result[i] != result[j]:
                return False
            else:
                i += 1
                j -= 1
        return True