class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        # right_sum = 0
        for num in range(len(nums)):
            right_sum = total_sum - left_sum-nums[num]     
            if left_sum == right_sum:
                return num
            left_sum +=nums[num]
        return -1
