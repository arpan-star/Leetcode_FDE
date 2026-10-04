class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        reverse_string_x = ""
        for i in string_x:
            reverse_string_x = i + reverse_string_x
        if reverse_string_x == string_x:
            return True
        else:
            return False
