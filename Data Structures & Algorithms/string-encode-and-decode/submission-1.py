class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the #
            while s[j] != "#":
                j += 1

            # Characters i → j contain the length
            length = int(s[i:j])

            # Move to first character of actual string
            i = j + 1

            # Extract exactly 'length' characters
            result.append(s[i:i + length])

            # Move to next encoded string
            i += length

        return result