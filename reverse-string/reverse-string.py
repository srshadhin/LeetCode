class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 1st Solution
        # i=0
        # while i < len(s):
        #     s.insert(i, s.pop())
        #     i+=1
        
        # #2nd Solution
        # for i in range(len(s)//2):
        #     s[i], s[-i-1] = s[-i-1], s[i]
        
        #3rd Solution
        f, l = 0, len(s)-1
        while f <l:
            s[f],  s[l] = s[l], s[f]
            f, l = f+1, l-1
        
        