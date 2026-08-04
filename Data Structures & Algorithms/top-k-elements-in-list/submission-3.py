from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # Bucket Sort:
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = count.get(n, 0) + 1
        # for n,c in count.items():
        #     freq[c].append(n)
        
        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if k == len(res):
        #             return res
        frequency = Counter(nums)

        sorted_nums = sorted(
            frequency,
            key=frequency.get,
            reverse=True
        )

        return sorted_nums[:k]