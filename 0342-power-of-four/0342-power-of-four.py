class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1: 
            return True
        power=4
        while power<=n:
            if power==n: 
                return True
            power*=4
        return False