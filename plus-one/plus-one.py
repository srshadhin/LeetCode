class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # strings = [str(integer) for integer in digits]
        # a_string = "". join(strings)
        # an_integer = int(a_string)+1
        # return [int(val) for val in str(an_integer)]
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1]+digits