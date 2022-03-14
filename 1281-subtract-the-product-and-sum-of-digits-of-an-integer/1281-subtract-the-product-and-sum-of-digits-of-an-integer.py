class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_of = 0
        pro_of = 1
        res = [int(x) for x in str(n)]
        for val in res:
            sum_of+=val
            pro_of*=val
        diff = pro_of-sum_of
        return diff
            
        