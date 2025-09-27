class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        curr_alt = 0
        high_alt =0
        for i in range(len(gain)):
            curr_alt = curr_alt + gain[i]
            high_alt = max(high_alt, curr_alt)
        return high_alt



        