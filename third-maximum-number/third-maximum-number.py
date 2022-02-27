class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_list = sorted(set(nums), reverse=True)
        x = len(sorted_list)
        if  x < 3:
            return max(sorted_list)
        else:
            return sorted_list[2]
        
        