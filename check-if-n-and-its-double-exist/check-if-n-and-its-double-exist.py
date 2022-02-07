class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for val in range(len(arr)):
            if arr[val]*2 in arr  and arr.index(arr[val]*2) !=val:
                return True
        return False
        