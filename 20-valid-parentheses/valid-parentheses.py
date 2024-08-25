class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
        "(" : ")", 
        "{" : "}",
        "[" : "]"
        }

        stack =[]

        for ch in s:
            if ch in brackets.keys():
                stack.append(ch)

            elif len(stack) == 0:
                return False

            elif brackets[stack.pop()] != ch:
                return False

        return len(stack) == 0
