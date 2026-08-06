class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        lib = {")":"(", "}":"{","]":"["}
        for char in s:
            if char in lib:
                if result and result[len(result) -1] == lib[char]:
                    result.pop()
                else:
                    return False
            else:
                result.append(char)
        print(result)
        return not result