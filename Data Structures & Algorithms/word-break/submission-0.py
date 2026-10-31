class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # dp[i] = can the first i characters of s be built?
        # Example len(s)=3 -> 4 spots: [False, False, False, False]
        dp = [False] * (len(s) + 1)

        # Empty string is valid
        dp[0] = True

        # i = how many characters we are trying to build
        for i in range(1, len(s) + 1):

            # Try every word in the dictionary
            for word in wordDict:

                # If word ends at i, where does it start?
                start = i - len(word)

                # Check:
                # 1. word fits
                # 2. everything before it was valid
                # 3. substring actually equals the word
                if start >= 0 and dp[start] and s[start:i] == word:
                    dp[i] = True
                    break

        # Is the entire string buildable?
        return dp[len(s)]