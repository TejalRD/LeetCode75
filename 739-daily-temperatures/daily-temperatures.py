class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []  # holds indices

        for i, temp in enumerate(temperatures):
            # While current temp is greater than the temp at top of stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                ans[prev_day] = i - prev_day  # days waited
            stack.append(i)

        return ans

        