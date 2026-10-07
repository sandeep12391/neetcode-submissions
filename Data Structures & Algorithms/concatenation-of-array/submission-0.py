class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newarr = [0] * (2 * n)
        for i in range(n):
            newarr[i] = nums[i]
            newarr[i + n] = nums[i]
        return newarr
            
        
