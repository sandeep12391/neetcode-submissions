from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)

        sorted_nums = sorted(
            frequency,
            key=frequency.get,
            reverse=True
        )

        return sorted_nums[:k]