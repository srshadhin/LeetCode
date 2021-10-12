from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = Counter(nums).values()
        for value in num:
            if value >= 2:
                return True
            else:
                return False
