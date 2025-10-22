class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)  # (b, a)

        heap = []          # min-heap of selected nums1 values
        sumA = 0
        best = 0

        for b, a in pairs:
            heappush(heap, a)
            sumA += a

            if len(heap) > k:
                sumA -= heappop(heap)  # drop smallest to keep only top-k sum

            if len(heap) == k:
                best = max(best, sumA * b)

            # Note: we *don’t* pop after scoring; we only prune when size>k.
        return best