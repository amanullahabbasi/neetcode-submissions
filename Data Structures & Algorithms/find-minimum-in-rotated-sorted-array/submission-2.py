class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = nums[0]
        for n in nums:
            if n < smallest:
                smallest = n
        return smallest