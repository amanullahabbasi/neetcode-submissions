from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1  # The position we need to reach.
        farthest = 0  # The farthest index we can reach so far.

        for index in range(len(nums)):  # Walk left to right.
            if index > farthest:  # This index is beyond our reach,
                return False  # so we are stuck.

            reach_from_here = index + nums[index]  # Farthest landing from this index.
            if reach_from_here > farthest:  # If it beats our best,
                farthest = reach_from_here  # update our best.

            if farthest >= last_index:  # If we can reach the end,
                return True  # we are done.

        return False  # Only reached if the loop ends without reaching the end.