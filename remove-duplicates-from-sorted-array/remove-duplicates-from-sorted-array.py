class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in range(len(nums)-1,0,-1):
            if nums[num] == nums[num-1]:
                del nums[num]