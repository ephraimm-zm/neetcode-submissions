class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        buckets = [0] * (len(nums) + 1)

        for num, freq in result.items():
            print(freq)
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        n = len(buckets) -  1
        final = []
        for i in range(n, -1, -1):
            if buckets[i] == 0:
                continue
            else:
                final.extend(buckets[i])
            if len(final) == k:
                return final