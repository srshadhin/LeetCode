import sys

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(1000000)
        st = int(''.join(map(str,num)))
        sum_of = st + k
        res = []

        for num in str(sum_of):
            res.append(int(num))
        return res