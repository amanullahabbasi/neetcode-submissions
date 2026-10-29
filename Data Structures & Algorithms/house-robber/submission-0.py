class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        cur = 0
        for n in nums:
            best = max(cur, prev + n)
            prev = cur
            cur = best
        return cur