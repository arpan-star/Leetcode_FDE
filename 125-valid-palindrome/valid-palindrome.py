class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.lower()
        s_list = []
        for i in t:
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                s_list.append(i)
        print(s_list)

        for i in range(len(s_list)):
            if s_list[i] == s_list[len(s_list) - i - 1]:
                continue
            else:
                return False
                break
        return True