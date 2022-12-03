class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        opposite = {"}": "{", ")": "(", "]": "["}
        for c  in s:
            if c in "({[":
                stack.append(c)
            elif len(stack) and stack[-1] == opposite[c]:
                stack.pop()
            else:
                return False
        return len(stack) == 0