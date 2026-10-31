class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        bucket = [0] * (len(nums) + 1)
        for number, freq in counter.items():
            if bucket[freq] == 0:
                bucket[freq] = [number]
            else:
                bucket[freq].append(number)
        n = len(bucket)
        ret = []
        for i in range(n - 1, -1, -1):
            if bucket[i] != 0:
                ret.extend(bucket[i])
            if len(ret) == k:
                break
        return ret
