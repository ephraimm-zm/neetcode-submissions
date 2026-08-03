class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in result:
                result[nums[i]] += 1
            else:
                result[nums[i]] = 1
        final = sorted(result.items(), key=lambda item: item[1], reverse=True)
        answer = []
        for i in range(k):
            answer.append(final[i][0])
        return answer
