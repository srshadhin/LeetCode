class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        checker = {}
        for key, value in enumerate(nums):
            if target - value in checker:
                return [checker[target - value], key]
            else:
                checker[value] = key
        return []