class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_list = []
        sum_of = 0
        for num in nums:
            sum_of +=num
            sum_list.append(sum_of)
        return sum_list