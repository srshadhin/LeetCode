class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = [str(integer) for integer in digits]
        a_string = "". join(strings)
        an_integer = int(a_string)+1
        return [int(val) for val in str(an_integer)]