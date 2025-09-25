class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        best = 0

        for right, val in enumerate(nums):
            if val == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # window [left, right] has at most k zeros
            best = max(best, right - left + 1)

        return best
