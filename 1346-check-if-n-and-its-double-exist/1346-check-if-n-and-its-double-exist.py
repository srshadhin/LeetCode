class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        check = set()
        for val in range(len(arr)):
            if arr[val] * 2 in check or arr[val] / 2 in check:
                return True
            check.add(arr[val])
        return False
        