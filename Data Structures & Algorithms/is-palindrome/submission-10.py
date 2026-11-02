class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for item in s:
            if item.isalnum():
                res.append(item.lower())
        i = 0
        j = len(res) - 1
        while i <= j:
            if res[i] == res[j]:
                i += 1
                j -= 1
            else:
                return False
        return True