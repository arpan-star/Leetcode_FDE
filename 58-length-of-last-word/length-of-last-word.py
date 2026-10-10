class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.strip()
        print(new)
        reverse_s = "".join(reversed(new))
        print(reverse_s)
        count = 0
        for i in reverse_s:
            if i == " ":
                break
            else:
                count+=1
        return count