from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        kept = 0
        last_end = float('-inf')
        for s, e in intervals:
            if s >= last_end:     # non-overlapping with the last kept interval
                kept += 1
                last_end = e
            # else: overlaps → skip (i.e., "remove" this one)
        
        return len(intervals) - kept
