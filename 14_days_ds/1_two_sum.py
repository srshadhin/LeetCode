from typing import List


class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        checker = {}
        for key, value in enumerate(nums):
            if target - value in checker:
                return [checker[target - value], key]
            else:
                checker[value] = key
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    obj_of_solution = Solution()
    get_output = obj_of_solution.twoSum(nums, target)
    expected_result = [0, 1]
    assert expected_result == get_output, expected_result
    print(get_output)

    nums = [3, 2, 4]
    target = 6
    obj_of_solution = Solution()
    get_output = obj_of_solution.twoSum(nums, target)
    expected_result = [1, 2]
    assert expected_result == get_output, expected_result
    print(get_output)
