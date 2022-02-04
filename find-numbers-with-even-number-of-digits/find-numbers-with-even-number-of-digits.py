class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in range(len(nums)):
            if len(str(nums[num])) % 2 ==0:
                count=count+1
        return count