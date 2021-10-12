from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = Counter(nums).values()
        return [value for value in num if value >= 2]
