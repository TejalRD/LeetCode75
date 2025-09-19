class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0   # position to write compressed result
        read = 0    # position to read characters

        while read < n:
            ch = chars[read]
            start = read
            # move read until the end of this run
            while read < n and chars[read] == ch:
                read += 1
            count = read - start

            # write the character
            chars[write] = ch
            write += 1

            # if run length > 1, write the digits of count
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write


        