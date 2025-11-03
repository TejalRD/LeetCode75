from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort by end coordinate to place arrows greedily at earliest finishing points
        points.sort(key=lambda p: p[1])

        arrows = 1
        arrow_x = points[0][1]  # shoot at the end of the first balloon

        for start, end in points[1:]:
            if start <= arrow_x:
                # current arrow at arrow_x also bursts this balloon
                continue
            # Need a new arrow; place it at this balloon's end
            arrows += 1
            arrow_x = end

        return arrows
