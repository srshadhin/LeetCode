class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = defaultdict(int)

        for i in nums:
            res[i]+=1
            
            if res[i] == 3:
                res.pop(i)

        return list(res.keys())[0]