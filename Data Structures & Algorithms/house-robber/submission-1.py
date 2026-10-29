class Solution:
    def rob(self, nums: List[int]) -> int:
        two_back = 0
        one_back = 0
        for n in nums:
            best = max(one_back, two_back + n)
            two_back = one_back
            one_back = best
        return one_back