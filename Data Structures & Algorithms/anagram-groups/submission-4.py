from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            item = tuple(count)
            if item in result:
                result[item].append(word)
            else:
                result[item] = [word]
        return list(result.values())