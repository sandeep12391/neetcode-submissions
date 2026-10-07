class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            largest = nums[i+1]
            for j in range(i + 1, len(nums)):
                largest = max(largest, nums[j])
            nums[i] = largest
        nums[len(nums) - 1] = -1
        return nums