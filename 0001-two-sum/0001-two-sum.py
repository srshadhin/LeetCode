class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, val in enumerate(nums):
            rem = target - val

            if rem in seen:
                return[idx, seen[rem]]
            else:
                seen[val]=idx





            

        