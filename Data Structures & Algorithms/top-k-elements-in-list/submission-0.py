class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        # Count frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # frequency -> numbers
        freq = [[] for i in range(len(nums) + 1)]

        for num, frequency in count.items():
            freq[frequency].append(num)

        result = []

        # Start from highest frequency
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result