class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        Dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        for a,b in zip(s,s[1:]):
            if Dict[a] < Dict[b]:
                result = result - Dict[a]
            else:
                result = result + Dict[a]
        return result + Dict[s[-1]]
