class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack: 
                    return False
                par = stack.pop()
                if par == '(' and char != ')':
                    return False
                if par == '{' and char != '}':
                    return False
                if par == '[' and char != ']':
                    return False
        if stack:
            return False
        return True
                