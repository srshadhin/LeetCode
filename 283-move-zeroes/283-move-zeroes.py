class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for j in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        