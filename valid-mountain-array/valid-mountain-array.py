class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        first = 0;
        last = len(arr) - 1
        while first + 1 < len(arr) - 1 and arr[first] < arr[first + 1]: 
            first += 1
        while last - 1 > 0 and arr[last] < arr[last - 1]: 
            last -= 1
        return first == last