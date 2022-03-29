class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        current = 0
        first_step = 1
        second_step = 2
        for i in range(2, n):
            current = first_step + second_step
            first_step = second_step
            second_step = current
        return current
        