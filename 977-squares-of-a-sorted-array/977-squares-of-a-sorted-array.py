class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        numsList = []
        for num in nums:
            numsList.append(num**2)
        soretedList = sorted(numsList)
        return soretedList
        