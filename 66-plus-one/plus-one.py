class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result1 = 0
        result2 = []
        for i in digits:
            result1 = result1 * 10 + i
        increment = result1 + 1
        temp = increment
        while temp > 0:
            result2.append(temp % 10)
            temp = temp // 10
        result2.reverse()
        return result2