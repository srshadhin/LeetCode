class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for num in range(len(nums)):
            print(num)
            if nums[num] == target:
                return num
        return -1
        