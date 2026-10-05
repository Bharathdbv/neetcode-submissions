class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c not in bracket_map:
                stack.append(c)
            else:
                if len(stack)!=0:
                    x = stack.pop()
                    if x != bracket_map[c]:
                        return False
                else:
                    return False
        
        if len(stack) != 0:
            return False
        else:
            return True