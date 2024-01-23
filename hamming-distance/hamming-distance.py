class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        mask = 1
        while xor != 0:
            if xor & mask != 0:
                distance += 1
            xor = xor >> 1
        return distance

