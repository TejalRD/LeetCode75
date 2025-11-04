class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = {}
        total = len(nums)

        for arr in nums:
            for num in arr:
                count[num] = count.get(num,0) +1

        result = [num for num, freq in count.items() if freq == total]  #list comprehension in Python — a compact way to build a new list by looping through something.
        return sorted(result)

        