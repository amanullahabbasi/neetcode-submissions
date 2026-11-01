class Solution:
    def isValid(self, s: str) -> bool:
        # key = a closer, value = the opener it needs
        pairs = {")": "(", "]": "[", "}": "{"}

        # holds only openers that are still waiting for their closer (top = newest)
        stack = []

        for ch in s:
            if ch in pairs:
                # ch is a closer, so it must match the newest waiting opener
                # stack empty: nothing to match
                # stack[-1] is the top: the wrong opener means the order is broken
                if not stack or stack[-1] != pairs[ch]:
                    return False
                # matched, so that opener is no longer waiting
                stack.pop()
            else:
                # ch is an opener: push it, only openers ever go on the stack
                stack.append(ch)

        # valid only if no opener is left waiting
        return not stack
        