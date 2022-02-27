class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_list = sorted(heights)
        counter = 0
        # Solution 1
        # for i in range(len(heights)):
        #     if heights[i] != sorted_list[i]:
        #         counter+=1
        # return counter
        for x, y in zip(heights, sorted_list):
            if x != y:
                counter +=1
        return counter