class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        sum_of = 1  # 1 is always a proper divisor
        sqrt_num = int(num ** 0.5)
        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                sum_of += i
                if i != num // i:  # Exclude perfect squares
                    sum_of += num // i     
        return sum_of == num
    