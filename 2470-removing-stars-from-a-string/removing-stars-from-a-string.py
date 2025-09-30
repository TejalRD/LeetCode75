class Solution:
    def removeStars(self, s: str) -> str:
        char_list = list(s)
        char_stack = []
        for char in char_list:
            if char != "*":
                char_stack.append(char)
            else:
                char_stack.pop()
        return "".join(char_stack)

        