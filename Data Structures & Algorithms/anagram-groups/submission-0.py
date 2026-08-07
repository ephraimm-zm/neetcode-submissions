class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            if "".join(sorted(word)) in result:
                result["".join(sorted(word))].append(word)
            else:
                result["".join(sorted(word))] = [word]
        new = list(result.values())
        return new