class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        num_sqrt = num ** 0.5

        if num_sqrt.is_integer():
            return True
        else:
            return False
    