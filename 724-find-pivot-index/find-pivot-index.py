class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suml =0
        sumr = sum(nums)
        for i in range(len(nums)):
            sumr = sumr - nums[i]
            if sumr == suml:
                return i
            suml = suml + nums[i]
        return -1 
        