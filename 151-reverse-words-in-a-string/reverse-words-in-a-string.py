class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        words = s.split()
        reverse_str = words[::-1]
        return ' '.join(reverse_str)
        