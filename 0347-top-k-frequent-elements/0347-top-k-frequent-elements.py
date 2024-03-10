class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        bucket = [[] for i in range(len(nums)+1)]
        
        print(bucket)
        
        for num in nums:
            mp[num] = 1 + mp.get(num, 0)
        
        for i,c in mp.items():
            bucket[c].append(i)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
            