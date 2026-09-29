class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1

        # Products of everything to the LEFT
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1

        # Multiply by everything to the RIGHT
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result