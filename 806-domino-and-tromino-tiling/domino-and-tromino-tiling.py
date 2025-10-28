class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2

        f0, f1, f2 = 1, 1, 2  # F[0], F[1], F[2]
        for k in range(3, n + 1):
            f3 = (2 * f2 + f0) % MOD  # F[k] = 2F[k-1] + F[k-3]
            f0, f1, f2 = f1, f2, f3
        return f2
        