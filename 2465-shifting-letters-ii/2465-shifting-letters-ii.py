class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        delta = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                delta[start] += 1
                delta[end + 1] -= 1
            else:
                delta[start] -= 1
                delta[end + 1] += 1

        shift = 0
        net_shifts = []
        for i in range(n):
            shift += delta[i]
            net_shifts.append(shift)

        result = []
        for i in range(n):
            new_char = chr((ord(s[i]) - ord('a') + net_shifts[i]) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)
