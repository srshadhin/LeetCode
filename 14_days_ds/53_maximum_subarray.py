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


"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
