class Solution:
    def isValid(self, s: str) -> bool:
        result = {")":"(", "}":"{", "]":"["}
        final = []
        for char in s:
            if not char in result:
                final.append(char)
            else:
                if final and result[char] == final[len(final) - 1]:
                    final.pop()
                else:
                    return False
        if final:
            return False
        else:
            return True