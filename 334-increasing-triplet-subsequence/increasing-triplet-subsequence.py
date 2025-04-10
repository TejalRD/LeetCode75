class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j=float('inf')
        for curr_num in nums:
            if curr_num<=i:
                i=curr_num
            elif curr_num<=j:
                j=curr_num
            else:
                return True
        return False
        