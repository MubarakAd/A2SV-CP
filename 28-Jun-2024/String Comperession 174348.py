# Problem: String Comperession - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        s = len(chars)

        while l < s:
            n = 0
            r = l
            while r < s and chars[l] == chars[r]:
                if chars[l] == chars[r]:
                    n += 1
                r += 1

            if n > 1:
                for k in range(l + 1, r):
                    chars.pop(l + 1)
                    s -= 1
                for k in range(len(str(n))):
                    l = l + 1
                    chars.insert(l, str(n)[k])
                    s += 1

            l += 1
            r = l

        return len(chars)