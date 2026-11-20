from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        result = sorted(count, key=count.get, reverse=True)
        return result[:k]
