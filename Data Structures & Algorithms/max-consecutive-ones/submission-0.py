class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter, maxCounter = 0,0
        for num in nums:
            if num == 1:
                counter += 1
                maxCounter = max(maxCounter, counter)
            else:
                counter = 0
        return maxCounter