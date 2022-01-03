"""
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
from collections import Counter


class Solution:
    def containsDuplicate(nums) -> bool:
        num = Counter(nums).values()
        return [value for value in num if value >= 2]


if __name__ == '__main__':
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    obj_of_sol = Solution.containsDuplicate(nums=nums)
    # print(obj_of_sol)
