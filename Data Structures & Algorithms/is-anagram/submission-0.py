class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countt={}

        for char in s:
            counts[char] = counts.get(char, 0) + 1


        for char in t: 
            countt[char] = countt.get(char, 0) + 1

        if counts == countt:
            return True
        return False