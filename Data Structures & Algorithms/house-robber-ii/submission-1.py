class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            two_back = 0
            one_back = 0
            for n in houses:
                best = max(one_back, two_back + n)
                two_back = one_back
                one_back = best
            return one_back

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))