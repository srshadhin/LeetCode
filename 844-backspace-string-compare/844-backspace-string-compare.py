class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_1 = []
        t_1 = []
        for i in s:
            if i == '#':
                if s_1 != []:
                    s_1.pop()
            else:
                s_1.append(i)
                
        for i in t:
            if i == '#':
                if t_1 != []:
                    t_1.pop()
            else:
                t_1.append(i)   
                
        return s_1 == t_1

        
        