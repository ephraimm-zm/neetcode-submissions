class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        test = { ")":"(", "}":"{", "]":"[" }
        for char in s:
            if char in test:
                if result:
                    if result[len(result) - 1] == test[char]:
                        result.pop()
                    else:
                        return False
            else:
                result.append(char)
        print(result)
        if result:
            return False
        else:
            return True