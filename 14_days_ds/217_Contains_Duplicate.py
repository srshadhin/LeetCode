"""
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = Counter(nums).values()
        return [value for value in num if value >= 2]
