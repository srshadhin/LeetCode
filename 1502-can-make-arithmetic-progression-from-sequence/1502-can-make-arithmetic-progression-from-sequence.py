class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)
        first_diff = sorted_arr[0] - sorted_arr[1]
        print(first_diff)
        for val in range(2, len(sorted_arr)):
            if first_diff != sorted_arr[val-1] - sorted_arr[val]:
                return False
        return True
                         