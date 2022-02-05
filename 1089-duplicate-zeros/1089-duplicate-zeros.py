class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # newArr = []
        # for val in arr:
        #     newArr.append(val)
        #     if val == 0:
        #         newArr.append(val)
        # while len(arr) != len(newArr):
        #     newArr.pop()
        # return newArr
        val = 0
        while(val < len(arr)):
            if arr[val] == 0:
                arr.pop()
                arr.insert(val,0)
                val+=1
            val+=1

                