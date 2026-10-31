class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # best and worst product ending at the current position
        current_max = nums[0]
        current_min = nums[0]

        # best product found anywhere so far
        answer = nums[0]

        for num in nums[1:]:
            # save old values because both new values need them
            old_max = current_max
            old_min = current_min

            # either start fresh at num, or extend previous max/min
            current_max = max(num, num * old_max, num * old_min)

            # keep minimum too because negative * negative can become positive
            current_min = min(num, num * old_max, num * old_min)

            # update overall best answer
            answer = max(answer, current_max)

        return answer