# class Solution:
#     def minFlips(self, a: int, b: int, c: int) -> int:
#         flips = 0
#         while a or b or c:
#             a_bit, b_bit, c_bit= a&1, b&1, c&1
#             if (a_bit | b_bit) !=c_bit:
#                 if c_bit ==1:
#                     flips +=1
#                 else:
#                     flips += (b_bit + b_bit)
#             a >>= 1
#             b >>= 1
#             c >>= 1
#         return flips

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:  # <-- include c here
            a_bit, b_bit, c_bit = a & 1, b & 1, c & 1
            if (a_bit | b_bit) != c_bit:
                if c_bit == 1:
                    flips += 1
                else:
                    flips += (a_bit + b_bit)  # 1 flip if one is 1, 2 flips if both are 1
            a >>= 1
            b >>= 1
            c >>= 1
        return flips

        