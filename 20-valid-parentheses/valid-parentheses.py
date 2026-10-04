class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")":
                if stack == []:
                    return False
                elif stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif i == "]":
                if stack == []:
                    return False
                elif stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif i == "}":
                if stack == []:
                    return False
                elif stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False