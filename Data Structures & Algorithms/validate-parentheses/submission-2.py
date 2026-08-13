class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack, LIFO
        stack = []
        HashMap = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for bracket in s:
            if bracket in HashMap:
                if not stack:
                    return False
                #closed bracket
                top = stack.pop()
                if HashMap[bracket] != top:
                    return False
            else:
                stack.append(bracket)
                #opening bracket
        if stack:
            return False
        else:
            return True