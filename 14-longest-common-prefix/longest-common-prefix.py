class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = []
        strs.sort()
        
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first),len(last))):
            if first[i] == last[i]:
                result.append(first[i])
                continue
            else:
                break

        
        return "".join(result)
        
