class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (''.join((i.lower()) for i in s if i.isalnum()))

        list = []
        for j in range(len(s)):
            if s[j] == s[len(s)-j-1]:
                list.append("true")
                continue
            else:
                list.append("false")
                break
        if "false" in list:
            return False
        else:
            return True