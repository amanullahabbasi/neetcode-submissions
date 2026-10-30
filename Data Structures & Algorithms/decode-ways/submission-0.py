class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        two_back = 1
        one_back = 1
        for i in range(2, len(s) + 1):
            ways = 0
            if s[i - 1] != "0":
                ways += one_back
            if 10 <= int(s[i - 2:i]) <= 26:
                ways += two_back
            two_back = one_back
            one_back = ways
        return one_back