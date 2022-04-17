class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        sum_of = 0
        for num in nums:
            if sum_of < 0:
                sum_of = 0
            sum_of = sum_of + num
            max_sub = max(max_sub, sum_of)
        return max_sub